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

## 2. SD-card `DCOLYMP` update (boot-hold)

The SD firmware directory name `DCOLYMP` (padded `"DCOLYMP    "`, 11 chars) appears twice:
- runtime `0x7dc5a3f4` — xref'd by **four** sites `0x7db93360 / 0x7db93442 / 0x7db93515 / 0x7db935a4`
  (the media/picfile module — same neighbourhood as the DCF getter `0x7db93fb8`, so DCOLYMP path
  resolution is handled by the picfile/DCF subsystem).
- runtime `0x7df46d20` — xref'd by `0x7de575f4` (second copy, separate caller).

This is the path the KMP app targets: write `DCOLYMP/E1139999.BIN` to the SD root, hold OK at boot.
The four picfile-module xrefs = directory-scan / path-build for the update file. **Tracing those
four callers is the next tick** (confirm filename pattern `E113xxxx.BIN`, validation, trigger).

## Dead ends / notes
- USB path: the real flash routine is behind a runtime-populated vtable slot (+36); can't follow the
  indirect `calls (a2)` to a fixed address from static analysis alone.
- Arg-ids 334-337 are opaque selectors; meaning not pinned without the update subsystem's message map.
- Cross-ref: `docs/firmware/update-server.md` (Workspace server side), `docs/firmware/updater-ow-2.5.md`
  (OW updater tool), `docs/firmware/usb-ptp.md` (PTP transport), `docs/STATUS.md` (app v1 update plan).
