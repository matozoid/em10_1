# OM Workspace 2.5.0.11 installer (reference/OWSetup_64bit.exe)

sha256 30dd0430b7fdfa3396006f0e452e83467778d58728eb7e9b41c455e6c9eb4907
Signed by OM Digital Solutions (DigiCert). Analyzed statically only, never executed.
Extraction: 7z only. Output in research/owsetup_x/ (not for commit; 100s of MB).

Nesting: OWSetup.exe -> .rsrc IDR_CAB (7z opens PE) -> MSI/OW_Pack_Framework.cab
-> application.cab -> app/ (232 files).

## Contains NO firmware images
Firmware BINs are downloaded at runtime from the OM server. Installer holds only the updater client.

## Updater client: app/FWUP/
- CameraUpdate.exe (MFC, mutex OlympusCameraFirmUpTool_Mutex; regkeys SOFTWARE\OMDS\CameraFirmUpTool)
- OlyGin.dll  "Digital Camera Communication Library": camera side.
    classes COlPtp, CWpdCtrl (PTP via WPD); exports/log strings:
    FirmwareCheck, GetFirmwareUpdateMode, TransFirmware, ChangePid, RebootCamera,
    GetCameraIcon. USB VID_07B4 (Olympus) and VID_33A2 (OM Digital); PID_%04x variable.
    -> "ChangePid" = camera switches USB personality before transfer (update mode).
- OlyWebXMLMgr.dll  server side XML: CSendFirmXML / CRcvFirmXML / IAnalizeFirmXML.
    tags: firmup_mode, firmware_demand, firmware_info, firmware_result, firmwares,
    firmware_version, serial_no.  -> camera serial+version are sent to server, server returns firmware list/URL.
- OlyWebAccess.dll / OlyWebPAC.dll: HTTP transport. Server hostnames NOT in plaintext
  (likely obfuscated/encrypted; need disassembly or a traffic capture).
- Other deps: OlylwApi2.dll, OlyLog.dll, olive.dll.

## Next
1. Disassemble OlyGin.dll TransFirmware/FirmwareCheck (Ghidra/radare2) -> document PTP vendor ops + chunking.
2. Capture updater <-> server traffic (mitmproxy on a Windows VM) to get current host + BIN URL for E-M10 (ID 1130).
   Do this with the camera attached and a real update check; BIN lands in a temp dir too.
3. Run updater under Wine? Unverified; USB passthrough to camera would be needed.
