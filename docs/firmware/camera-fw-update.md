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

**App takeaway (confirmed):** to update body firmware, write the official body image to SD as
`DCOLYMP/E1139999.BIN` (matches `E113????.BIN`); camera's `api_firmup_Check_FirmwareUpdate` finds it.
Our app only places the file + drives the boot-hold UI — it does **not** reimplement flashing.

## Dead ends / notes
- USB path: the real flash routine is behind a runtime-populated vtable slot (+36); can't follow the
  indirect `calls (a2)` to a fixed address from static analysis alone.
- Arg-ids 334-337 (USB path) are opaque selectors; meaning not pinned without the message map.
- Per-letter sub-component mapping (S/G/H/W/A/M/V/D/T/I/N) not yet identified — would need tracing each
  `_Execute` branch; low priority (app only needs the `E` body image).
- Cross-ref: `docs/firmware/update-server.md` (Workspace server side), `docs/firmware/updater-ow-2.5.md`
  (OW updater tool), `docs/firmware/usb-ptp.md` (PTP transport), `docs/STATUS.md` (app v1 update plan).
