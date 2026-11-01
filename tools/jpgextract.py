#!/usr/bin/env python3
"""Carve JPEG streams (FFD8FF ... FFD9) out of a resdump entry.
usage: jpgextract.py entry.bin outdir   (output is vendor content: keep local)"""
import sys, os, struct
d = open(sys.argv[1], 'rb').read(); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
pos = n = 0
while True:
    s = d.find(b'\xff\xd8\xff', pos)
    if s < 0: break
    # walk markers to find real EOI
    i = s + 2; e = -1
    while i + 4 <= len(d):
        if d[i] != 0xff: break
        m = d[i+1]
        if m == 0xda:  # SOS: scan entropy data to EOI
            j = i + 2 + struct.unpack('>H', d[i+2:i+4])[0]
            while j + 1 < len(d):
                if d[j] == 0xff and d[j+1] not in (0, 0xff) and not (0xd0 <= d[j+1] <= 0xd7):
                    break
                j += 1
            e = j + 2 if j + 1 < len(d) and d[j+1] == 0xd9 else -1
            break
        i += 2 + struct.unpack('>H', d[i+2:i+4])[0]
    if e < 0: pos = s + 3; continue
    open(f"{out}/{n:03d}_{s:06x}.jpg", 'wb').write(d[s:e]); n += 1; pos = e
print(n, "jpegs")
