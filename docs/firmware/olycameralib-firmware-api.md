# OlyCameraLib.dll firmware API (Ghidra 12.2 decompile, x64; research/decomp/OlyCameraLib.c)

Layering: IOlyCamera C++ interface. Each firmware wrapper does:
  isSupported = vtbl[+0x5b8](this, cmdId); exec = vtbl[+0x5c0](this, cmdId, buf, len)
  precondition: camera connected + session open; reads property 0x80000006 (run mode) via vtbl[+0x728];
  fails 0x80048101 if camera not in RUN_MODE_STANDALONE (value 1 = other mode).
Error codes: 0x80048001 not connected, 0x80048004 no session, 0x80048013 NOT SUPPORTED.

| wrapper (FUN_ addr)            | cmdId  |
|--------------------------------|--------|
| GetFirmwareUpdateMode          | 0x81   |
| FirmwareCheck (1800297b0)      | 0x82   |
| GetFirmwareStatus              | 0x83   |
| FirmwareUpdateInitiate         | 0x84   |
| GetFirmwareLanguageCode (1 arg out) | 0x85 |
| TransFirmware                  | 0x86 (also probes 0x100c, 0x80) |

RESOLVED: see docs/usb-protocol/firmware-update.md (ops 0x9119..0x9125).
ops, e.g. 0x94a2/0x94bd/0x94cf/0x94de seen in the DLL) is NOT yet determined.
Next: decompile vtbl +0x5b8/+0x5c0 implementations (find class vftable via RTTI), then verify
against a USB capture (usbmon/Wireshark) with real camera.
