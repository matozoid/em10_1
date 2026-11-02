# Camera-model selection — how OM Workspace keys develop/simulation by body

Open thread from `raw-decode-pipeline.md`: *which TruePic / DCx engine and which per-model profile
OM Workspace applies to an E-M10 Mark I file*. Static recon of the bundled Workspace install
(`research/owsetup_x/app`, build dated 2025-07-22 — current OM Workspace, interop RE, kept local).

## No model-name strings in the develop code

None of the develop/engine DLLs (`OlyImgProc2`, `OlyMaple`/DC9, `OlyPeony`/`OlyPomegranate`/DC11,
`OlyWalnut`/`OlyLoquat`/DC13, `OlyAcacia`, …) contain any `E-Mxx` / `OM-x` / `TG-x` model-name
string. Selection is therefore **not by display name** — it is by a numeric **camera-ID code** read
from the file's MakerNote (the ORF/JPEG **Equipment** sub-IFD tag `0x0100` *CameraType2*, a 6-char
string — see `orf-format.md`). The engine DLLs carry only a small set of these codes:

| DLL (engine gen) | camera-ID codes present |
|---|---|
| `OlyImgProc2`, `OlyLaurel` | `S0003`, `S0004` |
| `OlyLoquat`, `OlyWalnut` (DC13) | `S0067` |
| `OlyClover` | `S0067`, `S0080`, `S0089`, `S0092`, `S0095` |

## The model→code table lives in `MDP_AS.omdp`

The one place a full code↔model map exists is the **Art/colour Simulation** develop plugin
`app/plugins/MDP_AS.omdp` (2.1 MB) — this is the `CameraSimulation` data (reproduces each body's
in-camera OOC-JPEG / Picture-Mode look). The other MDP plugins carry no model table:
`MDP_Raw.omdp` (RAW develop params), `MDP_JPEG2`, `MDP_Tiff`, `MDP_DS`, `MDP_GDIP` all have **zero**
model-name or camera-ID strings — generic RAW develop is not per-model-gated here.

Records in `MDP_AS.omdp` are **code (6-char ASCII) immediately followed by the model name**; model
names store their Mark numeral as a Shift-JIS roman numeral (e.g. `E-M10Mark` + bytes `87 57` =
SJIS `0x8757` = Ⅳ ⇒ "E-M10 Mark Ⅳ"). Decoded pairs (newest→oldest in the table):

| code | model |
|---|---|
| `S0130` | OM-5 Mark II |
| `S0123` | OM-3 |
| `S0121` | OM-1 Mark II |
| `S0101` | OM-5 |
| `S0095` | OM-1 |
| `S0093` | E-P7 |
| `S0092` | E-M1 Mark III |
| **`S0088`** | **E-M10 Mark IV** |
| `S0080` | E-M1X |
| `D4605` | TG-7 |
| `A1034` | TG-7 Industry |
| `A1029` | OM-3 ASTRO |
| `A1027` | OM-1 Mark II RIR |

(TG/compact and special bodies use `D####` / `A####` codes; interchangeable-lens bodies use
`S####`.)

## Result for the E-M10 Mark I — profile absent (near dead end)

**The E-M10 Mark I (2014, TruePic VII) is not in this Workspace's model table at all.** The oldest
E-M10 present is the **Mark IV** (`S0088`); the oldest body of any line is roughly the 2019–2020
generation. So current OM Workspace ships **no `CameraSimulation` profile for the Mark I** — it
cannot reproduce the Mark I's exact OOC-JPEG colour/Picture-Mode rendering, because the per-model
simulation data for that body was dropped from the product.

Consequences for the KMP replacement:
- Generic RAW develop (`MDP_Raw` + a DCx engine) can still demosaic/develop a Mark I ORF — that
  path is not model-gated — but the colour "look" will be a generic develop, **not** a Mark I
  match.
- There is no Olympus-authored Mark I colour profile to extract from this build. Matching the Mark
  I OOC-JPEG look would require either an **older OM Workspace / Olympus Viewer 3** build (which
  still carried the Mark I simulation data) or deriving the profile empirically from Mark I
  OOC-JPEG vs RAW pairs shot on the user's camera.

## Open / next

- **Mark I camera-ID code unknown.** It is not in any bundled table. The definitive value is the
  *CameraType2* string in the Mark I's own files — read `Equipment:0x0100` from any Mark I ORF or
  JPEG MakerNote (the user has the camera; one sample file settles it). Cross-check against
  ExifTool's `%olympusCameraTypes`.
- Check whether an **Olympus Viewer 3** install (older) is obtainable to recover the Mark I
  `CameraSimulation` profile — the only Olympus-authored route to the exact look.
