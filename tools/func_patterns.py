#!/usr/bin/env python3 -I
"""Find groups of unlabelled block-0 functions that can be labelled together.

These are the scans that produced docs/firmware/symbol-families.md. They only list candidates; a person
still decides what a family is called and writes its section.

usage:
  func_patterns.py clusters [MIN=8] [MAXSIZE=200]
      Group unlabelled functions whose bytes are identical; print groups with at least MIN members,
      largest first, with the disassembly of one member.
  func_patterns.py small [MAXBYTES=12]
      Disassemble every unlabelled function of 3..MAXBYTES bytes and classify bodies of one or two
      instructions (field/global getters and setters, constant stores, fixed-address returns, empty
      functions, plain and narrowing thunks). Prints  address <TAB> refs <TAB> name <TAB> role.
  func_patterns.py shapes [MAXBYTES=12]
      Same disassembly, but only print how often each instruction-mnemonic sequence occurs: a quick way to
      see which shapes are worth a classifier.

Needs firmware/stock/dec/blk00_40300000.bin, research/decomp/func_strings_rt.tsv and
mn10300-elf-objdump on PATH. Function sizes come from Ghidra and are sometimes cut short after the
prologue; a 3- or 5-byte "function" that is only `movm`/`add` is such a fragment, not a real body.
"""
import collections, os, re, shutil, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import symbols

RT = 0x7d991020
BLK = os.path.join(symbols.ROOT, "firmware", "stock", "dec", "blk00_40300000.bin")
OBJDUMP = "mn10300-elf-objdump"
W = {"mov": "", "movhu": "u16_", "movbu": "u8_"}
C = {"mov": "", "movhu": "(u16)", "movbu": "(u8)"}
P = {"mov": "", "movhu": "(u16*)", "movbu": "(u8*)"}
EXT = {"exth": "s16", "exthu": "u16", "extb": "s8", "extbu": "u8"}


def unlabelled():
    lab = symbols.labelled()
    return [f for f in symbols.functions() if f[0] not in lab]


def disasm(addr, size):
    """Instructions of one function as a list of 'mnemonic operands' strings."""
    od = shutil.which(OBJDUMP) or sys.exit(OBJDUMP + " not found on PATH")
    a = int(addr, 16)
    out = subprocess.run([od, "-D", "-b", "binary", "-m", "am33-2", "--adjust-vma=%#x" % RT,
                          "--start-address=%#x" % a, "--stop-address=%#x" % (a + size), BLK],
                         capture_output=True, text=True).stdout
    ins = []
    for line in out.splitlines():
        parts = line.split("\t")
        if re.match(r"\s*[0-9a-f]+:", parts[0]) and len(parts) >= 3:
            ins.append(" ".join(" ".join(parts[2:]).split()))
    return ins


def disasm_all(funcs):
    with ThreadPoolExecutor(max_workers=8) as ex:
        return list(zip(funcs, ex.map(lambda f: disasm(f[0], f[1]), funcs)))


def mem(op):
    m = re.fullmatch(r"\((\d+),a0\)", op)
    if m:
        return "f" + m[1], "(this+%s)" % m[1]
    m = re.fullmatch(r"\((0x[0-9a-f]+)\)", op)
    if m:
        return "g" + m[1][2:], m[1]
    return None


def classify(ins):
    """Return (name, role) for a one- or two-instruction body, or None."""
    if len(ins) == 1 and ins[0] == "retf [],0":
        return "nop", "Empty function: `retf`."
    if len(ins) == 2 and ins[1] == "retf [],0":
        i = ins[0]
        m = re.fullmatch(r"(mov|movhu|movbu) \((\d+),a0\),(d0|a0)", i)
        if m:
            return "get_%sf%s" % (W[m[1]], m[2]), "Leaf `return %s*(this+%s)`." % (C[m[1]], m[2])
        m = re.fullmatch(r"(mov|movhu|movbu) (d0|a1|d1),\((\d+),a0\)", i)
        if m:
            return "set_%sf%s" % (W[m[1]], m[3]), "`*%s(this+%s) = %s`." % (P[m[1]], m[3], m[2])
        m = re.fullmatch(r"(mov|movhu|movbu) \((0x[0-9a-f]+)\),(d0|a0)", i)
        if m:
            return "global_%s%s_get" % (W[m[1]], m[2][2:]), "Leaf `return %s*%s`." % (C[m[1]], m[2])
        m = re.fullmatch(r"(mov|movhu|movbu) (d0|a0),\((0x[0-9a-f]+)\)", i)
        if m:
            return "global_%s%s_set" % (W[m[1]], m[3][2:]), "`*%s%s = %s`." % (P[m[1]], m[3], m[2])
        m = re.fullmatch(r"mov (-?\d+|0x[0-9a-f]+),a0", i)
        if m:
            v = int(m[1], 0) & 0xffffffff
            return "ret_ptr_%08x" % v, "`return 0x%08x` (a fixed address, in `a0`)." % v
    if len(ins) == 2 and ins[0].startswith("call") and ins[1].startswith("ret"):
        m = re.match(r"call (0x[0-9a-f]+)", ins[0])
        if m:
            return "thunk_to_%s" % m[1][2:], "Plain thunk: `call %s; ret`." % m[1]
    if len(ins) == 3 and ins[2].startswith("ret"):
        i0, i1 = ins[0], ins[1]
        m0 = re.fullmatch(r"(clr d0|mov (-?\d+|0x[0-9a-f]+),d0)", i0)
        m1 = re.fullmatch(r"(mov|movhu|movbu) d0,(.+)", i1)
        if m0 and m1 and mem(m1[2]):
            v = 0 if i0 == "clr d0" else int(m0[2], 0)
            k, t = mem(m1[2])
            vs = ("%#x" % (v & 0xffffffff)) if abs(v) > 255 else str(v)
            w = "" if m1[1] == "mov" else "_" + W[m1[1]].rstrip("_")
            return "store%s_%s_%s" % (w, vs.replace("-", "m"), k), "`*%s%s = %s`." % (P[m1[1]], t, vs)
        m1 = re.fullmatch(r"(mov|movhu|movbu) (.+),d0", i0)
        m2 = re.fullmatch(r"(exth|exthu|extb|extbu) d0", i1)
        if m1 and m2 and mem(m1[2]):
            k, t = mem(m1[2])
            return "get_%s_%s" % (EXT[m2[1]], k), "Leaf `return (%s)*%s%s`." % (EXT[m2[1]], P[m1[1]], t)
        mc = re.fullmatch(r"call (0x[0-9a-f]+),.*", i0)
        if mc and m2:
            return ("thunk_%s_%s" % (EXT[m2[1]], mc[1][2:]),
                    "`return (%s) %s()` — thunk with result conversion." % (EXT[m2[1]], mc[1]))
        m3 = re.fullmatch(r"(exth|exthu|extb|extbu) (d0|d1)", i0)
        mt = re.match(r"call (0x[0-9a-f]+)", i1)
        if m3 and mt:
            return ("thunk_arg%s_%s" % (EXT[m3[1]], mt[1][2:]),
                    "Converts `%s` to %s, then calls `%s`." % (m3[2], EXT[m3[1]], mt[1]))
        if mc and i1 == "clr d0":
            return "call0_%s" % mc[1][2:], "Calls `%s` and returns 0." % mc[1]
        if i0 == "clr d0" and mt:
            return "call_arg0_%s" % mt[1][2:], "Calls `%s` with `d0 = 0`." % mt[1]
    return None


def cmd_clusters(minimum, maxsize):
    b = open(BLK, "rb").read()
    groups = collections.defaultdict(list)
    for a, size, refs, _ in unlabelled():
        if 8 <= size <= maxsize:
            o = int(a, 16) - RT
            groups[b[o:o + size]].append(a)
    cl = sorted(((k, v) for k, v in groups.items() if len(v) >= minimum), key=lambda kv: -len(kv[1]))
    print("%d groups with at least %d identical members; %d functions"
          % (len(cl), minimum, sum(len(v) for _, v in cl)))
    for k, v in cl:
        print("=== %d copies, %d bytes, e.g. %s" % (len(v), len(k), v[0]))
        for i in disasm(v[0], len(k)):
            print("    " + i)


def small(maxbytes):
    return disasm_all([f for f in unlabelled() if 3 <= f[1] <= maxbytes])


def cmd_small(maxbytes):
    n = collections.Counter()
    for (a, size, refs, _), ins in small(maxbytes):
        r = classify(ins)
        if r:
            n[r[0].split("_")[0]] += 1
            print("%s\t%d\t%s_%s\t%s" % (a, refs, r[0], a, r[1]))
    print("# classified: %s" % dict(n), file=sys.stderr)


def cmd_shapes(maxbytes):
    c = collections.Counter("; ".join(i.split()[0] for i in ins) for _, ins in small(maxbytes))
    for shape, n in c.most_common(60):
        print("%6d  %s" % (n, shape))


def main(argv):
    if not argv:
        sys.exit(__doc__)
    num = [int(x) for x in argv[1:]]
    if argv[0] == "clusters":
        cmd_clusters(*(num + [8, 200][len(num):]))
    elif argv[0] == "small":
        cmd_small(*(num + [12][len(num):]))
    elif argv[0] == "shapes":
        cmd_shapes(*(num + [12][len(num):]))
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
