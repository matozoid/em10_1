# Status (2026-11-01)

## Known
- Community build "db firmware 0.3.1.b" (azqeurio/om-c-firmware, tag dbv0.3.1.b):
  closed source, Windows PyInstaller exes (Python 3.12), 119 MiB.
  sha256 25aacf5aaf69bbdfbe3b6759dc1bc83f8729b6ce23b320e2e89d3a2a55c54e599 (matches GitHub digest)
  Claims E-M10 Mark I: only "Panasonic aperture ring works" (community-tested, not by author).
  NOT executed. Unpacking blocked pending user decision.
- Prior art: lightsnowdev.blogspot.com 2014 posts: oly_fw_manip --unpack/--pack to XML,
  ~64 files per image, same crypto across OM-D line. Tool not public; blog URLs 404 now (try Wayback).
- Stock E-M10 Mark I firmware: v1.1 (May 2014) .. later; fetched via Olympus Digital Camera Updater.

## Verified facts (from archived 2014 lightsnowdev post, saved in research/sources/)
- Camera update ID: 1130 (E-M1 1090, E-M5 0970).
- Doc URL pattern: http://dl01.olympus-imaging.com/ww/ud2/[lang]/0001/[id]/index[N]a.html (N: v1.0=1, v1.1=2)
- v1.1 BIN: .../OLYMPUS_MASTER/FIRMWARES/0001/1130/OLY_E_113_1104_0000_0000.BIN
- dl01.olympus-imaging.com no longer resolves (2026-11-01); Wayback has no copy of the BIN.
- BIN unpacks to ~64 files; 00.main-code-01.bin holds main code. OS: uITRON.
  Strings: Broadcom BCM WiFi (SDPCMD CDC), OLYMPUS BlueSDK a4 (Bluetooth), "WIFI SHELL",
  "USF debugging shell Version 1.10", CGI commands used by Olympus Image Share app.
- Updater is spoofable: a Python script emulating the Olympus server let author flash any BIN,
  any version (no version/signature gate observed on E-M10, per blog). Unverified by us.
- Tool oly_fw_manip (--unpack/--pack/--analyze) not public; E-M5 Mark II hit "Index range exceeds
  random number generator". Reference thread: personal-view.com/talks/discussion/2789/olympus-hacks

## TODO
0. Source stock BIN: Olympus Digital Camera Updater 2.0 installer (Softpedia mirror lists E-M10 FW 1.4?? -
   suspect mislabel, E-M10 Mark I last known ~1.5), personal-view.com thread, or capture from a
   camera-attached updater run on a Windows machine.
1. Obtain stock firmware image(s) (updater package or capture from updater network call).
2. Identify container format, crypto; write own unpack/repack (tools/).
3. Camera USB enumeration: lsusb/udev/libgphoto2/PTP vendor ops; log to docs/usb-protocol.
4. Hardware teardown photos + chip IDs (iFixit E-M10 teardown as start).
5. Static analysis of community patcher to learn which firmware bytes it changes.

## 2026-11-01 additions
- reference/E-M10_MANUAL_ENGLISH.PDF added (fw 1.0 manual). USB modes in docs/usb-protocol/usb-modes.md.
- OM Workspace 2.5.0.11 unpacked: docs/firmware/updater-ow-2.5.md. Real PTP/firmware calls live in
  OlyCameraLib.dll (IOlyCamera::FirmwareCheck, FirmwareUpdateInitiate, GetFirmwareStatus,
  GetFirmwareUpdateMode, GetFirmwareLanguageCode, TransFirmware). Ghidra decompile in progress.
- Ghidra 12.2 at /home/danny/dev/ghidra_12.2_PUBLIC; headless script tools/ghidra/DumpDecomp.java.
- Extra goal: new app replacing OM Workspace (v1: firmware update). Stack: Kotlin Multiplatform + Compose (see docs/ARCHITECTURE.md).

## User camera (2026-11-01)
- Body firmware 1.4 (latest for original E-M10 per Wikipedia / havecamerawilltravel: Dec 2018; unconfirmed by 2nd source). Lens firmware 1.0.
- Wi-Fi AP SSID `E-M10-P-<serial>`; no Wi-Fi fwup support (see usb-protocol/wifi-api.md).
- Stock 1.4 BIN not yet obtained. Official host dl01.olympus-imaging.com dead. Sources seen: softpedia mirror (403 to us).

## 2026-11-02
- Stock E-M10 Mark I firmware 1.4 BIN OBTAINED (see firmware/update-server.md). Wi-Fi/USB/PTP flash path no longer required for v1:
  SD-card path (DCOLYMP/E1139999.BIN, hold OK at boot) may suffice. v1 app = query server + download + write to SD + instructions.
- Community exe unpacked (tools/pyi_extract.py, static only). Container codec cracked + reimplemented (tools/omfw.py); docs/firmware/container-format.md.
  Decoded blocks in firmware/stock/dec/. Next: identify CPU/arch of block 0 (load 0x40300000), load into Ghidra, map hooks.
