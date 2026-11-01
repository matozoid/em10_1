#!/usr/bin/env python3
"""Dump a block-1 UTF-16LE string table (res1 entries 1..34) to TSV: index<TAB>string.
usage: strtab.py e001_*.bin > out.tsv   (output is vendor text: keep local, gitignored)"""
import sys
d = open(sys.argv[1], 'rb').read()
s = d.decode('utf-16le', 'ignore').split('\0')
for i, x in enumerate(s):
    if x:
        print(f"{i}\t{x}")
