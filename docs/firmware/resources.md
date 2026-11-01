# Blocks 1 and 2: resource data (not code)

Both blocks start with a directory of 16-byte records `{u32 addr, u32 size, 0, 0}`
(load-space addresses, sizes multiples of 0x200). `tools/resdump.py blk load outdir`
splits a decoded block into entries. Extracted data is vendor content: keep local.

## Block 1 (load 0x41500000) — UI resources, ~70 entries
| entries | content |
|---|---|
| 0 (0x3d8800 B) | packed pixel/bitmap data (format not yet decoded) |
| 1–34 | **localized UI string tables**, UTF-16LE, NUL-separated, ~2355 strings each, one per language (Bulgarian, Chinese x2, Czech, Danish, Dutch?, Greek, ... Thai, Turkish, Ukrainian?). Strings contain `@Axxx@` placeholders for icon/glyph codes. Dump with `tools/strtab.py`. |
| 35+ | binary tables starting with small u16 headers (e.g. cell size 30x34 at +44); look like bitmap font / glyph data. Not decoded. |

## Block 2 (load 0x42d00000) — 7 entries, nested directories
| entry | content |
|---|---|
| 0 (0x763c00 B) | nested dir of 16 sub-entries. Sub 0 (0x240000) dense non-JPEG data; later subs carry **JPEG streams** (`FFD8` at +0x20; standard Huffman tables) — likely GUI/scene images or thumbnails. Pairs of subs: one image, one near-empty table. |
| 1,2,3,4 | sparse (3–11% nonzero) regions of 0x200–0x4000 B sub-records, mostly erased/zero: look like pre-allocated settings/calibration storage |
| 5,6 | denser (40–54%) small tables |

## String-table notes
Entry order follows language; e022 is Dutch. Strings may contain embedded newlines
(line-wrapped UI text). Example Dutch indices: 1766 "Privéverbinding", 1765 one-time
connection, 1763 SSID setting, 1767 password setting, 1975 "SSID", 1976 "Password",
2052 "Verbinding met smartphone". `@Axxx@` = inline icon glyph codes, not text: `@A078@` = Wi-Fi icon, `@A029@` = MENU button icon
(idx 2343 "Einde @A078@@A029@" renders as "Einde (Wi-Fi)(MENU)"; idx 2064 "Altijd @A078@-verbinding").
Glyph images presumably live in the block 1 binary entries 0 / 35+. Index = position in NUL-split list (empties count).

## JPEG extraction (`tools/jpgextract.py entry.bin outdir`)
Carves `FFD8FF..FFD9` streams by walking markers to SOS then scanning to EOI.
- Entry 0: 29 JPEGs (sizes 12 KB–588 KB). Sampled two: black frames with a rough
  white border = **art-filter frame/vignette overlay masks**. One per aspect/size
  combination (3:2 and 4:3 at 4608 wide, 16:9 at 1920/1280, 1:1 at 3456, smaller ones).
  Not photographs. Remaining ones unviewed; may include other filter overlays.
- Entry 5: 3 JPEGs = **Wi-Fi screen UI assets**: 1x920 gradient strip, 626x180 dark gradient panel, 638x57 "OLYMPUS IMAGE SHARE" title banner (use unconfirmed; the camera Wi-Fi screen text — SSID, password, "Privéverbinding", QR instruction, "Einde <Wi-Fi icon><MENU icon>" — comes from the string tables, the QR is generated at runtime, so these may be only backgrounds/banner or belong to another screen). Entries 1–4, 6: none.
- Output goes to gitignored `firmware/stock/jpg2/`.

## Block 1 fonts (entries 35-68) — decoded
Entry 35+k pairs with string table 1+k (same language order; JP/KO/CJK entries are the big ones).
Header 0x5c bytes, then glyph run (`tools/glyphs.py`, verified by rendering: renders `/` and
`"` correctly). Per glyph: `u8 rows-1, u16 (w-1)<<4, u8 9`, then 32 rows of 2-bit
antialiased RLE bytes `level<<6 | (run-1)`. After the run: `{u32 ptr(0xbf......), u16 w, u16 h}`
index table (8 B/record, ptr is a runtime address). Latin entry has ~151 glyphs, Chinese ~664.
These hold **text only**; `@Axxx@` icons (Wi-Fi, MENU) were not found here.

## Entries 0 and 69 — icon/graphic candidates (partly understood)
Both contain ~5300/~10500 `0xbf......` pointer words in serialized records:
`{u16 w,u16 h,u16 adv,u16 4,0,0,u32 size,u32 ptr,0}` followed by 4-bit-palette RLE data
(byte = colour<<4 | run, run 0 ends a row). First glyph of entry 0 renders as a ring, so
this looks like the icon/symbol bank, but row widths do not add up cleanly (11 vs 13), so
the exact format is **not decoded**. Cleanest next step: find the renderer in block 0 and
read it, rather than guess.

## Resource loader (block 0, 0x7db66a1c, label `res_get_lensdefel_*` is borrowed)
`res_get(type, idx, ...)` switches on type 0..6 (+ 0x8000|n variants). It indexes a 16-byte
directory record `{addr,size,0,0}` at `table + idx*0x10`, then allocates and loads `size` bytes
(`FUN_7db67224(size,0x101)`). A bank-select branch (`7db66baa/7db66bb4`) picks RAM base
**0xbf06a000** (bank 0) or **0xbf46a000** (bank 1) — 4 MB apart, matching the pointer ranges
inside block 1 entry 0 (0xbf06a0..) and entry 69 (0xbf46a0..). So **entry 0 = icon/graphic
bank 0, entry 69 = bank 1**, each loaded to RAM and referenced by absolute pointers.
Font index tables use base 0xbfcaa000 (type 0 case: `FUN_7d9dbe94(0xbfcaa000)`).
Pointer->file offset relation for banks still unresolved (descriptor ptrs are not linear
with file layout), so icon pixel decode remains open. 
`tools/ghidra/ScalarRefs.java lo hi` lists code operands in an address range.

## Status
Classified by structure/statistics only; formats unverified. Next: decode JPEG subs
(extract at `FFD8`), find which code references these addresses (block 0 runs at
load+0x3d691020, resources likely mapped separately), identify entry 0 bitmap format.
