# OM/Olympus firmware BIN container (VERIFIED on E-M10 Mark I 1.4)

Source: static read of the community tool's `vendor.container_codec` module (docstrings + bytecode); reimplemented
clean-room in `tools/omfw.py` (stdlib only). Verified: all 3 blocks of `OLY_E_113_1400_0000_0000.BIN` pass the footer
checksum, and all 9 community patch "old" byte strings match the decoded image at their offsets.

File = sequence of blocks. Block = 32 B header + `dlen` data + 32 B footer (`dlen` multiple of 16).

Header (little endian): `[0:2]="OE"`, `[2:4]` model id bytes (`11 30` = 1130), `@8 load addr u32`, `@12 dlen u32`,
`@16 ver u32` (0x1400 = 1.4 in block 0), `@20 u2 u32` (block type/index), rest 0.
Footer: `hdr[:28]` echo + `V u32` where `V + sum32LE(plain) + 2*sum32LE(hdr[:28]) == 0 (mod 2^32)`.
Data cipher (per 16-byte chunk): `plain[j] = enc[P[j]] ^ 0xFF`, `P=[1,3,0,2,6,4,7,5,11,10,9,8,13,14,12,15]`.
No compression, no signature seen: the only integrity check is this additive checksum. (Camera-side checks unverified.)

## E-M10 Mark I 1.4 blocks
| blk | file off | load addr | len | ver | u2 |
|---|---|---|---|---|---|
| 0 | 0x0 | 0x40300000 | 0x11fffc0 (18.9 MB) | 0x1400 | 0x100 |
| 1 | 0x1200000 | 0x41500000 | 0x17fffc0 (25.2 MB) | 0 | 0x101 |
| 2 | 0x2a00000 | 0x42d00000 | 0x18fffc0 (26.2 MB) | 0x100 | 0x106 |
Strings (block 0): FIRMUP_CLI/SRV, PC_PTP, PTPCOM, WIFI_HTTPD, WIFI_REMOCON_*, LENS_FIRM_UP, BC_FIRMUP.
Block 0 is the main code (community patches target it; image base for patch offsets = block-relative offset).

## Community patch model (profiles.json in the community exe, 23 camera profiles, 47 MB)
Per profile: `source_sha256` of stock BIN, features -> patches `{block, offset, old(b64), new(b64), label}`;
patches are applied to the DECODED block, then re-encoded + footer recomputed. E-M10 Mark I has one feature, `ring-native`
(Panasonic aperture ring), 9 patches: loader_patch@427, payload_cave@159728 (2201 B of 0xFF replaced by code), reset/init/
parser/request/callback/guard/input hooks (@1124507..1379078). Marked by the author "TEST_CANDIDATE: structure & CPU verified,
real device NOT verified" (user reports of it working were in the release notes; unverified here).
`runtime_base` 2107183136 = 0x7D9D... (see profiles.json). Patch tool/CPU emulation modules: `engine`, `om1_*`, `om5ii_*` in the exe.
Install: SD card `DCOLYMP/E1139999.BIN`.
