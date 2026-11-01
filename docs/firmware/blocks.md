# Firmware 1.4 block contents (E-M10 Mark I)

Decoded with `tools/omfw.py dec`. Container: `container-format.md`.

| blk | load | used | content |
|---|---|---|---|
| 0 | 0x40300000 | ~0x1000000 of 0x11fffc0 (rest 0xFF) | **All code.** MN103/AM33, RTOS with 145 tasks (`rtos-tasks.md`), strings, tables |
| 1 | 0x41500000 | ~0xd00000 of 0x17fffc0 (rest 0x00) | Resource pack: UI bitmaps etc. (4-bit/indexed pixel data) |
| 2 | 0x42d00000 | ~0x800000 of 0x18fffc0 (rest mostly 0x00) | Data tables (sub-directories, not MN103 code by byte stats) |

## Block 1 / 2 directory header
Both start with a directory of 16-byte records `{u32 addr, u32 size, 0, 0}` (little endian, addr is absolute load-space, sizes are multiples of 0x200). Consecutive entries are contiguous.
- blk1: ~70 entries from 0x800. First is 0x3d8800 bytes (0x41500800..0x418d9000), then ~0x1f400-byte images, then ~0x3a00-0x6000 small items, last 0x39a600.
- blk2: 7 entries: 0x763c00 @0x42d00400, 1 MB, 1 MB, 3 MB, 2 MB, 64 KB, 80 KB. Entry 0 itself starts with a nested directory `{0x42d00800,0x2400}, {0x42f40800,0x842}...`.

Contents of the sub-resources are NOT yet decoded (UNVERIFIED guesses: UI graphics/fonts/sound in blk1, ISP/lens/calibration tables in blk2).

## Implication
Understanding "how the firmware works" = reverse engineering block 0 (code) plus decoding resources in blocks 1 and 2.
