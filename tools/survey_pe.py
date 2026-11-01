#!/usr/bin/env python3
# Static survey of OM Workspace PE binaries: arch, #exports, key imports, purpose tags.
# Uses only file/objdump/strings as subprocesses (no execution of the targets).
import os, re, subprocess, sys

ROOT = sys.argv[1]
def run(*a):
    try: return subprocess.run(a, capture_output=True, text=True, timeout=120,
                               errors="replace").stdout
    except Exception as e: return f"<err {e}>"

# purpose keyword -> regex over strings (case-insensitive)
TAGS = {
    "PTP/opcode": r"\b(FirmwareUpdate|SendObjectInfo|GetDeviceInfo|OpenSession|PTP_|9119|9125|OperationsSupported)\b",
    "firmware":   r"(firmware|CameraUpdate|FWUP|\.BIN\b|OLYMPUS A|flashing|UpdateMode)",
    "RAW/ORF":    r"(\.ORF\b|\bORF\b|demosaic|Bayer|RawDevelop|color ?matrix|white ?balance)",
    "art-filter": r"(ArtFilter|art ?filter|PictureMode|PictureEffect)",
    "image-codec":r"(libjpeg|libpng|TIFF|opencv|OpenCV|JPEG|XMP|exif|Exif)",
    "database":   r"(sqlite|SQLite|SELECT .* FROM|CREATE TABLE)",
    "network":    r"(https?://|libcurl|OpenSSL|BoringSSL|ofu\.|infinityfree)",
    "gpu/cuda":   r"(cuda|cudart|cudnn|CUDA)",
    "movie":      r"(H264|H\.264|mp4|MPEG|movie|AVI)",
    "ui":         r"(wxWidgets|Qt5|MFC|DirectUI|GdiPlus)",
}
TAGRE = {k: re.compile(v, re.I) for k, v in TAGS.items()}

def pes(root):
    for dp, _, fns in os.walk(root):
        for fn in fns:
            if fn.lower().endswith((".dll", ".exe", ".node", ".pyd")):
                yield os.path.join(dp, fn)

def analyze(p):
    ft = run("file", "-b", p).strip()
    arch = "PE32+" if "PE32+" in ft else ("PE32" if "PE32" in ft else ft[:20])
    dp = run("objdump", "-p", p)
    imports = re.findall(r"DLL Name:\s*(\S+)", dp)
    # export name count: lines in the "[Ordinal/Name Pointer] Table"
    exp = 0
    m = re.search(r"\[Ordinal/Name Pointer\] Table(.*?)(\n\n|\Z)", dp, re.S)
    if m: exp = len(re.findall(r"\[\s*\d+\]\s+\S+", m.group(1)))
    s = run("strings", "-n", "6", p)
    tags = [k for k, rx in TAGRE.items() if rx.search(s)]
    return arch, exp, imports, tags, len(s)

rows = []
for p in sorted(pes(ROOT)):
    sz = os.path.getsize(p)
    arch, exp, imports, tags, slen = analyze(p)
    rows.append((os.path.relpath(p, ROOT), sz, arch, exp, imports, tags))

rows.sort(key=lambda r: -r[1])
print(f"{'binary':52} {'size':>9} {'arch':6} {'exp':>5}  tags")
print("-"*120)
for rel, sz, arch, exp, imports, tags in rows:
    print(f"{rel:52} {sz:9d} {arch:6} {exp:5d}  {','.join(tags)}")

print("\n\n== key imports per Oly* binary (non-system) ==")
SYS = re.compile(r"^(KERNEL32|USER32|GDI32|ole32|OLEAUT32|ADVAPI32|SHELL32|msvcrt|VCRUNTIME|"
                 r"api-ms-|MSVCP|MSVCR|WS2_32|SHLWAPI|COMCTL32|COMDLG32|WINMM|IMM32|"
                 r"GDIPLUS|VERSION|CRYPT32|bcrypt|RPCRT4|SETUPAPI|CFGMGR32|WINTRUST|"
                 r"dbghelp|PROPSYS|USERENV|d3d|dxgi|OPENGL)", re.I)
for rel, sz, arch, exp, imports, tags in rows:
    base = os.path.basename(rel)
    if not base.lower().startswith(("oly","om ","camera","olive","ved","filemgr","arc")): continue
    nonsys = [i for i in imports if not SYS.match(i)]
    if nonsys:
        print(f"{base:28} -> {', '.join(sorted(set(nonsys)))}")
