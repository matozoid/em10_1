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

### Block 2 entry 0: non-JPEG subs (2026-11-01)
Sub directory: 16-byte records at entry start, addr - 0x42d00400 = file offset. Subs 1-29 = the JPEGs below.
- **Sub 0** (off 0x400, 0x240000 B): ~0x23ffe0 bytes of i.i.d. 6-bit values (0..63), no spatial correlation at
  any row width; value frequencies are multiples of 1/256 (i.e. `LUT[rand8]`). A noise/grain or dither texture
  (Grainy Film art filter is a likely user); not a picture.
- **Subs 30-39** (0x6d8400 + k*0xa200, 41472 B each): 0x20-byte zero header, 160 rows x 128 u16 (120 used +
  8 zero pad), 10-bit values 0..1027, then trailer at u16 index 20720: `2013, 0x0a0a, 0x2f0e, ?, checksum`
  (date-like stamp 2013-10-10). Rendered 120x160 they are smooth masks: full frame, letterbox (two widths),
  pillarbox, rounded vignette, elliptical vignette. Low-res frame/shading maps, likely paired with the art-filter
  frame JPEGs or per-aspect shading. Orientation (120x160 vs transposed) unconfirmed.

### Block 2 entry 6 (0x14000 B)
Two subs: 0x43b74400 (0x6000 B) and 0x43b7a400 (0x8a00 B). 2 bytes per pixel, Y then chroma, Y only 0x00/0xfe,
chroma 0x00/0x80 (`fe80` = white, `0080` = black). Sub 0 at width 128 = black box with white border (128x96,
likely a placeholder/test frame). Sub 1 has a 32-px period of short white runs and no clean width: probably a
bit pattern / test table, not a UI picture. No photo-style backgrounds exist outside the block 2 JPEGs.

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
Callers of `res_get`: `api_tft_Get_OSD_ResourceAddr` (0x7dba50ec; args id, kind -> returns loaded buffer
address), `play_res_read`, `iseq_ps_if_res_read`, `phy_info`, `memory_addr`, etc. The OSD API is called only
from GUI class 0x7e3a472c vfn11/vfn12 (0x7e02f473 / 0x7e02f3fd, trace fmt `%1s %d %d`). Draw/blit
consumer and `@Axxx@` parser not yet located. Hand-decoding entry 0 row data gives inconsistent
row widths (13,13,13,11,...): rows may be delta-coded or use an unidentified code.
`tools/ghidra/ScalarRefs.java lo hi` lists code operands in an address range.

## Icon bank decode: dead ends (entry 0)
- Descriptor = 24 B `{u16 w=14, u16 h, u16 adv=22, u16 4, u16 0, u16 0, u32 size, u32 ptr(0xbf06a000+off), u32 0}`
  (141 found by scanning; w is always 14, h varies 13..194, adv 22). `ptr+size` matches desc end+8 in ~half.
- Tried: byte = colour<<4|run with run 0 = row end (rows inconsistent); row ends when sum of both nibbles == w
  (works on one 14x13 vertical-bar blob, fails elsewhere); fixed 5-byte rows. No consistent pixel start offset
  after the descriptor. Row counts ~19-20 irrespective of h.
- Likely consumer is the display HW OSD engine (`api_tft_init_OSD`), not a software blit. Next: trace OSD buffer
  fill / register programming from `api_tft_init_OSD` (0x7dba5074) instead of guessing bytes.
- `api_tft_Draw_Image` (0x7dba41c2) / `_Multi_Raw` (0x7dba4bcd) only fill a request block (src ptr, x/y/w/h, format code
  0x80/0x81/0x83/0x8e/0x90) and post it via `appexec_7db92a6b` / `FUN_7db92b39(3,0x10)`: drawing is delegated to another
  task/engine, so there is likely **no software decoder in block 0**. `api_tft_init_OSD` is a stub.
- Retested nibble-sum rows with region [ptr, desc) and both axis orders: 0 of 141 descriptors decode cleanly.
- `tools/ghidra/NibbleFuncs.java maxlen` finds small nibble-decode loops (no hit was a decoder).

## Icon bank: RLE pixel format (partly decoded, 2026-11-01)
- **Token = one byte `colour<<4 | (run-1)`** (run 1..16). Runs are **continuous across rows**: no row-end marker; a row
  is whenever the running sum reaches the image width. Colour 0 = transparent, 1 = edge/antialias, 4 = solid (palette
  index, palette not located yet).
- Verified on the first icon (entry 0 file offset 0x16, descriptor at 0x70): 18 wide x 14 high, 252 px exactly,
  symmetric shape. Descriptor `a=14` is therefore the **height** (the 14 in `{14, b}`), `b` is the **width**.
  Second icon: rows `04 10 41 10 03` = 13 px each, begins with `0c 0c` (two blank rows).
- Unresolved: the descriptor `ptr` does not point at the pixel start (icon 2: ptr lands mid-stream, 28 B after the
  first token). Pixel start sits 0-4 B after a short header (e.g. `15 c0 00 02`) following the previous descriptor.
  Icon 2's stream runs for ~20 rows, longer than `a=14`, so the descriptor semantics (height/width/ptr) are not fully
  understood. Descriptor variants also exist with the 4th u16 = 8 and adv 22..54 (~1000 candidates), mostly noise.
- Next: decode sequentially by walking the stream (row width from the descriptor), emit PNG sheet via PIL,
  then map `@Axxx@` codes to glyph indices.

### Record layout (confirmed 2026-11-01, supersedes "unresolved" above)
`[4B hdr][RLE pixels][0-3B pad][24B descriptor]`. The descriptor FOLLOWS its pixels. `ptr - base - 0x20` = record start
(hdr), `size` covers hdr + pixels, descriptor offset - (start+size) is 0..3 on all 1346 candidates. Descriptor `u16[0]`
(always 14) is not the height; **width = u16[1]**, height = total pixels / width (digits are 13x22). Hdr varies
(`15c00002`, `25100303`, ...), meaning unknown. `tools/icons.py entry.bin base out.png` decodes the 232 records whose
pixel count is a whole number of rows: digits 1-9, play/file, circle, flash bolt, disc, Wi-Fi file icons, panel frames.
The other ~1100 records do not divide by width (likely different hdr-selected encodings or multi-frame) - open.
Colour indices 0..4 seen mostly; index>4 exists (palette unknown, drawn magenta).

**Header byte 3 selects the encoding.** Records with `hdr[3]==2` (e.g. `15c00002`) decode cleanly with the
colour<<4|(run-1) RLE (232 of 232 whole-row). Records with `hdr[3]==3` (~1100, e.g. `25100303`, `2a100203`-style
digit/OSD glyphs and 8-wide `08700003` bitmaps) do NOT: token sums never divide by the width and show periodic
patterns (period 7-8 B) with colour nibbles up to 0xc. Probably a second format (multi-plane or different RLE).
Not yet decoded.

User-judged candidate sheets (2026-11-01): for `hdr[3]==3` records, reading tokens as `colour<<4 | run` (run = low
nibble, NOT run-1; zero-length runs allowed) gives structured grey areas and diagonal edges (record 0x854), unlike raw
1/2/4/8 bpp or run-1 RLE (noise). Row stride is not constant: best autocorrelation ~45 px for 0x854 although the
descriptor says w=34/adv=43, and diagonals skew between strides 44 and 46. So rows probably carry their own length or
end marker. Still undecoded.

Further hdr[3]==3 tests (user-judged noise): raw 1/2/4 bpp at byte strides 8/16/17 for record 0x854. Byte
autocorrelation peaks at stride 16 B (0.46) and multiples; 8-wide records (`08700003`, 50 B payload) show a 7-byte row
period with the last 4 nibbles of each 14-nibble row always 0 and alternating row types (possible interleaved
colour/alpha planes). Unresolved; entry 69 and `@Axxx@` mapping untouched.

Entry 69 (base 0xbf46a000): 1706 records, 160 with hdr[3]==2 (+52 whole-row hdr-3) decode via `tools/icons.py`: mode
box "P", label "PBH", rounded panel frames with a shadow edge (colour index >4, drawn magenta = likely
semi-transparent shadow), a big curved side panel. Same two-format split as entry 0.

Consumer search (2026-11-01): `api_tft_Draw_Image` (0x7dba41c2) re-confirmed as pure request marshalling. It maps
format 0x13->0x81, 0x12->0x80, 0x21->0x90, 0x16/0x07->0, copies src ptr, 4 rect u16 pairs, a u16 from the source
descriptor (+10) and a byte (+14), then posts via `FUN_7db92b39(3,0x10)`. No pixel decode in block 0, so the second
encoding is almost certainly consumed by the display engine (separate core or HW RLE blitter). Format code is chosen by
the caller; the `hdr[3]` 2/3 split likely corresponds to blitter pixel formats. Static analysis of block 0 cannot
resolve it; remaining routes are more blind decoding or finding the engine firmware.

### Icon formats SOLVED (2026-11-01, supersedes the open notes above)
Header (4 B, same as font glyphs): `H = (b0 | (b1&15)<<8) + 1`, `W = ((b1 | b2<<8) >> 4) + 1`, `b3` = format.
Header W equals descriptor width on every record. Descriptor `kind` = output bits per pixel (4 for fmt 2, 8 for fmt 3).

| fmt | encoding | verified |
|---|---|---|
| 2 | byte RLE `colour<<4 \| (run-1)`, runs continue across rows, 4-bit colour (0 = transparent) | 192/192 e0 |
| 3 | bitstream, LSB-first, in 64-bit words. Token = 10 bits: 2-bit `run-1` + 8-bit CLUT index. A token never straddles a 64-bit word boundary (leftover bits are zero padding, skip to next word). Runs end at each row end. | 1154/1154 e0, 1546/1546 e69, exact W*H |
| 9 | font glyph (`tools/glyphs.py`) | |

Format 3 explains earlier dead ends: max run 4 px gives the 2.667 bit/px uniform panels (6 tokens = 24 px per 64-bit
word). Index 0 = transparent; ~109 distinct indices (max ~0x6f) used in entry 0.

**Palettes (found 2026-11-01).** Block 0 file offset 0x382ec0 holds the ROM initializer of the `.data` table at RAM
0x6045e020: 58 pointers indexed by palette ID (ID 0 and 58+ null). Each points to `{u32 count=256, u32 ptr}` followed
by 256 x **ARGB8888** (stride 0x408). Entry 0 = `00ffffff` (transparent), 4 = `fffefefe` white, 0x10 = `ff000000`.
Reader: `FUN_7e23c7d0(id)` returns `table[id]`; `FUN_7e337f49(layer,id)` passes `(entry+4)` to `FUN_7e226722(layer,
ncolours)` (layer 1 = 16 colours, 2 = 256, 3 = 8); `cw_setColorPalette` / `GPISetPalette` push entries to the display
engine byte-wise (R,G,B from bits 23..0, alpha separately). `SetPalette_7e337fa3(mode)` loads triples (k-1, k, k-2)
into layers 1/2/3: mode 1 -> 0x2f/0x30/0x2e, 2 -> 8/9/7, 3 -> 0xe/0xf/0xd, 4 -> 5/6/4, 5 -> 0x2a/0x11/0x10,
6 -> 0xb/0xc/0xa, 7 -> 0x2c/0x2d/0x2b, 8 -> 0x32/0x33/0x31, 9 -> 0x35/0x36/0x34, 10 -> -/3/-, 11 -> -/2/-.
Log strings name the modes (Shooting, LV SCP, SCP, LV Guide, Play-Menu, Play Overall, LV Guide Hint, TOP_MENU,
MODE_GUIDE, MOVE_SHOOTING, SELF_ADJ); exact mode->string mapping not yet read.
Format-3 icons render correctly with ID 9. Format-2 icons look too dark with ID 8 (16-colour layer); their real
palette assignment is open.

Entry 0 tail (0x3b1e44-end): a 3525-entry table of `0xbf......` pointers (global image ID -> record, spanning
entries 0 and 69, likely the `@Axxx@`/image-ID index), then format-1 records (`b3=1`, 32 px tall, 4-bit nibbles,
background nibble 3), probably inline text icons. ID table entry = RAM addr of record start + 8 (record start
addr = bank base + file offset). 3047 of 3525 IDs resolve to decoded fmt-2/3 records (1346/1346 in e0, 1701/1706 in
e69, 1:1) found by the descriptor scan; the other 478 have no 24-byte descriptor. Of those, 218 carry a fmt-2/3
header and decode exactly via the ID table alone (`id_records()` in `tools/icons.py`; size unknown, decoders stop at
W*H): these are the wide images (>= 600 px): 640x480 / 720x480 / 720x405 / 640x360 live-view composition grids
(diagonals, thirds, 4x4, scale, aspect-ratio frames), 617xN / 620xN / 624xN dark translucent menu panels, 814x558 /
824x54 / 720x78 panel frames and title bars, 642xN dotted grids. All fmt 2 (16-colour layer). Five 820-wide "fmt 3"
hits in the fmt-1 tail are misparses; ~250 IDs have non-fmt-2/3 headers (fmt-1 region, plus odd ID 0 -> fmt 192,
IDs 1625/1626 -> fmt 15). Having an ID does not imply use; the bank
is likely shared across bodies. Which IDs block 0 actually draws: not investigated.
Sheet colours: palette ID 3 default, ID 6 for exposure-comp scale (user-judged); no single palette fits all icons.

Content (entry 0): digits/7-seg fonts in several sizes, PASM/iAUTO/scene/ART 1-12/ART BKT mode icons, flash
compensation labels, Wi-Fi, MENU/OK/touch buttons, battery, sliders, panel frames. `tools/icons.py entry.bin base_hex
out_prefix [--fmt 2|3]` writes paged sheets (gitignored, vendor data).

## Status
Classified by structure/statistics only; formats unverified. Next: decode JPEG subs
(extract at `FFD8`), find which code references these addresses (block 0 runs at
load+0x3d691020, resources likely mapped separately), identify entry 0 bitmap format.
