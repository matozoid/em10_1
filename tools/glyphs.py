#!/usr/bin/env python3
"""Decode block-1 per-language font entries (res1 e035..e068) to ASCII art.
Glyph record: u8 rows-1, u16 (w-1)<<4|lo, u8 b3 (=9 in samples), then `rows` rows of
2-bit RLE bytes (level<<6 | run-1) until row width w is reached. Glyph data starts at
file offset 0x5c; a {u32 ptr,u16 w,u16 h} index table follows the glyph run (not decoded).
usage: glyphs.py entry.bin [first [count]]   (vendor font data: keep output local)"""
import sys

def dec(d, o):
    if o + 4 > len(d): return None
    h = d[o] + 1; v = d[o+1] | d[o+2] << 8; w = (v >> 4) + 1; p = o + 4
    rows = []
    try:
        for _ in range(h):
            row = []
            while len(row) < w:
                c = d[p]; p += 1; row += [c >> 6] * ((c & 63) + 1)
            if len(row) != w: return None
            rows.append(row)
    except IndexError:
        return None
    return w, h, rows, p

def glyphs(d, start=0x5c):
    o, out = start, []
    while (r := dec(d, o)) and r[1] > 1:
        out.append((o, r[0], r[1], r[2])); o = r[3]
    return out

if __name__ == '__main__':
    d = open(sys.argv[1], 'rb').read()
    g = glyphs(d); a = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    n = int(sys.argv[3]) if len(sys.argv) > 3 else len(g)
    print(len(g), 'glyphs')
    for i, (o, w, h, rows) in enumerate(g[a:a+n], a):
        print(f'#{i} @0x{o:x} {w}x{h}')
        for r in rows: print(''.join(' .oO'[x] for x in r))
