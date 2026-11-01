#!/usr/bin/env python3
"""Split a decoded block 1/2 into directory entries. usage: resdump.py blk.bin load_addr outdir
Directory: 16-byte records {u32 addr, u32 size, 0, 0} from offset 0 until a zero record; entry data at addr-load."""
import struct, sys, os
b = open(sys.argv[1], 'rb').read(); load = int(sys.argv[2], 0); out = sys.argv[3]
os.makedirs(out, exist_ok=True)
i = 0
while True:
    a, s, x, y = struct.unpack_from('<IIII', b, i * 16)
    if a == 0 and s == 0: break
    o = a - load
    open(f"{out}/e{i:03d}_{a:08x}_{s:x}.bin", 'wb').write(b[o:o + s])
    print(i, hex(a), hex(s), b[o:o + 16].hex())
    i += 1
