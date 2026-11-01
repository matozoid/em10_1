# OM Workspace — binary architecture map

Static survey of the installed OM Workspace (`research/owsetup_x/app/`, ~90 PE modules, x64
except the 32-bit `FWUP/` updater set). Produced with `tools/survey_pe.py` (file/objdump/strings,
no execution); full dump in `research/decomp/ws_survey.txt`. Build strings show all first-party
DLLs come from `D:\src\OM\CommonLib-Windows\Common\...` (MSVC v142). This maps what each module
does so deep-dives can be targeted; it is reverse-engineering for interoperability, kept local
(see EULA note in `docs/mods/firmware-modding.md`).

## Top-level

- **`OM Workspace.exe`** — GUI shell (MFC, `mfc100u`). Links the image facade (`OlyImgProc2`,
  `OlyImgView`), file manager (`FileMgr2`), UI framework (`OlyUIFrw2`/`OlyUICtl2`), DB
  (`OlyDB4`), common lib (`olive`).
- **`OlyComSvc.exe`** — online/Wi-Fi communication service; imports only `WININET` (HTTP). **Not**
  USB/PTP — not a camera-control component.
- **`FWUP/` set** — standalone 32-bit firmware updater (`CameraUpdate.exe` + stripped copies of
  the Oly* libs + `OlyGross.dll`). Firmware-flash side; see `../usb-protocol/firmware-update.md`.
- **`cmd*.exe`** — headless batch/decode workers (`cmdBatch`, `cmdDecode`, `cmdBatchVideo`).

## Image pipeline (the heart of a Workspace replacement — largely un-analyzed)

Dataflow: **olive** (open file + metadata) → **OlyImgProc2** (decode RAW + filter framework) →
stage DLLs / **OlyMuse** (develop + art filters) → **OlyImgView** (render) / `cmdDecode` (export).

- **`olive.dll`** — misnamed "CommonLib": the **file-format + metadata + image-property layer**,
  imported by nearly every image DLL. Named exports:
  - file I/O: `OlyOpenFile`, `OlyCloseFile`, `OlyMapImage`, `OlyUnmapImage`, `OlyCreateInstance`,
    `OlyGetImgPropertyInstance`
  - EXIF/TIFF model: `IOlyExifIterator`, `IOlyIFDStore`, `IOlyTiffOperator`, `IOlyListExifID`,
    `IOlyStackExifID`, `IOlyImgProperty`/`IOlyImgProperty2`, `IOlyMPProperty`, `IOlyGPSProperty`,
    typed array interfaces (`IOlyRationalArray`, `IOlySRationalArray`, …)
  - **ORF / MakerNote**: `AddExtendMagicNumber`, `IsExtendMagicNumber`, `IsMakerNoteIFDTag`,
    `SetMakerNoteIFDTags` — Olympus RAW container + proprietary MakerNote IFD handling
  - `IOlyWhiteBalanceAdjust` — WB metadata
- **`OlyImgProc2.dll`** (155 exports) — the **develop/filter framework** (namespace `OLYIP2`).
  COM filter model `COlyBaseFilter` / `COlyFilterParam` implementing `IOlyIPFilter`, operating on
  `IOlyImage`. Key methods: `DoFilter`, `DoColorTransform`, `DoCustomTransform`,
  `DoGeometricTransform`, resamplers `DoFilterBiCubic`/`BiLinear`/`NearlestNeighber`,
  `ConvertRGB2YCC`. RAW entry: `GetRawDecorder` → `IOlyImageDecoder` (ns `OLYIMGDEC`),
  `IOlyIPRawParameter` + `SetRawParameter`/`ClearRawParameter`,
  `OlyIP2_SetInitialDecodeModeForRawParameter`. Filter IIDs: `IOlyIPFilterArt`,
  `IOlyIPFilterClearlyReduction`, `IOlyIPDustScratchFilterParam`, `IOlyIPDecodeImage`,
  `IOlyIPBatchFile`.
- **`OlyMuse.dll`** (9 MB) — **art-filter implementations** on RAW. `OlyGetRawArtFilter` + one
  interface per effect: Diorama, ToyCamera/ToyShading, GrainyFilm, SoftFocus, CrossFilter,
  Vintage, ShadeEffect, BlackOut, WhiteOut, GizaFrame, PlaCameraShading, `Oly Raw_ShadingCreator`.
  Suffixes `_DC9`/`_DC11`/`_DC13` = camera-generation variants of each effect.
- **Stage DLLs** (plant codenames, all import `olive` + `VCOMP`/OpenCL/CUDA → parallel kernels):
  `OlyLaurel` `OlyPoplar` `OlyWalnut` `OlyPeony` `OlyPomegranate` `OlyMaple` `OlyAcacia`
  `OlyClover` `OlyHibiscus` `OlyCamellia` `OlySunflower` `OlyLoquat`. Individual develop stages
  (demosaic, noise reduction, color, sharpening). `OlyCamellia` despite the name is an **image
  stage**, not camera comms. Several import `OlyCliviaCheck` → `cudart64_12` (GPU path).
- Support: `opencv_world3416` (OpenCV 3.4.16), `cudart64_12`/`110` (CUDA), `tbb` (Intel TBB),
  `XMPCore`/`XMPFiles` (Adobe XMP sidecar), `OlyDB4`→`OSLite` (SQLite catalog), `FileMgr2`
  (library/file mgmt), `OlyImgView` (viewport render), `vedFramework`/`Mag*` (movie/VED).

## Camera / firmware side (mostly already analyzed)

- **`OlyCameraLib.dll`** — the PTP camera SDK (self-contained: imports only `IPHLPAPI`, `PSAPI`,
  `OlyLog`). Opcode table + firmware-update protocol already extracted:
  `../usb-protocol/olympus-opcode-table.csv`, `../usb-protocol/firmware-update.md`. Decompile in
  `research/decomp/OlyCameraLib.c`.
- **`CameraUpdate.exe`** (FWUP) — updater front-end; decompile `research/decomp/CameraUpdate.c`.
  Imports `OlyGross.dll` (flash worker — the remaining firmware-side gap) + `olive`.
- **`OlyGin.dll`**, **`OlyWebXMLMgr.dll`** — decompiled (`research/decomp/OlyGin.c`,
  `OlyWebXMLMgr.c`); Wi-Fi / web-XML remote side.

## Remote camera control — two planes (don't conflate)

Workspace bundles a *full* tethered-control SDK, but it is the wrong plane for this body:

- **USB PTP control** — `OlyCameraLib.dll` (decompile `research/decomp/OlyCameraLib.c`) is a
  complete tethered SDK: LiveView, capture/shutter, RUN_MODE switching, `SetProperty`, and the
  opcode table (`../usb-protocol/olympus-opcode-table.csv`) has 65 control ops (0x9481–0x94de),
  420 device props (0xd0xx), 30 events (0xc0xx). The OM Workspace **GUI does not expose this**
  (no capture/tether strings in `OM Workspace.exe`); tethered shooting is the separate **OLYMPUS
  Capture** app on the same SDK. **The E-M10 Mark I does not implement the 0x94xx USB control
  interface** — proven live: it stalls 0x9481 and reports "No Image Capture" (see
  `../firmware/usb-ptp.md`). So this plane is unusable for this body.
- **Wi-Fi CGI control** — the OI.Share plane, and the one that actually works on the E-M10
  Mark I (verified live via `get_commandlist.cgi`, API 2.20). Full live view
  (`exec_takemisc?com=startliveview&port=`), shutter/AF (`exec_shutter`, `exec_takemotion`),
  and settings (`set_camprop`/`get_camprop`: takemode, aperture, shutter, ISO, expcomp, WB,
  artfilter). Plain HTTP on 192.168.0.10 → cross-platform, usable directly by the KMP app. See
  `../usb-protocol/wifi-api.md`. **This is the remote-control path for the replacement.**
  Still un-RE'd: the live-view UDP stream wire format (the `startliveview&port=` payload).

## Picked deep-dive targets (post-survey)

1. **`olive.dll` ORF + MakerNote reader** — foundational: a replacement must read .ORF and its
   Olympus MakerNote/WB/EXIF before anything else, and this layer is small and self-contained.
   **First dive.**
2. **`OlyImgProc2.dll` raw decoder + filter framework** — the develop pipeline contract
   (`IOlyImageDecoder`, `IOlyIPRawParameter`, `COlyBaseFilter`).
3. **`OlyMuse.dll` art filters** — per-effect algorithms, once the framework is understood.
