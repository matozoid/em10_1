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

So a valid body image must carry a **matching 20-byte internal integrity array** (5 words — possibly
5 per-region checksums, or a 20-byte digest) in addition to the container footer. firmup compares it
**before flashing** and rejects on mismatch.

> **Open caveat for the patched `E1139999.BIN`.** `fwpatch.py`/`omfw.py` recompute only the **container
> footer**, never this internal 20-byte integrity array. Our block-0 diff is confined to the 9 declared
> `ring-native` patch regions, so:
> - if the integrity array lies **inside** a patched region (the community `new` bytes already carry
>   the correct value) → the built image passes;
> - if it lies **outside** the patched regions → the built image keeps the **stock** array, which will
>   not match the patched payload → the camera **rejects** it (error `0x3202`, safe — no flash), it
>   does not brick.
>
> Either way the failure is fail-closed. Next step: locate the 20-byte array's file offset in decoded
> block 0 (from the `+4`/`+16`/`+0x60000` header math) and test whether it falls within any of the 9
> patch regions — that decides whether the current built image would actually flash, and whether
> `fwpatch.py` must learn to recompute it.

**App takeaway (confirmed):** to update body firmware, write the official body image to SD as
`DCOLYMP/E1139999.BIN` (matches `E113????.BIN`); the camera mounts SD, scans `DCOLYMP`, logs
`Binary file Hakken` on the match, reads it, and flashes. Our app only places the file + drives the
boot-hold UI — it does **not** reimplement flashing or the image header/validation.

## Dead ends / notes
- USB path: the real flash routine is behind a runtime-populated vtable slot (+36); can't follow the
  indirect `calls (a2)` to a fixed address from static analysis alone.
- Arg-ids 334-337 (USB path) are opaque selectors; meaning not pinned without the message map.
- Per-letter sub-component mapping (S/G/H/W/A/M/V/D/T/I/N) not yet identified — would need tracing each
  `_Execute` branch; low priority (app only needs the `E` body image).
- Cross-ref: `docs/firmware/update-server.md` (Workspace server side), `docs/firmware/updater-ow-2.5.md`
  (OW updater tool), `docs/firmware/usb-ptp.md` (PTP transport), `docs/STATUS.md` (app v1 update plan).
