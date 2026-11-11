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
| `subsystems.py` | group `FuncStrings.java` output by log-tag prefix |
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
