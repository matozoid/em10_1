#!/usr/bin/env python3 -I
"""Scan docs/ for runtime addresses and emit an address -> source-doc index.

Clean-room helper: reads only our own Markdown/CSV docs (never firmware bytes), so its output is
committable. Use it to find where a given address is already discussed, and to spot addresses that
appear in only one doc (candidates for promotion into docs/firmware/symbol-map.md).

usage:
  symbol_index.py [DOCS_DIR]      # default DOCS_DIR = docs
  symbol_index.py --once ADDR     # show which docs mention one address
"""
import re, os, sys, collections

ADDR = re.compile(r"0x(?:7d|7e|40|41|42)[0-9a-f]{6}")

def build(root):
    idx = collections.defaultdict(set)
    for dp, _, fs in os.walk(root):
        for f in fs:
            if not f.endswith((".md", ".csv", ".txt")):
                continue
            p = os.path.join(dp, f)
            t = open(p, encoding="utf-8", errors="replace").read()
            for m in set(ADDR.findall(t)):
                idx[m].add(os.path.relpath(p, root))
    return idx

def main():
    args = sys.argv[1:]
    if args and args[0] == "--once":
        idx = build("docs")
        a = args[1].lower()
        print("\n".join(sorted(idx.get(a, []))) or "(not documented)")
        return
    root = args[0] if args else "docs"
    idx = build(root)
    print("# address -> source docs (%d unique)\n" % len(idx))
    print("| address | docs |\n|---|---|")
    for a in sorted(idx):
        print("| `%s` | %s |" % (a, ", ".join("`%s`" % d for d in sorted(idx[a]))))

if __name__ == "__main__":
    main()
