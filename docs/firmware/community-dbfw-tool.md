# Community "db firmware" tool — architecture & patch schema (static recon)

Static analysis of the community firmware-mod app "db firmware" (azqeurio/om-c-firmware,
PyInstaller build, unpacked to `research/dbfw_extracted/`). **Never executed** (untrusted Windows
binary); only its bundled JSON/asset data was read. Purpose: understand how the community patches OM
firmware, and whether any of it applies to the E-M10 Mark I.

## Verdict for the E-M10 Mark I: not covered (dead end)

The tool ships patch profiles for a fixed set of **recent OM bodies only**:

| feature area | bodies present |
|---|---|
| shutter / native setting-commit (`assets\shutter\…`, manifests `r22`–`r24`) | om1-1.1, om1-1.9, om1ii-1.3, om3-1.1, om5-1.2, em1iii-1.6, em1x-2.4 |
| aperture-ring / custom-mode ("ring" validation) | same OM-1-generation set |
| menu-language / CJK-font injection | om5ii (OM-5 Mark II), E-P7 (`ep7-*.json`) |

There is **no E-M10 Mark I** profile (nor E-M10 II/III/IV, E-M5 II) anywhere — no shutter JSON, no
manifest entry, no language target, no `S0051`. This matches `STATUS.md`'s note that the only
community claim for the Mark I was "Panasonic aperture ring works" (untested by the author). So the
tool provides **no reusable patch** for our body; its value here is purely the *schema* below, as a
template for patches we would have to locate ourselves in the Mark I 1.4 BIN.

## Two patch mechanisms

### 1. Native-code patches (AM33 / MN103 family)

Per-body files `assets\shutter\native-commit-v3\<body>-<ver>.json` describe hooks into the camera's
**native menu "setting commit"** routine. Confirms these bodies run the **AM33 (Panasonic MN103)**
CPU family — same ISA as the E-M10 Mark I's block 0 (`docs/firmware/` / `rtos-tasks.md`), but a
newer SoC at a different load base (`0x60xxxxxx` here vs the Mark I's `0x40300000`/runtime
`0x7d991020`).

Schema (from `om3-1.1.json`):
- `native_binding.address` + `original_hex` + `sha256`: the exact bytes being replaced, verified
  against `source_sha256` of the whole image.
- `ABI`: `"D0=scalar key, D1=value; caller CALL [d2,d3],12; native RET [d2,d3],12"` — the AM33
  **register-list call/return** convention (`CALL (regs),imm` saves regs + reserves `imm` stack
  bytes). Identifies the calling convention of OM native setters.
- `desired_write` / `active_write`: two paired stores (a "desired" value then the "active" value),
  each with `target` address, `register_mask` (AM33 reg-list mask, e.g. `192` = `0xC0`),
  `frame_bytes`, and original bytes.
- `write_mode_getter` + `gate_requirement`: the patch **must call the native write-mode getter
  first; return value 1 = denied**, and must not run the paired desired/active setter for a denied
  request. `active_native_setter_gate_preserved: true` keeps the stock gate.
- `data` / `previous_data` / `helper_data`: base64 of the patched vs original native payload (cave
  code) and a helper thunk; `call_context: "Menu commit only, never boot/MODE load"`.
- `physical_camera_verified: false` — the author flags these as not hardware-confirmed.

This is the same *hook pattern* we found in the Mark I ring-native patch (replace stock insns in a
code cave, re-run them, jump back) — but keyed to OM-1-generation addresses, useless as-is on the
Mark I.

### 2. Resource / menu-language patches (block-1 string+font injection)

`om5ii_language_targets.json` (+ `korean_font_*.bin`, `korean_strings_*.bin`) inject extra menu
languages (jpn/kor/chs/cht) by patching **block 1** (the resource/string block — same block type we
decoded for the Mark I in `resources.md`). Each patch is `{block, offset, old, new}` where `old`/`new`
are base64 of **UTF-16LE menu strings** (e.g. "AEL/AFL", "A001A", "MF", "Home", "All Clear")
interleaved with CJK glyph data. So the CJK unlock is pure resource-table replacement, not code —
directly analogous to editing the Mark I's 34 UI string tables, if one wanted to relocalize.

## Packaging

Standard PyInstaller (`app.pyc.raw` = frozen entry, Python 3.12, PySide6 GUI, lxml/fonttools/numpy).
Manifests `r22`/`r23`/`r24-manifest.json` index each body's payload by `payload_sha256`,
`payload_len` (~1.2–1.5 KB), `native_patch_count` (~10–13), and a `descriptor_gate` flag referencing
`ring-descriptor-validation.json` / `ring-custom-mode-validation.json` (CPU/custom-mode
pre-checks run before patching). `app.pyc.raw` left un-decompiled — the JSON assets already reveal
the method, and the code is closed-source community work.

## Takeaways

- The tool confirms OM bodies through the OM-1 generation are AM33/MN103 and patched via native
  setting-commit hooks with a write-mode gate + descriptor validation — a good template for our own
  Mark I mods (`docs/mods/`, still TODO).
- It gives us **nothing directly usable** for the E-M10 Mark I: no address map, no profile. Any Mark
  I shutter/custom-mode/ring patch must be located independently in our own 1.4 BIN.
- CJK/menu relocalization is block-1 resource replacement — reachable with the Mark I resource
  tooling we already have, if ever wanted.
