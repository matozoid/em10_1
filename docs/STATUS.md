# Status (2026-11-11)

Current state of the E-M10 Mark I project. The chronological log for 2026-11-01/02 (first-day
findings, superseded TODO lists, Ghidra setup notes) is archived in
[`STATUS-log-2026-11-01_02.md`](STATUS-log-2026-11-01_02.md).

## Ground rules
- **The body is never opened.** No teardown, UART pads, JTAG or chip-off. Everything is static RE
  plus what the camera exposes over USB, Wi-Fi and the SD card.
- **Camera-state changes need the owner's go-ahead.** Read-only probes are fine. State-changing
  calls (`set_camprop`, shutter, GPS write) are confirmed with the owner each time.
- **No patched firmware is flashed.** The owner considers it too risky for now (2026-11-11); nothing
  has ever been flashed. Patched images are built and verified locally only.
- **Third-party material stays local.** Stock/community firmware, the community patch profile,
  decompiles and unpacked vendor software live in gitignored `firmware/`, `research/` and
  `reference/`. Only our own docs and tools are committed.
- **Symbol labelling is committed in batches** (per session or subsystem), not one commit per label.

## Target
| item | value |
|---|---|
| Body firmware | 1.4 (latest for the Mark I), `OLY_E_113_1400_0000_0000.BIN`, 70 254 592 B, sha256 `84d81b2d…` |
| Model / update id | 113 / 1130; camera-ID code `S0051` |
| CPU | Panasonic MN103 / AM33 (dual core), uITRON RTOS |
| Runtime base | block 0 executes at `0x7d991020` (container load address `0x40300000` is packaging only) |
| Wi-Fi chip | Broadcom BCM43362 over SDIO; chip firmware `43362a2-roml/sdio-apsta-idsup-idauth-pno`, built 2012-10-29 (strings returned by `bcm_fw_version_strings` `0x7e88982f`) |
| Wi-Fi | camera AP `E-M10-P-<serial>`, HTTP CGI at `192.168.0.10:80`, OI.Share descriptor v2.20 |
| USB | VID `07b4`; PTP/MTP only |

## Done

### Firmware container and patch pipeline — `firmware/container-format.md`, `mods/`
- Container codec cracked and reimplemented (`tools/omfw.py info|dec|rebuild`): 3 blocks, XOR +
  16-byte permutation, additive footer checksum. Round-trip is byte-exact.
- Model-agnostic patch engine `tools/fwpatch.py plan|build`, driven by an external profile JSON.
- Community patcher "db firmware 0.3.1.b" unpacked statically (never executed) and understood:
  `firmware/community-dbfw-tool.md`, `mods/community-feature-patches.md`,
  `mods/ring-cave-disassembly.md`.
- **"1.4 + ring-native" image built and verified locally** (`firmware/community/em10-1.4-ring/E1139999.BIN`,
  sha256 `837ecc9e…`, equal to the profile's expected output). Only block 0 differs from stock:
  1202 bytes, all inside the 9 declared patch regions. Headers are byte-identical to stock.
  See `mods/patching-pipeline.md`.

Ring-native hook sites (load-space addresses; add the runtime delta from `firmware/memory-map.md`).
All are `jmp` (opcode `DC`, rel32) into the payload cave `0x40326ff0..~0x40327400`, which is all
`0xFF` in stock:

| hook | site | target |
|---|---|---|
| parser | 0x4041b411 | 0x40326ff0 |
| input | 0x40450b06 | 0x40327048 |
| callback | 0x4042a4a2 | 0x40327178 |
| reset | 0x4041289b | 0x403271f4 |
| init | 0x40414daf | 0x40327208 |
| request | 0x4042a1ac | 0x403272e0 |
| guard | 0x4042a71b | 0x403273e0 |

`loader_patch@0x403001ab` is a no-op in this profile (old == new).

### In-camera firmware update — `firmware/camera-fw-update.md`, `firmware/flash-storage.md`
- **SD-card scanner located.** Task `FIRMUP_CLI` (creation id 0x14, entry `0x7de57532`) scans `DCOLYMP/`
  for `E113????.BIN` (body) and per-letter sub-component files; `E1139999.BIN` matches. It posts to
  `FIRMUP_SRV` (`0x7de57942`), which also serves the USB route. **What starts the scanner is not
  found.** Live: power-on with OK held and no firmware on the card boots 1–2 s slower; MENU or INFO
  held does not. That fits "OK selects the scan, it finds nothing, startup continues" but does not
  prove the delay is the scan.
- **Pre-flash validation fails closed.** Structural region-table parse (error `0x3321`/`0x3322`),
  image-id `'E'` check, and `usr_checksum` (error `0x3202`). Any failure aborts before writing.
- **`usr_checksum` is a header↔tail duplicate-array check, not a payload hash.** Mid-payload patches
  do not touch either 20-byte window, so the built ring-native image passes every packaging gate
  statically. Only its runtime behaviour on the real body is unverified.
- **Recovery is unproven.** The updater tasks live inside block 0, and the code that selects an SD
  update at power-on is unknown. A patch that breaks only the lens/rec path would probably leave
  an update route available; a patch that breaks boot, the scheduler or the SD stack would not.
- USB PC-link update (`startFirmUp` `0x7e21d6dc`) is located but the flash routine sits behind a
  runtime vtable slot; not followed further.

### Firmware internals — `firmware/`
- Block 0 in Ghidra: ~72.5k functions, ~10.4k auto-named from debug strings, vtable and class-graph
  renames (`classes.md`, `blocks.md`, `memory-map.md`).
- Task registry: 134 tasks with id, entry, priority, stack (`rtos-tasks.md`). **Names are shifted by
  one over at least part of the table** (see the correction there); needs re-deriving.
- **`symbol-map.md`: about 1 340 curated address rows** across ~40 subsystems: heap allocator, object
  model, OS/IPC primitives, libc cluster, soft-float, GUI app / panel manager / Super Control Panel,
  playback components (Cmp*), movie playback, AE, sensor black-correction, audio codec, VG draw
  engine, embedded Expat 1.95.5, OKAO face detection, on-camera httpd. `tools/symbol_index.py`
  regenerates the address→doc index.
- Mask-ROM primitives pinned from call sites: `0x47001000` memcpy, `0x4700110c` memset.
- Reset entry at `0x7d991020` is real startup code; on-chip interrupt controller at abs16
  `0x8000–0x80xx`; ISR dispatcher `0x7d9a1920` (`hardware/boot-and-io.md`).
- Blocks 1/2 resources fully decoded: 34 string tables, 34 fonts, 32 JPEGs, 3270 icon records
  (`resources.md`; `tools/glyphs.py`, `icons.py`, `jpgextract.py`).
- Display ASIC command set (`hardware/display-pipeline.md`).

### Wi-Fi — `firmware/wifi-cgi.md`, `usb-protocol/wifi-api.md`, `usb-protocol/liveview-udp.md`
- Every CGI in `get_commandlist` (23) and every rec-dispatcher leaf has a traced handler. Read-only
  calls verified live. Error codes 1001/1002/1004/1005 mapped.
- Live-view MJPEG-over-UDP wire format documented from OI.Share.
- No firmware update over Wi-Fi on this body (no `fwup_*`), no PTP/IP responder on TCP 15740.
- Cross-checked against `n0p/om-tether` (OM-1 II, descriptor v5.20): same CGI family, newer generation.

### USB — `firmware/usb-ptp.md`, `usb-protocol/`
- PTP is mailbox-driven (`TSK_PTPCOM`); there is no static opcode→handler table.
- Advertised vendor ops: 18 (`0x902c–0x902f`, `0x9116–0x9125`, `0x9801–0x9805`). Internal engine ops: 54.
- **OM Workspace's SDK command set is a different protocol generation** (`0x94xx`); it shares
  nothing usable with the Mark I (`usb-protocol/sdk-opcode-compat.md`). `0x9481`/`0x9482` stall live.
- No PTP memory-read op exists.

### Debug shell — `firmware/debug-shell.md`
- 59-command "USF debugging shell 1.10" mapped, including `flash addr` and `file memdump`.
- **Not reachable on stock 1.4 without opening the body.** Telnet is closed (live-tested), `0x8050`
  is the active-interrupt register and not a debug flag, the dispatch is driven by an autoexec script
  behind SFR latch `0x8ff00190 = 0x12345678`, and the interactive console is UART.

### OM Workspace / OI.Share — `workspace/`, `firmware/update-server.md`, `firmware/updater-ow-2.5.md`
- ORF/MakerNote reader, RAW decode pipeline, model selection, plugin architecture documented.
- Firmware update server protocol documented; stock 1.4 BIN obtained through it.
- Mark I (`S0051`) has no CameraSimulation profile in the current Workspace build.

## Not done
- **No flash of a patched image on the real camera**, and none planned while the owner judges the
  risk too high. Procedure and risk analysis are in `mods/patching-pipeline.md`.
- **No mod of our own.** Everything built so far reproduces the community ring-native patch. There
  is an MN10300 assembler and linker (binutils) but no C compiler, and no payload build setup.
- **ROM pictures at `0x46560000` are not extracted.** The only remaining route is a patch that dumps
  flash to SD or forces the shell up (`mods/firmware-modding.md`).
- **KMP app**: `app/` is an empty directory. Plan in [`ARCHITECTURE.md`](ARCHITECTURE.md).
- Stock firmware 1.0–1.3 BINs are not available.

## Open RE items
- What starts the SD scanner task at power-on (OK held), and whether that code is inside block 0.
- Re-derive the task registry names from the names the boot code logs (ids are shifted by one).
- Battery-level and version gates before an update; whether a written image is read back and verified.
- `0x7d9929ce` / `0x7d9928ee` flash commit (NAND-controller register sequence) — `flash-storage.md`.
- `0x7da82530` thunk → worker `0x7da8254b` in the firmup apply path.
- Entry functions of imaging/PTP/Wi-Fi tasks beyond the firmup set.
- Per-letter sub-component mapping of `S/G/H/W/A/M/V/D/T/I/N113????.BIN`.
- USB PC-link flash routine behind vtable slot +36; arg-ids 334–337.
- MMIO identity: `0x98001000` block, `0x8ff00000`, `0x99400000`, `0x9a000000–0x9e000000`; the 7
  boot-programmed interrupt channels are not tied to named sources.
- `switch_cammode` transition matrix (partially traced); camprop value encodings; GPS-write field layouts.
- `set_camprop` / `exec_shutter` live test (state-changing; ask first).
- Deferred as low value: `MDP_AS` CameraSimulation schema, `OlyBayerDecoder` demosaic math.

## Environment
- Ghidra 12.2 at `~/dev/ghidra_12.2_PUBLIC` with `michaelbrandi/ghidra-mn103-extension`
  (language `mn10300:LE:32:default`); project in `research/ghidra_proj/`. Headless scripts in
  `tools/ghidra/`. The extension is per-user: copy its `data/`, `Module.manifest` and
  `extension.properties` to `~/.config/ghidra/ghidra_12.2_PUBLIC/Extensions/mn103/` and run
  `$GHIDRA/support/sleigh mn103.slaspec` in `data/languages`. Open the project headless with
  `analyzeHeadless research/ghidra_proj em10 -process blk00_40300000.bin -noanalysis -readOnly
  -scriptPath tools/ghidra -postScript <Script>.java <args>`.
- GNU binutils 2.42 for `mn10300-elf` in `/usr/local/bin` (`mn10300-elf-objdump`, `-as`, `-ld`, ...).
  Build: `configure --target=mn10300-elf --prefix=/usr/local --disable-nls --disable-gdb
  --disable-sim --disable-gprofng --disable-werror`, then `make MAKEINFO=true` and
  `sudo make MAKEINFO=true install`. The `--target` is essential: without it a native binutils is
  installed that shadows the system `ld`/`as`. Build tree kept at `~/dev/binutils/mn10300/build`.
- `tools/dis.py START END` = annotated disassembly of block 0 at runtime addresses (hex immediates
  and referenced strings added to objdump's output).
- Decoded blocks in `firmware/stock/dec/`; resource extracts in `firmware/stock/res1`, `res2`,
  `jpg2`, `sheets`.
- Run Python tools that read firmware or vendor files with `python3 -I`.
