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

## JPEG extraction (`tools/jpgextract.py entry.bin outdir`)
Carves `FFD8FF..FFD9` streams by walking markers to SOS then scanning to EOI.
- Entry 0: 29 JPEGs (sizes 12 KB–588 KB). Sampled two: black frames with a rough
  white border = **art-filter frame/vignette overlay masks**. One per aspect/size
  combination (3:2 and 4:3 at 4608 wide, 16:9 at 1920/1280, 1:1 at 3456, smaller ones).
  Not photographs. Remaining ones unviewed; may include other filter overlays.
- Entry 5: 3 JPEGs (unviewed). Entries 1–4, 6: none.
- Output goes to gitignored `firmware/stock/jpg2/`.

## Status
Classified by structure/statistics only; formats unverified. Next: decode JPEG subs
(extract at `FFD8`), find which code references these addresses (block 0 runs at
load+0x3d691020, resources likely mapped separately), identify entry 0 bitmap format.
