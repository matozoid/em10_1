#!/usr/bin/env python3 -I
"""Resolve the firmware's API trace ids to names (docs/firmware/trace-catalog.md).

usage:
  trace_catalog.py list            print every  id <TAB> name
  trace_catalog.py ID [ID...]      resolve ids given in hex, e.g. 0x10c16

The lookup function 0x7dfc7272 walks three pointer tables that live in RAM from 0x6044e518. RAM is filled
at start-up from an image inside block 0; image address = RAM address + DELTA. Needs
firmware/stock/dec/blk00_40300000.bin.
"""
import os, struct, sys

RT = 0x7d991020
DELTA = 0x7dd03018 - 0x6044d158
TOP = 0x6044e518
BLK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "firmware", "stock", "dec", "blk00_40300000.bin")


class Catalog:
    def __init__(self, path=BLK):
        self.b = open(path, "rb").read()

    def u(self, ram):
        return struct.unpack_from("<I", self.b, ram + DELTA - RT)[0]

    def text(self, addr):
        o = addr - RT
        return self.b[o:o + 120].split(b"\0")[0].decode("latin1").strip()

    @staticmethod
    def ram(v):
        return 0x60440000 <= v < 0x60460000

    def name(self, ident):
        cat, group, item = (ident >> 16) & 255, (ident >> 8) & 255, ident & 255
        if ident >> 24 or not (cat and group and item):
            return None
        a = self.u(TOP + 4 * (cat - 1))
        if not self.ram(a):
            return None
        a = self.u(a + 4 * (group - 1))
        if not self.ram(a):
            return None
        p = self.u(a + 4 * (item - 1))
        return self.text(p) if RT <= p < RT + len(self.b) else None

    def entries(self):
        tops = [self.u(TOP + 4 * k) for k in range(8)]
        gtabs = tops[:next(k for k, v in enumerate(tops) if not self.ram(v))]
        bounds = sorted(set(gtabs + [TOP]))
        end = lambda start, marks: min([m for m in marks if m > start] or [start])
        groups = {c: [self.u(g + 4 * k) for k in range((end(g, bounds) - g) // 4)] for c, g in enumerate(gtabs, 1)}
        marks = sorted(set(v for vs in groups.values() for v in vs if self.ram(v)) | set(bounds))
        for c, tables in groups.items():
            for g, t in enumerate(tables, 1):
                if self.ram(t):
                    for i in range(1, (end(t, marks) - t) // 4 + 1):
                        n = self.name((c << 16) | (g << 8) | i)
                        if n is not None:
                            yield (c << 16) | (g << 8) | i, n


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cat = Catalog()
    if sys.argv[1] == "list":
        for ident, name in cat.entries():
            print("0x%05x\t%s" % (ident, name))
    else:
        for arg in sys.argv[1:]:
            print("%s\t%s" % (arg, cat.name(int(arg, 16))))
