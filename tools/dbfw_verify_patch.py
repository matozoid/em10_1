#!/usr/bin/env python3 -I
"""Check the community em10-1.4 ring-native patches against decoded stock block 0 (old bytes match,
payload cave is 0xFF fill). Superseded for general use by `fwpatch.py plan`; kept as the original
independent check. Profile JSON is third-party data: keep it local.
usage: dbfw_verify_patch.py PROFILES.json blk00_40300000.bin"""
import json, base64, sys
prof = json.load(open(sys.argv[1],"rb"))
blk0 = open(sys.argv[2],"rb").read()
p=[x for x in prof if (x.get("id") or x.get("body"))=="em10-1.4"][0]
ft=[f for f in p["features"] if f["id"]=="ring-native"][0]
print(f"block0 len={len(blk0)} (0x{len(blk0):x})")
for pt in ft["patches"]:
    if pt.get("block")!=0: 
        print("non-block0 patch:",pt.get("label")); continue
    off=pt["offset"]; old=base64.b64decode(pt["old"]); new=base64.b64decode(pt["new"])
    actual=blk0[off:off+len(old)]
    ok = actual==old
    tag=pt["label"]
    if tag=="payload_cave":
        ff = old.count(0xff); print(f"{tag:14} off=0x{off:x} len={len(old)} old_is_0xFF_fill={ff==len(old)} ({ff}/{len(old)}) match_stock={ok}")
    else:
        print(f"{tag:14} off=0x{off:x} len={len(old)} match_stock={ok}  old={old.hex()} new={new.hex()}")
