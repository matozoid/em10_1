#!/usr/bin/env python3
# Verify live USB DeviceInfo findings against the decrypted firmware block 0.
# Runtime base: file offset 0 == runtime 0x7d991020.  offset = addr - 0x7d991020.
import os, struct, sys
BLK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "firmware", "stock", "dec", "blk00_40300000.bin")
RT = 0x7d991020
b = open(BLK, "rb").read()
def off(a): return a - RT
def u16s(addr, n): return list(struct.unpack_from("<%dH" % n, b, off(addr)))
def hx(a): return " ".join(f"{x:#06x}" for x in a)

print("== per-mode OperationsSupported arrays (static) ==")
modes = {0x7e890e16:("mode0/5",29), 0x7e890e78:("mode1",18), 0x7e890e9c:("mode2/3",11),
         0x7e890e50:("mode4",20), 0x7e890eb2:("mode6",33)}
for addr,(name,n) in sorted(modes.items()):
    print(f"{addr:#010x} {name:8} ({n}): {hx(u16s(addr,n))}")

LIVE = [0x1001,0x1002,0x1003,0x1004,0x1005,0x1006,0x1007,0x1008,0x1009,0x100a,0x100b,
        0x100f,0x1014,0x1015,0x1016,0x101b,0x9801,0x9802,0x9803,0x9805]
static_m4 = u16s(0x7e890e50,20)
print("\n== LIVE MTP ops vs static mode4 (0x7e890e50) ==")
print("live  :", hx(LIVE))
print("static:", hx(static_m4))
print("MATCH :", static_m4 == LIVE)

# Search whole block for the 0x94xx OMD unlock opcodes (little-endian u16) to confirm absence
print("\n== search block 0 for OMD unlock opcodes 0x9481 / 0x9482 ==")
for oc in (0x9481, 0x9482):
    pat = struct.pack("<H", oc)
    hits = []
    i = b.find(pat)
    while i != -1 and len(hits) < 12:
        hits.append(i); i = b.find(pat, i+1)
    print(f"{oc:#06x}: {len(hits)}{'+' if len(hits)>=12 else ''} raw byte-pair hits"
          f" (runtime addrs: {', '.join(f'{RT+h:#010x}' for h in hits[:6])})")

# Confirm none of the per-mode op arrays contains 0x9481/0x9482
print("\n== 0x9481/0x9482 present in any per-mode ops array? ==")
allops = set()
for addr,(name,n) in modes.items(): allops |= set(u16s(addr,n))
for oc in (0x9481,0x9482): print(f"{oc:#06x} in advertised ops: {oc in allops}")
print("union of all advertised vendor ops (>=0x9000):",
      hx(sorted(x for x in allops if x>=0x9000)))
