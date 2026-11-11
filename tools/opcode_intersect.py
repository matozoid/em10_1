#!/usr/bin/env python3 -I
"""Intersect the OM Workspace SDK PTP opcode catalog with the opcodes the E-M10 Mark I implements.
Result is discussed in docs/usb-protocol/sdk-opcode-compat.md.
usage: opcode_intersect.py docs/usb-protocol/olympus-opcode-table.csv"""
import csv,sys
csvpath=sys.argv[1]
codes=set()
with open(csvpath) as f:
    r=csv.DictReader(f)
    for row in r:
        try: codes.add(int(row['ptp_code'],16))
        except: pass
def rng(a,b): return set(range(a,b+1))
# Mk I USB-advertised vendor (union all modes)
adv = {0x902c,0x902d,0x902e,0x902f,0x9116,0x9117,0x9119,0x911c,0x9120,0x9121,0x9122,0x9123,0x9124,0x9125,0x9801,0x9802,0x9803,0x9805}
# Mk I internal camera-control engine set (0x7e5bxxxx region)
eng = rng(0x9004,0x901d)|{0x9031,0x9032}|rng(0x9034,0x9037)|{0x903e}|rng(0x9040,0x9042)|rng(0x9046,0x904b)|rng(0x904f,0x9051)|rng(0x9200,0x9208)
mk1 = adv|eng
print("CSV opcodes total:",len(codes))
print("CSV range: 0x%04x..0x%04x"%(min(codes),max(codes)))
inter_adv=sorted(codes&adv); inter_eng=sorted(codes&eng)
print("\nCSV ∩ Mk I USB-advertised (%d):"%len(inter_adv), " ".join("0x%04x"%c for c in inter_adv))
print("\nCSV ∩ Mk I internal-engine (%d):"%len(inter_eng), " ".join("0x%04x"%c for c in inter_eng))
# CSV codes that are 0x94xx (OMD-only, NOT on Mk I)
omd=sorted(c for c in codes if 0x9480<=c<=0x94ff)
print("\nCSV 0x94xx OMD-only codes (Mk I lacks all): %d codes, 0x%04x..0x%04x"%(len(omd),min(omd),max(omd)))
# engine ops the camera has but CSV/SDK does NOT list
print("\nMk I engine ops NOT in CSV (%d):"%len(sorted(eng-codes))," ".join("0x%04x"%c for c in sorted(eng-codes)))
