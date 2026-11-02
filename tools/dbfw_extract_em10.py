#!/usr/bin/env python3
# Extract only E-M10 entries from the community db-firmware profiles/compatibility JSON.
# Untrusted data: run with `python3 -I`, pass file paths as argv.
import json, sys, re

def walk(o, path=""):
    """Yield (path, obj) for dict/list nodes mentioning em10."""
    if isinstance(o, dict):
        yield path, o
        for k, v in o.items():
            yield from walk(v, f"{path}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk(v, f"{path}[{i}]")

def summarize(obj, maxlen=120):
    out = {}
    for k, v in obj.items():
        if isinstance(v, str):
            if len(v) > maxlen:
                out[k] = f"<str len={len(v)}> {v[:60]}…"
            else:
                out[k] = v
        elif isinstance(v, (int, float, bool)) or v is None:
            out[k] = v
        elif isinstance(v, list):
            out[k] = f"<list n={len(v)}>"
        elif isinstance(v, dict):
            out[k] = f"<dict keys={list(v.keys())}>"
    return out

for fp in sys.argv[1:]:
    print(f"\n########## {fp} ##########")
    with open(fp, "rb") as f:
        data = json.load(f)
    # find nodes whose id/profile/body/title mentions em10 or panasonic
    seen = set()
    for path, obj in walk(data):
        if not isinstance(obj, dict):
            continue
        blob = " ".join(str(obj.get(k, "")) for k in
                        ("id", "profile", "body", "model", "title", "name", "file", "label"))
        if re.search(r"em10|panasonic|조리개", blob, re.I):
            key = path.rsplit("[", 1)[0]  # collapse list siblings
            if path in seen:
                continue
            seen.add(path)
            print(f"\n--- {path} ---")
            print(json.dumps(summarize(obj), ensure_ascii=False, indent=2))
