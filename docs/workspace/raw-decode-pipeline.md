# RAW decode pipeline — `OlyImgProc2.dll` + stage DLLs

Deep-dive #2 (see `architecture.md`). Where RAW pixels are turned into an image, downstream of
olive's ORF container reader (`orf-format.md`). Static recon; `OlyImgProc2.dll` imported into the
Ghidra project for decompilation. Interop RE, kept local.

## Framework vs concrete

`OlyImgProc2.dll` is the **develop/filter framework**, namespace `OLYIP2`. It does **not** contain
Bayer/demosaic/ORF code itself (no such strings). The RAW entry point is an export on
`COlyFilterParam`:

- `GetRawDecorder(IOlyImageDecoder** out)` [export 191] — hands back a decoder interface in
  namespace **`OLYIMGDEC`** (`IOlyImageDecoder`); the concrete decoder is supplied from outside.
- `SetRawParameter(IOlyIPRawParameter*, IOlyIPRawParameter*)` [206],
  `ClearRawParameter()` [162], `OlyIP2_SetInitialDecodeModeForRawParameter(u16)` [194].

Key framework RTTI: `COlyIPDecodeImage` (+ nested `CDecodeProgressCB`), `COlyIPRawImage`
(+ `CRawProgressCB`), `COlyIPRawParameter`, `COlyRawEditModeParam`,
`COlyIPFilterRawArtFilter` / `COlyIPFilterRawArtEffectFilter`. Interfaces (exported IIDs):
`IID_IOlyIPDecodeImage`, `IID_IOlyIPRawImage`, `IID_IOlyIPRawParameter`,
`IID_IOlyIPFilterRawArtFilter`, `IID_IOlyIPFilterRawArtEffectFilter`, `IID_IOlyIPDrawRequest`.

## Concrete demosaic — `COlyBayerDecoder`, replicated per stage

The actual sensor-to-RGB code is class **`COlyBayerDecoder`**, statically linked into **every
develop-stage plant DLL**: `OlyLoquat`, `OlyPeony`, `OlyWalnut`, `OlyPomegranate`, `OlyMaple`
(and demosaic strings also in `OlyPoplar`, `OlyDonna`, `OlyLaurel`). Each stage carries its own
copy — the pipeline is a chain of these stages (demosaic, NR, color, sharpen), several with a
GPU path (`OlyCliviaCheck`→`cudart64_12`, plus `opencv_world3416`). `OlyPoplar` additionally
exposes `IOlyCameraRawDevelopEventHandler` (ns `OLYCAM`) — the camera-develop event surface.

## Working model (to confirm by decompilation)

1. olive `COlyImgFmtOrf` opens the ORF/TIFF container, resolves IFD0 strips + MakerNote
   (`orf-format.md`), and yields raw 12-bit Bayer samples (strip read reused from the TIFF base —
   no ORF-specific compression strings seen, so unpack is plain TIFF strip handling).
2. `OlyImgProc2` `GetRawDecorder` → `IOlyImageDecoder` wraps those samples as a `COlyIPRawImage`
   under an `IOlyIPRawParameter` (WB, color matrix, gamma, develop mode set via
   `SetRawParameter` / `OlyIP2_SetInitialDecodeModeForRawParameter`).
3. `COlyBayerDecoder` in the active stage DLL demosaics to RGB; subsequent plant stages apply
   NR / color / sharpening; art filters via `OlyMuse` (`architecture.md`).

Next: decompile `GetRawDecorder` + `COlyIPDecodeImage` to pin the decoder hand-off and the
`IOlyIPRawParameter` field layout (the develop knobs a replacement must drive).
