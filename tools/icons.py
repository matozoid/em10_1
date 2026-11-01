#!/usr/bin/env python3
"""Decode OSD icon bank (block 1 entry 0 / 69) into paged PNG contact sheets.

usage: tools/icons.py entry.bin base_hex out_prefix [--fmt 2|3] [--page-height N]
Writes out_prefix_NN.png. Layout (reverse engineered, see docs/firmware/resources.md):
  record     = [4B hdr][payload][0-3B pad][24B descriptor]
  descriptor = <6HIII {u16 14, u16 width, u16 adv, u16 kind(4|8), 0, 0, u32 size, u32 ptr, u32 0}
               record start = ptr - base - 0x20; size covers hdr + payload
  hdr        = H-1 (12 bit) | W-1 (12 bit) << 12, then u8 format
  format 2   = byte RLE: colour<<4 | (run-1), runs continue across rows (4-bit colour, kind 4)
  format 3   = LSB-first bitstream of 64-bit words; token = 2-bit (run-1) + 8-bit CLUT index;
               a token never straddles a 64-bit word (skip to next word); runs stop at row end
               (8-bit index, kind 8)
  format 9   = font glyph (tools/glyphs.py)
Palettes: block 0 ROM table at file offset PALTAB (runtime .data copy at 0x6045e020), 58 entries indexed by
palette ID, each -> {u32 count=256, u32 ptr} -> 256 x ARGB8888. SetPalette(mode) loads ID k into the 256-colour
layer (fmt 3), k-1 into the 16-colour layer (fmt 2), k-2 into the 8-colour layer. --pal K (fmt 3, default 3),
--pal16 K (fmt 2, default 8), --override off=K,... per record; OVERRIDES holds user-judged picks.
Output is vendor data: keep local."""
import struct, sys
from PIL import Image, ImageDraw


def records(d, base):
    for off in range(0, len(d) - 24, 2):
        a, w, adv, kind, z1, z2, size, ptr, z = struct.unpack_from('<6HIII', d, off)
        if not (base <= ptr < base + len(d) and z == z1 == z2 == 0 and 4 <= w <= 800 and kind in (4, 8)):
            continue
        o = ptr - base - 0x20
        if o < 0 or not 0 <= off - (o + size) <= 3:
            continue
        b = d[o:o + size]
        H = (b[0] | (b[1] & 15) << 8) + 1
        W = ((b[1] | b[2] << 8) >> 4) + 1
        yield dict(off=off, o=o, W=W, H=H, fmt=b[3], kind=kind, adv=adv, p=b[4:])


IDTAB_OFF, IDTAB_N = 0x3b1e48, 3525  # in block 1 entry 0: image ID -> RAM addr of record start + 8


def id_records(d, base, e0):
    """Records of this bank reachable via the image-ID table (catches wide images the descriptor scan skips).
    Size is unknown here, so the payload slice is the worst case; decoders stop at W*H."""
    for i, t in enumerate(struct.unpack_from('<%dI' % IDTAB_N, e0, IDTAB_OFF)):
        o = t - 8 - base
        if not 0 <= o < len(d) - 4:
            continue
        h = d[o:o + 4]
        H = (h[0] | (h[1] & 15) << 8) + 1
        W = ((h[1] | h[2] << 8) >> 4) + 1
        if h[3] in (2, 3):
            yield dict(off=None, o=o, W=W, H=H, fmt=h[3], kind=None, adv=None, id=i,
                       p=d[o + 4:o + 4 + (W * H if h[3] == 2 else W * H * 4 // 3 + 16)])  # fmt 3 worst case: 6 tokens per 64-bit word


def dec2(p, W, H):
    px = []; T = W * H
    for b in p:
        px += [b >> 4] * ((b & 15) + 1)
        if len(px) >= T:
            return px if len(px) == T else None
    return None


def dec3(p, W, H):
    v = int.from_bytes(p, 'little'); n = len(p) * 8; pos = 0; px = []
    for _ in range(H):
        x = 0
        while x < W:
            if pos >> 6 != (pos + 9) >> 6:
                pos = ((pos >> 6) + 1) << 6
            if pos + 10 > n:
                return None
            c = ((v >> pos) & 3) + 1; val = (v >> (pos + 2)) & 255; pos += 10
            px += [val] * c; x += c
        if x != W:
            return None
    return px


PALTAB = 0x382ec0
BLK0_BASE = 0x7d991020


OVERRIDES = {0xbf06a000: {0xdc00: 6}}  # bank base -> {record offset: palette ID}


def load_palette(blk0, pid):
    p = struct.unpack_from('<I', blk0, PALTAB + 4 * pid)[0]
    n, dp = struct.unpack_from('<2I', blk0, p - BLK0_BASE)
    return list(struct.unpack_from('<%dI' % n, blk0, dp - BLK0_BASE))


def blend(argb, bg):
    a = argb >> 24
    return tuple((((argb >> s) & 255) * a + c * (255 - a)) // 255 for s, c in zip((16, 8, 0), bg))


def main():
    a = sys.argv
    d = open(a[1], 'rb').read(); base = int(a[2], 16); out = a[3]
    fmts = {int(a[a.index('--fmt') + 1])} if '--fmt' in a else {2, 3}
    blk0 = open(a[a.index('--blk0') + 1] if '--blk0' in a else 'firmware/stock/dec/blk00_40300000.bin', 'rb').read()
    # Palette per screen; no single one fits all icons. User-judged defaults (2026-11-01):
    # ID 3 for format 3 in general, ID 6 for the exposure-compensation scale.
    pid = int(a[a.index('--pal') + 1], 0) if '--pal' in a else 3
    pid16 = int(a[a.index('--pal16') + 1], 0) if '--pal16' in a else 8
    over = dict(OVERRIDES.get(base, {}))
    if '--override' in a:  # e.g. --override dc00=6,399a0=3 (record offsets, hex)
        for kv in a[a.index('--override') + 1].split(','):
            k, v = kv.split('='); over[int(k, 16)] = int(v, 0)
    cache = {}
    def pal_for(r):
        p = pid16 if r['fmt'] == 2 else over.get(r['o'], pid)
        if p not in cache:
            cache[p] = load_palette(blk0, p)
        return cache[p]
    PH = int(a[a.index('--page-height') + 1]) if '--page-height' in a else 4000
    items = []
    e0 = open(a[a.index('--e0') + 1] if '--e0' in a else 'firmware/stock/res1/e000_41500800_3d8800.bin', 'rb').read()
    rs = list(records(d, base)); seen = {r['o'] for r in rs}
    rs += [r for r in id_records(d, base, e0) if r['o'] not in seen]
    rs.sort(key=lambda r: r['o'])
    for r in rs:
        if r['fmt'] not in fmts:
            continue
        px = (dec2 if r['fmt'] == 2 else dec3)(r['p'], r['W'], r['H'])
        if px is None:
            print('decode fail', hex(r['o']), r['W'], r['H'], r['fmt']); continue
        items.append((r, px))
    print(len(items), 'images')
    PW = 1800; pages = [[]]; x = y = rowh = 0
    for r, px in items:
        S = 3 if max(r['W'], r['H']) <= 60 else 2 if max(r['W'], r['H']) <= 200 else 1
        tw, th = max(r['W'] * S, 48) + 6, r['H'] * S + 14
        if x + tw > PW:
            x = 0; y += rowh; rowh = 0
        if y + th > PH and pages[-1]:
            pages.append([]); x = y = rowh = 0
        pages[-1].append((r, px, S, x, y)); x += tw; rowh = max(rowh, th)
    for n, pg in enumerate(pages):
        hgt = max(y + r['H'] * S + 14 for r, px, S, x, y in pg) + 4
        img = Image.new('RGB', (PW, hgt), (40, 40, 40)); dr = ImageDraw.Draw(img)
        for r, px, S, x, y in pg:
            pal = pal_for(r)
            dr.text((x, y), '%x' % r['o'], fill=(255, 200, 0))
            tile = Image.new('RGB', (r['W'], r['H']))
            tile.putdata([blend(pal[v], (90, 90, 90) if ((i % r['W']) // 4 + (i // r['W']) // 4) % 2 else (60, 60, 60))
                          for i, v in enumerate(px)])
            img.paste(tile.resize((r['W'] * S, r['H'] * S), Image.NEAREST), (x, y + 12))
        img.save('%s_%02d.png' % (out, n))
    print(len(pages), 'pages')


if __name__ == '__main__':
    main()
