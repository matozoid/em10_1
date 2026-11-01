# Olympus OM-D E-M10 Mark I: documentation and modding

Goal: fully document hardware + firmware, make firmware modifiable.
Owner has the camera and can connect it over USB.

## Layout
- docs/hardware     board, SoC, flash, sensor, debug pads, teardown notes
- docs/firmware     container format, crypto, module layout, boot flow
- docs/usb-protocol USB modes (MTP/PTP/mass storage/updater), vendor commands
- docs/mods         what community patches do and how
- firmware/stock    official firmware images (hash-listed, not committed if large)
- firmware/community third-party builds (e.g. azqeurio/om-c-firmware); analysis only
- tools             our own unpack/repack/patch tooling
- research/sources  saved copies of external references

## Status
See docs/STATUS.md
