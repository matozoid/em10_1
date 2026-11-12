# New app architecture (proposal 2026-11-01, revised 2026-11-11)

Targets: Linux, Windows, macOS, Android, iOS.

## Decision (user: Kotlin Multiplatform)
- Language: Kotlin Multiplatform. UI: Compose Multiplatform (desktop JVM, Android, iOS).
- `commonMain` (pure Kotlin, no platform deps): PTP container/codec, operation + property tables,
  firmware BIN parse/pack, update state machine, server XML client (ktor). Unit-testable offline.
- Transport interface `PtpTransport` (expect/actual):
  - desktop JVM (Linux/Windows/macOS): libusb via JNI binding (usb4java or libusb4j, evaluate); fallback: libusb through JNA/Panama.
  - Android: android.hardware.usb UsbManager/UsbDeviceConnection (bulk transfers).
  - iOS: no USB host. Actual = Wi-Fi/CGI transport or ImageCaptureCore for import only.
- CLI: JVM module on commonMain for RE and scripting (ships first).
- Fixtures: raw USB captures replayed through a fake transport for tests.

Tradeoff vs Rust core: no native-speed need here; KMP gives one language to UI. Cost: JVM USB stack
on desktop is the weakest part; isolate behind PtpTransport so it can be swapped.

## Platform limits (important)
- iOS: no generic USB host access for third-party apps. USB firmware update NOT possible on iOS.
  iOS gets Wi-Fi features only (camera CGI), import via system APIs. Firmware update: desktop/Android
  (SD-card write).
- Android: USB Host API OK; needs per-device permission; wrap fd into libusb (libusb_wrap_sys_device).
- Windows: WinUSB/libusbK driver swap may conflict with WPD/MTP driver; document it.
- macOS: ptpcamerad claims PTP devices; must be handled/killed or use ImageCapture.
- Linux: udev rule for VID 07b4; gphoto2/udisks may claim device.

## Milestones (revised 2026-11-11)
Reordered after the RE results: the SD-card update path needs no USB at all, and OM Workspace's
`0x94xx` SDK command set does not apply to the Mark I (`usb-protocol/sdk-opcode-compat.md`).
Milestone 1 and the file-writing half of milestone 2 exist in `app/` as a JVM command line (2026-11-12).
Deviation from the plan above: the core talks to the network through a small `HttpTransport` interface
and the JVM implements it with `java.net.http`; ktor can supply the other platforms later.
1. `commonMain` core + CLI: firmware container parse/verify (port of `tools/omfw.py`), update-server
   XML client, download + sha256 check.
2. v1 firmware update, all desktop platforms + Android: query server, download the body BIN, write it
   to the SD card as `DCOLYMP/E1139999.BIN`, show the on-camera steps. The camera validates and
   flashes itself (`firmware/camera-fw-update.md`); the app does not implement flashing.
3. Compose UI for the update flow (desktop first, Android next).
4. Wi-Fi transport: capability discovery (`get_commandlist` + `get_caminfo` + `get_camprop?com=desc`),
   browse, thumbnails, download, remote shutter, live view. Works on all five platforms.
5. USB `PtpTransport`: device info and import over standard PTP/MTP. Camera control over USB is
   limited to the Mark I's own 18 advertised vendor ops; map them from live captures before building on them.
6. Patched-firmware builds (port of `tools/fwpatch.py`) as an opt-in feature, after a patched image
   has been proven on the real camera.


## Wi-Fi transport (added 2026-11-01)
Camera exposes plain-HTTP CGI API at 192.168.0.10 (see usb-protocol/wifi-api.md; verified on E-M10 Mark I).
- Use for: browse, thumbnails, download, remote shutter, liveview. Works on all 5 platforms incl. iOS.
- NOT for firmware update on E-M10 Mark I: `get_commandlist` advertises no `fwup_*`. Firmware flash = SD card
  (`DCOLYMP/E1139999.BIN`) or the USB PC-link updater.
- Consequence: iOS cannot push firmware to this camera over Wi-Fi or USB. iOS app = import/remote only
  (it could still download a BIN for the user to copy to a card). Newer cameras may advertise fwup_* (check commandlist at runtime).
- Camera AP has no internet: app must cache firmware downloads BEFORE joining camera Wi-Fi.
