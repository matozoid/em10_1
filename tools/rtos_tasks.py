#!/usr/bin/env python3
"""Dump the RTOS task id/name table from decoded block 0 (firmware/stock/dec/blk00_*.bin).
Records: u16 id + 24-byte NUL-padded name (stride 26). Anchor: the FIRMUP_CLI record.
usage: rtos_tasks.py blk00.bin [load_addr=0x40300000]"""
import sys
b = open(sys.argv[1], 'rb').read()
load = int(sys.argv[2], 0) if len(sys.argv) > 2 else 0x40300000
def rec(o):
    n = b[o+2:o+26]; s = n.split(b'\0')[0]
    ok = s.isascii() and s and all(32 <= c < 127 for c in s) and not any(n[len(s):])
    return int.from_bytes(b[o:o+2], 'little'), s.decode() if ok else '', bool(ok)
o = b.find(b'FIRMUP_CLI') - 2
while rec(o-26)[2]: o -= 26
print(f"# table at {load+o:#x}")
while rec(o)[2]:
    i, s, _ = rec(o); print(f"{i:#04x} {s}"); o += 26
