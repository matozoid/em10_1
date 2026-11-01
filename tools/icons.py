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
Palette (CLUT) is not yet located: colours are false. Output is vendor data: keep local."""
import colorsys, struct, sys
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


def dec2(p, W, H):
    px = []
    for b in p:
        px += [b >> 4] * ((b & 15) + 1)
    return px[:W * H] if len(px) >= W * H else None


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


def palette(fmt):
    if fmt == 2:
        return {0: None, 1: (120, 150, 200), 2: (160, 180, 220), 3: (200, 215, 240), 4: (255, 255, 255),
                **{i: (90 + 10 * i, 90, 90) for i in range(5, 16)}}
    pal = {0: None}
    for i in range(1, 256):  # false colour: golden-ratio hue walk, brightness by index
        r, g, b = colorsys.hsv_to_rgb((i * 0.618) % 1, 0.55, 0.55 + 0.45 * ((i * 7) % 16) / 15)
        pal[i] = (int(r * 255), int(g * 255), int(b * 255))
    return pal


def main():
    a = sys.argv
    d = open(a[1], 'rb').read(); base = int(a[2], 16); out = a[3]
    fmts = {int(a[a.index('--fmt') + 1])} if '--fmt' in a else {2, 3}
    PH = int(a[a.index('--page-height') + 1]) if '--page-height' in a else 4000
    items = []
    for r in records(d, base):
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
            pal = palette(r['fmt'])
            dr.text((x, y), '%x' % r['o'], fill=(255, 200, 0))
            tile = Image.new('RGB', (r['W'], r['H']))
            tile.putdata([pal.get(v) or ((70, 70, 70) if ((i % r['W']) // 4 + (i // r['W']) // 4) % 2 else (55, 55, 55))
                          for i, v in enumerate(px)])
            img.paste(tile.resize((r['W'] * S, r['H'] * S), Image.NEAREST), (x, y + 12))
        img.save('%s_%02d.png' % (out, n))
    print(len(pages), 'pages')


if __name__ == '__main__':
    main()
