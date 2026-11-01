# Firmware update over PTP (from OlyCameraLib.dll 2.5.0.11 decompile; UNVERIFIED on wire)

Table: docs/usb-protocol/olympus-opcode-table.csv (523 rows, static table at VA 0x180073030,
12-byte entries {u16 code, u16 pad, u32 internal_id, u32 flags}; flags 1/2 = event sets).
Codes 0x94xx = vendor ops, 0xC0xx/0xC1xx = events, 0xD0xx/0xD1xx = device props.

## Firmware ops (vendor PTP operation codes)
| internal | PTP op  | wrapper |
|----------|---------|---------|
| 0x80     | 0x9119  | send firmware chunk |
| 0x81     | 0x911c  | GetFirmwareUpdateMode |
| 0x82     | 0x9121  | FirmwareCheck |
| 0x83     | 0x9122  | GetFirmwareStatus |
| 0x84     | 0x9123  | FirmwareUpdateInitiate |
| 0x85     | 0x9124  | GetFirmwareLanguageCode (1 param out) |
| 0x86     | 0x9125  | TransFirmware: begin transfer |
Fallback if 0x86 unsupported: standard SendObjectInfo 0x100c.

## Preconditions
Session open; device prop 0x80000006 (run mode) must not be 1 ... code treats value==1 as
"not RUN_MODE_STANDALONE" and aborts (0x80048101).

## TransFirmware(this, format u16, buf, size, progressCb) flow
1. Op 0x9125 (or 0x100c) with 1 param 0x80000001 (storage id) + data phase of a 0x3c-byte dataset:
   ObjectInfo-like: StorageID=0x80000001, format code=<param2> (field at +4, u16), CompressedSize=<size>.
   Expect response 0x2001 OK.
2. Loop, chunk = 0xF800 (63488) bytes: op 0x9119, params (offset, length), data phase = chunk.
   Expect 0x2001 each; progress = sent/size. Callback return 1 = cancel.
3. On cancel/error: delete created object via FUN_180017900 (DeleteObject), return 0x80004004.
Then host calls FirmwareUpdateInitiate (0x9123), polls GetFirmwareStatus (0x9122); camera reboots into updater.

## Open questions
- Exact param layout for 0x9119/0x9125 (confirm via live capture).
- Where firmware BIN's `format` code comes from (CameraUpdate.exe passes it).
- Whether the camera verifies signature/CRC (blog says spoofed server flashed arbitrary BIN on E-M10).
- Script: decompile ghidra headless via tools/ghidra/DumpDecomp.java; function names: FUN_1800299a0 (TransFirmware),
  FUN_1800297b0 (FirmwareCheck), FUN_1800014a0 (id->opcode lookup), OlyCamLib_Initialize @1800340f0 (builds map).
