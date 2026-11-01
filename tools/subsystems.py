#!/usr/bin/env python3
"""Group Ghidra FuncStrings.java TSV output by log-tag prefix (e.g. GUI, APPEVENT_CAMST, WIFI_REMOCON_CGI).
usage: subsystems.py func_strings.tsv [min_count=5]"""
import re, sys, collections
rows = [l.rstrip('\n').split('\t') for l in open(sys.argv[1])][1:]
mn = int(sys.argv[2]) if len(sys.argv) > 2 else 5
c = collections.defaultdict(set)
for r in rows:
    if len(r) < 5 or not r[4]: continue
    for s in r[4].split(' | '):
        m = re.match(r'\[?([A-Za-z][A-Za-z0-9_]{2,15})[\]:_ ]', s)
        if m and (s.startswith('[') or '_' in m.group(1)): c[m.group(1)].add(r[0])
for k, v in sorted(c.items(), key=lambda kv: -len(kv[1])):
    if len(v) >= mn: print(f"{k}\t{len(v)}\t{sorted(v)[0]}")
