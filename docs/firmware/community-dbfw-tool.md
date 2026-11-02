# Community "db firmware" tool — architecture, patch schema, E-M10 ring port

Static analysis of the community firmware-mod app "db firmware" (azqeurio/om-c-firmware, release
`dbv0.3.1.b`, PyInstaller build, unpacked to `research/dbfw_extracted/`). **Never executed**
(untrusted Windows binary); only its bundled JSON/asset data was read with `python3 -I`
(`tools/dbfw_extract_em10.py`). Purpose: understand how the community patches OM firmware, and what —
if anything — applies to the E-M10 Mark I.

> Correction to an earlier draft of this doc: the real patch catalog is the **top-level**
> `profiles.json` (GUI catalog, 23 bodies) and `compatibility.json` (analysis records), **not** the
> `assets\shutter\` subfolder (which only holds a 6-body subset). The E-M10 **is** covered. See
> below.

## Body coverage (profiles.json — 23 bodies)

`om1-1.9, om1ii-1.3, om3-1.1, om5-1.2, om5ii-1.1, em1x-2.4, em1iii-1.6, em5iii-1.7, em10iv-1.1,
ep7-1.1, epl9-1.1, epl5-1.6, ep5-1.8, em1-4.6, epl6-1.4, em10-1.4, epl7-1.4, em5ii-4.1, em10ii-1.4,
penf-3.1, epl8-1.1, em1ii-3.7, em10iii-1.2`.

The headline feature across bodies is **`ring-native`** = "Panasonic 조리개링 지원 (A/M 모드)" =
*Panasonic aperture-ring support in A/M modes* (use a Panasonic/Lumix lens's physical aperture ring
to set aperture on these Olympus bodies). The OM-1-generation profiles are the mature ones; the
Reddit report of "om1 patches work fine" refers to those (hardware-verified elsewhere).

## E-M10 Mark I 1.4 ring-native port — TEST_CANDIDATE, not hardware-verified

`profiles.json` entry `em10-1.4` **does** ship a `ring-native` patch, `available: true`, but its
`ring_summary` is explicit: **"조리개링 TEST_CANDIDATE (구조·CPU 검증, 실기기 미검증)"** =
*aperture-ring TEST_CANDIDATE: structural + CPU-emulation verified, **real-device UNverified***.
`compatibility.json`'s matching analysis record (`targets[].id == em10-1.4`) earlier marked it
`PORT_REQUIRES_MODEL_SPECIFIC_IMPLEMENTATION` / `available_in_app: false` and recorded that a direct
transplant of the OM-1 R22 patch **failed** — all 15 OM-1 byte "needles" and 5 RAM literals scored
**zero hits** in the E-M10 block 0 (observation: *"could not find the same instruction sequences as
the 8 OM-1 hooks; this is not a verdict that the feature is impossible — the equivalent body-input /
protocol / loader path must be found separately"*). Between that failed analysis and the `dbv0.3.1.b`
release they built a **model-specific** E-M10 implementation
(`impl: ring-rom-capability-cache-gate-ring-port-all-113-resident-candidate-native-polls-69-81-84`),
which is the TEST_CANDIDATE shipped. **No one has confirmed it on a physical E-M10 Mark I.**

So: the repo's E-M10 ring feature exists and is selectable, but is unverified on hardware. Treat as
experimental.

### It targets exactly our firmware — and matches our own RE

Cross-validation against our files (strong confidence boost):

| field | db-firmware value | our value | match |
|---|---|---|---|
| `source_sha256` | `84d81b2d…c4e3590c` | `firmware/stock/OLY_E_113_1400_0000_0000.BIN` | ✅ identical |
| `block0_sha256` | `e2b22766…00c54f0e` | `firmware/stock/dec/blk00_40300000.bin` | ✅ identical |
| `runtime_base` | `2107183136` = `0x7D991020` | our Ghidra block-0 runtime base | ✅ identical |
| block checksums | block0 18874304 / block1 25165760 / block2 26214336 (all PASS) | our block sizes | ✅ |

Their block-0 decode matching ours byte-for-byte independently validates our container codec
(`tools/omfw.py`) and load-base choice.

The nine `em10-1.4` ring patches (block 0) land at **exactly** the hook sites we independently
reverse-engineered last session (then described as a "patched scratch copy" — it was in fact this
candidate):

| patch label | block0 offset | runtime addr | our prior note |
|---|---|---|---|
| `loader_patch` | `0x1ab` | `0x403001ab` | old == new (no-op) ✓ |
| `payload_cave` | `0x26ff0` | `0x40326ff0` | parser payload cave ✓ |
| `reset_hook` | `0x11289b` | `0x4041289b` | reset hook ✓ |
| `init_hook` | `0x114daf` | `0x40414daf` | init hook ✓ |
| `parser_hook` | `0x11b411` | `0x4041b411` | parser hook ✓ |
| `request_hook` | `0x12a1ac` | `0x4042a1ac` | request hook ✓ |
| `callback_hook` | `0x12a4a2` | `0x4042a4a2` | callback hook ✓ |
| `guard_hook` | `0x12a71b` | `0x4042a71b` | guard hook ✓ |
| `input_hook` | `0x150b06` | `0x40450b06` | input hook ✓ |

Each `*_hook` patch replaces a `jmp`-worth of stock bytes with a jump into the `payload_cave`
(`0x40326ff0`+), exactly as our hook-site analysis described. Only **block 0** (app code) is touched;
the bootloader/loader is not (the `loader_patch` is a no-op in this profile) — consistent with the
Reddit note that reflashing stock firmware is safe "as long as you don't mess with the bootloader."

### E-M10 ring gate mechanism (`descriptor_gate`)

`descriptor_gate`: `{pointer_cell: 0xa0a5c970, flags_offset: 560, flag_mask: 128}`. The patch follows
the RAM pointer at `0xa0a5c970` to the live lens-descriptor, checks `flags[+560] & 0x80` (ring-capable
bit), and only then consumes the lens's ring aperture value in A/M modes; otherwise it keeps the body
aperture setting. (OM-1's gate is `pointer_cell 0xa32caa8c, flags_offset 1096, identity_offset 1100,
identity_pair 0x6296cd2e, flag_mask 128` — same shape, different model-specific cell/offsets, which is
why the direct port failed.) `impl` "native-polls-69-81-84" = it hooks lens-comm response messages
69/81/84.

### Research leads for our own `docs/mods/` work

The `compatibility.json` `em10-1.4.sites` (15) name the subsystems a ring patch must reach — a map
for finding the equivalent E-M10 code ourselves: `request_hook, parser_hook, identity_hook,
response69/75/84/90_hook, selected_av_input_hook, iris_abs_hook, loader_end, PARAM_GET,
ACTIVE_EXPOSE_MODE, READ_LE16, LENS_METADATA, FAILURE_ERROR`. RAM literals of interest (OM-1 values,
to find E-M10 equivalents): `cache_prefix, lens_id_pair 0x6296cd2e, identity_status 0x6296cd2c,
readiness, iris_snapshot 0x62abc432`. Six `unresolved` items: A/M mode determination; lens-ID /
ready-state + cache-RAM ownership; selected-aperture getter + final AE consumption; code-cave
boot-load range; response buffer/stack/register contract; real-device boot/receive/preview/shoot.
The `READ_LE16` window sits at block-0 offset `0xf8408` (runtime `0x403f8408`) — the 16-bit-read
helper our parser-cave payload `call`s.

## Flashing metadata (for the KMP updater, `app/`)

From the `em10-1.4` profile — confirms our planned SD-card update path:

| field | value |
|---|---|
| `model_id` | `113` |
| `ofu_id` | `E11314` |
| `dlfile` (server/download name) | `OLY_E_113_1400_0000_0000.BIN` |
| `cardfile` | `E1139999.BIN` |
| `flash_dir` | `DCOLYMP` |
| `flash_path` | `DCOLYMP/E1139999.BIN` |
| `size` | `70254592` |

So a KMP updater writes the image to the SD card as `DCOLYMP/E1139999.BIN` and the camera flashes it
on boot/menu — matching `STATUS.md`'s hypothesised path, now corroborated by an independent source.

## The other mechanism — resource / language patches

Separately, `om5ii_language_targets.json` (+ `korean_font_*.bin`, `korean_strings_*.bin`) inject menu
languages (jpn/kor/chs/cht) by patching **block 1** (resource/string block — same block type we
decoded in `resources.md`): each patch is `{block, offset, old, new}` of base64 **UTF-16LE** menu
strings interleaved with CJK glyph data. Pure resource-table replacement, no code — analogous to
editing the Mark I's 34 UI string tables if relocalization were ever wanted.

## Packaging

Standard PyInstaller (`app.pyc.raw` = frozen entry, Python 3.12, PySide6 GUI, lxml/fonttools/numpy).
Manifests `r22`/`r23`/`r24-manifest.json` index payloads by sha256/len/`native_patch_count`.
`app.pyc.raw` left un-decompiled — the JSON catalog already reveals the method, and the code is
closed-source community work.

## Takeaways

- The repo **does** carry an E-M10 Mark I 1.4 Panasonic-aperture-ring patch, but only as a
  **TEST_CANDIDATE** (structural/CPU-emulation verified, **not** hardware-verified). "Works fine" in
  the Reddit thread refers to OM-1, not the E-M10 port.
- Independent hash + `runtime_base` + hook-site matches **confirm our firmware decode and hook-site
  RE were correct** — the scratch BIN we analyzed last session was this candidate.
- It gives us a concrete E-M10 ring implementation to study (gate cell `0xa0a5c970`, flags+560 &
  0x80; hooks at the 9 offsets above; lens-comm responses 69/81/84) plus a research map
  (`sites`/`unresolved`) for `docs/mods/`.
- Flashing metadata (`DCOLYMP/E1139999.BIN`, `model_id 113`, `ofu_id E11314`) feeds the KMP updater.
