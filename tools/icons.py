#!/usr/bin/env python3
"""Decode OSD icon bank (block 1 entry 0 / 69) into a PNG contact sheet.

usage: tools/icons.py entry.bin base_hex out.png [--all]
Record layout (reverse engineered, see docs/firmware/resources.md):
  [4B hdr][RLE pixels: byte = colour<<4 | (run-1), continuous across rows][0-3B pad][24B descriptor]
  descriptor {u16 h?, u16 width, u16 adv, u16 kind(4|8), u16 0, u16 0, u32 size, u32 ptr, u32 0}
  ptr = RAM addr of record start + 0x20; size covers hdr + pixels.
Output is derived from vendor data: keep local (gitignored)."""
import struct, sys
from PIL import Image, ImageDraw

PAL = {0: (16, 24, 64), 1: (120, 150, 200), 2: (160, 180, 220), 3: (200, 215, 240), 4: (255, 255, 255)}

def records(d, base):
    for off in range(0, len(d) - 24, 2):
        h, w, adv, kind, z1, z2, size, ptr, z = struct.unpack_from('<6HIII', d, off)
        if not (base <= ptr < base + len(d) and z == 0 and z1 == 0 and z2 == 0 and 4 <= w <= 800 and kind in (4, 8)):
            continue
        o = ptr - base - 0x20
        if o < 0 or not 0 <= off - (o + size) <= 3:
            continue
        px = []
        for b in d[o + 4:o + size]:
            px += [b >> 4] * ((b & 15) + 1)
        yield off, w, h, d[o:o + 4].hex(), px

def main():
    d = open(sys.argv[1], 'rb').read(); base = int(sys.argv[2], 16); out = sys.argv[3]
    allr = '--all' in sys.argv
    items = [r for r in records(d, base) if allr or len(r[4]) % r[1] == 0]
    print(len(items), 'images')
    S = 3; cw = 120; x = y = rowh = 0; W = 1600
    tiles = []
    for off, w, h, hdr, px in items:
        rows = max(1, len(px) // w)
        if w * S > 700: continue
        tiles.append((off, w, rows, px))
    H = 20
    # pack
    pos = []; x = y = rowh = 0
    for off, w, rows, px in tiles:
        tw, th = w * S + 6, rows * S + 14
        if x + tw > W: x = 0; y += rowh; rowh = 0
        pos.append((x, y)); x += tw; rowh = max(rowh, th)
    img = Image.new('RGB', (W, y + rowh + 4), (40, 40, 40))
    dr = ImageDraw.Draw(img)
    for (off, w, rows, px), (x, y) in zip(tiles, pos):
        dr.text((x, y), '%x' % off, fill=(255, 200, 0))
        for i, v in enumerate(px[:w * rows]):
            c = PAL.get(v, (255, 0, 255))
            xx = x + (i % w) * S; yy = y + 12 + (i // w) * S
            dr.rectangle([xx, yy, xx + S - 1, yy + S - 1], fill=c)
    img.save(out)

if __name__ == '__main__':
    main()
