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
| `0x7dfc01bf` | 10930 | `trace_log_printf` | **central leveled debug/trace printf** (#2 hottest fn). Arg `d0`=level/tag; format string + varargs on caller stack (callee reads fmt at `(16,sp)`, varargs follow). Gets log ctx `0x7dfc0312`, checks level-enabled `0x7dfc038f`, if emitting formats+writes via `0x7dfc040d`. **Correction:** prior "registry_get / bounds-checked indexed get" label was WRONG — call sites pass format strings (e.g. `*****Q OVER?!*****`), not indices | `symbol-map.md` |
| `0x7dfc0312` | — | `get_log_ctx` | lazy-init log-context singleton at RAM `0x6044cf18` (ctor `0x7dfc02ea` if null). Ctx struct: `+20`=flag (via `0x7dfc032a`), `+24`=verbosity **threshold** | `symbol-map.md` |
| `0x7dfc038f` | — | `log_level_suppressed` | verbosity gate: `a0`=ctx, `d0`=msg level; returns 1 (suppress) when `*(ctx+24)` threshold > level, else 0 (emit). Used by `trace_log_printf` and `0x7dfc0420` | `symbol-map.md` |
| `0x7dfc040d` | — | `log_format_emit` | HLS-tagged format+emit core (via `0x7dfc0420`): re-checks `log_level_suppressed`, allocs **300-byte** line buffer (`0x7e206a17`), copies prefix string `[HLS]: ` (`0x7e35db28` — a **prefix literal**, not a sink; correction of last tick), appends formatted msg via `vsprintf 0x7da82ef3`, appends `\n`+NUL, then under **lock id 7** writes the line to sink = `console_out 0x7d996e85`. So every `trace_log_printf` line is `[HLS]: …` → console_out | `symbol-map.md` |
| `0x7dfc0312` | — | `get_singleton` | lazy-init accessor for global singleton at RAM cell `0x6044cf18` (inits via `0x7dfc02ea` if null) | `symbol-map.md` |
| `0x7dfc038f` | — | `idx_in_bounds` | returns `1` if `d0 (index) < *(a0+24)` (collection count), else `0` | `symbol-map.md` |
| `0x7e206a0f` | 5384 | `heap_alloc_thunk` | tail-call → `alloc 0x7e208040`. **Corrected: this is the heap allocator thunk, not an accessor.** Sibling `0x7e206a17` (242 xrefs) same target; `0x7e206a1f` (1029)/`0x7e206a27` → `free 0x7e20804a`. Size in `d0`, returns ptr in `a0` (null on fail) | `symbol-map.md` |
| `0x7e326b8c` | 2967 | `vcall_slot80` | **virtual dispatch**: `vtbl=*(a0); calls *(vtbl+80)`; guards `a2!=0` & index `d0≤1`; returns `exth(ret)`. Confirms C++-style objects with vtable pointer at object `+0` | `symbol-map.md` |
| `0x7daaf41f` | 576 | `lens_log_enabled` | returns `(*(0x606bb690) & d0) != 0` — tests bits of the **lens debug-log enable mask** `0x606bb690` (**CORRECTED** from "lens state flag word": not a live FSM state — gates whether a lens-com phase emits debug output). Sibling `0x7daaf431` = `lens_logcat_name`: maps log-category code 1→`LENS_SETUP`, 2→`LENS_SETDOWN`, 3→`LENS_SLEEP_SHIFT`, 4→`LENS_SLEEP_RETURN`, 5→`LENS_COM_PAUSE`, 6→`LENS_COM_RESTART` (lens-com phase log categories) | `symbol-map.md` |
| `0x7daaf301` | — | `lens_log_setflag` | debug-console handler for `lens log [com]…` / `lens set` (strings `lens_logset_dbgflg on/off`, `LOGSET_ENABLE`/`LOGSET_DUMP`): SET path `flag \|= d0`; CLEAR-bit path `flag &= ~(1<<d1)`; RESET path `d1==50 → flag=0` ("DBGFLG ALL CLEAR"). Writes `0x606bb690`; emits usage/ack via `emit` `0x7d996ee2`. Confirms `0x606bb690` is a **log-enable mask**, set from the serial debug shell | `symbol-map.md` |
| `0x7e1e7e39` | 482 | `addObserver` | **observer-pattern** registration: `addObserver(subject=a0, observer=a1)`. Null observer → logs `"#ERR# addObserver = NULL!"` (`0x7e426408`) via `trace_log_printf` and returns; else builds an observer entry (3-word records copied through the stack frame) via `0x7e1e7ff6` and links it into the subject's observer list, warning `"#WARNING# Observer duplicate"` on repeat. Core pub/sub primitive of the C++ event system (482 xrefs) | `symbol-map.md` |
| `0x7e1e7ff6` | — | `observer_entry_init` | builds/initializes an observer list entry for `addObserver`: calls `0x7dfc0a5f`, seeds a vtable/type word `0x7e35d9c4`. Helper to `0x7e1e7e39` | `symbol-map.md` |
| `0x7daf5241` | 483 | `takefcs_dbg_mark` | thin wrapper over the `[TakeFcs]` debug printer `takefcs_dbgput 0x7daf51ee`: logs a `">>"` marker line (msg `0x7DBDCB77`) under trace category **4**. One of many AF/take-focus trace points | `symbol-map.md` |
| `0x7daf51ee` | — | `takefcs_dbgput` | category-gated **`[TakeFcs]`** (take-focus / AF-during-release) debug printer. Reads RAM flag mask `0xa0a662dc`; if `mask & category(d1)` set, emits prefix `"[TakeFcs]"` (`0x7DBDCB64`) via `emit 0x7d996ee2` then formats the message `d0` via `0x7d999a53`; category bit 6 also calls `0x7daf5340`. `0xa0a662dc` = TakeFcs debug-category enable mask (nearby `0xa0a6642c`/`34`/`38` = a TakeFcs 16-byte-entry record list, inited via `0x7d996f8e`) | `symbol-map.md` |
| `0x7dffc184` | 486 | `api_result_name` | **API result-code → name string** resolver. Input `d0` = result code (valid range `0xF0000001…0` i.e. signed `[-0x0FFFFFFF,0]`; else default). Normalizes `key = code + 0x10000000`, open-addressing hash lookup (low-5-bits index × 8) in 32-slot table **`0x7E3A1C84`** (8-byte `{key, jump_ptr}`); matched entry's +4 is a thunk that loads the name string and returns via tail `0x7dffc2c8`. Names block at `0x7e38ccbd`: `API_SUCCESS`, `API_ERROR_FAIL`, `API_ERROR_INVALID_ARG`, `API_ERROR_UNRESPONSIVE`, `API_ERROR_EXECUTE_SHOOTING`, `API_ERROR_STOP_THROUGH`, `API_ERROR_PROTECTED`, `API_ENLARGE_MAX`, `API_ERROR_ENLARGE_THUMBNAIL`, `API_REDUCE_MIN`, `API_SCROLL_MAX`, `API_ERROR_DISABLE_FUNCTION`, `API_ERROR_TIMEOUT`, `API_ERROR_LINK_DISCONNECT`, `API_ERROR_LINK_CONNECTING`, … — the layered-API (`[CAPI]`) return-code namespace | `symbol-map.md` |
| `0x7dab4abf` | 488 | `emit_printf` | `printf`-to-`emit` wrapper: 144-byte stack buffer, `sprintf 0x7da82515`(buf, fmt=`a0`, arg=`d0`), then `emit 0x7d996ee2`(buf) — routes straight to the raw console `emit` (LF→CRLF), bypassing the `0x8050`/suppress logic of `console_out`. Width-typed siblings: `0x7dab4ad9` (u16 arg `exthu`), `0x7dab4af4` (u8 arg `extbu`). Compare `console_printf 0x7db19dba` (via `console_out`, 2012-byte buf) | `symbol-map.md` |
| `0x7db19dba` | 550 | `console_printf` | `printf`-to-console wrapper: reserves a 2012-byte stack buffer, saves fmt=`a0` and arg=`d0` as the vararg list, calls `sprintf` `0x7da82515`(buf, fmt, …), then routes the result via `console_out` `0x7d996e85`. One of the main plain-text log entry points (550 xrefs) feeding the `0x8050`/`emit` console path | `symbol-map.md` |
| `0x7e204ff0` | 559 | `keyed_handle_ctor` | ctor for a **28-byte keyed-handle object**, vtable `0x7E42C02C`. Layout: +0 vtbl, +4 u16 **key/id**, +8 flag=1, +12/+16/+20 cleared, +24 = ptr arg `a1`. vtable = plain accessors only (NOT a log sink despite methods living in the `0x7dfc04xx` region): slot+8 `0x7dfc04cf` = key **equality match** on +4, +12/+16 get/set u16 +4, +20/+24 get/set ptr +16, +28/+32 get/set +20. Siblings: copy-ctor `0x7e20500f`, dtor-thunk `0x7e205051`. Almost all 559 call sites default-construct (`d0=0,a1=0`). **Naming dead end**: no RTTI/class string near vtable (only `$Id$` RCS tag); generic container/handle node | `symbol-map.md` |
| `0x7e0ef82a` | 573 | `errseq_log_msg` | **ERRSEQ** message-sequence trace: if flag `0x6045086c` bit `0x400` set, formats via `trace_log_printf` `0x7dfc01bf` using `ERRSEQ:L.%d RCV(%d) %s` / `ERRSEQ:L.%d SND(%d) %s` (RCV vs SND selected by `d0` bit `0x800000`; mid field = `(d3 & 0x7f0000)>>16`), then records an event word via `errseq_push` `0x7e0fffe3`. Sibling `0x7e0ef880` uses `ERRSEQ:L.%d ID(%d) req(0x%08X) back(0x%08X) inf(...)`. Message/mailbox layer diagnostic | `symbol-map.md` |
| `0x7e0fffe3` | — | `errseq_push` | ERRSEQ event ring recorder: base ptr `0x60450890`, write index `0x60450894`; `ring[idx++] = d0`; wrap when idx reaches 128 (128-entry u32 ring). No-op if base ptr is 0 | `symbol-map.md` |
| `0x6045086c` | — | `errseq_trace_flags` | ERRSEQ trace-enable bitmask. Bit `0x400` gates `errseq_log_msg`. Written by a cluster of setters `0x7e0ffb4a`…`0x7e0ffd2f` | `symbol-map.md` |
| `0x606bb690` | — | `lens_log_dbgflg` | lens debug-log enable bitmask. Each bit = one lens-com phase log category (see `lens_logcat_name`). Tested by `lens_log_enabled` `0x7daaf41f`; set/cleared by `lens_log_setflag` `0x7daaf301` from debug shell `lens log`/`lens set`. NOT lens hardware state | `symbol-map.md` |
| `0x7e326bb0` | 605 | `prop_set_checked` | checked byte-property setter on obj `a0`, value `d0`: null-obj → noop; reject if `d0 > max` (`0x7e262b60`); skip if `d0 == current` (`0x7e2633c8`); else commit via `0x7e26338b(obj,d0)`. Sibling `0x7e326bda` sets a different field (cap 32, requires `d1!=0`, via `0x7e23c7a0`) | `symbol-map.md` |
| `0x7d9999f9` | 3724 | `dbg_print_hex_routed` | **RESOLVED** (was `dbg_fmt_emit?`): twin of `dbg_print_hex 0x7d999a53` — gated by `0x6044a15c`, builds `" "+u32_to_hex8(d0)+"\n"`, emits via the `console_out 0x7d996e85` router (instead of plain `emit`) | `symbol-map.md` |
| `0x7d996e85` | 3105 | `console_out` | **RESOLVED** (was `sfr8050_byte_state`): string output **router**, arg `a0`=string. Reads console-mode SFR `0x8050`: if `0` → fall back to `emit 0x7d996ee2`. First byte `0xff`/`0xfe` = mode escape toggling suppress flag `0x6044a15a` (1/0). Else (if not suppressed) send string (len ≤128) to channel handle `0x7d9b0858` via `0x7d9c1429` | `symbol-map.md` |
| `0x7d997b14` | 1500 | `trace_log` | debug/trace emit, gated by global enable byte `0xa0a65f40` (0 = emit) + level `0xa0a65f41`; arg code's top byte (`>>24`, vs 62) = facility/category. Called from task wrappers (e.g. PC_PTP) | `symbol-map.md` |
| `0x7db8b6a7` | 720 | `dbglvl_check_func` | `[API DBGLVL]` FUNC-level verbosity gate: if category `d0 >= *(0x6044acac)` (FUNC level mask) print header `"\n-- app debug history --\n"` (str `0x7dc51f14`, continues `"%3d %-15s 0x%08x"`) via `console_out`. `0x6044acac` = **API FUNC debug-level mask** (not a count; corrected) | `symbol-map.md` |
| `0x7db8b6c8` | 1780 | `dbglvl_check_prm` | `[API DBGLVL]` PRM-level verbosity gate (was `range_check_or_log`, then `dbghist_print_entry`): prints category hex value via `dbg_print_hex_routed 0x7d9999f9` when `d0 < *(0x6044acb0)` (**API PRM debug-level mask**). Gates whether a debug line is emitted | `symbol-map.md` |
| `0x6044acac` / `0x6044acb0` | — | `api_dbglvl_func` / `api_dbglvl_prm` (RAM) | API debug-level masks (FUNC / PRM), set by the `DBGLVL` debug-shell command (`func`/`prm`/`all` subcmds parse a `%08X` arg at ~`0x7db8b4e0` via `strcmp 0x7da836f1`; `all`→both=15). Read by the `dbglvl_check_*` verbosity gates | `symbol-map.md` |
| `0x7dfc7272` | 1660 | `decode_packed_id` | decode packed 32-bit id: bits `23:16` → index (`−1`, `×4`) into RAM table `0x6044e518`; bits `15:8` → secondary lookup | `symbol-map.md` |
| `0x7db93fb8` | 1988 | `code_lookup_6000` | thunk→`0x7db93fc1`: table lookup by code, special-cases value `6000` | `symbol-map.md` |

RAM globals note: cell `0x6044cf18` and the firmup scratch `0x6044cbc4` share the `0x6044xxxx` page →
that page is a **shared RAM globals/BSS region** inside the `0x60000000` RAM aperture (distinct from
the `0xa0000000` cached SDRAM data segment above).

## Heap allocator (core memory management)
The `0x7e206a0f`/`...a17`/`...a1f`/`...a27` thunk cluster (~6.6k combined xrefs) wraps the heap. Core:
| address | symbol | role | source |
|---|---|---|---|
| `0x7e208040` | `alloc` | tail-call → `heap_alloc` (size `d0` → ptr `a0`) | `symbol-map.md` |
| `0x7e20804a` | `free` | null-safe: if `a0!=0` → `heap_free`; manager at `0x60452220`, custom-free hook via vtbl `+16` | `symbol-map.md` |
| `0x7db954ab` | `heap_alloc` | **size-class allocator**: buckets `≤124`→`0x7d996f56`, `≤2044`→`0x7d996fc6`, `≤16380`→`0x7d996f8e`, larger → further paths. Segregated-fit pools | `symbol-map.md` |
| `0x7db954ed` | `heap_free` | matching free (pointer in `a0`) | `symbol-map.md` |
| `0x7dff54c5` | `log_fmt_msg_b` | **CORRECTED** (was `obj_factory_512b`): formatted-log builder — `alloc(512)` + `sprintf 0x7da82515` with format string `0x7e3858c1` (`"…A_SD_CARD.MEDIA_EXTERNAL.MED…"`) + emit + free. `0x7e3858c1` is a string, not a class | `symbol-map.md` |
| `0x7da811b7` | `vformat` | printf format core (parses `%`=37); backs `sprintf 0x7da82515` and `vsprintf 0x7da82ef3`. 148-byte frame | `symbol-map.md` |
| `0x7da82ef3` | `vsprintf` | thin wrapper → `vformat 0x7da811b7` (dst=`a0`, fmt=`a1`, va_ptr=`d0`) | `symbol-map.md` |
| `0x7e334de7` | `dbg_printf_lvl2` | level-gated debug printf (806 xrefs): only if verbosity `0x6046017c >= 2` → `vsprintf 0x7da82ef3` into a 256 B stack buffer + emit via `0x7dff71b7` | `symbol-map.md` |
| `0x6046017c` | `dbg_verbosity` | debug print level; `dbg_printf_lvl2` emits only when `>= 2` | `symbol-map.md` |

## Capability / flag tests
| address | xrefs | symbol | role | source |
|---|---|---|---|---|
| `0x7ddca1ce` | 1695 | `cap_test` | **`cap_test(mask=d0, group=d1)`** → `(*(0x60711d7c + group*4) & mask) != 0`. A 2-D capability matrix (group index × bit mask) in RAM table `0x60711d7c`. Sample sites: `(grp 4, mask 0x8000000)`, `(grp d2, mask 64)`. Candidate for the ROM capability family behind the ring-feature `descriptor_gate` | `symbol-map.md`, `community-dbfw-tool.md` |
| `0x7ddca28a` | — | `cap_group_of` | sibling that computes a capability `group` from an id (feeds `cap_test` as `d1`) | `symbol-map.md` |
| `0x7dd79b00`+ | — | `cap_eval_hub` | capability-evaluation routine: many back-to-back `cap_test`/`cap_group_of` calls (feature-enable logic) | `symbol-map.md` |

RAM capability/flag table region: `0x60711xxx` (`0x60711d7c` matrix; neighbours `0x60711da8`,
`0x60711dac` read by the adjacent function) — inside the `0x60000000` RAM aperture.

## Object model — construction / dispatch / resolve
Corroborates the C++-style object model (vtable pointer at object `+0`; see `vcall_slot80`).
| address | xrefs | symbol | role | source |
|---|---|---|---|---|
| `0x7e2053c1` | 2182 | `OMReactive_ctor` | constructor of the **OMReactive** refcounted base class: writes vtable `0x7e42c10c` to obj `+0`, stores arg at `+4` (refcount), clears `+8` | `symbol-map.md` |
| `0x7e2053d2` | 2029 | `OMReactive_ctor_noarg` | same class, no-arg variant (installs vtable, clears `+8`, returns null `a0`) | `symbol-map.md` |
| `0x7e206dc9` | 950 | `OMReactive_ref_dec` | refcount decrement at obj `+4`; on underflow loads msg `"underflow in OMREactive less then 0"` (`0x7e42c580`) and calls assert stub | `symbol-map.md` |
| `0x7e206de4` | — | `OMReactive_ref_inc` | refcount increment at obj `+4`; on overflow (`0xffff`) loads `"overflow in OMREactive too many active"` (`0x7e42c5b0`) and calls assert stub | `symbol-map.md` |
| `0x7e2053aa` | — | `assert_stub` | **release no-op** (`retf` only) — the error-report target for OMReactive refcount asserts does nothing in production firmware | `symbol-map.md` |
| `0x7dff548d` | 2639 | `log_fmt_msg` | **CORRECTED** (was `obj_factory_512`): formatted-log builder — alloc 512 B scratch (`0x7e206a17`), `sprintf` with format string `0x7e385ebc` (`"%1s..%1s, %d..[HLS]: %1s"`), `console_out 0x7d996e85`, then free. The "class tag" was a **format string**, not a vtable | `symbol-map.md` |
| `0x7da82515` | 2099 | `sprintf` | **CORRECTED** (was `ctor_thunk`): variadic `sprintf(dst_desc=a0, fmt=arg, …)` → calls the format core `0x7da811b7`. (`0x7da82530` is a *different* thunk → `0x7da8254b`, not a format wrapper — see Open) | `symbol-map.md` |
| `0x7d9d36c4` | 2176 | `handle_to_obj` | resolve handle→object: if `a0==0` look up via `0x7d9d2bcc` (by id `d0`), else return `*(a0+4)` | `symbol-map.md` |
| `0x7dfc4738` | 1620 | `get_singleton2` | lazy-init singleton at RAM cell `0x6044d0e4`: if null, alloc 36-byte obj (`0x7e206a0f`) + ctor `0x7dfc4676` | `symbol-map.md` |
| `0x7e34b8f6` | 977 | `get_singleton_60460ea4` | lazy-init singleton (no lock) at RAM cell `0x60460ea4`: if null alloc **60-byte** obj (`0x7e206a0f`) + ctor `0x7e34b881`. Ctor = POD init (no vtable): memset(+0,0,12); bytes +12=0,+32=0xff; words +14/+18 = `0xffffffff` (unset markers), +24=0. No class-name string | `symbol-map.md` |
| `0x7dfc4922` | 698 | `evtrace_rec_e1` | event-trace record builder: tag `d0` with category byte `0xE1` (`\|0xE1000000`), alloc ring slot (`0x7dfc4bfe`), fill `{tagged_id, d1, a1, aux}` (aux = `0x7d996ba7()` if `*(a3+4)!=0`). Sibling `0x7dfc4950` = same with category `0xE2` | `symbol-map.md` |
| `0x7dfc49ea` | 510 | `evtrace_rec_e3` | event-trace record builder, category byte **`0xE3`** (`d2 = d0 \| 0xE3000000`). Guard: skip if `*(a0+4)==0 && d1==0`. Else alloc ring slot (`evtrace_alloc_slot 0x7dfc4bfe`), store `{tagged_id@0, d3@4}`, and if `*(a0+4)!=0` fill `aux@12 = 0x7d996ba7()`. Sibling `0x7dfc4a19` = same with category **`0xE4`**. Extends the `evtrace_rec_e1/e2` family (`0x7dfc4922`/`0x7dfc4950`) | `symbol-map.md` |
| `0x7dfc4bfe` | — | `evtrace_alloc_slot` | ring slot-alloc: read+increment write index `*(a0)`, return old index's slot ptr via `0x7dfc4bda(idx)`. Backs the `evtrace_rec_*` recorders (software event-trace ring) | `symbol-map.md` |
| `0x7e274009` | 708 | `tbl792_get` | bounds-checked pointer-array accessor: arg `a0`=obj, `d0`=index (u16). If `index >= 379` → null, else return `*(obj + 792 + index*4)`. Obj holds a **379-entry pointer table at `+792`**; sibling `0x7e274020` iterates it (via `0x7e24ff2a`, registry `0x604526cc`) | `symbol-map.md` |
| `0x7e22352e` | 847 | `type_gated_call` | type-gated method wrapper: gate `0x7e223618(a0)`; if registered → worker `0x7e2236c3(obj,arg)`. One of a sibling family (`…3543`, `…355a`…) each pairing a gate with a different worker | `symbol-map.md` |
| `0x7e1e82b4` | 825 | `enqueue_checked` | enqueue wrapper: call `0x7e206e08(...)` (queue-put); on failure (ret 0) logs `*****Q OVER?!*****` (queue overflow, str `0x7e42649b`) via `trace_log_printf`; returns the result | `symbol-map.md` |
| `0x7e206e08` | — | `queue_put` | queue/ring put primitive (callee of `enqueue_checked`); returns 0 on full → triggers "Q OVER?!" | `symbol-map.md` |
| `0x7e223636` | — | `obj_type_registered` | object-type gate: read type tag `*(a0)`, scan RAM registry table `0x604523c4` (stride-12, 2 entries) → 1 if match; else table `0x604523dc` also requiring entry `+20 == 1` (enabled). Returns bool. Thin adapters `0x7e223618` / `0x7e223627` just forward its result. Registry tables populated at runtime | `symbol-map.md` |
| `0x7e22ca31` | 1608 | `mgr_5c_call` | singleton accessor: if mgr `*(0x6045425c)` null → 0, else dispatch `0x7e22cb42` | `symbol-map.md` |
| `0x7e22ca49` | 841 | `mgr_5c_call2` | sibling 2-arg accessor on SAME mgr singleton `*(0x6045425c)`: if null → 0, else forward (a0→a1 obj, a1→d2 val) and dispatch `0x7e22cbbb`. Mgr ctor `0x7e22ca67` installs vtable `0x7e45e460` (slots all code ptrs, no inline class-name string → class unidentified) | `symbol-map.md` |
| `0x7e22cbbb` | — | `mgr_dispatch_indexed` | worker behind both mgr accessors: indexed handler dispatch. Bounds-check index vs u16 count `*(mgr+12)` (`>=` → 0); null arg → 0; gate on singleton `*(0x60452f9c)` (vtable call w/ -1, nonzero req). Handler table base `*(mgr+8)`, **16-byte entries**, `entry = base + index*16`; entry fnptr `+4`, target obj `+8` → virtual `calls` handler(arg). Mgr `0x6045425c` = indexed handler registry/dispatcher | `symbol-map.md` |
| `0x7e228ee3` | many | `factory_by_id` | subsystem descriptor **lookup**: arg `d0`=id. Reject id<12 or >137 → null. `d0-=11`; hashed open-addressing probe over table `0x7e45dda8` (32 slots ×8B = `{key:u32, thunk:fnptr}`, wrap `0x7e45dea8`); match → tail-`jmp` thunk. Each thunk just `mov imm,a0; ret` returning a per-id **handler-function ptr** (code `0x7e2286d6`–`0x7e22a540`, each has `movm`/`add -N,sp` prologue — NOT data; correction of earlier "descriptor" guess), invoked by caller via `calls(a0)`; key-0 slot → null. Table is sparse: populated keys {0–14,25,26,27,37,38,41,122,123,126} = ids {11–25,36–38,48,49,52,133,134,137}; all other ids → null (shared factory, most slots unused on this body — so the `0x60452f__` bank's high ids incl. gate 131 resolve to null). Drives `0x60452f__` bank init (`0x7e2254xx`: `a0=factory(id); *(cell)=a0`). id11 handler `0x7e2286d6` memsets+inits RAM state `0x607736d0` (count) / `0x607736d4` (table); id12 handler `0x7e228974` iterates that table — a per-subsystem init/iterate family | `symbol-map.md` |
| `0x7e227686` | — | `rec_table_count` | count records in a **78-byte-stride** table: base `*(0x60773344)`, table ptr at `+12`, scan u16 field until terminator halfword `==147`, return index. Sibling `0x7e2276a7` copies entry[i] (78B = 39 halfwords) into caller buffer `a2` | `symbol-map.md` |
| `0x60773344` | — | `rec_table_base` (RAM) | base ptr of the 78-byte-record table; set at `0x7e3407b2` from obj returned by getter `0x7e02ec5a` + virtual slot `(48,a1)`; field `+16`→cached to `0x6045e108`. **Naming dead end:** registration path (`0x7e334de7`) takes fn-ptr callbacks, not inline name strings — subsystem identity not recoverable via the vtable-string technique | `symbol-map.md` |
| `0x7e722617` | — | `get_adj_system` | returns the **`adj_system`** singleton `*(0x6091c53c)` — a **12524-byte** `[CAPI]`-tagged subsystem (camera adjustment/calibration). Init (`0x7e72262a`) allocs 12524 B, logs `"adj_system size:…"`. The whole `ctx_f10916_*` family operates on fields inside this object | `symbol-map.md` |
| `0x7e7229ac` | 518 | `adj_set_reg8368` | `adj_system` register setter (singleton `0x6091c53c`): stores arg `d0` → field **+8368**, clears status bytes **+8372** and **+8404**, then re-inits via `0x7e759152` and flushes via `0x7e722a88`. The flush (`0x7e722a88`) is gated on byte **+13** and, when set, formats/copies the **+9012** adjustment-data block (`%f`/`%d`, via `0x7e758c20`/`0x7da836ab`). Sibling `0x7e7229f5`/`a02` = set/get paired reg **+8364** | `symbol-map.md` |
| `0x7e724078` | 1490 | `ctx_f10916_dispatch` | gets `adj_system` via `get_adj_system 0x7e722617`, gates on byte field `+10916`, then calls `0x7e723f81` on sub-struct `+10148` | `symbol-map.md` |
| `0x7e7240a9` | 752 | `ctx_f10916_getval` | sibling of `ctx_f10916_dispatch`: same ctx (`0x7e722617`), gate byte `+10916` + readiness `0x7e723f81` on sub-struct `+10148`; if ready & `*(substruct)!=0` returns 64-bit pair (`d0:d1`) from `0x7da8484e`, else passes through caller's `d0:d1` default. Neighbor `0x7e7240e2` clears `+10916` (disable). So `+10916`=feature enable flag, `+10148`=feature state struct | `symbol-map.md` |
| `0x7e205040` | 1255 | `base_reset_vtbl_7e42c02c` | lifecycle reset/dtor stage: installs base vtable `0x7e42c02c` at obj `+0`, then `0x7e2050d6` zeroes member at obj `+24` if non-null; returns null `a0` | `symbol-map.md` |

Known vtable constants: `0x7e42c10c` (**OMReactive** refcounted base class, built by `OMReactive_ctor`), `0x7e42c02c` (base vtable installed by `base_reset_vtbl_7e42c02c`), `0x7e42c09c`
(sibling vtable installed nearby at `0x7e2050e2`). The `0x7e42cxxx` block is a **vtable array** for one
class hierarchy.

## OS / IPC primitives (hot, reused everywhere)
| address | symbol | role | source |
|---|---|---|---|
| `0x7d9c132d` | `os_read` | generic blocking read/receive: `a0=handle obj (deref `(a0)`), d0=len/id, d1=timeout` (`-1`=block). **154 xrefs.** Dispatches to backend `0x7d9c4093` (timed) vs `0x7d9a7ba0` (blocking) after handle-validity check `0x7d9c3fa8`. Used by firmup (SD file read) + PC_PTP (queue drain) | `symbol-map.md` |
| `0x7d9c1429` | `os_chan_io_prep` | channel I/O prep (bidirectional): seek/prep before `os_read` in firmup; also the **send** path in `console_out` (buf, len, handle, timeout `-1`) — not read-only | `camera-fw-update.md` |
| `0x7d9b0858` | `console_out_chan` | console output channel handle used by `console_out 0x7d996e85` | `symbol-map.md` |
| `0x7dfc0587` | `lock_get` | get lock object for id `d0`; lazy-inits the lock-manager singleton at `0x6044cf20` (alloc 44 B via `0x7e206a17` if null) | `symbol-map.md` |
| `0x7dfc056a` | `mutex_lock` | virtual `lock()`: inner obj `*(a0+4)`, `vtbl=*(obj)`, `calls *(vtbl+12)` | `symbol-map.md` |
| `0x7dfc057a` | `mutex_unlock` | virtual `unlock()`: inner obj `*(a0+4)`, `vtbl=*(obj)`, `calls *(vtbl+16)` | `symbol-map.md` |
| `0x7e02ec5a` | `get_singleton_6044eb38` | **double-checked-locking** singleton init (1061 xrefs): check `*(0x6044eb38)`; if null take lock id 2 (`lock_get`+`mutex_lock`), re-check, alloc 8 B + ctor `0x7e02ecb2`, store, release (`mutex_unlock`). Ctor `0x7e02ecb2`: obj+0 = ptr to **static config record `0x7e473a2c`** (NOT a vtable — slots are ints `{15,15,0x101,0,0,1,0xffff,7,1}`, a limits/param table), obj+4=0; then `0x7e05371c`→`0x7e02fd97` finish init | `symbol-map.md` |

## libc-style primitives
| address | symbol | role | source |
|---|---|---|---|
| `0x7da837b0` | `strncmp` | bounded compare: `a0=s1, a1=s2, d0=n`; returns 0 on equal-within-n or NUL, else signed byte diff. Used by `usr_checksum` id==2 path + region id-check | `symbol-map.md` |
| `0x7da837d4` | `strncpy` | bounded copy `a1→a0` up to `d0`, stops at NUL then pads (immediately follows `strncmp`) | `symbol-map.md` |
| `0x7d997773` | `strcmp` | unbounded byte compare `a0` vs `a1`; returns signed `*a0-*a1` at first mismatch, 0 if equal (574 xrefs). **Separate copy** in the core `0x7d99xxxx` region — distinct from the `0x7da83xxx` string cluster (two libc instances linked) | `symbol-map.md` |
| `0x7d99779f` | `strlen` | scan-to-NUL in core region (sibling of `strcmp 0x7d997773`); distinct from `strlen 0x7da8376d` | `symbol-map.md` |
| `0x47001000` | `memcpy` | mask-ROM `memcpy(dst=a0, src=a1, len=d0)` — 1394 xrefs | `memory-map.md` |
| `0x4700110c` | `memset` | mask-ROM `memset(dst=a0, val=d0, len=d1)` — 3612 xrefs (was mislabeled byte-copy) | `memory-map.md` |

## Debug shell — command dispatch (not reachable non-invasively; see `debug-shell.md`)
| address | symbol | role | source |
|---|---|---|---|
| `0x7dbbecec` | `shell_cmd_table` | master 59-entry `{char* name, void* handler}` table (dup `0x7dbbfa80`), stride 8 | `debug-shell.md` |
| `0x7dbbe24c` | `shell_autoexec_table` | 29-entry canned-command table run at debug init | `debug-shell.md` |
| `0x7da84eb8` | `shell_dispatch` | `strncmp`-loop over 59 entries (cmp via `0x7da836f1`), `calls *(entry+4)` on match; `a0`=args, `d0`=argc | `debug-shell.md` |
| `0x7da84d3e` | `shell_exec_line` | clears scratch `0x60710c04`, copies+tokenizes line into arg table `0x60710d04`, calls dispatch | `debug-shell.md` |
| `0x7da84ccf` | `shell_autoexec_run` | iterates `0x7dbbe24c`, runs each via `shell_exec_line`; polls HW `0x7d9c9cd8` mask `0x12345678` | `debug-shell.md` |
| `0x7da84cb9` | `shell_autoexec_gate` | runs autoexec only if mode `d0==1`; else logs (`0x7da84ea6`) | `debug-shell.md` |
| `0x8ff00190` | `dbg_mode_latch` | SFR written `0x12345678` by shell-init = "debug mode on" (hardware latch, not PTP/Wi-Fi settable) | `debug-shell.md` |

## Diagnostics — in-memory trace capture buffer
`0x7ddca749` (1047 xrefs) is a RAM trace-capture sink. When enabled it appends log strings to a
512 KB buffer, so the buffer is a **standing dump target** (its text accumulates in RAM).
| address / global | symbol | role | source |
|---|---|---|---|
| `0x7ddca749` | `trace_capture_append` | if enable `0x60711de8==1` and not-full `0x60711de9==0`: `strlen`(`0x7da8376d`)+`memcpy`(`0x7da837d6`) the string `a0` into buffer at base`+offset`, advance offset. Else fall back to `trace_log 0x7d996ee2` + `cap_test(0x10000,grp1)` | `symbol-map.md` |
| `0x7ddca7f0` | `trace_cap_puts_hex32` | formatted capture print (877 xrefs): `trace_capture_append(prefix a0)`, then append `" "+u32_to_hex8(d2)+"\n"`. Sibling `0x7ddca819` formats a 16-bit value via `0x7da894f1` | `symbol-map.md` |
| `0x7dd438e1` | `log_val_fmt` | value-logging wrapper (869 xrefs): logs message (`a0`, default ptr `0x7ded4e40` when null) + hex value (`d0`); routes to `dbg_print_hex_routed 0x7d9999f9` (console) vs plain `dbg_print_hex 0x7d999a53` by `console_present? 0x7dd53bb2` or flag `0x60709d54==1` | `symbol-map.md` |
| `0x7dd53bb2` | `console_present?` | thin wrapper → mask-ROM `0x47001b0a`, returns a byte (debug/console-attached query); gates log routing | `symbol-map.md` |
| `0x60711de8` | `trace_cap_enable` | byte, `==1` → record into the buffer | `symbol-map.md` |
| `0x60711de9` | `trace_cap_full` | byte, set to `1` when offset would reach cap (locks further writes) | `symbol-map.md` |
| `0x60711dfc` | `trace_cap_offset` | u32 current write offset into the buffer | `symbol-map.md` |
| `0x60711e00` | `trace_cap_base` | base of the ~512 KB capture buffer (cap `0x7FFFF`) | `symbol-map.md` |
| `0x7da8376d` | `strlen` | scan-to-NUL, returns `a1−a0` | `symbol-map.md` |
| `0x7d999a53` | `dbg_print_hex` | gated by `0x6044a15c` (output enable, halfword): emit `" " + u32_to_hex8(d0) + "\n"` via `emit 0x7d996ee2`; alt path when `0x6044a15a==1` (1043 xrefs) | `symbol-map.md` |
| `0x7d999aad` | `u32_to_hex8` | write 8 uppercase hex chars of `d0` to buffer `a0` (nibble loop, `+'0'`/`+'A'-10`) | `symbol-map.md` |
| `0x7d996ee2` | `emit` / `trace_puts` | raw string output sink (1466 xrefs); takes string in `a0`. Emits byte-by-byte via `console_putc 0x7d9c51fc`, translating `\n`(10)→`\r\n` (CRLF) | `symbol-map.md` |
| `0x7da886b4` | 680 | `dbg_trace_line` | gated debug trace-line emitter: only if enable `*(0x6044a15c)!=0`. If suppress flag `*(0x6044a15a)!=1` → `console_out(a0)` + a second fixed string; else formatted path `0x7dbbdb29` with `"%s %s"` / `"%s %08X %s"` (label, hex, suffix). Twin `0x7da886fb` = same via `emit 0x7d996ee2` | `symbol-map.md` |
| `0x7d9c51fc` | `console_putc` | terminal byte sink: char in `d0`. Guard/flush `0x7d9b1645`, then push char into a **767-entry RAM console ring at `0xa0bba15c`** (write index halfword at SFR `0x8ff00084`) and the hardware debug FIFO at the `0x8ff000xx` peripheral window (status `0x8ff0007e`/`007c`). Bottom of the entire log pipeline (`trace_log_printf`→`console_out`/`emit`→here) | `symbol-map.md` |
| `0x6044a15c` | `dbg_hexprint_enable` | halfword, non-zero → `dbg_print_hex` emits | `symbol-map.md` |

## Soft-float / FPU coprocessor intrinsics
Compiler-emitted FP helpers using MN10300 `udf04`/`udf05` user-defined (coprocessor/FPU) ops —
confirms the firmware does real float math via the coprocessor, not pure integer emulation.
| address | symbol | role | source |
|---|---|---|---|
| `0x7da8425a` | `fp_cmp_a` | `udf04 d1,d0`-based FP compare intrinsic; returns `2×result` in `d1` (heavily used — 1015+ xrefs) | `symbol-map.md` |
| `0x7da84248` | `fp_cmp_b` | `udf05 d1,d0` FP compare intrinsic (sibling predicate) | `symbol-map.md` |
| `0x7da8424f` | `fp_negate` | `xor 0x80000000,d0` (flip IEEE-754 sign bit), returns `2×` | `symbol-map.md` |
| `0x7da84261` | `fp_classify` | IEEE-754 single decompose: mantissa `&0x7fffff`, exponent `&0x7f800000`; detects inf/NaN (exp all-ones) and subnormal/zero | `symbol-map.md` |
| `0x7da84235` | `fp_op_udf02` | `udf02 d1,d0` coprocessor FP intrinsic; returns `2×result` in `d1` (same ×2 convention as `fp_cmp_a`; 689 xrefs). Exact op not pinned — no AM33 FPU udf-opcode spec (dead end on precise semantics) | `symbol-map.md` |
| `0x7da8423c` / `0x7da84243` | `fp_op_udf06` | `udf06 d0,d1` coprocessor FP intrinsic (binary at `…423c`; unary at `…4243` with `d1=0`); result in `d1`. Exact op not pinned (same dead end) | `symbol-map.md` |
| `0x7da83d02` | `__divdf3` | **double-precision** soft-float **divide** (571 xrefs; same emulated-double family as `__muldf2`, not the coprocessor path). Unpacks both IEEE-754 doubles (exp `lsr20 &2047`, mantissa + implicit `0x100000`), classifies specials (zero/inf/nan → bits 1/2/4): NaN→hi `0x7ff80000`, inf/0 quotient → hi `0x7ff00000` or 0. Else **subtracts** exponents (`ea-eb`, range-checks `>1024`→inf, `<-1075`→0), normalizes both mantissas, and divides via repeated hardware `divu d3,…` (restoring long division of the 52-bit mantissas, remainder-corrected) | `symbol-map.md` |
| `0x7da83f80` | `__muldf2` | **double-precision** soft-float **multiply** (763 xrefs; pure integer, NOT the udf04/05 coprocessor path — doubles are emulated, singles use the coprocessor). Decodes two IEEE-754 doubles (11-bit exp `lsr20 &2047`, 52-bit mantissa), classifies operands (zero/inf/nan → bits 1/2/4), returns NaN hi `0x7ff80000` or Inf `0x7ff00000` for specials, else adds biased exps (overflow >3069→inf, underflow <970→0) and `mulu` the mantissas | `symbol-map.md` |

## Subsystem singletons (named via inline RTTI/trace strings)
Cells cluster in a **singleton-pointer bank** at RAM `~0x60454418`–`0x60454440` (and a nearby
`0x604543xx` group): each slot holds one lazily-constructed subsystem controller. Getters follow the
shape `a0=*(cell); if null → alloc N + ctor + store`. Classes that install a vtable can be named from
the inline trace string that follows the vtable (see CPlayZoom); vtable-less struct singletons cannot.
| address | symbol | role | source |
|---|---|---|---|
| `0x7e24831c` | `CPlayZoom_instance` | lazy singleton getter for the **CPlayZoom** playback-zoom controller (924 xrefs): cell `0x60454418`, 184-byte object, ctor `0x7e24825d` (base `0x7e2414c5`), vtable `0x7e4693a0`. Class named by inline trace string `"CPlayZoom::setDbZoomInfo_Lite Called."` right after the vtable. Followed by an accessor bank (getters/setters at obj `+12/+16/+20/+32/...`) | `symbol-map.md` |
| `0x7e23dfec` | `singleton_604543e8` | lazy getter: cell `0x604543e8`, 336-byte **vtable-less** struct, ctor `0x7e23de5d` (defaults `+16=0xff`, rest 0). No class string (no vtable) → unnamed state/config struct | `symbol-map.md` |
| `0x7e24ff2a` | `global_ptr_60454428_get` | plain getter `return *(0x60454428)`; paired setter at `0x7e24ff33` (`*(0x60454428)=a0`). Global object-pointer slot, set elsewhere | `symbol-map.md` |

## Misc object accessors
| address | symbol | role | source |
|---|---|---|---|
| `0x7e1e8a41` | `obj_get_f264` | field getter `return *(a0+264)` (1015 xrefs; cf. `obj_get_f104`) | `symbol-map.md` |

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
