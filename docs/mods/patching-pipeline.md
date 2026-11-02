# Firmware patching pipeline (2026-11-02)

End-to-end path to build "firmware 1.4 + a patch" for the E-M10 Mark I and stage it for the camera's
SD updater. Stock body firmware is already **v1.4** (`OLY_E_113_1400_0000_0000.BIN`), so a mod is an
in-place edit of a decoded block, re-sealed into a valid container.

## Tools
- `tools/omfw.py` — container codec. `dec` (decode blocks), `rebuild` (re-encode + reseal footers).
  Round-trip is byte-exact (see `docs/firmware/container-format.md`).
- `tools/fwpatch.py` — **model-agnostic** patch engine. Generic only: all body-specific facts (source
  hash, offsets, bytes, SD filename) come from an external *profile* JSON. Commands:
  - `plan  STOCK.BIN PROFILE.json --id ID` — verify `source_sha256`, check each patch's `old` bytes
    match the current image, list patches, write nothing.
  - `build STOCK.BIN PROFILE.json OUT.BIN --id ID [--features a,b] [--force]` — apply, reseal, verify
    every footer re-parses, write `OUT.BIN`.
  - Safety: refuses if the stock sha ≠ profile `source_sha256`, if any `old` mismatches, or if a
    patch changes a block's length (patches are strictly in-place). `--force` overrides.

## Profile (data, kept local)
The community tool's `profiles.json` (23 bodies) carries the E-M10 Mk I entry `id=em10-1.4`:
`source_sha256` = stock sha `84d81b2d…`, `size` 70254592, `cardfile` `E1139999.BIN`,
`flash_path` `DCOLYMP/E1139999.BIN`, `model_id` 113, feature `ring-native` = 9 block-0 patches
(loader_patch @427, payload_cave @159728 (2201 B), reset/init/parser/request/callback/guard/input
hooks). Author marks it **TEST_CANDIDATE: structure & CPU verified, real-device UNVERIFIED**.

Per EULA, the community profile and its patch bytes, and any firmware image built from them, are
**not committed** (gitignored under `research/` and `firmware/community/`). `fwpatch.py`/`omfw.py`
are our own clean-room tools and are committed; they take the profile path as an argument.

## Status
`fwpatch.py plan` against the local profile: `source sha256 MATCH`, all 9 patches `old_matches=True`.
So the patch set applies cleanly to our stock image. Building the output `E1139999.BIN` (local only)
is the next step.

## Applying to the camera (live / hardware — user action)
1. Copy the built `E1139999.BIN` to the SD card root dir `DCOLYMP/` (so `DCOLYMP/E1139999.BIN`).
2. In the camera, the `api_firmup` updater mounts the card, scans `DCOLYMP` for `E113????.BIN`, finds
   it ("Binary file Hakken"), reads the 32-byte header, and flashes (see
   `docs/firmware/camera-fw-update.md`).
3. This is an irreversible on-camera flash. **Not performed from here** — the user runs it on the
   real body. The ring-native payload is unverified on hardware; flashing a bad body image can brick.
