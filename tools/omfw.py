#!/usr/bin/env python3 -I
"""Olympus/OM firmware container tool (clean-room from observed format; stdlib only).
Container = blocks; block = 32B header + dlen data + 32B footer.
 header: 'OE' model(BCD-ish) .. @8 load addr u32, @12 dlen u32, @16 ver u32, @20 u2 u32, rest reserved.
 footer: header[:28] echo + u32 V, with V + sum32(dec) + 2*sum32(hdr[:28]) == 0 (mod 2^32).
 data per 16B chunk: plain[j] = enc[P[j]] ^ 0xFF
usage: omfw.py info|dec|enc FILE [OUTDIR_OR_OUT]"""
import struct, sys, os
P = [1,3,0,2,6,4,7,5,11,10,9,8,13,14,12,15]
Q = [0]*16
for j,p in enumerate(P): Q[p] = j
M = 0xFFFFFFFF
def dec(d): return b"".join(bytes(d[i+P[j]]^0xFF for j in range(16)) for i in range(0,len(d),16))
def enc(d):
    out=bytearray()
    for i in range(0,len(d),16):
        c=d[i:i+16]; x=bytearray(16)
        for j in range(16): x[P[j]] = c[j]^0xFF
        out+=x
    return bytes(out)
def s32(b): return sum(struct.unpack("<%dI"%(len(b)//4), b)) & M
def footer_v(hdr, plain): return (-(s32(plain) + 2*s32(hdr[:28]))) & M
def blocks(raw):
    off=0; i=0
    while off < len(raw):
        h=raw[off:off+32]
        if len(h)!=32 or h[:2]!=b"OE": raise ValueError("bad header at %#x"%off)
        load,dlen,ver,u2 = struct.unpack("<4I", h[8:24])
        if dlen%16 or off+64+dlen>len(raw): raise ValueError("truncated block at %#x"%off)
        yield dict(idx=i,off=off,hdr=h,load=load,dlen=dlen,ver=ver,u2=u2,data=raw[off+32:off+32+dlen],ftr=raw[off+32+dlen:off+64+dlen])
        off+=64+dlen; i+=1
if __name__=="__main__":
    cmd,f=sys.argv[1],sys.argv[2]; raw=open(f,"rb").read()
    out=sys.argv[3] if len(sys.argv)>3 else None
    if cmd in("info","dec"):
        if out: os.makedirs(out,exist_ok=True)
        for b in blocks(raw):
            p=dec(b["data"]); v=footer_v(b["hdr"],p)
            ok = b["ftr"][:28]==b["hdr"][:28] and struct.unpack("<I",b["ftr"][28:])[0]==v
            print("blk%d off=%#x load=%#010x len=%#x ver=%#x u2=%#x footer_ok=%s sha=%s"%(b["idx"],b["off"],b["load"],b["dlen"],b["ver"],b["u2"],ok,__import__("hashlib").sha256(p).hexdigest()[:12]))
            if cmd=="dec" and out: open(os.path.join(out,"blk%02d_%08x.bin"%(b["idx"],b["load"])),"wb").write(p)
