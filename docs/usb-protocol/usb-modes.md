# USB modes (source: E-M10 manual, 161 pp, reference/E-M10_MANUAL_ENGLISH.PDF, text in research/manual/em10.txt)

Manual is based on firmware 1.0. Connector: Multi-connector (USB + AV, proprietary mini-B style, cable CB-USB6) and micro-HDMI (type D).

On connect (Custom menu > USB Mode = [Auto]) camera shows a picker:
- Storage: USB Mass Storage Class (SCSI). Image copy.
- MTP: PTP/MTP (Windows Photo Gallery). Likely the mode OlyCameraLib/WPD uses for the updater.
- Print: PictBridge.
- Exit.
Manual: camera controls disabled while connected.
Firmware version shown at Setup menu > Firmware (d tab).
Wi-Fi: smartphone link (Olympus Image Share); 2014 blog notes CGI commands + "WIFI SHELL" string.

TODO verify with real camera: lsusb IDs per mode (expect VID 07b4), update-mode PID via ChangePid.
