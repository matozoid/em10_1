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
| `0xa0000000`–`0xa0fc7860` | `GLOBAL_DATA` | main SDRAM `.data`/`.bss` + global pointer cells (2447 distinct refs in block 0, dense at `0xa0a3`–`0xa0a9`); cached DRAM data segment | `symbol-map.md` |
| `0xa0a5c970` | `descriptor_gate_cell` | global pointer cell read by the ring-feature descriptor gate (`flags_offset 560`, `flag_mask 128`) | `community-dbfw-tool.md` |

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

## Communication tasks — PTP / USB / WiFi (entries, confirmed via creation table `0x7d9a9384`)
Important for the app/protocol RE (host link + WiFi remote). All extracted by walking the task-creation
table; names cross-joined from `0x4035fb66`.
| entry | task id | name | prio | stack |
|---|---|---|---|---|
| `0x7e7d8dcf` | `0x24` | `PC_PTP` — PTP command task (host link) | 4 | `0x518` |
| `0x7e7cf804` | `0x67` | `PTPASYNC` — async PTP events | 11 | `0x800` |
| `0x7d9eb34c` | `0x66` | `PTPCOM` — PTP transport/comm | 10 | `0x600` |
| `0x7e7d9b3a` | `0x26` | `PC_USB` — USB device task | 4 | `0x718` |
| `0x7e7d9d2e` | `0x27` | `PC_USBPNP` — USB plug-and-play | 4 | `0x518` |
| `0x7e7dd991` | `0x28` | `PC_USBSRV` — USB service | 4 | `0x318` |
| `0x7e7d79b8` | `0x22` | `PC_HOSTCOM` — host command dispatch | 4 | `0x318` |
| `0x7e7d8e15` | `0x21` | `PC_EVENT` — host event push | 4 | `0x318` |
| `0x7e7d8fec` | `0x25` | `PC_UAM` — USB access manager | 4 | `0x318` |
| `0x7dd71a55` | `0x20` | `PC_1394PNP` — FireWire PnP (legacy) | 9 | `0x500` |
| `0x7e7d7d46` | `0x23` | `PC_I1394` — FireWire transport (legacy) | 4 | `0x718` |
| `0x7de2d14e` | `0x7a` | `WIFI_REMOCON_THROUGH` — WiFi remote-control pass-through | 4 | `0x1000` |
| `0x7dd6b376` | `0x6d` | `EYEFI` — Eye-Fi SD WiFi card task | 4 | `0x400` |

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

## Hottest helpers (by block-0 call count) — global registry / accessors
Ranked by direct `call` xrefs; these dominate the call graph, so naming them makes most disassembly
readable.
| address | xrefs | symbol | role | source |
|---|---|---|---|---|
| `0x7e207498` | 12294 | `obj_get_f104` | field getter: `return *(a0+104)` (hottest single call target — `+104` is a very hot object field) | `symbol-map.md` |
| `0x7dfc01bf` | 10930 | `registry_get` | bounds-checked indexed get on a global singleton collection: fetch `get_singleton()`, then `idx_in_bounds` before access | `symbol-map.md` |
| `0x7dfc0312` | — | `get_singleton` | lazy-init accessor for global singleton at RAM cell `0x6044cf18` (inits via `0x7dfc02ea` if null) | `symbol-map.md` |
| `0x7dfc038f` | — | `idx_in_bounds` | returns `1` if `d0 (index) < *(a0+24)` (collection count), else `0` | `symbol-map.md` |
| `0x7e206a0f` | 5384 | `accessor_thunks` | block of 4-byte trampolines to getter/setter pair `0x7e208040`/`0x7e20804a` | `symbol-map.md` |
| `0x7e326b8c` | 2967 | `vcall_slot80` | **virtual dispatch**: `vtbl=*(a0); calls *(vtbl+80)`; guards `a2!=0` & index `d0≤1`; returns `exth(ret)`. Confirms C++-style objects with vtable pointer at object `+0` | `symbol-map.md` |
| `0x7d9999f9` | 3724 | `dbg_fmt_emit?` | builds a 32-byte stack buffer using cached state from `0x7d996e85`; hot output/format path (tentative) | `symbol-map.md` |
| `0x7d996e85` | 3105 | `sfr8050_byte_state` | reads SFR `0x8050`, classifies input byte (`0xff→1`, `0xfe→0`), caches flag in RAM global `0x6044a15a` | `symbol-map.md` |
| `0x7d997b14` | 1500 | `trace_log` | debug/trace emit, gated by global enable byte `0xa0a65f40` (0 = emit) + level `0xa0a65f41`; arg code's top byte (`>>24`, vs 62) = facility/category. Called from task wrappers (e.g. PC_PTP) | `symbol-map.md` |
| `0x7db8b6c8` | 1780 | `range_check_or_log` | if `idx (d0) >= count *(0x6044acb0)` → emit via `0x7d9999f9` (out-of-range log/assert) | `symbol-map.md` |
| `0x7dfc7272` | 1660 | `decode_packed_id` | decode packed 32-bit id: bits `23:16` → index (`−1`, `×4`) into RAM table `0x6044e518`; bits `15:8` → secondary lookup | `symbol-map.md` |
| `0x7db93fb8` | 1988 | `code_lookup_6000` | thunk→`0x7db93fc1`: table lookup by code, special-cases value `6000` | `symbol-map.md` |

RAM globals note: cell `0x6044cf18` and the firmup scratch `0x6044cbc4` share the `0x6044xxxx` page →
that page is a **shared RAM globals/BSS region** inside the `0x60000000` RAM aperture (distinct from
the `0xa0000000` cached SDRAM data segment above).

## Capability / flag tests
| address | xrefs | symbol | role | source |
|---|---|---|---|---|
| `0x7ddca1ce` | 1695 | `cap_test` | grouped bitmask test: `return (*(0x60711d7c + d1*4) & d0) != 0`. Indexes RAM capability/flag table at `0x60711d7c` by group `d1`, ANDs mask `d0`. Candidate for the ROM capability-table family behind the ring-feature `descriptor_gate` | `symbol-map.md`, `community-dbfw-tool.md` |

RAM capability/flag table region: `0x60711xxx` (`0x60711d7c` bitmask table; neighbours `0x60711da8`,
`0x60711dac` read by the adjacent function) — inside the `0x60000000` RAM aperture.

## Object model — construction / dispatch / resolve
Corroborates the C++-style object model (vtable pointer at object `+0`; see `vcall_slot80`).
| address | xrefs | symbol | role | source |
|---|---|---|---|---|
| `0x7e2053c1` | 2182 | `ctor_vtbl_7e42c10c` | constructor: writes vtable const `0x7e42c10c` to obj `+0`, stores arg at `+4`, clears `+8` | `symbol-map.md` |
| `0x7e2053d2` | 2029 | `ctor_vtbl_7e42c10c_noarg` | same class, no-arg variant (installs vtable, clears `+8`, returns null `a0`) | `symbol-map.md` |
| `0x7dff548d` | 2639 | `obj_factory_512` | allocate a 512-byte object (via `0x7e206a17`), tag class `0x7e385ebc`, run ctor `0x7da82515` | `symbol-map.md` |
| `0x7da82515` | 2099 | `ctor_thunk` | 2-arg thunk → worker `0x7da811b7` (148-byte frame); sibling of apply thunk `0x7da82530`→`0x7da8254b` | `symbol-map.md` |
| `0x7d9d36c4` | 2176 | `handle_to_obj` | resolve handle→object: if `a0==0` look up via `0x7d9d2bcc` (by id `d0`), else return `*(a0+4)` | `symbol-map.md` |
| `0x7dfc4738` | 1620 | `get_singleton2` | lazy-init singleton at RAM cell `0x6044d0e4`: if null, alloc 36-byte obj (`0x7e206a0f`) + ctor `0x7dfc4676` | `symbol-map.md` |
| `0x7e22ca31` | 1608 | `mgr_5c_call` | singleton accessor: if mgr `*(0x6045425c)` null → 0, else dispatch `0x7e22cb42` | `symbol-map.md` |
| `0x7e724078` | 1490 | `ctx_f10916_dispatch` | gets ctx via `0x7e722617`, gates on byte field `+10916`, then calls `0x7e723f81` on sub-struct `+10148` | `symbol-map.md` |

Known vtable constants: `0x7e42c10c` (class built by `ctor_vtbl_7e42c10c`), `0x7e385ebc` (class tag set
by `obj_factory_512`).

## OS / IPC primitives (hot, reused everywhere)
| address | symbol | role | source |
|---|---|---|---|
| `0x7d9c132d` | `os_read` | generic blocking read/receive: `a0=handle obj (deref `(a0)`), d0=len/id, d1=timeout` (`-1`=block). **154 xrefs.** Dispatches to backend `0x7d9c4093` (timed) vs `0x7d9a7ba0` (blocking) after handle-validity check `0x7d9c3fa8`. Used by firmup (SD file read) + PC_PTP (queue drain) | `symbol-map.md` |
| `0x7d9c1429` | `os_read_prep` | companion seek/prep used before `os_read` in the firmup header read | `camera-fw-update.md` |

## libc-style primitives
| address | symbol | role | source |
|---|---|---|---|
| `0x7da837b0` | `strncmp` | bounded compare: `a0=s1, a1=s2, d0=n`; returns 0 on equal-within-n or NUL, else signed byte diff. Used by `usr_checksum` id==2 path + region id-check | `symbol-map.md` |
| `0x7da837d4` | `strncpy` | bounded copy `a1→a0` up to `d0`, stops at NUL then pads (immediately follows `strncmp`) | `symbol-map.md` |

## Open / to-label (tracked across loop ticks)
- `0x7da82530` = 2-arg **thunk** → worker `0x7da8254b` (68-byte frame): sets up `(a0, arg)`, writes
  global cell `0xa09f0978`, dispatches on a flag to a name/handle-open path (`0x7da82f08`, checks for
  `-1`) vs a non-empty-name path. Worker role (component/file open within apply) not fully decoded.
- `0x7d9929ce`/`0x7d9928ee` fmem commit — not fully decoded (NAND-controller MMIO register sequence
  one hop down). `flash-storage.md`.
- Imaging/PTP/WiFi task entries beyond the firmup set — many named in `rtos-tasks.md` but entry
  functions not yet decoded.

> Maintenance: when a tick confirms a new symbol, add a row here (address, name, role, source doc) and
> cite the evidence in the subsystem doc. Keep names stable so cross-doc references resolve.
