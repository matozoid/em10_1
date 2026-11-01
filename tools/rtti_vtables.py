#!/usr/bin/env python3
# Resolve MSVC x64 RTTI: for each ".?AV...@@" type-descriptor name, find its
# vtable(s) and the methods at each slot. Static read of the PE, no execution.
import struct, sys, re
PE = sys.argv[1]
b = open(PE, "rb").read()

# --- PE section table: map RVA<->file offset ---
pe_off = struct.unpack_from("<I", b, 0x3c)[0]
assert b[pe_off:pe_off+4] == b"PE\0\0"
nsec = struct.unpack_from("<H", b, pe_off+6)[0]
opt_sz = struct.unpack_from("<H", b, pe_off+20)[0]
image_base = struct.unpack_from("<Q", b, pe_off+24+24)[0]  # opt hdr ImageBase (PE32+)
sec_off = pe_off + 24 + opt_sz
secs = []
for i in range(nsec):
    o = sec_off + i*40
    name = b[o:o+8].rstrip(b"\0").decode("latin1")
    vsz, vaddr, rawsz, rawptr = struct.unpack_from("<IIII", b, o+8)
    secs.append((name, vaddr, vsz, rawptr, rawsz))

def rva2off(rva):
    for name, va, vsz, rp, rs in secs:
        if va <= rva < va + max(vsz, rs):
            return rp + (rva - va)
    return None
def off2rva(off):
    for name, va, vsz, rp, rs in secs:
        if rp <= off < rp + rs:
            return va + (off - rp)
    return None

# --- find all type descriptor names ".?AV...@@" / ".?AU...@@" ---
tds = {}  # name -> td_rva (start of TypeDescriptor struct = name_off - 0x10)
for m in re.finditer(rb"\.\?A[UV][\w@?$]+@@", b):
    name_off = m.start()
    td_off = name_off - 0x10
    tds[off2rva(td_off)] = m.group().decode("latin1")

want = [n for n in sys.argv[2:]] if len(sys.argv) > 2 else None

# --- scan .rdata for Complete Object Locators: signature,0,0,pTypeDesc(RVA),... ---
# x64 COL layout: u32 signature(1); u32 offset; u32 cdOffset; u32 pTypeDescriptor(RVA);
#                 u32 pClassDescriptor(RVA); u32 pSelf(RVA of the COL itself)
for name, va, vsz, rp, rs in secs:
    if name != ".rdata":
        continue
    data = b[rp:rp+rs]
    for i in range(0, len(data)-24, 4):
        sig, offv, cd, ptd = struct.unpack_from("<IIII", data, i)
        if sig != 1:
            continue
        if ptd not in tds:
            continue
        cname = tds[ptd]
        if want and not any(w in cname for w in want):
            continue
        col_rva = va + i
        # vtable: an 8-byte pointer to col_rva exists at vptr-8; vtable starts at +8
        col_ptr = image_base + col_rva
        needle = struct.pack("<Q", col_ptr)
        j = b.find(needle)
        while j != -1:
            if off2rva(j) is not None:
                vt_rva = off2rva(j) + 8
                # read up to 12 slots
                slots = []
                vo = rva2off(vt_rva)
                for s in range(12):
                    p = struct.unpack_from("<Q", b, vo + s*8)[0]
                    if p < image_base or p >= image_base + 0x200000:
                        break
                    slots.append(p - image_base + 0x180000000 - image_base + image_base)
                    slots[-1] = p  # keep absolute runtime
                print(f"{cname:34} COL@{image_base+col_rva:#012x} vtable@{image_base+vt_rva:#012x} "
                      f"slots={len(slots)}: " + " ".join(f"{x:#x}" for x in slots[:10]))
            j = b.find(needle, j+1)
