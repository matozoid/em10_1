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

## Picked deep-dive targets (post-survey)

1. **`olive.dll` ORF + MakerNote reader** — foundational: a replacement must read .ORF and its
   Olympus MakerNote/WB/EXIF before anything else, and this layer is small and self-contained.
   **First dive.**
2. **`OlyImgProc2.dll` raw decoder + filter framework** — the develop pipeline contract
   (`IOlyImageDecoder`, `IOlyIPRawParameter`, `COlyBaseFilter`).
3. **`OlyMuse.dll` art filters** — per-effect algorithms, once the framework is understood.
