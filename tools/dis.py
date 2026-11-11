#!/usr/bin/env python3 -I
"""Annotated MN10300 disassembly of decoded block 0, at runtime addresses.

Wraps mn10300-elf-objdump (GNU binutils built with --target=mn10300-elf, on PATH). objdump prints
32-bit immediates in decimal; this adds each one in hex and, when it points at a printable string
inside the block, the string itself.

usage:
  dis.py START END [--blk FILE]     START/END = runtime addresses, hex (0x optional)
  dis.py 7de57e24 7de58a90

Runtime base is 0x7d991020 (file offset 0 of blk00). Default FILE = firmware/stock/dec/blk00_40300000.bin.
"""
import os, re, shutil, subprocess, sys

RT = 0x7d991020
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_BLK = os.path.join(HERE, "..", "firmware", "stock", "dec", "blk00_40300000.bin")
OBJDUMP = "mn10300-elf-objdump"

def string_at(b, v):
    o = v - RT
    if not 0 <= o < len(b) - 4:
        return None
    m = re.match(rb"[\x20-\x7e]{4,}", b[o:o + 80])
    return m.group().decode() if m else None

def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    blk = argv[argv.index("--blk") + 1] if "--blk" in argv else DEFAULT_BLK
    if "--blk" in argv:
        args.remove(blk)
    if len(args) != 2:
        sys.exit(__doc__)
    start, end = (int(a, 16) for a in args)
    od = shutil.which(OBJDUMP)
    if not od:
        sys.exit(OBJDUMP + " not found on PATH (build binutils with --target=mn10300-elf)")
    b = open(blk, "rb").read()
    out = subprocess.run(
        [od, "-D", "-b", "binary", "-m", "am33-2", "--adjust-vma=%#x" % RT,
         "--start-address=%#x" % start, "--stop-address=%#x" % end, blk],
        capture_output=True, text=True, check=True).stdout
    for line in out.splitlines():
        m = re.match(r"\s*([0-9a-f]+):\s+((?:[0-9a-f]{2} )+)\s*(.*)", line)
        if not m:
            continue
        addr, ins = m.group(1), m.group(3).strip()
        if not ins:            # continuation row of a long instruction's bytes
            continue
        note = ""
        for n in re.findall(r"(?<![\w])(-?\d{6,}|0x[0-9a-f]{6,})", ins):
            v = int(n, 0) & 0xffffffff
            s = string_at(b, v)
            note += "  ; %#x" % v + (' "%s"' % s if s else "")
        print("%s: %-40s%s" % (addr, ins.replace("\t", " "), note))

if __name__ == "__main__":
    main(sys.argv[1:])
