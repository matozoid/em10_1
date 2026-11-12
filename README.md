# Olympus OM-D E-M10 Mark I: documentation and modding

Goal: fully document the firmware and the camera's external interfaces, make the firmware
modifiable, and build an app that replaces OM Workspace for this body.

The owner has the camera (body firmware 1.4) and can connect it over USB and Wi-Fi. The body is
never opened: no teardown, no UART/JTAG. Hardware knowledge comes from firmware analysis only.

## Status
See [docs/STATUS.md](docs/STATUS.md).

## Layout
Committed:
- `docs/STATUS.md`        current state, open items, ground rules
- `docs/ARCHITECTURE.md`  plan for the replacement app (Kotlin Multiplatform)
- `docs/firmware/`        container format, memory map, RTOS tasks, classes, resources, Wi-Fi CGI
                          handlers, USB PTP, debug shell, in-camera update, update server, and the
                          symbol files (`symbol-map.md`, `symbol-families.md`, `symbol-strings.md`)
- `docs/usb-protocol/`    USB modes, PTP opcode tables, Wi-Fi API, live-view UDP, myset format
- `docs/mods/`            patching pipeline, community patches and how they work
- `docs/workspace/`       OM Workspace internals: ORF format, RAW decode, plugins, model selection
- `docs/hardware/`        boot/reset code, on-chip I/O registers, display pipeline (from firmware)
- `tools/`                our own unpack/repack/patch/resource tools; `tools/ghidra/` headless scripts
- `app/`                  replacement app (Kotlin Multiplatform; milestone 1: firmware download/verify)

Local only (gitignored; third-party material is not redistributed):
- `firmware/stock/`       official firmware image, decoded blocks, extracted resources
- `firmware/community/`   images built from third-party patch profiles
- `research/`             Ghidra project, decompiles, unpacked vendor software, saved web sources
- `reference/`            manual, vendor installers, photos

## Quick start
```
python3 -I tools/omfw.py info firmware/stock/OLY_E_113_1400_0000_0000.BIN
python3 -I tools/omfw.py dec  firmware/stock/OLY_E_113_1400_0000_0000.BIN firmware/stock/dec
python3 -I tools/fwpatch.py plan STOCK.BIN PROFILE.json --id em10-1.4
python3 -I tools/symbol_index.py --once 0x7de57532
python3 -I tools/symbols.py stats
python3 tools/emcam.py info                       # on the camera's Wi-Fi; see tools/README.md
python3 -I tools/dis.py 7de57e24 7de58a90        # needs mn10300-elf-objdump, see docs/STATUS.md
```
