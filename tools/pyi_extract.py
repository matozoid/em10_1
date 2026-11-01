#!/usr/bin/env python3 -I
"""Minimal static PyInstaller archive reader (stdlib only). Never executes the target.
usage: pyi_extract.py <exe> <outdir> [--list]"""
import struct, sys, zlib, os
MAGIC = b"MEI\x0c\x0b\x0a\x0b\x0e"
exe, out = sys.argv[1], sys.argv[2]
listonly = "--list" in sys.argv
size = os.path.getsize(exe)
with open(exe, "rb") as f:
    tail = min(size, 1 << 20)
    f.seek(size - tail); buf = f.read()
    i = buf.rfind(MAGIC)
    if i < 0: sys.exit("no PyInstaller cookie")
    cpos = size - tail + i
    f.seek(cpos)
    # v2.1+ cookie: magic(8) pkg_len toc_off toc_len pyver pylib(64)
    magic, pkg_len, toc_off, toc_len, pyver = struct.unpack("!8sIIII", f.read(24))
    cookie_len = 24 + 64
    start = cpos + cookie_len - pkg_len
    print(f"cookie@{cpos} pkg_len={pkg_len} toc_off={toc_off} toc_len={toc_len} pyver={pyver} start={start}")
    f.seek(start + toc_off); toc = f.read(toc_len)
    ents, p = [], 0
    while p < len(toc):
        (elen,) = struct.unpack_from("!I", toc, p)
        pos, dlen, ulen, flag, typ = struct.unpack_from("!IIIBc", toc, p + 4)
        name = toc[p + 4 + 14 : p + elen].split(b"\0", 1)[0].decode("utf-8", "replace")
        ents.append((name, typ.decode(), pos, dlen, ulen, flag)); p += elen
    print(len(ents), "entries")
    for name, typ, pos, dlen, ulen, flag in ents:
        print(f"{typ} {ulen:>12} {dlen:>12} z={flag} {name}")
    if listonly: sys.exit(0)
    os.makedirs(out, exist_ok=True)
    for name, typ, pos, dlen, ulen, flag in ents:
        f.seek(start + pos); d = f.read(dlen)
        if flag: d = zlib.decompress(d)
        safe = os.path.normpath(name).lstrip("/").replace("..", "_")
        if typ in ("s", "m", "M") and "." not in os.path.basename(safe): safe += ".pyc.raw"
        dest = os.path.join(out, safe); os.makedirs(os.path.dirname(dest) or out, exist_ok=True)
        with open(dest, "wb") as o: o.write(d)
