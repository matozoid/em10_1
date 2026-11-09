# Wi-Fi HTTP API (from OLYMPUS Image Share 4.6.0 Android APK, static strings only)

APK: reference/OLYMPUS+Image+Share_4.6.0_APKPure.apk sha256 b8d66d1c5876d5dc11646c1288ef4eb9753b4df20e446b8267490c259201d933
Package namespace: jp.olympusimaging.oishare. Unpacked at research/oishare/ (not committed).
Camera is a Wi-Fi AP; camera address 192.168.0.10, plain HTTP, no auth seen in strings.
140 unique CGI strings: docs/usb-protocol/wifi-cgi-endpoints-oishare-4.6.0.txt

## Groups
- Mode: get_connectmode, get_caminfo, get_commandlist (app checks it for supported commands, e.g.
  checkSupportCommandFirmup), switch_cammode?mode=play|rec&lvqty=|shutter|maintenance|cameralog, set_timeout, exec_pwoff, exec_reboot
- Browse/transfer: get_imglist?DIR=, get_thumbnail, get_screennail, get_resizeimg, get_exif, get_dcffilenum, exec_erase, command.cgi?op=100&DIR=
- Remote: exec_shutter?com=1stpush|2ndpush|..., exec_takemisc?com=..., exec_takemotion?com=..., set_camprop/get_camprop?propname=..., live view (start_moviestream*, frame.cgi)
- Settings backup: request_getmysetdata, get_partialmysetdata?kind=&offset=, send_partialmysetdata, request_restoremysetdata,
  get_mysetdatasize/set_mysetdatasize. Blob de/encoding is native: libolytools.so MysetTools.DecodeMyset/EncodeMyset (DES, DecodeByDES/EncodeByDES).
- Camera log: switch_cammode?mode=cameralog, get_cameraloginfo, get_partialcameralogdata, clear_cameralogdata
- **Firmware update (Wi-Fi)**:
  fwup_getversions.cgi, fwup_updatemode.cgi, fwup_sendinfo.cgi?ObjectCompressSize=%d,
  fwup_sendsplit.cgi?OffsetPos=%d&Byte=%d, fwup_check.cgi, fwup_update.cgi, fwup_getfirmstatus.cgi
  App classes: settings/firmup/{FirmupCameraInfo,FirmupDownload,FirmupUpload,FirmupLicense}Activity; downloaded file name tail "b.bin".
  Inferred sequence (NOT verified): getversions -> updatemode -> sendinfo(size) -> sendsplit loop (POST body chunk at offset)
  -> check -> update -> poll getfirmstatus. Mirrors USB PTP flow (0x9125 start, 0x9119 chunks, 0x9122 status).
  Firmware BIN downloaded from Olympus servers by the phone first; host URL not found as literal (likely composed at runtime).

## Native libs
- libolytools.so: MysetTools (DES settings blob), CameraLog (MakeCamHeader/MakeCamLogData/MakeAppLogData)
- libProvidedByOlympus.so: EXIF reader, JPEG art filter/tone/color creator (image processing, not protocol)

## Relevance
Wi-Fi path works on iOS (no USB host needed) -> viable cross-platform firmware flasher/transport.
Unknown: whether E-M10 Mark I (2014, Wi-Fi) implements fwup_* (check get_commandlist on real camera), and chunk size/body format.

## Which app / which cameras (checked 2026-11-01)
- This APK is the NEW app: market link com.omdigitalsolutions.oishare ("OM Image Share"), v4.6.0, same
  jp.olympusimaging.oishare code namespace, "RemoconV21" remote UI. No camera model names hardcoded in dex strings;
  features are gated at runtime by get_commandlist.cgi / get_caminfo.cgi (CommandList/CameraInfo).
- Official OM Digital page (software.omsystem.com/oishare/en/) lists the ORIGINAL OM-D E-M10 under "Wi-Fi only"
  supported cameras (Mark II, Mark III/S also; Mark IV is Bluetooth). So the app can connect to the E-M10 Mark I.
- NOT established: that the E-M10 Mark I exposes fwup_* or that the app offers firmware update for it.
  Only a real get_commandlist.cgi response from the camera answers that. Older Olympus Image Share (OI.Share 1.x/2.x)
  APKs would show how the original-era protocol worked; worth getting for comparison.

## User-confirmed (2026-11-01)
Current OM Image Share app (4.6.0) works with the user's E-M10 Mark I (Wi-Fi). Camera speaks the CGI API above.
Still unconfirmed: fwup_* support on this camera (query get_commandlist.cgi).

## Live probe of E-M10 Mark I (2026-11-01, VERIFIED on real camera)
- AP SSID `E-M10-P-<serial>`, WPA2. Camera is DHCP server AND gateway at `192.168.0.10`; client gets `192.168.0.3`. No internet on AP.
- `get_connectmode.cgi` -> `<connectmode>private</connectmode>`
- `get_caminfo.cgi` -> `<caminfo><model>E-M10</model></caminfo>` (no firmware version here)
- `get_commandlist.cgi` -> `<oishare><version>2.20</version>`, supports: web, remote, gps, release.
  Lists cgi names with allowed params (switch_cammode, get_imglist, get_thumbnail, get_resizeimg, exec_takemotion,
  exec_takemisc, get_camprop/set_camprop, ...). Full list not captured (probe truncated at 4000 bytes; now 20000).
- `fwup_getversions.cgi` -> `HTTP 520 Vendor Internal Error`, `<errorcode>1001</errorcode>`.
  520 + error body means the CGI handler EXISTS-or-is-generic; need commandlist to know if fwup_* is advertised.
  Error 1001 likely "not in right mode / unsupported". Unresolved.
- Plain HTTP, no auth beyond Wi-Fi WPA2 key. Responses `Connection: close`.

### Full command list captured (2026-11-01) — CONCLUSION
`get_commandlist.cgi` (oishare API 2.20, 5616 bytes) advertises ONLY these CGIs:
get_connectmode, switch_cammode (rec|play|shutter, lvqty 320x240|640x480), get_caminfo, exec_pwoff, get_resizeimg
(1024/1600/1920/2048), get_movplaytime, clear_resvflg, get_rsvimglist, get_imglist, get_thumbnail, exec_takemotion,
exec_takemisc (liveview, getrecview, getlastjpg, ctrlzoom), get_camprop/set_camprop (takemode, drivemode, focalvalue,
expcomp, shutspeedvalue, isospeedvalue, wbvalue, artfilter; get-only: touchactiveframe, noisereduction, lowvibtime,
bulbtimelimit, digitaltelecon, desclist), get_activate, set_utctimediff, get_gpsdivunit, get_unusedcapacity,
get_dcffilenum, req_attachexifgps, req_storegpsinfo, exec_shutter, exec_shuttermisc.
- **No `fwup_*`, no `get_connectmode` switching to a firmware mode, no settings backup, no camera log.**
- `fwup_getversions.cgi` -> 520/1001 = handler rejects unadvertised CGI (treat as unsupported).
- => **E-M10 Mark I does NOT support Wi-Fi firmware update.** iOS-over-Wi-Fi flashing is NOT viable for this camera.
  Firmware update must go over USB (PTP vendor ops 0x9119/0x911c/0x9121-0x9125, see firmware-update.md).
  Wi-Fi CGI remains useful for browse/transfer/remote-shutter/liveview in later milestones (and works on iOS).

## External corroboration (`n0p/om-tether`, checked 2026-11-09)
The clean-room Linux project `github.com/n0p/om-tether` tethers an **OM-1 Mark II** and independently
describes this same OI.Share CGI family — its descriptor is **v5.20** vs the E-M10's **v2.20** (same
commands, ~2.5× more on the newer body). It confirms the two-generation picture: its primary path is
**PTP/IP on TCP 15740 in Wi-Fi station mode** with `0x94xx` ops, which the E-M10 Mark I does **not**
expose (verified here — `OLYSetConnectPCInfo`/`StationMode`/`ConnectPcInfo`/`not_CONN_MODE_TRANSFER`/
`get_screennail` are all absent from `blk00`; the shared CGI names `get_caminfo`/`get_imglist`/
`exec_takemisc`/`startliveview`/`set_camprop`… are present). E-M10 Wi-Fi is the camera's own AP +
HTTP CGI only — no 15740 responder. The `0x94xx` generation split is detailed in
[`sdk-opcode-compat.md`](sdk-opcode-compat.md).
