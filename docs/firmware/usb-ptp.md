# USB PTP — task structure, dispatch, and supported opcodes

Goal of this trace: find whether a USB (PTP/MTP) vendor operation can read camera
memory/flash — a cable-only route to the type-3 ROM pictures at 0x46560000 that needs no
debug shell and no reflash. Conclusion: **no such opcode is exposed**, and PTP dispatch is
*not* a static table, so the supported-opcode list below is the authoritative surface.

## TSK_PTPCOM task

- Task name string `TSK_PTPCOM` @ 0x7dbc0207; registered in the OS task-create sequence at
  0x7da880f2, whose entry pointer is **`PTPCOM_EXEC` @ 0x7e7cf737** (the `call 0x7e7cf737`
  immediately precedes the `mov 0x7dbc0207,A0` name-register call).
- `PTPCOM_EXEC` is **init only**, not a receive loop:
  - inits two mailboxes (`0x7d9c12bf` on `DAT_7d9b0722` / `DAT_7d9b0724`, names
    `PTPCOM_EXEC`/`PTPCOM_POST` @ 0x7e8902c8/0x7e8902d4),
  - registers the task on an event id via `0x7d9c1598(DAT_7d9b03f6, 1)`,
  - zeroes a **200-entry × 0x14-byte node pool at RAM 0xa0937fd8** (field[0] = in-use flag),
  - the pool allocator is `0x7e7d02fe`: circular free-slot scan (index at `0x60463ebc`,
    wraps at 0xc8=200), marks slot used, memsets 0x10 bytes, returns slot ptr,
  - allocates session buffers (`0x7e7d0905`: memset of 0x43c/0x38/0x14/0x1c/0xc/0x8-byte
    RAM blocks), then returns.
- So PTP commands are processed **mailbox-driven**, dispatched from the registered event
  handler, not by an inline `switch` in this function. The node pool at 0xa0937fd8 is a
  transaction/session object pool, *not* an opcode table.

## There is no static opcode→handler table

A full block-0 scan for `{u16 opcode, u16, u32 code-pointer}` and `{u32 opcode, u32 ptr}`
runs produced **zero** genuine PTP dispatch tables. Every candidate in the PTP opcode ranges
was one of:

- **code noise** — "handler" equal to the entry's own runtime address (relocation/code bytes
  that happen to match the opcode heuristic), e.g. runs at 0x7dbd694c, 0x7df008dc; or
- **GUI enum name-maps** — `{id, 0, char* name}` arrays that reuse the 0x10xx / 0x90xx number
  space for *GUI* ids, not PTP:
  - `0x7e5db0a4` : ids 0x1001–0x1015 → **`GM_*`** names (`GM_DELETE`, `GM_ONDRAW`,
    `GM_CLIENTTOSCREEN`…) = Windows-style GUI messages.
  - `0x7e5dd140` : ids 0x9000–0x9620 → **`EVT_*`** names (`EVT_KEY_1ST_RELEASE_ON`,
    `EVT_KEY_MENU_ON`…) = button/key SDK events.

  This is the same trap noted earlier for 0x7e45c100 (`GuiCallerImp::sendEvent`): **0x90xx in
  these tables are SDK event ids, not PTP operation codes.** Confirmed from two more copies.

Consequence: the PTP operation code received over USB is matched some other way (a `switch`,
or handlers registered at runtime into a pool, possibly partly on the second MN103 core),
and cannot be enumerated from a static table. The DeviceInfo list below is therefore the
reliable statement of what the camera's PTP actually supports.

## Supported PTP operations (DeviceInfo OperationsSupported)

`OperationsSupported` u16 arrays, the authoritative supported-op set:

- **0x7e890e78** (in the PTP data region, adjacent to the `PTPCOM`/`PTPCOM_POST` strings at
  0x7e8902xx) — three standard sub-lists plus vendor:
  - standard: 0x1001–0x100d, 0x100f, 0x1014–0x1017, 0x101b (GetDeviceInfo, Open/CloseSession,
    GetStorageIDs/Info, GetObjectHandles/Info/Object, DeleteObject, SendObjectInfo/Object,
    GetPartialObject, etc.)
  - vendor: **0x9116 0x9117 0x9119 0x911c 0x9120 0x9121 0x9122 0x9123 0x9124 0x9125,
    0x902c 0x902d 0x902e 0x902f**
- **0x7e5bc110 / 0x7e5bce28** (duplicate, in the 0x7e5bxxxx PTP code region) — vendor:
  **0x9004–0x901d, 0x9031 0x9032 0x9034–0x9037 0x903e, 0x9040–0x9042, 0x9046–0x904b,
  0x904f–0x9051, 0x9200–0x9208**

These are the standard Olympus/OM vendor camera-control set — session/property get-set, live
view, capture, movie, focus, storage — matching the OM SDK. **None is a general
"read memory / read flash" primitive.** (The 303- and 237-entry "arrays" at 0x7df6ec10 /
0x7df741e4 are image/pixel data — `1010 1010 …` and `9090 9090 …` fills — not opcode lists.)

## Per-mode DeviceInfo

`OLYMPUS_7e7d4456` is the live GetDeviceInfo responder. It picks which OperationsSupported
array to send from the current USB mode (`sVar5`, from `FUN_7e7caa83`):

| mode (sVar5) | ops array | count |
|---|---|---|
| 0, 5 | 0x7e890e16 | 0x1d (29) |
| 1 | 0x7e890e78 | 0x12 (18) |
| 2, 3 | 0x7e890e9c | 0x0b (11) |
| 4 | 0x7e890e50 | 0x14 (20) |
| 6 | 0x7e890eb2 | 0x21 (33) |

So the camera advertises different op sets for UMS / MTP / PTP-control / print. The richest
(mode 6, 33 ops) is the Olympus OM-D control/tether mode and its ops are the camera-control
set above — still no memory-read op.

## LIVE RESULT (2026-11-01): USB confirmed, no memory-read op

Camera connected over USB. UMS "Storage" mode enumerates as SCSI mass storage (PID 07b4:012e,
card mounts as a disk) — no PTP. Switched to MTP mode (PID **07b4:012f**); pulled real
`GetDeviceInfo` with `gphoto2 --debug --summary` (read-only; had to `pkill gvfsd-gphoto2`
first to free the interface). libgphoto2 identifies it as `PTP_VENDOR_GP_OLYMPUS_OMD`,
Vendor Extension ID 0xfffd (MTP), device version "1.00", serial V5PG20539.

**OperationsSupported (live, MTP mode) — the complete surface, 20 ops:**
`0x1001 0x1002 0x1003 0x1004 0x1005 0x1006 0x1007 0x1008 0x1009 0x100a 0x100b 0x100f 0x1014
0x1015 0x1016 0x101b` (GetDeviceInfo, Open/CloseSession, storage IDs/info, #objects,
object handles/info/object, thumbnail, DeleteObject, FormatStore, device-prop
desc/get/set, GetPartialObject) + `0x9801 0x9802 0x9803 0x9805` (MTP GetObjectProps
Supported/Desc/Value/List). Device capabilities: *File Download, File Deletion,
No Image Capture, No Open Capture, No vendor-specific capture*.

**Verdict: the live USB op surface is storage + object-metadata transfer only.** No Olympus
camera-control vendor ops are even exposed in this mode, let alone any raw memory/flash read.
Object ops (GetObject / GetPartialObject) read **DCIM files on the card by object handle**,
not arbitrary addresses — they cannot reach flash 0x46560000. This confirms the static
finding: **no PTP/USB path dumps camera memory.**

## Bottom line for extraction

- **No cable-only memory dump via USB.** Proven both statically (supported-op arrays are all
  standard + Olympus camera-control, none a memory read) and live (MTP mode exposes only
  storage/object + MTP-prop ops).
- The firmware-update path (`start_usb_firmup`) is a USB *write* op — relevant to the
  custom-firmware modding route (`../mods/firmware-modding.md`), i.e. flashing a patch over
  USB instead of SD, not to reading memory.

So the two viable ROM-picture routes remain: the debug shell `file memdump` (needs shell
access — Wi-Fi telnet is off, UART needs opening the body; see `debug-shell.md`) and a custom
firmware patch that copies flash→card. USB PTP does not add a third.

Not yet probed live: the OM-D control/tether mode (static mode 6, 33 ops) — entering it needs
the Olympus vendor session handshake, which changes camera state, so it was not exercised. Its
op set is known statically (camera-control only) and contains no memory read, so the negative
holds without it.
