# New app architecture (proposal, 2026-11-01)

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
  iOS gets Wi-Fi features only (camera CGI), import via system APIs. Firmware flashing: desktop/Android.
- Android: USB Host API OK; needs per-device permission; wrap fd into libusb (libusb_wrap_sys_device).
- Windows: WinUSB/libusbK driver swap may conflict with WPD/MTP driver; document it.
- macOS: ptpcamerad claims PTP devices; must be handled/killed or use ImageCapture.
- Linux: udev rule for VID 07b4; gphoto2/udisks may claim device.

## Milestones
1. RE: map PTP firmware ops from OlyCameraLib.dll + live USB captures.
2. omcore + CLI: device info, firmware version query.
3. Stock firmware fetch/verify; update-mode flash with our own BINs.
4. Flutter UI for firmware update (desktop first, Android next).
5. Import/browse (all platforms), iOS via Wi-Fi.


## Wi-Fi transport (added 2026-11-01)
Camera exposes plain-HTTP CGI API at 192.168.0.10 (see usb-protocol/wifi-api.md; verified on E-M10 Mark I).
- Use for: browse, thumbnails, download, remote shutter, liveview. Works on all 5 platforms incl. iOS.
- NOT for firmware update on E-M10 Mark I: `get_commandlist` advertises no `fwup_*`. Firmware flash = USB PTP only.
- Consequence: iOS cannot flash this camera. iOS app = import/remote only. Newer cameras may advertise fwup_* (check commandlist at runtime).
- Camera AP has no internet: app must cache firmware downloads BEFORE joining camera Wi-Fi.
