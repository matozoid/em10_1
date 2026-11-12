# Firmware symbol families (E-M10 Mark I, body fw 1.4)

Machine-listed symbols for routines that the firmware repeats many times: per-class copies of the same
small routine, compiler entry stubs, and one-line field writers. Each family was found by an exact byte
match or byte-pattern scan over block 0 and is described once at the top of its section; the rows only
give the address, name and the parameter that differs. Hand-analysed symbols live in
[`symbol-map.md`](symbol-map.md); `tools/symbol_index.py` indexes both files.

Runtime base `0x7d991020`; addresses are runtime addresses.

## OlyHfwOpe sub-component table getters (pattern family)
Every function in block 0 with the exact byte sequence of `olyhfw_ope_subcomp_get45` `0x7e29cf9d`
(`mov d0,d1; exthu d1; cmp N,d1; bcc; exthu d0; asl2 d0; add OFF,a0; mov (d0,a0),a0; …; retf`) is a
bounds-checked getter over a pointer table inside a GUI screen object: `(a0=this, d0=u16 idx)` →
`idx < N ? *(this + OFF + idx*4) : NULL`. A byte-pattern scan on 2026-11-12 found **197** such functions
(OFF = 792 in 192 of them), all in banks `0x7e27`–`0x7e2c`; each GUI screen class has its own copy sized to
its number of sub-components. The ones already listed in the main table keep their earlier names; the
remaining 127 are listed here, named `olyhfw_subcomp_get<N>_<address>`. The xref column is Ghidra's
reference count (`—` where the function list has no entry).

| address | xrefs | symbol | role | source |
|---|---|---|---|---|
| `0x7e27341d` | 13 | `olyhfw_subcomp_get13_7e27341d` | `idx < 13 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e273dd7` | 5 | `olyhfw_subcomp_get6_7e273dd7` | `idx < 6 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e2769d2` | 7 | `olyhfw_subcomp_get112_7e2769d2` | `idx < 112 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e277edf` | 10 | `olyhfw_subcomp_get10_7e277edf` | `idx < 10 ? *(this + 880 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e2781dd` | 7 | `olyhfw_subcomp_get11_7e2781dd` | `idx < 11 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e2784d7` | 9 | `olyhfw_subcomp_get11_7e2784d7` | `idx < 11 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e279326` | 7 | `olyhfw_subcomp_get9_7e279326` | `idx < 9 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e279d29` | 3 | `olyhfw_subcomp_get3_7e279d29` | `idx < 3 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e279f51` | 5 | `olyhfw_subcomp_get10_7e279f51` | `idx < 10 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e27a65c` | 8 | `olyhfw_subcomp_get9_7e27a65c` | `idx < 9 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e27a981` | 7 | `olyhfw_subcomp_get7_7e27a981` | `idx < 7 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e27b03d` | 7 | `olyhfw_subcomp_get9_7e27b03d` | `idx < 9 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e27bb24` | 5 | `olyhfw_subcomp_get9_7e27bb24` | `idx < 9 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e27bd51` | 14 | `olyhfw_subcomp_get15_7e27bd51` | `idx < 15 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e27c06d` | 6 | `olyhfw_subcomp_get9_7e27c06d` | `idx < 9 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e27c9f8` | 12 | `olyhfw_subcomp_get14_7e27c9f8` | `idx < 14 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e27d8d7` | 16 | `olyhfw_subcomp_get17_7e27d8d7` | `idx < 17 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e27dc41` | 15 | `olyhfw_subcomp_get15_7e27dc41` | `idx < 15 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e27e9f9` | 17 | `olyhfw_subcomp_get17_7e27e9f9` | `idx < 17 ? *(this + 792 + idx*4) : NULL` (bank `0x7e27`). | pattern scan |
| `0x7e2806f3` | 15 | `olyhfw_subcomp_get18_7e2806f3` | `idx < 18 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28186e` | 5 | `olyhfw_subcomp_get7_7e28186e` | `idx < 7 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e281aa6` | 11 | `olyhfw_subcomp_get12_7e281aa6` | `idx < 12 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e281d60` | 15 | `olyhfw_subcomp_get54_7e281d60` | `idx < 54 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28346c` | 7 | `olyhfw_subcomp_get42_7e28346c` | `idx < 42 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28376c` | 16 | `olyhfw_subcomp_get16_7e28376c` | `idx < 16 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28403f` | 9 | `olyhfw_subcomp_get9_7e28403f` | `idx < 9 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e287184` | 11 | `olyhfw_subcomp_get15_7e287184` | `idx < 15 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e287426` | 17 | `olyhfw_subcomp_get18_7e287426` | `idx < 18 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e287c64` | 5 | `olyhfw_subcomp_get6_7e287c64` | `idx < 6 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e287f06` | 11 | `olyhfw_subcomp_get41_7e287f06` | `idx < 41 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e288230` | 5 | `olyhfw_subcomp_get6_7e288230` | `idx < 6 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e288488` | 12 | `olyhfw_subcomp_get13_7e288488` | `idx < 13 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e288800` | 5 | `olyhfw_subcomp_get6_7e288800` | `idx < 6 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e288f25` | 3 | `olyhfw_subcomp_get4_7e288f25` | `idx < 4 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e289131` | 4 | `olyhfw_subcomp_get8_7e289131` | `idx < 8 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28af60` | 10 | `olyhfw_subcomp_get12_7e28af60` | `idx < 12 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28b4ef` | 13 | `olyhfw_subcomp_get25_7e28b4ef` | `idx < 25 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28bdc3` | 12 | `olyhfw_subcomp_get13_7e28bdc3` | `idx < 13 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28d2d9` | 11 | `olyhfw_subcomp_get13_7e28d2d9` | `idx < 13 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28d714` | 5 | `olyhfw_subcomp_get7_7e28d714` | `idx < 7 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28d9d0` | 13 | `olyhfw_subcomp_get13_7e28d9d0` | `idx < 13 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28e079` | 2 | `olyhfw_subcomp_get3_7e28e079` | `idx < 3 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28e305` | — | `olyhfw_subcomp_get1_7e28e305` | `idx < 1 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28e39a` | 7 | `olyhfw_subcomp_get8_7e28e39a` | `idx < 8 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28e600` | 10 | `olyhfw_subcomp_get88_7e28e600` | `idx < 88 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28ec9c` | 4 | `olyhfw_subcomp_get4_7e28ec9c` | `idx < 4 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28f002` | 3 | `olyhfw_subcomp_get11_7e28f002` | `idx < 11 ? *(this + 792 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e28f9f4` | 2 | `olyhfw_subcomp_get5_7e28f9f4` | `idx < 5 ? *(this + 796 + idx*4) : NULL` (bank `0x7e28`). | pattern scan |
| `0x7e2903c7` | 11 | `olyhfw_subcomp_get35_7e2903c7` | `idx < 35 ? *(this + 792 + idx*4) : NULL` (bank `0x7e29`). | pattern scan |
| `0x7e290c73` | 8 | `olyhfw_subcomp_get12_7e290c73` | `idx < 12 ? *(this + 792 + idx*4) : NULL` (bank `0x7e29`). | pattern scan |
| `0x7e294120` | 15 | `olyhfw_subcomp_get15_7e294120` | `idx < 15 ? *(this + 792 + idx*4) : NULL` (bank `0x7e29`). | pattern scan |
| `0x7e29477c` | 9 | `olyhfw_subcomp_get30_7e29477c` | `idx < 30 ? *(this + 792 + idx*4) : NULL` (bank `0x7e29`). | pattern scan |
| `0x7e294f27` | 9 | `olyhfw_subcomp_get10_7e294f27` | `idx < 10 ? *(this + 824 + idx*4) : NULL` (bank `0x7e29`). | pattern scan |
| `0x7e295305` | 15 | `olyhfw_subcomp_get16_7e295305` | `idx < 16 ? *(this + 792 + idx*4) : NULL` (bank `0x7e29`). | pattern scan |
| `0x7e297b21` | 13 | `olyhfw_subcomp_get30_7e297b21` | `idx < 30 ? *(this + 792 + idx*4) : NULL` (bank `0x7e29`). | pattern scan |
| `0x7e298967` | 5 | `olyhfw_subcomp_get5_7e298967` | `idx < 5 ? *(this + 808 + idx*4) : NULL` (bank `0x7e29`). | pattern scan |
| `0x7e29934d` | 8 | `olyhfw_subcomp_get21_7e29934d` | `idx < 21 ? *(this + 792 + idx*4) : NULL` (bank `0x7e29`). | pattern scan |
| `0x7e29bd70` | 8 | `olyhfw_subcomp_get9_7e29bd70` | `idx < 9 ? *(this + 792 + idx*4) : NULL` (bank `0x7e29`). | pattern scan |
| `0x7e29c2fc` | 9 | `olyhfw_subcomp_get10_7e29c2fc` | `idx < 10 ? *(this + 792 + idx*4) : NULL` (bank `0x7e29`). | pattern scan |
| `0x7e29c7ba` | 8 | `olyhfw_subcomp_get15_7e29c7ba` | `idx < 15 ? *(this + 792 + idx*4) : NULL` (bank `0x7e29`). | pattern scan |
| `0x7e29cc2d` | 7 | `olyhfw_subcomp_get8_7e29cc2d` | `idx < 8 ? *(this + 792 + idx*4) : NULL` (bank `0x7e29`). | pattern scan |
| `0x7e2a181a` | 17 | `olyhfw_subcomp_get28_7e2a181a` | `idx < 28 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2a`). | pattern scan |
| `0x7e2aa2b3` | 8 | `olyhfw_subcomp_get10_7e2aa2b3` | `idx < 10 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2a`). | pattern scan |
| `0x7e2aa6a3` | 6 | `olyhfw_subcomp_get6_7e2aa6a3` | `idx < 6 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2a`). | pattern scan |
| `0x7e2aa9b1` | 7 | `olyhfw_subcomp_get9_7e2aa9b1` | `idx < 9 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2a`). | pattern scan |
| `0x7e2af4b1` | 11 | `olyhfw_subcomp_get12_7e2af4b1` | `idx < 12 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2a`). | pattern scan |
| `0x7e2b05ed` | 11 | `olyhfw_subcomp_get16_7e2b05ed` | `idx < 16 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b0996` | 9 | `olyhfw_subcomp_get10_7e2b0996` | `idx < 10 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b0d84` | 14 | `olyhfw_subcomp_get32_7e2b0d84` | `idx < 32 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b1327` | 5 | `olyhfw_subcomp_get6_7e2b1327` | `idx < 6 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b16da` | 2 | `olyhfw_subcomp_get2_7e2b16da` | `idx < 2 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b1839` | 9 | `olyhfw_subcomp_get13_7e2b1839` | `idx < 13 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b1bd2` | 10 | `olyhfw_subcomp_get10_7e2b1bd2` | `idx < 10 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b2e35` | 9 | `olyhfw_subcomp_get21_7e2b2e35` | `idx < 21 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b3712` | 3 | `olyhfw_subcomp_get3_7e2b3712` | `idx < 3 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b3aff` | 5 | `olyhfw_subcomp_get5_7e2b3aff` | `idx < 5 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b3e18` | 8 | `olyhfw_subcomp_get8_7e2b3e18` | `idx < 8 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b42f3` | 6 | `olyhfw_subcomp_get6_7e2b42f3` | `idx < 6 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b467a` | 11 | `olyhfw_subcomp_get29_7e2b467a` | `idx < 29 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b5f54` | 6 | `olyhfw_subcomp_get6_7e2b5f54` | `idx < 6 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b626a` | 5 | `olyhfw_subcomp_get5_7e2b626a` | `idx < 5 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b64a6` | 10 | `olyhfw_subcomp_get14_7e2b64a6` | `idx < 14 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b681d` | 5 | `olyhfw_subcomp_get7_7e2b681d` | `idx < 7 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b6f5b` | 7 | `olyhfw_subcomp_get4_7e2b6f5b` | `idx < 4 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b7193` | 9 | `olyhfw_subcomp_get9_7e2b7193` | `idx < 9 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b73eb` | — | `olyhfw_subcomp_get1_7e2b73eb` | `idx < 1 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b8841` | 15 | `olyhfw_subcomp_get15_7e2b8841` | `idx < 15 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b9117` | 10 | `olyhfw_subcomp_get10_7e2b9117` | `idx < 10 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b93c4` | 14 | `olyhfw_subcomp_get14_7e2b93c4` | `idx < 14 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b9a38` | 14 | `olyhfw_subcomp_get14_7e2b9a38` | `idx < 14 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b9d53` | 2 | `olyhfw_subcomp_get2_7e2b9d53` | `idx < 2 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2b9f33` | 6 | `olyhfw_subcomp_get6_7e2b9f33` | `idx < 6 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2ba15a` | 2 | `olyhfw_subcomp_get2_7e2ba15a` | `idx < 2 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2ba33a` | 6 | `olyhfw_subcomp_get6_7e2ba33a` | `idx < 6 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bad77` | 4 | `olyhfw_subcomp_get4_7e2bad77` | `idx < 4 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bb2b2` | 17 | `olyhfw_subcomp_get17_7e2bb2b2` | `idx < 17 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bb594` | 2 | `olyhfw_subcomp_get2_7e2bb594` | `idx < 2 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bb780` | — | `olyhfw_subcomp_get3_7e2bb780` | `idx < 3 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bbdf6` | 8 | `olyhfw_subcomp_get8_7e2bbdf6` | `idx < 8 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bc4f4` | — | `olyhfw_subcomp_get3_7e2bc4f4` | `idx < 3 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bc665` | 9 | `olyhfw_subcomp_get14_7e2bc665` | `idx < 14 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bd2df` | — | `olyhfw_subcomp_get2_7e2bd2df` | `idx < 2 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bd450` | 5 | `olyhfw_subcomp_get5_7e2bd450` | `idx < 5 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bd65e` | 5 | `olyhfw_subcomp_get23_7e2bd65e` | `idx < 23 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bd938` | 13 | `olyhfw_subcomp_get67_7e2bd938` | `idx < 67 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bddfe` | 4 | `olyhfw_subcomp_get40_7e2bddfe` | `idx < 40 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2be0af` | 4 | `olyhfw_subcomp_get4_7e2be0af` | `idx < 4 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2be79d` | 2 | `olyhfw_subcomp_get2_7e2be79d` | `idx < 2 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bea2c` | 2 | `olyhfw_subcomp_get2_7e2bea2c` | `idx < 2 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bec23` | 2 | `olyhfw_subcomp_get2_7e2bec23` | `idx < 2 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bee1d` | 2 | `olyhfw_subcomp_get2_7e2bee1d` | `idx < 2 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bf0a6` | 2 | `olyhfw_subcomp_get2_7e2bf0a6` | `idx < 2 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bfa25` | 4 | `olyhfw_subcomp_get4_7e2bfa25` | `idx < 4 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2bfc37` | 10 | `olyhfw_subcomp_get10_7e2bfc37` | `idx < 10 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2b`). | pattern scan |
| `0x7e2c05ac` | 3 | `olyhfw_subcomp_get3_7e2c05ac` | `idx < 3 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2c`). | pattern scan |
| `0x7e2c07e8` | 2 | `olyhfw_subcomp_get3_7e2c07e8` | `idx < 3 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2c`). | pattern scan |
| `0x7e2c09da` | 9 | `olyhfw_subcomp_get9_7e2c09da` | `idx < 9 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2c`). | pattern scan |
| `0x7e2c0c80` | — | `olyhfw_subcomp_get3_7e2c0c80` | `idx < 3 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2c`). | pattern scan |
| `0x7e2c0df1` | 18 | `olyhfw_subcomp_get20_7e2c0df1` | `idx < 20 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2c`). | pattern scan |
| `0x7e2c109e` | — | `olyhfw_subcomp_get3_7e2c109e` | `idx < 3 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2c`). | pattern scan |
| `0x7e2c1714` | 8 | `olyhfw_subcomp_get8_7e2c1714` | `idx < 8 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2c`). | pattern scan |
| `0x7e2c1dfc` | — | `olyhfw_subcomp_get3_7e2c1dfc` | `idx < 3 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2c`). | pattern scan |
| `0x7e2c1f6d` | 7 | `olyhfw_subcomp_get9_7e2c1f6d` | `idx < 9 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2c`). | pattern scan |
| `0x7e2c2ba8` | 10 | `olyhfw_subcomp_get9_7e2c2ba8` | `idx < 9 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2c`). | pattern scan |
| `0x7e2c2e43` | 7 | `olyhfw_subcomp_get7_7e2c2e43` | `idx < 7 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2c`). | pattern scan |
| `0x7e2c30bb` | 18 | `olyhfw_subcomp_get18_7e2c30bb` | `idx < 18 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2c`). | pattern scan |
| `0x7e2c34af` | 10 | `olyhfw_subcomp_get10_7e2c34af` | `idx < 10 ? *(this + 792 + idx*4) : NULL` (bank `0x7e2c`). | pattern scan |

## Cmp component Idle-enter copies (pattern family)
Every Cmp component class carries its own copy of the same "enter Idle" routine: a `call`+`ret` wrapper
followed by a body that sets the state word to 49 at `+948` and `+256`, `+636 = 466`, `+632 = 0` and logs
`"Cmp_Play%s Idle"` ([[cmp-component-framework]]). A byte-pattern scan on 2026-11-12 finds **28** copies in
banks `0x7e15`–`0x7e1c`; 19 wrappers were already labelled individually in the main table. The remaining 9
wrappers are listed here as `cmp_enter_idle_<address>`; each body sits 8 bytes after its wrapper.

| address | xrefs | symbol | role | source |
|---|---|---|---|---|
| `0x7e127bf4` | 22 | `cmp_enter_idle_7e127bf4` | Cmp component Idle-state enter: thin wrapper → body `0x7e127bfc`, which sets state 49 (Idle) at `+948` and `+256`, `+636 = 466`, `+632 = 0`, and logs `"Cmp_Play%s Idle"`. Byte-identical to the other copies listed in the Cmp Idle-enter section. | pattern scan |
| `0x7e14b090` | 23 | `cmp_enter_idle_7e14b090` | Cmp component Idle-state enter: thin wrapper → body `0x7e14b098`, which sets state 49 (Idle) at `+948` and `+256`, `+636 = 466`, `+632 = 0`, and logs `"Cmp_Play%s Idle"`. Byte-identical to the other copies listed in the Cmp Idle-enter section. | pattern scan |
| `0x7e14e0b3` | 21 | `cmp_enter_idle_7e14e0b3` | Cmp component Idle-state enter: thin wrapper → body `0x7e14e0bb`, which sets state 49 (Idle) at `+948` and `+256`, `+636 = 466`, `+632 = 0`, and logs `"Cmp_Play%s Idle"`. Byte-identical to the other copies listed in the Cmp Idle-enter section. | pattern scan |
| `0x7e161797` | 22 | `cmp_enter_idle_7e161797` | Cmp component Idle-state enter: thin wrapper → body `0x7e16179f`, which sets state 49 (Idle) at `+948` and `+256`, `+636 = 466`, `+632 = 0`, and logs `"Cmp_Play%s Idle"`. Byte-identical to the other copies listed in the Cmp Idle-enter section. | pattern scan |
| `0x7e19fea8` | 20 | `cmp_enter_idle_7e19fea8` | Cmp component Idle-state enter: thin wrapper → body `0x7e19feb0`, which sets state 49 (Idle) at `+948` and `+256`, `+636 = 466`, `+632 = 0`, and logs `"Cmp_Play%s Idle"`. Byte-identical to the other copies listed in the Cmp Idle-enter section. | pattern scan |
| `0x7e1a4854` | 20 | `cmp_enter_idle_7e1a4854` | Cmp component Idle-state enter: thin wrapper → body `0x7e1a485c`, which sets state 49 (Idle) at `+948` and `+256`, `+636 = 466`, `+632 = 0`, and logs `"Cmp_Play%s Idle"`. Byte-identical to the other copies listed in the Cmp Idle-enter section. | pattern scan |
| `0x7e1a7126` | 20 | `cmp_enter_idle_7e1a7126` | Cmp component Idle-state enter: thin wrapper → body `0x7e1a712e`, which sets state 49 (Idle) at `+948` and `+256`, `+636 = 466`, `+632 = 0`, and logs `"Cmp_Play%s Idle"`. Byte-identical to the other copies listed in the Cmp Idle-enter section. | pattern scan |
| `0x7e1bc122` | 20 | `cmp_enter_idle_7e1bc122` | Cmp component Idle-state enter: thin wrapper → body `0x7e1bc12a`, which sets state 49 (Idle) at `+948` and `+256`, `+636 = 466`, `+632 = 0`, and logs `"Cmp_Play%s Idle"`. Byte-identical to the other copies listed in the Cmp Idle-enter section. | pattern scan |
| `0x7e1c3ddf` | 20 | `cmp_enter_idle_7e1c3ddf` | Cmp component Idle-state enter: thin wrapper → body `0x7e1c3de7`, which sets state 49 (Idle) at `+948` and `+256`, `+636 = 466`, `+632 = 0`, and logs `"Cmp_Play%s Idle"`. Byte-identical to the other copies listed in the Cmp Idle-enter section. | pattern scan |

## Replicated small routines (pattern families)
Groups of byte-identical or same-shaped routines that every component or GUI class carries its own copy
of. Found on 2026-11-12 by grouping block-0 functions with identical bytes and by byte-pattern scans;
rows already in the main table keep their earlier names. Names are `<family>_<address>`.

| family | copies | newly listed here |
|---|---|---|
| `guiobj_vstub_ret_m1` | 255 | 255 |
| `obj_clear_f24` | 45 | 45 |
| `obj_clear_f252_f256` | 35 | 35 |
| `cmp_release_f560` | 31 | 31 |
| `cb_f4_call_u16` | 29 | 29 |
| `cb_f36_call` | 29 | 29 |
| `cmp_state_enter_<N>` | 723 | 723 |

`cmp_state_enter_<N>`: `mov N,d0; mov d0,(948,a0); call body; ret` — the per-state wrappers of the Cmp
component state machine ([[cmp-component-framework]]); `+948` is the state word (49 = Idle, see the Idle-enter
family). State numbers seen and how many components carry each: 11×28, 13×28, 16×28, 18×28, 20×28, 22×28, 24×28, 26×28, 28×28, 30×28, 32×28, 34×28, 36×28, 38×28, 40×28, 42×28, 44×28, 46×28, 50×23, 52×20, 53×1, 54×18, 55×2, 56×15, 57×1, 58×16, 59×1, 60×13, 61×4, 62×11, 63×3, 64×10, 65×4, 66×9, 67×2, 68×9, 69×3, 70×9, 71×2, 72×9, 73×1, 74×6, 75×4, 76×4, 77×2, 78×4, 79×2, 80×3, 81×1, 82×3, 84×2, 86×1, 88×1.

| address | xrefs | symbol | role | source |
|---|---|---|---|---|
| `0x7e22b7e3` | 1 | `guiobj_vstub_ret_m1_7e22b7e3` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e22d588` | 2 | `guiobj_vstub_ret_m1_7e22d588` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2300df` | 1 | `guiobj_vstub_ret_m1_7e2300df` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e230572` | 3 | `guiobj_vstub_ret_m1_7e230572` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2320ae` | 1 | `guiobj_vstub_ret_m1_7e2320ae` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e232885` | 1 | `guiobj_vstub_ret_m1_7e232885` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e232a7e` | 1 | `guiobj_vstub_ret_m1_7e232a7e` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e233344` | 1 | `guiobj_vstub_ret_m1_7e233344` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e23d25a` | 1 | `guiobj_vstub_ret_m1_7e23d25a` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e23d54c` | 1 | `guiobj_vstub_ret_m1_7e23d54c` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e25517b` | 1 | `guiobj_vstub_ret_m1_7e25517b` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e255db4` | 1 | `guiobj_vstub_ret_m1_7e255db4` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e255f7f` | 1 | `guiobj_vstub_ret_m1_7e255f7f` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2574bf` | 1 | `guiobj_vstub_ret_m1_7e2574bf` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2581c3` | 1 | `guiobj_vstub_ret_m1_7e2581c3` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e258e12` | 1 | `guiobj_vstub_ret_m1_7e258e12` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e258f1c` | 1 | `guiobj_vstub_ret_m1_7e258f1c` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2590f4` | 1 | `guiobj_vstub_ret_m1_7e2590f4` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2592c1` | 1 | `guiobj_vstub_ret_m1_7e2592c1` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e259575` | 1 | `guiobj_vstub_ret_m1_7e259575` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2596ba` | 1 | `guiobj_vstub_ret_m1_7e2596ba` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e259893` | 1 | `guiobj_vstub_ret_m1_7e259893` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2599c7` | 1 | `guiobj_vstub_ret_m1_7e2599c7` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e259bcb` | 1 | `guiobj_vstub_ret_m1_7e259bcb` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e259db2` | 1 | `guiobj_vstub_ret_m1_7e259db2` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e25a637` | 1 | `guiobj_vstub_ret_m1_7e25a637` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e25a8f0` | 1 | `guiobj_vstub_ret_m1_7e25a8f0` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e25aafc` | 1 | `guiobj_vstub_ret_m1_7e25aafc` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e25ad77` | 1 | `guiobj_vstub_ret_m1_7e25ad77` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e25b09f` | 1 | `guiobj_vstub_ret_m1_7e25b09f` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e25b262` | 1 | `guiobj_vstub_ret_m1_7e25b262` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e25b522` | 1 | `guiobj_vstub_ret_m1_7e25b522` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e25b698` | 1 | `guiobj_vstub_ret_m1_7e25b698` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e25baf7` | 1 | `guiobj_vstub_ret_m1_7e25baf7` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e25bc70` | 1 | `guiobj_vstub_ret_m1_7e25bc70` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e25ecd0` | 1 | `guiobj_vstub_ret_m1_7e25ecd0` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2607bd` | 1 | `guiobj_vstub_ret_m1_7e2607bd` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e26216a` | 1 | `guiobj_vstub_ret_m1_7e26216a` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e262a81` | 1 | `guiobj_vstub_ret_m1_7e262a81` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2638b1` | 1 | `guiobj_vstub_ret_m1_7e2638b1` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e263d7a` | 1 | `guiobj_vstub_ret_m1_7e263d7a` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e264940` | 1 | `guiobj_vstub_ret_m1_7e264940` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e264aa0` | 2 | `guiobj_vstub_ret_m1_7e264aa0` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e265c8d` | 1 | `guiobj_vstub_ret_m1_7e265c8d` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e265f99` | 1 | `guiobj_vstub_ret_m1_7e265f99` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e266133` | 1 | `guiobj_vstub_ret_m1_7e266133` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2661e8` | 1 | `guiobj_vstub_ret_m1_7e2661e8` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e266368` | 1 | `guiobj_vstub_ret_m1_7e266368` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2664c9` | 1 | `guiobj_vstub_ret_m1_7e2664c9` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e266580` | 1 | `guiobj_vstub_ret_m1_7e266580` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2666d6` | 1 | `guiobj_vstub_ret_m1_7e2666d6` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e267240` | 1 | `guiobj_vstub_ret_m1_7e267240` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e26931b` | 1 | `guiobj_vstub_ret_m1_7e26931b` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e272b56` | 1 | `guiobj_vstub_ret_m1_7e272b56` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e272ea5` | 1 | `guiobj_vstub_ret_m1_7e272ea5` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2733f3` | 1 | `guiobj_vstub_ret_m1_7e2733f3` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e273731` | 1 | `guiobj_vstub_ret_m1_7e273731` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e273dad` | 1 | `guiobj_vstub_ret_m1_7e273dad` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e273fdf` | 1 | `guiobj_vstub_ret_m1_7e273fdf` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2769a8` | 1 | `guiobj_vstub_ret_m1_7e2769a8` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e276d18` | 1 | `guiobj_vstub_ret_m1_7e276d18` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e277425` | 1 | `guiobj_vstub_ret_m1_7e277425` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e277a9d` | 1 | `guiobj_vstub_ret_m1_7e277a9d` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e277eb5` | 1 | `guiobj_vstub_ret_m1_7e277eb5` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2781b3` | 1 | `guiobj_vstub_ret_m1_7e2781b3` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2784ad` | 1 | `guiobj_vstub_ret_m1_7e2784ad` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27873d` | 1 | `guiobj_vstub_ret_m1_7e27873d` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2792fc` | 1 | `guiobj_vstub_ret_m1_7e2792fc` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27955e` | 1 | `guiobj_vstub_ret_m1_7e27955e` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e279cff` | 1 | `guiobj_vstub_ret_m1_7e279cff` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e279f27` | 1 | `guiobj_vstub_ret_m1_7e279f27` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27a158` | 1 | `guiobj_vstub_ret_m1_7e27a158` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27a632` | 1 | `guiobj_vstub_ret_m1_7e27a632` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27a957` | 1 | `guiobj_vstub_ret_m1_7e27a957` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27ac62` | 1 | `guiobj_vstub_ret_m1_7e27ac62` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27b013` | 1 | `guiobj_vstub_ret_m1_7e27b013` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27b27a` | 1 | `guiobj_vstub_ret_m1_7e27b27a` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27b693` | 1 | `guiobj_vstub_ret_m1_7e27b693` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27bafa` | 1 | `guiobj_vstub_ret_m1_7e27bafa` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27bd27` | 1 | `guiobj_vstub_ret_m1_7e27bd27` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27c043` | 1 | `guiobj_vstub_ret_m1_7e27c043` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27c298` | 1 | `guiobj_vstub_ret_m1_7e27c298` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27c9ce` | 1 | `guiobj_vstub_ret_m1_7e27c9ce` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27cc8b` | 1 | `guiobj_vstub_ret_m1_7e27cc8b` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27d077` | 1 | `guiobj_vstub_ret_m1_7e27d077` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27d8ad` | 1 | `guiobj_vstub_ret_m1_7e27d8ad` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27dc17` | 1 | `guiobj_vstub_ret_m1_7e27dc17` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27dfec` | 1 | `guiobj_vstub_ret_m1_7e27dfec` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27e625` | 1 | `guiobj_vstub_ret_m1_7e27e625` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27e9cf` | 1 | `guiobj_vstub_ret_m1_7e27e9cf` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27edd8` | 1 | `guiobj_vstub_ret_m1_7e27edd8` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e27f52c` | 1 | `guiobj_vstub_ret_m1_7e27f52c` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e280273` | 1 | `guiobj_vstub_ret_m1_7e280273` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2806c9` | 1 | `guiobj_vstub_ret_m1_7e2806c9` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2809ab` | 1 | `guiobj_vstub_ret_m1_7e2809ab` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e281844` | 1 | `guiobj_vstub_ret_m1_7e281844` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e281a7c` | 1 | `guiobj_vstub_ret_m1_7e281a7c` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e281d36` | 1 | `guiobj_vstub_ret_m1_7e281d36` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2821da` | 1 | `guiobj_vstub_ret_m1_7e2821da` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e282600` | 1 | `guiobj_vstub_ret_m1_7e282600` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e282958` | 1 | `guiobj_vstub_ret_m1_7e282958` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e282f1a` | 1 | `guiobj_vstub_ret_m1_7e282f1a` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e283442` | 1 | `guiobj_vstub_ret_m1_7e283442` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e283742` | 1 | `guiobj_vstub_ret_m1_7e283742` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e283a80` | 1 | `guiobj_vstub_ret_m1_7e283a80` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e284015` | 1 | `guiobj_vstub_ret_m1_7e284015` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2842bc` | 1 | `guiobj_vstub_ret_m1_7e2842bc` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e284a73` | 1 | `guiobj_vstub_ret_m1_7e284a73` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28512f` | 1 | `guiobj_vstub_ret_m1_7e28512f` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e285bac` | 1 | `guiobj_vstub_ret_m1_7e285bac` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2861d4` | 1 | `guiobj_vstub_ret_m1_7e2861d4` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2867e9` | 1 | `guiobj_vstub_ret_m1_7e2867e9` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e286d08` | 1 | `guiobj_vstub_ret_m1_7e286d08` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28715a` | 1 | `guiobj_vstub_ret_m1_7e28715a` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2873fc` | 1 | `guiobj_vstub_ret_m1_7e2873fc` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28774d` | 1 | `guiobj_vstub_ret_m1_7e28774d` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e287c3a` | 1 | `guiobj_vstub_ret_m1_7e287c3a` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e287edc` | 1 | `guiobj_vstub_ret_m1_7e287edc` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e288206` | 1 | `guiobj_vstub_ret_m1_7e288206` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28845e` | 1 | `guiobj_vstub_ret_m1_7e28845e` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2887d6` | 1 | `guiobj_vstub_ret_m1_7e2887d6` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e288a26` | 1 | `guiobj_vstub_ret_m1_7e288a26` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e288efb` | 1 | `guiobj_vstub_ret_m1_7e288efb` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e289107` | 1 | `guiobj_vstub_ret_m1_7e289107` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e289349` | 1 | `guiobj_vstub_ret_m1_7e289349` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e289777` | 1 | `guiobj_vstub_ret_m1_7e289777` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e289d3d` | 1 | `guiobj_vstub_ret_m1_7e289d3d` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28a268` | 1 | `guiobj_vstub_ret_m1_7e28a268` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28af36` | 1 | `guiobj_vstub_ret_m1_7e28af36` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28b4c5` | 1 | `guiobj_vstub_ret_m1_7e28b4c5` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28bd99` | 1 | `guiobj_vstub_ret_m1_7e28bd99` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28c407` | 1 | `guiobj_vstub_ret_m1_7e28c407` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28d2af` | 1 | `guiobj_vstub_ret_m1_7e28d2af` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28d6ea` | 1 | `guiobj_vstub_ret_m1_7e28d6ea` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28d9a6` | 1 | `guiobj_vstub_ret_m1_7e28d9a6` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28e04f` | 1 | `guiobj_vstub_ret_m1_7e28e04f` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28e2db` | 1 | `guiobj_vstub_ret_m1_7e28e2db` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28e370` | 1 | `guiobj_vstub_ret_m1_7e28e370` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28e5d6` | 1 | `guiobj_vstub_ret_m1_7e28e5d6` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28ec72` | 1 | `guiobj_vstub_ret_m1_7e28ec72` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28efd8` | 1 | `guiobj_vstub_ret_m1_7e28efd8` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28f9ca` | 1 | `guiobj_vstub_ret_m1_7e28f9ca` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e28fb96` | 1 | `guiobj_vstub_ret_m1_7e28fb96` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e29039d` | 1 | `guiobj_vstub_ret_m1_7e29039d` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e290c49` | 1 | `guiobj_vstub_ret_m1_7e290c49` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e29114b` | 1 | `guiobj_vstub_ret_m1_7e29114b` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2940f6` | 1 | `guiobj_vstub_ret_m1_7e2940f6` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e294752` | 1 | `guiobj_vstub_ret_m1_7e294752` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e294efd` | 1 | `guiobj_vstub_ret_m1_7e294efd` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2952db` | 1 | `guiobj_vstub_ret_m1_7e2952db` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e296116` | 1 | `guiobj_vstub_ret_m1_7e296116` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e297af7` | 1 | `guiobj_vstub_ret_m1_7e297af7` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e297ec7` | 1 | `guiobj_vstub_ret_m1_7e297ec7` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e29893d` | 1 | `guiobj_vstub_ret_m1_7e29893d` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e299323` | 1 | `guiobj_vstub_ret_m1_7e299323` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e299847` | 1 | `guiobj_vstub_ret_m1_7e299847` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e29a5f6` | 1 | `guiobj_vstub_ret_m1_7e29a5f6` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e29afd0` | 1 | `guiobj_vstub_ret_m1_7e29afd0` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e29bd46` | 1 | `guiobj_vstub_ret_m1_7e29bd46` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e29c2d2` | 1 | `guiobj_vstub_ret_m1_7e29c2d2` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e29c790` | 1 | `guiobj_vstub_ret_m1_7e29c790` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e29cc03` | 1 | `guiobj_vstub_ret_m1_7e29cc03` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e29e026` | 1 | `guiobj_vstub_ret_m1_7e29e026` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e29e9c6` | 1 | `guiobj_vstub_ret_m1_7e29e9c6` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2a17f0` | 1 | `guiobj_vstub_ret_m1_7e2a17f0` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2a5a90` | 1 | `guiobj_vstub_ret_m1_7e2a5a90` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2a8110` | 1 | `guiobj_vstub_ret_m1_7e2a8110` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2a9316` | 1 | `guiobj_vstub_ret_m1_7e2a9316` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2aa289` | 1 | `guiobj_vstub_ret_m1_7e2aa289` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2aa679` | 1 | `guiobj_vstub_ret_m1_7e2aa679` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2aa987` | 1 | `guiobj_vstub_ret_m1_7e2aa987` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2aadff` | 1 | `guiobj_vstub_ret_m1_7e2aadff` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2add04` | 1 | `guiobj_vstub_ret_m1_7e2add04` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2af487` | 1 | `guiobj_vstub_ret_m1_7e2af487` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2afab9` | 1 | `guiobj_vstub_ret_m1_7e2afab9` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b015c` | 1 | `guiobj_vstub_ret_m1_7e2b015c` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b05c3` | 1 | `guiobj_vstub_ret_m1_7e2b05c3` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b096c` | 1 | `guiobj_vstub_ret_m1_7e2b096c` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b0d5a` | 1 | `guiobj_vstub_ret_m1_7e2b0d5a` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b12fd` | 1 | `guiobj_vstub_ret_m1_7e2b12fd` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b16b0` | 1 | `guiobj_vstub_ret_m1_7e2b16b0` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b1ba8` | 1 | `guiobj_vstub_ret_m1_7e2b1ba8` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b1ffa` | 1 | `guiobj_vstub_ret_m1_7e2b1ffa` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b2e0b` | 1 | `guiobj_vstub_ret_m1_7e2b2e0b` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b36e8` | 1 | `guiobj_vstub_ret_m1_7e2b36e8` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b3ad5` | 1 | `guiobj_vstub_ret_m1_7e2b3ad5` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b3dee` | 1 | `guiobj_vstub_ret_m1_7e2b3dee` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b42c9` | 1 | `guiobj_vstub_ret_m1_7e2b42c9` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b4650` | 1 | `guiobj_vstub_ret_m1_7e2b4650` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b5f2a` | 1 | `guiobj_vstub_ret_m1_7e2b5f2a` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b6240` | 1 | `guiobj_vstub_ret_m1_7e2b6240` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b647c` | 1 | `guiobj_vstub_ret_m1_7e2b647c` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b67f3` | 1 | `guiobj_vstub_ret_m1_7e2b67f3` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b6f31` | 1 | `guiobj_vstub_ret_m1_7e2b6f31` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b7169` | 1 | `guiobj_vstub_ret_m1_7e2b7169` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b73c1` | 1 | `guiobj_vstub_ret_m1_7e2b73c1` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b74f6` | 1 | `guiobj_vstub_ret_m1_7e2b74f6` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b7e0d` | 1 | `guiobj_vstub_ret_m1_7e2b7e0d` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b8817` | 1 | `guiobj_vstub_ret_m1_7e2b8817` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b8b74` | 1 | `guiobj_vstub_ret_m1_7e2b8b74` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b90ed` | 1 | `guiobj_vstub_ret_m1_7e2b90ed` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b939a` | 1 | `guiobj_vstub_ret_m1_7e2b939a` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b96b5` | 1 | `guiobj_vstub_ret_m1_7e2b96b5` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b9a0e` | 1 | `guiobj_vstub_ret_m1_7e2b9a0e` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b9d29` | 1 | `guiobj_vstub_ret_m1_7e2b9d29` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2b9f09` | 1 | `guiobj_vstub_ret_m1_7e2b9f09` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2ba130` | 1 | `guiobj_vstub_ret_m1_7e2ba130` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2ba310` | 1 | `guiobj_vstub_ret_m1_7e2ba310` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2ba592` | 1 | `guiobj_vstub_ret_m1_7e2ba592` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bad4d` | 1 | `guiobj_vstub_ret_m1_7e2bad4d` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2baf65` | 1 | `guiobj_vstub_ret_m1_7e2baf65` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bb288` | 1 | `guiobj_vstub_ret_m1_7e2bb288` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bb56a` | 1 | `guiobj_vstub_ret_m1_7e2bb56a` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bb756` | 1 | `guiobj_vstub_ret_m1_7e2bb756` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bb8c7` | 1 | `guiobj_vstub_ret_m1_7e2bb8c7` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bbdcc` | 1 | `guiobj_vstub_ret_m1_7e2bbdcc` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bc003` | 1 | `guiobj_vstub_ret_m1_7e2bc003` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bc4ca` | 1 | `guiobj_vstub_ret_m1_7e2bc4ca` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bc63b` | 1 | `guiobj_vstub_ret_m1_7e2bc63b` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bc8c0` | 1 | `guiobj_vstub_ret_m1_7e2bc8c0` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bcc8d` | 1 | `guiobj_vstub_ret_m1_7e2bcc8d` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bd2b5` | 1 | `guiobj_vstub_ret_m1_7e2bd2b5` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bd426` | 1 | `guiobj_vstub_ret_m1_7e2bd426` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bd634` | 1 | `guiobj_vstub_ret_m1_7e2bd634` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bd90e` | 1 | `guiobj_vstub_ret_m1_7e2bd90e` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bddd4` | 1 | `guiobj_vstub_ret_m1_7e2bddd4` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2be085` | 1 | `guiobj_vstub_ret_m1_7e2be085` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2be29a` | 1 | `guiobj_vstub_ret_m1_7e2be29a` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2be773` | 1 | `guiobj_vstub_ret_m1_7e2be773` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bea02` | 1 | `guiobj_vstub_ret_m1_7e2bea02` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bebf9` | 1 | `guiobj_vstub_ret_m1_7e2bebf9` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bedf3` | 1 | `guiobj_vstub_ret_m1_7e2bedf3` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bf07c` | 1 | `guiobj_vstub_ret_m1_7e2bf07c` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bf305` | 1 | `guiobj_vstub_ret_m1_7e2bf305` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bf9fb` | 1 | `guiobj_vstub_ret_m1_7e2bf9fb` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bfc0d` | 1 | `guiobj_vstub_ret_m1_7e2bfc0d` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2bff90` | 1 | `guiobj_vstub_ret_m1_7e2bff90` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c0582` | 1 | `guiobj_vstub_ret_m1_7e2c0582` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c07be` | 1 | `guiobj_vstub_ret_m1_7e2c07be` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c09b0` | 1 | `guiobj_vstub_ret_m1_7e2c09b0` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c0c56` | 1 | `guiobj_vstub_ret_m1_7e2c0c56` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c0dc7` | 1 | `guiobj_vstub_ret_m1_7e2c0dc7` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c1074` | 1 | `guiobj_vstub_ret_m1_7e2c1074` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c11e5` | 1 | `guiobj_vstub_ret_m1_7e2c11e5` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c16ea` | 1 | `guiobj_vstub_ret_m1_7e2c16ea` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c1921` | 1 | `guiobj_vstub_ret_m1_7e2c1921` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c1dd2` | 1 | `guiobj_vstub_ret_m1_7e2c1dd2` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c1f43` | 1 | `guiobj_vstub_ret_m1_7e2c1f43` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c2189` | 1 | `guiobj_vstub_ret_m1_7e2c2189` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c2556` | 1 | `guiobj_vstub_ret_m1_7e2c2556` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c2b7e` | 1 | `guiobj_vstub_ret_m1_7e2c2b7e` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c2e19` | 1 | `guiobj_vstub_ret_m1_7e2c2e19` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c3091` | 1 | `guiobj_vstub_ret_m1_7e2c3091` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c3485` | 1 | `guiobj_vstub_ret_m1_7e2c3485` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e2c3fa1` | 1 | `guiobj_vstub_ret_m1_7e2c3fa1` | Virtual stub that ignores its arguments and returns −1 (it compares `(u16)d0` with 6399 but both paths return −1): the "not handled" default for one vtable slot, copied into each GUI class. | pattern scan |
| `0x7e07e4d7` | 1 | `obj_clear_f24_7e07e4d7` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e08ef5f` | 1 | `obj_clear_f24_7e08ef5f` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e08eff2` | 1 | `obj_clear_f24_7e08eff2` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e08f085` | 1 | `obj_clear_f24_7e08f085` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e08f118` | 1 | `obj_clear_f24_7e08f118` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e08f277` | 1 | `obj_clear_f24_7e08f277` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e08f30f` | 1 | `obj_clear_f24_7e08f30f` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e08f3a2` | 1 | `obj_clear_f24_7e08f3a2` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e08f435` | 1 | `obj_clear_f24_7e08f435` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e08f4c8` | 1 | `obj_clear_f24_7e08f4c8` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e08f72f` | 1 | `obj_clear_f24_7e08f72f` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e08f7c2` | 1 | `obj_clear_f24_7e08f7c2` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0abcb8` | 1 | `obj_clear_f24_7e0abcb8` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0b4e3b` | 1 | `obj_clear_f24_7e0b4e3b` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0b4f00` | 1 | `obj_clear_f24_7e0b4f00` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0b4fc5` | 1 | `obj_clear_f24_7e0b4fc5` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0b6db9` | 1 | `obj_clear_f24_7e0b6db9` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0b6e54` | 1 | `obj_clear_f24_7e0b6e54` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0b6eb0` | 1 | `obj_clear_f24_7e0b6eb0` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0b9f6f` | 1 | `obj_clear_f24_7e0b9f6f` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0b9fd8` | 1 | `obj_clear_f24_7e0b9fd8` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0ba041` | 1 | `obj_clear_f24_7e0ba041` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0ba5d3` | 1 | `obj_clear_f24_7e0ba5d3` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0ba63c` | 1 | `obj_clear_f24_7e0ba63c` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0c79d8` | 1 | `obj_clear_f24_7e0c79d8` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0c7a8e` | 1 | `obj_clear_f24_7e0c7a8e` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0c7b17` | 1 | `obj_clear_f24_7e0c7b17` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0c7c7b` | 1 | `obj_clear_f24_7e0c7c7b` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0c7e48` | 1 | `obj_clear_f24_7e0c7e48` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0c7e8b` | 1 | `obj_clear_f24_7e0c7e8b` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0c7ece` | 1 | `obj_clear_f24_7e0c7ece` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0c7f57` | 1 | `obj_clear_f24_7e0c7f57` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0c7f9a` | 1 | `obj_clear_f24_7e0c7f9a` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0c8023` | 1 | `obj_clear_f24_7e0c8023` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0c80ac` | 1 | `obj_clear_f24_7e0c80ac` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0c81c1` | 1 | `obj_clear_f24_7e0c81c1` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0c82d6` | 1 | `obj_clear_f24_7e0c82d6` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0dbf27` | 1 | `obj_clear_f24_7e0dbf27` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0e8ea6` | 1 | `obj_clear_f24_7e0e8ea6` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e17af77` | 1 | `obj_clear_f24_7e17af77` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e1f08a3` | 1 | `obj_clear_f24_7e1f08a3` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e1f3900` | 1 | `obj_clear_f24_7e1f3900` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e204e11` | 1 | `obj_clear_f24_7e204e11` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e204e67` | 1 | `obj_clear_f24_7e204e67` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e2050d6` | 1 | `obj_clear_f24_7e2050d6` | `if (*(this+24) != 0) *(this+24) = 0`. | pattern scan |
| `0x7e0575dd` | 1 | `obj_clear_f252_f256_7e0575dd` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e058525` | 1 | `obj_clear_f252_f256_7e058525` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e058b12` | 1 | `obj_clear_f252_f256_7e058b12` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e05984d` | 1 | `obj_clear_f252_f256_7e05984d` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e07bac1` | 1 | `obj_clear_f252_f256_7e07bac1` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e07e945` | 1 | `obj_clear_f252_f256_7e07e945` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e07f0fc` | 1 | `obj_clear_f252_f256_7e07f0fc` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e083d49` | 1 | `obj_clear_f252_f256_7e083d49` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e08b2d0` | 1 | `obj_clear_f252_f256_7e08b2d0` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e08e795` | 1 | `obj_clear_f252_f256_7e08e795` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e097934` | 1 | `obj_clear_f252_f256_7e097934` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e098c98` | 1 | `obj_clear_f252_f256_7e098c98` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e09acfc` | 1 | `obj_clear_f252_f256_7e09acfc` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e09bbbf` | 1 | `obj_clear_f252_f256_7e09bbbf` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e09f71b` | 1 | `obj_clear_f252_f256_7e09f71b` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e0a0257` | 1 | `obj_clear_f252_f256_7e0a0257` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e0a275f` | 1 | `obj_clear_f252_f256_7e0a275f` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e0a348a` | 1 | `obj_clear_f252_f256_7e0a348a` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e0a3883` | 1 | `obj_clear_f252_f256_7e0a3883` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e0a44a9` | 1 | `obj_clear_f252_f256_7e0a44a9` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e0a4921` | 1 | `obj_clear_f252_f256_7e0a4921` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e0a7fe4` | 1 | `obj_clear_f252_f256_7e0a7fe4` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e0a9d58` | 1 | `obj_clear_f252_f256_7e0a9d58` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e0ab559` | 1 | `obj_clear_f252_f256_7e0ab559` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e0b1d86` | 1 | `obj_clear_f252_f256_7e0b1d86` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e0b21a5` | 1 | `obj_clear_f252_f256_7e0b21a5` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e0b5dbe` | 1 | `obj_clear_f252_f256_7e0b5dbe` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e0cae94` | 1 | `obj_clear_f252_f256_7e0cae94` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e0ccc44` | 1 | `obj_clear_f252_f256_7e0ccc44` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e1e8a9e` | 1 | `obj_clear_f252_f256_7e1e8a9e` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e1e8e75` | 1 | `obj_clear_f252_f256_7e1e8e75` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e1e92cc` | 1 | `obj_clear_f252_f256_7e1e92cc` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e1e974b` | 1 | `obj_clear_f252_f256_7e1e974b` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e1e9c2a` | 1 | `obj_clear_f252_f256_7e1e9c2a` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e1ea193` | 1 | `obj_clear_f252_f256_7e1ea193` | `*(this+252) = 0; *(this+256) = 0`. | pattern scan |
| `0x7e0e68e1` | 1 | `cmp_release_f560_7e0e68e1` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e1261b3` | 3 | `cmp_release_f560_7e1261b3` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e130366` | 3 | `cmp_release_f560_7e130366` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e1412f9` | 3 | `cmp_release_f560_7e1412f9` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e1493f8` | 3 | `cmp_release_f560_7e1493f8` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e14c5d8` | 3 | `cmp_release_f560_7e14c5d8` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e14ec9b` | 3 | `cmp_release_f560_7e14ec9b` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e1527b9` | 3 | `cmp_release_f560_7e1527b9` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e156fa4` | 3 | `cmp_release_f560_7e156fa4` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e15b882` | 3 | `cmp_release_f560_7e15b882` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e160040` | 3 | `cmp_release_f560_7e160040` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e1638f5` | 3 | `cmp_release_f560_7e1638f5` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e167502` | 3 | `cmp_release_f560_7e167502` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e16ae7e` | 3 | `cmp_release_f560_7e16ae7e` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e16e3c3` | 3 | `cmp_release_f560_7e16e3c3` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e170cc0` | 3 | `cmp_release_f560_7e170cc0` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e175aa4` | 3 | `cmp_release_f560_7e175aa4` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e179886` | 3 | `cmp_release_f560_7e179886` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e17ca87` | 3 | `cmp_release_f560_7e17ca87` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e18d82c` | 3 | `cmp_release_f560_7e18d82c` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e1a0ab9` | 3 | `cmp_release_f560_7e1a0ab9` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e1a8849` | 3 | `cmp_release_f560_7e1a8849` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e1ad5f0` | 3 | `cmp_release_f560_7e1ad5f0` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e1b1675` | 3 | `cmp_release_f560_7e1b1675` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e1b5aa8` | 3 | `cmp_release_f560_7e1b5aa8` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e1be6e2` | 3 | `cmp_release_f560_7e1be6e2` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e1c28c3` | 3 | `cmp_release_f560_7e1c28c3` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e1c5bc7` | 3 | `cmp_release_f560_7e1c5bc7` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e1c9b32` | 3 | `cmp_release_f560_7e1c9b32` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e1cf3c9` | 4 | `cmp_release_f560_7e1cf3c9` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7e1cf587` | 4 | `cmp_release_f560_7e1cf587` | If the pointer at `+560` is set, calls that object's vtable slot `+44` and clears the field. Release of the registered object that `cmp_clear_f560_if_eq` compares against. | pattern scan |
| `0x7dacfe23` | 1 | `cb_f4_call_u16_7dacfe23` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db266ff` | 1 | `cb_f4_call_u16_7db266ff` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db26723` | 1 | `cb_f4_call_u16_7db26723` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db26868` | 1 | `cb_f4_call_u16_7db26868` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db26c60` | 1 | `cb_f4_call_u16_7db26c60` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db26d7f` | 1 | `cb_f4_call_u16_7db26d7f` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db26e88` | 1 | `cb_f4_call_u16_7db26e88` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db26efe` | 1 | `cb_f4_call_u16_7db26efe` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db26f74` | 1 | `cb_f4_call_u16_7db26f74` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db27038` | 1 | `cb_f4_call_u16_7db27038` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db27077` | 1 | `cb_f4_call_u16_7db27077` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db270ed` | 1 | `cb_f4_call_u16_7db270ed` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db27163` | 1 | `cb_f4_call_u16_7db27163` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db27189` | 1 | `cb_f4_call_u16_7db27189` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db271ff` | 1 | `cb_f4_call_u16_7db271ff` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db27275` | 1 | `cb_f4_call_u16_7db27275` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db2729b` | 1 | `cb_f4_call_u16_7db2729b` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db272db` | 1 | `cb_f4_call_u16_7db272db` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db274c1` | 1 | `cb_f4_call_u16_7db274c1` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db27557` | 1 | `cb_f4_call_u16_7db27557` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db275d7` | 1 | `cb_f4_call_u16_7db275d7` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db27670` | 1 | `cb_f4_call_u16_7db27670` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db276bf` | 1 | `cb_f4_call_u16_7db276bf` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db277ac` | 1 | `cb_f4_call_u16_7db277ac` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db27844` | 1 | `cb_f4_call_u16_7db27844` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db279c8` | 1 | `cb_f4_call_u16_7db279c8` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db27a4c` | 1 | `cb_f4_call_u16_7db27a4c` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db27e21` | 1 | `cb_f4_call_u16_7db27e21` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db27e47` | 1 | `cb_f4_call_u16_7db27e47` | If the function pointer at `this+4` is set, calls it with `(u16)d0`. | pattern scan |
| `0x7db2ee93` | 0 | `cb_f36_call_7db2ee93` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2ef1f` | 0 | `cb_f36_call_7db2ef1f` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2efdb` | 0 | `cb_f36_call_7db2efdb` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f067` | 0 | `cb_f36_call_7db2f067` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f0f3` | 0 | `cb_f36_call_7db2f0f3` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f216` | 0 | `cb_f36_call_7db2f216` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f277` | 0 | `cb_f36_call_7db2f277` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f2bd` | 0 | `cb_f36_call_7db2f2bd` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f303` | 0 | `cb_f36_call_7db2f303` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f348` | 0 | `cb_f36_call_7db2f348` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f38d` | 0 | `cb_f36_call_7db2f38d` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f3d2` | 0 | `cb_f36_call_7db2f3d2` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f417` | 0 | `cb_f36_call_7db2f417` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f45c` | 1 | `cb_f36_call_7db2f45c` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f4a1` | 1 | `cb_f36_call_7db2f4a1` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f4e6` | 1 | `cb_f36_call_7db2f4e6` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f5b4` | 2 | `cb_f36_call_7db2f5b4` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f5f9` | 1 | `cb_f36_call_7db2f5f9` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f63b` | 1 | `cb_f36_call_7db2f63b` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f67d` | 1 | `cb_f36_call_7db2f67d` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f6a3` | 1 | `cb_f36_call_7db2f6a3` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f771` | 2 | `cb_f36_call_7db2f771` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f86a` | 2 | `cb_f36_call_7db2f86a` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f8ec` | 1 | `cb_f36_call_7db2f8ec` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f931` | 1 | `cb_f36_call_7db2f931` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f973` | 1 | `cb_f36_call_7db2f973` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f9b5` | 1 | `cb_f36_call_7db2f9b5` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2f9f7` | 1 | `cb_f36_call_7db2f9f7` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7db2fa39` | 1 | `cb_f36_call_7db2fa39` | Calls the function pointer at `this+36` with `(u16)d0` and `d1 = *(this) & 3`. | pattern scan |
| `0x7e126b00` | 1 | `cmp_state_enter_11_7e126b00` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e126b55`. | pattern scan |
| `0x7e126bac` | 1 | `cmp_state_enter_50_7e126bac` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e126c01`. | pattern scan |
| `0x7e126d77` | 1 | `cmp_state_enter_13_7e126d77` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e126dcc`. | pattern scan |
| `0x7e126fff` | 1 | `cmp_state_enter_16_7e126fff` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e127054`. | pattern scan |
| `0x7e127078` | 1 | `cmp_state_enter_18_7e127078` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e1270cd`. | pattern scan |
| `0x7e1270f1` | 1 | `cmp_state_enter_20_7e1270f1` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e127146`. | pattern scan |
| `0x7e12716a` | 1 | `cmp_state_enter_22_7e12716a` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e1271bf`. | pattern scan |
| `0x7e1271e3` | 1 | `cmp_state_enter_24_7e1271e3` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e127238`. | pattern scan |
| `0x7e12725c` | 1 | `cmp_state_enter_26_7e12725c` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e1272b1`. | pattern scan |
| `0x7e1272d5` | 1 | `cmp_state_enter_28_7e1272d5` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e12732a`. | pattern scan |
| `0x7e12734e` | 1 | `cmp_state_enter_30_7e12734e` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e1273a3`. | pattern scan |
| `0x7e1273c7` | 1 | `cmp_state_enter_32_7e1273c7` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e12741c`. | pattern scan |
| `0x7e127440` | 1 | `cmp_state_enter_34_7e127440` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e127495`. | pattern scan |
| `0x7e1274b9` | 1 | `cmp_state_enter_36_7e1274b9` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e12750e`. | pattern scan |
| `0x7e127604` | 1 | `cmp_state_enter_38_7e127604` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e127659`. | pattern scan |
| `0x7e12767d` | 1 | `cmp_state_enter_52_7e12767d` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e1276d2`. | pattern scan |
| `0x7e12799d` | 1 | `cmp_state_enter_40_7e12799d` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e1279f2`. | pattern scan |
| `0x7e127a16` | 1 | `cmp_state_enter_42_7e127a16` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e127a79`. | pattern scan |
| `0x7e127a9d` | 1 | `cmp_state_enter_44_7e127a9d` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e127af2`. | pattern scan |
| `0x7e127b16` | 1 | `cmp_state_enter_46_7e127b16` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e127b6b`. | pattern scan |
| `0x7e149d4d` | 1 | `cmp_state_enter_11_7e149d4d` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e149da2`. | pattern scan |
| `0x7e149df9` | 1 | `cmp_state_enter_13_7e149df9` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e149e4e`. | pattern scan |
| `0x7e14a099` | 1 | `cmp_state_enter_16_7e14a099` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e14a0ee`. | pattern scan |
| `0x7e14a112` | 1 | `cmp_state_enter_18_7e14a112` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e14a167`. | pattern scan |
| `0x7e14a18b` | 1 | `cmp_state_enter_20_7e14a18b` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e14a1e0`. | pattern scan |
| `0x7e14a204` | 1 | `cmp_state_enter_22_7e14a204` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e14a259`. | pattern scan |
| `0x7e14a27d` | 1 | `cmp_state_enter_24_7e14a27d` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e14a2d2`. | pattern scan |
| `0x7e14a2f6` | 1 | `cmp_state_enter_26_7e14a2f6` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e14a34b`. | pattern scan |
| `0x7e14a36f` | 1 | `cmp_state_enter_28_7e14a36f` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e14a3c4`. | pattern scan |
| `0x7e14a3e8` | 1 | `cmp_state_enter_30_7e14a3e8` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e14a43d`. | pattern scan |
| `0x7e14a461` | 1 | `cmp_state_enter_32_7e14a461` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e14a4b6`. | pattern scan |
| `0x7e14a4da` | 1 | `cmp_state_enter_34_7e14a4da` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e14a52f`. | pattern scan |
| `0x7e14a553` | 1 | `cmp_state_enter_36_7e14a553` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e14a5a8`. | pattern scan |
| `0x7e14a69e` | 1 | `cmp_state_enter_38_7e14a69e` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e14a6f3`. | pattern scan |
| `0x7e14a717` | 1 | `cmp_state_enter_40_7e14a717` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e14a76c`. | pattern scan |
| `0x7e14a790` | 1 | `cmp_state_enter_42_7e14a790` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e14a7f3`. | pattern scan |
| `0x7e14a817` | 1 | `cmp_state_enter_44_7e14a817` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e14a86c`. | pattern scan |
| `0x7e14a890` | 1 | `cmp_state_enter_46_7e14a890` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e14a8e5`. | pattern scan |
| `0x7e14a96e` | 1 | `cmp_state_enter_50_7e14a96e` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e14a9c3`. | pattern scan |
| `0x7e14aad1` | 1 | `cmp_state_enter_52_7e14aad1` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e14ab26`. | pattern scan |
| `0x7e14ae11` | 1 | `cmp_state_enter_54_7e14ae11` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e14ae66`. | pattern scan |
| `0x7e14cf1d` | 1 | `cmp_state_enter_11_7e14cf1d` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e14cf72`. | pattern scan |
| `0x7e14cfc9` | 1 | `cmp_state_enter_50_7e14cfc9` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e14d0a8`. | pattern scan |
| `0x7e14d56a` | 1 | `cmp_state_enter_13_7e14d56a` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e14d5bf`. | pattern scan |
| `0x7e14d7de` | 1 | `cmp_state_enter_16_7e14d7de` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e14d833`. | pattern scan |
| `0x7e14d857` | 1 | `cmp_state_enter_18_7e14d857` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e14d8ac`. | pattern scan |
| `0x7e14d8d0` | 1 | `cmp_state_enter_20_7e14d8d0` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e14d925`. | pattern scan |
| `0x7e14d949` | 1 | `cmp_state_enter_22_7e14d949` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e14d99e`. | pattern scan |
| `0x7e14d9c2` | 1 | `cmp_state_enter_24_7e14d9c2` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e14da17`. | pattern scan |
| `0x7e14da3b` | 1 | `cmp_state_enter_26_7e14da3b` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e14da90`. | pattern scan |
| `0x7e14dab4` | 1 | `cmp_state_enter_28_7e14dab4` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e14db09`. | pattern scan |
| `0x7e14db2d` | 1 | `cmp_state_enter_30_7e14db2d` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e14db82`. | pattern scan |
| `0x7e14dba6` | 1 | `cmp_state_enter_32_7e14dba6` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e14dbfb`. | pattern scan |
| `0x7e14dc1f` | 1 | `cmp_state_enter_34_7e14dc1f` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e14dc74`. | pattern scan |
| `0x7e14dc98` | 1 | `cmp_state_enter_36_7e14dc98` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e14dced`. | pattern scan |
| `0x7e14dde3` | 1 | `cmp_state_enter_38_7e14dde3` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e14de38`. | pattern scan |
| `0x7e14de5c` | 1 | `cmp_state_enter_40_7e14de5c` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e14deb1`. | pattern scan |
| `0x7e14ded5` | 1 | `cmp_state_enter_42_7e14ded5` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e14df38`. | pattern scan |
| `0x7e14df5c` | 1 | `cmp_state_enter_44_7e14df5c` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e14dfb1`. | pattern scan |
| `0x7e14dfd5` | 1 | `cmp_state_enter_46_7e14dfd5` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e14e02a`. | pattern scan |
| `0x7e14f617` | 1 | `cmp_state_enter_11_7e14f617` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e14f66c`. | pattern scan |
| `0x7e14f6c3` | 1 | `cmp_state_enter_50_7e14f6c3` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e14f718`. | pattern scan |
| `0x7e14f7e6` | 1 | `cmp_state_enter_13_7e14f7e6` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e14f83b`. | pattern scan |
| `0x7e14f85f` | 1 | `cmp_state_enter_52_7e14f85f` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e14f8b4`. | pattern scan |
| `0x7e14fdee` | 1 | `cmp_state_enter_54_7e14fdee` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e14fe43`. | pattern scan |
| `0x7e150017` | 1 | `cmp_state_enter_16_7e150017` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e15006c`. | pattern scan |
| `0x7e150090` | 1 | `cmp_state_enter_18_7e150090` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e1500e5`. | pattern scan |
| `0x7e150109` | 1 | `cmp_state_enter_20_7e150109` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e15015e`. | pattern scan |
| `0x7e150182` | 1 | `cmp_state_enter_22_7e150182` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e1501d7`. | pattern scan |
| `0x7e1501fb` | 1 | `cmp_state_enter_24_7e1501fb` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e150250`. | pattern scan |
| `0x7e150274` | 1 | `cmp_state_enter_26_7e150274` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e1502c9`. | pattern scan |
| `0x7e1502ed` | 1 | `cmp_state_enter_28_7e1502ed` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e150342`. | pattern scan |
| `0x7e150366` | 1 | `cmp_state_enter_30_7e150366` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e1503bb`. | pattern scan |
| `0x7e1503df` | 1 | `cmp_state_enter_32_7e1503df` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e150434`. | pattern scan |
| `0x7e150458` | 1 | `cmp_state_enter_34_7e150458` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e1504ad`. | pattern scan |
| `0x7e1504d1` | 1 | `cmp_state_enter_56_7e1504d1` | Cmp state-enter wrapper: sets the state word `+948 = 56`, then calls the state's body `0x7e150526`. | pattern scan |
| `0x7e1508c3` | 1 | `cmp_state_enter_36_7e1508c3` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e150918`. | pattern scan |
| `0x7e150a0e` | 1 | `cmp_state_enter_38_7e150a0e` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e150a63`. | pattern scan |
| `0x7e150a87` | 1 | `cmp_state_enter_58_7e150a87` | Cmp state-enter wrapper: sets the state word `+948 = 58`, then calls the state's body `0x7e150adc`. | pattern scan |
| `0x7e150bc2` | 1 | `cmp_state_enter_40_7e150bc2` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e150c17`. | pattern scan |
| `0x7e150c3b` | 1 | `cmp_state_enter_42_7e150c3b` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e150c9e`. | pattern scan |
| `0x7e150cc2` | 1 | `cmp_state_enter_60_7e150cc2` | Cmp state-enter wrapper: sets the state word `+948 = 60`, then calls the state's body `0x7e150d17`. | pattern scan |
| `0x7e150e37` | 1 | `cmp_state_enter_44_7e150e37` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e150e8c`. | pattern scan |
| `0x7e150eb0` | 1 | `cmp_state_enter_46_7e150eb0` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e150f05`. | pattern scan |
| `0x7e150f29` | 1 | `cmp_state_enter_62_7e150f29` | Cmp state-enter wrapper: sets the state word `+948 = 62`, then calls the state's body `0x7e150f7e`. | pattern scan |
| `0x7e151248` | 1 | `cmp_state_enter_64_7e151248` | Cmp state-enter wrapper: sets the state word `+948 = 64`, then calls the state's body `0x7e15129d`. | pattern scan |
| `0x7e153196` | 1 | `cmp_state_enter_11_7e153196` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e1531eb`. | pattern scan |
| `0x7e153242` | 1 | `cmp_state_enter_50_7e153242` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e153297`. | pattern scan |
| `0x7e15335a` | 1 | `cmp_state_enter_52_7e15335a` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e1533af`. | pattern scan |
| `0x7e153628` | 1 | `cmp_state_enter_54_7e153628` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e15367d`. | pattern scan |
| `0x7e153752` | 1 | `cmp_state_enter_56_7e153752` | Cmp state-enter wrapper: sets the state word `+948 = 56`, then calls the state's body `0x7e1537a7`. | pattern scan |
| `0x7e15395f` | 1 | `cmp_state_enter_58_7e15395f` | Cmp state-enter wrapper: sets the state word `+948 = 58`, then calls the state's body `0x7e1539b4`. | pattern scan |
| `0x7e153a62` | 1 | `cmp_state_enter_13_7e153a62` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e153ab7`. | pattern scan |
| `0x7e153adb` | 1 | `cmp_state_enter_60_7e153adb` | Cmp state-enter wrapper: sets the state word `+948 = 60`, then calls the state's body `0x7e153b30`. | pattern scan |
| `0x7e153cb4` | 1 | `cmp_state_enter_62_7e153cb4` | Cmp state-enter wrapper: sets the state word `+948 = 62`, then calls the state's body `0x7e153d09`. | pattern scan |
| `0x7e153f71` | 1 | `cmp_state_enter_64_7e153f71` | Cmp state-enter wrapper: sets the state word `+948 = 64`, then calls the state's body `0x7e153fc6`. | pattern scan |
| `0x7e15457f` | 1 | `cmp_state_enter_66_7e15457f` | Cmp state-enter wrapper: sets the state word `+948 = 66`, then calls the state's body `0x7e1545d4`. | pattern scan |
| `0x7e1546b0` | 1 | `cmp_state_enter_68_7e1546b0` | Cmp state-enter wrapper: sets the state word `+948 = 68`, then calls the state's body `0x7e154705`. | pattern scan |
| `0x7e1548aa` | 1 | `cmp_state_enter_16_7e1548aa` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e1548ff`. | pattern scan |
| `0x7e154923` | 1 | `cmp_state_enter_18_7e154923` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e154978`. | pattern scan |
| `0x7e15499c` | 1 | `cmp_state_enter_20_7e15499c` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e1549f1`. | pattern scan |
| `0x7e154a15` | 1 | `cmp_state_enter_70_7e154a15` | Cmp state-enter wrapper: sets the state word `+948 = 70`, then calls the state's body `0x7e154a6a`. | pattern scan |
| `0x7e154b1a` | 1 | `cmp_state_enter_22_7e154b1a` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e154b6f`. | pattern scan |
| `0x7e154b93` | 1 | `cmp_state_enter_24_7e154b93` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e154be8`. | pattern scan |
| `0x7e154c0c` | 1 | `cmp_state_enter_72_7e154c0c` | Cmp state-enter wrapper: sets the state word `+948 = 72`, then calls the state's body `0x7e154c61`. | pattern scan |
| `0x7e154d22` | 1 | `cmp_state_enter_26_7e154d22` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e154d77`. | pattern scan |
| `0x7e154d9b` | 1 | `cmp_state_enter_28_7e154d9b` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e154df0`. | pattern scan |
| `0x7e154e14` | 1 | `cmp_state_enter_30_7e154e14` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e154e69`. | pattern scan |
| `0x7e154e8d` | 1 | `cmp_state_enter_32_7e154e8d` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e154ee2`. | pattern scan |
| `0x7e154f06` | 1 | `cmp_state_enter_34_7e154f06` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e154f5b`. | pattern scan |
| `0x7e154f7f` | 1 | `cmp_state_enter_74_7e154f7f` | Cmp state-enter wrapper: sets the state word `+948 = 74`, then calls the state's body `0x7e154fd4`. | pattern scan |
| `0x7e155177` | 1 | `cmp_state_enter_76_7e155177` | Cmp state-enter wrapper: sets the state word `+948 = 76`, then calls the state's body `0x7e1551cc`. | pattern scan |
| `0x7e15528d` | 1 | `cmp_state_enter_78_7e15528d` | Cmp state-enter wrapper: sets the state word `+948 = 78`, then calls the state's body `0x7e1552e2`. | pattern scan |
| `0x7e1554a5` | 1 | `cmp_state_enter_36_7e1554a5` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e1554fa`. | pattern scan |
| `0x7e1555f0` | 1 | `cmp_state_enter_38_7e1555f0` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e155645`. | pattern scan |
| `0x7e155669` | 1 | `cmp_state_enter_80_7e155669` | Cmp state-enter wrapper: sets the state word `+948 = 80`, then calls the state's body `0x7e1556be`. | pattern scan |
| `0x7e15577b` | 1 | `cmp_state_enter_40_7e15577b` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e1557d0`. | pattern scan |
| `0x7e1557f4` | 1 | `cmp_state_enter_42_7e1557f4` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e155857`. | pattern scan |
| `0x7e15587b` | 1 | `cmp_state_enter_44_7e15587b` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e1558d0`. | pattern scan |
| `0x7e1558f4` | 1 | `cmp_state_enter_46_7e1558f4` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e155949`. | pattern scan |
| `0x7e15596d` | 1 | `cmp_state_enter_82_7e15596d` | Cmp state-enter wrapper: sets the state word `+948 = 82`, then calls the state's body `0x7e1559c2`. | pattern scan |
| `0x7e155a94` | 1 | `cmp_state_enter_84_7e155a94` | Cmp state-enter wrapper: sets the state word `+948 = 84`, then calls the state's body `0x7e155ae9`. | pattern scan |
| `0x7e155e09` | 1 | `cmp_state_enter_86_7e155e09` | Cmp state-enter wrapper: sets the state word `+948 = 86`, then calls the state's body `0x7e155e5e`. | pattern scan |
| `0x7e155f7d` | 1 | `cmp_state_enter_88_7e155f7d` | Cmp state-enter wrapper: sets the state word `+948 = 88`, then calls the state's body `0x7e155fd2`. | pattern scan |
| `0x7e157949` | 1 | `cmp_state_enter_11_7e157949` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e15799e`. | pattern scan |
| `0x7e1579f5` | 1 | `cmp_state_enter_50_7e1579f5` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e157a4a`. | pattern scan |
| `0x7e157b41` | 1 | `cmp_state_enter_52_7e157b41` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e157b96`. | pattern scan |
| `0x7e157c98` | 1 | `cmp_state_enter_54_7e157c98` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e157ced`. | pattern scan |
| `0x7e157dcb` | 1 | `cmp_state_enter_13_7e157dcb` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e157e20`. | pattern scan |
| `0x7e157e44` | 1 | `cmp_state_enter_56_7e157e44` | Cmp state-enter wrapper: sets the state word `+948 = 56`, then calls the state's body `0x7e157e99`. | pattern scan |
| `0x7e158493` | 1 | `cmp_state_enter_58_7e158493` | Cmp state-enter wrapper: sets the state word `+948 = 58`, then calls the state's body `0x7e1584e8`. | pattern scan |
| `0x7e158613` | 1 | `cmp_state_enter_60_7e158613` | Cmp state-enter wrapper: sets the state word `+948 = 60`, then calls the state's body `0x7e158668`. | pattern scan |
| `0x7e158bbd` | 1 | `cmp_state_enter_62_7e158bbd` | Cmp state-enter wrapper: sets the state word `+948 = 62`, then calls the state's body `0x7e158c12`. | pattern scan |
| `0x7e158f52` | 1 | `cmp_state_enter_16_7e158f52` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e158fa7`. | pattern scan |
| `0x7e158fcb` | 1 | `cmp_state_enter_18_7e158fcb` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e159020`. | pattern scan |
| `0x7e159044` | 1 | `cmp_state_enter_20_7e159044` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e159099`. | pattern scan |
| `0x7e1590bd` | 1 | `cmp_state_enter_64_7e1590bd` | Cmp state-enter wrapper: sets the state word `+948 = 64`, then calls the state's body `0x7e159112`. | pattern scan |
| `0x7e1591fb` | 1 | `cmp_state_enter_22_7e1591fb` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e159250`. | pattern scan |
| `0x7e159274` | 1 | `cmp_state_enter_24_7e159274` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e1592c9`. | pattern scan |
| `0x7e1592ed` | 1 | `cmp_state_enter_66_7e1592ed` | Cmp state-enter wrapper: sets the state word `+948 = 66`, then calls the state's body `0x7e159342`. | pattern scan |
| `0x7e159437` | 1 | `cmp_state_enter_26_7e159437` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e15948c`. | pattern scan |
| `0x7e1594b0` | 1 | `cmp_state_enter_28_7e1594b0` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e159505`. | pattern scan |
| `0x7e159529` | 1 | `cmp_state_enter_30_7e159529` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e15957e`. | pattern scan |
| `0x7e1595a2` | 1 | `cmp_state_enter_32_7e1595a2` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e1595f7`. | pattern scan |
| `0x7e15961b` | 1 | `cmp_state_enter_34_7e15961b` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e159670`. | pattern scan |
| `0x7e159694` | 1 | `cmp_state_enter_68_7e159694` | Cmp state-enter wrapper: sets the state word `+948 = 68`, then calls the state's body `0x7e1596e9`. | pattern scan |
| `0x7e1597de` | 1 | `cmp_state_enter_36_7e1597de` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e159833`. | pattern scan |
| `0x7e159929` | 1 | `cmp_state_enter_38_7e159929` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e15997e`. | pattern scan |
| `0x7e1599a9` | 1 | `cmp_state_enter_70_7e1599a9` | Cmp state-enter wrapper: sets the state word `+948 = 70`, then calls the state's body `0x7e1599fe`. | pattern scan |
| `0x7e159bfb` | 1 | `cmp_state_enter_40_7e159bfb` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e159c50`. | pattern scan |
| `0x7e159c74` | 1 | `cmp_state_enter_42_7e159c74` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e159cd7`. | pattern scan |
| `0x7e159cfb` | 1 | `cmp_state_enter_72_7e159cfb` | Cmp state-enter wrapper: sets the state word `+948 = 72`, then calls the state's body `0x7e159d50`. | pattern scan |
| `0x7e159f4d` | 1 | `cmp_state_enter_44_7e159f4d` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e159fa2`. | pattern scan |
| `0x7e159fc6` | 1 | `cmp_state_enter_46_7e159fc6` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e15a01b`. | pattern scan |
| `0x7e15a03f` | 1 | `cmp_state_enter_74_7e15a03f` | Cmp state-enter wrapper: sets the state word `+948 = 74`, then calls the state's body `0x7e15a094`. | pattern scan |
| `0x7e15c22e` | 1 | `cmp_state_enter_11_7e15c22e` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e15c283`. | pattern scan |
| `0x7e15c2da` | 1 | `cmp_state_enter_50_7e15c2da` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e15c32f`. | pattern scan |
| `0x7e15c3ff` | 1 | `cmp_state_enter_52_7e15c3ff` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e15c454`. | pattern scan |
| `0x7e15c67e` | 1 | `cmp_state_enter_13_7e15c67e` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e15c6d3`. | pattern scan |
| `0x7e15c6f7` | 1 | `cmp_state_enter_54_7e15c6f7` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e15c74c`. | pattern scan |
| `0x7e15ce2c` | 1 | `cmp_state_enter_58_7e15ce2c` | Cmp state-enter wrapper: sets the state word `+948 = 58`, then calls the state's body `0x7e15ce81`. | pattern scan |
| `0x7e15cfe3` | 1 | `cmp_state_enter_60_7e15cfe3` | Cmp state-enter wrapper: sets the state word `+948 = 60`, then calls the state's body `0x7e15d038`. | pattern scan |
| `0x7e15d177` | 1 | `cmp_state_enter_62_7e15d177` | Cmp state-enter wrapper: sets the state word `+948 = 62`, then calls the state's body `0x7e15d1d6`. | pattern scan |
| `0x7e15dc1e` | 1 | `cmp_state_enter_16_7e15dc1e` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e15dc73`. | pattern scan |
| `0x7e15dc97` | 1 | `cmp_state_enter_18_7e15dc97` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e15dcec`. | pattern scan |
| `0x7e15dd10` | 1 | `cmp_state_enter_20_7e15dd10` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e15dd65`. | pattern scan |
| `0x7e15dd89` | 1 | `cmp_state_enter_70_7e15dd89` | Cmp state-enter wrapper: sets the state word `+948 = 70`, then calls the state's body `0x7e15ddde`. | pattern scan |
| `0x7e15e04d` | 1 | `cmp_state_enter_22_7e15e04d` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e15e0a2`. | pattern scan |
| `0x7e15e0c6` | 1 | `cmp_state_enter_24_7e15e0c6` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e15e11b`. | pattern scan |
| `0x7e15e13f` | 1 | `cmp_state_enter_72_7e15e13f` | Cmp state-enter wrapper: sets the state word `+948 = 72`, then calls the state's body `0x7e15e194`. | pattern scan |
| `0x7e15e256` | 1 | `cmp_state_enter_26_7e15e256` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e15e2ab`. | pattern scan |
| `0x7e15e2cf` | 1 | `cmp_state_enter_28_7e15e2cf` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e15e324`. | pattern scan |
| `0x7e15e348` | 1 | `cmp_state_enter_74_7e15e348` | Cmp state-enter wrapper: sets the state word `+948 = 74`, then calls the state's body `0x7e15e39d`. | pattern scan |
| `0x7e15e45d` | 1 | `cmp_state_enter_30_7e15e45d` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e15e4b2`. | pattern scan |
| `0x7e15e4d6` | 1 | `cmp_state_enter_32_7e15e4d6` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e15e52b`. | pattern scan |
| `0x7e15e54f` | 1 | `cmp_state_enter_34_7e15e54f` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e15e5a4`. | pattern scan |
| `0x7e15e5c8` | 1 | `cmp_state_enter_76_7e15e5c8` | Cmp state-enter wrapper: sets the state word `+948 = 76`, then calls the state's body `0x7e15e61d`. | pattern scan |
| `0x7e15e6df` | 1 | `cmp_state_enter_36_7e15e6df` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e15e734`. | pattern scan |
| `0x7e15e82a` | 1 | `cmp_state_enter_38_7e15e82a` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e15e87f`. | pattern scan |
| `0x7e15e8a3` | 1 | `cmp_state_enter_40_7e15e8a3` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e15e8f8`. | pattern scan |
| `0x7e15e91c` | 1 | `cmp_state_enter_42_7e15e91c` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e15e97f`. | pattern scan |
| `0x7e15e9a3` | 1 | `cmp_state_enter_44_7e15e9a3` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e15e9f8`. | pattern scan |
| `0x7e15ea1c` | 1 | `cmp_state_enter_46_7e15ea1c` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e15ea71`. | pattern scan |
| `0x7e15ea95` | 1 | `cmp_state_enter_78_7e15ea95` | Cmp state-enter wrapper: sets the state word `+948 = 78`, then calls the state's body `0x7e15eaea`. | pattern scan |
| `0x7e15ec3e` | 1 | `cmp_state_enter_80_7e15ec3e` | Cmp state-enter wrapper: sets the state word `+948 = 80`, then calls the state's body `0x7e15ec93`. | pattern scan |
| `0x7e15ed9e` | 1 | `cmp_state_enter_82_7e15ed9e` | Cmp state-enter wrapper: sets the state word `+948 = 82`, then calls the state's body `0x7e15edf3`. | pattern scan |
| `0x7e16098b` | 1 | `cmp_state_enter_11_7e16098b` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e1609e0`. | pattern scan |
| `0x7e160a37` | 1 | `cmp_state_enter_50_7e160a37` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e160a8c`. | pattern scan |
| `0x7e160b33` | 1 | `cmp_state_enter_13_7e160b33` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e160b88`. | pattern scan |
| `0x7e160dbd` | 1 | `cmp_state_enter_52_7e160dbd` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e160e12`. | pattern scan |
| `0x7e160ec2` | 1 | `cmp_state_enter_16_7e160ec2` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e160f17`. | pattern scan |
| `0x7e160f3b` | 1 | `cmp_state_enter_18_7e160f3b` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e160f90`. | pattern scan |
| `0x7e160fb4` | 1 | `cmp_state_enter_20_7e160fb4` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e161009`. | pattern scan |
| `0x7e16102d` | 1 | `cmp_state_enter_22_7e16102d` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e161082`. | pattern scan |
| `0x7e1610a6` | 1 | `cmp_state_enter_24_7e1610a6` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e1610fb`. | pattern scan |
| `0x7e16111f` | 1 | `cmp_state_enter_26_7e16111f` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e161174`. | pattern scan |
| `0x7e161198` | 1 | `cmp_state_enter_28_7e161198` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e1611ed`. | pattern scan |
| `0x7e161211` | 1 | `cmp_state_enter_30_7e161211` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e161266`. | pattern scan |
| `0x7e16128a` | 1 | `cmp_state_enter_32_7e16128a` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e1612df`. | pattern scan |
| `0x7e161303` | 1 | `cmp_state_enter_34_7e161303` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e161358`. | pattern scan |
| `0x7e16137c` | 1 | `cmp_state_enter_36_7e16137c` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e1613d1`. | pattern scan |
| `0x7e1614c7` | 1 | `cmp_state_enter_38_7e1614c7` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e16151c`. | pattern scan |
| `0x7e161540` | 1 | `cmp_state_enter_40_7e161540` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e161595`. | pattern scan |
| `0x7e1615b9` | 1 | `cmp_state_enter_42_7e1615b9` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e16161c`. | pattern scan |
| `0x7e161640` | 1 | `cmp_state_enter_44_7e161640` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e161695`. | pattern scan |
| `0x7e1616b9` | 1 | `cmp_state_enter_46_7e1616b9` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e16170e`. | pattern scan |
| `0x7e164271` | 1 | `cmp_state_enter_11_7e164271` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e1642c6`. | pattern scan |
| `0x7e16431d` | 1 | `cmp_state_enter_50_7e16431d` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e164372`. | pattern scan |
| `0x7e164575` | 1 | `cmp_state_enter_13_7e164575` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e1645ca`. | pattern scan |
| `0x7e1645ee` | 1 | `cmp_state_enter_55_7e1645ee` | Cmp state-enter wrapper: sets the state word `+948 = 55`, then calls the state's body `0x7e164643`. | pattern scan |
| `0x7e164824` | 1 | `cmp_state_enter_58_7e164824` | Cmp state-enter wrapper: sets the state word `+948 = 58`, then calls the state's body `0x7e164879`. | pattern scan |
| `0x7e164a5a` | 1 | `cmp_state_enter_61_7e164a5a` | Cmp state-enter wrapper: sets the state word `+948 = 61`, then calls the state's body `0x7e164aaf`. | pattern scan |
| `0x7e164cd7` | 1 | `cmp_state_enter_64_7e164cd7` | Cmp state-enter wrapper: sets the state word `+948 = 64`, then calls the state's body `0x7e164d2c`. | pattern scan |
| `0x7e16533c` | 1 | `cmp_state_enter_66_7e16533c` | Cmp state-enter wrapper: sets the state word `+948 = 66`, then calls the state's body `0x7e165391`. | pattern scan |
| `0x7e165631` | 1 | `cmp_state_enter_69_7e165631` | Cmp state-enter wrapper: sets the state word `+948 = 69`, then calls the state's body `0x7e165686`. | pattern scan |
| `0x7e165926` | 1 | `cmp_state_enter_16_7e165926` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e16597b`. | pattern scan |
| `0x7e16599f` | 1 | `cmp_state_enter_18_7e16599f` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e1659f4`. | pattern scan |
| `0x7e165a18` | 1 | `cmp_state_enter_20_7e165a18` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e165a6d`. | pattern scan |
| `0x7e165a91` | 1 | `cmp_state_enter_22_7e165a91` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e165ae6`. | pattern scan |
| `0x7e165b0a` | 1 | `cmp_state_enter_24_7e165b0a` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e165b5f`. | pattern scan |
| `0x7e165b83` | 1 | `cmp_state_enter_26_7e165b83` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e165bd8`. | pattern scan |
| `0x7e165bfc` | 1 | `cmp_state_enter_28_7e165bfc` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e165c51`. | pattern scan |
| `0x7e165c75` | 1 | `cmp_state_enter_30_7e165c75` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e165cca`. | pattern scan |
| `0x7e165cee` | 1 | `cmp_state_enter_32_7e165cee` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e165d43`. | pattern scan |
| `0x7e165d67` | 1 | `cmp_state_enter_34_7e165d67` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e165dbc`. | pattern scan |
| `0x7e165de0` | 1 | `cmp_state_enter_36_7e165de0` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e165e35`. | pattern scan |
| `0x7e165f2b` | 1 | `cmp_state_enter_38_7e165f2b` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e165f80`. | pattern scan |
| `0x7e166103` | 1 | `cmp_state_enter_40_7e166103` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e166158`. | pattern scan |
| `0x7e16617c` | 1 | `cmp_state_enter_42_7e16617c` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e1661df`. | pattern scan |
| `0x7e166203` | 1 | `cmp_state_enter_44_7e166203` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e166258`. | pattern scan |
| `0x7e16627c` | 1 | `cmp_state_enter_75_7e16627c` | Cmp state-enter wrapper: sets the state word `+948 = 75`, then calls the state's body `0x7e1662d1`. | pattern scan |
| `0x7e16644f` | 1 | `cmp_state_enter_46_7e16644f` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e1664a4`. | pattern scan |
| `0x7e167f5d` | 1 | `cmp_state_enter_11_7e167f5d` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e167fb2`. | pattern scan |
| `0x7e168009` | 1 | `cmp_state_enter_50_7e168009` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e16805e`. | pattern scan |
| `0x7e168113` | 1 | `cmp_state_enter_52_7e168113` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e168168`. | pattern scan |
| `0x7e168235` | 1 | `cmp_state_enter_54_7e168235` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e16828a`. | pattern scan |
| `0x7e168333` | 1 | `cmp_state_enter_13_7e168333` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e168388`. | pattern scan |
| `0x7e1683ac` | 1 | `cmp_state_enter_56_7e1683ac` | Cmp state-enter wrapper: sets the state word `+948 = 56`, then calls the state's body `0x7e168401`. | pattern scan |
| `0x7e168949` | 1 | `cmp_state_enter_58_7e168949` | Cmp state-enter wrapper: sets the state word `+948 = 58`, then calls the state's body `0x7e16899e`. | pattern scan |
| `0x7e168aec` | 1 | `cmp_state_enter_60_7e168aec` | Cmp state-enter wrapper: sets the state word `+948 = 60`, then calls the state's body `0x7e168b41`. | pattern scan |
| `0x7e168c23` | 1 | `cmp_state_enter_62_7e168c23` | Cmp state-enter wrapper: sets the state word `+948 = 62`, then calls the state's body `0x7e168c78`. | pattern scan |
| `0x7e169287` | 1 | `cmp_state_enter_16_7e169287` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e1692dc`. | pattern scan |
| `0x7e169300` | 1 | `cmp_state_enter_18_7e169300` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e169355`. | pattern scan |
| `0x7e169379` | 1 | `cmp_state_enter_20_7e169379` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e1693ce`. | pattern scan |
| `0x7e1693f2` | 1 | `cmp_state_enter_64_7e1693f2` | Cmp state-enter wrapper: sets the state word `+948 = 64`, then calls the state's body `0x7e169447`. | pattern scan |
| `0x7e1694fd` | 1 | `cmp_state_enter_22_7e1694fd` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e169552`. | pattern scan |
| `0x7e169576` | 1 | `cmp_state_enter_24_7e169576` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e1695cb`. | pattern scan |
| `0x7e1695ef` | 1 | `cmp_state_enter_66_7e1695ef` | Cmp state-enter wrapper: sets the state word `+948 = 66`, then calls the state's body `0x7e169644`. | pattern scan |
| `0x7e169710` | 1 | `cmp_state_enter_26_7e169710` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e169765`. | pattern scan |
| `0x7e169789` | 1 | `cmp_state_enter_28_7e169789` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e1697de`. | pattern scan |
| `0x7e169802` | 1 | `cmp_state_enter_30_7e169802` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e169857`. | pattern scan |
| `0x7e16987b` | 1 | `cmp_state_enter_32_7e16987b` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e1698d0`. | pattern scan |
| `0x7e1698f4` | 1 | `cmp_state_enter_34_7e1698f4` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e169949`. | pattern scan |
| `0x7e16996d` | 1 | `cmp_state_enter_68_7e16996d` | Cmp state-enter wrapper: sets the state word `+948 = 68`, then calls the state's body `0x7e1699c2`. | pattern scan |
| `0x7e169a89` | 1 | `cmp_state_enter_36_7e169a89` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e169ade`. | pattern scan |
| `0x7e169bd4` | 1 | `cmp_state_enter_38_7e169bd4` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e169c29`. | pattern scan |
| `0x7e169c54` | 1 | `cmp_state_enter_40_7e169c54` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e169ca9`. | pattern scan |
| `0x7e169ccd` | 1 | `cmp_state_enter_42_7e169ccd` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e169d30`. | pattern scan |
| `0x7e169d54` | 1 | `cmp_state_enter_44_7e169d54` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e169da9`. | pattern scan |
| `0x7e169dcd` | 1 | `cmp_state_enter_46_7e169dcd` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e169e22`. | pattern scan |
| `0x7e169f86` | 1 | `cmp_state_enter_72_7e169f86` | Cmp state-enter wrapper: sets the state word `+948 = 72`, then calls the state's body `0x7e169fdb`. | pattern scan |
| `0x7e16b7eb` | 1 | `cmp_state_enter_11_7e16b7eb` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e16b840`. | pattern scan |
| `0x7e16b897` | 1 | `cmp_state_enter_50_7e16b897` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e16b8ec`. | pattern scan |
| `0x7e16ba36` | 1 | `cmp_state_enter_13_7e16ba36` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e16ba8b`. | pattern scan |
| `0x7e16baaf` | 1 | `cmp_state_enter_52_7e16baaf` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e16bb04`. | pattern scan |
| `0x7e16c024` | 1 | `cmp_state_enter_54_7e16c024` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e16c079`. | pattern scan |
| `0x7e16c1ff` | 1 | `cmp_state_enter_56_7e16c1ff` | Cmp state-enter wrapper: sets the state word `+948 = 56`, then calls the state's body `0x7e16c254`. | pattern scan |
| `0x7e16c300` | 1 | `cmp_state_enter_58_7e16c300` | Cmp state-enter wrapper: sets the state word `+948 = 58`, then calls the state's body `0x7e16c355`. | pattern scan |
| `0x7e16c4d4` | 1 | `cmp_state_enter_16_7e16c4d4` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e16c529`. | pattern scan |
| `0x7e16c54d` | 1 | `cmp_state_enter_18_7e16c54d` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e16c5a2`. | pattern scan |
| `0x7e16c5c6` | 1 | `cmp_state_enter_20_7e16c5c6` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e16c61b`. | pattern scan |
| `0x7e16c63f` | 1 | `cmp_state_enter_22_7e16c63f` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e16c694`. | pattern scan |
| `0x7e16c6b8` | 1 | `cmp_state_enter_24_7e16c6b8` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e16c70d`. | pattern scan |
| `0x7e16c731` | 1 | `cmp_state_enter_60_7e16c731` | Cmp state-enter wrapper: sets the state word `+948 = 60`, then calls the state's body `0x7e16c786`. | pattern scan |
| `0x7e16ca2b` | 1 | `cmp_state_enter_26_7e16ca2b` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e16ca80`. | pattern scan |
| `0x7e16caa4` | 1 | `cmp_state_enter_28_7e16caa4` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e16caf9`. | pattern scan |
| `0x7e16cb1d` | 1 | `cmp_state_enter_30_7e16cb1d` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e16cb72`. | pattern scan |
| `0x7e16cb96` | 1 | `cmp_state_enter_32_7e16cb96` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e16cbeb`. | pattern scan |
| `0x7e16cc0f` | 1 | `cmp_state_enter_34_7e16cc0f` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e16cc64`. | pattern scan |
| `0x7e16cc88` | 1 | `cmp_state_enter_36_7e16cc88` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e16ccdd`. | pattern scan |
| `0x7e16cdd3` | 1 | `cmp_state_enter_38_7e16cdd3` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e16ce28`. | pattern scan |
| `0x7e16ce4c` | 1 | `cmp_state_enter_40_7e16ce4c` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e16cea1`. | pattern scan |
| `0x7e16cec5` | 1 | `cmp_state_enter_42_7e16cec5` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e16cf28`. | pattern scan |
| `0x7e16cf4c` | 1 | `cmp_state_enter_44_7e16cf4c` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e16cfa1`. | pattern scan |
| `0x7e16cfc5` | 1 | `cmp_state_enter_46_7e16cfc5` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e16d01a`. | pattern scan |
| `0x7e16ed1e` | 1 | `cmp_state_enter_11_7e16ed1e` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e16ed73`. | pattern scan |
| `0x7e16edca` | 1 | `cmp_state_enter_50_7e16edca` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e16ee1f`. | pattern scan |
| `0x7e16eec2` | 1 | `cmp_state_enter_13_7e16eec2` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e16ef17`. | pattern scan |
| `0x7e16ef3b` | 1 | `cmp_state_enter_52_7e16ef3b` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e16ef90`. | pattern scan |
| `0x7e16f233` | 1 | `cmp_state_enter_54_7e16f233` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e16f288`. | pattern scan |
| `0x7e16f334` | 1 | `cmp_state_enter_16_7e16f334` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e16f389`. | pattern scan |
| `0x7e16f3ad` | 1 | `cmp_state_enter_18_7e16f3ad` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e16f402`. | pattern scan |
| `0x7e16f426` | 1 | `cmp_state_enter_20_7e16f426` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e16f47b`. | pattern scan |
| `0x7e16f49f` | 1 | `cmp_state_enter_22_7e16f49f` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e16f4f4`. | pattern scan |
| `0x7e16f518` | 1 | `cmp_state_enter_24_7e16f518` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e16f56d`. | pattern scan |
| `0x7e16f591` | 1 | `cmp_state_enter_26_7e16f591` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e16f5e6`. | pattern scan |
| `0x7e16f60a` | 1 | `cmp_state_enter_28_7e16f60a` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e16f65f`. | pattern scan |
| `0x7e16f683` | 1 | `cmp_state_enter_30_7e16f683` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e16f6d8`. | pattern scan |
| `0x7e16f6fc` | 1 | `cmp_state_enter_32_7e16f6fc` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e16f751`. | pattern scan |
| `0x7e16f775` | 1 | `cmp_state_enter_34_7e16f775` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e16f7ca`. | pattern scan |
| `0x7e16f7ee` | 1 | `cmp_state_enter_36_7e16f7ee` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e16f843`. | pattern scan |
| `0x7e16f939` | 1 | `cmp_state_enter_38_7e16f939` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e16f98e`. | pattern scan |
| `0x7e16f9b2` | 1 | `cmp_state_enter_40_7e16f9b2` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e16fa07`. | pattern scan |
| `0x7e16fa2b` | 1 | `cmp_state_enter_42_7e16fa2b` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e16fa8e`. | pattern scan |
| `0x7e16fab2` | 1 | `cmp_state_enter_44_7e16fab2` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e16fb07`. | pattern scan |
| `0x7e16fb2b` | 1 | `cmp_state_enter_56_7e16fb2b` | Cmp state-enter wrapper: sets the state word `+948 = 56`, then calls the state's body `0x7e16fb80`. | pattern scan |
| `0x7e16fcc2` | 1 | `cmp_state_enter_46_7e16fcc2` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e16fd17`. | pattern scan |
| `0x7e17171b` | 1 | `cmp_state_enter_11_7e17171b` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e171770`. | pattern scan |
| `0x7e1717c7` | 1 | `cmp_state_enter_50_7e1717c7` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e17181c`. | pattern scan |
| `0x7e1718cc` | 1 | `cmp_state_enter_52_7e1718cc` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e171921`. | pattern scan |
| `0x7e1719a9` | 1 | `cmp_state_enter_54_7e1719a9` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e1719fe`. | pattern scan |
| `0x7e171aa1` | 1 | `cmp_state_enter_13_7e171aa1` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e171af6`. | pattern scan |
| `0x7e171b1a` | 1 | `cmp_state_enter_56_7e171b1a` | Cmp state-enter wrapper: sets the state word `+948 = 56`, then calls the state's body `0x7e171b6f`. | pattern scan |
| `0x7e1720a8` | 1 | `cmp_state_enter_58_7e1720a8` | Cmp state-enter wrapper: sets the state word `+948 = 58`, then calls the state's body `0x7e1720fd`. | pattern scan |
| `0x7e17224b` | 1 | `cmp_state_enter_60_7e17224b` | Cmp state-enter wrapper: sets the state word `+948 = 60`, then calls the state's body `0x7e1722a0`. | pattern scan |
| `0x7e17237c` | 1 | `cmp_state_enter_62_7e17237c` | Cmp state-enter wrapper: sets the state word `+948 = 62`, then calls the state's body `0x7e1723d1`. | pattern scan |
| `0x7e172947` | 1 | `cmp_state_enter_16_7e172947` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e17299c`. | pattern scan |
| `0x7e1729c0` | 1 | `cmp_state_enter_18_7e1729c0` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e172a15`. | pattern scan |
| `0x7e172a39` | 1 | `cmp_state_enter_20_7e172a39` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e172a8e`. | pattern scan |
| `0x7e172ab2` | 1 | `cmp_state_enter_64_7e172ab2` | Cmp state-enter wrapper: sets the state word `+948 = 64`, then calls the state's body `0x7e172b07`. | pattern scan |
| `0x7e172bb7` | 1 | `cmp_state_enter_22_7e172bb7` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e172c0c`. | pattern scan |
| `0x7e172c30` | 1 | `cmp_state_enter_24_7e172c30` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e172c85`. | pattern scan |
| `0x7e172ca9` | 1 | `cmp_state_enter_66_7e172ca9` | Cmp state-enter wrapper: sets the state word `+948 = 66`, then calls the state's body `0x7e172cfe`. | pattern scan |
| `0x7e172dc0` | 1 | `cmp_state_enter_26_7e172dc0` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e172e15`. | pattern scan |
| `0x7e172e39` | 1 | `cmp_state_enter_28_7e172e39` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e172e8e`. | pattern scan |
| `0x7e172eb2` | 1 | `cmp_state_enter_30_7e172eb2` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e172f07`. | pattern scan |
| `0x7e172f2b` | 1 | `cmp_state_enter_32_7e172f2b` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e172f80`. | pattern scan |
| `0x7e172fa4` | 1 | `cmp_state_enter_34_7e172fa4` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e172ff9`. | pattern scan |
| `0x7e17301d` | 1 | `cmp_state_enter_68_7e17301d` | Cmp state-enter wrapper: sets the state word `+948 = 68`, then calls the state's body `0x7e173072`. | pattern scan |
| `0x7e173134` | 1 | `cmp_state_enter_36_7e173134` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e173189`. | pattern scan |
| `0x7e17327f` | 1 | `cmp_state_enter_38_7e17327f` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e1732d4`. | pattern scan |
| `0x7e1732ff` | 1 | `cmp_state_enter_40_7e1732ff` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e173354`. | pattern scan |
| `0x7e173378` | 1 | `cmp_state_enter_42_7e173378` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e1733db`. | pattern scan |
| `0x7e1733ff` | 1 | `cmp_state_enter_44_7e1733ff` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e173454`. | pattern scan |
| `0x7e173478` | 1 | `cmp_state_enter_46_7e173478` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e1734cd`. | pattern scan |
| `0x7e1734f1` | 1 | `cmp_state_enter_70_7e1734f1` | Cmp state-enter wrapper: sets the state word `+948 = 70`, then calls the state's body `0x7e173546`. | pattern scan |
| `0x7e173618` | 1 | `cmp_state_enter_72_7e173618` | Cmp state-enter wrapper: sets the state word `+948 = 72`, then calls the state's body `0x7e17366d`. | pattern scan |
| `0x7e176459` | 1 | `cmp_state_enter_50_7e176459` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e1764ae`. | pattern scan |
| `0x7e176687` | 1 | `cmp_state_enter_11_7e176687` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e1766dc`. | pattern scan |
| `0x7e176733` | 1 | `cmp_state_enter_52_7e176733` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e176788`. | pattern scan |
| `0x7e17683e` | 1 | `cmp_state_enter_54_7e17683e` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e176893`. | pattern scan |
| `0x7e176956` | 1 | `cmp_state_enter_56_7e176956` | Cmp state-enter wrapper: sets the state word `+948 = 56`, then calls the state's body `0x7e1769ab`. | pattern scan |
| `0x7e176a4e` | 1 | `cmp_state_enter_13_7e176a4e` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e176aa3`. | pattern scan |
| `0x7e176ac7` | 1 | `cmp_state_enter_58_7e176ac7` | Cmp state-enter wrapper: sets the state word `+948 = 58`, then calls the state's body `0x7e176b1c`. | pattern scan |
| `0x7e1770c0` | 1 | `cmp_state_enter_60_7e1770c0` | Cmp state-enter wrapper: sets the state word `+948 = 60`, then calls the state's body `0x7e177115`. | pattern scan |
| `0x7e177263` | 1 | `cmp_state_enter_62_7e177263` | Cmp state-enter wrapper: sets the state word `+948 = 62`, then calls the state's body `0x7e1772b8`. | pattern scan |
| `0x7e177394` | 1 | `cmp_state_enter_64_7e177394` | Cmp state-enter wrapper: sets the state word `+948 = 64`, then calls the state's body `0x7e1773e9`. | pattern scan |
| `0x7e1775d3` | 1 | `cmp_state_enter_16_7e1775d3` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e177628`. | pattern scan |
| `0x7e17764c` | 1 | `cmp_state_enter_18_7e17764c` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e1776a1`. | pattern scan |
| `0x7e1776c5` | 1 | `cmp_state_enter_20_7e1776c5` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e17771a`. | pattern scan |
| `0x7e17773e` | 1 | `cmp_state_enter_66_7e17773e` | Cmp state-enter wrapper: sets the state word `+948 = 66`, then calls the state's body `0x7e177793`. | pattern scan |
| `0x7e177843` | 1 | `cmp_state_enter_68_7e177843` | Cmp state-enter wrapper: sets the state word `+948 = 68`, then calls the state's body `0x7e177898`. | pattern scan |
| `0x7e177d19` | 1 | `cmp_state_enter_22_7e177d19` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e177d6e`. | pattern scan |
| `0x7e177d92` | 1 | `cmp_state_enter_24_7e177d92` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e177de7`. | pattern scan |
| `0x7e177e0b` | 1 | `cmp_state_enter_70_7e177e0b` | Cmp state-enter wrapper: sets the state word `+948 = 70`, then calls the state's body `0x7e177e60`. | pattern scan |
| `0x7e177f22` | 1 | `cmp_state_enter_26_7e177f22` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e177f77`. | pattern scan |
| `0x7e177f9b` | 1 | `cmp_state_enter_28_7e177f9b` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e177ff0`. | pattern scan |
| `0x7e178014` | 1 | `cmp_state_enter_30_7e178014` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e178069`. | pattern scan |
| `0x7e17808d` | 1 | `cmp_state_enter_32_7e17808d` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e1780e2`. | pattern scan |
| `0x7e178106` | 1 | `cmp_state_enter_34_7e178106` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e17815b`. | pattern scan |
| `0x7e17817f` | 1 | `cmp_state_enter_72_7e17817f` | Cmp state-enter wrapper: sets the state word `+948 = 72`, then calls the state's body `0x7e1781d4`. | pattern scan |
| `0x7e178296` | 1 | `cmp_state_enter_36_7e178296` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e1782eb`. | pattern scan |
| `0x7e1783e1` | 1 | `cmp_state_enter_38_7e1783e1` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e178436`. | pattern scan |
| `0x7e178461` | 1 | `cmp_state_enter_74_7e178461` | Cmp state-enter wrapper: sets the state word `+948 = 74`, then calls the state's body `0x7e1784b6`. | pattern scan |
| `0x7e1785db` | 1 | `cmp_state_enter_40_7e1785db` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e178630`. | pattern scan |
| `0x7e178654` | 1 | `cmp_state_enter_42_7e178654` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e1786b7`. | pattern scan |
| `0x7e1786db` | 1 | `cmp_state_enter_76_7e1786db` | Cmp state-enter wrapper: sets the state word `+948 = 76`, then calls the state's body `0x7e178730`. | pattern scan |
| `0x7e17883e` | 1 | `cmp_state_enter_44_7e17883e` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e178893`. | pattern scan |
| `0x7e1788b7` | 1 | `cmp_state_enter_78_7e1788b7` | Cmp state-enter wrapper: sets the state word `+948 = 78`, then calls the state's body `0x7e17890c`. | pattern scan |
| `0x7e178cb1` | 1 | `cmp_state_enter_46_7e178cb1` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e178d06`. | pattern scan |
| `0x7e18e1a6` | 1 | `cmp_state_enter_11_7e18e1a6` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e18e1fb`. | pattern scan |
| `0x7e18e252` | 1 | `cmp_state_enter_13_7e18e252` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e18e2a7`. | pattern scan |
| `0x7e18e576` | 1 | `cmp_state_enter_50_7e18e576` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e18e5cb`. | pattern scan |
| `0x7e18e7af` | 1 | `cmp_state_enter_52_7e18e7af` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e18e804`. | pattern scan |
| `0x7e18ea64` | 1 | `cmp_state_enter_54_7e18ea64` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e18eab9`. | pattern scan |
| `0x7e18ed06` | 1 | `cmp_state_enter_56_7e18ed06` | Cmp state-enter wrapper: sets the state word `+948 = 56`, then calls the state's body `0x7e18ed5b`. | pattern scan |
| `0x7e18ef5c` | 1 | `cmp_state_enter_58_7e18ef5c` | Cmp state-enter wrapper: sets the state word `+948 = 58`, then calls the state's body `0x7e18efb1`. | pattern scan |
| `0x7e18f088` | 1 | `cmp_state_enter_60_7e18f088` | Cmp state-enter wrapper: sets the state word `+948 = 60`, then calls the state's body `0x7e18f0dd`. | pattern scan |
| `0x7e18f1f6` | 1 | `cmp_state_enter_62_7e18f1f6` | Cmp state-enter wrapper: sets the state word `+948 = 62`, then calls the state's body `0x7e18f24b`. | pattern scan |
| `0x7e18f369` | 1 | `cmp_state_enter_65_7e18f369` | Cmp state-enter wrapper: sets the state word `+948 = 65`, then calls the state's body `0x7e18f3be`. | pattern scan |
| `0x7e18f499` | 1 | `cmp_state_enter_16_7e18f499` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e18f4ee`. | pattern scan |
| `0x7e18f512` | 1 | `cmp_state_enter_18_7e18f512` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e18f567`. | pattern scan |
| `0x7e18f58b` | 1 | `cmp_state_enter_20_7e18f58b` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e18f5e0`. | pattern scan |
| `0x7e18f604` | 1 | `cmp_state_enter_22_7e18f604` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e18f659`. | pattern scan |
| `0x7e18f67d` | 1 | `cmp_state_enter_24_7e18f67d` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e18f6d2`. | pattern scan |
| `0x7e18f6f6` | 1 | `cmp_state_enter_26_7e18f6f6` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e18f74b`. | pattern scan |
| `0x7e18f76f` | 1 | `cmp_state_enter_28_7e18f76f` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e18f7c4`. | pattern scan |
| `0x7e18f7e8` | 1 | `cmp_state_enter_30_7e18f7e8` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e18f83d`. | pattern scan |
| `0x7e18f861` | 1 | `cmp_state_enter_32_7e18f861` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e18f8b6`. | pattern scan |
| `0x7e18f8da` | 1 | `cmp_state_enter_34_7e18f8da` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e18f92f`. | pattern scan |
| `0x7e18f953` | 1 | `cmp_state_enter_36_7e18f953` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e18f9a8`. | pattern scan |
| `0x7e18fa9a` | 1 | `cmp_state_enter_38_7e18fa9a` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e18faef`. | pattern scan |
| `0x7e18fb13` | 1 | `cmp_state_enter_40_7e18fb13` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e18fb68`. | pattern scan |
| `0x7e18fb8c` | 1 | `cmp_state_enter_42_7e18fb8c` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e18fbef`. | pattern scan |
| `0x7e18fc13` | 1 | `cmp_state_enter_44_7e18fc13` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e18fc68`. | pattern scan |
| `0x7e18fc8c` | 1 | `cmp_state_enter_46_7e18fc8c` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e18fce1`. | pattern scan |
| `0x7e19f2de` | 1 | `cmp_state_enter_11_7e19f2de` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e19f333`. | pattern scan |
| `0x7e19f386` | 1 | `cmp_state_enter_13_7e19f386` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e19f3db`. | pattern scan |
| `0x7e19f5e2` | 1 | `cmp_state_enter_16_7e19f5e2` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e19f637`. | pattern scan |
| `0x7e19f659` | 1 | `cmp_state_enter_18_7e19f659` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e19f6ae`. | pattern scan |
| `0x7e19f6d0` | 1 | `cmp_state_enter_20_7e19f6d0` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e19f725`. | pattern scan |
| `0x7e19f747` | 1 | `cmp_state_enter_22_7e19f747` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e19f79c`. | pattern scan |
| `0x7e19f7c1` | 1 | `cmp_state_enter_24_7e19f7c1` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e19f816`. | pattern scan |
| `0x7e19f838` | 1 | `cmp_state_enter_26_7e19f838` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e19f88d`. | pattern scan |
| `0x7e19f8b2` | 1 | `cmp_state_enter_28_7e19f8b2` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e19f907`. | pattern scan |
| `0x7e19f92c` | 1 | `cmp_state_enter_30_7e19f92c` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e19f981`. | pattern scan |
| `0x7e19f9a6` | 1 | `cmp_state_enter_32_7e19f9a6` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e19f9fb`. | pattern scan |
| `0x7e19fa1d` | 1 | `cmp_state_enter_34_7e19fa1d` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e19fa72`. | pattern scan |
| `0x7e19fa94` | 1 | `cmp_state_enter_36_7e19fa94` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e19fae9`. | pattern scan |
| `0x7e19fbdb` | 1 | `cmp_state_enter_38_7e19fbdb` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e19fc30`. | pattern scan |
| `0x7e19fc55` | 1 | `cmp_state_enter_40_7e19fc55` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e19fcaa`. | pattern scan |
| `0x7e19fccc` | 1 | `cmp_state_enter_42_7e19fccc` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e19fd30`. | pattern scan |
| `0x7e19fd55` | 1 | `cmp_state_enter_44_7e19fd55` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e19fdaa`. | pattern scan |
| `0x7e19fdcc` | 1 | `cmp_state_enter_46_7e19fdcc` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e19fe21`. | pattern scan |
| `0x7e1a141c` | 1 | `cmp_state_enter_11_7e1a141c` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e1a1471`. | pattern scan |
| `0x7e1a14c4` | 1 | `cmp_state_enter_13_7e1a14c4` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e1a1519`. | pattern scan |
| `0x7e1a17a4` | 1 | `cmp_state_enter_16_7e1a17a4` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e1a17f9`. | pattern scan |
| `0x7e1a181b` | 1 | `cmp_state_enter_18_7e1a181b` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e1a1870`. | pattern scan |
| `0x7e1a1892` | 1 | `cmp_state_enter_20_7e1a1892` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e1a18e7`. | pattern scan |
| `0x7e1a1909` | 1 | `cmp_state_enter_22_7e1a1909` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e1a195e`. | pattern scan |
| `0x7e1a1982` | 1 | `cmp_state_enter_24_7e1a1982` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e1a19d7`. | pattern scan |
| `0x7e1a19f9` | 1 | `cmp_state_enter_26_7e1a19f9` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e1a1a4e`. | pattern scan |
| `0x7e1a1a72` | 1 | `cmp_state_enter_28_7e1a1a72` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e1a1ac7`. | pattern scan |
| `0x7e1a1aeb` | 1 | `cmp_state_enter_30_7e1a1aeb` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e1a1b40`. | pattern scan |
| `0x7e1a1b64` | 1 | `cmp_state_enter_32_7e1a1b64` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e1a1bb9`. | pattern scan |
| `0x7e1a1bdb` | 1 | `cmp_state_enter_34_7e1a1bdb` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e1a1c30`. | pattern scan |
| `0x7e1a1c54` | 1 | `cmp_state_enter_36_7e1a1c54` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e1a1ca9`. | pattern scan |
| `0x7e1a1d9f` | 1 | `cmp_state_enter_38_7e1a1d9f` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e1a1df4`. | pattern scan |
| `0x7e1a1e16` | 1 | `cmp_state_enter_50_7e1a1e16` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e1a1e6b`. | pattern scan |
| `0x7e1a204b` | 1 | `cmp_state_enter_52_7e1a204b` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e1a20a0`. | pattern scan |
| `0x7e1a2143` | 1 | `cmp_state_enter_54_7e1a2143` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e1a2198`. | pattern scan |
| `0x7e1a22f6` | 1 | `cmp_state_enter_56_7e1a22f6` | Cmp state-enter wrapper: sets the state word `+948 = 56`, then calls the state's body `0x7e1a234b`. | pattern scan |
| `0x7e1a23ee` | 1 | `cmp_state_enter_58_7e1a23ee` | Cmp state-enter wrapper: sets the state word `+948 = 58`, then calls the state's body `0x7e1a2443`. | pattern scan |
| `0x7e1a25da` | 1 | `cmp_state_enter_60_7e1a25da` | Cmp state-enter wrapper: sets the state word `+948 = 60`, then calls the state's body `0x7e1a262f`. | pattern scan |
| `0x7e1a283e` | 1 | `cmp_state_enter_40_7e1a283e` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e1a2893`. | pattern scan |
| `0x7e1a28b7` | 1 | `cmp_state_enter_42_7e1a28b7` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e1a291a`. | pattern scan |
| `0x7e1a293e` | 1 | `cmp_state_enter_44_7e1a293e` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e1a2993`. | pattern scan |
| `0x7e1a29b7` | 1 | `cmp_state_enter_46_7e1a29b7` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e1a2a0c`. | pattern scan |
| `0x7e1a3c74` | 1 | `cmp_state_enter_11_7e1a3c74` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e1a3cc9`. | pattern scan |
| `0x7e1a3d1c` | 1 | `cmp_state_enter_13_7e1a3d1c` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e1a3d71`. | pattern scan |
| `0x7e1a3f78` | 1 | `cmp_state_enter_16_7e1a3f78` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e1a3fcd`. | pattern scan |
| `0x7e1a3ff1` | 1 | `cmp_state_enter_18_7e1a3ff1` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e1a4046`. | pattern scan |
| `0x7e1a406a` | 1 | `cmp_state_enter_20_7e1a406a` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e1a40bf`. | pattern scan |
| `0x7e1a40e3` | 1 | `cmp_state_enter_22_7e1a40e3` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e1a4138`. | pattern scan |
| `0x7e1a415d` | 1 | `cmp_state_enter_24_7e1a415d` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e1a41b2`. | pattern scan |
| `0x7e1a41d6` | 1 | `cmp_state_enter_26_7e1a41d6` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e1a422b`. | pattern scan |
| `0x7e1a4250` | 1 | `cmp_state_enter_28_7e1a4250` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e1a42a5`. | pattern scan |
| `0x7e1a42ca` | 1 | `cmp_state_enter_30_7e1a42ca` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e1a431f`. | pattern scan |
| `0x7e1a4344` | 1 | `cmp_state_enter_32_7e1a4344` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e1a4399`. | pattern scan |
| `0x7e1a43bd` | 1 | `cmp_state_enter_34_7e1a43bd` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e1a4412`. | pattern scan |
| `0x7e1a4436` | 1 | `cmp_state_enter_36_7e1a4436` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e1a448b`. | pattern scan |
| `0x7e1a4581` | 1 | `cmp_state_enter_38_7e1a4581` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e1a45d6`. | pattern scan |
| `0x7e1a45fb` | 1 | `cmp_state_enter_40_7e1a45fb` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e1a4650`. | pattern scan |
| `0x7e1a4674` | 1 | `cmp_state_enter_42_7e1a4674` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e1a46d8`. | pattern scan |
| `0x7e1a46fd` | 1 | `cmp_state_enter_44_7e1a46fd` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e1a4752`. | pattern scan |
| `0x7e1a4776` | 1 | `cmp_state_enter_46_7e1a4776` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e1a47cb`. | pattern scan |
| `0x7e1a6540` | 1 | `cmp_state_enter_11_7e1a6540` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e1a6595`. | pattern scan |
| `0x7e1a65ec` | 1 | `cmp_state_enter_13_7e1a65ec` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e1a6641`. | pattern scan |
| `0x7e1a684a` | 1 | `cmp_state_enter_16_7e1a684a` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e1a689f`. | pattern scan |
| `0x7e1a68c3` | 1 | `cmp_state_enter_18_7e1a68c3` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e1a6918`. | pattern scan |
| `0x7e1a693c` | 1 | `cmp_state_enter_20_7e1a693c` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e1a6991`. | pattern scan |
| `0x7e1a69b5` | 1 | `cmp_state_enter_22_7e1a69b5` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e1a6a0a`. | pattern scan |
| `0x7e1a6a2f` | 1 | `cmp_state_enter_24_7e1a6a2f` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e1a6a84`. | pattern scan |
| `0x7e1a6aa8` | 1 | `cmp_state_enter_26_7e1a6aa8` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e1a6afd`. | pattern scan |
| `0x7e1a6b22` | 1 | `cmp_state_enter_28_7e1a6b22` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e1a6b77`. | pattern scan |
| `0x7e1a6b9c` | 1 | `cmp_state_enter_30_7e1a6b9c` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e1a6bf1`. | pattern scan |
| `0x7e1a6c16` | 1 | `cmp_state_enter_32_7e1a6c16` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e1a6c6b`. | pattern scan |
| `0x7e1a6c8f` | 1 | `cmp_state_enter_34_7e1a6c8f` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e1a6ce4`. | pattern scan |
| `0x7e1a6d08` | 1 | `cmp_state_enter_36_7e1a6d08` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e1a6d5d`. | pattern scan |
| `0x7e1a6e53` | 1 | `cmp_state_enter_38_7e1a6e53` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e1a6ea8`. | pattern scan |
| `0x7e1a6ecd` | 1 | `cmp_state_enter_40_7e1a6ecd` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e1a6f22`. | pattern scan |
| `0x7e1a6f46` | 1 | `cmp_state_enter_42_7e1a6f46` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e1a6faa`. | pattern scan |
| `0x7e1a6fcf` | 1 | `cmp_state_enter_44_7e1a6fcf` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e1a7024`. | pattern scan |
| `0x7e1a7048` | 1 | `cmp_state_enter_46_7e1a7048` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e1a709d`. | pattern scan |
| `0x7e1a9232` | 1 | `cmp_state_enter_11_7e1a9232` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e1a9287`. | pattern scan |
| `0x7e1a92de` | 1 | `cmp_state_enter_13_7e1a92de` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e1a9333`. | pattern scan |
| `0x7e1a96b2` | 1 | `cmp_state_enter_50_7e1a96b2` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e1a9707`. | pattern scan |
| `0x7e1a99f9` | 1 | `cmp_state_enter_52_7e1a99f9` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e1a9a4e`. | pattern scan |
| `0x7e1a9afd` | 1 | `cmp_state_enter_54_7e1a9afd` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e1a9b52`. | pattern scan |
| `0x7e1a9bff` | 1 | `cmp_state_enter_56_7e1a9bff` | Cmp state-enter wrapper: sets the state word `+948 = 56`, then calls the state's body `0x7e1a9c54`. | pattern scan |
| `0x7e1a9edc` | 1 | `cmp_state_enter_58_7e1a9edc` | Cmp state-enter wrapper: sets the state word `+948 = 58`, then calls the state's body `0x7e1a9f31`. | pattern scan |
| `0x7e1aa1b9` | 1 | `cmp_state_enter_60_7e1aa1b9` | Cmp state-enter wrapper: sets the state word `+948 = 60`, then calls the state's body `0x7e1aa20e`. | pattern scan |
| `0x7e1aa318` | 1 | `cmp_state_enter_62_7e1aa318` | Cmp state-enter wrapper: sets the state word `+948 = 62`, then calls the state's body `0x7e1aa36d`. | pattern scan |
| `0x7e1aa40c` | 1 | `cmp_state_enter_64_7e1aa40c` | Cmp state-enter wrapper: sets the state word `+948 = 64`, then calls the state's body `0x7e1aa461`. | pattern scan |
| `0x7e1aa767` | 1 | `cmp_state_enter_66_7e1aa767` | Cmp state-enter wrapper: sets the state word `+948 = 66`, then calls the state's body `0x7e1aa7bc`. | pattern scan |
| `0x7e1aa8ae` | 1 | `cmp_state_enter_68_7e1aa8ae` | Cmp state-enter wrapper: sets the state word `+948 = 68`, then calls the state's body `0x7e1aa903`. | pattern scan |
| `0x7e1aaa15` | 1 | `cmp_state_enter_70_7e1aaa15` | Cmp state-enter wrapper: sets the state word `+948 = 70`, then calls the state's body `0x7e1aaa6a`. | pattern scan |
| `0x7e1aab64` | 1 | `cmp_state_enter_72_7e1aab64` | Cmp state-enter wrapper: sets the state word `+948 = 72`, then calls the state's body `0x7e1aabb9`. | pattern scan |
| `0x7e1aaf56` | 1 | `cmp_state_enter_75_7e1aaf56` | Cmp state-enter wrapper: sets the state word `+948 = 75`, then calls the state's body `0x7e1aafab`. | pattern scan |
| `0x7e1ab281` | 1 | `cmp_state_enter_77_7e1ab281` | Cmp state-enter wrapper: sets the state word `+948 = 77`, then calls the state's body `0x7e1ab2d6`. | pattern scan |
| `0x7e1ab5dd` | 1 | `cmp_state_enter_79_7e1ab5dd` | Cmp state-enter wrapper: sets the state word `+948 = 79`, then calls the state's body `0x7e1ab632`. | pattern scan |
| `0x7e1ab7fd` | 1 | `cmp_state_enter_81_7e1ab7fd` | Cmp state-enter wrapper: sets the state word `+948 = 81`, then calls the state's body `0x7e1ab852`. | pattern scan |
| `0x7e1ab8fa` | 1 | `cmp_state_enter_16_7e1ab8fa` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e1ab94f`. | pattern scan |
| `0x7e1ab973` | 1 | `cmp_state_enter_18_7e1ab973` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e1ab9c8`. | pattern scan |
| `0x7e1ab9ec` | 1 | `cmp_state_enter_20_7e1ab9ec` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e1aba41`. | pattern scan |
| `0x7e1aba65` | 1 | `cmp_state_enter_22_7e1aba65` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e1ababa`. | pattern scan |
| `0x7e1abade` | 1 | `cmp_state_enter_24_7e1abade` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e1abb33`. | pattern scan |
| `0x7e1abb57` | 1 | `cmp_state_enter_26_7e1abb57` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e1abbac`. | pattern scan |
| `0x7e1abbd0` | 1 | `cmp_state_enter_28_7e1abbd0` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e1abc25`. | pattern scan |
| `0x7e1abc49` | 1 | `cmp_state_enter_30_7e1abc49` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e1abc9e`. | pattern scan |
| `0x7e1abcc2` | 1 | `cmp_state_enter_32_7e1abcc2` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e1abd17`. | pattern scan |
| `0x7e1abd3b` | 1 | `cmp_state_enter_34_7e1abd3b` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e1abd90`. | pattern scan |
| `0x7e1abdb4` | 1 | `cmp_state_enter_36_7e1abdb4` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e1abe09`. | pattern scan |
| `0x7e1abeff` | 1 | `cmp_state_enter_38_7e1abeff` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e1abf54`. | pattern scan |
| `0x7e1abf78` | 1 | `cmp_state_enter_40_7e1abf78` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e1abfcd`. | pattern scan |
| `0x7e1abff1` | 1 | `cmp_state_enter_42_7e1abff1` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e1ac054`. | pattern scan |
| `0x7e1ac078` | 1 | `cmp_state_enter_44_7e1ac078` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e1ac0cd`. | pattern scan |
| `0x7e1ac0f1` | 1 | `cmp_state_enter_46_7e1ac0f1` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e1ac146`. | pattern scan |
| `0x7e1ae091` | 1 | `cmp_state_enter_11_7e1ae091` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e1ae0e6`. | pattern scan |
| `0x7e1ae13d` | 1 | `cmp_state_enter_13_7e1ae13d` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e1ae192`. | pattern scan |
| `0x7e1ae4a1` | 1 | `cmp_state_enter_50_7e1ae4a1` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e1ae4f6`. | pattern scan |
| `0x7e1ae5be` | 1 | `cmp_state_enter_52_7e1ae5be` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e1ae613`. | pattern scan |
| `0x7e1ae721` | 1 | `cmp_state_enter_54_7e1ae721` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e1ae776`. | pattern scan |
| `0x7e1ae88d` | 1 | `cmp_state_enter_56_7e1ae88d` | Cmp state-enter wrapper: sets the state word `+948 = 56`, then calls the state's body `0x7e1ae8e2`. | pattern scan |
| `0x7e1aea2a` | 1 | `cmp_state_enter_58_7e1aea2a` | Cmp state-enter wrapper: sets the state word `+948 = 58`, then calls the state's body `0x7e1aea7f`. | pattern scan |
| `0x7e1aeba9` | 1 | `cmp_state_enter_60_7e1aeba9` | Cmp state-enter wrapper: sets the state word `+948 = 60`, then calls the state's body `0x7e1aebfe`. | pattern scan |
| `0x7e1aed02` | 1 | `cmp_state_enter_62_7e1aed02` | Cmp state-enter wrapper: sets the state word `+948 = 62`, then calls the state's body `0x7e1aed57`. | pattern scan |
| `0x7e1aee6e` | 1 | `cmp_state_enter_64_7e1aee6e` | Cmp state-enter wrapper: sets the state word `+948 = 64`, then calls the state's body `0x7e1aeec3`. | pattern scan |
| `0x7e1aefa6` | 1 | `cmp_state_enter_66_7e1aefa6` | Cmp state-enter wrapper: sets the state word `+948 = 66`, then calls the state's body `0x7e1aeffb`. | pattern scan |
| `0x7e1af102` | 1 | `cmp_state_enter_68_7e1af102` | Cmp state-enter wrapper: sets the state word `+948 = 68`, then calls the state's body `0x7e1af157`. | pattern scan |
| `0x7e1af25e` | 1 | `cmp_state_enter_70_7e1af25e` | Cmp state-enter wrapper: sets the state word `+948 = 70`, then calls the state's body `0x7e1af2b3`. | pattern scan |
| `0x7e1af3b7` | 1 | `cmp_state_enter_72_7e1af3b7` | Cmp state-enter wrapper: sets the state word `+948 = 72`, then calls the state's body `0x7e1af40c`. | pattern scan |
| `0x7e1af51b` | 1 | `cmp_state_enter_74_7e1af51b` | Cmp state-enter wrapper: sets the state word `+948 = 74`, then calls the state's body `0x7e1af570`. | pattern scan |
| `0x7e1af69f` | 1 | `cmp_state_enter_16_7e1af69f` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e1af6f4`. | pattern scan |
| `0x7e1af718` | 1 | `cmp_state_enter_18_7e1af718` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e1af76d`. | pattern scan |
| `0x7e1af791` | 1 | `cmp_state_enter_20_7e1af791` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e1af7e6`. | pattern scan |
| `0x7e1af80a` | 1 | `cmp_state_enter_22_7e1af80a` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e1af85f`. | pattern scan |
| `0x7e1af883` | 1 | `cmp_state_enter_24_7e1af883` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e1af8d8`. | pattern scan |
| `0x7e1af8fc` | 1 | `cmp_state_enter_26_7e1af8fc` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e1af951`. | pattern scan |
| `0x7e1af975` | 1 | `cmp_state_enter_28_7e1af975` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e1af9ca`. | pattern scan |
| `0x7e1af9ee` | 1 | `cmp_state_enter_30_7e1af9ee` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e1afa43`. | pattern scan |
| `0x7e1afa67` | 1 | `cmp_state_enter_32_7e1afa67` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e1afabc`. | pattern scan |
| `0x7e1afae0` | 1 | `cmp_state_enter_34_7e1afae0` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e1afb35`. | pattern scan |
| `0x7e1afb59` | 1 | `cmp_state_enter_36_7e1afb59` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e1afbae`. | pattern scan |
| `0x7e1afca4` | 1 | `cmp_state_enter_38_7e1afca4` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e1afcf9`. | pattern scan |
| `0x7e1afd1d` | 1 | `cmp_state_enter_40_7e1afd1d` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e1afd72`. | pattern scan |
| `0x7e1afd96` | 1 | `cmp_state_enter_42_7e1afd96` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e1afdf9`. | pattern scan |
| `0x7e1afe1d` | 1 | `cmp_state_enter_44_7e1afe1d` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e1afe72`. | pattern scan |
| `0x7e1afe96` | 1 | `cmp_state_enter_46_7e1afe96` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e1afeeb`. | pattern scan |
| `0x7e1b1fea` | 1 | `cmp_state_enter_11_7e1b1fea` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e1b203f`. | pattern scan |
| `0x7e1b2096` | 1 | `cmp_state_enter_13_7e1b2096` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e1b20eb`. | pattern scan |
| `0x7e1b2386` | 1 | `cmp_state_enter_50_7e1b2386` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e1b23db`. | pattern scan |
| `0x7e1b24b2` | 1 | `cmp_state_enter_52_7e1b24b2` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e1b2507`. | pattern scan |
| `0x7e1b25b4` | 1 | `cmp_state_enter_54_7e1b25b4` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e1b2609`. | pattern scan |
| `0x7e1b2dc5` | 1 | `cmp_state_enter_66_7e1b2dc5` | Cmp state-enter wrapper: sets the state word `+948 = 66`, then calls the state's body `0x7e1b2e1a`. | pattern scan |
| `0x7e1b2ec4` | 1 | `cmp_state_enter_68_7e1b2ec4` | Cmp state-enter wrapper: sets the state word `+948 = 68`, then calls the state's body `0x7e1b2f19`. | pattern scan |
| `0x7e1b2fdb` | 1 | `cmp_state_enter_70_7e1b2fdb` | Cmp state-enter wrapper: sets the state word `+948 = 70`, then calls the state's body `0x7e1b3030`. | pattern scan |
| `0x7e1b317d` | 1 | `cmp_state_enter_16_7e1b317d` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e1b31d2`. | pattern scan |
| `0x7e1b31f6` | 1 | `cmp_state_enter_18_7e1b31f6` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e1b324b`. | pattern scan |
| `0x7e1b326f` | 1 | `cmp_state_enter_20_7e1b326f` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e1b32c4`. | pattern scan |
| `0x7e1b32e8` | 1 | `cmp_state_enter_22_7e1b32e8` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e1b333d`. | pattern scan |
| `0x7e1b3361` | 1 | `cmp_state_enter_24_7e1b3361` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e1b33b6`. | pattern scan |
| `0x7e1b33da` | 1 | `cmp_state_enter_26_7e1b33da` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e1b342f`. | pattern scan |
| `0x7e1b3453` | 1 | `cmp_state_enter_28_7e1b3453` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e1b34a8`. | pattern scan |
| `0x7e1b34cc` | 1 | `cmp_state_enter_30_7e1b34cc` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e1b3521`. | pattern scan |
| `0x7e1b3545` | 1 | `cmp_state_enter_32_7e1b3545` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e1b359a`. | pattern scan |
| `0x7e1b35be` | 1 | `cmp_state_enter_34_7e1b35be` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e1b3613`. | pattern scan |
| `0x7e1b3637` | 1 | `cmp_state_enter_36_7e1b3637` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e1b368c`. | pattern scan |
| `0x7e1b3782` | 1 | `cmp_state_enter_38_7e1b3782` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e1b37d7`. | pattern scan |
| `0x7e1b37fb` | 1 | `cmp_state_enter_40_7e1b37fb` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e1b3850`. | pattern scan |
| `0x7e1b3874` | 1 | `cmp_state_enter_42_7e1b3874` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e1b38d7`. | pattern scan |
| `0x7e1b38fb` | 1 | `cmp_state_enter_44_7e1b38fb` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e1b3950`. | pattern scan |
| `0x7e1b3974` | 1 | `cmp_state_enter_46_7e1b3974` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e1b39c9`. | pattern scan |
| `0x7e1b647b` | 1 | `cmp_state_enter_50_7e1b647b` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e1b64d0`. | pattern scan |
| `0x7e1b6599` | 1 | `cmp_state_enter_11_7e1b6599` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e1b65ee`. | pattern scan |
| `0x7e1b6645` | 1 | `cmp_state_enter_52_7e1b6645` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e1b669a`. | pattern scan |
| `0x7e1b6772` | 1 | `cmp_state_enter_13_7e1b6772` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e1b67c7`. | pattern scan |
| `0x7e1b67eb` | 1 | `cmp_state_enter_54_7e1b67eb` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e1b6840`. | pattern scan |
| `0x7e1b6ba7` | 1 | `cmp_state_enter_56_7e1b6ba7` | Cmp state-enter wrapper: sets the state word `+948 = 56`, then calls the state's body `0x7e1b6bfc`. | pattern scan |
| `0x7e1b6d62` | 1 | `cmp_state_enter_58_7e1b6d62` | Cmp state-enter wrapper: sets the state word `+948 = 58`, then calls the state's body `0x7e1b700d`. | pattern scan |
| `0x7e1b71b2` | 1 | `cmp_state_enter_16_7e1b71b2` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e1b7207`. | pattern scan |
| `0x7e1b722b` | 1 | `cmp_state_enter_18_7e1b722b` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e1b7280`. | pattern scan |
| `0x7e1b72a4` | 1 | `cmp_state_enter_20_7e1b72a4` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e1b72f9`. | pattern scan |
| `0x7e1b731d` | 1 | `cmp_state_enter_61_7e1b731d` | Cmp state-enter wrapper: sets the state word `+948 = 61`, then calls the state's body `0x7e1b7372`. | pattern scan |
| `0x7e1b742e` | 1 | `cmp_state_enter_22_7e1b742e` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e1b7483`. | pattern scan |
| `0x7e1b74a7` | 1 | `cmp_state_enter_24_7e1b74a7` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e1b74fc`. | pattern scan |
| `0x7e1b7520` | 1 | `cmp_state_enter_63_7e1b7520` | Cmp state-enter wrapper: sets the state word `+948 = 63`, then calls the state's body `0x7e1b7575`. | pattern scan |
| `0x7e1b7636` | 1 | `cmp_state_enter_26_7e1b7636` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e1b768b`. | pattern scan |
| `0x7e1b76af` | 1 | `cmp_state_enter_28_7e1b76af` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e1b7704`. | pattern scan |
| `0x7e1b7728` | 1 | `cmp_state_enter_65_7e1b7728` | Cmp state-enter wrapper: sets the state word `+948 = 65`, then calls the state's body `0x7e1b777d`. | pattern scan |
| `0x7e1b783f` | 1 | `cmp_state_enter_30_7e1b783f` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e1b7894`. | pattern scan |
| `0x7e1b78b8` | 1 | `cmp_state_enter_32_7e1b78b8` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e1b790d`. | pattern scan |
| `0x7e1b7931` | 1 | `cmp_state_enter_34_7e1b7931` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e1b7986`. | pattern scan |
| `0x7e1b79aa` | 1 | `cmp_state_enter_67_7e1b79aa` | Cmp state-enter wrapper: sets the state word `+948 = 67`, then calls the state's body `0x7e1b79ff`. | pattern scan |
| `0x7e1b7abe` | 1 | `cmp_state_enter_69_7e1b7abe` | Cmp state-enter wrapper: sets the state word `+948 = 69`, then calls the state's body `0x7e1b7b13`. | pattern scan |
| `0x7e1b7b73` | 1 | `cmp_state_enter_36_7e1b7b73` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e1b7bc8`. | pattern scan |
| `0x7e1b7cbe` | 1 | `cmp_state_enter_38_7e1b7cbe` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e1b7d13`. | pattern scan |
| `0x7e1b7d37` | 1 | `cmp_state_enter_71_7e1b7d37` | Cmp state-enter wrapper: sets the state word `+948 = 71`, then calls the state's body `0x7e1b7d8c`. | pattern scan |
| `0x7e1b7ea2` | 1 | `cmp_state_enter_40_7e1b7ea2` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e1b7ef7`. | pattern scan |
| `0x7e1b7f1b` | 1 | `cmp_state_enter_42_7e1b7f1b` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e1b7f7e`. | pattern scan |
| `0x7e1b7fa2` | 1 | `cmp_state_enter_44_7e1b7fa2` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e1b7ff7`. | pattern scan |
| `0x7e1b81d5` | 1 | `cmp_state_enter_46_7e1b81d5` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e1b822a`. | pattern scan |
| `0x7e1b824e` | 1 | `cmp_state_enter_75_7e1b824e` | Cmp state-enter wrapper: sets the state word `+948 = 75`, then calls the state's body `0x7e1b82a3`. | pattern scan |
| `0x7e1bb53c` | 1 | `cmp_state_enter_11_7e1bb53c` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e1bb591`. | pattern scan |
| `0x7e1bb5e8` | 1 | `cmp_state_enter_13_7e1bb5e8` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e1bb63d`. | pattern scan |
| `0x7e1bb846` | 1 | `cmp_state_enter_16_7e1bb846` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e1bb89b`. | pattern scan |
| `0x7e1bb8bf` | 1 | `cmp_state_enter_18_7e1bb8bf` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e1bb914`. | pattern scan |
| `0x7e1bb938` | 1 | `cmp_state_enter_20_7e1bb938` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e1bb98d`. | pattern scan |
| `0x7e1bb9b1` | 1 | `cmp_state_enter_22_7e1bb9b1` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e1bba06`. | pattern scan |
| `0x7e1bba2b` | 1 | `cmp_state_enter_24_7e1bba2b` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e1bba80`. | pattern scan |
| `0x7e1bbaa4` | 1 | `cmp_state_enter_26_7e1bbaa4` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e1bbaf9`. | pattern scan |
| `0x7e1bbb1e` | 1 | `cmp_state_enter_28_7e1bbb1e` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e1bbb73`. | pattern scan |
| `0x7e1bbb98` | 1 | `cmp_state_enter_30_7e1bbb98` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e1bbbed`. | pattern scan |
| `0x7e1bbc12` | 1 | `cmp_state_enter_32_7e1bbc12` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e1bbc67`. | pattern scan |
| `0x7e1bbc8b` | 1 | `cmp_state_enter_34_7e1bbc8b` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e1bbce0`. | pattern scan |
| `0x7e1bbd04` | 1 | `cmp_state_enter_36_7e1bbd04` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e1bbd59`. | pattern scan |
| `0x7e1bbe4f` | 1 | `cmp_state_enter_38_7e1bbe4f` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e1bbea4`. | pattern scan |
| `0x7e1bbec9` | 1 | `cmp_state_enter_40_7e1bbec9` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e1bbf1e`. | pattern scan |
| `0x7e1bbf42` | 1 | `cmp_state_enter_42_7e1bbf42` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e1bbfa6`. | pattern scan |
| `0x7e1bbfcb` | 1 | `cmp_state_enter_44_7e1bbfcb` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e1bc020`. | pattern scan |
| `0x7e1bc044` | 1 | `cmp_state_enter_46_7e1bc044` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e1bc099`. | pattern scan |
| `0x7e1bf320` | 1 | `cmp_state_enter_11_7e1bf320` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e1bf375`. | pattern scan |
| `0x7e1bf3cc` | 1 | `cmp_state_enter_50_7e1bf3cc` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e1bf421`. | pattern scan |
| `0x7e1bf66b` | 1 | `cmp_state_enter_53_7e1bf66b` | Cmp state-enter wrapper: sets the state word `+948 = 53`, then calls the state's body `0x7e1bf6c0`. | pattern scan |
| `0x7e1bfa26` | 1 | `cmp_state_enter_55_7e1bfa26` | Cmp state-enter wrapper: sets the state word `+948 = 55`, then calls the state's body `0x7e1bfa7b`. | pattern scan |
| `0x7e1bfb3e` | 1 | `cmp_state_enter_57_7e1bfb3e` | Cmp state-enter wrapper: sets the state word `+948 = 57`, then calls the state's body `0x7e1bfb93`. | pattern scan |
| `0x7e1bfc5b` | 1 | `cmp_state_enter_59_7e1bfc5b` | Cmp state-enter wrapper: sets the state word `+948 = 59`, then calls the state's body `0x7e1bfcb0`. | pattern scan |
| `0x7e1bfd9e` | 1 | `cmp_state_enter_61_7e1bfd9e` | Cmp state-enter wrapper: sets the state word `+948 = 61`, then calls the state's body `0x7e1bfdf3`. | pattern scan |
| `0x7e1bfee8` | 1 | `cmp_state_enter_63_7e1bfee8` | Cmp state-enter wrapper: sets the state word `+948 = 63`, then calls the state's body `0x7e1bff3d`. | pattern scan |
| `0x7e1c00f5` | 1 | `cmp_state_enter_65_7e1c00f5` | Cmp state-enter wrapper: sets the state word `+948 = 65`, then calls the state's body `0x7e1c014a`. | pattern scan |
| `0x7e1c0392` | 1 | `cmp_state_enter_68_7e1c0392` | Cmp state-enter wrapper: sets the state word `+948 = 68`, then calls the state's body `0x7e1c03e7`. | pattern scan |
| `0x7e1c048c` | 1 | `cmp_state_enter_70_7e1c048c` | Cmp state-enter wrapper: sets the state word `+948 = 70`, then calls the state's body `0x7e1c04e1`. | pattern scan |
| `0x7e1c05d8` | 1 | `cmp_state_enter_72_7e1c05d8` | Cmp state-enter wrapper: sets the state word `+948 = 72`, then calls the state's body `0x7e1c062d`. | pattern scan |
| `0x7e1c071b` | 1 | `cmp_state_enter_74_7e1c071b` | Cmp state-enter wrapper: sets the state word `+948 = 74`, then calls the state's body `0x7e1c0770`. | pattern scan |
| `0x7e1c0842` | 1 | `cmp_state_enter_76_7e1c0842` | Cmp state-enter wrapper: sets the state word `+948 = 76`, then calls the state's body `0x7e1c0897`. | pattern scan |
| `0x7e1c09a1` | 1 | `cmp_state_enter_78_7e1c09a1` | Cmp state-enter wrapper: sets the state word `+948 = 78`, then calls the state's body `0x7e1c09f6`. | pattern scan |
| `0x7e1c0ad3` | 1 | `cmp_state_enter_80_7e1c0ad3` | Cmp state-enter wrapper: sets the state word `+948 = 80`, then calls the state's body `0x7e1c0b28`. | pattern scan |
| `0x7e1c0c69` | 1 | `cmp_state_enter_82_7e1c0c69` | Cmp state-enter wrapper: sets the state word `+948 = 82`, then calls the state's body `0x7e1c0cbe`. | pattern scan |
| `0x7e1c0da0` | 1 | `cmp_state_enter_84_7e1c0da0` | Cmp state-enter wrapper: sets the state word `+948 = 84`, then calls the state's body `0x7e1c0df5`. | pattern scan |
| `0x7e1c1078` | 1 | `cmp_state_enter_13_7e1c1078` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e1c10cd`. | pattern scan |
| `0x7e1c144c` | 1 | `cmp_state_enter_16_7e1c144c` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e1c14a1`. | pattern scan |
| `0x7e1c14c5` | 1 | `cmp_state_enter_18_7e1c14c5` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e1c151a`. | pattern scan |
| `0x7e1c153e` | 1 | `cmp_state_enter_20_7e1c153e` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e1c1593`. | pattern scan |
| `0x7e1c15b7` | 1 | `cmp_state_enter_22_7e1c15b7` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e1c160c`. | pattern scan |
| `0x7e1c1630` | 1 | `cmp_state_enter_24_7e1c1630` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e1c1685`. | pattern scan |
| `0x7e1c16a9` | 1 | `cmp_state_enter_26_7e1c16a9` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e1c16fe`. | pattern scan |
| `0x7e1c1722` | 1 | `cmp_state_enter_28_7e1c1722` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e1c1777`. | pattern scan |
| `0x7e1c179b` | 1 | `cmp_state_enter_30_7e1c179b` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e1c17f0`. | pattern scan |
| `0x7e1c1814` | 1 | `cmp_state_enter_32_7e1c1814` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e1c1869`. | pattern scan |
| `0x7e1c188d` | 1 | `cmp_state_enter_34_7e1c188d` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e1c18e2`. | pattern scan |
| `0x7e1c1906` | 1 | `cmp_state_enter_36_7e1c1906` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e1c195b`. | pattern scan |
| `0x7e1c1a51` | 1 | `cmp_state_enter_38_7e1c1a51` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e1c1aa6`. | pattern scan |
| `0x7e1c1aca` | 1 | `cmp_state_enter_40_7e1c1aca` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e1c1b1f`. | pattern scan |
| `0x7e1c1b43` | 1 | `cmp_state_enter_42_7e1c1b43` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e1c1ba6`. | pattern scan |
| `0x7e1c1bca` | 1 | `cmp_state_enter_44_7e1c1bca` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e1c1c1f`. | pattern scan |
| `0x7e1c1c43` | 1 | `cmp_state_enter_46_7e1c1c43` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e1c1c98`. | pattern scan |
| `0x7e1c3200` | 1 | `cmp_state_enter_11_7e1c3200` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e1c3255`. | pattern scan |
| `0x7e1c32ac` | 1 | `cmp_state_enter_13_7e1c32ac` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e1c3301`. | pattern scan |
| `0x7e1c350a` | 1 | `cmp_state_enter_16_7e1c350a` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e1c355f`. | pattern scan |
| `0x7e1c3583` | 1 | `cmp_state_enter_18_7e1c3583` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e1c35d8`. | pattern scan |
| `0x7e1c35fc` | 1 | `cmp_state_enter_20_7e1c35fc` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e1c3651`. | pattern scan |
| `0x7e1c3675` | 1 | `cmp_state_enter_22_7e1c3675` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e1c36ca`. | pattern scan |
| `0x7e1c36ee` | 1 | `cmp_state_enter_24_7e1c36ee` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e1c3743`. | pattern scan |
| `0x7e1c3767` | 1 | `cmp_state_enter_26_7e1c3767` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e1c37bc`. | pattern scan |
| `0x7e1c37e0` | 1 | `cmp_state_enter_28_7e1c37e0` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e1c3835`. | pattern scan |
| `0x7e1c3859` | 1 | `cmp_state_enter_30_7e1c3859` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e1c38ae`. | pattern scan |
| `0x7e1c38d2` | 1 | `cmp_state_enter_32_7e1c38d2` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e1c3927`. | pattern scan |
| `0x7e1c394b` | 1 | `cmp_state_enter_34_7e1c394b` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e1c39a0`. | pattern scan |
| `0x7e1c39c4` | 1 | `cmp_state_enter_36_7e1c39c4` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e1c3a19`. | pattern scan |
| `0x7e1c3b0f` | 1 | `cmp_state_enter_38_7e1c3b0f` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e1c3b64`. | pattern scan |
| `0x7e1c3b88` | 1 | `cmp_state_enter_40_7e1c3b88` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e1c3bdd`. | pattern scan |
| `0x7e1c3c01` | 1 | `cmp_state_enter_42_7e1c3c01` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e1c3c64`. | pattern scan |
| `0x7e1c3c88` | 1 | `cmp_state_enter_44_7e1c3c88` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e1c3cdd`. | pattern scan |
| `0x7e1c3d01` | 1 | `cmp_state_enter_46_7e1c3d01` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e1c3d56`. | pattern scan |
| `0x7e1c657a` | 1 | `cmp_state_enter_50_7e1c657a` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e1c65cf`. | pattern scan |
| `0x7e1c669f` | 1 | `cmp_state_enter_11_7e1c669f` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e1c66f4`. | pattern scan |
| `0x7e1c674b` | 1 | `cmp_state_enter_52_7e1c674b` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e1c67a0`. | pattern scan |
| `0x7e1c687e` | 1 | `cmp_state_enter_54_7e1c687e` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e1c68d3`. | pattern scan |
| `0x7e1c698b` | 1 | `cmp_state_enter_13_7e1c698b` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e1c69e0`. | pattern scan |
| `0x7e1c6a04` | 1 | `cmp_state_enter_56_7e1c6a04` | Cmp state-enter wrapper: sets the state word `+948 = 56`, then calls the state's body `0x7e1c6a59`. | pattern scan |
| `0x7e1c6f70` | 1 | `cmp_state_enter_58_7e1c6f70` | Cmp state-enter wrapper: sets the state word `+948 = 58`, then calls the state's body `0x7e1c71f0`. | pattern scan |
| `0x7e1c736a` | 1 | `cmp_state_enter_16_7e1c736a` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e1c73bf`. | pattern scan |
| `0x7e1c73e3` | 1 | `cmp_state_enter_18_7e1c73e3` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e1c7438`. | pattern scan |
| `0x7e1c745c` | 1 | `cmp_state_enter_20_7e1c745c` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e1c74b1`. | pattern scan |
| `0x7e1c74d5` | 1 | `cmp_state_enter_61_7e1c74d5` | Cmp state-enter wrapper: sets the state word `+948 = 61`, then calls the state's body `0x7e1c752a`. | pattern scan |
| `0x7e1c75f1` | 1 | `cmp_state_enter_63_7e1c75f1` | Cmp state-enter wrapper: sets the state word `+948 = 63`, then calls the state's body `0x7e1c7646`. | pattern scan |
| `0x7e1c78f8` | 1 | `cmp_state_enter_22_7e1c78f8` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e1c794d`. | pattern scan |
| `0x7e1c7971` | 1 | `cmp_state_enter_24_7e1c7971` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e1c79c6`. | pattern scan |
| `0x7e1c79ea` | 1 | `cmp_state_enter_65_7e1c79ea` | Cmp state-enter wrapper: sets the state word `+948 = 65`, then calls the state's body `0x7e1c7a3f`. | pattern scan |
| `0x7e1c7b3a` | 1 | `cmp_state_enter_26_7e1c7b3a` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e1c7b8f`. | pattern scan |
| `0x7e1c7bb3` | 1 | `cmp_state_enter_28_7e1c7bb3` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e1c7c08`. | pattern scan |
| `0x7e1c7c2c` | 1 | `cmp_state_enter_30_7e1c7c2c` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e1c7c81`. | pattern scan |
| `0x7e1c7ca5` | 1 | `cmp_state_enter_32_7e1c7ca5` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e1c7cfa`. | pattern scan |
| `0x7e1c7d1e` | 1 | `cmp_state_enter_34_7e1c7d1e` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e1c7d73`. | pattern scan |
| `0x7e1c7d97` | 1 | `cmp_state_enter_67_7e1c7d97` | Cmp state-enter wrapper: sets the state word `+948 = 67`, then calls the state's body `0x7e1c7dec`. | pattern scan |
| `0x7e1c7fad` | 1 | `cmp_state_enter_36_7e1c7fad` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e1c8002`. | pattern scan |
| `0x7e1c80f8` | 1 | `cmp_state_enter_69_7e1c80f8` | Cmp state-enter wrapper: sets the state word `+948 = 69`, then calls the state's body `0x7e1c814d`. | pattern scan |
| `0x7e1c81f3` | 1 | `cmp_state_enter_38_7e1c81f3` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e1c8248`. | pattern scan |
| `0x7e1c826c` | 1 | `cmp_state_enter_40_7e1c826c` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e1c82c1`. | pattern scan |
| `0x7e1c82e5` | 1 | `cmp_state_enter_42_7e1c82e5` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e1c8348`. | pattern scan |
| `0x7e1c836c` | 1 | `cmp_state_enter_71_7e1c836c` | Cmp state-enter wrapper: sets the state word `+948 = 71`, then calls the state's body `0x7e1c83c1`. | pattern scan |
| `0x7e1c85d0` | 1 | `cmp_state_enter_73_7e1c85d0` | Cmp state-enter wrapper: sets the state word `+948 = 73`, then calls the state's body `0x7e1c8625`. | pattern scan |
| `0x7e1c86f0` | 1 | `cmp_state_enter_44_7e1c86f0` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e1c8745`. | pattern scan |
| `0x7e1c8769` | 1 | `cmp_state_enter_75_7e1c8769` | Cmp state-enter wrapper: sets the state word `+948 = 75`, then calls the state's body `0x7e1c87be`. | pattern scan |
| `0x7e1c8897` | 1 | `cmp_state_enter_46_7e1c8897` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e1c88ec`. | pattern scan |
| `0x7e1c8910` | 1 | `cmp_state_enter_77_7e1c8910` | Cmp state-enter wrapper: sets the state word `+948 = 77`, then calls the state's body `0x7e1c8965`. | pattern scan |
| `0x7e1c8a62` | 1 | `cmp_state_enter_79_7e1c8a62` | Cmp state-enter wrapper: sets the state word `+948 = 79`, then calls the state's body `0x7e1c8ab7`. | pattern scan |
| `0x7e1ca4ac` | 1 | `cmp_state_enter_11_7e1ca4ac` | Cmp state-enter wrapper: sets the state word `+948 = 11`, then calls the state's body `0x7e1ca501`. | pattern scan |
| `0x7e1ca558` | 1 | `cmp_state_enter_50_7e1ca558` | Cmp state-enter wrapper: sets the state word `+948 = 50`, then calls the state's body `0x7e1ca5ad`. | pattern scan |
| `0x7e1ca652` | 1 | `cmp_state_enter_52_7e1ca652` | Cmp state-enter wrapper: sets the state word `+948 = 52`, then calls the state's body `0x7e1ca6a7`. | pattern scan |
| `0x7e1ca8fa` | 1 | `cmp_state_enter_13_7e1ca8fa` | Cmp state-enter wrapper: sets the state word `+948 = 13`, then calls the state's body `0x7e1ca94f`. | pattern scan |
| `0x7e1cac08` | 1 | `cmp_state_enter_54_7e1cac08` | Cmp state-enter wrapper: sets the state word `+948 = 54`, then calls the state's body `0x7e1cac5d`. | pattern scan |
| `0x7e1cadbf` | 1 | `cmp_state_enter_16_7e1cadbf` | Cmp state-enter wrapper: sets the state word `+948 = 16`, then calls the state's body `0x7e1cae14`. | pattern scan |
| `0x7e1cae38` | 1 | `cmp_state_enter_18_7e1cae38` | Cmp state-enter wrapper: sets the state word `+948 = 18`, then calls the state's body `0x7e1cae8d`. | pattern scan |
| `0x7e1caeb1` | 1 | `cmp_state_enter_20_7e1caeb1` | Cmp state-enter wrapper: sets the state word `+948 = 20`, then calls the state's body `0x7e1caf06`. | pattern scan |
| `0x7e1caf2a` | 1 | `cmp_state_enter_56_7e1caf2a` | Cmp state-enter wrapper: sets the state word `+948 = 56`, then calls the state's body `0x7e1caf7f`. | pattern scan |
| `0x7e1cb1a5` | 1 | `cmp_state_enter_22_7e1cb1a5` | Cmp state-enter wrapper: sets the state word `+948 = 22`, then calls the state's body `0x7e1cb1fa`. | pattern scan |
| `0x7e1cb21e` | 1 | `cmp_state_enter_24_7e1cb21e` | Cmp state-enter wrapper: sets the state word `+948 = 24`, then calls the state's body `0x7e1cb273`. | pattern scan |
| `0x7e1cb297` | 1 | `cmp_state_enter_58_7e1cb297` | Cmp state-enter wrapper: sets the state word `+948 = 58`, then calls the state's body `0x7e1cb2ec`. | pattern scan |
| `0x7e1cb3ae` | 1 | `cmp_state_enter_26_7e1cb3ae` | Cmp state-enter wrapper: sets the state word `+948 = 26`, then calls the state's body `0x7e1cb403`. | pattern scan |
| `0x7e1cb427` | 1 | `cmp_state_enter_28_7e1cb427` | Cmp state-enter wrapper: sets the state word `+948 = 28`, then calls the state's body `0x7e1cb47c`. | pattern scan |
| `0x7e1cb4a0` | 1 | `cmp_state_enter_60_7e1cb4a0` | Cmp state-enter wrapper: sets the state word `+948 = 60`, then calls the state's body `0x7e1cb4f5`. | pattern scan |
| `0x7e1cb5b7` | 1 | `cmp_state_enter_30_7e1cb5b7` | Cmp state-enter wrapper: sets the state word `+948 = 30`, then calls the state's body `0x7e1cb60c`. | pattern scan |
| `0x7e1cb630` | 1 | `cmp_state_enter_32_7e1cb630` | Cmp state-enter wrapper: sets the state word `+948 = 32`, then calls the state's body `0x7e1cb685`. | pattern scan |
| `0x7e1cb6a9` | 1 | `cmp_state_enter_34_7e1cb6a9` | Cmp state-enter wrapper: sets the state word `+948 = 34`, then calls the state's body `0x7e1cb6fe`. | pattern scan |
| `0x7e1cb722` | 1 | `cmp_state_enter_62_7e1cb722` | Cmp state-enter wrapper: sets the state word `+948 = 62`, then calls the state's body `0x7e1cb777`. | pattern scan |
| `0x7e1cb839` | 1 | `cmp_state_enter_36_7e1cb839` | Cmp state-enter wrapper: sets the state word `+948 = 36`, then calls the state's body `0x7e1cb88e`. | pattern scan |
| `0x7e1cb984` | 1 | `cmp_state_enter_38_7e1cb984` | Cmp state-enter wrapper: sets the state word `+948 = 38`, then calls the state's body `0x7e1cb9d9`. | pattern scan |
| `0x7e1cb9fd` | 1 | `cmp_state_enter_40_7e1cb9fd` | Cmp state-enter wrapper: sets the state word `+948 = 40`, then calls the state's body `0x7e1cba52`. | pattern scan |
| `0x7e1cba76` | 1 | `cmp_state_enter_42_7e1cba76` | Cmp state-enter wrapper: sets the state word `+948 = 42`, then calls the state's body `0x7e1cbad9`. | pattern scan |
| `0x7e1cbafd` | 1 | `cmp_state_enter_44_7e1cbafd` | Cmp state-enter wrapper: sets the state word `+948 = 44`, then calls the state's body `0x7e1cbb52`. | pattern scan |
| `0x7e1cbb76` | 1 | `cmp_state_enter_46_7e1cbb76` | Cmp state-enter wrapper: sets the state word `+948 = 46`, then calls the state's body `0x7e1cbbcb`. | pattern scan |
| `0x7e1cbbef` | 1 | `cmp_state_enter_64_7e1cbbef` | Cmp state-enter wrapper: sets the state word `+948 = 64`, then calls the state's body `0x7e1cbc44`. | pattern scan |

## Entry stubs and one-line field writers (pattern families)
Listed 2026-11-12 from block-0 function entries whose bytes match exactly:
- **`entry_thunk_<addr>`** (2102): `call <addr+8>,[regs],N; ret` — an 8-byte stub that calls the body placed
  directly after it. The compiler emits these in front of bodies that save registers; the real work is in the
  body, so a stub's name says only where its body is.
- **`obj_clear_f<off>_<addr>`** (894): `clr d0; mov d0,(off,a0); retf` — zero one 32-bit field. In the Cmp
  component classes these clear the per-state slots `+952`…`+1020` that follow the state word `+948`.
- **`obj_set1_f<off>_<addr>`** (41): `mov 1,d0; mov d0,(off,a0); retf` — set one field to 1.

| address | xrefs | symbol | role | source |
|---|---|---|---|---|
| `0x7d9dbb50` | 2 | `entry_thunk_7d9dbb50` | `call` to the body directly after it (`0x7d9dbb58`, register-save mask `0xf0`, frame 24) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfcb979` | 1 | `entry_thunk_7dfcb979` | `call` to the body directly after it (`0x7dfcb981`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfcb9b4` | 2 | `entry_thunk_7dfcb9b4` | `call` to the body directly after it (`0x7dfcb9bc`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfcba63` | 2 | `entry_thunk_7dfcba63` | `call` to the body directly after it (`0x7dfcba6b`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfcf8b2` | 1 | `entry_thunk_7dfcf8b2` | `call` to the body directly after it (`0x7dfcf8ba`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfcf8ed` | 2 | `entry_thunk_7dfcf8ed` | `call` to the body directly after it (`0x7dfcf8f5`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfcf99c` | 3 | `entry_thunk_7dfcf99c` | `call` to the body directly after it (`0x7dfcf9a4`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd0ae7` | 1 | `entry_thunk_7dfd0ae7` | `call` to the body directly after it (`0x7dfd0aef`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd0b22` | 1 | `entry_thunk_7dfd0b22` | `call` to the body directly after it (`0x7dfd0b2a`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd0b74` | 2 | `entry_thunk_7dfd0b74` | `call` to the body directly after it (`0x7dfd0b7c`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd0de3` | 1 | `entry_thunk_7dfd0de3` | `call` to the body directly after it (`0x7dfd0deb`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd0e1e` | 1 | `entry_thunk_7dfd0e1e` | `call` to the body directly after it (`0x7dfd0e26`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd0e70` | 2 | `entry_thunk_7dfd0e70` | `call` to the body directly after it (`0x7dfd0e78`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd1111` | 1 | `entry_thunk_7dfd1111` | `call` to the body directly after it (`0x7dfd1119`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd114c` | 2 | `entry_thunk_7dfd114c` | `call` to the body directly after it (`0x7dfd1154`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd11f9` | 3 | `entry_thunk_7dfd11f9` | `call` to the body directly after it (`0x7dfd1201`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd5240` | 1 | `entry_thunk_7dfd5240` | `call` to the body directly after it (`0x7dfd5248`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd5286` | 2 | `entry_thunk_7dfd5286` | `call` to the body directly after it (`0x7dfd528e`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd5403` | 1 | `entry_thunk_7dfd5403` | `call` to the body directly after it (`0x7dfd540b`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd549a` | 3 | `entry_thunk_7dfd549a` | `call` to the body directly after it (`0x7dfd54a2`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd626a` | 1 | `entry_thunk_7dfd626a` | `call` to the body directly after it (`0x7dfd6272`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd62a5` | 1 | `entry_thunk_7dfd62a5` | `call` to the body directly after it (`0x7dfd62ad`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd62f7` | 2 | `entry_thunk_7dfd62f7` | `call` to the body directly after it (`0x7dfd62ff`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd6a4b` | 1 | `entry_thunk_7dfd6a4b` | `call` to the body directly after it (`0x7dfd6a53`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd6a86` | 1 | `entry_thunk_7dfd6a86` | `call` to the body directly after it (`0x7dfd6a8e`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfd6ad8` | 2 | `entry_thunk_7dfd6ad8` | `call` to the body directly after it (`0x7dfd6ae0`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfe778f` | 1 | `entry_thunk_7dfe778f` | `call` to the body directly after it (`0x7dfe7797`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfe77d5` | 2 | `entry_thunk_7dfe77d5` | `call` to the body directly after it (`0x7dfe77dd`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfe7880` | 1 | `entry_thunk_7dfe7880` | `call` to the body directly after it (`0x7dfe7888`, register-save mask `0xa0`, frame 104) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfe78f6` | 3 | `entry_thunk_7dfe78f6` | `call` to the body directly after it (`0x7dfe78fe`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfe7f21` | 1 | `entry_thunk_7dfe7f21` | `call` to the body directly after it (`0x7dfe7f29`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfe7f5c` | 2 | `entry_thunk_7dfe7f5c` | `call` to the body directly after it (`0x7dfe7f64`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfe8007` | 2 | `entry_thunk_7dfe8007` | `call` to the body directly after it (`0x7dfe800f`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfe91bb` | 1 | `entry_thunk_7dfe91bb` | `call` to the body directly after it (`0x7dfe91c3`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfe91f6` | 1 | `entry_thunk_7dfe91f6` | `call` to the body directly after it (`0x7dfe91fe`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfe9248` | 2 | `entry_thunk_7dfe9248` | `call` to the body directly after it (`0x7dfe9250`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfea58b` | 1 | `entry_thunk_7dfea58b` | `call` to the body directly after it (`0x7dfea593`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfea5c6` | 2 | `entry_thunk_7dfea5c6` | `call` to the body directly after it (`0x7dfea5ce`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfea671` | 2 | `entry_thunk_7dfea671` | `call` to the body directly after it (`0x7dfea679`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfeadea` | 1 | `entry_thunk_7dfeadea` | `call` to the body directly after it (`0x7dfeadf2`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfeae25` | 1 | `entry_thunk_7dfeae25` | `call` to the body directly after it (`0x7dfeae2d`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfeae77` | 2 | `entry_thunk_7dfeae77` | `call` to the body directly after it (`0x7dfeae7f`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfed4eb` | 1 | `entry_thunk_7dfed4eb` | `call` to the body directly after it (`0x7dfed4f3`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfed526` | 1 | `entry_thunk_7dfed526` | `call` to the body directly after it (`0x7dfed52e`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dfed578` | 2 | `entry_thunk_7dfed578` | `call` to the body directly after it (`0x7dfed580`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7dff1928` | 1 | `entry_thunk_7dff1928` | `call` to the body directly after it (`0x7dff1930`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e036a87` | 1 | `entry_thunk_7e036a87` | `call` to the body directly after it (`0x7e036a8f`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e036ac2` | 2 | `entry_thunk_7e036ac2` | `call` to the body directly after it (`0x7e036aca`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e036b6f` | 3 | `entry_thunk_7e036b6f` | `call` to the body directly after it (`0x7e036b77`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0373a3` | 1 | `entry_thunk_7e0373a3` | `call` to the body directly after it (`0x7e0373ab`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0373de` | 1 | `entry_thunk_7e0373de` | `call` to the body directly after it (`0x7e0373e6`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e037430` | 2 | `entry_thunk_7e037430` | `call` to the body directly after it (`0x7e037438`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e037811` | 1 | `entry_thunk_7e037811` | `call` to the body directly after it (`0x7e037819`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e03784c` | 2 | `entry_thunk_7e03784c` | `call` to the body directly after it (`0x7e037854`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0378f9` | 3 | `entry_thunk_7e0378f9` | `call` to the body directly after it (`0x7e037901`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0401ae` | 2 | `entry_thunk_7e0401ae` | `call` to the body directly after it (`0x7e0401b6`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e04045c` | 2 | `entry_thunk_7e04045c` | `call` to the body directly after it (`0x7e040464`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0404c4` | 1 | `entry_thunk_7e0404c4` | `call` to the body directly after it (`0x7e0404cc`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0405ba` | 2 | `entry_thunk_7e0405ba` | `call` to the body directly after it (`0x7e0405c2`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e04064d` | 1 | `entry_thunk_7e04064d` | `call` to the body directly after it (`0x7e040655`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0406b4` | 1 | `entry_thunk_7e0406b4` | `call` to the body directly after it (`0x7e0406bc`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e040893` | 1 | `entry_thunk_7e040893` | `call` to the body directly after it (`0x7e04089b`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e04096a` | 1 | `entry_thunk_7e04096a` | `call` to the body directly after it (`0x7e040972`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0409fa` | 1 | `entry_thunk_7e0409fa` | `call` to the body directly after it (`0x7e040a02`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e040a64` | 2 | `entry_thunk_7e040a64` | `call` to the body directly after it (`0x7e040a6c`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e040b03` | 2 | `entry_thunk_7e040b03` | `call` to the body directly after it (`0x7e040b0b`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e040d2c` | 1 | `entry_thunk_7e040d2c` | `call` to the body directly after it (`0x7e040d34`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e040dbc` | 1 | `entry_thunk_7e040dbc` | `call` to the body directly after it (`0x7e040dc4`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e040e4f` | 3 | `entry_thunk_7e040e4f` | `call` to the body directly after it (`0x7e040e57`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e040ef3` | 1 | `entry_thunk_7e040ef3` | `call` to the body directly after it (`0x7e040efb`, register-save mask `0xb0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e040fed` | 1 | `entry_thunk_7e040fed` | `call` to the body directly after it (`0x7e040ff5`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e04105c` | 1 | `entry_thunk_7e04105c` | `call` to the body directly after it (`0x7e041064`, register-save mask `0xb0`, frame 36) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0412c5` | 1 | `entry_thunk_7e0412c5` | `call` to the body directly after it (`0x7e0412cd`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e041355` | 1 | `entry_thunk_7e041355` | `call` to the body directly after it (`0x7e04135d`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0413e8` | 1 | `entry_thunk_7e0413e8` | `call` to the body directly after it (`0x7e0413f0`, register-save mask `0xb0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0414e2` | 3 | `entry_thunk_7e0414e2` | `call` to the body directly after it (`0x7e0414ea`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e041589` | 1 | `entry_thunk_7e041589` | `call` to the body directly after it (`0x7e041591`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e041622` | 2 | `entry_thunk_7e041622` | `call` to the body directly after it (`0x7e04162a`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e04174e` | 1 | `entry_thunk_7e04174e` | `call` to the body directly after it (`0x7e041756`, register-save mask `0x20`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e041a14` | 1 | `entry_thunk_7e041a14` | `call` to the body directly after it (`0x7e041a1c`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e041abc` | 2 | `entry_thunk_7e041abc` | `call` to the body directly after it (`0x7e041ac4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e041ca2` | 1 | `entry_thunk_7e041ca2` | `call` to the body directly after it (`0x7e041caa`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e041d0b` | 1 | `entry_thunk_7e041d0b` | `call` to the body directly after it (`0x7e041d13`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e041e75` | 1 | `entry_thunk_7e041e75` | `call` to the body directly after it (`0x7e041e7d`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e041ed1` | 1 | `entry_thunk_7e041ed1` | `call` to the body directly after it (`0x7e041ed9`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e041f33` | 1 | `entry_thunk_7e041f33` | `call` to the body directly after it (`0x7e041f3b`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e041fc6` | 1 | `entry_thunk_7e041fc6` | `call` to the body directly after it (`0x7e041fce`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e042056` | 1 | `entry_thunk_7e042056` | `call` to the body directly after it (`0x7e04205e`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0420e9` | 1 | `entry_thunk_7e0420e9` | `call` to the body directly after it (`0x7e0420f1`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e042179` | 1 | `entry_thunk_7e042179` | `call` to the body directly after it (`0x7e042181`, register-save mask `0xf0`, frame 56) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0422e1` | 1 | `entry_thunk_7e0422e1` | `call` to the body directly after it (`0x7e0422e9`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e04236a` | 1 | `entry_thunk_7e04236a` | `call` to the body directly after it (`0x7e042372`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0423f3` | 2 | `entry_thunk_7e0423f3` | `call` to the body directly after it (`0x7e0423fb`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0424f8` | 1 | `entry_thunk_7e0424f8` | `call` to the body directly after it (`0x7e042500`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0425bd` | 4 | `entry_thunk_7e0425bd` | `call` to the body directly after it (`0x7e0425c5`, register-save mask `0xb0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0426bb` | 1 | `entry_thunk_7e0426bb` | `call` to the body directly after it (`0x7e0426c3`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0427bd` | 1 | `entry_thunk_7e0427bd` | `call` to the body directly after it (`0x7e0427c5`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e042944` | 1 | `entry_thunk_7e042944` | `call` to the body directly after it (`0x7e04294c`, register-save mask `0xb0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e042a3e` | 1 | `entry_thunk_7e042a3e` | `call` to the body directly after it (`0x7e042a46`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e042a8c` | 2 | `entry_thunk_7e042a8c` | `call` to the body directly after it (`0x7e042a94`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e042b7b` | 1 | `entry_thunk_7e042b7b` | `call` to the body directly after it (`0x7e042b83`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e042da6` | 1 | `entry_thunk_7e042da6` | `call` to the body directly after it (`0x7e042dae`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e042dfa` | 2 | `entry_thunk_7e042dfa` | `call` to the body directly after it (`0x7e042e02`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e042f96` | 1 | `entry_thunk_7e042f96` | `call` to the body directly after it (`0x7e042f9e`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e04302c` | 2 | `entry_thunk_7e04302c` | `call` to the body directly after it (`0x7e043034`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e043130` | 1 | `entry_thunk_7e043130` | `call` to the body directly after it (`0x7e043138`, register-save mask `0xb0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e04322a` | 1 | `entry_thunk_7e04322a` | `call` to the body directly after it (`0x7e043232`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e04338a` | 1 | `entry_thunk_7e04338a` | `call` to the body directly after it (`0x7e043392`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e04341a` | 1 | `entry_thunk_7e04341a` | `call` to the body directly after it (`0x7e043422`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0434ad` | 1 | `entry_thunk_7e0434ad` | `call` to the body directly after it (`0x7e0434b5`, register-save mask `0xb0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0435a7` | 1 | `entry_thunk_7e0435a7` | `call` to the body directly after it (`0x7e0435af`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e043616` | 3 | `entry_thunk_7e043616` | `call` to the body directly after it (`0x7e04361e`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0437d4` | 1 | `entry_thunk_7e0437d4` | `call` to the body directly after it (`0x7e0437dc`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e043828` | 2 | `entry_thunk_7e043828` | `call` to the body directly after it (`0x7e043830`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e043a59` | 3 | `entry_thunk_7e043a59` | `call` to the body directly after it (`0x7e043a61`, register-save mask `0xb0`, frame 52) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e043b97` | 1 | `entry_thunk_7e043b97` | `call` to the body directly after it (`0x7e043b9f`, register-save mask `0x30`, frame 36) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e043c68` | 1 | `entry_thunk_7e043c68` | `call` to the body directly after it (`0x7e043c70`, register-save mask `0xf0`, frame 68) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e043d9e` | 1 | `entry_thunk_7e043d9e` | `call` to the body directly after it (`0x7e043da6`, register-save mask `0xb0`, frame 48) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e043fc3` | 1 | `entry_thunk_7e043fc3` | `call` to the body directly after it (`0x7e043fcb`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e044020` | 2 | `entry_thunk_7e044020` | `call` to the body directly after it (`0x7e044028`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0440ba` | 1 | `entry_thunk_7e0440ba` | `call` to the body directly after it (`0x7e0440c2`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0448df` | 1 | `entry_thunk_7e0448df` | `call` to the body directly after it (`0x7e0448e7`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e04491a` | 1 | `entry_thunk_7e04491a` | `call` to the body directly after it (`0x7e044922`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e04496c` | 2 | `entry_thunk_7e04496c` | `call` to the body directly after it (`0x7e044974`, register-save mask `0x00`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e052148` | 1 | `entry_thunk_7e052148` | `call` to the body directly after it (`0x7e052150`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e052176` | 2 | `entry_thunk_7e052176` | `call` to the body directly after it (`0x7e05217e`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e057689` | 2 | `entry_thunk_7e057689` | `call` to the body directly after it (`0x7e057691`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0576fc` | 2 | `entry_thunk_7e0576fc` | `call` to the body directly after it (`0x7e057704`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0577a2` | 1 | `entry_thunk_7e0577a2` | `call` to the body directly after it (`0x7e0577aa`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0585b9` | 2 | `entry_thunk_7e0585b9` | `call` to the body directly after it (`0x7e0585c1`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e058691` | 2 | `entry_thunk_7e058691` | `call` to the body directly after it (`0x7e058699`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e058737` | 1 | `entry_thunk_7e058737` | `call` to the body directly after it (`0x7e05873f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e058bbb` | 2 | `entry_thunk_7e058bbb` | `call` to the body directly after it (`0x7e058bc3`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e058c93` | 2 | `entry_thunk_7e058c93` | `call` to the body directly after it (`0x7e058c9b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e058d39` | 1 | `entry_thunk_7e058d39` | `call` to the body directly after it (`0x7e058d41`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0594d8` | 1 | `obj_clear_f304_7e0594d8` | `*(this+304) = 0`. | pattern scan |
| `0x7e0594e0` | 1 | `obj_set1_f304_7e0594e0` | `*(this+304) = 1`. | pattern scan |
| `0x7e0599a2` | 2 | `entry_thunk_7e0599a2` | `call` to the body directly after it (`0x7e0599aa`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e059a0e` | 2 | `entry_thunk_7e059a0e` | `call` to the body directly after it (`0x7e059a16`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e059a9f` | 1 | `entry_thunk_7e059a9f` | `call` to the body directly after it (`0x7e059aa7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e05c990` | 1 | `entry_thunk_7e05c990` | `call` to the body directly after it (`0x7e05c998`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e05c9df` | 1 | `entry_thunk_7e05c9df` | `call` to the body directly after it (`0x7e05c9e7`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e05cab0` | 3 | `entry_thunk_7e05cab0` | `call` to the body directly after it (`0x7e05cab8`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e05cbf1` | 1 | `entry_thunk_7e05cbf1` | `call` to the body directly after it (`0x7e05cbf9`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e05cc73` | 1 | `entry_thunk_7e05cc73` | `call` to the body directly after it (`0x7e05cc7b`, register-save mask `0xf0`, frame 20) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e05d067` | 1 | `obj_clear_f412_7e05d067` | `*(this+412) = 0`. | pattern scan |
| `0x7e05d08d` | 1 | `entry_thunk_7e05d08d` | `call` to the body directly after it (`0x7e05d095`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e05d0e1` | 2 | `entry_thunk_7e05d0e1` | `call` to the body directly after it (`0x7e05d0e9`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e05d13d` | 1 | `obj_clear_f420_7e05d13d` | `*(this+420) = 0`. | pattern scan |
| `0x7e05d163` | 1 | `entry_thunk_7e05d163` | `call` to the body directly after it (`0x7e05d16b`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e05d1cc` | 2 | `entry_thunk_7e05d1cc` | `call` to the body directly after it (`0x7e05d1d4`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e07bb7d` | 2 | `entry_thunk_7e07bb7d` | `call` to the body directly after it (`0x7e07bb85`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e07bc55` | 2 | `entry_thunk_7e07bc55` | `call` to the body directly after it (`0x7e07bc5d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e07bcfb` | 1 | `entry_thunk_7e07bcfb` | `call` to the body directly after it (`0x7e07bd03`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e07dd7e` | 2 | `entry_thunk_7e07dd7e` | `call` to the body directly after it (`0x7e07dd86`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e07ddea` | 2 | `entry_thunk_7e07ddea` | `call` to the body directly after it (`0x7e07ddf2`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e07e007` | 3 | `entry_thunk_7e07e007` | `call` to the body directly after it (`0x7e07e00f`, register-save mask `0x00`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e07e0df` | 2 | `entry_thunk_7e07e0df` | `call` to the body directly after it (`0x7e07e0e7`, register-save mask `0xb0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e07e276` | 2 | `entry_thunk_7e07e276` | `call` to the body directly after it (`0x7e07e27e`, register-save mask `0xb0`, frame 48) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e07e9cb` | 1 | `entry_thunk_7e07e9cb` | `call` to the body directly after it (`0x7e07e9d3`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e07ea21` | 1 | `entry_thunk_7e07ea21` | `call` to the body directly after it (`0x7e07ea29`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e07eaf9` | 3 | `entry_thunk_7e07eaf9` | `call` to the body directly after it (`0x7e07eb01`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e07eb9f` | 1 | `entry_thunk_7e07eb9f` | `call` to the body directly after it (`0x7e07eba7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e07f182` | 1 | `entry_thunk_7e07f182` | `call` to the body directly after it (`0x7e07f18a`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e07f1d8` | 1 | `entry_thunk_7e07f1d8` | `call` to the body directly after it (`0x7e07f1e0`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e07f2b0` | 3 | `entry_thunk_7e07f2b0` | `call` to the body directly after it (`0x7e07f2b8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e07f356` | 1 | `entry_thunk_7e07f356` | `call` to the body directly after it (`0x7e07f35e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0800c8` | 1 | `obj_clear_f328_7e0800c8` | `*(this+328) = 0`. | pattern scan |
| `0x7e080108` | 1 | `entry_thunk_7e080108` | `call` to the body directly after it (`0x7e080110`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0816db` | 1 | `entry_thunk_7e0816db` | `call` to the body directly after it (`0x7e0816e3`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e081731` | 1 | `entry_thunk_7e081731` | `call` to the body directly after it (`0x7e081739`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e081816` | 3 | `entry_thunk_7e081816` | `call` to the body directly after it (`0x7e08181e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0819f1` | 1 | `obj_clear_f500_7e0819f1` | `*(this+500) = 0`. | pattern scan |
| `0x7e081a17` | 1 | `entry_thunk_7e081a17` | `call` to the body directly after it (`0x7e081a1f`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e081ab3` | 1 | `entry_thunk_7e081ab3` | `call` to the body directly after it (`0x7e081abb`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e081c9c` | 1 | `entry_thunk_7e081c9c` | `call` to the body directly after it (`0x7e081ca4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e081d1e` | 2 | `entry_thunk_7e081d1e` | `call` to the body directly after it (`0x7e081d26`, register-save mask `0xf0`, frame 64) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e081f91` | 2 | `entry_thunk_7e081f91` | `call` to the body directly after it (`0x7e081f99`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e08202d` | 2 | `entry_thunk_7e08202d` | `call` to the body directly after it (`0x7e082035`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e083de1` | 2 | `entry_thunk_7e083de1` | `call` to the body directly after it (`0x7e083de9`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e083eb9` | 2 | `entry_thunk_7e083eb9` | `call` to the body directly after it (`0x7e083ec1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e083f5f` | 1 | `entry_thunk_7e083f5f` | `call` to the body directly after it (`0x7e083f67`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e08b38c` | 2 | `entry_thunk_7e08b38c` | `call` to the body directly after it (`0x7e08b394`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e08b464` | 2 | `entry_thunk_7e08b464` | `call` to the body directly after it (`0x7e08b46c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e08b50a` | 1 | `entry_thunk_7e08b50a` | `call` to the body directly after it (`0x7e08b512`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e08e86e` | 1 | `entry_thunk_7e08e86e` | `call` to the body directly after it (`0x7e08e876`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e08e883` | 1 | `entry_thunk_7e08e883` | `call` to the body directly after it (`0x7e08e88b`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e08e8e7` | 1 | `entry_thunk_7e08e8e7` | `call` to the body directly after it (`0x7e08e8ef`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e08e9d3` | 1 | `entry_thunk_7e08e9d3` | `call` to the body directly after it (`0x7e08e9db`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e091b16` | 1 | `entry_thunk_7e091b16` | `call` to the body directly after it (`0x7e091b1e`, register-save mask `0xa0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e091c13` | 1 | `entry_thunk_7e091c13` | `call` to the body directly after it (`0x7e091c1b`, register-save mask `0xa0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e097a1c` | 2 | `entry_thunk_7e097a1c` | `call` to the body directly after it (`0x7e097a24`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e097a88` | 2 | `entry_thunk_7e097a88` | `call` to the body directly after it (`0x7e097a90`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e097b19` | 2 | `entry_thunk_7e097b19` | `call` to the body directly after it (`0x7e097b21`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e098d22` | 2 | `entry_thunk_7e098d22` | `call` to the body directly after it (`0x7e098d2a`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e098dfa` | 2 | `entry_thunk_7e098dfa` | `call` to the body directly after it (`0x7e098e02`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e098ea0` | 1 | `entry_thunk_7e098ea0` | `call` to the body directly after it (`0x7e098ea8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e09ada8` | 1 | `entry_thunk_7e09ada8` | `call` to the body directly after it (`0x7e09adb0`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e09adfe` | 1 | `entry_thunk_7e09adfe` | `call` to the body directly after it (`0x7e09ae06`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e09aed6` | 3 | `entry_thunk_7e09aed6` | `call` to the body directly after it (`0x7e09aede`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e09af7c` | 1 | `entry_thunk_7e09af7c` | `call` to the body directly after it (`0x7e09af84`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e09bc5f` | 1 | `entry_thunk_7e09bc5f` | `call` to the body directly after it (`0x7e09bc67`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e09bcb5` | 1 | `entry_thunk_7e09bcb5` | `call` to the body directly after it (`0x7e09bcbd`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e09bd8d` | 3 | `entry_thunk_7e09bd8d` | `call` to the body directly after it (`0x7e09bd95`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e09be33` | 1 | `entry_thunk_7e09be33` | `call` to the body directly after it (`0x7e09be3b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e09f7af` | 1 | `entry_thunk_7e09f7af` | `call` to the body directly after it (`0x7e09f7b7`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e09f805` | 1 | `entry_thunk_7e09f805` | `call` to the body directly after it (`0x7e09f80d`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e09f8dd` | 3 | `entry_thunk_7e09f8dd` | `call` to the body directly after it (`0x7e09f8e5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e09f983` | 1 | `entry_thunk_7e09f983` | `call` to the body directly after it (`0x7e09f98b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a02dd` | 1 | `entry_thunk_7e0a02dd` | `call` to the body directly after it (`0x7e0a02e5`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a0333` | 1 | `entry_thunk_7e0a0333` | `call` to the body directly after it (`0x7e0a033b`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a040b` | 3 | `entry_thunk_7e0a040b` | `call` to the body directly after it (`0x7e0a0413`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a04b1` | 1 | `entry_thunk_7e0a04b1` | `call` to the body directly after it (`0x7e0a04b9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a27ff` | 1 | `entry_thunk_7e0a27ff` | `call` to the body directly after it (`0x7e0a2807`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a2855` | 1 | `entry_thunk_7e0a2855` | `call` to the body directly after it (`0x7e0a285d`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a292d` | 3 | `entry_thunk_7e0a292d` | `call` to the body directly after it (`0x7e0a2935`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a29d3` | 1 | `entry_thunk_7e0a29d3` | `call` to the body directly after it (`0x7e0a29db`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a3514` | 2 | `entry_thunk_7e0a3514` | `call` to the body directly after it (`0x7e0a351c`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a35ec` | 2 | `entry_thunk_7e0a35ec` | `call` to the body directly after it (`0x7e0a35f4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a3692` | 1 | `entry_thunk_7e0a3692` | `call` to the body directly after it (`0x7e0a369a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a390d` | 2 | `entry_thunk_7e0a390d` | `call` to the body directly after it (`0x7e0a3915`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a39e5` | 2 | `entry_thunk_7e0a39e5` | `call` to the body directly after it (`0x7e0a39ed`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a3a8b` | 1 | `entry_thunk_7e0a3a8b` | `call` to the body directly after it (`0x7e0a3a93`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a4561` | 1 | `entry_thunk_7e0a4561` | `call` to the body directly after it (`0x7e0a4569`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a45c5` | 2 | `entry_thunk_7e0a45c5` | `call` to the body directly after it (`0x7e0a45cd`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a4656` | 1 | `entry_thunk_7e0a4656` | `call` to the body directly after it (`0x7e0a465e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a49b5` | 2 | `entry_thunk_7e0a49b5` | `call` to the body directly after it (`0x7e0a49bd`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a4a21` | 2 | `entry_thunk_7e0a4a21` | `call` to the body directly after it (`0x7e0a4a29`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a4ab2` | 1 | `entry_thunk_7e0a4ab2` | `call` to the body directly after it (`0x7e0a4aba`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a63a5` | 2 | `entry_thunk_7e0a63a5` | `call` to the body directly after it (`0x7e0a63ad`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a6411` | 2 | `entry_thunk_7e0a6411` | `call` to the body directly after it (`0x7e0a6419`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a6624` | 1 | `entry_thunk_7e0a6624` | `call` to the body directly after it (`0x7e0a662c`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a6702` | 1 | `entry_thunk_7e0a6702` | `call` to the body directly after it (`0x7e0a670a`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a67c4` | 1 | `entry_thunk_7e0a67c4` | `call` to the body directly after it (`0x7e0a67cc`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a6832` | 1 | `entry_thunk_7e0a6832` | `call` to the body directly after it (`0x7e0a683a`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a6912` | 2 | `entry_thunk_7e0a6912` | `call` to the body directly after it (`0x7e0a691a`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a69a1` | 2 | `entry_thunk_7e0a69a1` | `call` to the body directly after it (`0x7e0a69a9`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a6be9` | 2 | `entry_thunk_7e0a6be9` | `call` to the body directly after it (`0x7e0a6bf1`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a6c57` | 1 | `entry_thunk_7e0a6c57` | `call` to the body directly after it (`0x7e0a6c5f`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a6cfe` | 2 | `entry_thunk_7e0a6cfe` | `call` to the body directly after it (`0x7e0a6d06`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a6d41` | 1 | `entry_thunk_7e0a6d41` | `call` to the body directly after it (`0x7e0a6d49`, register-save mask `0xf0`, frame 56) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a6e78` | 1 | `entry_thunk_7e0a6e78` | `call` to the body directly after it (`0x7e0a6e80`, register-save mask `0xa0`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a6fd1` | 2 | `entry_thunk_7e0a6fd1` | `call` to the body directly after it (`0x7e0a6fd9`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a77cc` | 1 | `entry_thunk_7e0a77cc` | `call` to the body directly after it (`0x7e0a77d4`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a7822` | 1 | `entry_thunk_7e0a7822` | `call` to the body directly after it (`0x7e0a782a`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a7900` | 3 | `entry_thunk_7e0a7900` | `call` to the body directly after it (`0x7e0a7908`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a7ac0` | 1 | `obj_clear_f280_7e0a7ac0` | `*(this+280) = 0`. | pattern scan |
| `0x7e0a7af1` | 1 | `entry_thunk_7e0a7af1` | `call` to the body directly after it (`0x7e0a7af9`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a7b5d` | 3 | `entry_thunk_7e0a7b5d` | `call` to the body directly after it (`0x7e0a7b65`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a7bab` | 1 | `entry_thunk_7e0a7bab` | `call` to the body directly after it (`0x7e0a7bb3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a7c01` | 1 | `obj_clear_f288_7e0a7c01` | `*(this+288) = 0`. | pattern scan |
| `0x7e0a7c32` | 1 | `entry_thunk_7e0a7c32` | `call` to the body directly after it (`0x7e0a7c3a`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a7c8b` | 1 | `entry_thunk_7e0a7c8b` | `call` to the body directly after it (`0x7e0a7c93`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a7cce` | 2 | `entry_thunk_7e0a7cce` | `call` to the body directly after it (`0x7e0a7cd6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a8090` | 1 | `entry_thunk_7e0a8090` | `call` to the body directly after it (`0x7e0a8098`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a80e6` | 1 | `entry_thunk_7e0a80e6` | `call` to the body directly after it (`0x7e0a80ee`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a81be` | 3 | `entry_thunk_7e0a81be` | `call` to the body directly after it (`0x7e0a81c6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a8264` | 1 | `entry_thunk_7e0a8264` | `call` to the body directly after it (`0x7e0a826c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a87c6` | 1 | `obj_clear_f328_7e0a87c6` | `*(this+328) = 0`. | pattern scan |
| `0x7e0a8820` | 1 | `entry_thunk_7e0a8820` | `call` to the body directly after it (`0x7e0a8828`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a8887` | 1 | `entry_thunk_7e0a8887` | `call` to the body directly after it (`0x7e0a888f`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a8958` | 3 | `entry_thunk_7e0a8958` | `call` to the body directly after it (`0x7e0a8960`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a8ac3` | 3 | `entry_thunk_7e0a8ac3` | `call` to the body directly after it (`0x7e0a8acb`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a8c5e` | 1 | `entry_thunk_7e0a8c5e` | `call` to the body directly after it (`0x7e0a8c66`, register-save mask `0x30`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a8cdb` | 2 | `entry_thunk_7e0a8cdb` | `call` to the body directly after it (`0x7e0a8ce3`, register-save mask `0x30`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a9ea9` | 1 | `entry_thunk_7e0a9ea9` | `call` to the body directly after it (`0x7e0a9eb1`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a9eff` | 1 | `entry_thunk_7e0a9eff` | `call` to the body directly after it (`0x7e0a9f07`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0a9fdc` | 2 | `entry_thunk_7e0a9fdc` | `call` to the body directly after it (`0x7e0a9fe4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0aa0bb` | 1 | `entry_thunk_7e0aa0bb` | `call` to the body directly after it (`0x7e0aa0c3`, register-save mask `0x20`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ab63e` | 1 | `entry_thunk_7e0ab63e` | `call` to the body directly after it (`0x7e0ab646`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ab694` | 1 | `entry_thunk_7e0ab694` | `call` to the body directly after it (`0x7e0ab69c`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ab765` | 3 | `entry_thunk_7e0ab765` | `call` to the body directly after it (`0x7e0ab76d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ab80b` | 1 | `entry_thunk_7e0ab80b` | `call` to the body directly after it (`0x7e0ab813`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ac93b` | 1 | `entry_thunk_7e0ac93b` | `call` to the body directly after it (`0x7e0ac943`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ac98f` | 1 | `entry_thunk_7e0ac98f` | `call` to the body directly after it (`0x7e0ac997`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0aca74` | 3 | `entry_thunk_7e0aca74` | `call` to the body directly after it (`0x7e0aca7c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0acc1f` | 1 | `entry_thunk_7e0acc1f` | `call` to the body directly after it (`0x7e0acc27`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0accb4` | 5 | `entry_thunk_7e0accb4` | `call` to the body directly after it (`0x7e0accbc`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ace00` | 2 | `entry_thunk_7e0ace00` | `call` to the body directly after it (`0x7e0ace08`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ad3a4` | 1 | `obj_clear_f288_7e0ad3a4` | `*(this+288) = 0`. | pattern scan |
| `0x7e0ad3fe` | 1 | `entry_thunk_7e0ad3fe` | `call` to the body directly after it (`0x7e0ad406`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ad461` | 2 | `obj_clear_f292_7e0ad461` | `*(this+292) = 0`. | pattern scan |
| `0x7e0ad511` | 1 | `entry_thunk_7e0ad511` | `call` to the body directly after it (`0x7e0ad519`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ad5a1` | 3 | `entry_thunk_7e0ad5a1` | `call` to the body directly after it (`0x7e0ad5a9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ad65a` | 1 | `obj_clear_f296_7e0ad65a` | `*(this+296) = 0`. | pattern scan |
| `0x7e0ad706` | 1 | `entry_thunk_7e0ad706` | `call` to the body directly after it (`0x7e0ad70e`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ad754` | 2 | `entry_thunk_7e0ad754` | `call` to the body directly after it (`0x7e0ad75c`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ae3f6` | 1 | `obj_clear_f560_7e0ae3f6` | `*(this+560) = 0`. | pattern scan |
| `0x7e0ae451` | 1 | `entry_thunk_7e0ae451` | `call` to the body directly after it (`0x7e0ae459`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ae534` | 1 | `entry_thunk_7e0ae534` | `call` to the body directly after it (`0x7e0ae53c`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ae5a0` | 1 | `entry_thunk_7e0ae5a0` | `call` to the body directly after it (`0x7e0ae5a8`, register-save mask `0xb0`, frame 36) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ae6a7` | 3 | `entry_thunk_7e0ae6a7` | `call` to the body directly after it (`0x7e0ae6af`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ae760` | 1 | `obj_clear_f564_7e0ae760` | `*(this+564) = 0`. | pattern scan |
| `0x7e0ae80c` | 1 | `entry_thunk_7e0ae80c` | `call` to the body directly after it (`0x7e0ae814`, register-save mask `0x00`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ae9ac` | 1 | `entry_thunk_7e0ae9ac` | `call` to the body directly after it (`0x7e0ae9b4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0aea05` | 2 | `entry_thunk_7e0aea05` | `call` to the body directly after it (`0x7e0aea0d`, register-save mask `0x00`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0af9e6` | 1 | `obj_clear_f320_7e0af9e6` | `*(this+320) = 0`. | pattern scan |
| `0x7e0b1e3e` | 2 | `entry_thunk_7e0b1e3e` | `call` to the body directly after it (`0x7e0b1e46`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b1eaa` | 2 | `entry_thunk_7e0b1eaa` | `call` to the body directly after it (`0x7e0b1eb2`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b1f49` | 1 | `entry_thunk_7e0b1f49` | `call` to the body directly after it (`0x7e0b1f51`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b222b` | 1 | `entry_thunk_7e0b222b` | `call` to the body directly after it (`0x7e0b2233`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b2281` | 1 | `entry_thunk_7e0b2281` | `call` to the body directly after it (`0x7e0b2289`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b2359` | 3 | `entry_thunk_7e0b2359` | `call` to the body directly after it (`0x7e0b2361`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b23ff` | 1 | `entry_thunk_7e0b23ff` | `call` to the body directly after it (`0x7e0b2407`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b3fb8` | 4 | `entry_thunk_7e0b3fb8` | `call` to the body directly after it (`0x7e0b3fc0`, register-save mask `0x00`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b4120` | 1 | `entry_thunk_7e0b4120` | `call` to the body directly after it (`0x7e0b4128`, register-save mask `0x20`, frame 20) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b41ae` | 1 | `entry_thunk_7e0b41ae` | `call` to the body directly after it (`0x7e0b41b6`, register-save mask `0x30`, frame 24) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b4259` | 1 | `entry_thunk_7e0b4259` | `call` to the body directly after it (`0x7e0b4261`, register-save mask `0x20`, frame 20) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b42ff` | 1 | `entry_thunk_7e0b42ff` | `call` to the body directly after it (`0x7e0b4307`, register-save mask `0x20`, frame 20) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b43cb` | 1 | `entry_thunk_7e0b43cb` | `call` to the body directly after it (`0x7e0b43d3`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b44dc` | 1 | `entry_thunk_7e0b44dc` | `call` to the body directly after it (`0x7e0b44e4`, register-save mask `0x30`, frame 24) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b45ef` | 1 | `entry_thunk_7e0b45ef` | `call` to the body directly after it (`0x7e0b45f7`, register-save mask `0x30`, frame 24) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b468a` | 1 | `entry_thunk_7e0b468a` | `call` to the body directly after it (`0x7e0b4692`, register-save mask `0xa0`, frame 24) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b476d` | 1 | `entry_thunk_7e0b476d` | `call` to the body directly after it (`0x7e0b4775`, register-save mask `0x20`, frame 20) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b47f5` | 1 | `entry_thunk_7e0b47f5` | `call` to the body directly after it (`0x7e0b47fd`, register-save mask `0x20`, frame 20) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b4879` | 2 | `entry_thunk_7e0b4879` | `call` to the body directly after it (`0x7e0b4881`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b490b` | 1 | `entry_thunk_7e0b490b` | `call` to the body directly after it (`0x7e0b4913`, register-save mask `0x20`, frame 20) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b4aef` | 1 | `entry_thunk_7e0b4aef` | `call` to the body directly after it (`0x7e0b4af7`, register-save mask `0xf0`, frame 48) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b4c42` | 1 | `entry_thunk_7e0b4c42` | `call` to the body directly after it (`0x7e0b4c4a`, register-save mask `0x20`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b4d01` | 1 | `entry_thunk_7e0b4d01` | `call` to the body directly after it (`0x7e0b4d09`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b56e3` | 2 | `entry_thunk_7e0b56e3` | `call` to the body directly after it (`0x7e0b56eb`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b5e44` | 1 | `entry_thunk_7e0b5e44` | `call` to the body directly after it (`0x7e0b5e4c`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b5e9a` | 1 | `entry_thunk_7e0b5e9a` | `call` to the body directly after it (`0x7e0b5ea2`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b5f72` | 3 | `entry_thunk_7e0b5f72` | `call` to the body directly after it (`0x7e0b5f7a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b6018` | 1 | `entry_thunk_7e0b6018` | `call` to the body directly after it (`0x7e0b6020`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b6568` | 1 | `entry_thunk_7e0b6568` | `call` to the body directly after it (`0x7e0b6570`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b65be` | 1 | `entry_thunk_7e0b65be` | `call` to the body directly after it (`0x7e0b65c6`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b668f` | 3 | `entry_thunk_7e0b668f` | `call` to the body directly after it (`0x7e0b6697`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b67f6` | 1 | `entry_thunk_7e0b67f6` | `call` to the body directly after it (`0x7e0b67fe`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b686f` | 2 | `entry_thunk_7e0b686f` | `call` to the body directly after it (`0x7e0b6877`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b7241` | 1 | `entry_thunk_7e0b7241` | `call` to the body directly after it (`0x7e0b7249`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b7290` | 1 | `entry_thunk_7e0b7290` | `call` to the body directly after it (`0x7e0b7298`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b7361` | 3 | `entry_thunk_7e0b7361` | `call` to the body directly after it (`0x7e0b7369`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b741a` | 1 | `obj_clear_f340_7e0b741a` | `*(this+340) = 0`. | pattern scan |
| `0x7e0b74f9` | 2 | `entry_thunk_7e0b74f9` | `call` to the body directly after it (`0x7e0b7501`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b8cbd` | 1 | `entry_thunk_7e0b8cbd` | `call` to the body directly after it (`0x7e0b8cc5`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b8d1f` | 1 | `entry_thunk_7e0b8d1f` | `call` to the body directly after it (`0x7e0b8d27`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b8e11` | 3 | `entry_thunk_7e0b8e11` | `call` to the body directly after it (`0x7e0b8e19`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b9017` | 1 | `obj_clear_f840_7e0b9017` | `*(this+840) = 0`. | pattern scan |
| `0x7e0b9030` | 2 | `entry_thunk_7e0b9030` | `call` to the body directly after it (`0x7e0b9038`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b91fc` | 3 | `obj_clear_f856_7e0b91fc` | `*(this+856) = 0`. | pattern scan |
| `0x7e0b927f` | 4 | `entry_thunk_7e0b927f` | `call` to the body directly after it (`0x7e0b9287`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b94a0` | 2 | `entry_thunk_7e0b94a0` | `call` to the body directly after it (`0x7e0b94a8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b9623` | 1 | `entry_thunk_7e0b9623` | `call` to the body directly after it (`0x7e0b962b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b9700` | 1 | `entry_thunk_7e0b9700` | `call` to the body directly after it (`0x7e0b9708`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b98a4` | 2 | `obj_clear_f860_7e0b98a4` | `*(this+860) = 0`. | pattern scan |
| `0x7e0b992f` | 1 | `entry_thunk_7e0b992f` | `call` to the body directly after it (`0x7e0b9937`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b9a2d` | 2 | `entry_thunk_7e0b9a2d` | `call` to the body directly after it (`0x7e0b9a35`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b9afd` | 1 | `entry_thunk_7e0b9afd` | `call` to the body directly after it (`0x7e0b9b05`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b9b58` | 5 | `entry_thunk_7e0b9b58` | `call` to the body directly after it (`0x7e0b9b60`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b9cbd` | 2 | `obj_clear_f864_7e0b9cbd` | `*(this+864) = 0`. | pattern scan |
| `0x7e0b9da0` | 1 | `entry_thunk_7e0b9da0` | `call` to the body directly after it (`0x7e0b9da8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b9e5b` | 2 | `entry_thunk_7e0b9e5b` | `call` to the body directly after it (`0x7e0b9e63`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0b9eee` | 1 | `entry_thunk_7e0b9eee` | `call` to the body directly after it (`0x7e0b9ef6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0babc3` | 1 | `obj_set1_f328_7e0babc3` | `*(this+328) = 1`. | pattern scan |
| `0x7e0bb111` | 1 | `entry_thunk_7e0bb111` | `call` to the body directly after it (`0x7e0bb119`, register-save mask `0xf0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bb18d` | 1 | `entry_thunk_7e0bb18d` | `call` to the body directly after it (`0x7e0bb195`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bb26b` | 3 | `entry_thunk_7e0bb26b` | `call` to the body directly after it (`0x7e0bb273`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bb40c` | 1 | `entry_thunk_7e0bb40c` | `call` to the body directly after it (`0x7e0bb414`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bb632` | 1 | `entry_thunk_7e0bb632` | `call` to the body directly after it (`0x7e0bb63a`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bb6eb` | 3 | `obj_clear_f604_7e0bb6eb` | `*(this+604) = 0`. | pattern scan |
| `0x7e0bb77f` | 2 | `entry_thunk_7e0bb77f` | `call` to the body directly after it (`0x7e0bb787`, register-save mask `0xf0`, frame 228) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bbd2f` | 1 | `entry_thunk_7e0bbd2f` | `call` to the body directly after it (`0x7e0bbd37`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bbdbf` | 1 | `entry_thunk_7e0bbdbf` | `call` to the body directly after it (`0x7e0bbdc7`, register-save mask `0xf0`, frame 60) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bbfac` | 3 | `obj_clear_f608_7e0bbfac` | `*(this+608) = 0`. | pattern scan |
| `0x7e0bc02b` | 1 | `entry_thunk_7e0bc02b` | `call` to the body directly after it (`0x7e0bc033`, register-save mask `0xf0`, frame 248) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bc4e2` | 1 | `entry_thunk_7e0bc4e2` | `call` to the body directly after it (`0x7e0bc4ea`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bc55e` | 6 | `entry_thunk_7e0bc55e` | `call` to the body directly after it (`0x7e0bc566`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bc7b9` | 3 | `entry_thunk_7e0bc7b9` | `call` to the body directly after it (`0x7e0bc7c1`, register-save mask `0xf0`, frame 64) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0be07b` | 1 | `entry_thunk_7e0be07b` | `call` to the body directly after it (`0x7e0be083`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0be0d1` | 1 | `entry_thunk_7e0be0d1` | `call` to the body directly after it (`0x7e0be0d9`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0be1b6` | 3 | `entry_thunk_7e0be1b6` | `call` to the body directly after it (`0x7e0be1be`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0be6e7` | 1 | `entry_thunk_7e0be6e7` | `call` to the body directly after it (`0x7e0be6ef`, register-save mask `0x00`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0be776` | 2 | `entry_thunk_7e0be776` | `call` to the body directly after it (`0x7e0be77e`, register-save mask `0x00`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0be8ca` | 2 | `entry_thunk_7e0be8ca` | `call` to the body directly after it (`0x7e0be8d2`, register-save mask `0x00`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0be928` | 1 | `entry_thunk_7e0be928` | `call` to the body directly after it (`0x7e0be930`, register-save mask `0xb0`, frame 36) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bf214` | 1 | `entry_thunk_7e0bf214` | `call` to the body directly after it (`0x7e0bf21c`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bf268` | 1 | `entry_thunk_7e0bf268` | `call` to the body directly after it (`0x7e0bf270`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bf34d` | 3 | `entry_thunk_7e0bf34d` | `call` to the body directly after it (`0x7e0bf355`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bf50d` | 1 | `obj_clear_f320_7e0bf50d` | `*(this+320) = 0`. | pattern scan |
| `0x7e0bf533` | 1 | `entry_thunk_7e0bf533` | `call` to the body directly after it (`0x7e0bf53b`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bf5b5` | 3 | `entry_thunk_7e0bf5b5` | `call` to the body directly after it (`0x7e0bf5bd`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bf694` | 3 | `entry_thunk_7e0bf694` | `call` to the body directly after it (`0x7e0bf69c`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0bf96d` | 5 | `entry_thunk_7e0bf96d` | `call` to the body directly after it (`0x7e0bf975`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c044f` | 1 | `entry_thunk_7e0c044f` | `call` to the body directly after it (`0x7e0c0457`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c04a5` | 1 | `entry_thunk_7e0c04a5` | `call` to the body directly after it (`0x7e0c04ad`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c058a` | 3 | `entry_thunk_7e0c058a` | `call` to the body directly after it (`0x7e0c0592`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c06ed` | 1 | `entry_thunk_7e0c06ed` | `call` to the body directly after it (`0x7e0c06f5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c0742` | 1 | `entry_thunk_7e0c0742` | `call` to the body directly after it (`0x7e0c074a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c0797` | 5 | `entry_thunk_7e0c0797` | `call` to the body directly after it (`0x7e0c079f`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c0850` | 1 | `entry_thunk_7e0c0850` | `call` to the body directly after it (`0x7e0c0858`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c41c2` | 1 | `entry_thunk_7e0c41c2` | `call` to the body directly after it (`0x7e0c41ca`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c4218` | 1 | `entry_thunk_7e0c4218` | `call` to the body directly after it (`0x7e0c4220`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c42fd` | 3 | `entry_thunk_7e0c42fd` | `call` to the body directly after it (`0x7e0c4305`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c45e2` | 2 | `entry_thunk_7e0c45e2` | `call` to the body directly after it (`0x7e0c45ea`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c463f` | 1 | `entry_thunk_7e0c463f` | `call` to the body directly after it (`0x7e0c4647`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c46a5` | 4 | `entry_thunk_7e0c46a5` | `call` to the body directly after it (`0x7e0c46ad`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c4938` | 1 | `entry_thunk_7e0c4938` | `call` to the body directly after it (`0x7e0c4940`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c497b` | 1 | `entry_thunk_7e0c497b` | `call` to the body directly after it (`0x7e0c4983`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c49db` | 1 | `obj_clear_f4244_7e0c49db` | `*(this+4244) = 0`. | pattern scan |
| `0x7e0c4a0c` | 1 | `entry_thunk_7e0c4a0c` | `call` to the body directly after it (`0x7e0c4a14`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c4a60` | 1 | `entry_thunk_7e0c4a60` | `call` to the body directly after it (`0x7e0c4a68`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c4abf` | 3 | `entry_thunk_7e0c4abf` | `call` to the body directly after it (`0x7e0c4ac7`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c4c0e` | 2 | `obj_clear_f4260_7e0c4c0e` | `*(this+4260) = 0`. | pattern scan |
| `0x7e0c4c8f` | 2 | `entry_thunk_7e0c4c8f` | `call` to the body directly after it (`0x7e0c4c97`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c4d08` | 2 | `entry_thunk_7e0c4d08` | `call` to the body directly after it (`0x7e0c4d10`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c4f56` | 1 | `obj_clear_f4264_7e0c4f56` | `*(this+4264) = 0`. | pattern scan |
| `0x7e0c4f7c` | 2 | `entry_thunk_7e0c4f7c` | `call` to the body directly after it (`0x7e0c4f84`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c5001` | 1 | `entry_thunk_7e0c5001` | `call` to the body directly after it (`0x7e0c5009`, register-save mask `0xf0`, frame 60) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c510d` | 1 | `obj_clear_f4272_7e0c510d` | `*(this+4272) = 0`. | pattern scan |
| `0x7e0c5133` | 2 | `entry_thunk_7e0c5133` | `call` to the body directly after it (`0x7e0c513b`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c51b8` | 1 | `entry_thunk_7e0c51b8` | `call` to the body directly after it (`0x7e0c51c0`, register-save mask `0xf0`, frame 60) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c534d` | 2 | `obj_clear_f4288_7e0c534d` | `*(this+4288) = 0`. | pattern scan |
| `0x7e0c5394` | 1 | `entry_thunk_7e0c5394` | `call` to the body directly after it (`0x7e0c539c`, register-save mask `0xf0`, frame 68) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c54d3` | 1 | `entry_thunk_7e0c54d3` | `call` to the body directly after it (`0x7e0c54db`, register-save mask `0xb0`, frame 56) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c55c6` | 2 | `entry_thunk_7e0c55c6` | `call` to the body directly after it (`0x7e0c55ce`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c5770` | 1 | `entry_thunk_7e0c5770` | `call` to the body directly after it (`0x7e0c5778`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c5964` | 1 | `entry_thunk_7e0c5964` | `call` to the body directly after it (`0x7e0c596c`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c59f6` | 1 | `entry_thunk_7e0c59f6` | `call` to the body directly after it (`0x7e0c59fe`, register-save mask `0xf0`, frame 56) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c5e3a` | 1 | `entry_thunk_7e0c5e3a` | `call` to the body directly after it (`0x7e0c5e42`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c5ec9` | 2 | `entry_thunk_7e0c5ec9` | `call` to the body directly after it (`0x7e0c5ed1`, register-save mask `0xb0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c5f77` | 1 | `entry_thunk_7e0c5f77` | `call` to the body directly after it (`0x7e0c5f7f`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c5ffd` | 3 | `entry_thunk_7e0c5ffd` | `call` to the body directly after it (`0x7e0c6005`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c60e9` | 1 | `entry_thunk_7e0c60e9` | `call` to the body directly after it (`0x7e0c60f1`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c6156` | 1 | `entry_thunk_7e0c6156` | `call` to the body directly after it (`0x7e0c615e`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c62ad` | 1 | `entry_thunk_7e0c62ad` | `call` to the body directly after it (`0x7e0c62b5`, register-save mask `0xb0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c63d4` | 2 | `entry_thunk_7e0c63d4` | `call` to the body directly after it (`0x7e0c63dc`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c64a9` | 1 | `entry_thunk_7e0c64a9` | `call` to the body directly after it (`0x7e0c64b1`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c6557` | 2 | `entry_thunk_7e0c6557` | `call` to the body directly after it (`0x7e0c655f`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c65ac` | 1 | `entry_thunk_7e0c65ac` | `call` to the body directly after it (`0x7e0c65b4`, register-save mask `0xf0`, frame 56) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c6838` | 2 | `obj_clear_f4312_7e0c6838` | `*(this+4312) = 0`. | pattern scan |
| `0x7e0c687f` | 1 | `entry_thunk_7e0c687f` | `call` to the body directly after it (`0x7e0c6887`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c68d9` | 1 | `entry_thunk_7e0c68d9` | `call` to the body directly after it (`0x7e0c68e1`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c6937` | 1 | `entry_thunk_7e0c6937` | `call` to the body directly after it (`0x7e0c693f`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c6a09` | 1 | `entry_thunk_7e0c6a09` | `call` to the body directly after it (`0x7e0c6a11`, register-save mask `0xb0`, frame 20) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c6a89` | 2 | `entry_thunk_7e0c6a89` | `call` to the body directly after it (`0x7e0c6a91`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c6d1a` | 1 | `entry_thunk_7e0c6d1a` | `call` to the body directly after it (`0x7e0c6d22`, register-save mask `0xb0`, frame 64) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c6e5f` | 1 | `entry_thunk_7e0c6e5f` | `call` to the body directly after it (`0x7e0c6e67`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c6f44` | 4 | `entry_thunk_7e0c6f44` | `call` to the body directly after it (`0x7e0c6f4c`, register-save mask `0xf0`, frame 112) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c7187` | 2 | `entry_thunk_7e0c7187` | `call` to the body directly after it (`0x7e0c718f`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c71ca` | 7 | `entry_thunk_7e0c71ca` | `call` to the body directly after it (`0x7e0c71d2`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c731f` | 1 | `entry_thunk_7e0c731f` | `call` to the body directly after it (`0x7e0c7327`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c73b2` | 1 | `entry_thunk_7e0c73b2` | `call` to the body directly after it (`0x7e0c73ba`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c745b` | 1 | `entry_thunk_7e0c745b` | `call` to the body directly after it (`0x7e0c7463`, register-save mask `0xf0`, frame 64) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c7678` | 1 | `entry_thunk_7e0c7678` | `call` to the body directly after it (`0x7e0c7680`, register-save mask `0x30`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c7755` | 2 | `obj_clear_f4316_7e0c7755` | `*(this+4316) = 0`. | pattern scan |
| `0x7e0c7791` | 1 | `entry_thunk_7e0c7791` | `call` to the body directly after it (`0x7e0c7799`, register-save mask `0xb0`, frame 64) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c78ff` | 1 | `entry_thunk_7e0c78ff` | `call` to the body directly after it (`0x7e0c7907`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c8b9c` | 1 | `entry_thunk_7e0c8b9c` | `call` to the body directly after it (`0x7e0c8ba4`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c8bf2` | 1 | `entry_thunk_7e0c8bf2` | `call` to the body directly after it (`0x7e0c8bfa`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c8cc3` | 3 | `entry_thunk_7e0c8cc3` | `call` to the body directly after it (`0x7e0c8ccb`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c8e1b` | 1 | `entry_thunk_7e0c8e1b` | `call` to the body directly after it (`0x7e0c8e23`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c9907` | 1 | `entry_thunk_7e0c9907` | `call` to the body directly after it (`0x7e0c990f`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c995d` | 1 | `entry_thunk_7e0c995d` | `call` to the body directly after it (`0x7e0c9965`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c9a2e` | 3 | `entry_thunk_7e0c9a2e` | `call` to the body directly after it (`0x7e0c9a36`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c9ae7` | 1 | `obj_clear_f324_7e0c9ae7` | `*(this+324) = 0`. | pattern scan |
| `0x7e0c9b87` | 1 | `entry_thunk_7e0c9b87` | `call` to the body directly after it (`0x7e0c9b8f`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0c9c12` | 2 | `entry_thunk_7e0c9c12` | `call` to the body directly after it (`0x7e0c9c1a`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0cafa0` | 1 | `entry_thunk_7e0cafa0` | `call` to the body directly after it (`0x7e0cafa8`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0caff6` | 1 | `entry_thunk_7e0caff6` | `call` to the body directly after it (`0x7e0caffe`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0cb0ce` | 3 | `entry_thunk_7e0cb0ce` | `call` to the body directly after it (`0x7e0cb0d6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0cb174` | 1 | `entry_thunk_7e0cb174` | `call` to the body directly after it (`0x7e0cb17c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ccd5c` | 1 | `entry_thunk_7e0ccd5c` | `call` to the body directly after it (`0x7e0ccd64`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ccdb2` | 1 | `entry_thunk_7e0ccdb2` | `call` to the body directly after it (`0x7e0ccdba`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0cce8a` | 3 | `entry_thunk_7e0cce8a` | `call` to the body directly after it (`0x7e0cce92`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ccf30` | 1 | `entry_thunk_7e0ccf30` | `call` to the body directly after it (`0x7e0ccf38`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d4843` | 1 | `entry_thunk_7e0d4843` | `call` to the body directly after it (`0x7e0d484b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d485f` | 1 | `entry_thunk_7e0d485f` | `call` to the body directly after it (`0x7e0d4867`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d493a` | 2 | `entry_thunk_7e0d493a` | `call` to the body directly after it (`0x7e0d4942`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d49b7` | 1 | `entry_thunk_7e0d49b7` | `call` to the body directly after it (`0x7e0d49bf`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d63d9` | 1 | `entry_thunk_7e0d63d9` | `call` to the body directly after it (`0x7e0d63e1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d63f5` | 1 | `entry_thunk_7e0d63f5` | `call` to the body directly after it (`0x7e0d63fd`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d64d0` | 2 | `entry_thunk_7e0d64d0` | `call` to the body directly after it (`0x7e0d64d8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d654d` | 1 | `entry_thunk_7e0d654d` | `call` to the body directly after it (`0x7e0d6555`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d6b2c` | 1 | `entry_thunk_7e0d6b2c` | `call` to the body directly after it (`0x7e0d6b34`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d6b48` | 1 | `entry_thunk_7e0d6b48` | `call` to the body directly after it (`0x7e0d6b50`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d6c41` | 3 | `entry_thunk_7e0d6c41` | `call` to the body directly after it (`0x7e0d6c49`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d6cc1` | 1 | `entry_thunk_7e0d6cc1` | `call` to the body directly after it (`0x7e0d6cc9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d7396` | 1 | `entry_thunk_7e0d7396` | `call` to the body directly after it (`0x7e0d739e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d73b2` | 1 | `entry_thunk_7e0d73b2` | `call` to the body directly after it (`0x7e0d73ba`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d748d` | 2 | `entry_thunk_7e0d748d` | `call` to the body directly after it (`0x7e0d7495`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d759a` | 2 | `entry_thunk_7e0d759a` | `call` to the body directly after it (`0x7e0d75a2`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d760d` | 1 | `entry_thunk_7e0d760d` | `call` to the body directly after it (`0x7e0d7615`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d9050` | 1 | `entry_thunk_7e0d9050` | `call` to the body directly after it (`0x7e0d9058`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d9065` | 1 | `entry_thunk_7e0d9065` | `call` to the body directly after it (`0x7e0d906d`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d90c9` | 2 | `entry_thunk_7e0d90c9` | `call` to the body directly after it (`0x7e0d90d1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d92c8` | 2 | `entry_thunk_7e0d92c8` | `call` to the body directly after it (`0x7e0d92d0`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d9328` | 1 | `entry_thunk_7e0d9328` | `call` to the body directly after it (`0x7e0d9330`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d9401` | 1 | `obj_clear_f468_7e0d9401` | `*(this+468) = 0`. | pattern scan |
| `0x7e0d941a` | 1 | `entry_thunk_7e0d941a` | `call` to the body directly after it (`0x7e0d9422`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d945d` | 1 | `entry_thunk_7e0d945d` | `call` to the body directly after it (`0x7e0d9465`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d95a9` | 2 | `entry_thunk_7e0d95a9` | `call` to the body directly after it (`0x7e0d95b1`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d9672` | 5 | `entry_thunk_7e0d9672` | `call` to the body directly after it (`0x7e0d967a`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d96fd` | 1 | `entry_thunk_7e0d96fd` | `call` to the body directly after it (`0x7e0d9705`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d98ab` | 1 | `entry_thunk_7e0d98ab` | `call` to the body directly after it (`0x7e0d98b3`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d9939` | 1 | `entry_thunk_7e0d9939` | `call` to the body directly after it (`0x7e0d9941`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d998d` | 1 | `entry_thunk_7e0d998d` | `call` to the body directly after it (`0x7e0d9995`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d99aa` | 1 | `entry_thunk_7e0d99aa` | `call` to the body directly after it (`0x7e0d99b2`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d9aec` | 1 | `entry_thunk_7e0d9aec` | `call` to the body directly after it (`0x7e0d9af4`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d9cc2` | 1 | `entry_thunk_7e0d9cc2` | `call` to the body directly after it (`0x7e0d9cca`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0d9d76` | 1 | `entry_thunk_7e0d9d76` | `call` to the body directly after it (`0x7e0d9d7e`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0da97b` | 1 | `obj_set1_f184_7e0da97b` | `*(this+184) = 1`. | pattern scan |
| `0x7e0db38f` | 1 | `entry_thunk_7e0db38f` | `call` to the body directly after it (`0x7e0db397`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0db3a4` | 1 | `entry_thunk_7e0db3a4` | `call` to the body directly after it (`0x7e0db3ac`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0db408` | 2 | `entry_thunk_7e0db408` | `call` to the body directly after it (`0x7e0db410`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0db72f` | 2 | `entry_thunk_7e0db72f` | `call` to the body directly after it (`0x7e0db737`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0db788` | 1 | `entry_thunk_7e0db788` | `call` to the body directly after it (`0x7e0db790`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0db836` | 1 | `obj_clear_f272_7e0db836` | `*(this+272) = 0`. | pattern scan |
| `0x7e0dcd58` | 1 | `entry_thunk_7e0dcd58` | `call` to the body directly after it (`0x7e0dcd60`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0dcd74` | 1 | `entry_thunk_7e0dcd74` | `call` to the body directly after it (`0x7e0dcd7c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0dce4f` | 2 | `entry_thunk_7e0dce4f` | `call` to the body directly after it (`0x7e0dce57`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0dcf55` | 3 | `entry_thunk_7e0dcf55` | `call` to the body directly after it (`0x7e0dcf5d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0dcfb1` | 1 | `entry_thunk_7e0dcfb1` | `call` to the body directly after it (`0x7e0dcfb9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0dd0fb` | 2 | `entry_thunk_7e0dd0fb` | `call` to the body directly after it (`0x7e0dd103`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0dd535` | 1 | `entry_thunk_7e0dd535` | `call` to the body directly after it (`0x7e0dd53d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0dd551` | 1 | `entry_thunk_7e0dd551` | `call` to the body directly after it (`0x7e0dd559`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0dd648` | 3 | `entry_thunk_7e0dd648` | `call` to the body directly after it (`0x7e0dd650`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0dd7a4` | 3 | `entry_thunk_7e0dd7a4` | `call` to the body directly after it (`0x7e0dd7ac`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0dd830` | 1 | `entry_thunk_7e0dd830` | `call` to the body directly after it (`0x7e0dd838`, register-save mask `0xf0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0dd922` | 1 | `entry_thunk_7e0dd922` | `call` to the body directly after it (`0x7e0dd92a`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ddb37` | 1 | `entry_thunk_7e0ddb37` | `call` to the body directly after it (`0x7e0ddb3f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ddb53` | 1 | `entry_thunk_7e0ddb53` | `call` to the body directly after it (`0x7e0ddb5b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ddc4b` | 3 | `entry_thunk_7e0ddc4b` | `call` to the body directly after it (`0x7e0ddc53`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ddd10` | 1 | `obj_clear_f192_7e0ddd10` | `*(this+192) = 0`. | pattern scan |
| `0x7e0ddda0` | 3 | `entry_thunk_7e0ddda0` | `call` to the body directly after it (`0x7e0ddda8`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0dde1f` | 1 | `entry_thunk_7e0dde1f` | `call` to the body directly after it (`0x7e0dde27`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0ddeab` | 1 | `entry_thunk_7e0ddeab` | `call` to the body directly after it (`0x7e0ddeb3`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0df1b7` | 1 | `entry_thunk_7e0df1b7` | `call` to the body directly after it (`0x7e0df1bf`, register-save mask `0x00`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0df1eb` | 1 | `entry_thunk_7e0df1eb` | `call` to the body directly after it (`0x7e0df1f3`, register-save mask `0x20`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0df30f` | 3 | `entry_thunk_7e0df30f` | `call` to the body directly after it (`0x7e0df317`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0df4ec` | 1 | `obj_clear_f1116_7e0df4ec` | `*(this+1116) = 0`. | pattern scan |
| `0x7e0df505` | 1 | `entry_thunk_7e0df505` | `call` to the body directly after it (`0x7e0df50d`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0df559` | 1 | `entry_thunk_7e0df559` | `call` to the body directly after it (`0x7e0df561`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0df58e` | 1 | `obj_clear_f1124_7e0df58e` | `*(this+1124) = 0`. | pattern scan |
| `0x7e0df5b4` | 2 | `entry_thunk_7e0df5b4` | `call` to the body directly after it (`0x7e0df5bc`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0df608` | 1 | `entry_thunk_7e0df608` | `call` to the body directly after it (`0x7e0df610`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0df66b` | 1 | `obj_clear_f1132_7e0df66b` | `*(this+1132) = 0`. | pattern scan |
| `0x7e0df684` | 2 | `entry_thunk_7e0df684` | `call` to the body directly after it (`0x7e0df68c`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e2d5a` | 1 | `obj_clear_f552_7e0e2d5a` | `*(this+552) = 0`. | pattern scan |
| `0x7e0e2d9f` | 1 | `entry_thunk_7e0e2d9f` | `call` to the body directly after it (`0x7e0e2da7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e2dc1` | 2 | `entry_thunk_7e0e2dc1` | `call` to the body directly after it (`0x7e0e2dc9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e2e70` | 1 | `obj_clear_f972_7e0e2e70` | `*(this+972) = 0`. | pattern scan |
| `0x7e0e2eb6` | 1 | `entry_thunk_7e0e2eb6` | `call` to the body directly after it (`0x7e0e2ebe`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e2f35` | 2 | `entry_thunk_7e0e2f35` | `call` to the body directly after it (`0x7e0e2f3d`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e310f` | 2 | `entry_thunk_7e0e310f` | `call` to the body directly after it (`0x7e0e3117`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e3261` | 2 | `entry_thunk_7e0e3261` | `call` to the body directly after it (`0x7e0e3269`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e3498` | 2 | `entry_thunk_7e0e3498` | `call` to the body directly after it (`0x7e0e34a0`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e352a` | 1 | `entry_thunk_7e0e352a` | `call` to the body directly after it (`0x7e0e3532`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e357d` | 1 | `entry_thunk_7e0e357d` | `call` to the body directly after it (`0x7e0e3585`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e35d9` | 4 | `entry_thunk_7e0e35d9` | `call` to the body directly after it (`0x7e0e35e1`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e4e70` | 1 | `entry_thunk_7e0e4e70` | `call` to the body directly after it (`0x7e0e4e78`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e4f31` | 2 | `entry_thunk_7e0e4f31` | `call` to the body directly after it (`0x7e0e4f39`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e50b4` | 2 | `entry_thunk_7e0e50b4` | `call` to the body directly after it (`0x7e0e50bc`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e51b7` | 1 | `entry_thunk_7e0e51b7` | `call` to the body directly after it (`0x7e0e51bf`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e525e` | 1 | `entry_thunk_7e0e525e` | `call` to the body directly after it (`0x7e0e5266`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e52a1` | 1 | `entry_thunk_7e0e52a1` | `call` to the body directly after it (`0x7e0e52a9`, register-save mask `0xf0`, frame 84) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e698c` | 1 | `obj_clear_f552_7e0e698c` | `*(this+552) = 0`. | pattern scan |
| `0x7e0e69e9` | 1 | `entry_thunk_7e0e69e9` | `call` to the body directly after it (`0x7e0e69f1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e6a0b` | 2 | `entry_thunk_7e0e6a0b` | `call` to the body directly after it (`0x7e0e6a13`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e6b33` | 2 | `entry_thunk_7e0e6b33` | `call` to the body directly after it (`0x7e0e6b3b`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e6c42` | 1 | `entry_thunk_7e0e6c42` | `call` to the body directly after it (`0x7e0e6c4a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e6c9b` | 1 | `entry_thunk_7e0e6c9b` | `call` to the body directly after it (`0x7e0e6ca3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e6cee` | 1 | `entry_thunk_7e0e6cee` | `call` to the body directly after it (`0x7e0e6cf6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e6d10` | 3 | `entry_thunk_7e0e6d10` | `call` to the body directly after it (`0x7e0e6d18`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e0e6db9` | 1 | `entry_thunk_7e0e6db9` | `call` to the body directly after it (`0x7e0e6dc1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11c258` | 1 | `entry_thunk_7e11c258` | `call` to the body directly after it (`0x7e11c260`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11c274` | 1 | `entry_thunk_7e11c274` | `call` to the body directly after it (`0x7e11c27c`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11c3bb` | 3 | `entry_thunk_7e11c3bb` | `call` to the body directly after it (`0x7e11c3c3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11c505` | 1 | `obj_clear_f444_7e11c505` | `*(this+444) = 0`. | pattern scan |
| `0x7e11c51e` | 3 | `entry_thunk_7e11c51e` | `call` to the body directly after it (`0x7e11c526`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11e274` | 1 | `entry_thunk_7e11e274` | `call` to the body directly after it (`0x7e11e27c`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11e2d6` | 6 | `obj_clear_f460_7e11e2d6` | `*(this+460) = 0`. | pattern scan |
| `0x7e11e831` | 2 | `entry_thunk_7e11e831` | `call` to the body directly after it (`0x7e11e839`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11eca1` | 1 | `entry_thunk_7e11eca1` | `call` to the body directly after it (`0x7e11eca9`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11ecbe` | 1 | `entry_thunk_7e11ecbe` | `call` to the body directly after it (`0x7e11ecc6`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11ecdb` | 1 | `entry_thunk_7e11ecdb` | `call` to the body directly after it (`0x7e11ece3`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11ecf8` | 2 | `entry_thunk_7e11ecf8` | `call` to the body directly after it (`0x7e11ed00`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11ef35` | 1 | `entry_thunk_7e11ef35` | `call` to the body directly after it (`0x7e11ef3d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11f01b` | 1 | `entry_thunk_7e11f01b` | `call` to the body directly after it (`0x7e11f023`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11f0d8` | 2 | `obj_clear_f464_7e11f0d8` | `*(this+464) = 0`. | pattern scan |
| `0x7e11f28b` | 1 | `entry_thunk_7e11f28b` | `call` to the body directly after it (`0x7e11f293`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11f3cb` | 1 | `entry_thunk_7e11f3cb` | `call` to the body directly after it (`0x7e11f3d3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11f580` | 2 | `entry_thunk_7e11f580` | `call` to the body directly after it (`0x7e11f588`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11f6c7` | 2 | `entry_thunk_7e11f6c7` | `call` to the body directly after it (`0x7e11f6cf`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11f7fb` | 1 | `entry_thunk_7e11f7fb` | `call` to the body directly after it (`0x7e11f803`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11f849` | 1 | `entry_thunk_7e11f849` | `call` to the body directly after it (`0x7e11f851`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11f88c` | 7 | `entry_thunk_7e11f88c` | `call` to the body directly after it (`0x7e11f894`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e11ff53` | 3 | `obj_clear_f468_7e11ff53` | `*(this+468) = 0`. | pattern scan |
| `0x7e120206` | 2 | `entry_thunk_7e120206` | `call` to the body directly after it (`0x7e12020e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e120443` | 1 | `entry_thunk_7e120443` | `call` to the body directly after it (`0x7e12044b`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e120460` | 1 | `entry_thunk_7e120460` | `call` to the body directly after it (`0x7e120468`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e120545` | 2 | `entry_thunk_7e120545` | `call` to the body directly after it (`0x7e12054d`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e120588` | 4 | `entry_thunk_7e120588` | `call` to the body directly after it (`0x7e120590`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e121d77` | 1 | `entry_thunk_7e121d77` | `call` to the body directly after it (`0x7e121d7f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e121d93` | 1 | `entry_thunk_7e121d93` | `call` to the body directly after it (`0x7e121d9b`, register-save mask `0xf0`, frame 80) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e121f90` | 3 | `entry_thunk_7e121f90` | `call` to the body directly after it (`0x7e121f98`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1228bc` | 1 | `entry_thunk_7e1228bc` | `call` to the body directly after it (`0x7e1228c4`, register-save mask `0xb0`, frame 52) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e122c6d` | 1 | `entry_thunk_7e122c6d` | `call` to the body directly after it (`0x7e122c75`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1231c8` | 1 | `entry_thunk_7e1231c8` | `call` to the body directly after it (`0x7e1231d0`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1232be` | 1 | `entry_thunk_7e1232be` | `call` to the body directly after it (`0x7e1232c6`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e123369` | 1 | `entry_thunk_7e123369` | `call` to the body directly after it (`0x7e123371`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e123431` | 1 | `entry_thunk_7e123431` | `call` to the body directly after it (`0x7e123439`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1235ad` | 1 | `entry_thunk_7e1235ad` | `call` to the body directly after it (`0x7e1235b5`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e123658` | 1 | `entry_thunk_7e123658` | `call` to the body directly after it (`0x7e123660`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e123707` | 1 | `entry_thunk_7e123707` | `call` to the body directly after it (`0x7e12370f`, register-save mask `0xb0`, frame 52) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1238e4` | 10 | `entry_thunk_7e1238e4` | `call` to the body directly after it (`0x7e1238ec`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e12403a` | 1 | `entry_thunk_7e12403a` | `call` to the body directly after it (`0x7e124042`, register-save mask `0xf0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e124139` | 1 | `entry_thunk_7e124139` | `call` to the body directly after it (`0x7e124141`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e124209` | 1 | `obj_clear_f712_7e124209` | `*(this+712) = 0`. | pattern scan |
| `0x7e12426e` | 1 | `entry_thunk_7e12426e` | `call` to the body directly after it (`0x7e124276`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e12434a` | 1 | `entry_thunk_7e12434a` | `call` to the body directly after it (`0x7e124352`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e124426` | 3 | `entry_thunk_7e124426` | `call` to the body directly after it (`0x7e12442e`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e124559` | 1 | `obj_clear_f724_7e124559` | `*(this+724) = 0`. | pattern scan |
| `0x7e1246e1` | 2 | `entry_thunk_7e1246e1` | `call` to the body directly after it (`0x7e1246e9`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e12481f` | 1 | `entry_thunk_7e12481f` | `call` to the body directly after it (`0x7e124827`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1248b9` | 3 | `entry_thunk_7e1248b9` | `call` to the body directly after it (`0x7e1248c1`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e124a61` | 1 | `obj_clear_f736_7e124a61` | `*(this+736) = 0`. | pattern scan |
| `0x7e124a6d` | 3 | `entry_thunk_7e124a6d` | `call` to the body directly after it (`0x7e124a75`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e124b6b` | 2 | `entry_thunk_7e124b6b` | `call` to the body directly after it (`0x7e124b73`, register-save mask `0x00`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e124ecb` | 1 | `entry_thunk_7e124ecb` | `call` to the body directly after it (`0x7e124ed3`, register-save mask `0x00`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e125119` | 1 | `entry_thunk_7e125119` | `call` to the body directly after it (`0x7e125121`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e125135` | 1 | `entry_thunk_7e125135` | `call` to the body directly after it (`0x7e12513d`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e125266` | 3 | `entry_thunk_7e125266` | `call` to the body directly after it (`0x7e12526e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1252e5` | 1 | `entry_thunk_7e1252e5` | `call` to the body directly after it (`0x7e1252ed`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e125552` | 1 | `entry_thunk_7e125552` | `call` to the body directly after it (`0x7e12555a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e12556e` | 1 | `entry_thunk_7e12556e` | `call` to the body directly after it (`0x7e125576`, register-save mask `0xf0`, frame 36) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1256af` | 3 | `entry_thunk_7e1256af` | `call` to the body directly after it (`0x7e1256b7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e125741` | 1 | `obj_clear_f240_7e125741` | `*(this+240) = 0`. | pattern scan |
| `0x7e125794` | 1 | `entry_thunk_7e125794` | `call` to the body directly after it (`0x7e12579c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1258d2` | 5 | `entry_thunk_7e1258d2` | `call` to the body directly after it (`0x7e1258da`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e125c4d` | 1 | `entry_thunk_7e125c4d` | `call` to the body directly after it (`0x7e125c55`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e125fd5` | 2 | `obj_set1_f252_7e125fd5` | `*(this+252) = 1`. | pattern scan |
| `0x7e125fde` | 1 | `obj_clear_f552_7e125fde` | `*(this+552) = 0`. | pattern scan |
| `0x7e126022` | 1 | `entry_thunk_7e126022` | `call` to the body directly after it (`0x7e12602a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e126046` | 2 | `entry_thunk_7e126046` | `call` to the body directly after it (`0x7e12604e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e126180` | 2 | `entry_thunk_7e126180` | `call` to the body directly after it (`0x7e126188`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e126293` | 1 | `entry_thunk_7e126293` | `call` to the body directly after it (`0x7e12629b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1262f0` | 1 | `entry_thunk_7e1262f0` | `call` to the body directly after it (`0x7e1262f8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e126345` | 1 | `entry_thunk_7e126345` | `call` to the body directly after it (`0x7e12634d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e126369` | 3 | `entry_thunk_7e126369` | `call` to the body directly after it (`0x7e126371`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e126b0e` | 2 | `obj_clear_f952_7e126b0e` | `*(this+952) = 0`. | pattern scan |
| `0x7e126b55` | 1 | `entry_thunk_7e126b55` | `call` to the body directly after it (`0x7e126b5d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e126bba` | 2 | `obj_clear_f1024_7e126bba` | `*(this+1024) = 0`. | pattern scan |
| `0x7e126c01` | 1 | `entry_thunk_7e126c01` | `call` to the body directly after it (`0x7e126c09`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e126d85` | 2 | `obj_clear_f956_7e126d85` | `*(this+956) = 0`. | pattern scan |
| `0x7e126dcc` | 1 | `entry_thunk_7e126dcc` | `call` to the body directly after it (`0x7e126dd4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e126df0` | 1 | `entry_thunk_7e126df0` | `call` to the body directly after it (`0x7e126df8`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e12700d` | 2 | `obj_clear_f960_7e12700d` | `*(this+960) = 0`. | pattern scan |
| `0x7e127054` | 1 | `entry_thunk_7e127054` | `call` to the body directly after it (`0x7e12705c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e127086` | 2 | `obj_clear_f964_7e127086` | `*(this+964) = 0`. | pattern scan |
| `0x7e1270cd` | 1 | `entry_thunk_7e1270cd` | `call` to the body directly after it (`0x7e1270d5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1270ff` | 2 | `obj_clear_f968_7e1270ff` | `*(this+968) = 0`. | pattern scan |
| `0x7e127146` | 1 | `entry_thunk_7e127146` | `call` to the body directly after it (`0x7e12714e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e127178` | 2 | `obj_clear_f972_7e127178` | `*(this+972) = 0`. | pattern scan |
| `0x7e1271bf` | 1 | `entry_thunk_7e1271bf` | `call` to the body directly after it (`0x7e1271c7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1271f1` | 2 | `obj_clear_f976_7e1271f1` | `*(this+976) = 0`. | pattern scan |
| `0x7e127238` | 1 | `entry_thunk_7e127238` | `call` to the body directly after it (`0x7e127240`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e12726a` | 2 | `obj_clear_f980_7e12726a` | `*(this+980) = 0`. | pattern scan |
| `0x7e1272b1` | 1 | `entry_thunk_7e1272b1` | `call` to the body directly after it (`0x7e1272b9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1272e3` | 2 | `obj_clear_f984_7e1272e3` | `*(this+984) = 0`. | pattern scan |
| `0x7e12732a` | 1 | `entry_thunk_7e12732a` | `call` to the body directly after it (`0x7e127332`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e12735c` | 2 | `obj_clear_f988_7e12735c` | `*(this+988) = 0`. | pattern scan |
| `0x7e1273a3` | 1 | `entry_thunk_7e1273a3` | `call` to the body directly after it (`0x7e1273ab`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1273d5` | 2 | `obj_clear_f992_7e1273d5` | `*(this+992) = 0`. | pattern scan |
| `0x7e12741c` | 1 | `entry_thunk_7e12741c` | `call` to the body directly after it (`0x7e127424`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e12744e` | 2 | `obj_clear_f996_7e12744e` | `*(this+996) = 0`. | pattern scan |
| `0x7e127495` | 1 | `entry_thunk_7e127495` | `call` to the body directly after it (`0x7e12749d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1274c7` | 2 | `obj_clear_f1000_7e1274c7` | `*(this+1000) = 0`. | pattern scan |
| `0x7e12750e` | 1 | `entry_thunk_7e12750e` | `call` to the body directly after it (`0x7e127516`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e127612` | 2 | `obj_clear_f1004_7e127612` | `*(this+1004) = 0`. | pattern scan |
| `0x7e127659` | 1 | `entry_thunk_7e127659` | `call` to the body directly after it (`0x7e127661`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e12768b` | 2 | `obj_clear_f1028_7e12768b` | `*(this+1028) = 0`. | pattern scan |
| `0x7e1276d2` | 1 | `entry_thunk_7e1276d2` | `call` to the body directly after it (`0x7e1276da`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1279ab` | 2 | `obj_clear_f1008_7e1279ab` | `*(this+1008) = 0`. | pattern scan |
| `0x7e1279f2` | 1 | `entry_thunk_7e1279f2` | `call` to the body directly after it (`0x7e1279fa`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e127a79` | 1 | `entry_thunk_7e127a79` | `call` to the body directly after it (`0x7e127a81`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e127aab` | 2 | `obj_clear_f1016_7e127aab` | `*(this+1016) = 0`. | pattern scan |
| `0x7e127af2` | 1 | `entry_thunk_7e127af2` | `call` to the body directly after it (`0x7e127afa`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e127b24` | 2 | `obj_clear_f1020_7e127b24` | `*(this+1020) = 0`. | pattern scan |
| `0x7e127b6b` | 1 | `entry_thunk_7e127b6b` | `call` to the body directly after it (`0x7e127b73`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e127b8f` | 1 | `entry_thunk_7e127b8f` | `call` to the body directly after it (`0x7e127b97`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e130188` | 2 | `obj_set1_f252_7e130188` | `*(this+252) = 1`. | pattern scan |
| `0x7e130191` | 1 | `obj_clear_f552_7e130191` | `*(this+552) = 0`. | pattern scan |
| `0x7e1301d5` | 1 | `entry_thunk_7e1301d5` | `call` to the body directly after it (`0x7e1301dd`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1301f9` | 2 | `entry_thunk_7e1301f9` | `call` to the body directly after it (`0x7e130201`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e130333` | 2 | `entry_thunk_7e130333` | `call` to the body directly after it (`0x7e13033b`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e130446` | 1 | `entry_thunk_7e130446` | `call` to the body directly after it (`0x7e13044e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1304a3` | 1 | `entry_thunk_7e1304a3` | `call` to the body directly after it (`0x7e1304ab`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1304f8` | 1 | `entry_thunk_7e1304f8` | `call` to the body directly after it (`0x7e130500`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e13051c` | 3 | `entry_thunk_7e13051c` | `call` to the body directly after it (`0x7e130524`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e130df5` | 3 | `entry_thunk_7e130df5` | `call` to the body directly after it (`0x7e130dfd`, register-save mask `0x00`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e130f64` | 3 | `entry_thunk_7e130f64` | `call` to the body directly after it (`0x7e130f6c`, register-save mask `0xa0`, frame 24) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e130fe7` | 3 | `entry_thunk_7e130fe7` | `call` to the body directly after it (`0x7e130fef`, register-save mask `0xf0`, frame 144) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e131723` | 2 | `obj_clear_f952_7e131723` | `*(this+952) = 0`. | pattern scan |
| `0x7e13175f` | 1 | `entry_thunk_7e13175f` | `call` to the body directly after it (`0x7e131767`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1317c4` | 2 | `obj_clear_f956_7e1317c4` | `*(this+956) = 0`. | pattern scan |
| `0x7e131800` | 1 | `entry_thunk_7e131800` | `call` to the body directly after it (`0x7e131808`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e131832` | 2 | `obj_clear_f11824_7e131832` | `*(this+11824) = 0`. | pattern scan |
| `0x7e13186e` | 1 | `entry_thunk_7e13186e` | `call` to the body directly after it (`0x7e131876`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e132168` | 1 | `entry_thunk_7e132168` | `call` to the body directly after it (`0x7e132170`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1324f4` | 2 | `obj_clear_f11828_7e1324f4` | `*(this+11828) = 0`. | pattern scan |
| `0x7e132530` | 1 | `entry_thunk_7e132530` | `call` to the body directly after it (`0x7e132538`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1326cf` | 1 | `entry_thunk_7e1326cf` | `call` to the body directly after it (`0x7e1326d7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e132727` | 2 | `obj_clear_f11832_7e132727` | `*(this+11832) = 0`. | pattern scan |
| `0x7e132763` | 1 | `entry_thunk_7e132763` | `call` to the body directly after it (`0x7e13276b`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e132b17` | 2 | `obj_clear_f11836_7e132b17` | `*(this+11836) = 0`. | pattern scan |
| `0x7e132b53` | 1 | `entry_thunk_7e132b53` | `call` to the body directly after it (`0x7e132b5b`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e132bd3` | 1 | `entry_thunk_7e132bd3` | `call` to the body directly after it (`0x7e132bdb`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e132c2b` | 2 | `obj_clear_f11840_7e132c2b` | `*(this+11840) = 0`. | pattern scan |
| `0x7e132c67` | 1 | `entry_thunk_7e132c67` | `call` to the body directly after it (`0x7e132c6f`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e132d27` | 2 | `obj_clear_f11844_7e132d27` | `*(this+11844) = 0`. | pattern scan |
| `0x7e132d63` | 1 | `entry_thunk_7e132d63` | `call` to the body directly after it (`0x7e132d6b`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e132f92` | 2 | `obj_clear_f11848_7e132f92` | `*(this+11848) = 0`. | pattern scan |
| `0x7e132fce` | 1 | `entry_thunk_7e132fce` | `call` to the body directly after it (`0x7e132fd6`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1332ee` | 2 | `obj_clear_f11852_7e1332ee` | `*(this+11852) = 0`. | pattern scan |
| `0x7e13332a` | 1 | `entry_thunk_7e13332a` | `call` to the body directly after it (`0x7e133332`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e133504` | 2 | `obj_clear_f11856_7e133504` | `*(this+11856) = 0`. | pattern scan |
| `0x7e133540` | 1 | `entry_thunk_7e133540` | `call` to the body directly after it (`0x7e133548`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e133610` | 2 | `obj_clear_f11860_7e133610` | `*(this+11860) = 0`. | pattern scan |
| `0x7e13364c` | 1 | `entry_thunk_7e13364c` | `call` to the body directly after it (`0x7e133654`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e13370e` | 1 | `entry_thunk_7e13370e` | `call` to the body directly after it (`0x7e133716`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e133766` | 2 | `obj_clear_f11864_7e133766` | `*(this+11864) = 0`. | pattern scan |
| `0x7e1337a2` | 1 | `entry_thunk_7e1337a2` | `call` to the body directly after it (`0x7e1337aa`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e133947` | 2 | `obj_clear_f11868_7e133947` | `*(this+11868) = 0`. | pattern scan |
| `0x7e133983` | 1 | `entry_thunk_7e133983` | `call` to the body directly after it (`0x7e13398b`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e133bfc` | 2 | `obj_clear_f11872_7e133bfc` | `*(this+11872) = 0`. | pattern scan |
| `0x7e133c38` | 1 | `entry_thunk_7e133c38` | `call` to the body directly after it (`0x7e133c40`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e133d55` | 2 | `obj_clear_f11876_7e133d55` | `*(this+11876) = 0`. | pattern scan |
| `0x7e133d91` | 1 | `entry_thunk_7e133d91` | `call` to the body directly after it (`0x7e133d99`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e133e51` | 2 | `obj_clear_f11880_7e133e51` | `*(this+11880) = 0`. | pattern scan |
| `0x7e133e8d` | 1 | `entry_thunk_7e133e8d` | `call` to the body directly after it (`0x7e133e95`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e133f74` | 2 | `obj_clear_f11884_7e133f74` | `*(this+11884) = 0`. | pattern scan |
| `0x7e133fb0` | 1 | `entry_thunk_7e133fb0` | `call` to the body directly after it (`0x7e133fb8`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e134082` | 2 | `obj_clear_f960_7e134082` | `*(this+960) = 0`. | pattern scan |
| `0x7e1340be` | 1 | `entry_thunk_7e1340be` | `call` to the body directly after it (`0x7e1340c6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1340f0` | 2 | `obj_clear_f964_7e1340f0` | `*(this+964) = 0`. | pattern scan |
| `0x7e13412c` | 1 | `entry_thunk_7e13412c` | `call` to the body directly after it (`0x7e134134`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e13415e` | 2 | `obj_clear_f968_7e13415e` | `*(this+968) = 0`. | pattern scan |
| `0x7e13419a` | 1 | `entry_thunk_7e13419a` | `call` to the body directly after it (`0x7e1341a2`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1341cc` | 2 | `obj_clear_f972_7e1341cc` | `*(this+972) = 0`. | pattern scan |
| `0x7e134208` | 1 | `entry_thunk_7e134208` | `call` to the body directly after it (`0x7e134210`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e13423a` | 2 | `obj_clear_f976_7e13423a` | `*(this+976) = 0`. | pattern scan |
| `0x7e134276` | 1 | `entry_thunk_7e134276` | `call` to the body directly after it (`0x7e13427e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1342a8` | 2 | `obj_clear_f980_7e1342a8` | `*(this+980) = 0`. | pattern scan |
| `0x7e1342e4` | 1 | `entry_thunk_7e1342e4` | `call` to the body directly after it (`0x7e1342ec`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e134316` | 2 | `obj_clear_f984_7e134316` | `*(this+984) = 0`. | pattern scan |
| `0x7e134352` | 1 | `entry_thunk_7e134352` | `call` to the body directly after it (`0x7e13435a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e134376` | 1 | `entry_thunk_7e134376` | `call` to the body directly after it (`0x7e13437e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1343ce` | 2 | `obj_clear_f988_7e1343ce` | `*(this+988) = 0`. | pattern scan |
| `0x7e13440a` | 1 | `entry_thunk_7e13440a` | `call` to the body directly after it (`0x7e134412`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e13443c` | 2 | `obj_clear_f992_7e13443c` | `*(this+992) = 0`. | pattern scan |
| `0x7e134478` | 1 | `entry_thunk_7e134478` | `call` to the body directly after it (`0x7e134480`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1344aa` | 2 | `obj_clear_f996_7e1344aa` | `*(this+996) = 0`. | pattern scan |
| `0x7e1344e6` | 1 | `entry_thunk_7e1344e6` | `call` to the body directly after it (`0x7e1344ee`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e134518` | 2 | `obj_clear_f1000_7e134518` | `*(this+1000) = 0`. | pattern scan |
| `0x7e134554` | 1 | `entry_thunk_7e134554` | `call` to the body directly after it (`0x7e13455c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e134658` | 2 | `obj_clear_f1004_7e134658` | `*(this+1004) = 0`. | pattern scan |
| `0x7e134694` | 1 | `entry_thunk_7e134694` | `call` to the body directly after it (`0x7e13469c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1346c6` | 2 | `obj_clear_f1008_7e1346c6` | `*(this+1008) = 0`. | pattern scan |
| `0x7e134702` | 1 | `entry_thunk_7e134702` | `call` to the body directly after it (`0x7e13470a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e13477e` | 1 | `entry_thunk_7e13477e` | `call` to the body directly after it (`0x7e134786`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1347b0` | 2 | `obj_clear_f1016_7e1347b0` | `*(this+1016) = 0`. | pattern scan |
| `0x7e1347ec` | 1 | `entry_thunk_7e1347ec` | `call` to the body directly after it (`0x7e1347f4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e13481e` | 2 | `obj_clear_f1020_7e13481e` | `*(this+1020) = 0`. | pattern scan |
| `0x7e13485a` | 1 | `entry_thunk_7e13485a` | `call` to the body directly after it (`0x7e134862`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e13487e` | 1 | `entry_thunk_7e13487e` | `call` to the body directly after it (`0x7e134886`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14111b` | 2 | `obj_set1_f252_7e14111b` | `*(this+252) = 1`. | pattern scan |
| `0x7e141124` | 1 | `obj_clear_f552_7e141124` | `*(this+552) = 0`. | pattern scan |
| `0x7e141168` | 1 | `entry_thunk_7e141168` | `call` to the body directly after it (`0x7e141170`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14118c` | 2 | `entry_thunk_7e14118c` | `call` to the body directly after it (`0x7e141194`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1412c6` | 2 | `entry_thunk_7e1412c6` | `call` to the body directly after it (`0x7e1412ce`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1413d9` | 1 | `entry_thunk_7e1413d9` | `call` to the body directly after it (`0x7e1413e1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e141436` | 1 | `entry_thunk_7e141436` | `call` to the body directly after it (`0x7e14143e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14148b` | 1 | `entry_thunk_7e14148b` | `call` to the body directly after it (`0x7e141493`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1414af` | 3 | `entry_thunk_7e1414af` | `call` to the body directly after it (`0x7e1414b7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e141df8` | 3 | `entry_thunk_7e141df8` | `call` to the body directly after it (`0x7e141e00`, register-save mask `0x00`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1420b6` | 3 | `entry_thunk_7e1420b6` | `call` to the body directly after it (`0x7e1420be`, register-save mask `0xf0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1421f1` | 3 | `entry_thunk_7e1421f1` | `call` to the body directly after it (`0x7e1421f9`, register-save mask `0x20`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1426da` | 1 | `entry_thunk_7e1426da` | `call` to the body directly after it (`0x7e1426e2`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14275d` | 2 | `obj_clear_f15660_7e14275d` | `*(this+15660) = 0`. | pattern scan |
| `0x7e142799` | 1 | `entry_thunk_7e142799` | `call` to the body directly after it (`0x7e1427a1`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e142d28` | 2 | `obj_clear_f15664_7e142d28` | `*(this+15664) = 0`. | pattern scan |
| `0x7e142d64` | 1 | `entry_thunk_7e142d64` | `call` to the body directly after it (`0x7e142d6c`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e142f56` | 2 | `obj_clear_f15668_7e142f56` | `*(this+15668) = 0`. | pattern scan |
| `0x7e142f92` | 1 | `entry_thunk_7e142f92` | `call` to the body directly after it (`0x7e142f9a`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e143113` | 2 | `obj_clear_f952_7e143113` | `*(this+952) = 0`. | pattern scan |
| `0x7e14314f` | 1 | `entry_thunk_7e14314f` | `call` to the body directly after it (`0x7e143157`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1431a6` | 1 | `entry_thunk_7e1431a6` | `call` to the body directly after it (`0x7e1431ae`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1431fe` | 2 | `obj_clear_f15672_7e1431fe` | `*(this+15672) = 0`. | pattern scan |
| `0x7e14323a` | 1 | `entry_thunk_7e14323a` | `call` to the body directly after it (`0x7e143242`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14325e` | 1 | `entry_thunk_7e14325e` | `call` to the body directly after it (`0x7e143266`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1432a8` | 1 | `entry_thunk_7e1432a8` | `call` to the body directly after it (`0x7e1432b0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14331d` | 1 | `entry_thunk_7e14331d` | `call` to the body directly after it (`0x7e143325`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e143367` | 1 | `entry_thunk_7e143367` | `call` to the body directly after it (`0x7e14336f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e143415` | 2 | `obj_clear_f15676_7e143415` | `*(this+15676) = 0`. | pattern scan |
| `0x7e143451` | 1 | `entry_thunk_7e143451` | `call` to the body directly after it (`0x7e143459`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e143899` | 2 | `obj_clear_f15680_7e143899` | `*(this+15680) = 0`. | pattern scan |
| `0x7e1438d5` | 1 | `entry_thunk_7e1438d5` | `call` to the body directly after it (`0x7e1438dd`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e143ad1` | 2 | `obj_clear_f956_7e143ad1` | `*(this+956) = 0`. | pattern scan |
| `0x7e143b0d` | 1 | `entry_thunk_7e143b0d` | `call` to the body directly after it (`0x7e143b15`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e143b3f` | 2 | `obj_clear_f15684_7e143b3f` | `*(this+15684) = 0`. | pattern scan |
| `0x7e143b7b` | 1 | `entry_thunk_7e143b7b` | `call` to the body directly after it (`0x7e143b83`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e143f2d` | 2 | `obj_clear_f15688_7e143f2d` | `*(this+15688) = 0`. | pattern scan |
| `0x7e143f69` | 1 | `entry_thunk_7e143f69` | `call` to the body directly after it (`0x7e143f71`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e144249` | 2 | `obj_clear_f15692_7e144249` | `*(this+15692) = 0`. | pattern scan |
| `0x7e144285` | 1 | `entry_thunk_7e144285` | `call` to the body directly after it (`0x7e14428d`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1443cd` | 1 | `entry_thunk_7e1443cd` | `call` to the body directly after it (`0x7e1443d5`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1448b7` | 2 | `obj_clear_f15696_7e1448b7` | `*(this+15696) = 0`. | pattern scan |
| `0x7e1448f3` | 2 | `entry_thunk_7e1448f3` | `call` to the body directly after it (`0x7e1448fb`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e144cc2` | 1 | `entry_thunk_7e144cc2` | `call` to the body directly after it (`0x7e144cca`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e144e4c` | 2 | `obj_clear_f15700_7e144e4c` | `*(this+15700) = 0`. | pattern scan |
| `0x7e144e88` | 1 | `entry_thunk_7e144e88` | `call` to the body directly after it (`0x7e144e90`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1450af` | 2 | `obj_clear_f960_7e1450af` | `*(this+960) = 0`. | pattern scan |
| `0x7e1450eb` | 1 | `entry_thunk_7e1450eb` | `call` to the body directly after it (`0x7e1450f3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14511d` | 2 | `obj_clear_f964_7e14511d` | `*(this+964) = 0`. | pattern scan |
| `0x7e145159` | 1 | `entry_thunk_7e145159` | `call` to the body directly after it (`0x7e145161`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14518b` | 2 | `obj_clear_f968_7e14518b` | `*(this+968) = 0`. | pattern scan |
| `0x7e1451c7` | 1 | `entry_thunk_7e1451c7` | `call` to the body directly after it (`0x7e1451cf`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1451f9` | 2 | `obj_clear_f15704_7e1451f9` | `*(this+15704) = 0`. | pattern scan |
| `0x7e145235` | 1 | `entry_thunk_7e145235` | `call` to the body directly after it (`0x7e14523d`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e145303` | 2 | `obj_clear_f15708_7e145303` | `*(this+15708) = 0`. | pattern scan |
| `0x7e14533f` | 1 | `entry_thunk_7e14533f` | `call` to the body directly after it (`0x7e145347`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14596a` | 2 | `obj_clear_f972_7e14596a` | `*(this+972) = 0`. | pattern scan |
| `0x7e1459a6` | 1 | `entry_thunk_7e1459a6` | `call` to the body directly after it (`0x7e1459ae`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1459d8` | 2 | `obj_clear_f976_7e1459d8` | `*(this+976) = 0`. | pattern scan |
| `0x7e145a14` | 1 | `entry_thunk_7e145a14` | `call` to the body directly after it (`0x7e145a1c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e145a46` | 2 | `obj_clear_f980_7e145a46` | `*(this+980) = 0`. | pattern scan |
| `0x7e145a82` | 1 | `entry_thunk_7e145a82` | `call` to the body directly after it (`0x7e145a8a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e145ab4` | 2 | `obj_clear_f984_7e145ab4` | `*(this+984) = 0`. | pattern scan |
| `0x7e145af0` | 1 | `entry_thunk_7e145af0` | `call` to the body directly after it (`0x7e145af8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e145b22` | 2 | `obj_clear_f988_7e145b22` | `*(this+988) = 0`. | pattern scan |
| `0x7e145b5e` | 1 | `entry_thunk_7e145b5e` | `call` to the body directly after it (`0x7e145b66`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e145b90` | 2 | `obj_clear_f992_7e145b90` | `*(this+992) = 0`. | pattern scan |
| `0x7e145bcc` | 1 | `entry_thunk_7e145bcc` | `call` to the body directly after it (`0x7e145bd4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e145bfe` | 2 | `obj_clear_f996_7e145bfe` | `*(this+996) = 0`. | pattern scan |
| `0x7e145c3a` | 1 | `entry_thunk_7e145c3a` | `call` to the body directly after it (`0x7e145c42`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e145c6c` | 2 | `obj_clear_f15712_7e145c6c` | `*(this+15712) = 0`. | pattern scan |
| `0x7e145ca8` | 1 | `entry_thunk_7e145ca8` | `call` to the body directly after it (`0x7e145cb0`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e146404` | 2 | `obj_clear_f15716_7e146404` | `*(this+15716) = 0`. | pattern scan |
| `0x7e146440` | 1 | `entry_thunk_7e146440` | `call` to the body directly after it (`0x7e146448`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14674f` | 2 | `obj_clear_f15720_7e14674f` | `*(this+15720) = 0`. | pattern scan |
| `0x7e14678b` | 1 | `entry_thunk_7e14678b` | `call` to the body directly after it (`0x7e146793`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e146d32` | 2 | `obj_clear_f15724_7e146d32` | `*(this+15724) = 0`. | pattern scan |
| `0x7e146d6e` | 1 | `entry_thunk_7e146d6e` | `call` to the body directly after it (`0x7e146d76`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e146fe3` | 2 | `obj_clear_f15728_7e146fe3` | `*(this+15728) = 0`. | pattern scan |
| `0x7e14701f` | 1 | `entry_thunk_7e14701f` | `call` to the body directly after it (`0x7e147027`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1472cd` | 2 | `obj_clear_f15732_7e1472cd` | `*(this+15732) = 0`. | pattern scan |
| `0x7e147309` | 1 | `entry_thunk_7e147309` | `call` to the body directly after it (`0x7e147311`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14751c` | 2 | `obj_clear_f1000_7e14751c` | `*(this+1000) = 0`. | pattern scan |
| `0x7e147558` | 1 | `entry_thunk_7e147558` | `call` to the body directly after it (`0x7e147560`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14765c` | 2 | `obj_clear_f15736_7e14765c` | `*(this+15736) = 0`. | pattern scan |
| `0x7e147698` | 1 | `entry_thunk_7e147698` | `call` to the body directly after it (`0x7e1476a0`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1477d1` | 1 | `entry_thunk_7e1477d1` | `call` to the body directly after it (`0x7e1477d9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14781b` | 1 | `entry_thunk_7e14781b` | `call` to the body directly after it (`0x7e147823`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e147865` | 1 | `entry_thunk_7e147865` | `call` to the body directly after it (`0x7e14786d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1478ec` | 2 | `obj_clear_f1004_7e1478ec` | `*(this+1004) = 0`. | pattern scan |
| `0x7e147928` | 1 | `entry_thunk_7e147928` | `call` to the body directly after it (`0x7e147930`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14794c` | 1 | `entry_thunk_7e14794c` | `call` to the body directly after it (`0x7e147954`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e147996` | 1 | `entry_thunk_7e147996` | `call` to the body directly after it (`0x7e14799e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1479ee` | 2 | `obj_clear_f15740_7e1479ee` | `*(this+15740) = 0`. | pattern scan |
| `0x7e147a2a` | 1 | `entry_thunk_7e147a2a` | `call` to the body directly after it (`0x7e147a32`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e147b0f` | 2 | `obj_clear_f1008_7e147b0f` | `*(this+1008) = 0`. | pattern scan |
| `0x7e147b4b` | 1 | `entry_thunk_7e147b4b` | `call` to the body directly after it (`0x7e147b53`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e147bc7` | 1 | `entry_thunk_7e147bc7` | `call` to the body directly after it (`0x7e147bcf`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e147bf9` | 2 | `obj_clear_f1016_7e147bf9` | `*(this+1016) = 0`. | pattern scan |
| `0x7e147c35` | 1 | `entry_thunk_7e147c35` | `call` to the body directly after it (`0x7e147c3d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e147c67` | 2 | `obj_clear_f15744_7e147c67` | `*(this+15744) = 0`. | pattern scan |
| `0x7e147ca3` | 1 | `entry_thunk_7e147ca3` | `call` to the body directly after it (`0x7e147cab`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e147df9` | 2 | `obj_clear_f1020_7e147df9` | `*(this+1020) = 0`. | pattern scan |
| `0x7e147e35` | 1 | `entry_thunk_7e147e35` | `call` to the body directly after it (`0x7e147e3d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e147e67` | 2 | `obj_clear_f15748_7e147e67` | `*(this+15748) = 0`. | pattern scan |
| `0x7e147ea3` | 1 | `entry_thunk_7e147ea3` | `call` to the body directly after it (`0x7e147eab`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e147fe3` | 2 | `obj_clear_f15752_7e147fe3` | `*(this+15752) = 0`. | pattern scan |
| `0x7e14801f` | 1 | `entry_thunk_7e14801f` | `call` to the body directly after it (`0x7e148027`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1481ab` | 2 | `obj_clear_f15756_7e1481ab` | `*(this+15756) = 0`. | pattern scan |
| `0x7e1481e7` | 1 | `entry_thunk_7e1481e7` | `call` to the body directly after it (`0x7e1481ef`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e148316` | 1 | `entry_thunk_7e148316` | `call` to the body directly after it (`0x7e14831e`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14921a` | 2 | `obj_set1_f252_7e14921a` | `*(this+252) = 1`. | pattern scan |
| `0x7e149223` | 1 | `obj_clear_f552_7e149223` | `*(this+552) = 0`. | pattern scan |
| `0x7e149267` | 1 | `entry_thunk_7e149267` | `call` to the body directly after it (`0x7e14926f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14928b` | 2 | `entry_thunk_7e14928b` | `call` to the body directly after it (`0x7e149293`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1493c5` | 2 | `entry_thunk_7e1493c5` | `call` to the body directly after it (`0x7e1493cd`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1494d8` | 1 | `entry_thunk_7e1494d8` | `call` to the body directly after it (`0x7e1494e0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e149535` | 1 | `entry_thunk_7e149535` | `call` to the body directly after it (`0x7e14953d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14958a` | 1 | `entry_thunk_7e14958a` | `call` to the body directly after it (`0x7e149592`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1495ae` | 3 | `entry_thunk_7e1495ae` | `call` to the body directly after it (`0x7e1495b6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e149d5b` | 2 | `obj_clear_f952_7e149d5b` | `*(this+952) = 0`. | pattern scan |
| `0x7e149da2` | 1 | `entry_thunk_7e149da2` | `call` to the body directly after it (`0x7e149daa`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e149e07` | 2 | `obj_clear_f956_7e149e07` | `*(this+956) = 0`. | pattern scan |
| `0x7e149e4e` | 1 | `entry_thunk_7e149e4e` | `call` to the body directly after it (`0x7e149e56`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e149e72` | 1 | `entry_thunk_7e149e72` | `call` to the body directly after it (`0x7e149e7a`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a0a7` | 2 | `obj_clear_f960_7e14a0a7` | `*(this+960) = 0`. | pattern scan |
| `0x7e14a0ee` | 1 | `entry_thunk_7e14a0ee` | `call` to the body directly after it (`0x7e14a0f6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a120` | 2 | `obj_clear_f964_7e14a120` | `*(this+964) = 0`. | pattern scan |
| `0x7e14a167` | 1 | `entry_thunk_7e14a167` | `call` to the body directly after it (`0x7e14a16f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a199` | 2 | `obj_clear_f968_7e14a199` | `*(this+968) = 0`. | pattern scan |
| `0x7e14a1e0` | 1 | `entry_thunk_7e14a1e0` | `call` to the body directly after it (`0x7e14a1e8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a212` | 2 | `obj_clear_f972_7e14a212` | `*(this+972) = 0`. | pattern scan |
| `0x7e14a259` | 1 | `entry_thunk_7e14a259` | `call` to the body directly after it (`0x7e14a261`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a28b` | 2 | `obj_clear_f976_7e14a28b` | `*(this+976) = 0`. | pattern scan |
| `0x7e14a2d2` | 1 | `entry_thunk_7e14a2d2` | `call` to the body directly after it (`0x7e14a2da`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a304` | 2 | `obj_clear_f980_7e14a304` | `*(this+980) = 0`. | pattern scan |
| `0x7e14a34b` | 1 | `entry_thunk_7e14a34b` | `call` to the body directly after it (`0x7e14a353`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a37d` | 2 | `obj_clear_f984_7e14a37d` | `*(this+984) = 0`. | pattern scan |
| `0x7e14a3c4` | 1 | `entry_thunk_7e14a3c4` | `call` to the body directly after it (`0x7e14a3cc`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a3f6` | 2 | `obj_clear_f988_7e14a3f6` | `*(this+988) = 0`. | pattern scan |
| `0x7e14a43d` | 1 | `entry_thunk_7e14a43d` | `call` to the body directly after it (`0x7e14a445`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a46f` | 2 | `obj_clear_f992_7e14a46f` | `*(this+992) = 0`. | pattern scan |
| `0x7e14a4b6` | 1 | `entry_thunk_7e14a4b6` | `call` to the body directly after it (`0x7e14a4be`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a4e8` | 2 | `obj_clear_f996_7e14a4e8` | `*(this+996) = 0`. | pattern scan |
| `0x7e14a52f` | 1 | `entry_thunk_7e14a52f` | `call` to the body directly after it (`0x7e14a537`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a561` | 2 | `obj_clear_f1000_7e14a561` | `*(this+1000) = 0`. | pattern scan |
| `0x7e14a5a8` | 1 | `entry_thunk_7e14a5a8` | `call` to the body directly after it (`0x7e14a5b0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a6ac` | 2 | `obj_clear_f1004_7e14a6ac` | `*(this+1004) = 0`. | pattern scan |
| `0x7e14a6f3` | 1 | `entry_thunk_7e14a6f3` | `call` to the body directly after it (`0x7e14a6fb`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a725` | 2 | `obj_clear_f1008_7e14a725` | `*(this+1008) = 0`. | pattern scan |
| `0x7e14a76c` | 1 | `entry_thunk_7e14a76c` | `call` to the body directly after it (`0x7e14a774`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a7f3` | 1 | `entry_thunk_7e14a7f3` | `call` to the body directly after it (`0x7e14a7fb`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a825` | 2 | `obj_clear_f1016_7e14a825` | `*(this+1016) = 0`. | pattern scan |
| `0x7e14a86c` | 1 | `entry_thunk_7e14a86c` | `call` to the body directly after it (`0x7e14a874`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a89e` | 2 | `obj_clear_f1020_7e14a89e` | `*(this+1020) = 0`. | pattern scan |
| `0x7e14a8e5` | 1 | `entry_thunk_7e14a8e5` | `call` to the body directly after it (`0x7e14a8ed`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a909` | 1 | `entry_thunk_7e14a909` | `call` to the body directly after it (`0x7e14a911`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14a97c` | 2 | `obj_clear_f1048_7e14a97c` | `*(this+1048) = 0`. | pattern scan |
| `0x7e14a9c3` | 1 | `entry_thunk_7e14a9c3` | `call` to the body directly after it (`0x7e14a9cb`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14aadf` | 2 | `obj_clear_f1052_7e14aadf` | `*(this+1052) = 0`. | pattern scan |
| `0x7e14ab26` | 1 | `entry_thunk_7e14ab26` | `call` to the body directly after it (`0x7e14ab2e`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14ae1f` | 2 | `obj_clear_f1056_7e14ae1f` | `*(this+1056) = 0`. | pattern scan |
| `0x7e14ae66` | 1 | `entry_thunk_7e14ae66` | `call` to the body directly after it (`0x7e14ae6e`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14c3fa` | 2 | `obj_set1_f252_7e14c3fa` | `*(this+252) = 1`. | pattern scan |
| `0x7e14c403` | 1 | `obj_clear_f552_7e14c403` | `*(this+552) = 0`. | pattern scan |
| `0x7e14c447` | 1 | `entry_thunk_7e14c447` | `call` to the body directly after it (`0x7e14c44f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14c46b` | 2 | `entry_thunk_7e14c46b` | `call` to the body directly after it (`0x7e14c473`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14c5a5` | 2 | `entry_thunk_7e14c5a5` | `call` to the body directly after it (`0x7e14c5ad`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14c6b8` | 1 | `entry_thunk_7e14c6b8` | `call` to the body directly after it (`0x7e14c6c0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14c715` | 1 | `entry_thunk_7e14c715` | `call` to the body directly after it (`0x7e14c71d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14c76a` | 1 | `entry_thunk_7e14c76a` | `call` to the body directly after it (`0x7e14c772`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14c78e` | 3 | `entry_thunk_7e14c78e` | `call` to the body directly after it (`0x7e14c796`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14cf2b` | 2 | `obj_clear_f952_7e14cf2b` | `*(this+952) = 0`. | pattern scan |
| `0x7e14cf72` | 1 | `entry_thunk_7e14cf72` | `call` to the body directly after it (`0x7e14cf7a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14cfd7` | 2 | `obj_clear_f1064_7e14cfd7` | `*(this+1064) = 0`. | pattern scan |
| `0x7e14d01e` | 1 | `entry_thunk_7e14d01e` | `call` to the body directly after it (`0x7e14d026`, register-save mask `0xa0`, frame 20) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14d0a8` | 1 | `entry_thunk_7e14d0a8` | `call` to the body directly after it (`0x7e14d0b0`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14d578` | 2 | `obj_clear_f956_7e14d578` | `*(this+956) = 0`. | pattern scan |
| `0x7e14d5bf` | 1 | `entry_thunk_7e14d5bf` | `call` to the body directly after it (`0x7e14d5c7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14d5e3` | 1 | `entry_thunk_7e14d5e3` | `call` to the body directly after it (`0x7e14d5eb`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14d7ec` | 2 | `obj_clear_f960_7e14d7ec` | `*(this+960) = 0`. | pattern scan |
| `0x7e14d833` | 1 | `entry_thunk_7e14d833` | `call` to the body directly after it (`0x7e14d83b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14d865` | 2 | `obj_clear_f964_7e14d865` | `*(this+964) = 0`. | pattern scan |
| `0x7e14d8ac` | 1 | `entry_thunk_7e14d8ac` | `call` to the body directly after it (`0x7e14d8b4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14d8de` | 2 | `obj_clear_f968_7e14d8de` | `*(this+968) = 0`. | pattern scan |
| `0x7e14d925` | 1 | `entry_thunk_7e14d925` | `call` to the body directly after it (`0x7e14d92d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14d957` | 2 | `obj_clear_f972_7e14d957` | `*(this+972) = 0`. | pattern scan |
| `0x7e14d99e` | 1 | `entry_thunk_7e14d99e` | `call` to the body directly after it (`0x7e14d9a6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14d9d0` | 2 | `obj_clear_f976_7e14d9d0` | `*(this+976) = 0`. | pattern scan |
| `0x7e14da17` | 1 | `entry_thunk_7e14da17` | `call` to the body directly after it (`0x7e14da1f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14da49` | 2 | `obj_clear_f980_7e14da49` | `*(this+980) = 0`. | pattern scan |
| `0x7e14da90` | 1 | `entry_thunk_7e14da90` | `call` to the body directly after it (`0x7e14da98`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14dac2` | 2 | `obj_clear_f984_7e14dac2` | `*(this+984) = 0`. | pattern scan |
| `0x7e14db09` | 1 | `entry_thunk_7e14db09` | `call` to the body directly after it (`0x7e14db11`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14db3b` | 2 | `obj_clear_f988_7e14db3b` | `*(this+988) = 0`. | pattern scan |
| `0x7e14db82` | 1 | `entry_thunk_7e14db82` | `call` to the body directly after it (`0x7e14db8a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14dbb4` | 2 | `obj_clear_f992_7e14dbb4` | `*(this+992) = 0`. | pattern scan |
| `0x7e14dbfb` | 1 | `entry_thunk_7e14dbfb` | `call` to the body directly after it (`0x7e14dc03`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14dc2d` | 2 | `obj_clear_f996_7e14dc2d` | `*(this+996) = 0`. | pattern scan |
| `0x7e14dc74` | 1 | `entry_thunk_7e14dc74` | `call` to the body directly after it (`0x7e14dc7c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14dca6` | 2 | `obj_clear_f1000_7e14dca6` | `*(this+1000) = 0`. | pattern scan |
| `0x7e14dced` | 1 | `entry_thunk_7e14dced` | `call` to the body directly after it (`0x7e14dcf5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14ddf1` | 2 | `obj_clear_f1004_7e14ddf1` | `*(this+1004) = 0`. | pattern scan |
| `0x7e14de38` | 1 | `entry_thunk_7e14de38` | `call` to the body directly after it (`0x7e14de40`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14de6a` | 2 | `obj_clear_f1008_7e14de6a` | `*(this+1008) = 0`. | pattern scan |
| `0x7e14deb1` | 1 | `entry_thunk_7e14deb1` | `call` to the body directly after it (`0x7e14deb9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14df38` | 1 | `entry_thunk_7e14df38` | `call` to the body directly after it (`0x7e14df40`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14df6a` | 2 | `obj_clear_f1016_7e14df6a` | `*(this+1016) = 0`. | pattern scan |
| `0x7e14dfb1` | 1 | `entry_thunk_7e14dfb1` | `call` to the body directly after it (`0x7e14dfb9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14dfe3` | 2 | `obj_clear_f1020_7e14dfe3` | `*(this+1020) = 0`. | pattern scan |
| `0x7e14e02a` | 1 | `entry_thunk_7e14e02a` | `call` to the body directly after it (`0x7e14e032`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14e04e` | 1 | `entry_thunk_7e14e04e` | `call` to the body directly after it (`0x7e14e056`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14eabd` | 2 | `obj_set1_f252_7e14eabd` | `*(this+252) = 1`. | pattern scan |
| `0x7e14eac6` | 1 | `obj_clear_f552_7e14eac6` | `*(this+552) = 0`. | pattern scan |
| `0x7e14eb0a` | 1 | `entry_thunk_7e14eb0a` | `call` to the body directly after it (`0x7e14eb12`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14eb2e` | 2 | `entry_thunk_7e14eb2e` | `call` to the body directly after it (`0x7e14eb36`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14ec68` | 2 | `entry_thunk_7e14ec68` | `call` to the body directly after it (`0x7e14ec70`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14ed7b` | 1 | `entry_thunk_7e14ed7b` | `call` to the body directly after it (`0x7e14ed83`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14edd8` | 1 | `entry_thunk_7e14edd8` | `call` to the body directly after it (`0x7e14ede0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14ee2d` | 1 | `entry_thunk_7e14ee2d` | `call` to the body directly after it (`0x7e14ee35`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14ee51` | 3 | `entry_thunk_7e14ee51` | `call` to the body directly after it (`0x7e14ee59`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14f625` | 2 | `obj_clear_f952_7e14f625` | `*(this+952) = 0`. | pattern scan |
| `0x7e14f66c` | 1 | `entry_thunk_7e14f66c` | `call` to the body directly after it (`0x7e14f674`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14f6d1` | 2 | `obj_clear_f1252_7e14f6d1` | `*(this+1252) = 0`. | pattern scan |
| `0x7e14f718` | 1 | `entry_thunk_7e14f718` | `call` to the body directly after it (`0x7e14f720`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14f7f4` | 2 | `obj_clear_f956_7e14f7f4` | `*(this+956) = 0`. | pattern scan |
| `0x7e14f83b` | 1 | `entry_thunk_7e14f83b` | `call` to the body directly after it (`0x7e14f843`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14f86d` | 2 | `obj_clear_f1256_7e14f86d` | `*(this+1256) = 0`. | pattern scan |
| `0x7e14f8b4` | 1 | `entry_thunk_7e14f8b4` | `call` to the body directly after it (`0x7e14f8bc`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14fb59` | 1 | `entry_thunk_7e14fb59` | `call` to the body directly after it (`0x7e14fb61`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e14fdfc` | 2 | `obj_clear_f1260_7e14fdfc` | `*(this+1260) = 0`. | pattern scan |
| `0x7e14fe43` | 1 | `entry_thunk_7e14fe43` | `call` to the body directly after it (`0x7e14fe4b`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e150025` | 2 | `obj_clear_f960_7e150025` | `*(this+960) = 0`. | pattern scan |
| `0x7e15006c` | 1 | `entry_thunk_7e15006c` | `call` to the body directly after it (`0x7e150074`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15009e` | 2 | `obj_clear_f964_7e15009e` | `*(this+964) = 0`. | pattern scan |
| `0x7e1500e5` | 1 | `entry_thunk_7e1500e5` | `call` to the body directly after it (`0x7e1500ed`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e150117` | 2 | `obj_clear_f968_7e150117` | `*(this+968) = 0`. | pattern scan |
| `0x7e15015e` | 1 | `entry_thunk_7e15015e` | `call` to the body directly after it (`0x7e150166`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e150190` | 2 | `obj_clear_f972_7e150190` | `*(this+972) = 0`. | pattern scan |
| `0x7e1501d7` | 1 | `entry_thunk_7e1501d7` | `call` to the body directly after it (`0x7e1501df`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e150209` | 2 | `obj_clear_f976_7e150209` | `*(this+976) = 0`. | pattern scan |
| `0x7e150250` | 1 | `entry_thunk_7e150250` | `call` to the body directly after it (`0x7e150258`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e150282` | 2 | `obj_clear_f980_7e150282` | `*(this+980) = 0`. | pattern scan |
| `0x7e1502c9` | 1 | `entry_thunk_7e1502c9` | `call` to the body directly after it (`0x7e1502d1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1502fb` | 2 | `obj_clear_f984_7e1502fb` | `*(this+984) = 0`. | pattern scan |
| `0x7e150342` | 1 | `entry_thunk_7e150342` | `call` to the body directly after it (`0x7e15034a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e150374` | 2 | `obj_clear_f988_7e150374` | `*(this+988) = 0`. | pattern scan |
| `0x7e1503bb` | 1 | `entry_thunk_7e1503bb` | `call` to the body directly after it (`0x7e1503c3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1503ed` | 2 | `obj_clear_f992_7e1503ed` | `*(this+992) = 0`. | pattern scan |
| `0x7e150434` | 1 | `entry_thunk_7e150434` | `call` to the body directly after it (`0x7e15043c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e150466` | 2 | `obj_clear_f996_7e150466` | `*(this+996) = 0`. | pattern scan |
| `0x7e1504ad` | 1 | `entry_thunk_7e1504ad` | `call` to the body directly after it (`0x7e1504b5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1504df` | 2 | `obj_clear_f1264_7e1504df` | `*(this+1264) = 0`. | pattern scan |
| `0x7e150526` | 1 | `entry_thunk_7e150526` | `call` to the body directly after it (`0x7e15052e`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1508d1` | 2 | `obj_clear_f1000_7e1508d1` | `*(this+1000) = 0`. | pattern scan |
| `0x7e150918` | 1 | `entry_thunk_7e150918` | `call` to the body directly after it (`0x7e150920`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e150a1c` | 2 | `obj_clear_f1004_7e150a1c` | `*(this+1004) = 0`. | pattern scan |
| `0x7e150a63` | 1 | `entry_thunk_7e150a63` | `call` to the body directly after it (`0x7e150a6b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e150a95` | 2 | `obj_clear_f1268_7e150a95` | `*(this+1268) = 0`. | pattern scan |
| `0x7e150adc` | 1 | `entry_thunk_7e150adc` | `call` to the body directly after it (`0x7e150ae4`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e150bd0` | 2 | `obj_clear_f1008_7e150bd0` | `*(this+1008) = 0`. | pattern scan |
| `0x7e150c17` | 1 | `entry_thunk_7e150c17` | `call` to the body directly after it (`0x7e150c1f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e150c9e` | 1 | `entry_thunk_7e150c9e` | `call` to the body directly after it (`0x7e150ca6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e150cd0` | 2 | `obj_clear_f1272_7e150cd0` | `*(this+1272) = 0`. | pattern scan |
| `0x7e150d17` | 1 | `entry_thunk_7e150d17` | `call` to the body directly after it (`0x7e150d1f`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e150e45` | 2 | `obj_clear_f1016_7e150e45` | `*(this+1016) = 0`. | pattern scan |
| `0x7e150e8c` | 1 | `entry_thunk_7e150e8c` | `call` to the body directly after it (`0x7e150e94`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e150ebe` | 2 | `obj_clear_f1020_7e150ebe` | `*(this+1020) = 0`. | pattern scan |
| `0x7e150f05` | 1 | `entry_thunk_7e150f05` | `call` to the body directly after it (`0x7e150f0d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e150f37` | 2 | `obj_clear_f1276_7e150f37` | `*(this+1276) = 0`. | pattern scan |
| `0x7e150f7e` | 1 | `entry_thunk_7e150f7e` | `call` to the body directly after it (`0x7e150f86`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1511e3` | 1 | `entry_thunk_7e1511e3` | `call` to the body directly after it (`0x7e1511eb`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e151256` | 2 | `obj_clear_f1280_7e151256` | `*(this+1280) = 0`. | pattern scan |
| `0x7e15129d` | 1 | `entry_thunk_7e15129d` | `call` to the body directly after it (`0x7e1512a5`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1525db` | 2 | `obj_set1_f252_7e1525db` | `*(this+252) = 1`. | pattern scan |
| `0x7e1525e4` | 1 | `obj_clear_f552_7e1525e4` | `*(this+552) = 0`. | pattern scan |
| `0x7e152628` | 1 | `entry_thunk_7e152628` | `call` to the body directly after it (`0x7e152630`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15264c` | 2 | `entry_thunk_7e15264c` | `call` to the body directly after it (`0x7e152654`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e152786` | 2 | `entry_thunk_7e152786` | `call` to the body directly after it (`0x7e15278e`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e152899` | 1 | `entry_thunk_7e152899` | `call` to the body directly after it (`0x7e1528a1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1528f6` | 1 | `entry_thunk_7e1528f6` | `call` to the body directly after it (`0x7e1528fe`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15294b` | 1 | `entry_thunk_7e15294b` | `call` to the body directly after it (`0x7e152953`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15296f` | 3 | `entry_thunk_7e15296f` | `call` to the body directly after it (`0x7e152977`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1531a4` | 2 | `obj_clear_f952_7e1531a4` | `*(this+952) = 0`. | pattern scan |
| `0x7e1531eb` | 1 | `entry_thunk_7e1531eb` | `call` to the body directly after it (`0x7e1531f3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e153250` | 2 | `obj_clear_f1252_7e153250` | `*(this+1252) = 0`. | pattern scan |
| `0x7e153297` | 1 | `entry_thunk_7e153297` | `call` to the body directly after it (`0x7e15329f`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e153368` | 2 | `obj_clear_f1256_7e153368` | `*(this+1256) = 0`. | pattern scan |
| `0x7e1533af` | 1 | `entry_thunk_7e1533af` | `call` to the body directly after it (`0x7e1533b7`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e153636` | 2 | `obj_clear_f1260_7e153636` | `*(this+1260) = 0`. | pattern scan |
| `0x7e15367d` | 1 | `entry_thunk_7e15367d` | `call` to the body directly after it (`0x7e153685`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e153760` | 2 | `obj_clear_f1264_7e153760` | `*(this+1264) = 0`. | pattern scan |
| `0x7e1537a7` | 1 | `entry_thunk_7e1537a7` | `call` to the body directly after it (`0x7e1537af`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15396d` | 2 | `obj_clear_f1268_7e15396d` | `*(this+1268) = 0`. | pattern scan |
| `0x7e1539b4` | 1 | `entry_thunk_7e1539b4` | `call` to the body directly after it (`0x7e1539bc`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e153a70` | 2 | `obj_clear_f956_7e153a70` | `*(this+956) = 0`. | pattern scan |
| `0x7e153ab7` | 1 | `entry_thunk_7e153ab7` | `call` to the body directly after it (`0x7e153abf`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e153ae9` | 2 | `obj_clear_f1272_7e153ae9` | `*(this+1272) = 0`. | pattern scan |
| `0x7e153b30` | 1 | `entry_thunk_7e153b30` | `call` to the body directly after it (`0x7e153b38`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e153cc2` | 2 | `obj_clear_f1276_7e153cc2` | `*(this+1276) = 0`. | pattern scan |
| `0x7e153d09` | 1 | `entry_thunk_7e153d09` | `call` to the body directly after it (`0x7e153d11`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e153f7f` | 2 | `obj_clear_f1280_7e153f7f` | `*(this+1280) = 0`. | pattern scan |
| `0x7e153fc6` | 1 | `entry_thunk_7e153fc6` | `call` to the body directly after it (`0x7e153fce`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1541e2` | 1 | `entry_thunk_7e1541e2` | `call` to the body directly after it (`0x7e1541ea`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15458d` | 2 | `obj_clear_f1284_7e15458d` | `*(this+1284) = 0`. | pattern scan |
| `0x7e1545d4` | 1 | `entry_thunk_7e1545d4` | `call` to the body directly after it (`0x7e1545dc`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1546be` | 2 | `obj_clear_f1288_7e1546be` | `*(this+1288) = 0`. | pattern scan |
| `0x7e154705` | 1 | `entry_thunk_7e154705` | `call` to the body directly after it (`0x7e15470d`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1548b8` | 2 | `obj_clear_f960_7e1548b8` | `*(this+960) = 0`. | pattern scan |
| `0x7e1548ff` | 1 | `entry_thunk_7e1548ff` | `call` to the body directly after it (`0x7e154907`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e154931` | 2 | `obj_clear_f964_7e154931` | `*(this+964) = 0`. | pattern scan |
| `0x7e154978` | 1 | `entry_thunk_7e154978` | `call` to the body directly after it (`0x7e154980`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1549aa` | 2 | `obj_clear_f968_7e1549aa` | `*(this+968) = 0`. | pattern scan |
| `0x7e1549f1` | 1 | `entry_thunk_7e1549f1` | `call` to the body directly after it (`0x7e1549f9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e154a23` | 2 | `obj_clear_f1292_7e154a23` | `*(this+1292) = 0`. | pattern scan |
| `0x7e154a6a` | 1 | `entry_thunk_7e154a6a` | `call` to the body directly after it (`0x7e154a72`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e154b28` | 2 | `obj_clear_f972_7e154b28` | `*(this+972) = 0`. | pattern scan |
| `0x7e154b6f` | 1 | `entry_thunk_7e154b6f` | `call` to the body directly after it (`0x7e154b77`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e154ba1` | 2 | `obj_clear_f976_7e154ba1` | `*(this+976) = 0`. | pattern scan |
| `0x7e154be8` | 1 | `entry_thunk_7e154be8` | `call` to the body directly after it (`0x7e154bf0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e154c1a` | 2 | `obj_clear_f1296_7e154c1a` | `*(this+1296) = 0`. | pattern scan |
| `0x7e154c61` | 1 | `entry_thunk_7e154c61` | `call` to the body directly after it (`0x7e154c69`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e154d30` | 2 | `obj_clear_f980_7e154d30` | `*(this+980) = 0`. | pattern scan |
| `0x7e154d77` | 1 | `entry_thunk_7e154d77` | `call` to the body directly after it (`0x7e154d7f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e154da9` | 2 | `obj_clear_f984_7e154da9` | `*(this+984) = 0`. | pattern scan |
| `0x7e154df0` | 1 | `entry_thunk_7e154df0` | `call` to the body directly after it (`0x7e154df8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e154e22` | 2 | `obj_clear_f988_7e154e22` | `*(this+988) = 0`. | pattern scan |
| `0x7e154e69` | 1 | `entry_thunk_7e154e69` | `call` to the body directly after it (`0x7e154e71`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e154e9b` | 2 | `obj_clear_f992_7e154e9b` | `*(this+992) = 0`. | pattern scan |
| `0x7e154ee2` | 1 | `entry_thunk_7e154ee2` | `call` to the body directly after it (`0x7e154eea`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e154f14` | 2 | `obj_clear_f996_7e154f14` | `*(this+996) = 0`. | pattern scan |
| `0x7e154f5b` | 1 | `entry_thunk_7e154f5b` | `call` to the body directly after it (`0x7e154f63`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e154f8d` | 2 | `obj_clear_f1300_7e154f8d` | `*(this+1300) = 0`. | pattern scan |
| `0x7e154fd4` | 1 | `entry_thunk_7e154fd4` | `call` to the body directly after it (`0x7e154fdc`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e155185` | 2 | `obj_clear_f1304_7e155185` | `*(this+1304) = 0`. | pattern scan |
| `0x7e1551cc` | 1 | `entry_thunk_7e1551cc` | `call` to the body directly after it (`0x7e1551d4`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15529b` | 2 | `obj_clear_f1308_7e15529b` | `*(this+1308) = 0`. | pattern scan |
| `0x7e1552e2` | 1 | `entry_thunk_7e1552e2` | `call` to the body directly after it (`0x7e1552ea`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1554b3` | 2 | `obj_clear_f1000_7e1554b3` | `*(this+1000) = 0`. | pattern scan |
| `0x7e1554fa` | 1 | `entry_thunk_7e1554fa` | `call` to the body directly after it (`0x7e155502`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1555fe` | 2 | `obj_clear_f1004_7e1555fe` | `*(this+1004) = 0`. | pattern scan |
| `0x7e155645` | 1 | `entry_thunk_7e155645` | `call` to the body directly after it (`0x7e15564d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e155677` | 2 | `obj_clear_f1312_7e155677` | `*(this+1312) = 0`. | pattern scan |
| `0x7e1556be` | 1 | `entry_thunk_7e1556be` | `call` to the body directly after it (`0x7e1556c6`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e155789` | 2 | `obj_clear_f1008_7e155789` | `*(this+1008) = 0`. | pattern scan |
| `0x7e1557d0` | 1 | `entry_thunk_7e1557d0` | `call` to the body directly after it (`0x7e1557d8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e155857` | 1 | `entry_thunk_7e155857` | `call` to the body directly after it (`0x7e15585f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e155889` | 2 | `obj_clear_f1016_7e155889` | `*(this+1016) = 0`. | pattern scan |
| `0x7e1558d0` | 1 | `entry_thunk_7e1558d0` | `call` to the body directly after it (`0x7e1558d8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e155902` | 2 | `obj_clear_f1020_7e155902` | `*(this+1020) = 0`. | pattern scan |
| `0x7e155949` | 1 | `entry_thunk_7e155949` | `call` to the body directly after it (`0x7e155951`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15597b` | 2 | `obj_clear_f1316_7e15597b` | `*(this+1316) = 0`. | pattern scan |
| `0x7e1559c2` | 1 | `entry_thunk_7e1559c2` | `call` to the body directly after it (`0x7e1559ca`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e155aa2` | 2 | `obj_clear_f1320_7e155aa2` | `*(this+1320) = 0`. | pattern scan |
| `0x7e155ae9` | 1 | `entry_thunk_7e155ae9` | `call` to the body directly after it (`0x7e155af1`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e155da4` | 1 | `entry_thunk_7e155da4` | `call` to the body directly after it (`0x7e155dac`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e155e17` | 2 | `obj_clear_f1324_7e155e17` | `*(this+1324) = 0`. | pattern scan |
| `0x7e155e5e` | 1 | `entry_thunk_7e155e5e` | `call` to the body directly after it (`0x7e155e66`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e155f8b` | 2 | `obj_clear_f1328_7e155f8b` | `*(this+1328) = 0`. | pattern scan |
| `0x7e155fd2` | 1 | `entry_thunk_7e155fd2` | `call` to the body directly after it (`0x7e155fda`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e156dc6` | 2 | `obj_set1_f252_7e156dc6` | `*(this+252) = 1`. | pattern scan |
| `0x7e156dcf` | 1 | `obj_clear_f552_7e156dcf` | `*(this+552) = 0`. | pattern scan |
| `0x7e156e13` | 1 | `entry_thunk_7e156e13` | `call` to the body directly after it (`0x7e156e1b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e156e37` | 2 | `entry_thunk_7e156e37` | `call` to the body directly after it (`0x7e156e3f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e156f71` | 2 | `entry_thunk_7e156f71` | `call` to the body directly after it (`0x7e156f79`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e157084` | 1 | `entry_thunk_7e157084` | `call` to the body directly after it (`0x7e15708c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1570e1` | 1 | `entry_thunk_7e1570e1` | `call` to the body directly after it (`0x7e1570e9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e157136` | 1 | `entry_thunk_7e157136` | `call` to the body directly after it (`0x7e15713e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15715a` | 3 | `entry_thunk_7e15715a` | `call` to the body directly after it (`0x7e157162`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e157957` | 2 | `obj_clear_f952_7e157957` | `*(this+952) = 0`. | pattern scan |
| `0x7e15799e` | 1 | `entry_thunk_7e15799e` | `call` to the body directly after it (`0x7e1579a6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e157a03` | 2 | `obj_clear_f1268_7e157a03` | `*(this+1268) = 0`. | pattern scan |
| `0x7e157a4a` | 1 | `entry_thunk_7e157a4a` | `call` to the body directly after it (`0x7e157a52`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e157b4f` | 2 | `obj_clear_f1272_7e157b4f` | `*(this+1272) = 0`. | pattern scan |
| `0x7e157b96` | 1 | `entry_thunk_7e157b96` | `call` to the body directly after it (`0x7e157b9e`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e157ca6` | 2 | `obj_clear_f1276_7e157ca6` | `*(this+1276) = 0`. | pattern scan |
| `0x7e157ced` | 1 | `entry_thunk_7e157ced` | `call` to the body directly after it (`0x7e157cf5`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e157dd9` | 2 | `obj_clear_f956_7e157dd9` | `*(this+956) = 0`. | pattern scan |
| `0x7e157e20` | 1 | `entry_thunk_7e157e20` | `call` to the body directly after it (`0x7e157e28`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e157e52` | 2 | `obj_clear_f1280_7e157e52` | `*(this+1280) = 0`. | pattern scan |
| `0x7e157e99` | 1 | `entry_thunk_7e157e99` | `call` to the body directly after it (`0x7e157ea1`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e158190` | 1 | `entry_thunk_7e158190` | `call` to the body directly after it (`0x7e158198`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1584a1` | 2 | `obj_clear_f1284_7e1584a1` | `*(this+1284) = 0`. | pattern scan |
| `0x7e1584e8` | 1 | `entry_thunk_7e1584e8` | `call` to the body directly after it (`0x7e1584f0`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e158621` | 2 | `obj_clear_f1288_7e158621` | `*(this+1288) = 0`. | pattern scan |
| `0x7e158668` | 1 | `entry_thunk_7e158668` | `call` to the body directly after it (`0x7e158670`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e158bcb` | 2 | `obj_clear_f1292_7e158bcb` | `*(this+1292) = 0`. | pattern scan |
| `0x7e158c12` | 1 | `entry_thunk_7e158c12` | `call` to the body directly after it (`0x7e158c1a`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e158f60` | 2 | `obj_clear_f960_7e158f60` | `*(this+960) = 0`. | pattern scan |
| `0x7e158fa7` | 1 | `entry_thunk_7e158fa7` | `call` to the body directly after it (`0x7e158faf`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e158fd9` | 2 | `obj_clear_f964_7e158fd9` | `*(this+964) = 0`. | pattern scan |
| `0x7e159020` | 1 | `entry_thunk_7e159020` | `call` to the body directly after it (`0x7e159028`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e159052` | 2 | `obj_clear_f968_7e159052` | `*(this+968) = 0`. | pattern scan |
| `0x7e159099` | 1 | `entry_thunk_7e159099` | `call` to the body directly after it (`0x7e1590a1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1590cb` | 2 | `obj_clear_f1296_7e1590cb` | `*(this+1296) = 0`. | pattern scan |
| `0x7e159112` | 1 | `entry_thunk_7e159112` | `call` to the body directly after it (`0x7e15911a`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e159209` | 2 | `obj_clear_f972_7e159209` | `*(this+972) = 0`. | pattern scan |
| `0x7e159250` | 1 | `entry_thunk_7e159250` | `call` to the body directly after it (`0x7e159258`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e159282` | 2 | `obj_clear_f976_7e159282` | `*(this+976) = 0`. | pattern scan |
| `0x7e1592c9` | 1 | `entry_thunk_7e1592c9` | `call` to the body directly after it (`0x7e1592d1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1592fb` | 2 | `obj_clear_f1300_7e1592fb` | `*(this+1300) = 0`. | pattern scan |
| `0x7e159342` | 1 | `entry_thunk_7e159342` | `call` to the body directly after it (`0x7e15934a`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e159445` | 2 | `obj_clear_f980_7e159445` | `*(this+980) = 0`. | pattern scan |
| `0x7e15948c` | 1 | `entry_thunk_7e15948c` | `call` to the body directly after it (`0x7e159494`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1594be` | 2 | `obj_clear_f984_7e1594be` | `*(this+984) = 0`. | pattern scan |
| `0x7e159505` | 1 | `entry_thunk_7e159505` | `call` to the body directly after it (`0x7e15950d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e159537` | 2 | `obj_clear_f988_7e159537` | `*(this+988) = 0`. | pattern scan |
| `0x7e15957e` | 1 | `entry_thunk_7e15957e` | `call` to the body directly after it (`0x7e159586`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1595b0` | 2 | `obj_clear_f992_7e1595b0` | `*(this+992) = 0`. | pattern scan |
| `0x7e1595f7` | 1 | `entry_thunk_7e1595f7` | `call` to the body directly after it (`0x7e1595ff`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e159629` | 2 | `obj_clear_f996_7e159629` | `*(this+996) = 0`. | pattern scan |
| `0x7e159670` | 1 | `entry_thunk_7e159670` | `call` to the body directly after it (`0x7e159678`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1596a2` | 2 | `obj_clear_f1304_7e1596a2` | `*(this+1304) = 0`. | pattern scan |
| `0x7e1596e9` | 1 | `entry_thunk_7e1596e9` | `call` to the body directly after it (`0x7e1596f1`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1597ec` | 2 | `obj_clear_f1000_7e1597ec` | `*(this+1000) = 0`. | pattern scan |
| `0x7e159833` | 1 | `entry_thunk_7e159833` | `call` to the body directly after it (`0x7e15983b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e159937` | 2 | `obj_clear_f1004_7e159937` | `*(this+1004) = 0`. | pattern scan |
| `0x7e15997e` | 1 | `entry_thunk_7e15997e` | `call` to the body directly after it (`0x7e159986`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1599b7` | 2 | `obj_clear_f1308_7e1599b7` | `*(this+1308) = 0`. | pattern scan |
| `0x7e1599fe` | 1 | `entry_thunk_7e1599fe` | `call` to the body directly after it (`0x7e159a06`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e159c09` | 2 | `obj_clear_f1008_7e159c09` | `*(this+1008) = 0`. | pattern scan |
| `0x7e159c50` | 1 | `entry_thunk_7e159c50` | `call` to the body directly after it (`0x7e159c58`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e159cd7` | 1 | `entry_thunk_7e159cd7` | `call` to the body directly after it (`0x7e159cdf`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e159d09` | 2 | `obj_clear_f1312_7e159d09` | `*(this+1312) = 0`. | pattern scan |
| `0x7e159d50` | 1 | `entry_thunk_7e159d50` | `call` to the body directly after it (`0x7e159d58`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e159f5b` | 2 | `obj_clear_f1016_7e159f5b` | `*(this+1016) = 0`. | pattern scan |
| `0x7e159fa2` | 1 | `entry_thunk_7e159fa2` | `call` to the body directly after it (`0x7e159faa`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e159fd4` | 2 | `obj_clear_f1020_7e159fd4` | `*(this+1020) = 0`. | pattern scan |
| `0x7e15a01b` | 1 | `entry_thunk_7e15a01b` | `call` to the body directly after it (`0x7e15a023`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15a04d` | 2 | `obj_clear_f1316_7e15a04d` | `*(this+1316) = 0`. | pattern scan |
| `0x7e15a094` | 1 | `entry_thunk_7e15a094` | `call` to the body directly after it (`0x7e15a09c`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15a29a` | 1 | `entry_thunk_7e15a29a` | `call` to the body directly after it (`0x7e15a2a2`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15b6a4` | 2 | `obj_set1_f252_7e15b6a4` | `*(this+252) = 1`. | pattern scan |
| `0x7e15b6ad` | 1 | `obj_clear_f552_7e15b6ad` | `*(this+552) = 0`. | pattern scan |
| `0x7e15b6f1` | 1 | `entry_thunk_7e15b6f1` | `call` to the body directly after it (`0x7e15b6f9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15b715` | 2 | `entry_thunk_7e15b715` | `call` to the body directly after it (`0x7e15b71d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15b84f` | 2 | `entry_thunk_7e15b84f` | `call` to the body directly after it (`0x7e15b857`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15b962` | 1 | `entry_thunk_7e15b962` | `call` to the body directly after it (`0x7e15b96a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15b9bf` | 1 | `entry_thunk_7e15b9bf` | `call` to the body directly after it (`0x7e15b9c7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15ba14` | 1 | `entry_thunk_7e15ba14` | `call` to the body directly after it (`0x7e15ba1c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15ba38` | 3 | `entry_thunk_7e15ba38` | `call` to the body directly after it (`0x7e15ba40`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15c23c` | 2 | `obj_clear_f952_7e15c23c` | `*(this+952) = 0`. | pattern scan |
| `0x7e15c283` | 1 | `entry_thunk_7e15c283` | `call` to the body directly after it (`0x7e15c28b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15c2e8` | 2 | `obj_clear_f1320_7e15c2e8` | `*(this+1320) = 0`. | pattern scan |
| `0x7e15c32f` | 1 | `entry_thunk_7e15c32f` | `call` to the body directly after it (`0x7e15c337`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15c40d` | 2 | `obj_clear_f1324_7e15c40d` | `*(this+1324) = 0`. | pattern scan |
| `0x7e15c454` | 1 | `entry_thunk_7e15c454` | `call` to the body directly after it (`0x7e15c45c`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15c68c` | 2 | `obj_clear_f956_7e15c68c` | `*(this+956) = 0`. | pattern scan |
| `0x7e15c6d3` | 1 | `entry_thunk_7e15c6d3` | `call` to the body directly after it (`0x7e15c6db`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15c705` | 2 | `obj_clear_f1328_7e15c705` | `*(this+1328) = 0`. | pattern scan |
| `0x7e15c74c` | 1 | `entry_thunk_7e15c74c` | `call` to the body directly after it (`0x7e15c754`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15c98d` | 1 | `entry_thunk_7e15c98d` | `call` to the body directly after it (`0x7e15c995`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15cd14` | 1 | `entry_thunk_7e15cd14` | `call` to the body directly after it (`0x7e15cd1c`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15ce3a` | 2 | `obj_clear_f1336_7e15ce3a` | `*(this+1336) = 0`. | pattern scan |
| `0x7e15ce81` | 1 | `entry_thunk_7e15ce81` | `call` to the body directly after it (`0x7e15ce89`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15cff1` | 2 | `obj_clear_f1340_7e15cff1` | `*(this+1340) = 0`. | pattern scan |
| `0x7e15d038` | 1 | `entry_thunk_7e15d038` | `call` to the body directly after it (`0x7e15d040`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15d185` | 2 | `obj_clear_f1344_7e15d185` | `*(this+1344) = 0`. | pattern scan |
| `0x7e15d1d6` | 1 | `entry_thunk_7e15d1d6` | `call` to the body directly after it (`0x7e15d1de`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15d32b` | 1 | `entry_thunk_7e15d32b` | `call` to the body directly after it (`0x7e15d333`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15d4b8` | 2 | `entry_thunk_7e15d4b8` | `call` to the body directly after it (`0x7e15d4c0`, register-save mask `0xb0`, frame 48) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15d5e5` | 1 | `entry_thunk_7e15d5e5` | `call` to the body directly after it (`0x7e15d5ed`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15d771` | 2 | `entry_thunk_7e15d771` | `call` to the body directly after it (`0x7e15d779`, register-save mask `0xb0`, frame 48) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15d8a4` | 1 | `entry_thunk_7e15d8a4` | `call` to the body directly after it (`0x7e15d8ac`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15d9ed` | 1 | `entry_thunk_7e15d9ed` | `call` to the body directly after it (`0x7e15d9f5`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15dc2c` | 2 | `obj_clear_f960_7e15dc2c` | `*(this+960) = 0`. | pattern scan |
| `0x7e15dc73` | 1 | `entry_thunk_7e15dc73` | `call` to the body directly after it (`0x7e15dc7b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15dca5` | 2 | `obj_clear_f964_7e15dca5` | `*(this+964) = 0`. | pattern scan |
| `0x7e15dcec` | 1 | `entry_thunk_7e15dcec` | `call` to the body directly after it (`0x7e15dcf4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15dd1e` | 2 | `obj_clear_f968_7e15dd1e` | `*(this+968) = 0`. | pattern scan |
| `0x7e15dd65` | 1 | `entry_thunk_7e15dd65` | `call` to the body directly after it (`0x7e15dd6d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15dd97` | 2 | `obj_clear_f1348_7e15dd97` | `*(this+1348) = 0`. | pattern scan |
| `0x7e15ddde` | 1 | `entry_thunk_7e15ddde` | `call` to the body directly after it (`0x7e15dde6`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15e05b` | 2 | `obj_clear_f972_7e15e05b` | `*(this+972) = 0`. | pattern scan |
| `0x7e15e0a2` | 1 | `entry_thunk_7e15e0a2` | `call` to the body directly after it (`0x7e15e0aa`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15e0d4` | 2 | `obj_clear_f976_7e15e0d4` | `*(this+976) = 0`. | pattern scan |
| `0x7e15e11b` | 1 | `entry_thunk_7e15e11b` | `call` to the body directly after it (`0x7e15e123`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15e14d` | 2 | `obj_clear_f1352_7e15e14d` | `*(this+1352) = 0`. | pattern scan |
| `0x7e15e194` | 1 | `entry_thunk_7e15e194` | `call` to the body directly after it (`0x7e15e19c`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15e264` | 2 | `obj_clear_f980_7e15e264` | `*(this+980) = 0`. | pattern scan |
| `0x7e15e2ab` | 1 | `entry_thunk_7e15e2ab` | `call` to the body directly after it (`0x7e15e2b3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15e2dd` | 2 | `obj_clear_f984_7e15e2dd` | `*(this+984) = 0`. | pattern scan |
| `0x7e15e324` | 1 | `entry_thunk_7e15e324` | `call` to the body directly after it (`0x7e15e32c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15e356` | 2 | `obj_clear_f1356_7e15e356` | `*(this+1356) = 0`. | pattern scan |
| `0x7e15e39d` | 1 | `entry_thunk_7e15e39d` | `call` to the body directly after it (`0x7e15e3a5`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15e46b` | 2 | `obj_clear_f988_7e15e46b` | `*(this+988) = 0`. | pattern scan |
| `0x7e15e4b2` | 1 | `entry_thunk_7e15e4b2` | `call` to the body directly after it (`0x7e15e4ba`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15e4e4` | 2 | `obj_clear_f992_7e15e4e4` | `*(this+992) = 0`. | pattern scan |
| `0x7e15e52b` | 1 | `entry_thunk_7e15e52b` | `call` to the body directly after it (`0x7e15e533`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15e55d` | 2 | `obj_clear_f996_7e15e55d` | `*(this+996) = 0`. | pattern scan |
| `0x7e15e5a4` | 1 | `entry_thunk_7e15e5a4` | `call` to the body directly after it (`0x7e15e5ac`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15e5d6` | 2 | `obj_clear_f1360_7e15e5d6` | `*(this+1360) = 0`. | pattern scan |
| `0x7e15e61d` | 1 | `entry_thunk_7e15e61d` | `call` to the body directly after it (`0x7e15e625`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15e6ed` | 2 | `obj_clear_f1000_7e15e6ed` | `*(this+1000) = 0`. | pattern scan |
| `0x7e15e734` | 1 | `entry_thunk_7e15e734` | `call` to the body directly after it (`0x7e15e73c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15e838` | 2 | `obj_clear_f1004_7e15e838` | `*(this+1004) = 0`. | pattern scan |
| `0x7e15e87f` | 1 | `entry_thunk_7e15e87f` | `call` to the body directly after it (`0x7e15e887`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15e8b1` | 2 | `obj_clear_f1008_7e15e8b1` | `*(this+1008) = 0`. | pattern scan |
| `0x7e15e8f8` | 1 | `entry_thunk_7e15e8f8` | `call` to the body directly after it (`0x7e15e900`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15e97f` | 1 | `entry_thunk_7e15e97f` | `call` to the body directly after it (`0x7e15e987`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15e9b1` | 2 | `obj_clear_f1016_7e15e9b1` | `*(this+1016) = 0`. | pattern scan |
| `0x7e15e9f8` | 1 | `entry_thunk_7e15e9f8` | `call` to the body directly after it (`0x7e15ea00`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15ea2a` | 2 | `obj_clear_f1020_7e15ea2a` | `*(this+1020) = 0`. | pattern scan |
| `0x7e15ea71` | 1 | `entry_thunk_7e15ea71` | `call` to the body directly after it (`0x7e15ea79`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15eaa3` | 2 | `obj_clear_f1364_7e15eaa3` | `*(this+1364) = 0`. | pattern scan |
| `0x7e15eaea` | 1 | `entry_thunk_7e15eaea` | `call` to the body directly after it (`0x7e15eaf2`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15ec4c` | 2 | `obj_clear_f1368_7e15ec4c` | `*(this+1368) = 0`. | pattern scan |
| `0x7e15ec93` | 1 | `entry_thunk_7e15ec93` | `call` to the body directly after it (`0x7e15ec9b`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15ed39` | 1 | `entry_thunk_7e15ed39` | `call` to the body directly after it (`0x7e15ed41`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15edac` | 2 | `obj_clear_f1372_7e15edac` | `*(this+1372) = 0`. | pattern scan |
| `0x7e15edf3` | 1 | `entry_thunk_7e15edf3` | `call` to the body directly after it (`0x7e15edfb`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15ef10` | 2 | `entry_thunk_7e15ef10` | `call` to the body directly after it (`0x7e15ef18`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15fe62` | 2 | `obj_set1_f252_7e15fe62` | `*(this+252) = 1`. | pattern scan |
| `0x7e15fe6b` | 1 | `obj_clear_f552_7e15fe6b` | `*(this+552) = 0`. | pattern scan |
| `0x7e15feaf` | 1 | `entry_thunk_7e15feaf` | `call` to the body directly after it (`0x7e15feb7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e15fed3` | 2 | `entry_thunk_7e15fed3` | `call` to the body directly after it (`0x7e15fedb`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16000d` | 2 | `entry_thunk_7e16000d` | `call` to the body directly after it (`0x7e160015`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e160120` | 1 | `entry_thunk_7e160120` | `call` to the body directly after it (`0x7e160128`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16017d` | 1 | `entry_thunk_7e16017d` | `call` to the body directly after it (`0x7e160185`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1601d2` | 1 | `entry_thunk_7e1601d2` | `call` to the body directly after it (`0x7e1601da`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1601f6` | 3 | `entry_thunk_7e1601f6` | `call` to the body directly after it (`0x7e1601fe`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e160999` | 2 | `obj_clear_f952_7e160999` | `*(this+952) = 0`. | pattern scan |
| `0x7e1609e0` | 1 | `entry_thunk_7e1609e0` | `call` to the body directly after it (`0x7e1609e8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e160a45` | 2 | `obj_clear_f1240_7e160a45` | `*(this+1240) = 0`. | pattern scan |
| `0x7e160a8c` | 1 | `entry_thunk_7e160a8c` | `call` to the body directly after it (`0x7e160a94`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e160b41` | 2 | `obj_clear_f956_7e160b41` | `*(this+956) = 0`. | pattern scan |
| `0x7e160b88` | 1 | `entry_thunk_7e160b88` | `call` to the body directly after it (`0x7e160b90`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e160bac` | 1 | `entry_thunk_7e160bac` | `call` to the body directly after it (`0x7e160bb4`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e160dcb` | 2 | `obj_clear_f1244_7e160dcb` | `*(this+1244) = 0`. | pattern scan |
| `0x7e160e12` | 1 | `entry_thunk_7e160e12` | `call` to the body directly after it (`0x7e160e1a`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e160ed0` | 2 | `obj_clear_f960_7e160ed0` | `*(this+960) = 0`. | pattern scan |
| `0x7e160f17` | 1 | `entry_thunk_7e160f17` | `call` to the body directly after it (`0x7e160f1f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e160f49` | 2 | `obj_clear_f964_7e160f49` | `*(this+964) = 0`. | pattern scan |
| `0x7e160f90` | 1 | `entry_thunk_7e160f90` | `call` to the body directly after it (`0x7e160f98`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e160fc2` | 2 | `obj_clear_f968_7e160fc2` | `*(this+968) = 0`. | pattern scan |
| `0x7e161009` | 1 | `entry_thunk_7e161009` | `call` to the body directly after it (`0x7e161011`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16103b` | 2 | `obj_clear_f972_7e16103b` | `*(this+972) = 0`. | pattern scan |
| `0x7e161082` | 1 | `entry_thunk_7e161082` | `call` to the body directly after it (`0x7e16108a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1610b4` | 2 | `obj_clear_f976_7e1610b4` | `*(this+976) = 0`. | pattern scan |
| `0x7e1610fb` | 1 | `entry_thunk_7e1610fb` | `call` to the body directly after it (`0x7e161103`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16112d` | 2 | `obj_clear_f980_7e16112d` | `*(this+980) = 0`. | pattern scan |
| `0x7e161174` | 1 | `entry_thunk_7e161174` | `call` to the body directly after it (`0x7e16117c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1611a6` | 2 | `obj_clear_f984_7e1611a6` | `*(this+984) = 0`. | pattern scan |
| `0x7e1611ed` | 1 | `entry_thunk_7e1611ed` | `call` to the body directly after it (`0x7e1611f5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16121f` | 2 | `obj_clear_f988_7e16121f` | `*(this+988) = 0`. | pattern scan |
| `0x7e161266` | 1 | `entry_thunk_7e161266` | `call` to the body directly after it (`0x7e16126e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e161298` | 2 | `obj_clear_f992_7e161298` | `*(this+992) = 0`. | pattern scan |
| `0x7e1612df` | 1 | `entry_thunk_7e1612df` | `call` to the body directly after it (`0x7e1612e7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e161311` | 2 | `obj_clear_f996_7e161311` | `*(this+996) = 0`. | pattern scan |
| `0x7e161358` | 1 | `entry_thunk_7e161358` | `call` to the body directly after it (`0x7e161360`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16138a` | 2 | `obj_clear_f1000_7e16138a` | `*(this+1000) = 0`. | pattern scan |
| `0x7e1613d1` | 1 | `entry_thunk_7e1613d1` | `call` to the body directly after it (`0x7e1613d9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1614d5` | 2 | `obj_clear_f1004_7e1614d5` | `*(this+1004) = 0`. | pattern scan |
| `0x7e16151c` | 1 | `entry_thunk_7e16151c` | `call` to the body directly after it (`0x7e161524`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16154e` | 2 | `obj_clear_f1008_7e16154e` | `*(this+1008) = 0`. | pattern scan |
| `0x7e161595` | 1 | `entry_thunk_7e161595` | `call` to the body directly after it (`0x7e16159d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16161c` | 1 | `entry_thunk_7e16161c` | `call` to the body directly after it (`0x7e161624`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16164e` | 2 | `obj_clear_f1016_7e16164e` | `*(this+1016) = 0`. | pattern scan |
| `0x7e161695` | 1 | `entry_thunk_7e161695` | `call` to the body directly after it (`0x7e16169d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1616c7` | 2 | `obj_clear_f1020_7e1616c7` | `*(this+1020) = 0`. | pattern scan |
| `0x7e16170e` | 1 | `entry_thunk_7e16170e` | `call` to the body directly after it (`0x7e161716`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e161732` | 1 | `entry_thunk_7e161732` | `call` to the body directly after it (`0x7e16173a`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e163717` | 2 | `obj_set1_f252_7e163717` | `*(this+252) = 1`. | pattern scan |
| `0x7e163720` | 1 | `obj_clear_f552_7e163720` | `*(this+552) = 0`. | pattern scan |
| `0x7e163764` | 1 | `entry_thunk_7e163764` | `call` to the body directly after it (`0x7e16376c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e163788` | 2 | `entry_thunk_7e163788` | `call` to the body directly after it (`0x7e163790`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1638c2` | 2 | `entry_thunk_7e1638c2` | `call` to the body directly after it (`0x7e1638ca`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1639d5` | 1 | `entry_thunk_7e1639d5` | `call` to the body directly after it (`0x7e1639dd`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e163a32` | 1 | `entry_thunk_7e163a32` | `call` to the body directly after it (`0x7e163a3a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e163a87` | 1 | `entry_thunk_7e163a87` | `call` to the body directly after it (`0x7e163a8f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e163aab` | 3 | `entry_thunk_7e163aab` | `call` to the body directly after it (`0x7e163ab3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16427f` | 2 | `obj_clear_f952_7e16427f` | `*(this+952) = 0`. | pattern scan |
| `0x7e1642c6` | 1 | `entry_thunk_7e1642c6` | `call` to the body directly after it (`0x7e1642ce`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16432b` | 2 | `obj_clear_f1304_7e16432b` | `*(this+1304) = 0`. | pattern scan |
| `0x7e164372` | 1 | `entry_thunk_7e164372` | `call` to the body directly after it (`0x7e16437a`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e164447` | 1 | `entry_thunk_7e164447` | `call` to the body directly after it (`0x7e16444f`, register-save mask `0x20`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16448b` | 1 | `entry_thunk_7e16448b` | `call` to the body directly after it (`0x7e164493`, register-save mask `0x20`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e164500` | 1 | `entry_thunk_7e164500` | `call` to the body directly after it (`0x7e164508`, register-save mask `0x20`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e164583` | 2 | `obj_clear_f956_7e164583` | `*(this+956) = 0`. | pattern scan |
| `0x7e1645ca` | 1 | `entry_thunk_7e1645ca` | `call` to the body directly after it (`0x7e1645d2`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1645fc` | 2 | `obj_clear_f1308_7e1645fc` | `*(this+1308) = 0`. | pattern scan |
| `0x7e164643` | 1 | `entry_thunk_7e164643` | `call` to the body directly after it (`0x7e16464b`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e164718` | 1 | `entry_thunk_7e164718` | `call` to the body directly after it (`0x7e164720`, register-save mask `0x20`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e164832` | 2 | `obj_clear_f1312_7e164832` | `*(this+1312) = 0`. | pattern scan |
| `0x7e164879` | 1 | `entry_thunk_7e164879` | `call` to the body directly after it (`0x7e164881`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16494e` | 1 | `entry_thunk_7e16494e` | `call` to the body directly after it (`0x7e164956`, register-save mask `0x20`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e164a68` | 2 | `obj_clear_f1316_7e164a68` | `*(this+1316) = 0`. | pattern scan |
| `0x7e164aaf` | 1 | `entry_thunk_7e164aaf` | `call` to the body directly after it (`0x7e164ab7`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e164b8f` | 1 | `entry_thunk_7e164b8f` | `call` to the body directly after it (`0x7e164b97`, register-save mask `0x20`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e164ce5` | 2 | `obj_clear_f1320_7e164ce5` | `*(this+1320) = 0`. | pattern scan |
| `0x7e164d2c` | 1 | `entry_thunk_7e164d2c` | `call` to the body directly after it (`0x7e164d34`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e165039` | 1 | `entry_thunk_7e165039` | `call` to the body directly after it (`0x7e165041`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16534a` | 2 | `obj_clear_f1324_7e16534a` | `*(this+1324) = 0`. | pattern scan |
| `0x7e165391` | 1 | `entry_thunk_7e165391` | `call` to the body directly after it (`0x7e165399`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1654e9` | 1 | `entry_thunk_7e1654e9` | `call` to the body directly after it (`0x7e1654f1`, register-save mask `0x20`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16563f` | 2 | `obj_clear_f1328_7e16563f` | `*(this+1328) = 0`. | pattern scan |
| `0x7e165686` | 1 | `entry_thunk_7e165686` | `call` to the body directly after it (`0x7e16568e`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1657de` | 1 | `entry_thunk_7e1657de` | `call` to the body directly after it (`0x7e1657e6`, register-save mask `0x20`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e165934` | 2 | `obj_clear_f960_7e165934` | `*(this+960) = 0`. | pattern scan |
| `0x7e16597b` | 1 | `entry_thunk_7e16597b` | `call` to the body directly after it (`0x7e165983`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1659ad` | 2 | `obj_clear_f964_7e1659ad` | `*(this+964) = 0`. | pattern scan |
| `0x7e1659f4` | 1 | `entry_thunk_7e1659f4` | `call` to the body directly after it (`0x7e1659fc`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e165a26` | 2 | `obj_clear_f968_7e165a26` | `*(this+968) = 0`. | pattern scan |
| `0x7e165a6d` | 1 | `entry_thunk_7e165a6d` | `call` to the body directly after it (`0x7e165a75`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e165a9f` | 2 | `obj_clear_f972_7e165a9f` | `*(this+972) = 0`. | pattern scan |
| `0x7e165ae6` | 1 | `entry_thunk_7e165ae6` | `call` to the body directly after it (`0x7e165aee`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e165b18` | 2 | `obj_clear_f976_7e165b18` | `*(this+976) = 0`. | pattern scan |
| `0x7e165b5f` | 1 | `entry_thunk_7e165b5f` | `call` to the body directly after it (`0x7e165b67`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e165b91` | 2 | `obj_clear_f980_7e165b91` | `*(this+980) = 0`. | pattern scan |
| `0x7e165bd8` | 1 | `entry_thunk_7e165bd8` | `call` to the body directly after it (`0x7e165be0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e165c0a` | 2 | `obj_clear_f984_7e165c0a` | `*(this+984) = 0`. | pattern scan |
| `0x7e165c51` | 1 | `entry_thunk_7e165c51` | `call` to the body directly after it (`0x7e165c59`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e165c83` | 2 | `obj_clear_f988_7e165c83` | `*(this+988) = 0`. | pattern scan |
| `0x7e165cca` | 1 | `entry_thunk_7e165cca` | `call` to the body directly after it (`0x7e165cd2`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e165cfc` | 2 | `obj_clear_f992_7e165cfc` | `*(this+992) = 0`. | pattern scan |
| `0x7e165d43` | 1 | `entry_thunk_7e165d43` | `call` to the body directly after it (`0x7e165d4b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e165d75` | 2 | `obj_clear_f996_7e165d75` | `*(this+996) = 0`. | pattern scan |
| `0x7e165dbc` | 1 | `entry_thunk_7e165dbc` | `call` to the body directly after it (`0x7e165dc4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e165dee` | 2 | `obj_clear_f1000_7e165dee` | `*(this+1000) = 0`. | pattern scan |
| `0x7e165e35` | 1 | `entry_thunk_7e165e35` | `call` to the body directly after it (`0x7e165e3d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e165f39` | 2 | `obj_clear_f1004_7e165f39` | `*(this+1004) = 0`. | pattern scan |
| `0x7e165f80` | 1 | `entry_thunk_7e165f80` | `call` to the body directly after it (`0x7e165f88`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e165fa4` | 1 | `entry_thunk_7e165fa4` | `call` to the body directly after it (`0x7e165fac`, register-save mask `0x20`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e166019` | 1 | `entry_thunk_7e166019` | `call` to the body directly after it (`0x7e166021`, register-save mask `0x20`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16608e` | 1 | `entry_thunk_7e16608e` | `call` to the body directly after it (`0x7e166096`, register-save mask `0x20`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e166111` | 2 | `obj_clear_f1008_7e166111` | `*(this+1008) = 0`. | pattern scan |
| `0x7e166158` | 1 | `entry_thunk_7e166158` | `call` to the body directly after it (`0x7e166160`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1661df` | 1 | `entry_thunk_7e1661df` | `call` to the body directly after it (`0x7e1661e7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e166211` | 2 | `obj_clear_f1016_7e166211` | `*(this+1016) = 0`. | pattern scan |
| `0x7e166258` | 1 | `entry_thunk_7e166258` | `call` to the body directly after it (`0x7e166260`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16628a` | 2 | `obj_clear_f1332_7e16628a` | `*(this+1332) = 0`. | pattern scan |
| `0x7e1662d1` | 1 | `entry_thunk_7e1662d1` | `call` to the body directly after it (`0x7e1662d9`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16645d` | 2 | `obj_clear_f1020_7e16645d` | `*(this+1020) = 0`. | pattern scan |
| `0x7e1664a4` | 1 | `entry_thunk_7e1664a4` | `call` to the body directly after it (`0x7e1664ac`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1664c8` | 1 | `entry_thunk_7e1664c8` | `call` to the body directly after it (`0x7e1664d0`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e167324` | 2 | `obj_set1_f252_7e167324` | `*(this+252) = 1`. | pattern scan |
| `0x7e16732d` | 1 | `obj_clear_f552_7e16732d` | `*(this+552) = 0`. | pattern scan |
| `0x7e167371` | 1 | `entry_thunk_7e167371` | `call` to the body directly after it (`0x7e167379`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e167395` | 2 | `entry_thunk_7e167395` | `call` to the body directly after it (`0x7e16739d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1674cf` | 2 | `entry_thunk_7e1674cf` | `call` to the body directly after it (`0x7e1674d7`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1675e2` | 1 | `entry_thunk_7e1675e2` | `call` to the body directly after it (`0x7e1675ea`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16763f` | 1 | `entry_thunk_7e16763f` | `call` to the body directly after it (`0x7e167647`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e167694` | 1 | `entry_thunk_7e167694` | `call` to the body directly after it (`0x7e16769c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1676b8` | 3 | `entry_thunk_7e1676b8` | `call` to the body directly after it (`0x7e1676c0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e167f6b` | 2 | `obj_clear_f952_7e167f6b` | `*(this+952) = 0`. | pattern scan |
| `0x7e167fb2` | 1 | `entry_thunk_7e167fb2` | `call` to the body directly after it (`0x7e167fba`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e168017` | 2 | `obj_clear_f1336_7e168017` | `*(this+1336) = 0`. | pattern scan |
| `0x7e16805e` | 1 | `entry_thunk_7e16805e` | `call` to the body directly after it (`0x7e168066`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e168121` | 2 | `obj_clear_f1340_7e168121` | `*(this+1340) = 0`. | pattern scan |
| `0x7e168168` | 1 | `entry_thunk_7e168168` | `call` to the body directly after it (`0x7e168170`, register-save mask `0xb0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e168243` | 2 | `obj_clear_f1344_7e168243` | `*(this+1344) = 0`. | pattern scan |
| `0x7e16828a` | 1 | `entry_thunk_7e16828a` | `call` to the body directly after it (`0x7e168292`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e168341` | 2 | `obj_clear_f956_7e168341` | `*(this+956) = 0`. | pattern scan |
| `0x7e168388` | 1 | `entry_thunk_7e168388` | `call` to the body directly after it (`0x7e168390`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1683ba` | 2 | `obj_clear_f1348_7e1683ba` | `*(this+1348) = 0`. | pattern scan |
| `0x7e168401` | 1 | `entry_thunk_7e168401` | `call` to the body directly after it (`0x7e168409`, register-save mask `0xf0`, frame 56) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16865c` | 1 | `entry_thunk_7e16865c` | `call` to the body directly after it (`0x7e168664`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e168957` | 2 | `obj_clear_f1352_7e168957` | `*(this+1352) = 0`. | pattern scan |
| `0x7e16899e` | 1 | `entry_thunk_7e16899e` | `call` to the body directly after it (`0x7e1689a6`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e168afa` | 2 | `obj_clear_f1356_7e168afa` | `*(this+1356) = 0`. | pattern scan |
| `0x7e168b41` | 1 | `entry_thunk_7e168b41` | `call` to the body directly after it (`0x7e168b49`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e168c31` | 2 | `obj_clear_f1360_7e168c31` | `*(this+1360) = 0`. | pattern scan |
| `0x7e168c78` | 1 | `entry_thunk_7e168c78` | `call` to the body directly after it (`0x7e168c80`, register-save mask `0xf0`, frame 132) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e169295` | 2 | `obj_clear_f960_7e169295` | `*(this+960) = 0`. | pattern scan |
| `0x7e1692dc` | 1 | `entry_thunk_7e1692dc` | `call` to the body directly after it (`0x7e1692e4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16930e` | 2 | `obj_clear_f964_7e16930e` | `*(this+964) = 0`. | pattern scan |
| `0x7e169355` | 1 | `entry_thunk_7e169355` | `call` to the body directly after it (`0x7e16935d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e169387` | 2 | `obj_clear_f968_7e169387` | `*(this+968) = 0`. | pattern scan |
| `0x7e1693ce` | 1 | `entry_thunk_7e1693ce` | `call` to the body directly after it (`0x7e1693d6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e169400` | 2 | `obj_clear_f1364_7e169400` | `*(this+1364) = 0`. | pattern scan |
| `0x7e169447` | 1 | `entry_thunk_7e169447` | `call` to the body directly after it (`0x7e16944f`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16950b` | 2 | `obj_clear_f972_7e16950b` | `*(this+972) = 0`. | pattern scan |
| `0x7e169552` | 1 | `entry_thunk_7e169552` | `call` to the body directly after it (`0x7e16955a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e169584` | 2 | `obj_clear_f976_7e169584` | `*(this+976) = 0`. | pattern scan |
| `0x7e1695cb` | 1 | `entry_thunk_7e1695cb` | `call` to the body directly after it (`0x7e1695d3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1695fd` | 2 | `obj_clear_f1368_7e1695fd` | `*(this+1368) = 0`. | pattern scan |
| `0x7e169644` | 1 | `entry_thunk_7e169644` | `call` to the body directly after it (`0x7e16964c`, register-save mask `0xb0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16971e` | 2 | `obj_clear_f980_7e16971e` | `*(this+980) = 0`. | pattern scan |
| `0x7e169765` | 1 | `entry_thunk_7e169765` | `call` to the body directly after it (`0x7e16976d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e169797` | 2 | `obj_clear_f984_7e169797` | `*(this+984) = 0`. | pattern scan |
| `0x7e1697de` | 1 | `entry_thunk_7e1697de` | `call` to the body directly after it (`0x7e1697e6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e169810` | 2 | `obj_clear_f988_7e169810` | `*(this+988) = 0`. | pattern scan |
| `0x7e169857` | 1 | `entry_thunk_7e169857` | `call` to the body directly after it (`0x7e16985f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e169889` | 2 | `obj_clear_f992_7e169889` | `*(this+992) = 0`. | pattern scan |
| `0x7e1698d0` | 1 | `entry_thunk_7e1698d0` | `call` to the body directly after it (`0x7e1698d8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e169902` | 2 | `obj_clear_f996_7e169902` | `*(this+996) = 0`. | pattern scan |
| `0x7e169949` | 1 | `entry_thunk_7e169949` | `call` to the body directly after it (`0x7e169951`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16997b` | 2 | `obj_clear_f1372_7e16997b` | `*(this+1372) = 0`. | pattern scan |
| `0x7e1699c2` | 1 | `entry_thunk_7e1699c2` | `call` to the body directly after it (`0x7e1699ca`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e169a97` | 2 | `obj_clear_f1000_7e169a97` | `*(this+1000) = 0`. | pattern scan |
| `0x7e169ade` | 1 | `entry_thunk_7e169ade` | `call` to the body directly after it (`0x7e169ae6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e169be2` | 2 | `obj_clear_f1004_7e169be2` | `*(this+1004) = 0`. | pattern scan |
| `0x7e169c29` | 1 | `entry_thunk_7e169c29` | `call` to the body directly after it (`0x7e169c31`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e169c62` | 2 | `obj_clear_f1008_7e169c62` | `*(this+1008) = 0`. | pattern scan |
| `0x7e169ca9` | 1 | `entry_thunk_7e169ca9` | `call` to the body directly after it (`0x7e169cb1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e169d30` | 1 | `entry_thunk_7e169d30` | `call` to the body directly after it (`0x7e169d38`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e169d62` | 2 | `obj_clear_f1016_7e169d62` | `*(this+1016) = 0`. | pattern scan |
| `0x7e169da9` | 1 | `entry_thunk_7e169da9` | `call` to the body directly after it (`0x7e169db1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e169ddb` | 2 | `obj_clear_f1020_7e169ddb` | `*(this+1020) = 0`. | pattern scan |
| `0x7e169e22` | 1 | `entry_thunk_7e169e22` | `call` to the body directly after it (`0x7e169e2a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e169eb4` | 1 | `entry_thunk_7e169eb4` | `call` to the body directly after it (`0x7e169ebc`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e169f94` | 2 | `obj_clear_f1380_7e169f94` | `*(this+1380) = 0`. | pattern scan |
| `0x7e169fdb` | 1 | `entry_thunk_7e169fdb` | `call` to the body directly after it (`0x7e169fe3`, register-save mask `0xf0`, frame 60) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16a1aa` | 1 | `entry_thunk_7e16a1aa` | `call` to the body directly after it (`0x7e16a1b2`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16aca0` | 2 | `obj_set1_f252_7e16aca0` | `*(this+252) = 1`. | pattern scan |
| `0x7e16aca9` | 1 | `obj_clear_f552_7e16aca9` | `*(this+552) = 0`. | pattern scan |
| `0x7e16aced` | 1 | `entry_thunk_7e16aced` | `call` to the body directly after it (`0x7e16acf5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16ad11` | 2 | `entry_thunk_7e16ad11` | `call` to the body directly after it (`0x7e16ad19`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16ae4b` | 2 | `entry_thunk_7e16ae4b` | `call` to the body directly after it (`0x7e16ae53`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16af5e` | 1 | `entry_thunk_7e16af5e` | `call` to the body directly after it (`0x7e16af66`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16afbb` | 1 | `entry_thunk_7e16afbb` | `call` to the body directly after it (`0x7e16afc3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16b010` | 1 | `entry_thunk_7e16b010` | `call` to the body directly after it (`0x7e16b018`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16b034` | 3 | `entry_thunk_7e16b034` | `call` to the body directly after it (`0x7e16b03c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16b7f9` | 2 | `obj_clear_f952_7e16b7f9` | `*(this+952) = 0`. | pattern scan |
| `0x7e16b840` | 1 | `entry_thunk_7e16b840` | `call` to the body directly after it (`0x7e16b848`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16b8a5` | 2 | `obj_clear_f1240_7e16b8a5` | `*(this+1240) = 0`. | pattern scan |
| `0x7e16b8ec` | 1 | `entry_thunk_7e16b8ec` | `call` to the body directly after it (`0x7e16b8f4`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16ba44` | 2 | `obj_clear_f956_7e16ba44` | `*(this+956) = 0`. | pattern scan |
| `0x7e16ba8b` | 1 | `entry_thunk_7e16ba8b` | `call` to the body directly after it (`0x7e16ba93`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16babd` | 2 | `obj_clear_f1244_7e16babd` | `*(this+1244) = 0`. | pattern scan |
| `0x7e16bb04` | 1 | `entry_thunk_7e16bb04` | `call` to the body directly after it (`0x7e16bb0c`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16bdc3` | 1 | `entry_thunk_7e16bdc3` | `call` to the body directly after it (`0x7e16bdcb`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16c032` | 2 | `obj_clear_f1248_7e16c032` | `*(this+1248) = 0`. | pattern scan |
| `0x7e16c079` | 1 | `entry_thunk_7e16c079` | `call` to the body directly after it (`0x7e16c081`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16c20d` | 2 | `obj_clear_f1252_7e16c20d` | `*(this+1252) = 0`. | pattern scan |
| `0x7e16c254` | 1 | `entry_thunk_7e16c254` | `call` to the body directly after it (`0x7e16c25c`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16c30e` | 2 | `obj_clear_f1256_7e16c30e` | `*(this+1256) = 0`. | pattern scan |
| `0x7e16c355` | 1 | `entry_thunk_7e16c355` | `call` to the body directly after it (`0x7e16c35d`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16c4e2` | 2 | `obj_clear_f960_7e16c4e2` | `*(this+960) = 0`. | pattern scan |
| `0x7e16c529` | 1 | `entry_thunk_7e16c529` | `call` to the body directly after it (`0x7e16c531`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16c55b` | 2 | `obj_clear_f964_7e16c55b` | `*(this+964) = 0`. | pattern scan |
| `0x7e16c5a2` | 1 | `entry_thunk_7e16c5a2` | `call` to the body directly after it (`0x7e16c5aa`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16c5d4` | 2 | `obj_clear_f968_7e16c5d4` | `*(this+968) = 0`. | pattern scan |
| `0x7e16c61b` | 1 | `entry_thunk_7e16c61b` | `call` to the body directly after it (`0x7e16c623`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16c64d` | 2 | `obj_clear_f972_7e16c64d` | `*(this+972) = 0`. | pattern scan |
| `0x7e16c694` | 1 | `entry_thunk_7e16c694` | `call` to the body directly after it (`0x7e16c69c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16c6c6` | 2 | `obj_clear_f976_7e16c6c6` | `*(this+976) = 0`. | pattern scan |
| `0x7e16c70d` | 1 | `entry_thunk_7e16c70d` | `call` to the body directly after it (`0x7e16c715`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16c73f` | 2 | `obj_clear_f1260_7e16c73f` | `*(this+1260) = 0`. | pattern scan |
| `0x7e16c786` | 1 | `entry_thunk_7e16c786` | `call` to the body directly after it (`0x7e16c78e`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16ca39` | 2 | `obj_clear_f980_7e16ca39` | `*(this+980) = 0`. | pattern scan |
| `0x7e16ca80` | 1 | `entry_thunk_7e16ca80` | `call` to the body directly after it (`0x7e16ca88`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16cab2` | 2 | `obj_clear_f984_7e16cab2` | `*(this+984) = 0`. | pattern scan |
| `0x7e16caf9` | 1 | `entry_thunk_7e16caf9` | `call` to the body directly after it (`0x7e16cb01`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16cb2b` | 2 | `obj_clear_f988_7e16cb2b` | `*(this+988) = 0`. | pattern scan |
| `0x7e16cb72` | 1 | `entry_thunk_7e16cb72` | `call` to the body directly after it (`0x7e16cb7a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16cba4` | 2 | `obj_clear_f992_7e16cba4` | `*(this+992) = 0`. | pattern scan |
| `0x7e16cbeb` | 1 | `entry_thunk_7e16cbeb` | `call` to the body directly after it (`0x7e16cbf3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16cc1d` | 2 | `obj_clear_f996_7e16cc1d` | `*(this+996) = 0`. | pattern scan |
| `0x7e16cc64` | 1 | `entry_thunk_7e16cc64` | `call` to the body directly after it (`0x7e16cc6c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16cc96` | 2 | `obj_clear_f1000_7e16cc96` | `*(this+1000) = 0`. | pattern scan |
| `0x7e16ccdd` | 1 | `entry_thunk_7e16ccdd` | `call` to the body directly after it (`0x7e16cce5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16cde1` | 2 | `obj_clear_f1004_7e16cde1` | `*(this+1004) = 0`. | pattern scan |
| `0x7e16ce28` | 1 | `entry_thunk_7e16ce28` | `call` to the body directly after it (`0x7e16ce30`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16ce5a` | 2 | `obj_clear_f1008_7e16ce5a` | `*(this+1008) = 0`. | pattern scan |
| `0x7e16cea1` | 1 | `entry_thunk_7e16cea1` | `call` to the body directly after it (`0x7e16cea9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16cf28` | 1 | `entry_thunk_7e16cf28` | `call` to the body directly after it (`0x7e16cf30`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16cf5a` | 2 | `obj_clear_f1016_7e16cf5a` | `*(this+1016) = 0`. | pattern scan |
| `0x7e16cfa1` | 1 | `entry_thunk_7e16cfa1` | `call` to the body directly after it (`0x7e16cfa9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16cfd3` | 2 | `obj_clear_f1020_7e16cfd3` | `*(this+1020) = 0`. | pattern scan |
| `0x7e16d01a` | 1 | `entry_thunk_7e16d01a` | `call` to the body directly after it (`0x7e16d022`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16d03e` | 1 | `entry_thunk_7e16d03e` | `call` to the body directly after it (`0x7e16d046`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16e1e5` | 2 | `obj_set1_f252_7e16e1e5` | `*(this+252) = 1`. | pattern scan |
| `0x7e16e1ee` | 1 | `obj_clear_f552_7e16e1ee` | `*(this+552) = 0`. | pattern scan |
| `0x7e16e232` | 1 | `entry_thunk_7e16e232` | `call` to the body directly after it (`0x7e16e23a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16e256` | 2 | `entry_thunk_7e16e256` | `call` to the body directly after it (`0x7e16e25e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16e390` | 2 | `entry_thunk_7e16e390` | `call` to the body directly after it (`0x7e16e398`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16e4a3` | 1 | `entry_thunk_7e16e4a3` | `call` to the body directly after it (`0x7e16e4ab`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16e500` | 1 | `entry_thunk_7e16e500` | `call` to the body directly after it (`0x7e16e508`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16e555` | 1 | `entry_thunk_7e16e555` | `call` to the body directly after it (`0x7e16e55d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16e579` | 3 | `entry_thunk_7e16e579` | `call` to the body directly after it (`0x7e16e581`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16ed2c` | 2 | `obj_clear_f952_7e16ed2c` | `*(this+952) = 0`. | pattern scan |
| `0x7e16ed73` | 1 | `entry_thunk_7e16ed73` | `call` to the body directly after it (`0x7e16ed7b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16edd8` | 2 | `obj_clear_f1260_7e16edd8` | `*(this+1260) = 0`. | pattern scan |
| `0x7e16ee1f` | 1 | `entry_thunk_7e16ee1f` | `call` to the body directly after it (`0x7e16ee27`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16eed0` | 2 | `obj_clear_f956_7e16eed0` | `*(this+956) = 0`. | pattern scan |
| `0x7e16ef17` | 1 | `entry_thunk_7e16ef17` | `call` to the body directly after it (`0x7e16ef1f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16ef49` | 2 | `obj_clear_f1264_7e16ef49` | `*(this+1264) = 0`. | pattern scan |
| `0x7e16ef90` | 1 | `entry_thunk_7e16ef90` | `call` to the body directly after it (`0x7e16ef98`, register-save mask `0xb0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16eff6` | 1 | `entry_thunk_7e16eff6` | `call` to the body directly after it (`0x7e16effe`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16f241` | 2 | `obj_clear_f1268_7e16f241` | `*(this+1268) = 0`. | pattern scan |
| `0x7e16f288` | 1 | `entry_thunk_7e16f288` | `call` to the body directly after it (`0x7e16f290`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16f342` | 2 | `obj_clear_f960_7e16f342` | `*(this+960) = 0`. | pattern scan |
| `0x7e16f389` | 1 | `entry_thunk_7e16f389` | `call` to the body directly after it (`0x7e16f391`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16f3bb` | 2 | `obj_clear_f964_7e16f3bb` | `*(this+964) = 0`. | pattern scan |
| `0x7e16f402` | 1 | `entry_thunk_7e16f402` | `call` to the body directly after it (`0x7e16f40a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16f434` | 2 | `obj_clear_f968_7e16f434` | `*(this+968) = 0`. | pattern scan |
| `0x7e16f47b` | 1 | `entry_thunk_7e16f47b` | `call` to the body directly after it (`0x7e16f483`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16f4ad` | 2 | `obj_clear_f972_7e16f4ad` | `*(this+972) = 0`. | pattern scan |
| `0x7e16f4f4` | 1 | `entry_thunk_7e16f4f4` | `call` to the body directly after it (`0x7e16f4fc`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16f526` | 2 | `obj_clear_f976_7e16f526` | `*(this+976) = 0`. | pattern scan |
| `0x7e16f56d` | 1 | `entry_thunk_7e16f56d` | `call` to the body directly after it (`0x7e16f575`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16f59f` | 2 | `obj_clear_f980_7e16f59f` | `*(this+980) = 0`. | pattern scan |
| `0x7e16f5e6` | 1 | `entry_thunk_7e16f5e6` | `call` to the body directly after it (`0x7e16f5ee`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16f618` | 2 | `obj_clear_f984_7e16f618` | `*(this+984) = 0`. | pattern scan |
| `0x7e16f65f` | 1 | `entry_thunk_7e16f65f` | `call` to the body directly after it (`0x7e16f667`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16f691` | 2 | `obj_clear_f988_7e16f691` | `*(this+988) = 0`. | pattern scan |
| `0x7e16f6d8` | 1 | `entry_thunk_7e16f6d8` | `call` to the body directly after it (`0x7e16f6e0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16f70a` | 2 | `obj_clear_f992_7e16f70a` | `*(this+992) = 0`. | pattern scan |
| `0x7e16f751` | 1 | `entry_thunk_7e16f751` | `call` to the body directly after it (`0x7e16f759`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16f783` | 2 | `obj_clear_f996_7e16f783` | `*(this+996) = 0`. | pattern scan |
| `0x7e16f7ca` | 1 | `entry_thunk_7e16f7ca` | `call` to the body directly after it (`0x7e16f7d2`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16f7fc` | 2 | `obj_clear_f1000_7e16f7fc` | `*(this+1000) = 0`. | pattern scan |
| `0x7e16f843` | 1 | `entry_thunk_7e16f843` | `call` to the body directly after it (`0x7e16f84b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16f947` | 2 | `obj_clear_f1004_7e16f947` | `*(this+1004) = 0`. | pattern scan |
| `0x7e16f98e` | 1 | `entry_thunk_7e16f98e` | `call` to the body directly after it (`0x7e16f996`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16f9c0` | 2 | `obj_clear_f1008_7e16f9c0` | `*(this+1008) = 0`. | pattern scan |
| `0x7e16fa07` | 1 | `entry_thunk_7e16fa07` | `call` to the body directly after it (`0x7e16fa0f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16fa8e` | 1 | `entry_thunk_7e16fa8e` | `call` to the body directly after it (`0x7e16fa96`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16fac0` | 2 | `obj_clear_f1016_7e16fac0` | `*(this+1016) = 0`. | pattern scan |
| `0x7e16fb07` | 1 | `entry_thunk_7e16fb07` | `call` to the body directly after it (`0x7e16fb0f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16fb39` | 2 | `obj_clear_f1272_7e16fb39` | `*(this+1272) = 0`. | pattern scan |
| `0x7e16fb80` | 1 | `entry_thunk_7e16fb80` | `call` to the body directly after it (`0x7e16fb88`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16fcd0` | 2 | `obj_clear_f1020_7e16fcd0` | `*(this+1020) = 0`. | pattern scan |
| `0x7e16fd17` | 1 | `entry_thunk_7e16fd17` | `call` to the body directly after it (`0x7e16fd1f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e16fd3b` | 1 | `entry_thunk_7e16fd3b` | `call` to the body directly after it (`0x7e16fd43`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e170ae2` | 2 | `obj_set1_f252_7e170ae2` | `*(this+252) = 1`. | pattern scan |
| `0x7e170aeb` | 1 | `obj_clear_f552_7e170aeb` | `*(this+552) = 0`. | pattern scan |
| `0x7e170b2f` | 1 | `entry_thunk_7e170b2f` | `call` to the body directly after it (`0x7e170b37`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e170b53` | 2 | `entry_thunk_7e170b53` | `call` to the body directly after it (`0x7e170b5b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e170c8d` | 2 | `entry_thunk_7e170c8d` | `call` to the body directly after it (`0x7e170c95`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e170da0` | 1 | `entry_thunk_7e170da0` | `call` to the body directly after it (`0x7e170da8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e170dfd` | 1 | `entry_thunk_7e170dfd` | `call` to the body directly after it (`0x7e170e05`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e170e52` | 1 | `entry_thunk_7e170e52` | `call` to the body directly after it (`0x7e170e5a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e170e76` | 3 | `entry_thunk_7e170e76` | `call` to the body directly after it (`0x7e170e7e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e171729` | 2 | `obj_clear_f952_7e171729` | `*(this+952) = 0`. | pattern scan |
| `0x7e171770` | 1 | `entry_thunk_7e171770` | `call` to the body directly after it (`0x7e171778`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1717d5` | 2 | `obj_clear_f1344_7e1717d5` | `*(this+1344) = 0`. | pattern scan |
| `0x7e17181c` | 1 | `entry_thunk_7e17181c` | `call` to the body directly after it (`0x7e171824`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1718da` | 2 | `obj_clear_f1348_7e1718da` | `*(this+1348) = 0`. | pattern scan |
| `0x7e171921` | 1 | `entry_thunk_7e171921` | `call` to the body directly after it (`0x7e171929`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1719b7` | 2 | `obj_clear_f1352_7e1719b7` | `*(this+1352) = 0`. | pattern scan |
| `0x7e1719fe` | 1 | `entry_thunk_7e1719fe` | `call` to the body directly after it (`0x7e171a06`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e171aaf` | 2 | `obj_clear_f956_7e171aaf` | `*(this+956) = 0`. | pattern scan |
| `0x7e171af6` | 1 | `entry_thunk_7e171af6` | `call` to the body directly after it (`0x7e171afe`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e171b28` | 2 | `obj_clear_f1356_7e171b28` | `*(this+1356) = 0`. | pattern scan |
| `0x7e171b6f` | 1 | `entry_thunk_7e171b6f` | `call` to the body directly after it (`0x7e171b77`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e171dbb` | 1 | `entry_thunk_7e171dbb` | `call` to the body directly after it (`0x7e171dc3`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1720b6` | 2 | `obj_clear_f1360_7e1720b6` | `*(this+1360) = 0`. | pattern scan |
| `0x7e1720fd` | 1 | `entry_thunk_7e1720fd` | `call` to the body directly after it (`0x7e172105`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e172259` | 2 | `obj_clear_f1364_7e172259` | `*(this+1364) = 0`. | pattern scan |
| `0x7e1722a0` | 1 | `entry_thunk_7e1722a0` | `call` to the body directly after it (`0x7e1722a8`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17238a` | 2 | `obj_clear_f1368_7e17238a` | `*(this+1368) = 0`. | pattern scan |
| `0x7e1723d1` | 1 | `entry_thunk_7e1723d1` | `call` to the body directly after it (`0x7e1723d9`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e172955` | 2 | `obj_clear_f960_7e172955` | `*(this+960) = 0`. | pattern scan |
| `0x7e17299c` | 1 | `entry_thunk_7e17299c` | `call` to the body directly after it (`0x7e1729a4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1729ce` | 2 | `obj_clear_f964_7e1729ce` | `*(this+964) = 0`. | pattern scan |
| `0x7e172a15` | 1 | `entry_thunk_7e172a15` | `call` to the body directly after it (`0x7e172a1d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e172a47` | 2 | `obj_clear_f968_7e172a47` | `*(this+968) = 0`. | pattern scan |
| `0x7e172a8e` | 1 | `entry_thunk_7e172a8e` | `call` to the body directly after it (`0x7e172a96`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e172ac0` | 2 | `obj_clear_f1372_7e172ac0` | `*(this+1372) = 0`. | pattern scan |
| `0x7e172b07` | 1 | `entry_thunk_7e172b07` | `call` to the body directly after it (`0x7e172b0f`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e172bc5` | 2 | `obj_clear_f972_7e172bc5` | `*(this+972) = 0`. | pattern scan |
| `0x7e172c0c` | 1 | `entry_thunk_7e172c0c` | `call` to the body directly after it (`0x7e172c14`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e172c3e` | 2 | `obj_clear_f976_7e172c3e` | `*(this+976) = 0`. | pattern scan |
| `0x7e172c85` | 1 | `entry_thunk_7e172c85` | `call` to the body directly after it (`0x7e172c8d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e172cb7` | 2 | `obj_clear_f1376_7e172cb7` | `*(this+1376) = 0`. | pattern scan |
| `0x7e172cfe` | 1 | `entry_thunk_7e172cfe` | `call` to the body directly after it (`0x7e172d06`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e172dce` | 2 | `obj_clear_f980_7e172dce` | `*(this+980) = 0`. | pattern scan |
| `0x7e172e15` | 1 | `entry_thunk_7e172e15` | `call` to the body directly after it (`0x7e172e1d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e172e47` | 2 | `obj_clear_f984_7e172e47` | `*(this+984) = 0`. | pattern scan |
| `0x7e172e8e` | 1 | `entry_thunk_7e172e8e` | `call` to the body directly after it (`0x7e172e96`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e172ec0` | 2 | `obj_clear_f988_7e172ec0` | `*(this+988) = 0`. | pattern scan |
| `0x7e172f07` | 1 | `entry_thunk_7e172f07` | `call` to the body directly after it (`0x7e172f0f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e172f39` | 2 | `obj_clear_f992_7e172f39` | `*(this+992) = 0`. | pattern scan |
| `0x7e172f80` | 1 | `entry_thunk_7e172f80` | `call` to the body directly after it (`0x7e172f88`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e172fb2` | 2 | `obj_clear_f996_7e172fb2` | `*(this+996) = 0`. | pattern scan |
| `0x7e172ff9` | 1 | `entry_thunk_7e172ff9` | `call` to the body directly after it (`0x7e173001`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17302b` | 2 | `obj_clear_f1380_7e17302b` | `*(this+1380) = 0`. | pattern scan |
| `0x7e173072` | 1 | `entry_thunk_7e173072` | `call` to the body directly after it (`0x7e17307a`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e173142` | 2 | `obj_clear_f1000_7e173142` | `*(this+1000) = 0`. | pattern scan |
| `0x7e173189` | 1 | `entry_thunk_7e173189` | `call` to the body directly after it (`0x7e173191`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17328d` | 2 | `obj_clear_f1004_7e17328d` | `*(this+1004) = 0`. | pattern scan |
| `0x7e1732d4` | 1 | `entry_thunk_7e1732d4` | `call` to the body directly after it (`0x7e1732dc`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17330d` | 2 | `obj_clear_f1008_7e17330d` | `*(this+1008) = 0`. | pattern scan |
| `0x7e173354` | 1 | `entry_thunk_7e173354` | `call` to the body directly after it (`0x7e17335c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1733db` | 1 | `entry_thunk_7e1733db` | `call` to the body directly after it (`0x7e1733e3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17340d` | 2 | `obj_clear_f1016_7e17340d` | `*(this+1016) = 0`. | pattern scan |
| `0x7e173454` | 1 | `entry_thunk_7e173454` | `call` to the body directly after it (`0x7e17345c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e173486` | 2 | `obj_clear_f1020_7e173486` | `*(this+1020) = 0`. | pattern scan |
| `0x7e1734cd` | 1 | `entry_thunk_7e1734cd` | `call` to the body directly after it (`0x7e1734d5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1734ff` | 2 | `obj_clear_f1384_7e1734ff` | `*(this+1384) = 0`. | pattern scan |
| `0x7e173546` | 1 | `entry_thunk_7e173546` | `call` to the body directly after it (`0x7e17354e`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e173626` | 2 | `obj_clear_f1388_7e173626` | `*(this+1388) = 0`. | pattern scan |
| `0x7e17366d` | 1 | `entry_thunk_7e17366d` | `call` to the body directly after it (`0x7e173675`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e173874` | 1 | `entry_thunk_7e173874` | `call` to the body directly after it (`0x7e17387c`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1758c6` | 2 | `obj_set1_f252_7e1758c6` | `*(this+252) = 1`. | pattern scan |
| `0x7e1758cf` | 1 | `obj_clear_f552_7e1758cf` | `*(this+552) = 0`. | pattern scan |
| `0x7e175913` | 1 | `entry_thunk_7e175913` | `call` to the body directly after it (`0x7e17591b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e175937` | 2 | `entry_thunk_7e175937` | `call` to the body directly after it (`0x7e17593f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e175a71` | 2 | `entry_thunk_7e175a71` | `call` to the body directly after it (`0x7e175a79`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e175b84` | 1 | `entry_thunk_7e175b84` | `call` to the body directly after it (`0x7e175b8c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e175be1` | 1 | `entry_thunk_7e175be1` | `call` to the body directly after it (`0x7e175be9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e175c36` | 1 | `entry_thunk_7e175c36` | `call` to the body directly after it (`0x7e175c3e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e175c5a` | 3 | `entry_thunk_7e175c5a` | `call` to the body directly after it (`0x7e175c62`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e176467` | 2 | `obj_clear_f1336_7e176467` | `*(this+1336) = 0`. | pattern scan |
| `0x7e1764ae` | 1 | `entry_thunk_7e1764ae` | `call` to the body directly after it (`0x7e1764b6`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e176695` | 2 | `obj_clear_f952_7e176695` | `*(this+952) = 0`. | pattern scan |
| `0x7e1766dc` | 1 | `entry_thunk_7e1766dc` | `call` to the body directly after it (`0x7e1766e4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e176741` | 2 | `obj_clear_f1340_7e176741` | `*(this+1340) = 0`. | pattern scan |
| `0x7e176788` | 1 | `entry_thunk_7e176788` | `call` to the body directly after it (`0x7e176790`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17684c` | 2 | `obj_clear_f1344_7e17684c` | `*(this+1344) = 0`. | pattern scan |
| `0x7e176893` | 1 | `entry_thunk_7e176893` | `call` to the body directly after it (`0x7e17689b`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e176964` | 2 | `obj_clear_f1348_7e176964` | `*(this+1348) = 0`. | pattern scan |
| `0x7e1769ab` | 1 | `entry_thunk_7e1769ab` | `call` to the body directly after it (`0x7e1769b3`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e176a5c` | 2 | `obj_clear_f956_7e176a5c` | `*(this+956) = 0`. | pattern scan |
| `0x7e176aa3` | 1 | `entry_thunk_7e176aa3` | `call` to the body directly after it (`0x7e176aab`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e176ad5` | 2 | `obj_clear_f1352_7e176ad5` | `*(this+1352) = 0`. | pattern scan |
| `0x7e176b1c` | 1 | `entry_thunk_7e176b1c` | `call` to the body directly after it (`0x7e176b24`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e176d9f` | 1 | `entry_thunk_7e176d9f` | `call` to the body directly after it (`0x7e176da7`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1770ce` | 2 | `obj_clear_f1356_7e1770ce` | `*(this+1356) = 0`. | pattern scan |
| `0x7e177115` | 1 | `entry_thunk_7e177115` | `call` to the body directly after it (`0x7e17711d`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e177271` | 2 | `obj_clear_f1360_7e177271` | `*(this+1360) = 0`. | pattern scan |
| `0x7e1772b8` | 1 | `entry_thunk_7e1772b8` | `call` to the body directly after it (`0x7e1772c0`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1773a2` | 2 | `obj_clear_f1364_7e1773a2` | `*(this+1364) = 0`. | pattern scan |
| `0x7e1773e9` | 1 | `entry_thunk_7e1773e9` | `call` to the body directly after it (`0x7e1773f1`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1775e1` | 2 | `obj_clear_f960_7e1775e1` | `*(this+960) = 0`. | pattern scan |
| `0x7e177628` | 1 | `entry_thunk_7e177628` | `call` to the body directly after it (`0x7e177630`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17765a` | 2 | `obj_clear_f964_7e17765a` | `*(this+964) = 0`. | pattern scan |
| `0x7e1776a1` | 1 | `entry_thunk_7e1776a1` | `call` to the body directly after it (`0x7e1776a9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1776d3` | 2 | `obj_clear_f968_7e1776d3` | `*(this+968) = 0`. | pattern scan |
| `0x7e17771a` | 1 | `entry_thunk_7e17771a` | `call` to the body directly after it (`0x7e177722`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17774c` | 2 | `obj_clear_f1368_7e17774c` | `*(this+1368) = 0`. | pattern scan |
| `0x7e177793` | 1 | `entry_thunk_7e177793` | `call` to the body directly after it (`0x7e17779b`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e177851` | 2 | `obj_clear_f1372_7e177851` | `*(this+1372) = 0`. | pattern scan |
| `0x7e177898` | 1 | `entry_thunk_7e177898` | `call` to the body directly after it (`0x7e1778a0`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e177d27` | 2 | `obj_clear_f972_7e177d27` | `*(this+972) = 0`. | pattern scan |
| `0x7e177d6e` | 1 | `entry_thunk_7e177d6e` | `call` to the body directly after it (`0x7e177d76`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e177da0` | 2 | `obj_clear_f976_7e177da0` | `*(this+976) = 0`. | pattern scan |
| `0x7e177de7` | 1 | `entry_thunk_7e177de7` | `call` to the body directly after it (`0x7e177def`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e177e19` | 2 | `obj_clear_f1376_7e177e19` | `*(this+1376) = 0`. | pattern scan |
| `0x7e177e60` | 1 | `entry_thunk_7e177e60` | `call` to the body directly after it (`0x7e177e68`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e177f30` | 2 | `obj_clear_f980_7e177f30` | `*(this+980) = 0`. | pattern scan |
| `0x7e177f77` | 1 | `entry_thunk_7e177f77` | `call` to the body directly after it (`0x7e177f7f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e177fa9` | 2 | `obj_clear_f984_7e177fa9` | `*(this+984) = 0`. | pattern scan |
| `0x7e177ff0` | 1 | `entry_thunk_7e177ff0` | `call` to the body directly after it (`0x7e177ff8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e178022` | 2 | `obj_clear_f988_7e178022` | `*(this+988) = 0`. | pattern scan |
| `0x7e178069` | 1 | `entry_thunk_7e178069` | `call` to the body directly after it (`0x7e178071`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17809b` | 2 | `obj_clear_f992_7e17809b` | `*(this+992) = 0`. | pattern scan |
| `0x7e1780e2` | 1 | `entry_thunk_7e1780e2` | `call` to the body directly after it (`0x7e1780ea`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e178114` | 2 | `obj_clear_f996_7e178114` | `*(this+996) = 0`. | pattern scan |
| `0x7e17815b` | 1 | `entry_thunk_7e17815b` | `call` to the body directly after it (`0x7e178163`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17818d` | 2 | `obj_clear_f1380_7e17818d` | `*(this+1380) = 0`. | pattern scan |
| `0x7e1781d4` | 1 | `entry_thunk_7e1781d4` | `call` to the body directly after it (`0x7e1781dc`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1782a4` | 2 | `obj_clear_f1000_7e1782a4` | `*(this+1000) = 0`. | pattern scan |
| `0x7e1782eb` | 1 | `entry_thunk_7e1782eb` | `call` to the body directly after it (`0x7e1782f3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1783ef` | 2 | `obj_clear_f1004_7e1783ef` | `*(this+1004) = 0`. | pattern scan |
| `0x7e178436` | 1 | `entry_thunk_7e178436` | `call` to the body directly after it (`0x7e17843e`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17846f` | 2 | `obj_clear_f1384_7e17846f` | `*(this+1384) = 0`. | pattern scan |
| `0x7e1784b6` | 1 | `entry_thunk_7e1784b6` | `call` to the body directly after it (`0x7e1784be`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1785e9` | 2 | `obj_clear_f1008_7e1785e9` | `*(this+1008) = 0`. | pattern scan |
| `0x7e178630` | 1 | `entry_thunk_7e178630` | `call` to the body directly after it (`0x7e178638`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1786b7` | 1 | `entry_thunk_7e1786b7` | `call` to the body directly after it (`0x7e1786bf`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1786e9` | 2 | `obj_clear_f1388_7e1786e9` | `*(this+1388) = 0`. | pattern scan |
| `0x7e178730` | 1 | `entry_thunk_7e178730` | `call` to the body directly after it (`0x7e178738`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17884c` | 2 | `obj_clear_f1016_7e17884c` | `*(this+1016) = 0`. | pattern scan |
| `0x7e178893` | 1 | `entry_thunk_7e178893` | `call` to the body directly after it (`0x7e17889b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1788c5` | 2 | `obj_clear_f1392_7e1788c5` | `*(this+1392) = 0`. | pattern scan |
| `0x7e17890c` | 1 | `entry_thunk_7e17890c` | `call` to the body directly after it (`0x7e178914`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e178cbf` | 2 | `obj_clear_f1020_7e178cbf` | `*(this+1020) = 0`. | pattern scan |
| `0x7e178d06` | 1 | `entry_thunk_7e178d06` | `call` to the body directly after it (`0x7e178d0e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e178d2a` | 1 | `entry_thunk_7e178d2a` | `call` to the body directly after it (`0x7e178d32`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1796b4` | 2 | `obj_set1_f252_7e1796b4` | `*(this+252) = 1`. | pattern scan |
| `0x7e1796bd` | 1 | `obj_clear_f552_7e1796bd` | `*(this+552) = 0`. | pattern scan |
| `0x7e179701` | 1 | `entry_thunk_7e179701` | `call` to the body directly after it (`0x7e179709`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e179725` | 2 | `entry_thunk_7e179725` | `call` to the body directly after it (`0x7e17972d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e179853` | 2 | `entry_thunk_7e179853` | `call` to the body directly after it (`0x7e17985b`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e179966` | 1 | `entry_thunk_7e179966` | `call` to the body directly after it (`0x7e17996e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1799c3` | 1 | `entry_thunk_7e1799c3` | `call` to the body directly after it (`0x7e1799cb`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e179a18` | 1 | `entry_thunk_7e179a18` | `call` to the body directly after it (`0x7e179a20`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e179a3c` | 3 | `entry_thunk_7e179a3c` | `call` to the body directly after it (`0x7e179a44`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e179ae6` | 1 | `entry_thunk_7e179ae6` | `call` to the body directly after it (`0x7e179aee`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17c8a9` | 2 | `obj_set1_f252_7e17c8a9` | `*(this+252) = 1`. | pattern scan |
| `0x7e17c8b2` | 1 | `obj_clear_f552_7e17c8b2` | `*(this+552) = 0`. | pattern scan |
| `0x7e17c8f6` | 1 | `entry_thunk_7e17c8f6` | `call` to the body directly after it (`0x7e17c8fe`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17c91a` | 2 | `entry_thunk_7e17c91a` | `call` to the body directly after it (`0x7e17c922`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17ca54` | 2 | `entry_thunk_7e17ca54` | `call` to the body directly after it (`0x7e17ca5c`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17cb67` | 1 | `entry_thunk_7e17cb67` | `call` to the body directly after it (`0x7e17cb6f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17cbc4` | 1 | `entry_thunk_7e17cbc4` | `call` to the body directly after it (`0x7e17cbcc`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17cc19` | 1 | `entry_thunk_7e17cc19` | `call` to the body directly after it (`0x7e17cc21`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17cc3d` | 3 | `entry_thunk_7e17cc3d` | `call` to the body directly after it (`0x7e17cc45`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17d69a` | 1 | `obj_clear_f1356_7e17d69a` | `*(this+1356) = 0`. | pattern scan |
| `0x7e17d6c0` | 1 | `entry_thunk_7e17d6c0` | `call` to the body directly after it (`0x7e17d6c8`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17d848` | 2 | `entry_thunk_7e17d848` | `call` to the body directly after it (`0x7e17d850`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17d907` | 1 | `entry_thunk_7e17d907` | `call` to the body directly after it (`0x7e17d90f`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17da09` | 1 | `entry_thunk_7e17da09` | `call` to the body directly after it (`0x7e17da11`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17dbdb` | 4 | `entry_thunk_7e17dbdb` | `call` to the body directly after it (`0x7e17dbe3`, register-save mask `0x00`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17e340` | 1 | `entry_thunk_7e17e340` | `call` to the body directly after it (`0x7e17e348`, register-save mask `0xb0`, frame 72) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17e659` | 1 | `entry_thunk_7e17e659` | `call` to the body directly after it (`0x7e17e661`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17e6c7` | 1 | `entry_thunk_7e17e6c7` | `call` to the body directly after it (`0x7e17e6cf`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17e75c` | 2 | `obj_clear_f1380_7e17e75c` | `*(this+1380) = 0`. | pattern scan |
| `0x7e17e7d5` | 1 | `entry_thunk_7e17e7d5` | `call` to the body directly after it (`0x7e17e7dd`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17e82c` | 1 | `entry_thunk_7e17e82c` | `call` to the body directly after it (`0x7e17e834`, register-save mask `0xf0`, frame 64) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17e9e4` | 1 | `entry_thunk_7e17e9e4` | `call` to the body directly after it (`0x7e17e9ec`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17eae3` | 1 | `entry_thunk_7e17eae3` | `call` to the body directly after it (`0x7e17eaeb`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17ebe2` | 1 | `entry_thunk_7e17ebe2` | `call` to the body directly after it (`0x7e17ebea`, register-save mask `0xb0`, frame 76) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17ef9b` | 1 | `entry_thunk_7e17ef9b` | `call` to the body directly after it (`0x7e17efa3`, register-save mask `0xf0`, frame 112) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17f855` | 1 | `entry_thunk_7e17f855` | `call` to the body directly after it (`0x7e17f85d`, register-save mask `0xf0`, frame 112) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17fa78` | 2 | `entry_thunk_7e17fa78` | `call` to the body directly after it (`0x7e17fa80`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17fbdd` | 1 | `entry_thunk_7e17fbdd` | `call` to the body directly after it (`0x7e17fbe5`, register-save mask `0xf0`, frame 20) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17fcbc` | 1 | `entry_thunk_7e17fcbc` | `call` to the body directly after it (`0x7e17fcc4`, register-save mask `0xf0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17fd4e` | 2 | `entry_thunk_7e17fd4e` | `call` to the body directly after it (`0x7e17fd56`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17fda5` | 1 | `entry_thunk_7e17fda5` | `call` to the body directly after it (`0x7e17fdad`, register-save mask `0xf0`, frame 24) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17fe70` | 1 | `entry_thunk_7e17fe70` | `call` to the body directly after it (`0x7e17fe78`, register-save mask `0xb0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e17ff1e` | 1 | `entry_thunk_7e17ff1e` | `call` to the body directly after it (`0x7e17ff26`, register-save mask `0xb0`, frame 52) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e180033` | 1 | `entry_thunk_7e180033` | `call` to the body directly after it (`0x7e18003b`, register-save mask `0xf0`, frame 120) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e180713` | 1 | `entry_thunk_7e180713` | `call` to the body directly after it (`0x7e18071b`, register-save mask `0xf0`, frame 100) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1808c0` | 1 | `entry_thunk_7e1808c0` | `call` to the body directly after it (`0x7e1808c8`, register-save mask `0xb0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1809e1` | 1 | `obj_clear_f1392_7e1809e1` | `*(this+1392) = 0`. | pattern scan |
| `0x7e180a1d` | 1 | `entry_thunk_7e180a1d` | `call` to the body directly after it (`0x7e180a25`, register-save mask `0xf0`, frame 64) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e180be8` | 1 | `entry_thunk_7e180be8` | `call` to the body directly after it (`0x7e180bf0`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e180c93` | 2 | `entry_thunk_7e180c93` | `call` to the body directly after it (`0x7e180c9b`, register-save mask `0xf0`, frame 56) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1811dc` | 1 | `obj_clear_f1396_7e1811dc` | `*(this+1396) = 0`. | pattern scan |
| `0x7e181218` | 1 | `entry_thunk_7e181218` | `call` to the body directly after it (`0x7e181220`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1812c3` | 1 | `entry_thunk_7e1812c3` | `call` to the body directly after it (`0x7e1812cb`, register-save mask `0xf0`, frame 72) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e181446` | 1 | `entry_thunk_7e181446` | `call` to the body directly after it (`0x7e18144e`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18159b` | 1 | `obj_clear_f1400_7e18159b` | `*(this+1400) = 0`. | pattern scan |
| `0x7e1815d7` | 1 | `entry_thunk_7e1815d7` | `call` to the body directly after it (`0x7e1815df`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18168b` | 1 | `entry_thunk_7e18168b` | `call` to the body directly after it (`0x7e181693`, register-save mask `0xf0`, frame 56) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e181804` | 1 | `entry_thunk_7e181804` | `call` to the body directly after it (`0x7e18180c`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1818b4` | 1 | `obj_clear_f1404_7e1818b4` | `*(this+1404) = 0`. | pattern scan |
| `0x7e1818f0` | 1 | `entry_thunk_7e1818f0` | `call` to the body directly after it (`0x7e1818f8`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e181967` | 1 | `entry_thunk_7e181967` | `call` to the body directly after it (`0x7e18196f`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e181a14` | 1 | `entry_thunk_7e181a14` | `call` to the body directly after it (`0x7e181a1c`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e181ba8` | 5 | `entry_thunk_7e181ba8` | `call` to the body directly after it (`0x7e181bb0`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e182128` | 1 | `entry_thunk_7e182128` | `call` to the body directly after it (`0x7e182130`, register-save mask `0xb0`, frame 56) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18225e` | 1 | `entry_thunk_7e18225e` | `call` to the body directly after it (`0x7e182266`, register-save mask `0xb0`, frame 36) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1822ff` | 1 | `entry_thunk_7e1822ff` | `call` to the body directly after it (`0x7e182307`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1823a7` | 2 | `entry_thunk_7e1823a7` | `call` to the body directly after it (`0x7e1823af`, register-save mask `0xf0`, frame 52) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e182691` | 1 | `entry_thunk_7e182691` | `call` to the body directly after it (`0x7e182699`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1827f4` | 1 | `entry_thunk_7e1827f4` | `call` to the body directly after it (`0x7e1827fc`, register-save mask `0xf0`, frame 72) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1829c4` | 3 | `entry_thunk_7e1829c4` | `call` to the body directly after it (`0x7e1829cc`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e182be2` | 1 | `entry_thunk_7e182be2` | `call` to the body directly after it (`0x7e182bea`, register-save mask `0xb0`, frame 24) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e182d92` | 1 | `entry_thunk_7e182d92` | `call` to the body directly after it (`0x7e182d9a`, register-save mask `0xb0`, frame 36) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e182ee3` | 1 | `entry_thunk_7e182ee3` | `call` to the body directly after it (`0x7e182eeb`, register-save mask `0xf0`, frame 104) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e183290` | 3 | `entry_thunk_7e183290` | `call` to the body directly after it (`0x7e183298`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1833ed` | 2 | `entry_thunk_7e1833ed` | `call` to the body directly after it (`0x7e1833f5`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e183506` | 1 | `entry_thunk_7e183506` | `call` to the body directly after it (`0x7e18350e`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e183641` | 1 | `entry_thunk_7e183641` | `call` to the body directly after it (`0x7e183649`, register-save mask `0xf0`, frame 52) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e183b2e` | 2 | `entry_thunk_7e183b2e` | `call` to the body directly after it (`0x7e183b36`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e183c82` | 1 | `entry_thunk_7e183c82` | `call` to the body directly after it (`0x7e183c8a`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e183ec5` | 1 | `entry_thunk_7e183ec5` | `call` to the body directly after it (`0x7e183ecd`, register-save mask `0xb0`, frame 20) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18411f` | 2 | `entry_thunk_7e18411f` | `call` to the body directly after it (`0x7e184127`, register-save mask `0xb0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e184298` | 3 | `entry_thunk_7e184298` | `call` to the body directly after it (`0x7e1842a0`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e184357` | 1 | `entry_thunk_7e184357` | `call` to the body directly after it (`0x7e18435f`, register-save mask `0xb0`, frame 52) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e184471` | 2 | `obj_clear_f1420_7e184471` | `*(this+1420) = 0`. | pattern scan |
| `0x7e1844b8` | 2 | `entry_thunk_7e1844b8` | `call` to the body directly after it (`0x7e1844c0`, register-save mask `0xb0`, frame 20) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18463b` | 2 | `entry_thunk_7e18463b` | `call` to the body directly after it (`0x7e184643`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e184783` | 1 | `entry_thunk_7e184783` | `call` to the body directly after it (`0x7e18478b`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18487b` | 2 | `obj_clear_f1424_7e18487b` | `*(this+1424) = 0`. | pattern scan |
| `0x7e1849e5` | 1 | `entry_thunk_7e1849e5` | `call` to the body directly after it (`0x7e1849ed`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e184abc` | 2 | `entry_thunk_7e184abc` | `call` to the body directly after it (`0x7e184ac4`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e184b7d` | 1 | `entry_thunk_7e184b7d` | `call` to the body directly after it (`0x7e184b85`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e184c5d` | 1 | `entry_thunk_7e184c5d` | `call` to the body directly after it (`0x7e184c65`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e184ced` | 1 | `entry_thunk_7e184ced` | `call` to the body directly after it (`0x7e184cf5`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e184d55` | 1 | `entry_thunk_7e184d55` | `call` to the body directly after it (`0x7e184d5d`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e184dbd` | 1 | `entry_thunk_7e184dbd` | `call` to the body directly after it (`0x7e184dc5`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e184e38` | 2 | `obj_clear_f1428_7e184e38` | `*(this+1428) = 0`. | pattern scan |
| `0x7e184e89` | 1 | `entry_thunk_7e184e89` | `call` to the body directly after it (`0x7e184e91`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e184f47` | 1 | `entry_thunk_7e184f47` | `call` to the body directly after it (`0x7e184f4f`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18501a` | 1 | `entry_thunk_7e18501a` | `call` to the body directly after it (`0x7e185022`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1850a1` | 1 | `entry_thunk_7e1850a1` | `call` to the body directly after it (`0x7e1850a9`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1851de` | 1 | `entry_thunk_7e1851de` | `call` to the body directly after it (`0x7e1851e6`, register-save mask `0xf0`, frame 52) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e185619` | 1 | `entry_thunk_7e185619` | `call` to the body directly after it (`0x7e185621`, register-save mask `0xb0`, frame 52) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e185a87` | 2 | `entry_thunk_7e185a87` | `call` to the body directly after it (`0x7e185a8f`, register-save mask `0xf0`, frame 88) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e185cc0` | 1 | `entry_thunk_7e185cc0` | `call` to the body directly after it (`0x7e185cc8`, register-save mask `0xf0`, frame 52) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e185e8e` | 1 | `entry_thunk_7e185e8e` | `call` to the body directly after it (`0x7e185e96`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e185f57` | 1 | `entry_thunk_7e185f57` | `call` to the body directly after it (`0x7e185f5f`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e186054` | 1 | `entry_thunk_7e186054` | `call` to the body directly after it (`0x7e18605c`, register-save mask `0xf0`, frame 84) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1862b3` | 1 | `entry_thunk_7e1862b3` | `call` to the body directly after it (`0x7e1862bb`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18638d` | 1 | `entry_thunk_7e18638d` | `call` to the body directly after it (`0x7e186395`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e186410` | 1 | `entry_thunk_7e186410` | `call` to the body directly after it (`0x7e186418`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1864dd` | 1 | `entry_thunk_7e1864dd` | `call` to the body directly after it (`0x7e1864e5`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1864fa` | 1 | `entry_thunk_7e1864fa` | `call` to the body directly after it (`0x7e186502`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18660a` | 1 | `entry_thunk_7e18660a` | `call` to the body directly after it (`0x7e186612`, register-save mask `0xf0`, frame 20) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1866e9` | 1 | `entry_thunk_7e1866e9` | `call` to the body directly after it (`0x7e1866f1`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18674c` | 1 | `entry_thunk_7e18674c` | `call` to the body directly after it (`0x7e186754`, register-save mask `0xb0`, frame 20) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1867e8` | 2 | `entry_thunk_7e1867e8` | `call` to the body directly after it (`0x7e1867f0`, register-save mask `0xf0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18686d` | 1 | `entry_thunk_7e18686d` | `call` to the body directly after it (`0x7e186875`, register-save mask `0xb0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e186925` | 1 | `entry_thunk_7e186925` | `call` to the body directly after it (`0x7e18692d`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1869b4` | 1 | `entry_thunk_7e1869b4` | `call` to the body directly after it (`0x7e1869bc`, register-save mask `0xf0`, frame 200) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e186e2b` | 1 | `entry_thunk_7e186e2b` | `call` to the body directly after it (`0x7e186e33`, register-save mask `0xf0`, frame 120) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e188bce` | 1 | `entry_thunk_7e188bce` | `call` to the body directly after it (`0x7e188bd6`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e188c11` | 1 | `entry_thunk_7e188c11` | `call` to the body directly after it (`0x7e188c19`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e188c54` | 1 | `entry_thunk_7e188c54` | `call` to the body directly after it (`0x7e188c5c`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e188c97` | 1 | `entry_thunk_7e188c97` | `call` to the body directly after it (`0x7e188c9f`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e188cda` | 1 | `entry_thunk_7e188cda` | `call` to the body directly after it (`0x7e188ce2`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e188dfa` | 1 | `entry_thunk_7e188dfa` | `call` to the body directly after it (`0x7e188e02`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e188ec5` | 1 | `entry_thunk_7e188ec5` | `call` to the body directly after it (`0x7e188ecd`, register-save mask `0xf0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e188fb0` | 1 | `entry_thunk_7e188fb0` | `call` to the body directly after it (`0x7e188fb8`, register-save mask `0xf0`, frame 24) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18908c` | 1 | `entry_thunk_7e18908c` | `call` to the body directly after it (`0x7e189094`, register-save mask `0xb0`, frame 20) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e189156` | 1 | `entry_thunk_7e189156` | `call` to the body directly after it (`0x7e18915e`, register-save mask `0xf0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1892ee` | 1 | `entry_thunk_7e1892ee` | `call` to the body directly after it (`0x7e1892f6`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18965a` | 1 | `entry_thunk_7e18965a` | `call` to the body directly after it (`0x7e189662`, register-save mask `0xb0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1897c2` | 1 | `entry_thunk_7e1897c2` | `call` to the body directly after it (`0x7e1897ca`, register-save mask `0xb0`, frame 196) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18989c` | 1 | `entry_thunk_7e18989c` | `call` to the body directly after it (`0x7e1898a4`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e189966` | 1 | `entry_thunk_7e189966` | `call` to the body directly after it (`0x7e18996e`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e189a81` | 1 | `entry_thunk_7e189a81` | `call` to the body directly after it (`0x7e189a89`, register-save mask `0xf0`, frame 80) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e189e1c` | 1 | `entry_thunk_7e189e1c` | `call` to the body directly after it (`0x7e189e24`, register-save mask `0xf0`, frame 36) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e189f0e` | 1 | `entry_thunk_7e189f0e` | `call` to the body directly after it (`0x7e189f16`, register-save mask `0xb0`, frame 36) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e189fdb` | 1 | `entry_thunk_7e189fdb` | `call` to the body directly after it (`0x7e189fe3`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18a0c6` | 3 | `entry_thunk_7e18a0c6` | `call` to the body directly after it (`0x7e18a0ce`, register-save mask `0xf0`, frame 216) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18a730` | 1 | `obj_clear_f1452_7e18a730` | `*(this+1452) = 0`. | pattern scan |
| `0x7e18a76c` | 1 | `entry_thunk_7e18a76c` | `call` to the body directly after it (`0x7e18a774`, register-save mask `0xf0`, frame 64) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18a9e6` | 1 | `entry_thunk_7e18a9e6` | `call` to the body directly after it (`0x7e18a9ee`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18aab9` | 1 | `obj_clear_f584_7e18aab9` | `*(this+584) = 0`. | pattern scan |
| `0x7e18aaf5` | 1 | `entry_thunk_7e18aaf5` | `call` to the body directly after it (`0x7e18aafd`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18ac81` | 2 | `entry_thunk_7e18ac81` | `call` to the body directly after it (`0x7e18ac89`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18ae61` | 2 | `entry_thunk_7e18ae61` | `call` to the body directly after it (`0x7e18ae69`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18aeb8` | 1 | `entry_thunk_7e18aeb8` | `call` to the body directly after it (`0x7e18aec0`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18b00d` | 1 | `entry_thunk_7e18b00d` | `call` to the body directly after it (`0x7e18b015`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18b060` | 2 | `entry_thunk_7e18b060` | `call` to the body directly after it (`0x7e18b068`, register-save mask `0xf0`, frame 84) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18b429` | 2 | `entry_thunk_7e18b429` | `call` to the body directly after it (`0x7e18b431`, register-save mask `0xf0`, frame 108) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18b847` | 1 | `entry_thunk_7e18b847` | `call` to the body directly after it (`0x7e18b84f`, register-save mask `0xf0`, frame 80) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18ba90` | 1 | `entry_thunk_7e18ba90` | `call` to the body directly after it (`0x7e18ba98`, register-save mask `0xb0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18bb58` | 1 | `entry_thunk_7e18bb58` | `call` to the body directly after it (`0x7e18bb60`, register-save mask `0xb0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18bc1f` | 1 | `entry_thunk_7e18bc1f` | `call` to the body directly after it (`0x7e18bc27`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18be67` | 1 | `entry_thunk_7e18be67` | `call` to the body directly after it (`0x7e18be6f`, register-save mask `0xf0`, frame 36) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18bffb` | 2 | `entry_thunk_7e18bffb` | `call` to the body directly after it (`0x7e18c003`, register-save mask `0xf0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18d64e` | 2 | `obj_set1_f252_7e18d64e` | `*(this+252) = 1`. | pattern scan |
| `0x7e18d657` | 1 | `obj_clear_f552_7e18d657` | `*(this+552) = 0`. | pattern scan |
| `0x7e18d69b` | 1 | `entry_thunk_7e18d69b` | `call` to the body directly after it (`0x7e18d6a3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18d6bf` | 2 | `entry_thunk_7e18d6bf` | `call` to the body directly after it (`0x7e18d6c7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18d7f9` | 2 | `entry_thunk_7e18d7f9` | `call` to the body directly after it (`0x7e18d801`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18d90c` | 1 | `entry_thunk_7e18d90c` | `call` to the body directly after it (`0x7e18d914`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18d969` | 1 | `entry_thunk_7e18d969` | `call` to the body directly after it (`0x7e18d971`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18d9be` | 1 | `entry_thunk_7e18d9be` | `call` to the body directly after it (`0x7e18d9c6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18d9e2` | 3 | `entry_thunk_7e18d9e2` | `call` to the body directly after it (`0x7e18d9ea`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18e1b4` | 2 | `obj_clear_f952_7e18e1b4` | `*(this+952) = 0`. | pattern scan |
| `0x7e18e1fb` | 1 | `entry_thunk_7e18e1fb` | `call` to the body directly after it (`0x7e18e203`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18e260` | 2 | `obj_clear_f956_7e18e260` | `*(this+956) = 0`. | pattern scan |
| `0x7e18e2a7` | 1 | `entry_thunk_7e18e2a7` | `call` to the body directly after it (`0x7e18e2af`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18e2cb` | 1 | `entry_thunk_7e18e2cb` | `call` to the body directly after it (`0x7e18e2d3`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18e584` | 2 | `obj_clear_f1244_7e18e584` | `*(this+1244) = 0`. | pattern scan |
| `0x7e18e5cb` | 1 | `entry_thunk_7e18e5cb` | `call` to the body directly after it (`0x7e18e5d3`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18e7bd` | 2 | `obj_clear_f1248_7e18e7bd` | `*(this+1248) = 0`. | pattern scan |
| `0x7e18e804` | 1 | `entry_thunk_7e18e804` | `call` to the body directly after it (`0x7e18e80c`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18ea72` | 2 | `obj_clear_f1252_7e18ea72` | `*(this+1252) = 0`. | pattern scan |
| `0x7e18eab9` | 1 | `entry_thunk_7e18eab9` | `call` to the body directly after it (`0x7e18eac1`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18ed14` | 2 | `obj_clear_f1256_7e18ed14` | `*(this+1256) = 0`. | pattern scan |
| `0x7e18ed5b` | 1 | `entry_thunk_7e18ed5b` | `call` to the body directly after it (`0x7e18ed63`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18ef6a` | 2 | `obj_clear_f1260_7e18ef6a` | `*(this+1260) = 0`. | pattern scan |
| `0x7e18efb1` | 1 | `entry_thunk_7e18efb1` | `call` to the body directly after it (`0x7e18efb9`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18f096` | 2 | `obj_clear_f1264_7e18f096` | `*(this+1264) = 0`. | pattern scan |
| `0x7e18f0dd` | 1 | `entry_thunk_7e18f0dd` | `call` to the body directly after it (`0x7e18f0e5`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18f204` | 2 | `obj_clear_f1268_7e18f204` | `*(this+1268) = 0`. | pattern scan |
| `0x7e18f24b` | 1 | `entry_thunk_7e18f24b` | `call` to the body directly after it (`0x7e18f253`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18f316` | 1 | `entry_thunk_7e18f316` | `call` to the body directly after it (`0x7e18f31e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18f377` | 2 | `obj_clear_f1272_7e18f377` | `*(this+1272) = 0`. | pattern scan |
| `0x7e18f3be` | 1 | `entry_thunk_7e18f3be` | `call` to the body directly after it (`0x7e18f3c6`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18f4a7` | 2 | `obj_clear_f960_7e18f4a7` | `*(this+960) = 0`. | pattern scan |
| `0x7e18f4ee` | 1 | `entry_thunk_7e18f4ee` | `call` to the body directly after it (`0x7e18f4f6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18f520` | 2 | `obj_clear_f964_7e18f520` | `*(this+964) = 0`. | pattern scan |
| `0x7e18f567` | 1 | `entry_thunk_7e18f567` | `call` to the body directly after it (`0x7e18f56f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18f599` | 2 | `obj_clear_f968_7e18f599` | `*(this+968) = 0`. | pattern scan |
| `0x7e18f5e0` | 1 | `entry_thunk_7e18f5e0` | `call` to the body directly after it (`0x7e18f5e8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18f612` | 2 | `obj_clear_f972_7e18f612` | `*(this+972) = 0`. | pattern scan |
| `0x7e18f659` | 1 | `entry_thunk_7e18f659` | `call` to the body directly after it (`0x7e18f661`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18f68b` | 2 | `obj_clear_f976_7e18f68b` | `*(this+976) = 0`. | pattern scan |
| `0x7e18f6d2` | 1 | `entry_thunk_7e18f6d2` | `call` to the body directly after it (`0x7e18f6da`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18f704` | 2 | `obj_clear_f980_7e18f704` | `*(this+980) = 0`. | pattern scan |
| `0x7e18f74b` | 1 | `entry_thunk_7e18f74b` | `call` to the body directly after it (`0x7e18f753`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18f77d` | 2 | `obj_clear_f984_7e18f77d` | `*(this+984) = 0`. | pattern scan |
| `0x7e18f7c4` | 1 | `entry_thunk_7e18f7c4` | `call` to the body directly after it (`0x7e18f7cc`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18f7f6` | 2 | `obj_clear_f988_7e18f7f6` | `*(this+988) = 0`. | pattern scan |
| `0x7e18f83d` | 1 | `entry_thunk_7e18f83d` | `call` to the body directly after it (`0x7e18f845`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18f86f` | 2 | `obj_clear_f992_7e18f86f` | `*(this+992) = 0`. | pattern scan |
| `0x7e18f8b6` | 1 | `entry_thunk_7e18f8b6` | `call` to the body directly after it (`0x7e18f8be`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18f8e8` | 2 | `obj_clear_f996_7e18f8e8` | `*(this+996) = 0`. | pattern scan |
| `0x7e18f92f` | 1 | `entry_thunk_7e18f92f` | `call` to the body directly after it (`0x7e18f937`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18f961` | 2 | `obj_clear_f1000_7e18f961` | `*(this+1000) = 0`. | pattern scan |
| `0x7e18f9a8` | 1 | `entry_thunk_7e18f9a8` | `call` to the body directly after it (`0x7e18f9b0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18faa8` | 2 | `obj_clear_f1004_7e18faa8` | `*(this+1004) = 0`. | pattern scan |
| `0x7e18faef` | 1 | `entry_thunk_7e18faef` | `call` to the body directly after it (`0x7e18faf7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18fb21` | 2 | `obj_clear_f1008_7e18fb21` | `*(this+1008) = 0`. | pattern scan |
| `0x7e18fb68` | 1 | `entry_thunk_7e18fb68` | `call` to the body directly after it (`0x7e18fb70`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18fbef` | 1 | `entry_thunk_7e18fbef` | `call` to the body directly after it (`0x7e18fbf7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18fc21` | 2 | `obj_clear_f1016_7e18fc21` | `*(this+1016) = 0`. | pattern scan |
| `0x7e18fc68` | 1 | `entry_thunk_7e18fc68` | `call` to the body directly after it (`0x7e18fc70`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18fc9a` | 2 | `obj_clear_f1020_7e18fc9a` | `*(this+1020) = 0`. | pattern scan |
| `0x7e18fce1` | 1 | `entry_thunk_7e18fce1` | `call` to the body directly after it (`0x7e18fce9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e18fd05` | 1 | `entry_thunk_7e18fd05` | `call` to the body directly after it (`0x7e18fd0d`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19e7d2` | 1 | `obj_clear_f552_7e19e7d2` | `*(this+552) = 0`. | pattern scan |
| `0x7e19e817` | 1 | `entry_thunk_7e19e817` | `call` to the body directly after it (`0x7e19e81f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19e83b` | 2 | `entry_thunk_7e19e83b` | `call` to the body directly after it (`0x7e19e843`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19e979` | 2 | `entry_thunk_7e19e979` | `call` to the body directly after it (`0x7e19e981`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19ea93` | 1 | `entry_thunk_7e19ea93` | `call` to the body directly after it (`0x7e19ea9b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19eaf0` | 1 | `entry_thunk_7e19eaf0` | `call` to the body directly after it (`0x7e19eaf8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19eb45` | 1 | `entry_thunk_7e19eb45` | `call` to the body directly after it (`0x7e19eb4d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19eb69` | 3 | `entry_thunk_7e19eb69` | `call` to the body directly after it (`0x7e19eb71`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19f2ec` | 2 | `obj_clear_f952_7e19f2ec` | `*(this+952) = 0`. | pattern scan |
| `0x7e19f333` | 1 | `entry_thunk_7e19f333` | `call` to the body directly after it (`0x7e19f33b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19f394` | 2 | `obj_clear_f956_7e19f394` | `*(this+956) = 0`. | pattern scan |
| `0x7e19f3db` | 1 | `entry_thunk_7e19f3db` | `call` to the body directly after it (`0x7e19f3e3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19f3fd` | 1 | `entry_thunk_7e19f3fd` | `call` to the body directly after it (`0x7e19f405`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19f5f0` | 2 | `obj_clear_f960_7e19f5f0` | `*(this+960) = 0`. | pattern scan |
| `0x7e19f637` | 1 | `entry_thunk_7e19f637` | `call` to the body directly after it (`0x7e19f63f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19f667` | 2 | `obj_clear_f964_7e19f667` | `*(this+964) = 0`. | pattern scan |
| `0x7e19f6ae` | 1 | `entry_thunk_7e19f6ae` | `call` to the body directly after it (`0x7e19f6b6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19f6de` | 2 | `obj_clear_f968_7e19f6de` | `*(this+968) = 0`. | pattern scan |
| `0x7e19f725` | 1 | `entry_thunk_7e19f725` | `call` to the body directly after it (`0x7e19f72d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19f755` | 2 | `obj_clear_f972_7e19f755` | `*(this+972) = 0`. | pattern scan |
| `0x7e19f79c` | 1 | `entry_thunk_7e19f79c` | `call` to the body directly after it (`0x7e19f7a4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19f7cf` | 2 | `obj_clear_f976_7e19f7cf` | `*(this+976) = 0`. | pattern scan |
| `0x7e19f816` | 1 | `entry_thunk_7e19f816` | `call` to the body directly after it (`0x7e19f81e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19f846` | 2 | `obj_clear_f980_7e19f846` | `*(this+980) = 0`. | pattern scan |
| `0x7e19f88d` | 1 | `entry_thunk_7e19f88d` | `call` to the body directly after it (`0x7e19f895`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19f8c0` | 2 | `obj_clear_f984_7e19f8c0` | `*(this+984) = 0`. | pattern scan |
| `0x7e19f907` | 1 | `entry_thunk_7e19f907` | `call` to the body directly after it (`0x7e19f90f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19f93a` | 2 | `obj_clear_f988_7e19f93a` | `*(this+988) = 0`. | pattern scan |
| `0x7e19f981` | 1 | `entry_thunk_7e19f981` | `call` to the body directly after it (`0x7e19f989`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19f9b4` | 2 | `obj_clear_f992_7e19f9b4` | `*(this+992) = 0`. | pattern scan |
| `0x7e19f9fb` | 1 | `entry_thunk_7e19f9fb` | `call` to the body directly after it (`0x7e19fa03`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19fa2b` | 2 | `obj_clear_f996_7e19fa2b` | `*(this+996) = 0`. | pattern scan |
| `0x7e19fa72` | 1 | `entry_thunk_7e19fa72` | `call` to the body directly after it (`0x7e19fa7a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19faa2` | 2 | `obj_clear_f1000_7e19faa2` | `*(this+1000) = 0`. | pattern scan |
| `0x7e19fae9` | 1 | `entry_thunk_7e19fae9` | `call` to the body directly after it (`0x7e19faf1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19fbe9` | 2 | `obj_clear_f1004_7e19fbe9` | `*(this+1004) = 0`. | pattern scan |
| `0x7e19fc30` | 1 | `entry_thunk_7e19fc30` | `call` to the body directly after it (`0x7e19fc38`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19fc63` | 2 | `obj_clear_f1008_7e19fc63` | `*(this+1008) = 0`. | pattern scan |
| `0x7e19fcaa` | 1 | `entry_thunk_7e19fcaa` | `call` to the body directly after it (`0x7e19fcb2`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19fd30` | 1 | `entry_thunk_7e19fd30` | `call` to the body directly after it (`0x7e19fd38`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19fd63` | 2 | `obj_clear_f1016_7e19fd63` | `*(this+1016) = 0`. | pattern scan |
| `0x7e19fdaa` | 1 | `entry_thunk_7e19fdaa` | `call` to the body directly after it (`0x7e19fdb2`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19fdda` | 2 | `obj_clear_f1020_7e19fdda` | `*(this+1020) = 0`. | pattern scan |
| `0x7e19fe21` | 1 | `entry_thunk_7e19fe21` | `call` to the body directly after it (`0x7e19fe29`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e19fe43` | 1 | `entry_thunk_7e19fe43` | `call` to the body directly after it (`0x7e19fe4b`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a08db` | 2 | `obj_set1_f252_7e1a08db` | `*(this+252) = 1`. | pattern scan |
| `0x7e1a08e4` | 1 | `obj_clear_f552_7e1a08e4` | `*(this+552) = 0`. | pattern scan |
| `0x7e1a0928` | 1 | `entry_thunk_7e1a0928` | `call` to the body directly after it (`0x7e1a0930`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a094c` | 2 | `entry_thunk_7e1a094c` | `call` to the body directly after it (`0x7e1a0954`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a0a86` | 2 | `entry_thunk_7e1a0a86` | `call` to the body directly after it (`0x7e1a0a8e`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a0b99` | 1 | `entry_thunk_7e1a0b99` | `call` to the body directly after it (`0x7e1a0ba1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a0bf6` | 1 | `entry_thunk_7e1a0bf6` | `call` to the body directly after it (`0x7e1a0bfe`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a0c4b` | 1 | `entry_thunk_7e1a0c4b` | `call` to the body directly after it (`0x7e1a0c53`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a0c6f` | 3 | `entry_thunk_7e1a0c6f` | `call` to the body directly after it (`0x7e1a0c77`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a142a` | 2 | `obj_clear_f952_7e1a142a` | `*(this+952) = 0`. | pattern scan |
| `0x7e1a1471` | 1 | `entry_thunk_7e1a1471` | `call` to the body directly after it (`0x7e1a1479`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a14d2` | 2 | `obj_clear_f956_7e1a14d2` | `*(this+956) = 0`. | pattern scan |
| `0x7e1a1519` | 1 | `entry_thunk_7e1a1519` | `call` to the body directly after it (`0x7e1a1521`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a153b` | 1 | `entry_thunk_7e1a153b` | `call` to the body directly after it (`0x7e1a1543`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a17b2` | 2 | `obj_clear_f960_7e1a17b2` | `*(this+960) = 0`. | pattern scan |
| `0x7e1a17f9` | 1 | `entry_thunk_7e1a17f9` | `call` to the body directly after it (`0x7e1a1801`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a1829` | 2 | `obj_clear_f964_7e1a1829` | `*(this+964) = 0`. | pattern scan |
| `0x7e1a1870` | 1 | `entry_thunk_7e1a1870` | `call` to the body directly after it (`0x7e1a1878`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a18a0` | 2 | `obj_clear_f968_7e1a18a0` | `*(this+968) = 0`. | pattern scan |
| `0x7e1a18e7` | 1 | `entry_thunk_7e1a18e7` | `call` to the body directly after it (`0x7e1a18ef`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a1917` | 2 | `obj_clear_f972_7e1a1917` | `*(this+972) = 0`. | pattern scan |
| `0x7e1a195e` | 1 | `entry_thunk_7e1a195e` | `call` to the body directly after it (`0x7e1a1966`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a1990` | 2 | `obj_clear_f976_7e1a1990` | `*(this+976) = 0`. | pattern scan |
| `0x7e1a19d7` | 1 | `entry_thunk_7e1a19d7` | `call` to the body directly after it (`0x7e1a19df`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a1a07` | 2 | `obj_clear_f980_7e1a1a07` | `*(this+980) = 0`. | pattern scan |
| `0x7e1a1a4e` | 1 | `entry_thunk_7e1a1a4e` | `call` to the body directly after it (`0x7e1a1a56`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a1a80` | 2 | `obj_clear_f984_7e1a1a80` | `*(this+984) = 0`. | pattern scan |
| `0x7e1a1ac7` | 1 | `entry_thunk_7e1a1ac7` | `call` to the body directly after it (`0x7e1a1acf`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a1af9` | 2 | `obj_clear_f988_7e1a1af9` | `*(this+988) = 0`. | pattern scan |
| `0x7e1a1b40` | 1 | `entry_thunk_7e1a1b40` | `call` to the body directly after it (`0x7e1a1b48`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a1b72` | 2 | `obj_clear_f992_7e1a1b72` | `*(this+992) = 0`. | pattern scan |
| `0x7e1a1bb9` | 1 | `entry_thunk_7e1a1bb9` | `call` to the body directly after it (`0x7e1a1bc1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a1be9` | 2 | `obj_clear_f996_7e1a1be9` | `*(this+996) = 0`. | pattern scan |
| `0x7e1a1c30` | 1 | `entry_thunk_7e1a1c30` | `call` to the body directly after it (`0x7e1a1c38`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a1c62` | 2 | `obj_clear_f1000_7e1a1c62` | `*(this+1000) = 0`. | pattern scan |
| `0x7e1a1ca9` | 1 | `entry_thunk_7e1a1ca9` | `call` to the body directly after it (`0x7e1a1cb1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a1dad` | 2 | `obj_clear_f1004_7e1a1dad` | `*(this+1004) = 0`. | pattern scan |
| `0x7e1a1df4` | 1 | `entry_thunk_7e1a1df4` | `call` to the body directly after it (`0x7e1a1dfc`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a1e24` | 2 | `obj_clear_f1024_7e1a1e24` | `*(this+1024) = 0`. | pattern scan |
| `0x7e1a1e6b` | 1 | `entry_thunk_7e1a1e6b` | `call` to the body directly after it (`0x7e1a1e73`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a2059` | 2 | `obj_clear_f1028_7e1a2059` | `*(this+1028) = 0`. | pattern scan |
| `0x7e1a20a0` | 1 | `entry_thunk_7e1a20a0` | `call` to the body directly after it (`0x7e1a20a8`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a2151` | 2 | `obj_clear_f1032_7e1a2151` | `*(this+1032) = 0`. | pattern scan |
| `0x7e1a2198` | 1 | `entry_thunk_7e1a2198` | `call` to the body directly after it (`0x7e1a21a0`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a2304` | 2 | `obj_clear_f1036_7e1a2304` | `*(this+1036) = 0`. | pattern scan |
| `0x7e1a234b` | 1 | `entry_thunk_7e1a234b` | `call` to the body directly after it (`0x7e1a2353`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a23fc` | 2 | `obj_clear_f1040_7e1a23fc` | `*(this+1040) = 0`. | pattern scan |
| `0x7e1a2443` | 1 | `entry_thunk_7e1a2443` | `call` to the body directly after it (`0x7e1a244b`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a25e8` | 2 | `obj_clear_f1044_7e1a25e8` | `*(this+1044) = 0`. | pattern scan |
| `0x7e1a262f` | 1 | `entry_thunk_7e1a262f` | `call` to the body directly after it (`0x7e1a2637`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a284c` | 2 | `obj_clear_f1008_7e1a284c` | `*(this+1008) = 0`. | pattern scan |
| `0x7e1a2893` | 1 | `entry_thunk_7e1a2893` | `call` to the body directly after it (`0x7e1a289b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a291a` | 1 | `entry_thunk_7e1a291a` | `call` to the body directly after it (`0x7e1a2922`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a294c` | 2 | `obj_clear_f1016_7e1a294c` | `*(this+1016) = 0`. | pattern scan |
| `0x7e1a2993` | 1 | `entry_thunk_7e1a2993` | `call` to the body directly after it (`0x7e1a299b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a29c5` | 2 | `obj_clear_f1020_7e1a29c5` | `*(this+1020) = 0`. | pattern scan |
| `0x7e1a2a0c` | 1 | `entry_thunk_7e1a2a0c` | `call` to the body directly after it (`0x7e1a2a14`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a2a30` | 1 | `entry_thunk_7e1a2a30` | `call` to the body directly after it (`0x7e1a2a38`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a3154` | 1 | `obj_clear_f552_7e1a3154` | `*(this+552) = 0`. | pattern scan |
| `0x7e1a3199` | 1 | `entry_thunk_7e1a3199` | `call` to the body directly after it (`0x7e1a31a1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a31bd` | 2 | `entry_thunk_7e1a31bd` | `call` to the body directly after it (`0x7e1a31c5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a32fb` | 2 | `entry_thunk_7e1a32fb` | `call` to the body directly after it (`0x7e1a3303`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a3415` | 1 | `entry_thunk_7e1a3415` | `call` to the body directly after it (`0x7e1a341d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a3472` | 1 | `entry_thunk_7e1a3472` | `call` to the body directly after it (`0x7e1a347a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a34c7` | 1 | `entry_thunk_7e1a34c7` | `call` to the body directly after it (`0x7e1a34cf`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a34eb` | 3 | `entry_thunk_7e1a34eb` | `call` to the body directly after it (`0x7e1a34f3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a3c82` | 2 | `obj_clear_f952_7e1a3c82` | `*(this+952) = 0`. | pattern scan |
| `0x7e1a3cc9` | 1 | `entry_thunk_7e1a3cc9` | `call` to the body directly after it (`0x7e1a3cd1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a3d2a` | 2 | `obj_clear_f956_7e1a3d2a` | `*(this+956) = 0`. | pattern scan |
| `0x7e1a3d71` | 1 | `entry_thunk_7e1a3d71` | `call` to the body directly after it (`0x7e1a3d79`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a3d93` | 1 | `entry_thunk_7e1a3d93` | `call` to the body directly after it (`0x7e1a3d9b`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a3f86` | 2 | `obj_clear_f960_7e1a3f86` | `*(this+960) = 0`. | pattern scan |
| `0x7e1a3fcd` | 1 | `entry_thunk_7e1a3fcd` | `call` to the body directly after it (`0x7e1a3fd5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a3fff` | 2 | `obj_clear_f964_7e1a3fff` | `*(this+964) = 0`. | pattern scan |
| `0x7e1a4046` | 1 | `entry_thunk_7e1a4046` | `call` to the body directly after it (`0x7e1a404e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a4078` | 2 | `obj_clear_f968_7e1a4078` | `*(this+968) = 0`. | pattern scan |
| `0x7e1a40bf` | 1 | `entry_thunk_7e1a40bf` | `call` to the body directly after it (`0x7e1a40c7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a40f1` | 2 | `obj_clear_f972_7e1a40f1` | `*(this+972) = 0`. | pattern scan |
| `0x7e1a4138` | 1 | `entry_thunk_7e1a4138` | `call` to the body directly after it (`0x7e1a4140`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a416b` | 2 | `obj_clear_f976_7e1a416b` | `*(this+976) = 0`. | pattern scan |
| `0x7e1a41b2` | 1 | `entry_thunk_7e1a41b2` | `call` to the body directly after it (`0x7e1a41ba`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a41e4` | 2 | `obj_clear_f980_7e1a41e4` | `*(this+980) = 0`. | pattern scan |
| `0x7e1a422b` | 1 | `entry_thunk_7e1a422b` | `call` to the body directly after it (`0x7e1a4233`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a425e` | 2 | `obj_clear_f984_7e1a425e` | `*(this+984) = 0`. | pattern scan |
| `0x7e1a42a5` | 1 | `entry_thunk_7e1a42a5` | `call` to the body directly after it (`0x7e1a42ad`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a42d8` | 2 | `obj_clear_f988_7e1a42d8` | `*(this+988) = 0`. | pattern scan |
| `0x7e1a431f` | 1 | `entry_thunk_7e1a431f` | `call` to the body directly after it (`0x7e1a4327`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a4352` | 2 | `obj_clear_f992_7e1a4352` | `*(this+992) = 0`. | pattern scan |
| `0x7e1a4399` | 1 | `entry_thunk_7e1a4399` | `call` to the body directly after it (`0x7e1a43a1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a43cb` | 2 | `obj_clear_f996_7e1a43cb` | `*(this+996) = 0`. | pattern scan |
| `0x7e1a4412` | 1 | `entry_thunk_7e1a4412` | `call` to the body directly after it (`0x7e1a441a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a4444` | 2 | `obj_clear_f1000_7e1a4444` | `*(this+1000) = 0`. | pattern scan |
| `0x7e1a448b` | 1 | `entry_thunk_7e1a448b` | `call` to the body directly after it (`0x7e1a4493`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a458f` | 2 | `obj_clear_f1004_7e1a458f` | `*(this+1004) = 0`. | pattern scan |
| `0x7e1a45d6` | 1 | `entry_thunk_7e1a45d6` | `call` to the body directly after it (`0x7e1a45de`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a4609` | 2 | `obj_clear_f1008_7e1a4609` | `*(this+1008) = 0`. | pattern scan |
| `0x7e1a4650` | 1 | `entry_thunk_7e1a4650` | `call` to the body directly after it (`0x7e1a4658`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a46d8` | 1 | `entry_thunk_7e1a46d8` | `call` to the body directly after it (`0x7e1a46e0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a470b` | 2 | `obj_clear_f1016_7e1a470b` | `*(this+1016) = 0`. | pattern scan |
| `0x7e1a4752` | 1 | `entry_thunk_7e1a4752` | `call` to the body directly after it (`0x7e1a475a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a4784` | 2 | `obj_clear_f1020_7e1a4784` | `*(this+1020) = 0`. | pattern scan |
| `0x7e1a47cb` | 1 | `entry_thunk_7e1a47cb` | `call` to the body directly after it (`0x7e1a47d3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a47ef` | 1 | `entry_thunk_7e1a47ef` | `call` to the body directly after it (`0x7e1a47f7`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a5a1e` | 1 | `obj_clear_f552_7e1a5a1e` | `*(this+552) = 0`. | pattern scan |
| `0x7e1a5a63` | 1 | `entry_thunk_7e1a5a63` | `call` to the body directly after it (`0x7e1a5a6b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a5a87` | 2 | `entry_thunk_7e1a5a87` | `call` to the body directly after it (`0x7e1a5a8f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a5bc5` | 2 | `entry_thunk_7e1a5bc5` | `call` to the body directly after it (`0x7e1a5bcd`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a5cdf` | 1 | `entry_thunk_7e1a5cdf` | `call` to the body directly after it (`0x7e1a5ce7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a5d3c` | 1 | `entry_thunk_7e1a5d3c` | `call` to the body directly after it (`0x7e1a5d44`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a5d91` | 1 | `entry_thunk_7e1a5d91` | `call` to the body directly after it (`0x7e1a5d99`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a5db5` | 3 | `entry_thunk_7e1a5db5` | `call` to the body directly after it (`0x7e1a5dbd`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a654e` | 2 | `obj_clear_f952_7e1a654e` | `*(this+952) = 0`. | pattern scan |
| `0x7e1a6595` | 1 | `entry_thunk_7e1a6595` | `call` to the body directly after it (`0x7e1a659d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a65fa` | 2 | `obj_clear_f956_7e1a65fa` | `*(this+956) = 0`. | pattern scan |
| `0x7e1a6641` | 1 | `entry_thunk_7e1a6641` | `call` to the body directly after it (`0x7e1a6649`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a6665` | 1 | `entry_thunk_7e1a6665` | `call` to the body directly after it (`0x7e1a666d`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a6858` | 2 | `obj_clear_f960_7e1a6858` | `*(this+960) = 0`. | pattern scan |
| `0x7e1a689f` | 1 | `entry_thunk_7e1a689f` | `call` to the body directly after it (`0x7e1a68a7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a68d1` | 2 | `obj_clear_f964_7e1a68d1` | `*(this+964) = 0`. | pattern scan |
| `0x7e1a6918` | 1 | `entry_thunk_7e1a6918` | `call` to the body directly after it (`0x7e1a6920`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a694a` | 2 | `obj_clear_f968_7e1a694a` | `*(this+968) = 0`. | pattern scan |
| `0x7e1a6991` | 1 | `entry_thunk_7e1a6991` | `call` to the body directly after it (`0x7e1a6999`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a69c3` | 2 | `obj_clear_f972_7e1a69c3` | `*(this+972) = 0`. | pattern scan |
| `0x7e1a6a0a` | 1 | `entry_thunk_7e1a6a0a` | `call` to the body directly after it (`0x7e1a6a12`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a6a3d` | 2 | `obj_clear_f976_7e1a6a3d` | `*(this+976) = 0`. | pattern scan |
| `0x7e1a6a84` | 1 | `entry_thunk_7e1a6a84` | `call` to the body directly after it (`0x7e1a6a8c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a6ab6` | 2 | `obj_clear_f980_7e1a6ab6` | `*(this+980) = 0`. | pattern scan |
| `0x7e1a6afd` | 1 | `entry_thunk_7e1a6afd` | `call` to the body directly after it (`0x7e1a6b05`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a6b30` | 2 | `obj_clear_f984_7e1a6b30` | `*(this+984) = 0`. | pattern scan |
| `0x7e1a6b77` | 1 | `entry_thunk_7e1a6b77` | `call` to the body directly after it (`0x7e1a6b7f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a6baa` | 2 | `obj_clear_f988_7e1a6baa` | `*(this+988) = 0`. | pattern scan |
| `0x7e1a6bf1` | 1 | `entry_thunk_7e1a6bf1` | `call` to the body directly after it (`0x7e1a6bf9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a6c24` | 2 | `obj_clear_f992_7e1a6c24` | `*(this+992) = 0`. | pattern scan |
| `0x7e1a6c6b` | 1 | `entry_thunk_7e1a6c6b` | `call` to the body directly after it (`0x7e1a6c73`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a6c9d` | 2 | `obj_clear_f996_7e1a6c9d` | `*(this+996) = 0`. | pattern scan |
| `0x7e1a6ce4` | 1 | `entry_thunk_7e1a6ce4` | `call` to the body directly after it (`0x7e1a6cec`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a6d16` | 2 | `obj_clear_f1000_7e1a6d16` | `*(this+1000) = 0`. | pattern scan |
| `0x7e1a6d5d` | 1 | `entry_thunk_7e1a6d5d` | `call` to the body directly after it (`0x7e1a6d65`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a6e61` | 2 | `obj_clear_f1004_7e1a6e61` | `*(this+1004) = 0`. | pattern scan |
| `0x7e1a6ea8` | 1 | `entry_thunk_7e1a6ea8` | `call` to the body directly after it (`0x7e1a6eb0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a6edb` | 2 | `obj_clear_f1008_7e1a6edb` | `*(this+1008) = 0`. | pattern scan |
| `0x7e1a6f22` | 1 | `entry_thunk_7e1a6f22` | `call` to the body directly after it (`0x7e1a6f2a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a6faa` | 1 | `entry_thunk_7e1a6faa` | `call` to the body directly after it (`0x7e1a6fb2`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a6fdd` | 2 | `obj_clear_f1016_7e1a6fdd` | `*(this+1016) = 0`. | pattern scan |
| `0x7e1a7024` | 1 | `entry_thunk_7e1a7024` | `call` to the body directly after it (`0x7e1a702c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a7056` | 2 | `obj_clear_f1020_7e1a7056` | `*(this+1020) = 0`. | pattern scan |
| `0x7e1a709d` | 1 | `entry_thunk_7e1a709d` | `call` to the body directly after it (`0x7e1a70a5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a70c1` | 1 | `entry_thunk_7e1a70c1` | `call` to the body directly after it (`0x7e1a70c9`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a866b` | 2 | `obj_set1_f252_7e1a866b` | `*(this+252) = 1`. | pattern scan |
| `0x7e1a8674` | 1 | `obj_clear_f552_7e1a8674` | `*(this+552) = 0`. | pattern scan |
| `0x7e1a86b8` | 1 | `entry_thunk_7e1a86b8` | `call` to the body directly after it (`0x7e1a86c0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a86dc` | 2 | `entry_thunk_7e1a86dc` | `call` to the body directly after it (`0x7e1a86e4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a8816` | 2 | `entry_thunk_7e1a8816` | `call` to the body directly after it (`0x7e1a881e`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a8929` | 1 | `entry_thunk_7e1a8929` | `call` to the body directly after it (`0x7e1a8931`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a8986` | 1 | `entry_thunk_7e1a8986` | `call` to the body directly after it (`0x7e1a898e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a89db` | 1 | `entry_thunk_7e1a89db` | `call` to the body directly after it (`0x7e1a89e3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a89ff` | 3 | `entry_thunk_7e1a89ff` | `call` to the body directly after it (`0x7e1a8a07`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a9240` | 2 | `obj_clear_f952_7e1a9240` | `*(this+952) = 0`. | pattern scan |
| `0x7e1a9287` | 1 | `entry_thunk_7e1a9287` | `call` to the body directly after it (`0x7e1a928f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a92ec` | 2 | `obj_clear_f956_7e1a92ec` | `*(this+956) = 0`. | pattern scan |
| `0x7e1a9333` | 1 | `entry_thunk_7e1a9333` | `call` to the body directly after it (`0x7e1a933b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a9357` | 1 | `entry_thunk_7e1a9357` | `call` to the body directly after it (`0x7e1a935f`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a96c0` | 2 | `obj_clear_f1136_7e1a96c0` | `*(this+1136) = 0`. | pattern scan |
| `0x7e1a9707` | 1 | `entry_thunk_7e1a9707` | `call` to the body directly after it (`0x7e1a970f`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a9a07` | 2 | `obj_clear_f1140_7e1a9a07` | `*(this+1140) = 0`. | pattern scan |
| `0x7e1a9a4e` | 1 | `entry_thunk_7e1a9a4e` | `call` to the body directly after it (`0x7e1a9a56`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a9b0b` | 2 | `obj_clear_f1144_7e1a9b0b` | `*(this+1144) = 0`. | pattern scan |
| `0x7e1a9b52` | 1 | `entry_thunk_7e1a9b52` | `call` to the body directly after it (`0x7e1a9b5a`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a9c0d` | 2 | `obj_clear_f1148_7e1a9c0d` | `*(this+1148) = 0`. | pattern scan |
| `0x7e1a9c54` | 1 | `entry_thunk_7e1a9c54` | `call` to the body directly after it (`0x7e1a9c5c`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1a9eea` | 2 | `obj_clear_f1152_7e1a9eea` | `*(this+1152) = 0`. | pattern scan |
| `0x7e1a9f31` | 1 | `entry_thunk_7e1a9f31` | `call` to the body directly after it (`0x7e1a9f39`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1aa1c7` | 2 | `obj_clear_f1156_7e1aa1c7` | `*(this+1156) = 0`. | pattern scan |
| `0x7e1aa20e` | 1 | `entry_thunk_7e1aa20e` | `call` to the body directly after it (`0x7e1aa216`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1aa326` | 2 | `obj_clear_f1160_7e1aa326` | `*(this+1160) = 0`. | pattern scan |
| `0x7e1aa36d` | 1 | `entry_thunk_7e1aa36d` | `call` to the body directly after it (`0x7e1aa375`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1aa41a` | 2 | `obj_clear_f1164_7e1aa41a` | `*(this+1164) = 0`. | pattern scan |
| `0x7e1aa461` | 1 | `entry_thunk_7e1aa461` | `call` to the body directly after it (`0x7e1aa469`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1aa775` | 2 | `obj_clear_f1168_7e1aa775` | `*(this+1168) = 0`. | pattern scan |
| `0x7e1aa7bc` | 1 | `entry_thunk_7e1aa7bc` | `call` to the body directly after it (`0x7e1aa7c4`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1aa8bc` | 2 | `obj_clear_f1172_7e1aa8bc` | `*(this+1172) = 0`. | pattern scan |
| `0x7e1aa903` | 1 | `entry_thunk_7e1aa903` | `call` to the body directly after it (`0x7e1aa90b`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1aaa23` | 2 | `obj_clear_f1176_7e1aaa23` | `*(this+1176) = 0`. | pattern scan |
| `0x7e1aaa6a` | 1 | `entry_thunk_7e1aaa6a` | `call` to the body directly after it (`0x7e1aaa72`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1aab72` | 2 | `obj_clear_f1180_7e1aab72` | `*(this+1180) = 0`. | pattern scan |
| `0x7e1aabb9` | 1 | `entry_thunk_7e1aabb9` | `call` to the body directly after it (`0x7e1aabc1`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1aaf03` | 1 | `entry_thunk_7e1aaf03` | `call` to the body directly after it (`0x7e1aaf0b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1aaf64` | 2 | `obj_clear_f1184_7e1aaf64` | `*(this+1184) = 0`. | pattern scan |
| `0x7e1aafab` | 1 | `entry_thunk_7e1aafab` | `call` to the body directly after it (`0x7e1aafb3`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ab28f` | 2 | `obj_clear_f1188_7e1ab28f` | `*(this+1188) = 0`. | pattern scan |
| `0x7e1ab2d6` | 1 | `entry_thunk_7e1ab2d6` | `call` to the body directly after it (`0x7e1ab2de`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ab5eb` | 2 | `obj_clear_f1192_7e1ab5eb` | `*(this+1192) = 0`. | pattern scan |
| `0x7e1ab632` | 1 | `entry_thunk_7e1ab632` | `call` to the body directly after it (`0x7e1ab63a`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ab80b` | 2 | `obj_clear_f1196_7e1ab80b` | `*(this+1196) = 0`. | pattern scan |
| `0x7e1ab852` | 1 | `entry_thunk_7e1ab852` | `call` to the body directly after it (`0x7e1ab85a`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ab908` | 2 | `obj_clear_f960_7e1ab908` | `*(this+960) = 0`. | pattern scan |
| `0x7e1ab94f` | 1 | `entry_thunk_7e1ab94f` | `call` to the body directly after it (`0x7e1ab957`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ab981` | 2 | `obj_clear_f964_7e1ab981` | `*(this+964) = 0`. | pattern scan |
| `0x7e1ab9c8` | 1 | `entry_thunk_7e1ab9c8` | `call` to the body directly after it (`0x7e1ab9d0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ab9fa` | 2 | `obj_clear_f968_7e1ab9fa` | `*(this+968) = 0`. | pattern scan |
| `0x7e1aba41` | 1 | `entry_thunk_7e1aba41` | `call` to the body directly after it (`0x7e1aba49`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1aba73` | 2 | `obj_clear_f972_7e1aba73` | `*(this+972) = 0`. | pattern scan |
| `0x7e1ababa` | 1 | `entry_thunk_7e1ababa` | `call` to the body directly after it (`0x7e1abac2`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1abaec` | 2 | `obj_clear_f976_7e1abaec` | `*(this+976) = 0`. | pattern scan |
| `0x7e1abb33` | 1 | `entry_thunk_7e1abb33` | `call` to the body directly after it (`0x7e1abb3b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1abb65` | 2 | `obj_clear_f980_7e1abb65` | `*(this+980) = 0`. | pattern scan |
| `0x7e1abbac` | 1 | `entry_thunk_7e1abbac` | `call` to the body directly after it (`0x7e1abbb4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1abbde` | 2 | `obj_clear_f984_7e1abbde` | `*(this+984) = 0`. | pattern scan |
| `0x7e1abc25` | 1 | `entry_thunk_7e1abc25` | `call` to the body directly after it (`0x7e1abc2d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1abc57` | 2 | `obj_clear_f988_7e1abc57` | `*(this+988) = 0`. | pattern scan |
| `0x7e1abc9e` | 1 | `entry_thunk_7e1abc9e` | `call` to the body directly after it (`0x7e1abca6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1abcd0` | 2 | `obj_clear_f992_7e1abcd0` | `*(this+992) = 0`. | pattern scan |
| `0x7e1abd17` | 1 | `entry_thunk_7e1abd17` | `call` to the body directly after it (`0x7e1abd1f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1abd49` | 2 | `obj_clear_f996_7e1abd49` | `*(this+996) = 0`. | pattern scan |
| `0x7e1abd90` | 1 | `entry_thunk_7e1abd90` | `call` to the body directly after it (`0x7e1abd98`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1abdc2` | 2 | `obj_clear_f1000_7e1abdc2` | `*(this+1000) = 0`. | pattern scan |
| `0x7e1abe09` | 1 | `entry_thunk_7e1abe09` | `call` to the body directly after it (`0x7e1abe11`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1abf0d` | 2 | `obj_clear_f1004_7e1abf0d` | `*(this+1004) = 0`. | pattern scan |
| `0x7e1abf54` | 1 | `entry_thunk_7e1abf54` | `call` to the body directly after it (`0x7e1abf5c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1abf86` | 2 | `obj_clear_f1008_7e1abf86` | `*(this+1008) = 0`. | pattern scan |
| `0x7e1abfcd` | 1 | `entry_thunk_7e1abfcd` | `call` to the body directly after it (`0x7e1abfd5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ac054` | 1 | `entry_thunk_7e1ac054` | `call` to the body directly after it (`0x7e1ac05c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ac086` | 2 | `obj_clear_f1016_7e1ac086` | `*(this+1016) = 0`. | pattern scan |
| `0x7e1ac0cd` | 1 | `entry_thunk_7e1ac0cd` | `call` to the body directly after it (`0x7e1ac0d5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ac0ff` | 2 | `obj_clear_f1020_7e1ac0ff` | `*(this+1020) = 0`. | pattern scan |
| `0x7e1ac146` | 1 | `entry_thunk_7e1ac146` | `call` to the body directly after it (`0x7e1ac14e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ac16a` | 1 | `entry_thunk_7e1ac16a` | `call` to the body directly after it (`0x7e1ac172`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ad412` | 2 | `obj_set1_f252_7e1ad412` | `*(this+252) = 1`. | pattern scan |
| `0x7e1ad41b` | 1 | `obj_clear_f552_7e1ad41b` | `*(this+552) = 0`. | pattern scan |
| `0x7e1ad45f` | 1 | `entry_thunk_7e1ad45f` | `call` to the body directly after it (`0x7e1ad467`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ad483` | 2 | `entry_thunk_7e1ad483` | `call` to the body directly after it (`0x7e1ad48b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ad5bd` | 2 | `entry_thunk_7e1ad5bd` | `call` to the body directly after it (`0x7e1ad5c5`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ad6d0` | 1 | `entry_thunk_7e1ad6d0` | `call` to the body directly after it (`0x7e1ad6d8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ad72d` | 1 | `entry_thunk_7e1ad72d` | `call` to the body directly after it (`0x7e1ad735`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ad782` | 1 | `entry_thunk_7e1ad782` | `call` to the body directly after it (`0x7e1ad78a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ad7a6` | 3 | `entry_thunk_7e1ad7a6` | `call` to the body directly after it (`0x7e1ad7ae`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ae09f` | 2 | `obj_clear_f952_7e1ae09f` | `*(this+952) = 0`. | pattern scan |
| `0x7e1ae0e6` | 1 | `entry_thunk_7e1ae0e6` | `call` to the body directly after it (`0x7e1ae0ee`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ae14b` | 2 | `obj_clear_f956_7e1ae14b` | `*(this+956) = 0`. | pattern scan |
| `0x7e1ae192` | 1 | `entry_thunk_7e1ae192` | `call` to the body directly after it (`0x7e1ae19a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ae1b6` | 1 | `entry_thunk_7e1ae1b6` | `call` to the body directly after it (`0x7e1ae1be`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ae4af` | 2 | `obj_clear_f1108_7e1ae4af` | `*(this+1108) = 0`. | pattern scan |
| `0x7e1ae4f6` | 1 | `entry_thunk_7e1ae4f6` | `call` to the body directly after it (`0x7e1ae4fe`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ae5cc` | 2 | `obj_clear_f1112_7e1ae5cc` | `*(this+1112) = 0`. | pattern scan |
| `0x7e1ae613` | 1 | `entry_thunk_7e1ae613` | `call` to the body directly after it (`0x7e1ae61b`, register-save mask `0xf0`, frame 72) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ae72f` | 2 | `obj_clear_f1116_7e1ae72f` | `*(this+1116) = 0`. | pattern scan |
| `0x7e1ae776` | 1 | `entry_thunk_7e1ae776` | `call` to the body directly after it (`0x7e1ae77e`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ae89b` | 2 | `obj_clear_f1120_7e1ae89b` | `*(this+1120) = 0`. | pattern scan |
| `0x7e1ae8e2` | 1 | `entry_thunk_7e1ae8e2` | `call` to the body directly after it (`0x7e1ae8ea`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1aea38` | 2 | `obj_clear_f1124_7e1aea38` | `*(this+1124) = 0`. | pattern scan |
| `0x7e1aea7f` | 1 | `entry_thunk_7e1aea7f` | `call` to the body directly after it (`0x7e1aea87`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1aebb7` | 2 | `obj_clear_f1128_7e1aebb7` | `*(this+1128) = 0`. | pattern scan |
| `0x7e1aebfe` | 1 | `entry_thunk_7e1aebfe` | `call` to the body directly after it (`0x7e1aec06`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1aed10` | 2 | `obj_clear_f1132_7e1aed10` | `*(this+1132) = 0`. | pattern scan |
| `0x7e1aed57` | 1 | `entry_thunk_7e1aed57` | `call` to the body directly after it (`0x7e1aed5f`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1aee7c` | 2 | `obj_clear_f1136_7e1aee7c` | `*(this+1136) = 0`. | pattern scan |
| `0x7e1aeec3` | 1 | `entry_thunk_7e1aeec3` | `call` to the body directly after it (`0x7e1aeecb`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1aefb4` | 2 | `obj_clear_f1140_7e1aefb4` | `*(this+1140) = 0`. | pattern scan |
| `0x7e1aeffb` | 1 | `entry_thunk_7e1aeffb` | `call` to the body directly after it (`0x7e1af003`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1af110` | 2 | `obj_clear_f1144_7e1af110` | `*(this+1144) = 0`. | pattern scan |
| `0x7e1af157` | 1 | `entry_thunk_7e1af157` | `call` to the body directly after it (`0x7e1af15f`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1af26c` | 2 | `obj_clear_f1148_7e1af26c` | `*(this+1148) = 0`. | pattern scan |
| `0x7e1af2b3` | 1 | `entry_thunk_7e1af2b3` | `call` to the body directly after it (`0x7e1af2bb`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1af3c5` | 2 | `obj_clear_f1152_7e1af3c5` | `*(this+1152) = 0`. | pattern scan |
| `0x7e1af40c` | 1 | `entry_thunk_7e1af40c` | `call` to the body directly after it (`0x7e1af414`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1af529` | 2 | `obj_clear_f1156_7e1af529` | `*(this+1156) = 0`. | pattern scan |
| `0x7e1af570` | 1 | `entry_thunk_7e1af570` | `call` to the body directly after it (`0x7e1af578`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1af6ad` | 2 | `obj_clear_f960_7e1af6ad` | `*(this+960) = 0`. | pattern scan |
| `0x7e1af6f4` | 1 | `entry_thunk_7e1af6f4` | `call` to the body directly after it (`0x7e1af6fc`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1af726` | 2 | `obj_clear_f964_7e1af726` | `*(this+964) = 0`. | pattern scan |
| `0x7e1af76d` | 1 | `entry_thunk_7e1af76d` | `call` to the body directly after it (`0x7e1af775`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1af79f` | 2 | `obj_clear_f968_7e1af79f` | `*(this+968) = 0`. | pattern scan |
| `0x7e1af7e6` | 1 | `entry_thunk_7e1af7e6` | `call` to the body directly after it (`0x7e1af7ee`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1af818` | 2 | `obj_clear_f972_7e1af818` | `*(this+972) = 0`. | pattern scan |
| `0x7e1af85f` | 1 | `entry_thunk_7e1af85f` | `call` to the body directly after it (`0x7e1af867`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1af891` | 2 | `obj_clear_f976_7e1af891` | `*(this+976) = 0`. | pattern scan |
| `0x7e1af8d8` | 1 | `entry_thunk_7e1af8d8` | `call` to the body directly after it (`0x7e1af8e0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1af90a` | 2 | `obj_clear_f980_7e1af90a` | `*(this+980) = 0`. | pattern scan |
| `0x7e1af951` | 1 | `entry_thunk_7e1af951` | `call` to the body directly after it (`0x7e1af959`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1af983` | 2 | `obj_clear_f984_7e1af983` | `*(this+984) = 0`. | pattern scan |
| `0x7e1af9ca` | 1 | `entry_thunk_7e1af9ca` | `call` to the body directly after it (`0x7e1af9d2`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1af9fc` | 2 | `obj_clear_f988_7e1af9fc` | `*(this+988) = 0`. | pattern scan |
| `0x7e1afa43` | 1 | `entry_thunk_7e1afa43` | `call` to the body directly after it (`0x7e1afa4b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1afa75` | 2 | `obj_clear_f992_7e1afa75` | `*(this+992) = 0`. | pattern scan |
| `0x7e1afabc` | 1 | `entry_thunk_7e1afabc` | `call` to the body directly after it (`0x7e1afac4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1afaee` | 2 | `obj_clear_f996_7e1afaee` | `*(this+996) = 0`. | pattern scan |
| `0x7e1afb35` | 1 | `entry_thunk_7e1afb35` | `call` to the body directly after it (`0x7e1afb3d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1afb67` | 2 | `obj_clear_f1000_7e1afb67` | `*(this+1000) = 0`. | pattern scan |
| `0x7e1afbae` | 1 | `entry_thunk_7e1afbae` | `call` to the body directly after it (`0x7e1afbb6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1afcb2` | 2 | `obj_clear_f1004_7e1afcb2` | `*(this+1004) = 0`. | pattern scan |
| `0x7e1afcf9` | 1 | `entry_thunk_7e1afcf9` | `call` to the body directly after it (`0x7e1afd01`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1afd2b` | 2 | `obj_clear_f1008_7e1afd2b` | `*(this+1008) = 0`. | pattern scan |
| `0x7e1afd72` | 1 | `entry_thunk_7e1afd72` | `call` to the body directly after it (`0x7e1afd7a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1afdf9` | 1 | `entry_thunk_7e1afdf9` | `call` to the body directly after it (`0x7e1afe01`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1afe2b` | 2 | `obj_clear_f1016_7e1afe2b` | `*(this+1016) = 0`. | pattern scan |
| `0x7e1afe72` | 1 | `entry_thunk_7e1afe72` | `call` to the body directly after it (`0x7e1afe7a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1afea4` | 2 | `obj_clear_f1020_7e1afea4` | `*(this+1020) = 0`. | pattern scan |
| `0x7e1afeeb` | 1 | `entry_thunk_7e1afeeb` | `call` to the body directly after it (`0x7e1afef3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1aff0f` | 1 | `entry_thunk_7e1aff0f` | `call` to the body directly after it (`0x7e1aff17`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b1497` | 2 | `obj_set1_f252_7e1b1497` | `*(this+252) = 1`. | pattern scan |
| `0x7e1b14a0` | 1 | `obj_clear_f552_7e1b14a0` | `*(this+552) = 0`. | pattern scan |
| `0x7e1b14e4` | 1 | `entry_thunk_7e1b14e4` | `call` to the body directly after it (`0x7e1b14ec`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b1508` | 2 | `entry_thunk_7e1b1508` | `call` to the body directly after it (`0x7e1b1510`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b1642` | 2 | `entry_thunk_7e1b1642` | `call` to the body directly after it (`0x7e1b164a`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b1755` | 1 | `entry_thunk_7e1b1755` | `call` to the body directly after it (`0x7e1b175d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b17b2` | 1 | `entry_thunk_7e1b17b2` | `call` to the body directly after it (`0x7e1b17ba`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b1807` | 1 | `entry_thunk_7e1b1807` | `call` to the body directly after it (`0x7e1b180f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b182b` | 3 | `entry_thunk_7e1b182b` | `call` to the body directly after it (`0x7e1b1833`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b1ff8` | 2 | `obj_clear_f952_7e1b1ff8` | `*(this+952) = 0`. | pattern scan |
| `0x7e1b203f` | 1 | `entry_thunk_7e1b203f` | `call` to the body directly after it (`0x7e1b2047`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b20a4` | 2 | `obj_clear_f956_7e1b20a4` | `*(this+956) = 0`. | pattern scan |
| `0x7e1b20eb` | 1 | `entry_thunk_7e1b20eb` | `call` to the body directly after it (`0x7e1b20f3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b210f` | 1 | `entry_thunk_7e1b210f` | `call` to the body directly after it (`0x7e1b2117`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b2394` | 2 | `obj_clear_f8752_7e1b2394` | `*(this+8752) = 0`. | pattern scan |
| `0x7e1b23db` | 1 | `entry_thunk_7e1b23db` | `call` to the body directly after it (`0x7e1b23e3`, register-save mask `0xb0`, frame 36) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b24c0` | 2 | `obj_clear_f8756_7e1b24c0` | `*(this+8756) = 0`. | pattern scan |
| `0x7e1b2507` | 1 | `entry_thunk_7e1b2507` | `call` to the body directly after it (`0x7e1b250f`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b25c2` | 2 | `obj_clear_f8760_7e1b25c2` | `*(this+8760) = 0`. | pattern scan |
| `0x7e1b2609` | 1 | `entry_thunk_7e1b2609` | `call` to the body directly after it (`0x7e1b2611`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b27de` | 1 | `entry_thunk_7e1b27de` | `call` to the body directly after it (`0x7e1b27e6`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b283a` | 1 | `entry_thunk_7e1b283a` | `call` to the body directly after it (`0x7e1b2842`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b298c` | 1 | `entry_thunk_7e1b298c` | `call` to the body directly after it (`0x7e1b2994`, register-save mask `0xa0`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b2a56` | 1 | `entry_thunk_7e1b2a56` | `call` to the body directly after it (`0x7e1b2a5e`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b2b6c` | 2 | `entry_thunk_7e1b2b6c` | `call` to the body directly after it (`0x7e1b2b74`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b2bef` | 1 | `entry_thunk_7e1b2bef` | `call` to the body directly after it (`0x7e1b2bf7`, register-save mask `0xe0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b2ccf` | 1 | `entry_thunk_7e1b2ccf` | `call` to the body directly after it (`0x7e1b2cd7`, register-save mask `0xf0`, frame 56) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b2dd3` | 2 | `obj_clear_f8780_7e1b2dd3` | `*(this+8780) = 0`. | pattern scan |
| `0x7e1b2e1a` | 1 | `entry_thunk_7e1b2e1a` | `call` to the body directly after it (`0x7e1b2e22`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b2ed2` | 2 | `obj_clear_f8784_7e1b2ed2` | `*(this+8784) = 0`. | pattern scan |
| `0x7e1b2f19` | 1 | `entry_thunk_7e1b2f19` | `call` to the body directly after it (`0x7e1b2f21`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b2fe9` | 2 | `obj_clear_f8788_7e1b2fe9` | `*(this+8788) = 0`. | pattern scan |
| `0x7e1b3030` | 1 | `entry_thunk_7e1b3030` | `call` to the body directly after it (`0x7e1b3038`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b318b` | 2 | `obj_clear_f960_7e1b318b` | `*(this+960) = 0`. | pattern scan |
| `0x7e1b31d2` | 1 | `entry_thunk_7e1b31d2` | `call` to the body directly after it (`0x7e1b31da`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b3204` | 2 | `obj_clear_f964_7e1b3204` | `*(this+964) = 0`. | pattern scan |
| `0x7e1b324b` | 1 | `entry_thunk_7e1b324b` | `call` to the body directly after it (`0x7e1b3253`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b327d` | 2 | `obj_clear_f968_7e1b327d` | `*(this+968) = 0`. | pattern scan |
| `0x7e1b32c4` | 1 | `entry_thunk_7e1b32c4` | `call` to the body directly after it (`0x7e1b32cc`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b32f6` | 2 | `obj_clear_f972_7e1b32f6` | `*(this+972) = 0`. | pattern scan |
| `0x7e1b333d` | 1 | `entry_thunk_7e1b333d` | `call` to the body directly after it (`0x7e1b3345`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b336f` | 2 | `obj_clear_f976_7e1b336f` | `*(this+976) = 0`. | pattern scan |
| `0x7e1b33b6` | 1 | `entry_thunk_7e1b33b6` | `call` to the body directly after it (`0x7e1b33be`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b33e8` | 2 | `obj_clear_f980_7e1b33e8` | `*(this+980) = 0`. | pattern scan |
| `0x7e1b342f` | 1 | `entry_thunk_7e1b342f` | `call` to the body directly after it (`0x7e1b3437`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b3461` | 2 | `obj_clear_f984_7e1b3461` | `*(this+984) = 0`. | pattern scan |
| `0x7e1b34a8` | 1 | `entry_thunk_7e1b34a8` | `call` to the body directly after it (`0x7e1b34b0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b34da` | 2 | `obj_clear_f988_7e1b34da` | `*(this+988) = 0`. | pattern scan |
| `0x7e1b3521` | 1 | `entry_thunk_7e1b3521` | `call` to the body directly after it (`0x7e1b3529`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b3553` | 2 | `obj_clear_f992_7e1b3553` | `*(this+992) = 0`. | pattern scan |
| `0x7e1b359a` | 1 | `entry_thunk_7e1b359a` | `call` to the body directly after it (`0x7e1b35a2`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b35cc` | 2 | `obj_clear_f996_7e1b35cc` | `*(this+996) = 0`. | pattern scan |
| `0x7e1b3613` | 1 | `entry_thunk_7e1b3613` | `call` to the body directly after it (`0x7e1b361b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b3645` | 2 | `obj_clear_f1000_7e1b3645` | `*(this+1000) = 0`. | pattern scan |
| `0x7e1b368c` | 1 | `entry_thunk_7e1b368c` | `call` to the body directly after it (`0x7e1b3694`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b3790` | 2 | `obj_clear_f1004_7e1b3790` | `*(this+1004) = 0`. | pattern scan |
| `0x7e1b37d7` | 1 | `entry_thunk_7e1b37d7` | `call` to the body directly after it (`0x7e1b37df`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b3809` | 2 | `obj_clear_f1008_7e1b3809` | `*(this+1008) = 0`. | pattern scan |
| `0x7e1b3850` | 1 | `entry_thunk_7e1b3850` | `call` to the body directly after it (`0x7e1b3858`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b38d7` | 1 | `entry_thunk_7e1b38d7` | `call` to the body directly after it (`0x7e1b38df`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b3909` | 2 | `obj_clear_f1016_7e1b3909` | `*(this+1016) = 0`. | pattern scan |
| `0x7e1b3950` | 1 | `entry_thunk_7e1b3950` | `call` to the body directly after it (`0x7e1b3958`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b3982` | 2 | `obj_clear_f1020_7e1b3982` | `*(this+1020) = 0`. | pattern scan |
| `0x7e1b39c9` | 1 | `entry_thunk_7e1b39c9` | `call` to the body directly after it (`0x7e1b39d1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b39ed` | 1 | `entry_thunk_7e1b39ed` | `call` to the body directly after it (`0x7e1b39f5`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b58ca` | 2 | `obj_set1_f252_7e1b58ca` | `*(this+252) = 1`. | pattern scan |
| `0x7e1b58d3` | 1 | `obj_clear_f552_7e1b58d3` | `*(this+552) = 0`. | pattern scan |
| `0x7e1b5917` | 1 | `entry_thunk_7e1b5917` | `call` to the body directly after it (`0x7e1b591f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b593b` | 2 | `entry_thunk_7e1b593b` | `call` to the body directly after it (`0x7e1b5943`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b5a75` | 2 | `entry_thunk_7e1b5a75` | `call` to the body directly after it (`0x7e1b5a7d`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b5b88` | 1 | `entry_thunk_7e1b5b88` | `call` to the body directly after it (`0x7e1b5b90`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b5be5` | 1 | `entry_thunk_7e1b5be5` | `call` to the body directly after it (`0x7e1b5bed`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b5c3a` | 1 | `entry_thunk_7e1b5c3a` | `call` to the body directly after it (`0x7e1b5c42`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b5c5e` | 3 | `entry_thunk_7e1b5c5e` | `call` to the body directly after it (`0x7e1b5c66`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b6489` | 2 | `obj_clear_f1276_7e1b6489` | `*(this+1276) = 0`. | pattern scan |
| `0x7e1b64d0` | 1 | `entry_thunk_7e1b64d0` | `call` to the body directly after it (`0x7e1b64d8`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b65a7` | 2 | `obj_clear_f952_7e1b65a7` | `*(this+952) = 0`. | pattern scan |
| `0x7e1b65ee` | 1 | `entry_thunk_7e1b65ee` | `call` to the body directly after it (`0x7e1b65f6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b6653` | 2 | `obj_clear_f1280_7e1b6653` | `*(this+1280) = 0`. | pattern scan |
| `0x7e1b669a` | 1 | `entry_thunk_7e1b669a` | `call` to the body directly after it (`0x7e1b66a2`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b6780` | 2 | `obj_clear_f956_7e1b6780` | `*(this+956) = 0`. | pattern scan |
| `0x7e1b67c7` | 1 | `entry_thunk_7e1b67c7` | `call` to the body directly after it (`0x7e1b67cf`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b67f9` | 2 | `obj_clear_f1284_7e1b67f9` | `*(this+1284) = 0`. | pattern scan |
| `0x7e1b6840` | 1 | `entry_thunk_7e1b6840` | `call` to the body directly after it (`0x7e1b6848`, register-save mask `0xb0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b68a4` | 1 | `entry_thunk_7e1b68a4` | `call` to the body directly after it (`0x7e1b68ac`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b6bb5` | 2 | `obj_clear_f1288_7e1b6bb5` | `*(this+1288) = 0`. | pattern scan |
| `0x7e1b6bfc` | 1 | `entry_thunk_7e1b6bfc` | `call` to the body directly after it (`0x7e1b6c04`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b6d70` | 2 | `obj_clear_f1292_7e1b6d70` | `*(this+1292) = 0`. | pattern scan |
| `0x7e1b6db7` | 2 | `entry_thunk_7e1b6db7` | `call` to the body directly after it (`0x7e1b6dbf`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b700d` | 1 | `entry_thunk_7e1b700d` | `call` to the body directly after it (`0x7e1b7015`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b71c0` | 2 | `obj_clear_f960_7e1b71c0` | `*(this+960) = 0`. | pattern scan |
| `0x7e1b7207` | 1 | `entry_thunk_7e1b7207` | `call` to the body directly after it (`0x7e1b720f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b7239` | 2 | `obj_clear_f964_7e1b7239` | `*(this+964) = 0`. | pattern scan |
| `0x7e1b7280` | 1 | `entry_thunk_7e1b7280` | `call` to the body directly after it (`0x7e1b7288`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b72b2` | 2 | `obj_clear_f968_7e1b72b2` | `*(this+968) = 0`. | pattern scan |
| `0x7e1b72f9` | 1 | `entry_thunk_7e1b72f9` | `call` to the body directly after it (`0x7e1b7301`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b732b` | 2 | `obj_clear_f1296_7e1b732b` | `*(this+1296) = 0`. | pattern scan |
| `0x7e1b7372` | 1 | `entry_thunk_7e1b7372` | `call` to the body directly after it (`0x7e1b737a`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b743c` | 2 | `obj_clear_f972_7e1b743c` | `*(this+972) = 0`. | pattern scan |
| `0x7e1b7483` | 1 | `entry_thunk_7e1b7483` | `call` to the body directly after it (`0x7e1b748b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b74b5` | 2 | `obj_clear_f976_7e1b74b5` | `*(this+976) = 0`. | pattern scan |
| `0x7e1b74fc` | 1 | `entry_thunk_7e1b74fc` | `call` to the body directly after it (`0x7e1b7504`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b752e` | 2 | `obj_clear_f1300_7e1b752e` | `*(this+1300) = 0`. | pattern scan |
| `0x7e1b7575` | 1 | `entry_thunk_7e1b7575` | `call` to the body directly after it (`0x7e1b757d`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b7644` | 2 | `obj_clear_f980_7e1b7644` | `*(this+980) = 0`. | pattern scan |
| `0x7e1b768b` | 1 | `entry_thunk_7e1b768b` | `call` to the body directly after it (`0x7e1b7693`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b76bd` | 2 | `obj_clear_f984_7e1b76bd` | `*(this+984) = 0`. | pattern scan |
| `0x7e1b7704` | 1 | `entry_thunk_7e1b7704` | `call` to the body directly after it (`0x7e1b770c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b7736` | 2 | `obj_clear_f1304_7e1b7736` | `*(this+1304) = 0`. | pattern scan |
| `0x7e1b777d` | 1 | `entry_thunk_7e1b777d` | `call` to the body directly after it (`0x7e1b7785`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b784d` | 2 | `obj_clear_f988_7e1b784d` | `*(this+988) = 0`. | pattern scan |
| `0x7e1b7894` | 1 | `entry_thunk_7e1b7894` | `call` to the body directly after it (`0x7e1b789c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b78c6` | 2 | `obj_clear_f992_7e1b78c6` | `*(this+992) = 0`. | pattern scan |
| `0x7e1b790d` | 1 | `entry_thunk_7e1b790d` | `call` to the body directly after it (`0x7e1b7915`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b793f` | 2 | `obj_clear_f996_7e1b793f` | `*(this+996) = 0`. | pattern scan |
| `0x7e1b7986` | 1 | `entry_thunk_7e1b7986` | `call` to the body directly after it (`0x7e1b798e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b79b8` | 2 | `obj_clear_f1308_7e1b79b8` | `*(this+1308) = 0`. | pattern scan |
| `0x7e1b79ff` | 1 | `entry_thunk_7e1b79ff` | `call` to the body directly after it (`0x7e1b7a07`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b7acc` | 2 | `obj_clear_f1312_7e1b7acc` | `*(this+1312) = 0`. | pattern scan |
| `0x7e1b7b13` | 1 | `entry_thunk_7e1b7b13` | `call` to the body directly after it (`0x7e1b7b1b`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b7b81` | 2 | `obj_clear_f1000_7e1b7b81` | `*(this+1000) = 0`. | pattern scan |
| `0x7e1b7bc8` | 1 | `entry_thunk_7e1b7bc8` | `call` to the body directly after it (`0x7e1b7bd0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b7ccc` | 2 | `obj_clear_f1004_7e1b7ccc` | `*(this+1004) = 0`. | pattern scan |
| `0x7e1b7d13` | 1 | `entry_thunk_7e1b7d13` | `call` to the body directly after it (`0x7e1b7d1b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b7d45` | 2 | `obj_clear_f1316_7e1b7d45` | `*(this+1316) = 0`. | pattern scan |
| `0x7e1b7d8c` | 1 | `entry_thunk_7e1b7d8c` | `call` to the body directly after it (`0x7e1b7d94`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b7eb0` | 2 | `obj_clear_f1008_7e1b7eb0` | `*(this+1008) = 0`. | pattern scan |
| `0x7e1b7ef7` | 1 | `entry_thunk_7e1b7ef7` | `call` to the body directly after it (`0x7e1b7eff`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b7f7e` | 1 | `entry_thunk_7e1b7f7e` | `call` to the body directly after it (`0x7e1b7f86`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b7fb0` | 2 | `obj_clear_f1016_7e1b7fb0` | `*(this+1016) = 0`. | pattern scan |
| `0x7e1b7ff7` | 1 | `entry_thunk_7e1b7ff7` | `call` to the body directly after it (`0x7e1b7fff`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b8089` | 1 | `entry_thunk_7e1b8089` | `call` to the body directly after it (`0x7e1b8091`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b81e3` | 2 | `obj_clear_f1020_7e1b81e3` | `*(this+1020) = 0`. | pattern scan |
| `0x7e1b822a` | 1 | `entry_thunk_7e1b822a` | `call` to the body directly after it (`0x7e1b8232`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b825c` | 2 | `obj_clear_f1324_7e1b825c` | `*(this+1324) = 0`. | pattern scan |
| `0x7e1b82a3` | 1 | `entry_thunk_7e1b82a3` | `call` to the body directly after it (`0x7e1b82ab`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1b83cc` | 1 | `entry_thunk_7e1b83cc` | `call` to the body directly after it (`0x7e1b83d4`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1baa1a` | 1 | `obj_clear_f552_7e1baa1a` | `*(this+552) = 0`. | pattern scan |
| `0x7e1baa5f` | 1 | `entry_thunk_7e1baa5f` | `call` to the body directly after it (`0x7e1baa67`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1baa83` | 2 | `entry_thunk_7e1baa83` | `call` to the body directly after it (`0x7e1baa8b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1babc1` | 2 | `entry_thunk_7e1babc1` | `call` to the body directly after it (`0x7e1babc9`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bacdb` | 1 | `entry_thunk_7e1bacdb` | `call` to the body directly after it (`0x7e1bace3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bad38` | 1 | `entry_thunk_7e1bad38` | `call` to the body directly after it (`0x7e1bad40`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bad8d` | 1 | `entry_thunk_7e1bad8d` | `call` to the body directly after it (`0x7e1bad95`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1badb1` | 3 | `entry_thunk_7e1badb1` | `call` to the body directly after it (`0x7e1badb9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bb54a` | 2 | `obj_clear_f952_7e1bb54a` | `*(this+952) = 0`. | pattern scan |
| `0x7e1bb591` | 1 | `entry_thunk_7e1bb591` | `call` to the body directly after it (`0x7e1bb599`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bb5f6` | 2 | `obj_clear_f956_7e1bb5f6` | `*(this+956) = 0`. | pattern scan |
| `0x7e1bb63d` | 1 | `entry_thunk_7e1bb63d` | `call` to the body directly after it (`0x7e1bb645`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bb661` | 1 | `entry_thunk_7e1bb661` | `call` to the body directly after it (`0x7e1bb669`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bb854` | 2 | `obj_clear_f960_7e1bb854` | `*(this+960) = 0`. | pattern scan |
| `0x7e1bb89b` | 1 | `entry_thunk_7e1bb89b` | `call` to the body directly after it (`0x7e1bb8a3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bb8cd` | 2 | `obj_clear_f964_7e1bb8cd` | `*(this+964) = 0`. | pattern scan |
| `0x7e1bb914` | 1 | `entry_thunk_7e1bb914` | `call` to the body directly after it (`0x7e1bb91c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bb946` | 2 | `obj_clear_f968_7e1bb946` | `*(this+968) = 0`. | pattern scan |
| `0x7e1bb98d` | 1 | `entry_thunk_7e1bb98d` | `call` to the body directly after it (`0x7e1bb995`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bb9bf` | 2 | `obj_clear_f972_7e1bb9bf` | `*(this+972) = 0`. | pattern scan |
| `0x7e1bba06` | 1 | `entry_thunk_7e1bba06` | `call` to the body directly after it (`0x7e1bba0e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bba39` | 2 | `obj_clear_f976_7e1bba39` | `*(this+976) = 0`. | pattern scan |
| `0x7e1bba80` | 1 | `entry_thunk_7e1bba80` | `call` to the body directly after it (`0x7e1bba88`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bbab2` | 2 | `obj_clear_f980_7e1bbab2` | `*(this+980) = 0`. | pattern scan |
| `0x7e1bbaf9` | 1 | `entry_thunk_7e1bbaf9` | `call` to the body directly after it (`0x7e1bbb01`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bbb2c` | 2 | `obj_clear_f984_7e1bbb2c` | `*(this+984) = 0`. | pattern scan |
| `0x7e1bbb73` | 1 | `entry_thunk_7e1bbb73` | `call` to the body directly after it (`0x7e1bbb7b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bbba6` | 2 | `obj_clear_f988_7e1bbba6` | `*(this+988) = 0`. | pattern scan |
| `0x7e1bbbed` | 1 | `entry_thunk_7e1bbbed` | `call` to the body directly after it (`0x7e1bbbf5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bbc20` | 2 | `obj_clear_f992_7e1bbc20` | `*(this+992) = 0`. | pattern scan |
| `0x7e1bbc67` | 1 | `entry_thunk_7e1bbc67` | `call` to the body directly after it (`0x7e1bbc6f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bbc99` | 2 | `obj_clear_f996_7e1bbc99` | `*(this+996) = 0`. | pattern scan |
| `0x7e1bbce0` | 1 | `entry_thunk_7e1bbce0` | `call` to the body directly after it (`0x7e1bbce8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bbd12` | 2 | `obj_clear_f1000_7e1bbd12` | `*(this+1000) = 0`. | pattern scan |
| `0x7e1bbd59` | 1 | `entry_thunk_7e1bbd59` | `call` to the body directly after it (`0x7e1bbd61`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bbe5d` | 2 | `obj_clear_f1004_7e1bbe5d` | `*(this+1004) = 0`. | pattern scan |
| `0x7e1bbea4` | 1 | `entry_thunk_7e1bbea4` | `call` to the body directly after it (`0x7e1bbeac`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bbed7` | 2 | `obj_clear_f1008_7e1bbed7` | `*(this+1008) = 0`. | pattern scan |
| `0x7e1bbf1e` | 1 | `entry_thunk_7e1bbf1e` | `call` to the body directly after it (`0x7e1bbf26`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bbfa6` | 1 | `entry_thunk_7e1bbfa6` | `call` to the body directly after it (`0x7e1bbfae`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bbfd9` | 2 | `obj_clear_f1016_7e1bbfd9` | `*(this+1016) = 0`. | pattern scan |
| `0x7e1bc020` | 1 | `entry_thunk_7e1bc020` | `call` to the body directly after it (`0x7e1bc028`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bc052` | 2 | `obj_clear_f1020_7e1bc052` | `*(this+1020) = 0`. | pattern scan |
| `0x7e1bc099` | 1 | `entry_thunk_7e1bc099` | `call` to the body directly after it (`0x7e1bc0a1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bc0bd` | 1 | `entry_thunk_7e1bc0bd` | `call` to the body directly after it (`0x7e1bc0c5`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1be504` | 2 | `obj_set1_f252_7e1be504` | `*(this+252) = 1`. | pattern scan |
| `0x7e1be50d` | 1 | `obj_clear_f552_7e1be50d` | `*(this+552) = 0`. | pattern scan |
| `0x7e1be551` | 1 | `entry_thunk_7e1be551` | `call` to the body directly after it (`0x7e1be559`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1be575` | 2 | `entry_thunk_7e1be575` | `call` to the body directly after it (`0x7e1be57d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1be6af` | 2 | `entry_thunk_7e1be6af` | `call` to the body directly after it (`0x7e1be6b7`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1be7c2` | 1 | `entry_thunk_7e1be7c2` | `call` to the body directly after it (`0x7e1be7ca`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1be81f` | 1 | `entry_thunk_7e1be81f` | `call` to the body directly after it (`0x7e1be827`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1be874` | 1 | `entry_thunk_7e1be874` | `call` to the body directly after it (`0x7e1be87c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1be898` | 3 | `entry_thunk_7e1be898` | `call` to the body directly after it (`0x7e1be8a0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bf32e` | 2 | `obj_clear_f952_7e1bf32e` | `*(this+952) = 0`. | pattern scan |
| `0x7e1bf375` | 1 | `entry_thunk_7e1bf375` | `call` to the body directly after it (`0x7e1bf37d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bf3da` | 2 | `obj_clear_f1136_7e1bf3da` | `*(this+1136) = 0`. | pattern scan |
| `0x7e1bf421` | 1 | `entry_thunk_7e1bf421` | `call` to the body directly after it (`0x7e1bf429`, register-save mask `0xb0`, frame 52) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bf5df` | 1 | `entry_thunk_7e1bf5df` | `call` to the body directly after it (`0x7e1bf5e7`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bf679` | 2 | `obj_clear_f1140_7e1bf679` | `*(this+1140) = 0`. | pattern scan |
| `0x7e1bf6c0` | 1 | `entry_thunk_7e1bf6c0` | `call` to the body directly after it (`0x7e1bf6c8`, register-save mask `0xf0`, frame 164) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bfa34` | 2 | `obj_clear_f1144_7e1bfa34` | `*(this+1144) = 0`. | pattern scan |
| `0x7e1bfa7b` | 1 | `entry_thunk_7e1bfa7b` | `call` to the body directly after it (`0x7e1bfa83`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bfb4c` | 2 | `obj_clear_f1148_7e1bfb4c` | `*(this+1148) = 0`. | pattern scan |
| `0x7e1bfb93` | 1 | `entry_thunk_7e1bfb93` | `call` to the body directly after it (`0x7e1bfb9b`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bfc69` | 2 | `obj_clear_f1152_7e1bfc69` | `*(this+1152) = 0`. | pattern scan |
| `0x7e1bfcb0` | 1 | `entry_thunk_7e1bfcb0` | `call` to the body directly after it (`0x7e1bfcb8`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bfdac` | 2 | `obj_clear_f1156_7e1bfdac` | `*(this+1156) = 0`. | pattern scan |
| `0x7e1bfdf3` | 1 | `entry_thunk_7e1bfdf3` | `call` to the body directly after it (`0x7e1bfdfb`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1bfef6` | 2 | `obj_clear_f1160_7e1bfef6` | `*(this+1160) = 0`. | pattern scan |
| `0x7e1bff3d` | 1 | `entry_thunk_7e1bff3d` | `call` to the body directly after it (`0x7e1bff45`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c0103` | 2 | `obj_clear_f1164_7e1c0103` | `*(this+1164) = 0`. | pattern scan |
| `0x7e1c014a` | 1 | `entry_thunk_7e1c014a` | `call` to the body directly after it (`0x7e1c0152`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c0309` | 1 | `entry_thunk_7e1c0309` | `call` to the body directly after it (`0x7e1c0311`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c03a0` | 2 | `obj_clear_f1168_7e1c03a0` | `*(this+1168) = 0`. | pattern scan |
| `0x7e1c03e7` | 1 | `entry_thunk_7e1c03e7` | `call` to the body directly after it (`0x7e1c03ef`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c049a` | 2 | `obj_clear_f1172_7e1c049a` | `*(this+1172) = 0`. | pattern scan |
| `0x7e1c04e1` | 1 | `entry_thunk_7e1c04e1` | `call` to the body directly after it (`0x7e1c04e9`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c05e6` | 2 | `obj_clear_f1176_7e1c05e6` | `*(this+1176) = 0`. | pattern scan |
| `0x7e1c062d` | 1 | `entry_thunk_7e1c062d` | `call` to the body directly after it (`0x7e1c0635`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c0729` | 2 | `obj_clear_f1180_7e1c0729` | `*(this+1180) = 0`. | pattern scan |
| `0x7e1c0770` | 1 | `entry_thunk_7e1c0770` | `call` to the body directly after it (`0x7e1c0778`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c0850` | 2 | `obj_clear_f1184_7e1c0850` | `*(this+1184) = 0`. | pattern scan |
| `0x7e1c0897` | 1 | `entry_thunk_7e1c0897` | `call` to the body directly after it (`0x7e1c089f`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c09af` | 2 | `obj_clear_f1188_7e1c09af` | `*(this+1188) = 0`. | pattern scan |
| `0x7e1c09f6` | 1 | `entry_thunk_7e1c09f6` | `call` to the body directly after it (`0x7e1c09fe`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c0ae1` | 2 | `obj_clear_f1192_7e1c0ae1` | `*(this+1192) = 0`. | pattern scan |
| `0x7e1c0b28` | 1 | `entry_thunk_7e1c0b28` | `call` to the body directly after it (`0x7e1c0b30`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c0c77` | 2 | `obj_clear_f1196_7e1c0c77` | `*(this+1196) = 0`. | pattern scan |
| `0x7e1c0cbe` | 1 | `entry_thunk_7e1c0cbe` | `call` to the body directly after it (`0x7e1c0cc6`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c0dae` | 2 | `obj_clear_f1200_7e1c0dae` | `*(this+1200) = 0`. | pattern scan |
| `0x7e1c0df5` | 1 | `entry_thunk_7e1c0df5` | `call` to the body directly after it (`0x7e1c0dfd`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c1086` | 2 | `obj_clear_f956_7e1c1086` | `*(this+956) = 0`. | pattern scan |
| `0x7e1c10cd` | 1 | `entry_thunk_7e1c10cd` | `call` to the body directly after it (`0x7e1c10d5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c10f1` | 1 | `entry_thunk_7e1c10f1` | `call` to the body directly after it (`0x7e1c10f9`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c145a` | 2 | `obj_clear_f960_7e1c145a` | `*(this+960) = 0`. | pattern scan |
| `0x7e1c14a1` | 1 | `entry_thunk_7e1c14a1` | `call` to the body directly after it (`0x7e1c14a9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c14d3` | 2 | `obj_clear_f964_7e1c14d3` | `*(this+964) = 0`. | pattern scan |
| `0x7e1c151a` | 1 | `entry_thunk_7e1c151a` | `call` to the body directly after it (`0x7e1c1522`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c154c` | 2 | `obj_clear_f968_7e1c154c` | `*(this+968) = 0`. | pattern scan |
| `0x7e1c1593` | 1 | `entry_thunk_7e1c1593` | `call` to the body directly after it (`0x7e1c159b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c15c5` | 2 | `obj_clear_f972_7e1c15c5` | `*(this+972) = 0`. | pattern scan |
| `0x7e1c160c` | 1 | `entry_thunk_7e1c160c` | `call` to the body directly after it (`0x7e1c1614`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c163e` | 2 | `obj_clear_f976_7e1c163e` | `*(this+976) = 0`. | pattern scan |
| `0x7e1c1685` | 1 | `entry_thunk_7e1c1685` | `call` to the body directly after it (`0x7e1c168d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c16b7` | 2 | `obj_clear_f980_7e1c16b7` | `*(this+980) = 0`. | pattern scan |
| `0x7e1c16fe` | 1 | `entry_thunk_7e1c16fe` | `call` to the body directly after it (`0x7e1c1706`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c1730` | 2 | `obj_clear_f984_7e1c1730` | `*(this+984) = 0`. | pattern scan |
| `0x7e1c1777` | 1 | `entry_thunk_7e1c1777` | `call` to the body directly after it (`0x7e1c177f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c17a9` | 2 | `obj_clear_f988_7e1c17a9` | `*(this+988) = 0`. | pattern scan |
| `0x7e1c17f0` | 1 | `entry_thunk_7e1c17f0` | `call` to the body directly after it (`0x7e1c17f8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c1822` | 2 | `obj_clear_f992_7e1c1822` | `*(this+992) = 0`. | pattern scan |
| `0x7e1c1869` | 1 | `entry_thunk_7e1c1869` | `call` to the body directly after it (`0x7e1c1871`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c189b` | 2 | `obj_clear_f996_7e1c189b` | `*(this+996) = 0`. | pattern scan |
| `0x7e1c18e2` | 1 | `entry_thunk_7e1c18e2` | `call` to the body directly after it (`0x7e1c18ea`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c1914` | 2 | `obj_clear_f1000_7e1c1914` | `*(this+1000) = 0`. | pattern scan |
| `0x7e1c195b` | 1 | `entry_thunk_7e1c195b` | `call` to the body directly after it (`0x7e1c1963`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c1a5f` | 2 | `obj_clear_f1004_7e1c1a5f` | `*(this+1004) = 0`. | pattern scan |
| `0x7e1c1aa6` | 1 | `entry_thunk_7e1c1aa6` | `call` to the body directly after it (`0x7e1c1aae`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c1ad8` | 2 | `obj_clear_f1008_7e1c1ad8` | `*(this+1008) = 0`. | pattern scan |
| `0x7e1c1b1f` | 1 | `entry_thunk_7e1c1b1f` | `call` to the body directly after it (`0x7e1c1b27`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c1ba6` | 1 | `entry_thunk_7e1c1ba6` | `call` to the body directly after it (`0x7e1c1bae`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c1bd8` | 2 | `obj_clear_f1016_7e1c1bd8` | `*(this+1016) = 0`. | pattern scan |
| `0x7e1c1c1f` | 1 | `entry_thunk_7e1c1c1f` | `call` to the body directly after it (`0x7e1c1c27`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c1c51` | 2 | `obj_clear_f1020_7e1c1c51` | `*(this+1020) = 0`. | pattern scan |
| `0x7e1c1c98` | 1 | `entry_thunk_7e1c1c98` | `call` to the body directly after it (`0x7e1c1ca0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c1cbc` | 1 | `entry_thunk_7e1c1cbc` | `call` to the body directly after it (`0x7e1c1cc4`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c26e5` | 2 | `obj_set1_f252_7e1c26e5` | `*(this+252) = 1`. | pattern scan |
| `0x7e1c26ee` | 1 | `obj_clear_f552_7e1c26ee` | `*(this+552) = 0`. | pattern scan |
| `0x7e1c2732` | 1 | `entry_thunk_7e1c2732` | `call` to the body directly after it (`0x7e1c273a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c2756` | 2 | `entry_thunk_7e1c2756` | `call` to the body directly after it (`0x7e1c275e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c2890` | 2 | `entry_thunk_7e1c2890` | `call` to the body directly after it (`0x7e1c2898`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c29a3` | 1 | `entry_thunk_7e1c29a3` | `call` to the body directly after it (`0x7e1c29ab`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c2a00` | 1 | `entry_thunk_7e1c2a00` | `call` to the body directly after it (`0x7e1c2a08`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c2a55` | 1 | `entry_thunk_7e1c2a55` | `call` to the body directly after it (`0x7e1c2a5d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c2a79` | 3 | `entry_thunk_7e1c2a79` | `call` to the body directly after it (`0x7e1c2a81`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c320e` | 2 | `obj_clear_f952_7e1c320e` | `*(this+952) = 0`. | pattern scan |
| `0x7e1c3255` | 1 | `entry_thunk_7e1c3255` | `call` to the body directly after it (`0x7e1c325d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c32ba` | 2 | `obj_clear_f956_7e1c32ba` | `*(this+956) = 0`. | pattern scan |
| `0x7e1c3301` | 1 | `entry_thunk_7e1c3301` | `call` to the body directly after it (`0x7e1c3309`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c3325` | 1 | `entry_thunk_7e1c3325` | `call` to the body directly after it (`0x7e1c332d`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c3518` | 2 | `obj_clear_f960_7e1c3518` | `*(this+960) = 0`. | pattern scan |
| `0x7e1c355f` | 1 | `entry_thunk_7e1c355f` | `call` to the body directly after it (`0x7e1c3567`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c3591` | 2 | `obj_clear_f964_7e1c3591` | `*(this+964) = 0`. | pattern scan |
| `0x7e1c35d8` | 1 | `entry_thunk_7e1c35d8` | `call` to the body directly after it (`0x7e1c35e0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c360a` | 2 | `obj_clear_f968_7e1c360a` | `*(this+968) = 0`. | pattern scan |
| `0x7e1c3651` | 1 | `entry_thunk_7e1c3651` | `call` to the body directly after it (`0x7e1c3659`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c3683` | 2 | `obj_clear_f972_7e1c3683` | `*(this+972) = 0`. | pattern scan |
| `0x7e1c36ca` | 1 | `entry_thunk_7e1c36ca` | `call` to the body directly after it (`0x7e1c36d2`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c36fc` | 2 | `obj_clear_f976_7e1c36fc` | `*(this+976) = 0`. | pattern scan |
| `0x7e1c3743` | 1 | `entry_thunk_7e1c3743` | `call` to the body directly after it (`0x7e1c374b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c3775` | 2 | `obj_clear_f980_7e1c3775` | `*(this+980) = 0`. | pattern scan |
| `0x7e1c37bc` | 1 | `entry_thunk_7e1c37bc` | `call` to the body directly after it (`0x7e1c37c4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c37ee` | 2 | `obj_clear_f984_7e1c37ee` | `*(this+984) = 0`. | pattern scan |
| `0x7e1c3835` | 1 | `entry_thunk_7e1c3835` | `call` to the body directly after it (`0x7e1c383d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c3867` | 2 | `obj_clear_f988_7e1c3867` | `*(this+988) = 0`. | pattern scan |
| `0x7e1c38ae` | 1 | `entry_thunk_7e1c38ae` | `call` to the body directly after it (`0x7e1c38b6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c38e0` | 2 | `obj_clear_f992_7e1c38e0` | `*(this+992) = 0`. | pattern scan |
| `0x7e1c3927` | 1 | `entry_thunk_7e1c3927` | `call` to the body directly after it (`0x7e1c392f`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c3959` | 2 | `obj_clear_f996_7e1c3959` | `*(this+996) = 0`. | pattern scan |
| `0x7e1c39a0` | 1 | `entry_thunk_7e1c39a0` | `call` to the body directly after it (`0x7e1c39a8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c39d2` | 2 | `obj_clear_f1000_7e1c39d2` | `*(this+1000) = 0`. | pattern scan |
| `0x7e1c3a19` | 1 | `entry_thunk_7e1c3a19` | `call` to the body directly after it (`0x7e1c3a21`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c3b1d` | 2 | `obj_clear_f1004_7e1c3b1d` | `*(this+1004) = 0`. | pattern scan |
| `0x7e1c3b64` | 1 | `entry_thunk_7e1c3b64` | `call` to the body directly after it (`0x7e1c3b6c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c3b96` | 2 | `obj_clear_f1008_7e1c3b96` | `*(this+1008) = 0`. | pattern scan |
| `0x7e1c3bdd` | 1 | `entry_thunk_7e1c3bdd` | `call` to the body directly after it (`0x7e1c3be5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c3c64` | 1 | `entry_thunk_7e1c3c64` | `call` to the body directly after it (`0x7e1c3c6c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c3c96` | 2 | `obj_clear_f1016_7e1c3c96` | `*(this+1016) = 0`. | pattern scan |
| `0x7e1c3cdd` | 1 | `entry_thunk_7e1c3cdd` | `call` to the body directly after it (`0x7e1c3ce5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c3d0f` | 2 | `obj_clear_f1020_7e1c3d0f` | `*(this+1020) = 0`. | pattern scan |
| `0x7e1c3d56` | 1 | `entry_thunk_7e1c3d56` | `call` to the body directly after it (`0x7e1c3d5e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c3d7a` | 1 | `entry_thunk_7e1c3d7a` | `call` to the body directly after it (`0x7e1c3d82`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c4484` | 1 | `obj_clear_f552_7e1c4484` | `*(this+552) = 0`. | pattern scan |
| `0x7e1c44c9` | 1 | `entry_thunk_7e1c44c9` | `call` to the body directly after it (`0x7e1c44d1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c44ed` | 2 | `entry_thunk_7e1c44ed` | `call` to the body directly after it (`0x7e1c44f5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c462b` | 2 | `entry_thunk_7e1c462b` | `call` to the body directly after it (`0x7e1c4633`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c4745` | 1 | `entry_thunk_7e1c4745` | `call` to the body directly after it (`0x7e1c474d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c47a2` | 1 | `entry_thunk_7e1c47a2` | `call` to the body directly after it (`0x7e1c47aa`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c47f7` | 1 | `entry_thunk_7e1c47f7` | `call` to the body directly after it (`0x7e1c47ff`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c481b` | 3 | `entry_thunk_7e1c481b` | `call` to the body directly after it (`0x7e1c4823`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c4b1e` | 1 | `entry_thunk_7e1c4b1e` | `call` to the body directly after it (`0x7e1c4b26`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c4b6c` | 1 | `entry_thunk_7e1c4b6c` | `call` to the body directly after it (`0x7e1c4b74`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c4bba` | 6 | `entry_thunk_7e1c4bba` | `call` to the body directly after it (`0x7e1c4bc2`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c4dbf` | 1 | `entry_thunk_7e1c4dbf` | `call` to the body directly after it (`0x7e1c4dc7`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c4e0d` | 1 | `entry_thunk_7e1c4e0d` | `call` to the body directly after it (`0x7e1c4e15`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c4e5b` | 1 | `entry_thunk_7e1c4e5b` | `call` to the body directly after it (`0x7e1c4e63`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c4ea9` | 1 | `entry_thunk_7e1c4ea9` | `call` to the body directly after it (`0x7e1c4eb1`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c4f05` | 2 | `obj_clear_f584_7e1c4f05` | `*(this+584) = 0`. | pattern scan |
| `0x7e1c4f4c` | 1 | `entry_thunk_7e1c4f4c` | `call` to the body directly after it (`0x7e1c4f54`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c50d6` | 2 | `entry_thunk_7e1c50d6` | `call` to the body directly after it (`0x7e1c50de`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c52b6` | 2 | `entry_thunk_7e1c52b6` | `call` to the body directly after it (`0x7e1c52be`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c59e9` | 2 | `obj_set1_f252_7e1c59e9` | `*(this+252) = 1`. | pattern scan |
| `0x7e1c59f2` | 1 | `obj_clear_f552_7e1c59f2` | `*(this+552) = 0`. | pattern scan |
| `0x7e1c5a36` | 1 | `entry_thunk_7e1c5a36` | `call` to the body directly after it (`0x7e1c5a3e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c5a5a` | 2 | `entry_thunk_7e1c5a5a` | `call` to the body directly after it (`0x7e1c5a62`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c5b94` | 2 | `entry_thunk_7e1c5b94` | `call` to the body directly after it (`0x7e1c5b9c`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c5ca7` | 1 | `entry_thunk_7e1c5ca7` | `call` to the body directly after it (`0x7e1c5caf`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c5d04` | 1 | `entry_thunk_7e1c5d04` | `call` to the body directly after it (`0x7e1c5d0c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c5d59` | 1 | `entry_thunk_7e1c5d59` | `call` to the body directly after it (`0x7e1c5d61`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c5d7d` | 3 | `entry_thunk_7e1c5d7d` | `call` to the body directly after it (`0x7e1c5d85`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c6588` | 2 | `obj_clear_f1256_7e1c6588` | `*(this+1256) = 0`. | pattern scan |
| `0x7e1c65cf` | 1 | `entry_thunk_7e1c65cf` | `call` to the body directly after it (`0x7e1c65d7`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c66ad` | 2 | `obj_clear_f952_7e1c66ad` | `*(this+952) = 0`. | pattern scan |
| `0x7e1c66f4` | 1 | `entry_thunk_7e1c66f4` | `call` to the body directly after it (`0x7e1c66fc`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c6759` | 2 | `obj_clear_f1260_7e1c6759` | `*(this+1260) = 0`. | pattern scan |
| `0x7e1c67a0` | 1 | `entry_thunk_7e1c67a0` | `call` to the body directly after it (`0x7e1c67a8`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c688c` | 2 | `obj_clear_f1264_7e1c688c` | `*(this+1264) = 0`. | pattern scan |
| `0x7e1c68d3` | 1 | `entry_thunk_7e1c68d3` | `call` to the body directly after it (`0x7e1c68db`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c6999` | 2 | `obj_clear_f956_7e1c6999` | `*(this+956) = 0`. | pattern scan |
| `0x7e1c69e0` | 1 | `entry_thunk_7e1c69e0` | `call` to the body directly after it (`0x7e1c69e8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c6a12` | 2 | `obj_clear_f1268_7e1c6a12` | `*(this+1268) = 0`. | pattern scan |
| `0x7e1c6a59` | 1 | `entry_thunk_7e1c6a59` | `call` to the body directly after it (`0x7e1c6a61`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c6c41` | 1 | `entry_thunk_7e1c6c41` | `call` to the body directly after it (`0x7e1c6c49`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c6f7e` | 2 | `obj_clear_f1272_7e1c6f7e` | `*(this+1272) = 0`. | pattern scan |
| `0x7e1c6fc5` | 2 | `entry_thunk_7e1c6fc5` | `call` to the body directly after it (`0x7e1c6fcd`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c71f0` | 1 | `entry_thunk_7e1c71f0` | `call` to the body directly after it (`0x7e1c71f8`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c7378` | 2 | `obj_clear_f960_7e1c7378` | `*(this+960) = 0`. | pattern scan |
| `0x7e1c73bf` | 1 | `entry_thunk_7e1c73bf` | `call` to the body directly after it (`0x7e1c73c7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c73f1` | 2 | `obj_clear_f964_7e1c73f1` | `*(this+964) = 0`. | pattern scan |
| `0x7e1c7438` | 1 | `entry_thunk_7e1c7438` | `call` to the body directly after it (`0x7e1c7440`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c746a` | 2 | `obj_clear_f968_7e1c746a` | `*(this+968) = 0`. | pattern scan |
| `0x7e1c74b1` | 1 | `entry_thunk_7e1c74b1` | `call` to the body directly after it (`0x7e1c74b9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c74e3` | 2 | `obj_clear_f1276_7e1c74e3` | `*(this+1276) = 0`. | pattern scan |
| `0x7e1c752a` | 1 | `entry_thunk_7e1c752a` | `call` to the body directly after it (`0x7e1c7532`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c75ff` | 2 | `obj_clear_f1280_7e1c75ff` | `*(this+1280) = 0`. | pattern scan |
| `0x7e1c7646` | 1 | `entry_thunk_7e1c7646` | `call` to the body directly after it (`0x7e1c764e`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c7906` | 2 | `obj_clear_f972_7e1c7906` | `*(this+972) = 0`. | pattern scan |
| `0x7e1c794d` | 1 | `entry_thunk_7e1c794d` | `call` to the body directly after it (`0x7e1c7955`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c797f` | 2 | `obj_clear_f976_7e1c797f` | `*(this+976) = 0`. | pattern scan |
| `0x7e1c79c6` | 1 | `entry_thunk_7e1c79c6` | `call` to the body directly after it (`0x7e1c79ce`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c79f8` | 2 | `obj_clear_f1284_7e1c79f8` | `*(this+1284) = 0`. | pattern scan |
| `0x7e1c7a3f` | 1 | `entry_thunk_7e1c7a3f` | `call` to the body directly after it (`0x7e1c7a47`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c7b48` | 2 | `obj_clear_f980_7e1c7b48` | `*(this+980) = 0`. | pattern scan |
| `0x7e1c7b8f` | 1 | `entry_thunk_7e1c7b8f` | `call` to the body directly after it (`0x7e1c7b97`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c7bc1` | 2 | `obj_clear_f984_7e1c7bc1` | `*(this+984) = 0`. | pattern scan |
| `0x7e1c7c08` | 1 | `entry_thunk_7e1c7c08` | `call` to the body directly after it (`0x7e1c7c10`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c7c3a` | 2 | `obj_clear_f988_7e1c7c3a` | `*(this+988) = 0`. | pattern scan |
| `0x7e1c7c81` | 1 | `entry_thunk_7e1c7c81` | `call` to the body directly after it (`0x7e1c7c89`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c7cb3` | 2 | `obj_clear_f992_7e1c7cb3` | `*(this+992) = 0`. | pattern scan |
| `0x7e1c7cfa` | 1 | `entry_thunk_7e1c7cfa` | `call` to the body directly after it (`0x7e1c7d02`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c7d2c` | 2 | `obj_clear_f996_7e1c7d2c` | `*(this+996) = 0`. | pattern scan |
| `0x7e1c7d73` | 1 | `entry_thunk_7e1c7d73` | `call` to the body directly after it (`0x7e1c7d7b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c7da5` | 2 | `obj_clear_f1288_7e1c7da5` | `*(this+1288) = 0`. | pattern scan |
| `0x7e1c7dec` | 1 | `entry_thunk_7e1c7dec` | `call` to the body directly after it (`0x7e1c7df4`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c7fbb` | 2 | `obj_clear_f1000_7e1c7fbb` | `*(this+1000) = 0`. | pattern scan |
| `0x7e1c8002` | 1 | `entry_thunk_7e1c8002` | `call` to the body directly after it (`0x7e1c800a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c8106` | 2 | `obj_clear_f1292_7e1c8106` | `*(this+1292) = 0`. | pattern scan |
| `0x7e1c814d` | 1 | `entry_thunk_7e1c814d` | `call` to the body directly after it (`0x7e1c8155`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c8201` | 2 | `obj_clear_f1004_7e1c8201` | `*(this+1004) = 0`. | pattern scan |
| `0x7e1c8248` | 1 | `entry_thunk_7e1c8248` | `call` to the body directly after it (`0x7e1c8250`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c827a` | 2 | `obj_clear_f1008_7e1c827a` | `*(this+1008) = 0`. | pattern scan |
| `0x7e1c82c1` | 1 | `entry_thunk_7e1c82c1` | `call` to the body directly after it (`0x7e1c82c9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c8348` | 1 | `entry_thunk_7e1c8348` | `call` to the body directly after it (`0x7e1c8350`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c837a` | 2 | `obj_clear_f1296_7e1c837a` | `*(this+1296) = 0`. | pattern scan |
| `0x7e1c83c1` | 1 | `entry_thunk_7e1c83c1` | `call` to the body directly after it (`0x7e1c83c9`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c85de` | 2 | `obj_clear_f1300_7e1c85de` | `*(this+1300) = 0`. | pattern scan |
| `0x7e1c8625` | 1 | `entry_thunk_7e1c8625` | `call` to the body directly after it (`0x7e1c862d`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c86fe` | 2 | `obj_clear_f1016_7e1c86fe` | `*(this+1016) = 0`. | pattern scan |
| `0x7e1c8745` | 1 | `entry_thunk_7e1c8745` | `call` to the body directly after it (`0x7e1c874d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c8777` | 2 | `obj_clear_f1304_7e1c8777` | `*(this+1304) = 0`. | pattern scan |
| `0x7e1c87be` | 1 | `entry_thunk_7e1c87be` | `call` to the body directly after it (`0x7e1c87c6`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c88a5` | 2 | `obj_clear_f1020_7e1c88a5` | `*(this+1020) = 0`. | pattern scan |
| `0x7e1c88ec` | 1 | `entry_thunk_7e1c88ec` | `call` to the body directly after it (`0x7e1c88f4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c891e` | 2 | `obj_clear_f1308_7e1c891e` | `*(this+1308) = 0`. | pattern scan |
| `0x7e1c8965` | 1 | `entry_thunk_7e1c8965` | `call` to the body directly after it (`0x7e1c896d`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c8a70` | 2 | `obj_clear_f1312_7e1c8a70` | `*(this+1312) = 0`. | pattern scan |
| `0x7e1c8ab7` | 1 | `entry_thunk_7e1c8ab7` | `call` to the body directly after it (`0x7e1c8abf`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c8bbd` | 1 | `entry_thunk_7e1c8bbd` | `call` to the body directly after it (`0x7e1c8bc5`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c9954` | 2 | `obj_set1_f252_7e1c9954` | `*(this+252) = 1`. | pattern scan |
| `0x7e1c995d` | 1 | `obj_clear_f552_7e1c995d` | `*(this+552) = 0`. | pattern scan |
| `0x7e1c99a1` | 1 | `entry_thunk_7e1c99a1` | `call` to the body directly after it (`0x7e1c99a9`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c99c5` | 2 | `entry_thunk_7e1c99c5` | `call` to the body directly after it (`0x7e1c99cd`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c9aff` | 2 | `entry_thunk_7e1c9aff` | `call` to the body directly after it (`0x7e1c9b07`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c9c12` | 1 | `entry_thunk_7e1c9c12` | `call` to the body directly after it (`0x7e1c9c1a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c9c6f` | 1 | `entry_thunk_7e1c9c6f` | `call` to the body directly after it (`0x7e1c9c77`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c9cc4` | 1 | `entry_thunk_7e1c9cc4` | `call` to the body directly after it (`0x7e1c9ccc`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1c9ce8` | 3 | `entry_thunk_7e1c9ce8` | `call` to the body directly after it (`0x7e1c9cf0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ca4ba` | 2 | `obj_clear_f952_7e1ca4ba` | `*(this+952) = 0`. | pattern scan |
| `0x7e1ca501` | 1 | `entry_thunk_7e1ca501` | `call` to the body directly after it (`0x7e1ca509`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ca566` | 2 | `obj_clear_f1256_7e1ca566` | `*(this+1256) = 0`. | pattern scan |
| `0x7e1ca5ad` | 1 | `entry_thunk_7e1ca5ad` | `call` to the body directly after it (`0x7e1ca5b5`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ca660` | 2 | `obj_clear_f1260_7e1ca660` | `*(this+1260) = 0`. | pattern scan |
| `0x7e1ca6a7` | 1 | `entry_thunk_7e1ca6a7` | `call` to the body directly after it (`0x7e1ca6af`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ca908` | 2 | `obj_clear_f956_7e1ca908` | `*(this+956) = 0`. | pattern scan |
| `0x7e1ca94f` | 1 | `entry_thunk_7e1ca94f` | `call` to the body directly after it (`0x7e1ca957`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ca973` | 1 | `entry_thunk_7e1ca973` | `call` to the body directly after it (`0x7e1ca97b`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cac16` | 2 | `obj_clear_f1264_7e1cac16` | `*(this+1264) = 0`. | pattern scan |
| `0x7e1cac5d` | 1 | `entry_thunk_7e1cac5d` | `call` to the body directly after it (`0x7e1cac65`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cadcd` | 2 | `obj_clear_f960_7e1cadcd` | `*(this+960) = 0`. | pattern scan |
| `0x7e1cae14` | 1 | `entry_thunk_7e1cae14` | `call` to the body directly after it (`0x7e1cae1c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cae46` | 2 | `obj_clear_f964_7e1cae46` | `*(this+964) = 0`. | pattern scan |
| `0x7e1cae8d` | 1 | `entry_thunk_7e1cae8d` | `call` to the body directly after it (`0x7e1cae95`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1caebf` | 2 | `obj_clear_f968_7e1caebf` | `*(this+968) = 0`. | pattern scan |
| `0x7e1caf06` | 1 | `entry_thunk_7e1caf06` | `call` to the body directly after it (`0x7e1caf0e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1caf38` | 2 | `obj_clear_f1268_7e1caf38` | `*(this+1268) = 0`. | pattern scan |
| `0x7e1caf7f` | 1 | `entry_thunk_7e1caf7f` | `call` to the body directly after it (`0x7e1caf87`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cb1b3` | 2 | `obj_clear_f972_7e1cb1b3` | `*(this+972) = 0`. | pattern scan |
| `0x7e1cb1fa` | 1 | `entry_thunk_7e1cb1fa` | `call` to the body directly after it (`0x7e1cb202`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cb22c` | 2 | `obj_clear_f976_7e1cb22c` | `*(this+976) = 0`. | pattern scan |
| `0x7e1cb273` | 1 | `entry_thunk_7e1cb273` | `call` to the body directly after it (`0x7e1cb27b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cb2a5` | 2 | `obj_clear_f1272_7e1cb2a5` | `*(this+1272) = 0`. | pattern scan |
| `0x7e1cb2ec` | 1 | `entry_thunk_7e1cb2ec` | `call` to the body directly after it (`0x7e1cb2f4`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cb3bc` | 2 | `obj_clear_f980_7e1cb3bc` | `*(this+980) = 0`. | pattern scan |
| `0x7e1cb403` | 1 | `entry_thunk_7e1cb403` | `call` to the body directly after it (`0x7e1cb40b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cb435` | 2 | `obj_clear_f984_7e1cb435` | `*(this+984) = 0`. | pattern scan |
| `0x7e1cb47c` | 1 | `entry_thunk_7e1cb47c` | `call` to the body directly after it (`0x7e1cb484`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cb4ae` | 2 | `obj_clear_f1276_7e1cb4ae` | `*(this+1276) = 0`. | pattern scan |
| `0x7e1cb4f5` | 1 | `entry_thunk_7e1cb4f5` | `call` to the body directly after it (`0x7e1cb4fd`, register-save mask `0xf0`, frame 16) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cb5c5` | 2 | `obj_clear_f988_7e1cb5c5` | `*(this+988) = 0`. | pattern scan |
| `0x7e1cb60c` | 1 | `entry_thunk_7e1cb60c` | `call` to the body directly after it (`0x7e1cb614`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cb63e` | 2 | `obj_clear_f992_7e1cb63e` | `*(this+992) = 0`. | pattern scan |
| `0x7e1cb685` | 1 | `entry_thunk_7e1cb685` | `call` to the body directly after it (`0x7e1cb68d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cb6b7` | 2 | `obj_clear_f996_7e1cb6b7` | `*(this+996) = 0`. | pattern scan |
| `0x7e1cb6fe` | 1 | `entry_thunk_7e1cb6fe` | `call` to the body directly after it (`0x7e1cb706`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cb730` | 2 | `obj_clear_f1280_7e1cb730` | `*(this+1280) = 0`. | pattern scan |
| `0x7e1cb777` | 1 | `entry_thunk_7e1cb777` | `call` to the body directly after it (`0x7e1cb77f`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cb847` | 2 | `obj_clear_f1000_7e1cb847` | `*(this+1000) = 0`. | pattern scan |
| `0x7e1cb88e` | 1 | `entry_thunk_7e1cb88e` | `call` to the body directly after it (`0x7e1cb896`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cb992` | 2 | `obj_clear_f1004_7e1cb992` | `*(this+1004) = 0`. | pattern scan |
| `0x7e1cb9d9` | 1 | `entry_thunk_7e1cb9d9` | `call` to the body directly after it (`0x7e1cb9e1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cba0b` | 2 | `obj_clear_f1008_7e1cba0b` | `*(this+1008) = 0`. | pattern scan |
| `0x7e1cba52` | 1 | `entry_thunk_7e1cba52` | `call` to the body directly after it (`0x7e1cba5a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cbad9` | 1 | `entry_thunk_7e1cbad9` | `call` to the body directly after it (`0x7e1cbae1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cbb0b` | 2 | `obj_clear_f1016_7e1cbb0b` | `*(this+1016) = 0`. | pattern scan |
| `0x7e1cbb52` | 1 | `entry_thunk_7e1cbb52` | `call` to the body directly after it (`0x7e1cbb5a`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cbb84` | 2 | `obj_clear_f1020_7e1cbb84` | `*(this+1020) = 0`. | pattern scan |
| `0x7e1cbbcb` | 1 | `entry_thunk_7e1cbbcb` | `call` to the body directly after it (`0x7e1cbbd3`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cbbfd` | 2 | `obj_clear_f1284_7e1cbbfd` | `*(this+1284) = 0`. | pattern scan |
| `0x7e1cbc44` | 1 | `entry_thunk_7e1cbc44` | `call` to the body directly after it (`0x7e1cbc4c`, register-save mask `0xb0`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cbcea` | 1 | `entry_thunk_7e1cbcea` | `call` to the body directly after it (`0x7e1cbcf2`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cc8ca` | 1 | `entry_thunk_7e1cc8ca` | `call` to the body directly after it (`0x7e1cc8d2`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cc93b` | 2 | `obj_clear_f408_7e1cc93b` | `*(this+408) = 0`. | pattern scan |
| `0x7e1cc9f5` | 2 | `entry_thunk_7e1cc9f5` | `call` to the body directly after it (`0x7e1cc9fd`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ccac0` | 1 | `entry_thunk_7e1ccac0` | `call` to the body directly after it (`0x7e1ccac8`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ccb7c` | 1 | `entry_thunk_7e1ccb7c` | `call` to the body directly after it (`0x7e1ccb84`, register-save mask `0xf0`, frame 60) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ccccd` | 1 | `entry_thunk_7e1ccccd` | `call` to the body directly after it (`0x7e1cccd5`, register-save mask `0xf0`, frame 64) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cce14` | 1 | `entry_thunk_7e1cce14` | `call` to the body directly after it (`0x7e1cce1c`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ccee8` | 2 | `entry_thunk_7e1ccee8` | `call` to the body directly after it (`0x7e1ccef0`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ccf5a` | 1 | `entry_thunk_7e1ccf5a` | `call` to the body directly after it (`0x7e1ccf62`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ccff9` | 3 | `entry_thunk_7e1ccff9` | `call` to the body directly after it (`0x7e1cd001`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cd09f` | 1 | `entry_thunk_7e1cd09f` | `call` to the body directly after it (`0x7e1cd0a7`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cec8b` | 1 | `entry_thunk_7e1cec8b` | `call` to the body directly after it (`0x7e1cec93`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ceca7` | 1 | `entry_thunk_7e1ceca7` | `call` to the body directly after it (`0x7e1cecaf`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ced9e` | 3 | `entry_thunk_7e1ced9e` | `call` to the body directly after it (`0x7e1ceda6`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cee1d` | 1 | `entry_thunk_7e1cee1d` | `call` to the body directly after it (`0x7e1cee25`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cef85` | 2 | `obj_set1_f252_7e1cef85` | `*(this+252) = 1`. | pattern scan |
| `0x7e1cef8e` | 1 | `obj_clear_f552_7e1cef8e` | `*(this+552) = 0`. | pattern scan |
| `0x7e1cefd2` | 1 | `entry_thunk_7e1cefd2` | `call` to the body directly after it (`0x7e1cefda`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ceff6` | 2 | `entry_thunk_7e1ceff6` | `call` to the body directly after it (`0x7e1ceffe`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cf0fa` | 1 | `obj_clear_f972_7e1cf0fa` | `*(this+972) = 0`. | pattern scan |
| `0x7e1cf140` | 1 | `entry_thunk_7e1cf140` | `call` to the body directly after it (`0x7e1cf148`, register-save mask `0xb0`, frame 32) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cf1bf` | 1 | `entry_thunk_7e1cf1bf` | `call` to the body directly after it (`0x7e1cf1c7`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cf396` | 2 | `entry_thunk_7e1cf396` | `call` to the body directly after it (`0x7e1cf39e`, register-save mask `0x30`, frame 12) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cf4ea` | 2 | `entry_thunk_7e1cf4ea` | `call` to the body directly after it (`0x7e1cf4f2`, register-save mask `0xb0`, frame 40) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cf71e` | 2 | `entry_thunk_7e1cf71e` | `call` to the body directly after it (`0x7e1cf726`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cf7b2` | 1 | `entry_thunk_7e1cf7b2` | `call` to the body directly after it (`0x7e1cf7ba`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cf807` | 1 | `entry_thunk_7e1cf807` | `call` to the body directly after it (`0x7e1cf80f`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1cf863` | 4 | `entry_thunk_7e1cf863` | `call` to the body directly after it (`0x7e1cf86b`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d116b` | 1 | `entry_thunk_7e1d116b` | `call` to the body directly after it (`0x7e1d1173`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d1228` | 2 | `entry_thunk_7e1d1228` | `call` to the body directly after it (`0x7e1d1230`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d13a3` | 2 | `entry_thunk_7e1d13a3` | `call` to the body directly after it (`0x7e1d13ab`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d14aa` | 1 | `entry_thunk_7e1d14aa` | `call` to the body directly after it (`0x7e1d14b2`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d1550` | 1 | `entry_thunk_7e1d1550` | `call` to the body directly after it (`0x7e1d1558`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d1593` | 1 | `entry_thunk_7e1d1593` | `call` to the body directly after it (`0x7e1d159b`, register-save mask `0xf0`, frame 84) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d1853` | 1 | `entry_thunk_7e1d1853` | `call` to the body directly after it (`0x7e1d185b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d186f` | 1 | `entry_thunk_7e1d186f` | `call` to the body directly after it (`0x7e1d1877`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d194a` | 2 | `entry_thunk_7e1d194a` | `call` to the body directly after it (`0x7e1d1952`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d19c9` | 1 | `entry_thunk_7e1d19c9` | `call` to the body directly after it (`0x7e1d19d1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d3e8a` | 1 | `entry_thunk_7e1d3e8a` | `call` to the body directly after it (`0x7e1d3e92`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d3ef7` | 1 | `entry_thunk_7e1d3ef7` | `call` to the body directly after it (`0x7e1d3eff`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d406c` | 2 | `entry_thunk_7e1d406c` | `call` to the body directly after it (`0x7e1d4074`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d40ff` | 1 | `entry_thunk_7e1d40ff` | `call` to the body directly after it (`0x7e1d4107`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d416c` | 1 | `entry_thunk_7e1d416c` | `call` to the body directly after it (`0x7e1d4174`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d4197` | 3 | `entry_thunk_7e1d4197` | `call` to the body directly after it (`0x7e1d419f`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d6e23` | 3 | `entry_thunk_7e1d6e23` | `call` to the body directly after it (`0x7e1d6e2b`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d7d69` | 3 | `entry_thunk_7e1d7d69` | `call` to the body directly after it (`0x7e1d7d71`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d863f` | 2 | `entry_thunk_7e1d863f` | `call` to the body directly after it (`0x7e1d8647`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d8d8f` | 2 | `entry_thunk_7e1d8d8f` | `call` to the body directly after it (`0x7e1d8d97`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1d973d` | 7 | `entry_thunk_7e1d973d` | `call` to the body directly after it (`0x7e1d9745`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1daff1` | 2 | `entry_thunk_7e1daff1` | `call` to the body directly after it (`0x7e1daff9`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1db82d` | 2 | `entry_thunk_7e1db82d` | `call` to the body directly after it (`0x7e1db835`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1dc552` | 5 | `entry_thunk_7e1dc552` | `call` to the body directly after it (`0x7e1dc55a`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1dd014` | 3 | `entry_thunk_7e1dd014` | `call` to the body directly after it (`0x7e1dd01c`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ddcb3` | 4 | `entry_thunk_7e1ddcb3` | `call` to the body directly after it (`0x7e1ddcbb`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1de55d` | 2 | `entry_thunk_7e1de55d` | `call` to the body directly after it (`0x7e1de565`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ded38` | 1 | `entry_thunk_7e1ded38` | `call` to the body directly after it (`0x7e1ded40`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1df354` | 2 | `entry_thunk_7e1df354` | `call` to the body directly after it (`0x7e1df35c`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1dffc9` | 1 | `entry_thunk_7e1dffc9` | `call` to the body directly after it (`0x7e1dffd1`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e0748` | 3 | `entry_thunk_7e1e0748` | `call` to the body directly after it (`0x7e1e0750`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e0e3a` | 4 | `entry_thunk_7e1e0e3a` | `call` to the body directly after it (`0x7e1e0e42`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e1449` | 2 | `obj_clear_f3916_7e1e1449` | `*(this+3916) = 0`. | pattern scan |
| `0x7e1e1b89` | 1 | `entry_thunk_7e1e1b89` | `call` to the body directly after it (`0x7e1e1b91`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e1ba6` | 1 | `entry_thunk_7e1e1ba6` | `call` to the body directly after it (`0x7e1e1bae`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e1c0a` | 1 | `entry_thunk_7e1e1c0a` | `call` to the body directly after it (`0x7e1e1c12`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e1c66` | 1 | `entry_thunk_7e1e1c66` | `call` to the body directly after it (`0x7e1e1c6e`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e1db3` | 1 | `entry_thunk_7e1e1db3` | `call` to the body directly after it (`0x7e1e1dbb`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e5f2c` | 2 | `entry_thunk_7e1e5f2c` | `call` to the body directly after it (`0x7e1e5f34`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e601f` | 2 | `entry_thunk_7e1e601f` | `call` to the body directly after it (`0x7e1e6027`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e609a` | 1 | `entry_thunk_7e1e609a` | `call` to the body directly after it (`0x7e1e60a2`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e6603` | 1 | `entry_thunk_7e1e6603` | `call` to the body directly after it (`0x7e1e660b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e661d` | 1 | `entry_thunk_7e1e661d` | `call` to the body directly after it (`0x7e1e6625`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e6713` | 3 | `entry_thunk_7e1e6713` | `call` to the body directly after it (`0x7e1e671b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e6791` | 1 | `entry_thunk_7e1e6791` | `call` to the body directly after it (`0x7e1e6799`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e8b3e` | 1 | `entry_thunk_7e1e8b3e` | `call` to the body directly after it (`0x7e1e8b46`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e8b90` | 1 | `entry_thunk_7e1e8b90` | `call` to the body directly after it (`0x7e1e8b98`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e8c64` | 3 | `entry_thunk_7e1e8c64` | `call` to the body directly after it (`0x7e1e8c6c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e8d08` | 1 | `entry_thunk_7e1e8d08` | `call` to the body directly after it (`0x7e1e8d10`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e8efb` | 1 | `entry_thunk_7e1e8efb` | `call` to the body directly after it (`0x7e1e8f03`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e8f4d` | 1 | `entry_thunk_7e1e8f4d` | `call` to the body directly after it (`0x7e1e8f55`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e9021` | 3 | `entry_thunk_7e1e9021` | `call` to the body directly after it (`0x7e1e9029`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e90c5` | 1 | `entry_thunk_7e1e90c5` | `call` to the body directly after it (`0x7e1e90cd`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e935e` | 1 | `entry_thunk_7e1e935e` | `call` to the body directly after it (`0x7e1e9366`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e93b0` | 1 | `entry_thunk_7e1e93b0` | `call` to the body directly after it (`0x7e1e93b8`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e9484` | 3 | `entry_thunk_7e1e9484` | `call` to the body directly after it (`0x7e1e948c`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e9528` | 1 | `entry_thunk_7e1e9528` | `call` to the body directly after it (`0x7e1e9530`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e97dd` | 1 | `entry_thunk_7e1e97dd` | `call` to the body directly after it (`0x7e1e97e5`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e982f` | 1 | `entry_thunk_7e1e982f` | `call` to the body directly after it (`0x7e1e9837`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e9903` | 3 | `entry_thunk_7e1e9903` | `call` to the body directly after it (`0x7e1e990b`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e99a7` | 1 | `entry_thunk_7e1e99a7` | `call` to the body directly after it (`0x7e1e99af`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e9cbc` | 1 | `entry_thunk_7e1e9cbc` | `call` to the body directly after it (`0x7e1e9cc4`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e9d0e` | 1 | `entry_thunk_7e1e9d0e` | `call` to the body directly after it (`0x7e1e9d16`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e9de2` | 3 | `entry_thunk_7e1e9de2` | `call` to the body directly after it (`0x7e1e9dea`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1e9e86` | 1 | `entry_thunk_7e1e9e86` | `call` to the body directly after it (`0x7e1e9e8e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ea219` | 1 | `entry_thunk_7e1ea219` | `call` to the body directly after it (`0x7e1ea221`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ea26b` | 1 | `entry_thunk_7e1ea26b` | `call` to the body directly after it (`0x7e1ea273`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ea33f` | 3 | `entry_thunk_7e1ea33f` | `call` to the body directly after it (`0x7e1ea347`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ea3e3` | 1 | `entry_thunk_7e1ea3e3` | `call` to the body directly after it (`0x7e1ea3eb`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1eb0a7` | 1 | `entry_thunk_7e1eb0a7` | `call` to the body directly after it (`0x7e1eb0af`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1eb0f7` | 2 | `obj_clear_f324_7e1eb0f7` | `*(this+324) = 0`. | pattern scan |
| `0x7e1eb1b3` | 2 | `entry_thunk_7e1eb1b3` | `call` to the body directly after it (`0x7e1eb1bb`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1eb2cb` | 1 | `entry_thunk_7e1eb2cb` | `call` to the body directly after it (`0x7e1eb2d3`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1eb2e8` | 3 | `entry_thunk_7e1eb2e8` | `call` to the body directly after it (`0x7e1eb2f0`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1eb4ac` | 2 | `obj_clear_f332_7e1eb4ac` | `*(this+332) = 0`. | pattern scan |
| `0x7e1eb54b` | 1 | `entry_thunk_7e1eb54b` | `call` to the body directly after it (`0x7e1eb553`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1eb60f` | 1 | `entry_thunk_7e1eb60f` | `call` to the body directly after it (`0x7e1eb617`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1eb717` | 1 | `entry_thunk_7e1eb717` | `call` to the body directly after it (`0x7e1eb71f`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1eb8e5` | 3 | `obj_clear_f340_7e1eb8e5` | `*(this+340) = 0`. | pattern scan |
| `0x7e1eba77` | 1 | `entry_thunk_7e1eba77` | `call` to the body directly after it (`0x7e1eba7f`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1eba94` | 1 | `entry_thunk_7e1eba94` | `call` to the body directly after it (`0x7e1eba9c`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ebbba` | 3 | `obj_clear_f344_7e1ebbba` | `*(this+344) = 0`. | pattern scan |
| `0x7e1ebd4c` | 1 | `entry_thunk_7e1ebd4c` | `call` to the body directly after it (`0x7e1ebd54`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ebd69` | 1 | `entry_thunk_7e1ebd69` | `call` to the body directly after it (`0x7e1ebd71`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ebe8b` | 3 | `obj_clear_f348_7e1ebe8b` | `*(this+348) = 0`. | pattern scan |
| `0x7e1ec01c` | 1 | `entry_thunk_7e1ec01c` | `call` to the body directly after it (`0x7e1ec024`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ec039` | 1 | `entry_thunk_7e1ec039` | `call` to the body directly after it (`0x7e1ec041`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ec5b5` | 1 | `entry_thunk_7e1ec5b5` | `call` to the body directly after it (`0x7e1ec5bd`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ec5d9` | 1 | `entry_thunk_7e1ec5d9` | `call` to the body directly after it (`0x7e1ec5e1`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ec6ee` | 3 | `entry_thunk_7e1ec6ee` | `call` to the body directly after it (`0x7e1ec6f6`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ec977` | 3 | `entry_thunk_7e1ec977` | `call` to the body directly after it (`0x7e1ec97f`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1eca42` | 3 | `entry_thunk_7e1eca42` | `call` to the body directly after it (`0x7e1eca4a`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ecd48` | 1 | `entry_thunk_7e1ecd48` | `call` to the body directly after it (`0x7e1ecd50`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ece31` | 1 | `entry_thunk_7e1ece31` | `call` to the body directly after it (`0x7e1ece39`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ecf03` | 1 | `entry_thunk_7e1ecf03` | `call` to the body directly after it (`0x7e1ecf0b`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ecf76` | 1 | `entry_thunk_7e1ecf76` | `call` to the body directly after it (`0x7e1ecf7e`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f4f71` | 2 | `obj_set1_f252_7e1f4f71` | `*(this+252) = 1`. | pattern scan |
| `0x7e1f4f7a` | 1 | `obj_clear_f332_7e1f4f7a` | `*(this+332) = 0`. | pattern scan |
| `0x7e1f4fc6` | 1 | `entry_thunk_7e1f4fc6` | `call` to the body directly after it (`0x7e1f4fce`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f501a` | 1 | `entry_thunk_7e1f501a` | `call` to the body directly after it (`0x7e1f5022`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f5037` | 2 | `entry_thunk_7e1f5037` | `call` to the body directly after it (`0x7e1f503f`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f5172` | 2 | `obj_clear_f336_7e1f5172` | `*(this+336) = 0`. | pattern scan |
| `0x7e1f5210` | 2 | `entry_thunk_7e1f5210` | `call` to the body directly after it (`0x7e1f5218`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f530f` | 1 | `entry_thunk_7e1f530f` | `call` to the body directly after it (`0x7e1f5317`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f5366` | 1 | `entry_thunk_7e1f5366` | `call` to the body directly after it (`0x7e1f536e`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f5469` | 3 | `entry_thunk_7e1f5469` | `call` to the body directly after it (`0x7e1f5471`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f5534` | 1 | `obj_clear_f356_7e1f5534` | `*(this+356) = 0`. | pattern scan |
| `0x7e1f56e9` | 2 | `entry_thunk_7e1f56e9` | `call` to the body directly after it (`0x7e1f56f1`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f577e` | 1 | `entry_thunk_7e1f577e` | `call` to the body directly after it (`0x7e1f5786`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f5ddc` | 1 | `obj_clear_f332_7e1f5ddc` | `*(this+332) = 0`. | pattern scan |
| `0x7e1f5e7c` | 1 | `entry_thunk_7e1f5e7c` | `call` to the body directly after it (`0x7e1f5e84`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f5ed0` | 1 | `entry_thunk_7e1f5ed0` | `call` to the body directly after it (`0x7e1f5ed8`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f5eed` | 2 | `entry_thunk_7e1f5eed` | `call` to the body directly after it (`0x7e1f5ef5`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f600e` | 2 | `obj_clear_f336_7e1f600e` | `*(this+336) = 0`. | pattern scan |
| `0x7e1f60c1` | 2 | `entry_thunk_7e1f60c1` | `call` to the body directly after it (`0x7e1f60c9`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f61c2` | 1 | `entry_thunk_7e1f61c2` | `call` to the body directly after it (`0x7e1f61ca`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f6219` | 1 | `entry_thunk_7e1f6219` | `call` to the body directly after it (`0x7e1f6221`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f631f` | 3 | `entry_thunk_7e1f631f` | `call` to the body directly after it (`0x7e1f6327`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f63da` | 1 | `entry_thunk_7e1f63da` | `call` to the body directly after it (`0x7e1f63e2`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f67bd` | 2 | `obj_set1_f252_7e1f67bd` | `*(this+252) = 1`. | pattern scan |
| `0x7e1f67c6` | 1 | `obj_clear_f328_7e1f67c6` | `*(this+328) = 0`. | pattern scan |
| `0x7e1f6818` | 1 | `entry_thunk_7e1f6818` | `call` to the body directly after it (`0x7e1f6820`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f686c` | 2 | `entry_thunk_7e1f686c` | `call` to the body directly after it (`0x7e1f6874`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f696a` | 2 | `obj_clear_f332_7e1f696a` | `*(this+332) = 0`. | pattern scan |
| `0x7e1f6a0c` | 2 | `entry_thunk_7e1f6a0c` | `call` to the body directly after it (`0x7e1f6a14`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f6b48` | 1 | `entry_thunk_7e1f6b48` | `call` to the body directly after it (`0x7e1f6b50`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f6b65` | 3 | `entry_thunk_7e1f6b65` | `call` to the body directly after it (`0x7e1f6b6d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f6c30` | 1 | `obj_clear_f348_7e1f6c30` | `*(this+348) = 0`. | pattern scan |
| `0x7e1f6dc2` | 2 | `entry_thunk_7e1f6dc2` | `call` to the body directly after it (`0x7e1f6dca`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f6e96` | 1 | `entry_thunk_7e1f6e96` | `call` to the body directly after it (`0x7e1f6e9e`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f74cd` | 1 | `obj_clear_f328_7e1f74cd` | `*(this+328) = 0`. | pattern scan |
| `0x7e1f7576` | 1 | `entry_thunk_7e1f7576` | `call` to the body directly after it (`0x7e1f757e`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f75ca` | 2 | `entry_thunk_7e1f75ca` | `call` to the body directly after it (`0x7e1f75d2`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f76aa` | 2 | `obj_clear_f332_7e1f76aa` | `*(this+332) = 0`. | pattern scan |
| `0x7e1f7764` | 2 | `entry_thunk_7e1f7764` | `call` to the body directly after it (`0x7e1f776c`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f78a0` | 1 | `entry_thunk_7e1f78a0` | `call` to the body directly after it (`0x7e1f78a8`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f78bd` | 3 | `entry_thunk_7e1f78bd` | `call` to the body directly after it (`0x7e1f78c5`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f7978` | 1 | `entry_thunk_7e1f7978` | `call` to the body directly after it (`0x7e1f7980`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f8877` | 1 | `obj_clear_f332_7e1f8877` | `*(this+332) = 0`. | pattern scan |
| `0x7e1f88c3` | 1 | `entry_thunk_7e1f88c3` | `call` to the body directly after it (`0x7e1f88cb`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f8917` | 1 | `entry_thunk_7e1f8917` | `call` to the body directly after it (`0x7e1f891f`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f8934` | 2 | `entry_thunk_7e1f8934` | `call` to the body directly after it (`0x7e1f893c`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f8a73` | 2 | `obj_clear_f336_7e1f8a73` | `*(this+336) = 0`. | pattern scan |
| `0x7e1f8b11` | 2 | `entry_thunk_7e1f8b11` | `call` to the body directly after it (`0x7e1f8b19`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f8c12` | 1 | `entry_thunk_7e1f8c12` | `call` to the body directly after it (`0x7e1f8c1a`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f8c69` | 1 | `entry_thunk_7e1f8c69` | `call` to the body directly after it (`0x7e1f8c71`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f8d6e` | 3 | `entry_thunk_7e1f8d6e` | `call` to the body directly after it (`0x7e1f8d76`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1f8e39` | 1 | `obj_clear_f368_7e1f8e39` | `*(this+368) = 0`. | pattern scan |
| `0x7e1fa34e` | 1 | `entry_thunk_7e1fa34e` | `call` to the body directly after it (`0x7e1fa356`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fa4a8` | 1 | `entry_thunk_7e1fa4a8` | `call` to the body directly after it (`0x7e1fa4b0`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fa602` | 1 | `entry_thunk_7e1fa602` | `call` to the body directly after it (`0x7e1fa60a`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fa75c` | 1 | `entry_thunk_7e1fa75c` | `call` to the body directly after it (`0x7e1fa764`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fa8b6` | 1 | `entry_thunk_7e1fa8b6` | `call` to the body directly after it (`0x7e1fa8be`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1faa10` | 1 | `entry_thunk_7e1faa10` | `call` to the body directly after it (`0x7e1faa18`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fab6a` | 1 | `entry_thunk_7e1fab6a` | `call` to the body directly after it (`0x7e1fab72`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1facc4` | 1 | `entry_thunk_7e1facc4` | `call` to the body directly after it (`0x7e1faccc`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fae1e` | 1 | `entry_thunk_7e1fae1e` | `call` to the body directly after it (`0x7e1fae26`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1faf78` | 1 | `entry_thunk_7e1faf78` | `call` to the body directly after it (`0x7e1faf80`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fb0d2` | 1 | `entry_thunk_7e1fb0d2` | `call` to the body directly after it (`0x7e1fb0da`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fb22c` | 1 | `entry_thunk_7e1fb22c` | `call` to the body directly after it (`0x7e1fb234`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fb386` | 1 | `entry_thunk_7e1fb386` | `call` to the body directly after it (`0x7e1fb38e`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fb4e0` | 1 | `entry_thunk_7e1fb4e0` | `call` to the body directly after it (`0x7e1fb4e8`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fb63f` | 1 | `entry_thunk_7e1fb63f` | `call` to the body directly after it (`0x7e1fb647`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fb799` | 1 | `entry_thunk_7e1fb799` | `call` to the body directly after it (`0x7e1fb7a1`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fb8f3` | 1 | `entry_thunk_7e1fb8f3` | `call` to the body directly after it (`0x7e1fb8fb`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fba4d` | 1 | `entry_thunk_7e1fba4d` | `call` to the body directly after it (`0x7e1fba55`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fbba7` | 1 | `entry_thunk_7e1fbba7` | `call` to the body directly after it (`0x7e1fbbaf`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fbd01` | 1 | `entry_thunk_7e1fbd01` | `call` to the body directly after it (`0x7e1fbd09`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fbe5b` | 1 | `entry_thunk_7e1fbe5b` | `call` to the body directly after it (`0x7e1fbe63`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fbfb5` | 1 | `entry_thunk_7e1fbfb5` | `call` to the body directly after it (`0x7e1fbfbd`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fc10f` | 1 | `entry_thunk_7e1fc10f` | `call` to the body directly after it (`0x7e1fc117`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fc1bd` | 1 | `entry_thunk_7e1fc1bd` | `call` to the body directly after it (`0x7e1fc1c5`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fc317` | 1 | `entry_thunk_7e1fc317` | `call` to the body directly after it (`0x7e1fc31f`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fc471` | 1 | `entry_thunk_7e1fc471` | `call` to the body directly after it (`0x7e1fc479`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fc5cb` | 1 | `entry_thunk_7e1fc5cb` | `call` to the body directly after it (`0x7e1fc5d3`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fc725` | 1 | `entry_thunk_7e1fc725` | `call` to the body directly after it (`0x7e1fc72d`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fc87f` | 1 | `entry_thunk_7e1fc87f` | `call` to the body directly after it (`0x7e1fc887`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fc9d9` | 1 | `entry_thunk_7e1fc9d9` | `call` to the body directly after it (`0x7e1fc9e1`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fcb38` | 1 | `entry_thunk_7e1fcb38` | `call` to the body directly after it (`0x7e1fcb40`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fcc92` | 1 | `entry_thunk_7e1fcc92` | `call` to the body directly after it (`0x7e1fcc9a`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fcdec` | 1 | `entry_thunk_7e1fcdec` | `call` to the body directly after it (`0x7e1fcdf4`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fcf46` | 1 | `entry_thunk_7e1fcf46` | `call` to the body directly after it (`0x7e1fcf4e`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fd0a0` | 1 | `entry_thunk_7e1fd0a0` | `call` to the body directly after it (`0x7e1fd0a8`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fd1fa` | 1 | `entry_thunk_7e1fd1fa` | `call` to the body directly after it (`0x7e1fd202`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fd394` | 1 | `entry_thunk_7e1fd394` | `call` to the body directly after it (`0x7e1fd39c`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fd4ee` | 1 | `entry_thunk_7e1fd4ee` | `call` to the body directly after it (`0x7e1fd4f6`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fd648` | 1 | `entry_thunk_7e1fd648` | `call` to the body directly after it (`0x7e1fd650`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fd8f6` | 2 | `obj_set1_f252_7e1fd8f6` | `*(this+252) = 1`. | pattern scan |
| `0x7e1fd8ff` | 1 | `obj_clear_f328_7e1fd8ff` | `*(this+328) = 0`. | pattern scan |
| `0x7e1fd953` | 1 | `entry_thunk_7e1fd953` | `call` to the body directly after it (`0x7e1fd95b`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fd9a7` | 2 | `entry_thunk_7e1fd9a7` | `call` to the body directly after it (`0x7e1fd9af`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fdaa3` | 2 | `obj_clear_f332_7e1fdaa3` | `*(this+332) = 0`. | pattern scan |
| `0x7e1fdb45` | 2 | `entry_thunk_7e1fdb45` | `call` to the body directly after it (`0x7e1fdb4d`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fdc79` | 1 | `entry_thunk_7e1fdc79` | `call` to the body directly after it (`0x7e1fdc81`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fdc96` | 3 | `entry_thunk_7e1fdc96` | `call` to the body directly after it (`0x7e1fdc9e`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fdd63` | 1 | `obj_clear_f344_7e1fdd63` | `*(this+344) = 0`. | pattern scan |
| `0x7e1fdee1` | 2 | `entry_thunk_7e1fdee1` | `call` to the body directly after it (`0x7e1fdee9`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fdfb1` | 1 | `entry_thunk_7e1fdfb1` | `call` to the body directly after it (`0x7e1fdfb9`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fe6d8` | 1 | `obj_clear_f328_7e1fe6d8` | `*(this+328) = 0`. | pattern scan |
| `0x7e1fe736` | 1 | `entry_thunk_7e1fe736` | `call` to the body directly after it (`0x7e1fe73e`, register-save mask `0x20`, frame 8) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fe7d0` | 1 | `entry_thunk_7e1fe7d0` | `call` to the body directly after it (`0x7e1fe7d8`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fe824` | 1 | `entry_thunk_7e1fe824` | `call` to the body directly after it (`0x7e1fe82c`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fe899` | 2 | `entry_thunk_7e1fe899` | `call` to the body directly after it (`0x7e1fe8a1`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fe9a1` | 2 | `obj_clear_f332_7e1fe9a1` | `*(this+332) = 0`. | pattern scan |
| `0x7e1fea43` | 2 | `entry_thunk_7e1fea43` | `call` to the body directly after it (`0x7e1fea4b`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1feb73` | 1 | `entry_thunk_7e1feb73` | `call` to the body directly after it (`0x7e1feb7b`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1feb90` | 3 | `entry_thunk_7e1feb90` | `call` to the body directly after it (`0x7e1feb98`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1fef9e` | 1 | `entry_thunk_7e1fef9e` | `call` to the body directly after it (`0x7e1fefa6`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ff0f8` | 2 | `entry_thunk_7e1ff0f8` | `call` to the body directly after it (`0x7e1ff100`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ff571` | 2 | `obj_set1_f252_7e1ff571` | `*(this+252) = 1`. | pattern scan |
| `0x7e1ff57a` | 1 | `obj_clear_f332_7e1ff57a` | `*(this+332) = 0`. | pattern scan |
| `0x7e1ff5c6` | 1 | `entry_thunk_7e1ff5c6` | `call` to the body directly after it (`0x7e1ff5ce`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ff61c` | 1 | `entry_thunk_7e1ff61c` | `call` to the body directly after it (`0x7e1ff624`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ff639` | 2 | `entry_thunk_7e1ff639` | `call` to the body directly after it (`0x7e1ff641`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ff76e` | 2 | `obj_clear_f336_7e1ff76e` | `*(this+336) = 0`. | pattern scan |
| `0x7e1ff80c` | 2 | `entry_thunk_7e1ff80c` | `call` to the body directly after it (`0x7e1ff814`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ff907` | 1 | `entry_thunk_7e1ff907` | `call` to the body directly after it (`0x7e1ff90f`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ff958` | 1 | `entry_thunk_7e1ff958` | `call` to the body directly after it (`0x7e1ff960`, register-save mask `0xf0`, frame 60) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ffa9c` | 4 | `entry_thunk_7e1ffa9c` | `call` to the body directly after it (`0x7e1ffaa4`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e1ffeff` | 7 | `entry_thunk_7e1ffeff` | `call` to the body directly after it (`0x7e1fff07`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e200142` | 1 | `entry_thunk_7e200142` | `call` to the body directly after it (`0x7e20014a`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e200278` | 1 | `entry_thunk_7e200278` | `call` to the body directly after it (`0x7e200280`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e2003ae` | 2 | `entry_thunk_7e2003ae` | `call` to the body directly after it (`0x7e2003b6`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e20051e` | 1 | `entry_thunk_7e20051e` | `call` to the body directly after it (`0x7e200526`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e20057f` | 1 | `entry_thunk_7e20057f` | `call` to the body directly after it (`0x7e200587`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e200cf2` | 1 | `obj_clear_f332_7e200cf2` | `*(this+332) = 0`. | pattern scan |
| `0x7e200d3e` | 1 | `entry_thunk_7e200d3e` | `call` to the body directly after it (`0x7e200d46`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e200d94` | 1 | `entry_thunk_7e200d94` | `call` to the body directly after it (`0x7e200d9c`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e200db1` | 2 | `entry_thunk_7e200db1` | `call` to the body directly after it (`0x7e200db9`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e200ee7` | 2 | `obj_clear_f336_7e200ee7` | `*(this+336) = 0`. | pattern scan |
| `0x7e200f85` | 2 | `entry_thunk_7e200f85` | `call` to the body directly after it (`0x7e200f8d`, register-save mask `0xf0`, frame 44) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e201080` | 1 | `entry_thunk_7e201080` | `call` to the body directly after it (`0x7e201088`, register-save mask `0xb0`, frame 28) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e2010d1` | 1 | `entry_thunk_7e2010d1` | `call` to the body directly after it (`0x7e2010d9`, register-save mask `0xf0`, frame 60) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e201215` | 4 | `entry_thunk_7e201215` | `call` to the body directly after it (`0x7e20121d`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e201683` | 6 | `entry_thunk_7e201683` | `call` to the body directly after it (`0x7e20168b`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e2018c6` | 1 | `entry_thunk_7e2018c6` | `call` to the body directly after it (`0x7e2018ce`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e2019fc` | 1 | `entry_thunk_7e2019fc` | `call` to the body directly after it (`0x7e201a04`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e201b32` | 1 | `entry_thunk_7e201b32` | `call` to the body directly after it (`0x7e201b3a`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e201c68` | 1 | `entry_thunk_7e201c68` | `call` to the body directly after it (`0x7e201c70`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e201cc9` | 1 | `entry_thunk_7e201cc9` | `call` to the body directly after it (`0x7e201cd1`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e243c1b` | 2 | `obj_set1_f6888_7e243c1b` | `*(this+6888) = 1`. | pattern scan |
| `0x7e269ccf` | 2 | `obj_clear_f680_7e269ccf` | `*(this+680) = 0`. | pattern scan |
| `0x7e34ddf0` | 1 | `obj_set1_f200_7e34ddf0` | `*(this+200) = 1`. | pattern scan |
| `0x7e34f2b5` | 1 | `obj_set1_f200_7e34f2b5` | `*(this+200) = 1`. | pattern scan |
| `0x7e352cd4` | 1 | `obj_set1_f200_7e352cd4` | `*(this+200) = 1`. | pattern scan |
| `0x7e7fadfd` | 1 | `entry_thunk_7e7fadfd` | `call` to the body directly after it (`0x7e7fae05`, register-save mask `0x00`, frame 0) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e83364d` | 1 | `obj_set1_f144_7e83364d` | `*(this+144) = 1`. | pattern scan |
| `0x7e87e83e` | 1 | `entry_thunk_7e87e83e` | `call` to the body directly after it (`0x7e87e846`, register-save mask `0xe0`, frame 20) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
| `0x7e88d140` | 1 | `entry_thunk_7e88d140` | `call` to the body directly after it (`0x7e88d148`, register-save mask `0x00`, frame 4) and `ret`: the separate entry stub the compiler emits in front of a body that saves registers. | pattern scan |
