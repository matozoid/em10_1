# Firmware symbol map (E-M10 Mark I, body fw 1.4)

Master index of **named / confirmed** runtime symbols recovered by static RE of the decoded firmware
container (`OLY_E_113_1400_0000_0000.BIN`). One place to look up "what lives at address X" and to see
coverage. Per-subsystem detail lives in the linked docs; this file is the cross-reference.

- **Runtime base = `0x7d991020`.** Block-0 code/data resolve at `fileoff + 0x7d991020` (NOT the
  container's stated load `0x40300000`; xrefs only resolve against `0x7d991020`). See
  `docs/firmware/memory-map.md`, `docs/firmware/flash-storage.md`.
- Architecture: Panasonic MN10300 / AM33. Immediates render **decimal** in our objdump build.
- Regenerate the full address→doc index with `python3 -I tools/symbol_index.py` (or
  `--once 0x7de57532` to locate one address). This curated table is the important subset.

## Memory / layout anchors
| address | symbol | role | source |
|---|---|---|---|
| `0x7d991020` | `RUNTIME_BASE` | block-0 exec/reset base; reset entry | `memory-map.md`, `flash-storage.md` |
| `0x40300000` | `BLK0_LOAD` | container packaging load addr of block 0 (not exec base) | `container-format.md`, `blocks.md` |
| `0x41500000` | `BLK1_LOAD` | container load addr of block 1 | `blocks.md` |
| `0x42d00000` | `BLK2_LOAD` | container load addr of block 2 | `blocks.md` |
| `0x4035fb66` | `TASK_NAME_TBL` | id→name table, 145 records, 26-byte stride | `rtos-tasks.md` |
| `0x7d9a9384` | `TASK_CREATE_TBL` | task-creation descriptors, 134 records, 28-byte stride (`+0` id, `+12` fn, `+16` prio, `+20` stack) | `rtos-tasks.md` |
| `0x6000xxxx` | `FIRMUP_SCRATCH` | firmup RAM scratch (`0x60001130`, `0x6044cbc4`+) | `flash-storage.md`, `camera-fw-update.md` |

## RTOS tasks (entry points — confirmed via two-table cross-join)
| entry | task id | name | prio | stack | source |
|---|---|---|---|---|---|
| `0x7de57532` | `0x14` | `FIRMUP_SRV` — SD `DCOLYMP` body-fw scanner/flasher | 8 | `0x800` | `rtos-tasks.md`, `camera-fw-update.md` |
| `0x7de9d4f4` | `0x13` | `FIRMUP_CLI` — firmup client half | 11 | `0x800` | `rtos-tasks.md` |
| `0x7da887f7` | `0x53` | `FIRMUP_LED` — update-LED driver | 11 | `0x400` | `rtos-tasks.md` |
| `0x7db87ef8` | `0x41` | `SYSFMEM` — flash-memory manager (queue serialiser) | 4 | — | `flash-storage.md` |
| `0x7daa5466` | `0x1a` | `LENS_FIRM_UP` — lens-firmware updater | 4 | `0x700` | `rtos-tasks.md` |
| `0x7de400ae` | `0x34` | `REC_MAIN` — record pipeline main | 11 | `0x3700` | `rtos-tasks.md` |
| `0x7dafa287` | `0x46` | `TAKE_MAIN` | 4 | `0x500` | `rtos-tasks.md` |
| `0x7dfc0061` | `0x63` | `CA_MAIN` — camera-app main | 11 | `0x9000` | `rtos-tasks.md` |

## Firmware-update / flash path
| address | symbol | role | source |
|---|---|---|---|
| `0x7de57e24` | `firmup_validate` | top of pre-flash image validator (fail-closed) | `camera-fw-update.md` |
| `0x7da8883e` | `region_table_parse` | walks ≤32-record region table; size-sum check (err `0x3321`) | `camera-fw-update.md` |
| `0x7da88820` | `rgn_hdr_get+8` | region-header accessor: `u32 @+8` (data ptr/fieldA) | `symbol-map.md` |
| `0x7da88826` | `rgn_hdr_get+12` | region-header accessor: `u32 @+12` (payload length) | `symbol-map.md` |
| `0x7da88838` | `rgn_hdr_get+22` | region-header accessor: `u8 @+22` (type selector) | `symbol-map.md` |
| `0x7de58985` | `firmup_check_id` | image-id gate: id byte `== 0x45 'E'` (via `0x7da8880b`) | `camera-fw-update.md` |
| `0x7de573d1` | `usr_checksum` | header↔tail 20-byte duplicate-array check (err `0x3202`/`0x3204`); NOT a payload hash | `camera-fw-update.md`, `patching-pipeline.md` |
| `0x7de58970` | `TYPE_FIRMUP_WRITE_OK` | validation-passed → begin write | `camera-fw-update.md` |
| `0x7de57dd1` | `SUCCESS_REBOOT` | post-flash success/reboot | `camera-fw-update.md` |
| `0x7d9cc860` | `firmup_apply_dispatch` | 9-slot component-descriptor apply loop | `flash-storage.md` |
| `0x7d9ca000`–`0x7d9cd900` | `fmem_phys_leaf` | physical NAND read/erase/program (BML/STL) | `flash-storage.md` |
| `0x7d9cdaaa` | `flash_err_handler` | common write/erase error bail | `flash-storage.md` |
| `0x7e21d6dc` | `startFirmUp` | USB-link firmware-update entry | `usb-ptp.md`, `camera-fw-update.md` |

## Open / to-label (tracked across loop ticks)
- `0x7da82530` per-slot apply helper; `0x7d9929ce`/`0x7d9928ee` fmem commit — not fully decoded
  (NAND-controller MMIO register sequence one hop down). `flash-storage.md`.
- `0x7da837b0` — generic compare/copy helper reused by `usr_checksum` id==2 path and region id-check;
  exact semantics (memcmp vs DMA) not pinned.
- Imaging/PTP/WiFi task entries beyond the firmup set — many named in `rtos-tasks.md` but entry
  functions not yet decoded.

> Maintenance: when a tick confirms a new symbol, add a row here (address, name, role, source doc) and
> cite the evidence in the subsystem doc. Keep names stable so cross-doc references resolve.
