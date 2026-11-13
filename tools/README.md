# tools

Our own scripts. Python is stdlib-only unless noted; run anything that reads firmware or vendor
files with `python3 -I`. Outputs derived from vendor data (decoded blocks, icons, strings, images)
go under gitignored `firmware/` or `research/` and are never committed.

## Firmware container and patching
| script | purpose |
|---|---|
| `omfw.py info\|dec\|rebuild` | container codec: list blocks, decode, re-encode and reseal footers |
| `fwpatch.py plan\|build` | apply a patch profile (external JSON) to a stock BIN, with hash and old-byte checks |
| `dbfw_verify_patch.py` | original standalone check of the community ring-native patches; `fwpatch.py plan` covers it |
| `dbfw_extract_em10.py` | pull the E-M10 entries out of the community tool's profile/compatibility JSON |
| `pyi_extract.py` | static PyInstaller archive reader (never executes the target) |
| `fetch-firmware.sh [CODE] [--download]` | query the OM firmware server; optionally download the BIN to `firmware/stock/` |

## Block 0 (code) analysis
| script | purpose |
|---|---|
| `dis.py START END` | annotated disassembly at runtime addresses; needs `mn10300-elf-objdump` (see `docs/STATUS.md`) |
| `rtos_tasks.py` | dump the RTOS task id/name table |
| `verify_usb.py` | check live USB DeviceInfo findings against the per-mode opcode arrays in block 0 |
| `symbol_index.py` | address → doc index built from `docs/` only (output is committable) |
| `symbols.py stats\|export\|dupes\|candidates` | work with the three symbol documents: counts, name export for Ghidra, duplicate check, unlabelled functions by reference count |
| `func_patterns.py clusters\|small\|shapes` | find unlabelled functions that can be labelled as a group: byte-identical copies, one- and two-instruction bodies; needs `mn10300-elf-objdump` |
| `subsystems.py` | group `FuncStrings.java` output by log-tag prefix |
| `trace_catalog.py list\|ID...` | resolve the API layer's three-byte trace ids to names (`docs/firmware/trace-catalog.md`) |
| `opcode_intersect.py` | OM Workspace SDK opcodes vs the Mark I's own (`docs/usb-protocol/sdk-opcode-compat.md`) |

## Blocks 1/2 (resources)
| script | purpose |
|---|---|
| `resdump.py` | split a decoded resource block into directory entries |
| `strtab.py` | UTF-16 string table → TSV |
| `glyphs.py` | decode font glyphs to ASCII art |
| `icons.py` | decode OSD icon banks to PNG contact sheets |
| `jpgextract.py` | carve JPEG streams from a resource entry |
| `sheet.py fonts\|jpegs` | PNG contact sheets of fonts and carved JPEGs |

## OM Workspace binaries
| script | purpose |
|---|---|
| `survey_pe.py` | static survey of PE files: arch, exports, key imports |
| `rtti_vtables.py` | resolve MSVC x64 RTTI type names to vtables and slots |

## Live camera (read-only unless stated)
| script | purpose |
|---|---|
| `emcam.py` | Wi-Fi client: info, list/download/pull files, thumbnails, resized JPEGs, properties; state-changing: mode switch, set property, shutter, live view, power off; `probe` (read-only) and `livetest` (guided, asks before each state-changing step) write reports for a live run. `emcam.py -h` lists everything |
| `emcam_mock.py [PORT]` | fake camera for developing clients offline (same replies, per-mode errors, live-view stream); use with `emcam.py --host 127.0.0.1:PORT` |
| `ptpraw.py` | minimal raw PTP client over libusb: OpenSession, GetDeviceInfo; no writes |
| `probe-camera-wifi.sh` | join the camera AP, query read-only CGI endpoints, rejoin home Wi-Fi |
| `probe-camprop.sh` | read-only camprop CGI test; `SWITCH=1` also switches camera mode and back |

The two probe scripts need `CAM_SSID` (camera AP name, `E-M10-P-<serial>`) and `HOME_CON`
(NetworkManager connection to rejoin) in the environment, and prompt for the camera Wi-Fi password
unless `CAM_PASS` is set.

## `ghidra/` — headless scripts
Run with `analyzeHeadless research/ghidra_proj em10 -process blk00_40300000.bin -noanalysis
-readOnly -scriptPath tools/ghidra -postScript <Script>.java <args>`. Drop `-readOnly` for the
scripts that rename.

| script | purpose |
|---|---|
| `ApplyNames.java TSV [dry]` | apply names from `symbols.py export` to the project (renames; run without `-readOnly`) |
| `DecompAt.java ADDR...` | decompile the functions containing the given addresses |
| `DisasAt.java ADDR N ...` | disassemble N bytes at each address (clears and re-disassembles: not for `-readOnly`) |
| `DumpDecomp.java OUT` | decompile every function into one C file |
| `Callers.java ADDR` | callers of a function, with call sites |
| `DataRefs.java ADDR` | instructions referencing a data address, with read/write type |
| `ScalarRefs.java LO HI` | instructions with a scalar operand in a range |
| `StringXrefs.java TEXT...` | strings containing a substring and the functions that reference them |
| `FindFunc.java TEXT...` | functions whose name contains a substring |
| `ListFuncs.java N` | function count and first N functions |
| `FuncStrings.java OUT` | TSV of functions with callers, callees and referenced strings |
| `NameFuncs.java OUT` | auto-name functions from referenced strings (renames) |
| `VTables.java OUT [rename]` | find vtable-like arrays; optionally name members |
| `VtRefs.java TSV MIN` | functions referencing vtable candidates |
| `ClassGraph.java TSV OUT [rename]` | inheritance and constructor naming from vtables |
| `ImmHist.java MIN` | histogram of 32-bit immediates by 1 MB bucket |
| `NibbleFuncs.java` | find candidate nibble/RLE decoder functions |

## Labelling workflow
1. `symbols.py candidates 20 99999 40` — pick unlabelled functions, most referenced first.
2. Read them with `dis.py` or `ghidra/DecompAt.java`; for groups use `func_patterns.py`.
3. Add rows: hand-analysed ones to `docs/firmware/symbol-map.md`, machine-listed groups to
   `symbol-families.md` with one explanation per group, string-derived names to `symbol-strings.md`.
   When a script appends to one of these files, read the file before opening it for writing.
4. `symbols.py dupes` — no address should gain a second row.
5. Commit per batch. Optionally `symbols.py export names.tsv` and `ApplyNames.java` to refresh Ghidra.
