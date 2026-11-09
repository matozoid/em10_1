# OM Workspace SDK opcodes vs the E-M10 Mark I — protocol-generation mismatch

Cross-check between OM Workspace's camera-control SDK command catalog and the opcodes the E-M10
Mark I actually implements. Answers: *can the KMP replacement reuse OM Workspace's `OlyCameraLib`
command set to control the Mark I?* **No.** They are different protocol generations.

Sources: `olympus-opcode-table.csv` (523 PTP opcodes extracted from `OlyCameraLib`, the Workspace
camera SDK; internal_id↔ptp_code↔flags) vs the Mark I's advertised + internal vendor opcode sets
established live and statically in `usb-ptp.md`. Computed by `scratchpad/opcode_intersect.py`
(python3 -I).

## Numbers

| set | count | range |
|---|---|---|
| `OlyCameraLib` SDK catalog | 523 | 0x9119 … 0xd1d1 |
| — of which `0x94xx` (OMD tether/control gen) | **65** | 0x9481 … 0x94de |
| Mark I USB-advertised vendor ops (all modes) | 18 | 0x902c–0x902f, 0x9116–0x9125, 0x9801–0x9805 |
| Mark I internal camera-control engine ops (`0x7e5bxxxx`) | 54 | 0x9004–0x901d, 0x9031–0x9208 |

Intersections:

- **SDK ∩ Mark I USB-advertised = 8 opcodes**: `0x9119 0x911c 0x9120 0x9121 0x9122 0x9123 0x9124
  0x9125`. And these live only in the Mark I's mode-0/5/6 arrays — modes with **no USB-menu entry**
  on this body (no "PC Control"; `usb-ptp.md`), so they are not reachable over USB at all in
  practice. In the one reachable control personality (MTP, mode 4) the vendor overlap is **zero**.
- **SDK ∩ Mark I internal-engine = 0 opcodes.** The SDK's PTP commands use **none** of the Mark I's
  54 native `0x90xx` engine ops.
- **All 65 of the SDK's `0x94xx` opcodes are absent from the Mark I** — consistent with the live
  test where `0x9481`/`0x9482` STALL the pipe (`usb-ptp.md`): the Mark I does not implement the OMD
  `0x94xx` generation.

## Interpretation

`OlyCameraLib` (OM Workspace / OM Capture) drives cameras with the **`0x94xx` "OMD" PTP command
generation** introduced on later bodies (E-M1-era and newer). The **E-M10 Mark I (2014) predates
it** and exposes an older/separate vendor protocol:

- its **`0x90xx` engine set** (0x9004–0x9208) — used internally and by the older PTP/tether path,
  not by the modern desktop SDK;
- the **Wi-Fi CGI layer** (`exec_*.cgi` / `get_camprop.cgi` / `set_camprop.cgi`, already fully
  documented in `wifi-cgi.md` / `wifi-api.md` / `liveview-udp.md`), which is the Mark I's real
  remote-control surface.

So the two command vocabularies barely overlap (8 opcodes, none usably reachable), and the SDK's
dominant `0x94xx` set is entirely unsupported.

## Consequence for the KMP replacement

- **Do not model the Mark I control layer on `OlyCameraLib`'s opcode table.** Reusing the Workspace
  SDK command set would target a protocol the Mark I does not speak.
- The Mark I's usable remote-control path is the **Wi-Fi CGI surface** (control, live view, image
  pull, camprop get/set) plus, over USB, only standard MTP storage/object ops (no vendor control in
  the reachable mode). Build the control layer on those.
- `olympus-opcode-table.csv` remains useful only as a reference for *newer* OM bodies, not the
  Mark I. Its 8-opcode Mark I overlap is a dead end for a USB control path on this body.

## Names for the `0x94xx` generation (reference, NOT E-M10 behaviour)

Our `olympus-opcode-table.csv` lists the SDK catalog as numbers only. The public names below come
from libgphoto2's `camlibs/ptp2/ptp.h` + OM Capture traces (via the clean-room `n0p/om-tether`
project, which drives an **OM-1 Mark II** over PTP/IP and independently confirms this generation
split). These name the SDK / OM-1-era generation — a decode aid for the CSV and for a future
newer-body profile, **not** operations the E-M10 Mark I implements.

Operations: `0x9481` OMD_Capture (bulb: param 3 press / 6 release) · `0x9482` GetDateTime ·
`0x9483` MagnifyLiveViewPoint · `0x9484` GetLiveViewImage (JPEG) · `0x9485` OMD_GetImage (SDRAM) ·
`0x9486` ChangedProperties (heavy poll) · `0x9487` MFDrive · `0x9488` MagnifyLiveViewArea ·
`0x9489` SetProperties · `0x948A` PollProperties (light poll) · `0x948B` SetProperties2 ·
`0x948D` OpticalZoomDrive · `0x94A1` DetectOneTouchWB · `0x94BA` TransferModeStartStop (keep-alive) ·
`0x94BB` GetUntransferList · `0x94BC` GetLocalObjectInfo · `0x94BD` GetLocalObject ·
`0x94BE` DeleteLocalObject · `0x94BF` SetConnectPcInfo · `0x94C0` GetConnectPcInfo ·
`0x94C1` ClearConnectPcInfo · `0x94C2` GetOTWBKelvin · `0x94C3` StationMode · `0x94C4` GetAFTargetFrames.

Device properties: `0xD002` aperture · `0xD003` focus mode · `0xD004` metering · `0xD006` exp mode ·
`0xD007` ISO (**older bodies — E-M10 gen**) · `0xD009` drive mode · `0xD00D` image format ·
`0xD01C` shutter speed (`(num<<16)|den`) · `0xD01E` WB · `0xD052` CameraControlMode (1=PC, 2=standalone) ·
`0xD06D` LiveViewModeOM · `0xD0DC` CaptureTarget (1=SDRAM, 2=card) · `0xD1C0` ISO (OM-1+, replaces `0xD007`).

Events: `0x4002` ObjectAdded · `0x400D` CaptureComplete · `0xC001` OLY_CreateRecView ·
`0xC002`/`0xC102` OLY_ObjectAdded · `0xC003` OLY_AF_Frame · `0xC004` OLY_DirectStoreImage ·
`0xC005` OLY_CompleteCameraControlOff · `0xC008` OLY_DevicePropChanged ·
`0xC00C`/`0xC10C` OLY_ImageTransferModeFinish · `0xC00D`/`0xC10D` OLY_ImageRecordFinish ·
`0xC00E` OLY_SlotStatusChange · `0xC011` OLY_NotifyAFTargetFrame (match the `0xc0xx` CSV rows).

PTP/IP transport (newer-body only, absent on E-M10): CIPA DC-005, TCP 15740, command+event sockets,
`u32 len | u32 type | payload`; acceptance compares only `GUID[10..15]` == paired MAC reversed.
