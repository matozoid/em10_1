#!/usr/bin/env python3 -I
"""Work with the three symbol documents (stdlib only; reads our own docs plus the local function list).

  docs/firmware/symbol-map.md        hand-analysed symbols
  docs/firmware/symbol-families.md   pattern families (machine-listed)
  docs/firmware/symbol-strings.md    names derived from log strings (heuristic)

A symbol row is a Markdown table row that starts with  | `0xADDRESS` |  and has the name in the first
backticked cell after the address (the xrefs column, when present, is skipped).

usage:
  symbols.py stats                      rows per file and per section
  symbols.py export [OUT.tsv]           address <TAB> name <TAB> file   (first row wins per address;
                                        symbol-map.md has priority, then families, then strings)
  symbols.py dupes                      addresses listed more than once, names used more than once
  symbols.py candidates LO HI [MAXSIZE] unlabelled functions with LO..HI references, most referenced
                                        first; bodies up to MAXSIZE bytes are disassembled (needs
                                        tools/dis.py and research/decomp/func_strings_rt.tsv)
"""
import collections, csv, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
DOCS = [os.path.join(ROOT, "docs", "firmware", f)
        for f in ("symbol-map.md", "symbol-families.md", "symbol-strings.md")]
FUNCS = os.path.join(ROOT, "research", "decomp", "func_strings_rt.tsv")
ROW = re.compile(r"^\| `0x([0-9a-f]{8})` \|(.*)$")
NAME = re.compile(r"`([A-Za-z_][A-Za-z0-9_:+]*)`")


def rows():
    """Yield (address, name, file, section) for every symbol row, in file priority order."""
    for path in DOCS:
        section = ""
        for line in open(path, encoding="utf-8"):
            if line.startswith("## "):
                section = line[3:].strip()
                continue
            m = ROW.match(line)
            if not m:
                continue
            cells = m.group(2).split("|")
            name = ""
            for cell in cells[:2]:          # name is the 1st cell, or the 2nd when a xrefs column exists
                n = NAME.search(cell)
                if n:
                    name = n.group(1)
                    break
            yield m.group(1), name, os.path.basename(path), section


def labelled():
    return {a for a, _, _, _ in rows()}


def functions():
    """(address, size, refs, strings) from the Ghidra FuncStrings export."""
    out = []
    for r in list(csv.reader(open(FUNCS, encoding="utf-8", errors="replace"), delimiter="\t"))[1:]:
        out.append((r[0], int(r[1]), int(r[2]), r[4] if len(r) > 4 else ""))
    return out


def cmd_stats():
    per = collections.OrderedDict()
    for a, _, f, s in rows():
        per.setdefault(f, collections.Counter())[s] += 1
    total = len(labelled())
    for f, c in per.items():
        print("%s: %d rows" % (f, sum(c.values())))
        for s, n in c.most_common():
            if n >= 20:
                print("    %6d  %s" % (n, s))
    print("distinct addresses: %d" % total)
    if os.path.exists(FUNCS):
        fs = functions()
        lab = labelled()
        print("functions in the Ghidra export: %d, of which labelled: %d"
              % (len(fs), sum(1 for f in fs if f[0] in lab)))


def cmd_export(out):
    seen = set()
    w = open(out, "w", encoding="utf-8") if out else sys.stdout
    n = 0
    for a, name, f, _ in rows():
        if a in seen or not name:
            continue
        seen.add(a)
        w.write("%s\t%s\t%s\n" % (a, name, f))
        n += 1
    if out:
        w.close()
        print("wrote %d names to %s" % (n, out))


def cmd_dupes():
    by_addr = collections.defaultdict(list)
    by_name = collections.defaultdict(set)
    for a, name, f, s in rows():
        by_addr[a].append("%s / %s" % (f, s))
        if name:
            by_name[name].add(a)
    da = {a: v for a, v in by_addr.items() if len(v) > 1}
    dn = {n: v for n, v in by_name.items() if len(v) > 1}
    print("addresses listed more than once: %d" % len(da))
    for a in sorted(da):
        print("  0x%s  %s" % (a, "  |  ".join(da[a])))
    print("names used for more than one address: %d" % len(dn))
    for n in sorted(dn):
        print("  %s  %s" % (n, " ".join("0x" + a for a in sorted(dn[n]))))


def cmd_candidates(lo, hi, maxsize):
    lab = labelled()
    text = "".join(open(p, encoding="utf-8").read() for p in DOCS)
    c = sorted((f for f in functions() if f[0] not in lab and lo <= f[2] <= hi),
               key=lambda f: (-f[2], f[0]))
    print("candidates: %d" % len(c))
    for a, size, refs, strings in c:
        print("== %s refs=%d size=%d mentions=%d %s" % (a, refs, size, text.count("0x" + a), strings[:100]))
        if size <= maxsize:
            end = "%x" % (int(a, 16) + size)
            print(subprocess.run([sys.executable, "-I", os.path.join(HERE, "dis.py"), a, end],
                                 capture_output=True, text=True).stdout.rstrip())


def main(argv):
    if not argv:
        sys.exit(__doc__)
    cmd = argv[0]
    if cmd == "stats":
        cmd_stats()
    elif cmd == "export":
        cmd_export(argv[1] if len(argv) > 1 else None)
    elif cmd == "dupes":
        cmd_dupes()
    elif cmd == "candidates" and len(argv) >= 3:
        cmd_candidates(int(argv[1]), int(argv[2]), int(argv[3]) if len(argv) > 3 else 0)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
