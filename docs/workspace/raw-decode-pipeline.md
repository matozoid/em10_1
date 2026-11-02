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

## Stage-plugin ABI (plant codename DLLs)

Every develop-stage DLL exports the **same 3-function plugin ABI**, codename-substituted:

```
OlyGet<Name>Instance     // return the stage's filter/develop instance
Oly<Name>Initialize      // one-time stage init
Oly<Name>Finalize        // teardown
```

seen for Maple, Peony, Loquat, Walnut, Pomegranate, … . `OlyLoquat` adds
`OlyLoquatCliviaSkipSwitch` — a toggle for the **Clivia** GPU path (`OlyCliviaCheck` →
`cudart64_12`), i.e. skip-GPU/CPU-fallback control. So each plant DLL is a hot-pluggable develop
stage returning a COM-style instance; the host chains them.

### Codename → engine generation (decompiled + RTTI-mapped)

The plant DLLs are **not** single filter steps — each is a full **TruePic image-engine-generation
raw processor**. `OlyGetMapleInstance` builds a **`COlyDC9RawProc`** (5544-byte state object;
vtable `+0x98` = configure/open, `+0x08` = AddRef; `OlyMapleInitialize`/`Finalize` just set up /
tear down two `CRITICAL_SECTION`s). RTTI across the set:

| DLL | generation | components present |
|---|---|---|
| `OlyMaple` | **DC9** | `COlyDC9RawProc`, `DC9NR`, `DC9CameraSimulation`, `DC9DisplayParameters`, `DC9ParamManage(OWN)` |
| `OlyPeony`, `OlyPomegranate` | **DC11** | `COlyDC11RawProc`, NR (`DC9NR`), `DC11CameraSimulation`, `DC11DisplayParameters`, `DC11ParamManager` |
| `OlyWalnut`, `OlyLoquat` | **DC13** | `COlyDC13RawProc`, `DC13NR`, `DC13CameraSimulation`, `DC13DisplayParameters`, `DC13ParamManager` |
| `OlyPoplar` | DC11+DC13 | `ParamManager` (cross-gen parameter orchestration) |
| `OlyAcacia` | DC13 | `DC13NRCM` (noise reduction / colour management) |

So each generation engine bundles: **RawProc** (develop core), **NR** (noise reduction),
**CameraSimulation** (reproduce the in-camera OOC-JPEG look — Picture Modes / colour), 
**DisplayParameters**, and **ParamManager** (the develop-knob manager = the sub-objects behind
`IOlyIPRawParameter`). `OlyMuse`'s art filters carry matching `_DC9`/`_DC11`/`_DC13` suffixes
(`architecture.md`): the whole develop path is bucketed by engine generation.

Open: which DCx the E-M10 Mark I (TruePic VII) selects — the RawProc `+0x98` configure path keys
off camera/model; needs a decompile of that selector or a live develop trace to pin. For a
replacement, **`CameraSimulation`** is the component to study to match OOC-JPEG rendering.

## Working model (to confirm by decompilation)

1. olive `COlyImgFmtOrf` opens the ORF/TIFF container, resolves IFD0 strips + MakerNote
   (`orf-format.md`), and yields raw 12-bit Bayer samples (strip read reused from the TIFF base —
   no ORF-specific compression strings seen, so unpack is plain TIFF strip handling).
2. `OlyImgProc2` `GetRawDecorder` → `IOlyImageDecoder` wraps those samples as a `COlyIPRawImage`
   under an `IOlyIPRawParameter` (WB, color matrix, gamma, develop mode set via
   `SetRawParameter` / `OlyIP2_SetInitialDecodeModeForRawParameter`).
3. `COlyBayerDecoder` in the active stage DLL demosaics to RGB; subsequent plant stages apply
   NR / color / sharpening; art filters via `OlyMuse` (`architecture.md`).

## Verified decode contract (decompiled)

`OlyImgProc2` only *brokers* the decoder; the concrete decoder is injected from a stage DLL.

- **`COlyFilterParam`** holds two raw-parameter objects: `+0x18` (primary) and `+0x20`
  (secondary/fallback). `SetRawParameter(p1, p2)` releases any prior, `AddRef`s + stores both,
  and sets the dirty flag at `+0xd`.
- **`GetRawDecorder(IOlyImageDecoder** out)`** calls the primary raw param's vtable **`+0x48`**
  (GetDecoder); on failure it retries the secondary. It returns whatever decoder the raw param
  holds — OlyImgProc2 does not create one.
- **`IOlyIPRawParameter` object layout**: `+8` = the **`IOlyImageDecoder`** instance (GetDecoder
  `+0x48` just returns `this+8` AddRef'd); `+0x10 … +0x58` = ~10 further COM sub-objects = the
  develop knobs (WB / color matrix / tone / NR / …), each released in the param's release-all
  method. So the concrete `COlyBayerDecoder` (from the active stage DLL) is slotted into
  `rawParam+8` by the host, then surfaced through this interface.
- **`OlyIP2_SetInitialDecodeModeForRawParameter(u16 mode)`** writes a **process-global** default
  decode mode into a static `COlyIPRawImage` config blob (`s___AVCOlyIPRawImage… + 0x1c`), i.e. a
  one-time initial mode applied to newly built raw params.

Contract for a replacement: build/obtain an `IOlyImageDecoder` (the Bayer decoder), wrap it + the
develop sub-objects in an `IOlyIPRawParameter`, hand that to `COlyFilterParam::SetRawParameter`,
then pull the decoder back via `GetRawDecorder`. The pixel math lives in `COlyBayerDecoder`
(stage DLLs) — the next thing to decompile for the actual demosaic/develop algorithm.
