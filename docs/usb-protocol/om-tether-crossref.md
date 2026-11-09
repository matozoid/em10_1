# Cross-reference: `n0p/om-tether` (OM System tethering project)

Checked the docs of the external project **`github.com/n0p/om-tether`** (2026-11-09) against our
E-M10 Mark I findings. This note records what it adds, what it confirms, and what does **not** apply
to our body. No code or binaries from it are vendored — it is clean-room MIT, and its facts come from
CIPA DC-005, libgphoto2's public `camlibs/ptp2/ptp.h` (LGPL), and traces of OM Capture / OI.Share.

## What the project is (and why most of it is a different camera)

`om-tether` is a Linux reimplementation of **OM Capture**'s Wi-Fi tethering, developed and verified
against an **OM System OM-1 Mark II (fw 1.00)** — a 2024 body. Its core path is **PTP/IP (CIPA
DC-005) over TCP 15740 in Wi-Fi station/infrastructure mode**, using the Olympus/OMD **`0x94xx`**
vendor opcode generation.

That is the **later** protocol generation. We already established (see
[`sdk-opcode-compat.md`](sdk-opcode-compat.md)) that the **E-M10 Mark I (2014) predates it**: all 65
`0x94xx` SDK opcodes are absent from the Mark I, `0x9481`/`0x9482` stall the USB pipe on real
hardware, and OM Digital's own support list gives station-mode/AP transfer only to OM-1, OM-1 II,
E-M1X and E-M1 Mark III — not the E-M10 line. So the repo's whole PTP/IP-tethering layer is
**non-applicable** to our target; it is useful only as context for the model-agnostic side and for
any future newer-body profile.

## Verified against our own firmware (string probes in `blk00`, 2026-11-09)

Confirms the generation split empirically. `present` = literal string in the E-M10 1.4 image.

| repo feature / string | in E-M10 blk00? | verdict |
|---|---|---|
| `get_caminfo`, `get_imglist`, `get_thumbnail`, `set_camprop`/`get_camprop`, `exec_takemotion`, `exec_takemisc`, `startliveview`, `get_commandlist`, `get_connectmode`, `exec_pwoff`, `get_resizeimg`, `get_rsv`, `get_activate` | **present** | shared OI.Share HTTP-CGI surface — already in [`wifi-api.md`](wifi-api.md) |
| `OLYSetConnectPCInfo` / `ConnectPcInfo` / `StationMode` | absent | OM-1-era PC-pairing; E-M10 has no USB→Wi-Fi PC pairing |
| `not_CONN_MODE_TRANSFER` / `CONN_MODE_TRANSFER` | absent | OM-1 httpd self-limit; not in E-M10 |
| `OLYTransferModeStartStop` (`0x94BA` keep-alive) | absent | station-mode transfer; n/a |
| `get_screennail` | absent | E-M10 uses `get_resizeimg` instead |

E-M10 OI.Share API version is **`<version>2.20</version>`** (getter `Maintenance::getApiVersion`);
the repo's OM-1 II descriptor is **v5.20**. Same CGI family, ~2.5× fewer commands on the Mark I,
different generation.

## Genuinely new reference material (names for numbers we already had)

Our [`olympus-opcode-table.csv`](olympus-opcode-table.csv) lists the OM Workspace / `OlyCameraLib`
SDK catalog as `internal_id,ptp_code,flags` with **no human names**. The repo (via libgphoto2 +
OM Capture traces) supplies names for that `0x94xx`/`0xD0xx`/`0xC0xx` generation. These name the
**SDK/OM-1 generation**, which the Mark I does **not** implement — kept here as a decode aid for the
CSV and for a future newer-body profile, **not** as E-M10 behaviour:

Operations: `0x9481` OMD_Capture (bulb: param 3 press / 6 release), `0x9482` GetDateTime,
`0x9483` MagnifyLiveViewPoint, `0x9484` GetLiveViewImage (JPEG), `0x9485` OMD_GetImage (from SDRAM),
`0x9486` ChangedProperties (heavy poll), `0x9487` MFDrive, `0x9488` MagnifyLiveViewArea,
`0x9489` SetProperties, `0x948A` PollProperties (light poll), `0x948B` SetProperties2,
`0x948D` OpticalZoomDrive, `0x94A1` DetectOneTouchWB, `0x94BA` TransferModeStartStop,
`0x94BB` GetUntransferList, `0x94BC` GetLocalObjectInfo, `0x94BD` GetLocalObject,
`0x94BE` DeleteLocalObject, `0x94BF` SetConnectPcInfo, `0x94C0` GetConnectPcInfo,
`0x94C1` ClearConnectPcInfo, `0x94C2` GetOTWBKelvin, `0x94C3` StationMode, `0x94C4` GetAFTargetFrames.

Device properties (OM-1 gen): `0xD002` aperture, `0xD003` focus mode, `0xD004` metering,
`0xD006` exposure mode, `0xD007` ISO (**older bodies — i.e. the E-M10 gen**), `0xD009` drive mode,
`0xD00D` image format (0x020 RAW, 0x101 LF JPEG…), `0xD01C` shutter speed (`(num<<16)|den`),
`0xD01E` white balance, `0xD052` CameraControlMode (1=PC control, 2=standalone),
`0xD06D` LiveViewModeOM (0x04000300 enables LV on OM-1), `0xD0DC` CaptureTarget (1=SDRAM, 2=card),
`0xD1C0` ISO (OM-1 and later, replaces `0xD007`).

Events: `0x4002` ObjectAdded (standard), `0x400D` CaptureComplete, `0xC001` OLY_CreateRecView,
`0xC002`/`0xC102` OLY_ObjectAdded, `0xC003` OLY_AF_Frame, `0xC004` OLY_DirectStoreImage,
`0xC005` OLY_CompleteCameraControlOff, `0xC008` OLY_DevicePropChanged, `0xC00C`/`0xC10C`
OLY_ImageTransferModeFinish, `0xC00D`/`0xC10D` OLY_ImageRecordFinish, `0xC00E` OLY_SlotStatusChange,
`0xC011` OLY_NotifyAFTargetFrame. (These match the `0xc0xx` rows already in our CSV, which carry the
`flags` 1/2 variant split but no names.)

## PTP/IP transport spec (newer-body context only — NOT E-M10)

For the model-agnostic record: CIPA PTP/IP, TCP 15740, two sockets (command + event). Packet =
`u32 length (incl. 8-byte header) | u32 type | payload`. Types 1–12 (Init_Command_Request/Ack,
Init_Event_Request/Ack, Init_Fail, Operation_Request/Response, Event, Start/Data/End_Data,
Cancel), 13/14 = PROBE_REQUEST/RESPONSE (the firmware's own names, not Ping/Pong). Acceptance on the
OM-1 II compares only **6 bytes**: `GUID[10..15]` must equal the paired MAC **reversed**
(`00×10 + MAC[5..0]`), checked against the `SetConnectPcInfo` table. Discovery is mDNS `_ptp._tcp`
+ SSDP/UPnP. **The E-M10 Mark I exposes none of this** — its Wi-Fi is OI.Share HTTP CGI on the
camera's own AP (`192.168.0.10`, port 80) only; no 15740 responder, no station mode.

## Dead ends for the E-M10 Mark I (do not chase)

- PTP/IP on 15740, station/infrastructure Wi-Fi, PC pairing (`ConnectPcInfo`), `0x94xx` opcodes,
  keep-alive `0x94BA`, `0xC102` station-mode object-added events — all OM-1/E-M1 generation.
- Wi-Fi firmware update (`fwup_*`): already ruled out live (520/1001); USB PTP only
  (see [`firmware-update.md`](firmware-update.md)).

## Still useful to us

- The OI.Share HTTP CGI surface (shared, already mapped in `wifi-api.md`) — browse/transfer/
  remote-shutter/live-view, works on iOS too.
- `[TPCFirmup]` USB-PTP firmware-update op strings are present in E-M10 blk00
  (`GetFirmwareUpdateMode`, `GetVersions`, `SendObjectSplit`, `FirmwareCheck`, `UpdateInitiate`,
  `SendFirmDataInfo`) — consistent with our USB `0x9119/0x911c/0x9121-0x9125` path.
- libgphoto2's `ptp.h` remains the best public name catalogue if we ever add a newer-body profile.
