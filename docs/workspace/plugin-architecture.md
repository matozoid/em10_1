# OM Workspace plugin architecture — `PluginMgr` + MDP/FNP plugins

Static recon of `research/owsetup_x/app` (current OM Workspace, 2025-07-22; interop RE, kept local).
Explains the `app/plugins/*.omdp` / `*.ofnp` files referenced from `model-selection.md`.

## The plugin files are renamed PE32+ DLLs

Every `app/plugins/*.omdp` and `*.ofnp` begins `MZ…` and is a **PE32+ x86-64 DLL** (just a
non-`.dll` extension). Each exports a **single COM-style factory**:

| extension | factory export | kind |
|---|---|---|
| `.omdp` | `OlyCreateMediaPluginInstance` | **MDP** = Media (format/develop) plugin |
| `.ofnp` | `OlyCreateFuncPluginInstance` | **FNP** = Function (app-feature) plugin |

(`FNP_Browser.ofnp` additionally exports `OlyGetUpdateEditImageMgr` /
`OlyFinalizeUpdateEditImageMgr` — an edit-image-manager singleton; all others export only the one
factory.)

## Host loader — `PluginMgr.dll`

`PluginMgr.dll` is the host that loads and dispatches both plugin families (it is the only module
holding the factory-export name strings). RTTI / exports (namespace **`OLYPLGMGR`**):

- Interfaces: `IOlyPluginManager`, `IOlyMediaPluginManager`, `IOlyFuncPluginManager`.
- Classes: `COlyPluginManager`, `COlyMediaPluginManager`, `COlyFuncPluginManager`,
  `COlyPluginIterator` (enumerates discovered plugins).
- Source files: `OlyPluginManager.cpp`, `OlyFuncPluginManager.cpp`.
- Lifecycle/accessor exports:
  - MDP side: `OlyMDPMgrInitialize` / `OlyMDPMgrFinalize`, `OlyGetMDPMgrInstance`, per-plugin
    `OlyMDPInitialize`.
  - FNP side: `OlyFNPMgrInitialize` / `OlyFNPMgrFinalize`, `OlyGetFNPMgrInstance`, per-plugin
    `OlyFNPInitialize`.

So Workspace is a thin host over two plugin managers: the host calls `OlyGet{MDP,FNP}MgrInstance`,
the manager scans `app/plugins/` for `*.omdp` / `*.ofnp`, `LoadLibrary`s each, resolves the single
factory export, and builds plugin instances it iterates via `COlyPluginIterator`.

## The two plugin families

**MDP — media/format plugins** (`.omdp`, one per media type the app reads/develops):

| plugin | role |
|---|---|
| `MDP_Raw` | RAW (ORF) develop — generic, not model-named (`model-selection.md`) |
| `MDP_AS`  | **Art/colour Simulation** — the per-model `CameraSimulation` data (OOC-JPEG look); the only plugin carrying the camera-ID→model table |
| `MDP_JPEG2` | JPEG decode |
| `MDP_Tiff` | TIFF |
| `MDP_DS` | (display/down-sample?) |
| `MDP_GDIP` | GDI+-backed decode |

**FNP — function plugins** (`.ofnp`, one per app feature):
`AGPS`, `Browser`, `CameraRawDev`, `Composite`, `CompositePlus`, `FocusAnalyzer`, `OlySupport`,
`Print`, `Stitch`, `Timelapse`, `Transfer`.

## Why this matters for the replacement

- The OOC-JPEG colour engine is reachable as a **self-contained plugin DLL** (`MDP_AS.omdp`) with
  one documented factory (`OlyCreateMediaPluginInstance`) — not tangled into the main app. A
  Mark I (`S0051`) colour profile, if recovered from an **older** Workspace/Viewer 3 `MDP_AS`,
  would plug into this same ABI.
- The develop pipeline DLLs (`OlyImgProc2` + DCx stage DLLs, `raw-decode-pipeline.md`) sit *below*
  `MDP_Raw`; `MDP_Raw` is the plugin face the host sees, the DCx engines are its backend.

## Open / next

- Decompile `MDP_AS`'s `OlyCreateMediaPluginInstance` + the instance vtable to learn the per-model
  profile lookup (keyed on CameraType2 code) and the on-disk layout of a `CameraSimulation`
  profile block — the schema needed to read a Mark I profile out of an older `MDP_AS`.
