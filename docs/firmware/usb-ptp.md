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

## Bottom line for extraction

- No cable-only memory dump via a documented PTP op: the supported vendor set is
  camera-control, not memory access.
- Proving a *negative* for all ~70 vendor ops from statics is hard (handlers are reached via
  the mailbox/event path, not a table). Two ways to close it:
  1. **Live, read-only USB probe** — connect USB, send `GetDeviceInfo` (0x1001), confirm the
     OperationsSupported list above against the real camera, then exercise candidate vendor
     ops. Non-destructive but a live action → needs user approval.
  2. Trace each vendor handler from the event-dispatch path (slow; not table-driven).
- The firmware-update path (`start_usb_firmup`) is a USB *write* op — relevant to the
  custom-firmware modding route (`../mods/firmware-modding.md`), i.e. flashing a patch over
  USB instead of SD, not to reading memory.

So the two viable ROM-picture routes remain: the debug shell `file memdump` (needs shell
access — Wi-Fi telnet is off, UART needs opening the body; see `debug-shell.md`) and a custom
firmware patch that copies flash→card. USB PTP does not add a third.
