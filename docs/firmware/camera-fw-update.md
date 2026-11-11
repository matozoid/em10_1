# Camera-side firmware-update paths (2026-11-02)

Two in-camera routes apply a new firmware image. Both relevant to the KMP app's update feature.
Static RE of `firmware/stock/dec/blk00_40300000.bin` (runtime base `0x7d991020`).

## 1. USB PC-link update (OM Workspace "camera update")

Lives in the **PC-connect sub-app state machine** (same module as `command PcCommon`,
`checkPcMode`, `startPc`, `startPrint`; log-tag cluster at runtime `0x7e43a32c-0x7e43a600`). The
camera, while in USB PC mode, receives a firmware-update request over the device-link (PTP/MTP
vendor channel) and runs this event chain:

`receiveCbkDevLinkReqFirmUp` → `startFirmUp` → `updateFirmware`

### Handler `startFirmUp` @ `0x7e21d6dc`
```
prologue: movm [a2],(sp); add -12,sp
log "startFirmUp"      : mov 0x7e43a54b,a1 ; call 0x7e22352e   (PC-app trace logger, a1=tag)
                         mov 50,d0 ; call 0x7e22346e            (sub-app setup, d0=50)
log "updateFirmware"   : mov 0x7e43a557,a0 ; call 0x7e223fed    (logger variant, a0=tag)
dispatch update        : mov 337,d0 ; mov d0,(4,sp)             (stack arg = 337 / 0x151)
                         mov (a0),a2 ; mov (36,a2),a2           (obj = *(a0); method = obj->+0x24)
                         mov 334,d0 ; mov 335,d1 ; mov 336,a1   (args 0x14e/0x14f/0x150)
                         calls (a2)                              (INDIRECT -> real flash routine)
epilogue: ret [a2],12
```

So `updateFirmware` is **dispatched through an object vtable**: it loads an object pointer, fetches
the method pointer at struct offset **+36 (0x24)**, and `calls` it with four magic arg-ids
334/335/336/337 (`0x14e..0x151` — message/param selectors into the update subsystem). The concrete
flash routine is behind that vtable slot; not resolved statically (object instance is set up at
runtime), noted as the next hop.

Loggers: `0x7e22352e` (a1=tag) and `0x7e223fed` (a0=tag) are the PC-app trace printers for this
state machine.

## 2. SD-card `DCOLYMP` update (RESOLVED — `api_firmup` subsystem)

Firmware files go in the SD directory `DCOLYMP` (stored padded `"DCOLYMP    "`, 11-char 8.3 form).
The firmware-update API is `api_firmup_*` (symbol cluster at `0x7dc5a274`):
`api_firmup_Check_FirmwareUpdate` / `_Execute_FirmwareUpdate` (generic),
plus `_Strobe` and `_Lens` accessory variants, `_Firmup_Client_END`, and dummy
Start/End/Shutdown_Display hooks.

### Filename patterns (8.3, model-id `113` embedded)
The body updater scans `DCOLYMP` for files matching a table of FAT 8.3 patterns (`?` = wildcard),
all carrying model id **113** — the E-M10 Mk I's id (confirmed by flash metadata). Table at runtime
`0x7df46d44` (right after the second `DCOLYMP` copy `0x7df46d20`, scanned via `0x7de575f4`):

| pattern | component |
|---|---|
| `E113????BIN` | **main body/camera firmware** — `E1139999.BIN` matches (`E113` + `9999`) |
| `S113????BIN`, `G113????BIN`, `H113????BIN`, `W113????BIN`, `A113????BIN`, `M113????BIN`, `V113????BIN`, `D113????BIN`, `T113????BIN`, `I113????BIN`, `N113????BIN` | sub-component firmwares (sensor / image-proc / Wi-Fi / etc. — per-letter mapping not yet pinned) |
| `DATE????BIN` | date/calibration data blob |
| `PICTURE1JPG`, `PICTURE2JPG` | boot/splash images loaded from `DCOLYMP` |

The **accessory** updater (strobe/lens) uses its own two patterns, `F???????BIN` (strobe) and
`L???????BIN` (lens), from the first symbol cluster `0x7dc5a3f4`+, scanned by the picfile callers
`0x7db93360 / 0x7db93442 / 0x7db93515 / 0x7db935a4`.

### Scan/dispatch primitives
- `0x7de577a7` = directory pattern-scan (find file matching an 8.3 wildcard in `DCOLYMP`); each caller
  builds a stack param block of {dir-name ptr, pattern ptr, work-buffer `0xa0ca2800`, tag `0x1be24a40`}.
- `0x7db8b6a7` (a0=tag, d0=level) and `0x7d9999f9` = `[firmup]` trace loggers; error tag
  `"[firmup]File Init Err."` @ `0x7df46d2c`. Component framework tagged `CIC_*` (`CIC_MUTEX`, `}CIC_END`).

### Body-update scan flow (`0x7de57532`)
The body scanner (`api_firmup_Check_FirmwareUpdate` leaf; symbol tags @ `0x7db93270`/`0x7db9328a`)
runs, tagging each step with `[firmup]` log strings (@ `0x7df46ef4`+):

1. Mount SD media (`0x7de57763`). Fail → `"[firmup]Mount Err:"`, bail with -1. OK → `"[firmup]mount_ok"`.
   (The earlier `"[firmup]File Init Err."` @ `0x7df46d2c` is the pre-mount media-handle-open failure.)
2. Allocate work buffers (`0x7de57767`, size `1800`=0x708; config struct @ `0x7df46df8` holds buffer
   sizes 0x60000 / 0x100000 and RAM scratch pointers `0x6044cbc4`/`0x6044cbd8`).
3. Loop over the `X113????BIN` pattern table, calling the 8.3 dir pattern-scan `0x7de577a7` per entry.
   - result `0xE00` (3584) or `0xE0C` (3596) → `jmp 0x7de57712` = **match / handle-found** branch →
     `"[firmup]...Binary file Hakken !!!!!"` ("Hakken" = 発見, *found*) → `"[firmup]...read file_size ="`
     → `"[firmup]ld_img_st"` (load image, then validate + flash).
   - result `0` → not this pattern, bump found-counter `(12,sp)`, continue.
   - other nonzero → error, close/free via `0x7dc9cdd5`.
4. Loggers: `0x7d9999f9` (fmt, d0=value) and `0x7d996e85` (tag-only). `0xE00`/`0xE0C` are the
   media-layer "entry found" result codes. More tags: `"[firmup]file_mount/ start."`,
   `"[firmup] Time"`, `"[firmup]Are?."`.

### Component-slot table + per-file read (loop body `0x7de575d6`-`0x7de5771f`)
The scan iterates a **9-record descriptor array** at `0x7df46df8` (28 bytes/record; `add 28,a3`
per iteration, `cmp 9` exit). Each record = one firmware-component slot:

| field | meaning |
|---|---|
| +4 | max image size for the slot: rec0..8 = `0x60000, 0x100000, 0x20000, 0x620000, 0xe00000, 0x5000000, 0x4000000, 0x4000000, 0x2c40` (biggest = main firmware regions) |
| +16 | per-slot RAM state ptr (`0x6044cbc4`+, 4-byte spaced) |
| +20 | flag/count (1 or 4) |
| +24 | component id: `2, 0, 5, 0xa, 0xf, 1, 0xb, 0x12, 7` |

For each slot whose `X113????.BIN` file is found, the inner block (`0x7de576a0`) reads a **32-byte
header** (`mov 32,d0 → (132,sp)`; read via `0x7d9c1429` / `0x7d9c132d` into stack buf `sp+196`),
then checks a header halfword `(196,sp)==0` (version/validity gate). After the 9-slot loop, if any
file was found (`(12,sp)>0`) it dispatches the apply/flash via `0x7dc9ccc0` (d0=3, d1=2); else closes
and logs `"[firmup]Are?."`.

> Correction to prior tick: `0x7de57712` is the **loop-advance** label (next descriptor record), not a
> "match branch"; the found-file work is the inner block at `0x7de576a0`.

### Pre-flash image validation (safe-flash gate) (2026-11-03)
Before committing anything, `FIRMUP_SRV` validates the image and **aborts without flashing on any
failure** — so a malformed/corrupt/truncated image is rejected, not written. Flow (runtime base
`0x7d991020`):

1. `0x7de57e24` (image validator) → core parser `0x7da8883e`. The parser is **not a byte checksum**;
   it walks the image's **internal region table — up to 32 sub-image records** — reading each record's
   field + size (`0x7da88820`/`0x7da88826`), rounding size up by 64, building 16-byte descriptors
   `{ptr, field, size}`, and accumulating the running offset. It returns structural error `0x3321`
   (13089) if the records overflow / don't fit, and the caller compares the parsed total against the
   file size.
2. On mismatch the validator logs and sets error `0x3322` (13090) → `[firmup]...FIRMUP_CHECKSUM_ERROR`
   (`0x7de57abc`); a separate `[firmup]...usr_checksum_error` (`0x7de57ec1`) covers the user/image
   checksum field, and `[firmup]...checksum_error` (`0x7de589ce`) the write-phase check. Any of these
   jumps to the abort path (`0x7de58350` / `0x7de57da0`) — **no flash**.
3. Only when validation passes does it reach the write phase: `[firmup]TYPE_FIRMUP_WRITE_OK`
   (`0x7de58970`) → `[firmup]SUCCESS_REBOOT` (`0x7de57dd1`).

**Safe-flash takeaway:** the camera gates the flash behind structural + checksum validation of the
image, so a bad download/copy fails closed (aborts) rather than bricking. This is independent of the
*container footer* additive checksum that `omfw.py` recomputes (`docs/firmware/container-format.md`):
firmup re-validates the mounted file's own internal region table + checksum field.

#### usr_checksum internals (2026-11-03)
Chain: validator `0x7de57e24` → `0x7de58985` (body types 0/2 only; also asserts the image id byte
`== 0x45 'E'` via `0x7da8880b`) → worker `0x7de573d1`. The worker:
- reads header word `+4` (a derived pointer) and header flag `+16`;
- when flag `== 1`, runs a **5-iteration compare loop** of 32-bit words: `mov (d0,a1),d3;
  mov (d0,a0),d1; cmp d1,d3; bne → error 0x3202 (12802)` — i.e. it compares a **20-byte (5×u32)
  integrity array** (stored copy vs a reference/recomputed copy), advancing `d0` by 4 each step,
  `d2 < 5`;
- flag `!= 1` → error `0x3204 (12804)`; the reference address is built from the header pointer plus a
  `+0x60000` region base and small fixed offsets (`-8` / `+64 -32`).

So a valid body image must carry a **matching 20-byte internal integrity array** in addition to the
container footer. firmup compares it **before flashing** and rejects on mismatch.

##### RESOLVED (2026-11-03): it is a header↔tail duplicate-array check, not a payload hash
Full decode of the flag-`==1` compare loop (`0x7de57421` hardware loop) settles where the two operands
come from — both are **in the image**, no content hash is computed:
- `a1 = P` — the region data base (descriptor `+4` = region header `+8` pointer);
- `a0 = P + 64 + *(P+12) − 32` — i.e. 32 bytes before the region's end (`*(P+12)` = payload length,
  `64` = region-header size). So `a0` points at the **last 32 bytes of the region payload**;
- loop `i = 0..4`: `cmp *(P + i*4), *(a0 + i*4)` → first mismatch = error `0x3202`.

So `usr_checksum` asserts that the **first 20 bytes of the region header** equal the **first 20 bytes
of the region's trailing 32-byte block** — a *duplicate-array consistency check* (the same 20-byte
stamp is written both at the region head and near its tail). It does **not** checksum the payload body.
Consequence: a patch in the **middle** of the payload changes neither copy, so the check still passes.

**Verdict for the built `E1139999.BIN`:** all 9 `ring-native` patches lie between **0.00 % and 7.31 %**
of block 0 (offsets 427 … 1 379 085 in an 18 874 304-byte block). The two compared windows are
`[0 : 20)` (header) and `[blk−32 : blk−12)` (tail). **No patch intersects either window** (verified
numerically). Therefore the patched image's header/tail stamps are byte-identical to stock and the
`usr_checksum` gate **passes** — this is the accepting outcome (a), not the rejecting outcome (b).
`fwpatch.py` does **not** need to recompute this array for the ring-native patch set.

> Residual bound: the exact region partitioning (the ≤32-record table built at runtime) is not pinned
> statically, so in principle a payload split into multiple inner regions could place some inner
> region's tail window over a patch. For the ring-native offsets that is not the case against the
> single-region (whole-block) model, and the qualitative result — *a duplicate-array check, defeated
> only by touching a head/tail stamp, never by a mid-payload edit* — holds regardless of partition.
> The gate is fail-closed either way, so an unexpected partition would reject-not-brick.

**App takeaway (confirmed):** to update body firmware, write the official body image to SD as
`DCOLYMP/E1139999.BIN` (matches `E113????.BIN`); the camera mounts SD, scans `DCOLYMP`, logs
`Binary file Hakken` on the match, reads it, and flashes. Our app only places the file + drives the
boot-hold UI — it does **not** reimplement flashing or the image header/validation.

## Update-flow trace and corrections (2026-11-11)

Static trace with `tools/dis.py` and the Ghidra project, plus one live observation. This section
**supersedes** the task naming used above and in `rtos-tasks.md` for the update tasks.

### Task names are shifted by one around the update tasks
The creation table (`0x7d9a9384`) ids are one higher than the name-table (`0x4035fb66`) ids here.
Evidence is in the boot code itself, which logs a name right after starting each task:

| creation id | entry | what the code is | name the firmware logs / correct name |
|---|---|---|---|
| 0x13 | `0x7de9d4f4` | queue worker, started from the file-foreground init | FILEFGND (name-table 0x12) |
| 0x14 | `0x7de57532` | SD `DCOLYMP` scanner; **posts** requests to mailbox cell `0x7d9b06ee` | **FIRMUP_CLI** (name-table 0x13) |
| 0x15 | `0x7de57942` | request loop (`[fupsrv]Get request.`); **reads** mailbox `0x7d9b06ee` | **FIRMUP_SRV** (name-table 0x14); boot logs `"FIRMUP_SRV"` at `0x7da87344` after starting it |
| 0x4f | — | started by boot at `0x7da877b5` with log `"USTART1"` | USRSTART_FIRST (name-table 0x4e) |

So `0x7de57532` is the **client** (SD scanner), not `FIRMUP_SRV`. The 134-task registry in
`rtos-tasks.md` was built by joining the two tables on equal ids and is therefore suspect over at
least this range; it needs re-deriving from the names the boot code logs.

### One update server, two clients
- `FIRMUP_SRV` (`0x7de57942`) is started unconditionally in the normal boot sequence (`0x7da8733d`).
- Its requests come from the SD scanner (`0x7de576c2`) and from the USB path (`FirmwareCheck`
  `0x7e7d3b95`, `0x7e7d2e83`). Validation and writing are shared; the route only changes how the
  image arrives.
- The USB path is fully visible: GUI `Check_FirmwareUpdate` `0x7e14d0b0` →
  `api_firmup_Check_FirmwareUpdate` → on success `start_usb_firmup` `0x7e14d026` →
  `api_firmup_Execute_FirmwareUpdate`.

### Image checks in the validator (`0x7de57e24`)
Per region record (parser `0x7da8883e`, up to 32 records): byte 1 must be `'E'` (`0x7da8880b`),
bytes 2–3 big-endian must be `0x1130` (`0x7da88811`; mismatch = error `0x3202`), byte 20 is the
component kind (`0x7da88832`): 0 = USR, 1 = OSD, then PIC, WAV, FRAME, ADJSLF, RESCOM, NOREXE, …
(order as tested in the code; only 0 and 1 are confirmed against the header layout). The stock 1.4
BIN's three blocks have kind bytes 0, 1, 6, i.e. USR + OSD + (by that order) RESCOM, and **no NOREXE
component**. Components are written in a fixed order with resources first and USR near the end;
NOREXE, when an image has one, is written after USR.

Correction: the string `Boot ha yaranai zeyo` ("boot is not done") at `0x7de58917` is only a log line
after the NOREXE step. It is not evidence that a boot stage is protected.

### SD-card trigger: not found statically, but consistent with a live observation
- No code in block 0 starts task 0x14 (the SD scanner). All 157 call sites of the task-start routine
  `0x7d9c17ff` were resolved; none passes its id cell `0x7d9b028c`, which has no references at all.
  The only generic starter is the debug-shell `OlyTaskStart` command. The strings
  `REBOOT SYSTEM UPDATE`, `REBOOT USER UPDATE`, `RebootFlag` are referenced by no code.
- When the scanner finds no matching file it does not fail: `0x7dc9cdd5` logs `exit`, starts
  USRSTART_FIRST (`"USTART1"`) and ends its own task, i.e. it hands over to normal startup.
- **Live (owner, 2026-11-11):** power-on with OK held, card without firmware files: the camera starts
  normally but takes one to two seconds longer than usual. That matches "scanner runs, finds
  nothing, hands over to normal startup", so an OK-at-power-on SD check probably exists and is
  selected by something not yet found (a start mechanism other than `0x7d9c17ff`, or boot code
  outside the update file). It is not proof: the delay could have another cause.
- `0x7de57763`, called by both the boot sequence and the scanner and described above as "mount SD",
  is a stub that returns 0.

### Consequence for recovery claims
The statement that a bad patch "leaves the SD updater running, so stock can be reflashed" rests on
an SD trigger that is observed only indirectly and whose selecting code is unknown. If that code
lives in block 0, a patch that breaks early startup removes it. Treat SD recovery as **unproven**.

## Dead ends / notes
- USB path: the real flash routine is behind a runtime-populated vtable slot (+36); can't follow the
  indirect `calls (a2)` to a fixed address from static analysis alone.
- Arg-ids 334-337 (USB path) are opaque selectors; meaning not pinned without the message map.
- Per-letter sub-component mapping (S/G/H/W/A/M/V/D/T/I/N) not yet identified — would need tracing each
  `_Execute` branch; low priority (app only needs the `E` body image).
- Cross-ref: `docs/firmware/update-server.md` (Workspace server side), `docs/firmware/updater-ow-2.5.md`
  (OW updater tool), `docs/firmware/usb-ptp.md` (PTP transport), `docs/ARCHITECTURE.md` (app v1 update plan).
