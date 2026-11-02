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

## Status — BUILT + VERIFIED (local)
`fwpatch.py build` produced `firmware/community/em10-1.4-ring/E1139999.BIN` (gitignored):
- `source sha256 MATCH`, all 9 patches `old_matches=True`, 9 applied.
- Output 70254592 bytes (same as stock — all patches in-place), sha `837ecc9e…`.

Independent verification (`omfw.py info` + decoded-block diff vs stock):
- all 3 block footers `footer_ok=True`;
- blocks 1 & 2 byte-identical to stock; only block 0 changed;
- the block-0 diff is **1202 bytes, every one inside a declared patch region, 0 bytes outside** —
  no collateral damage from re-encode/reseal;
- 8 of 9 regions actually change bytes; `loader_patch` @427 is a no-op (its `new` already equals the
  stock bytes there).

So "firmware 1.4 + patch" is **created and validated locally**. Remaining = the on-camera flash,
which is the user's hardware action (below).

### Header-gate check (brick-risk reduction)
All three container block headers in the built `E1139999.BIN` are **byte-identical to stock** (the
camera already accepts stock 1.4's headers, and `rebuild` preserves headers — only block-0 data +
footer change). File diffs vs stock are confined to `0x27010`–`0x11fffff` (block-0 encoded data +
recomputed footer); blocks 1 & 2 are untouched. So the camera's post-mount header/validity gate sees
exactly what it accepts for stock. The only part that cannot be cleared statically is the **patch
payload's runtime behaviour on the real body** — the author's TEST_CANDIDATE caveat stands.

### Recovery path survives a bad payload (why brick risk is low) (2026-11-02)
The SD-card updater (`DCOLYMP/E113????.BIN` scanner) is RTOS task **`FIRMUP_SRV`** (id 0x14, entry
`0x7de57532`, priority 8) — confirmed by cross-joining the id→name table (`0x4035fb66`) with the
task-creation table (`0x7d9a9384`); see `docs/firmware/rtos-tasks.md`. It is a standalone task spawned
at kernel init alongside 133 others, **not** code buried behind the rec/menu app. So:
- A payload that only misbehaves in the lens / aperture-ring / rec subsystem leaves `FIRMUP_SRV`
  running → the camera still scans SD on power-up-with-button-held and can reflash stock 1.4 to
  recover. This is the common failure mode for the `ring-native` patch (it hooks the lens/aperture
  path; its cave is at block-0 `0x27010`+, far from cold-boot entry at offset 0, which is unpatched).
- True brick requires the payload to take down the **kernel/scheduler**, the **SD/media stack**, or to
  corrupt **cold-boot bring-up** (block-0 offset 0, the reset entry at `0x7d991020`) so the task
  table at `0x7d9a9384` is never walked. The ring-native patches touch none of these regions.
- There is **no separate bootloader partition** observed: block 0 is both the cold-boot reset stub and
  the main OS, and the recovery updater is an OS task — so recovery depends on block 0 reaching task
  spawn. Packaging integrity (valid headers/footers, unchanged reset entry) is what protects that, and
  all of it checks out for the built image.

Net: with packaging verified and the patch confined to the lens subsystem, a bad flash most likely
yields a malfunctioning-but-recoverable camera (reflash stock), not a dead one. Residual risk is the
unverified runtime behaviour on real hardware — if the payload corrupts boot or the scheduler, the
SD recovery task never starts and recovery is lost.

## Applying to the camera (live / hardware — user action)
1. Copy the built `E1139999.BIN` to the SD card root dir `DCOLYMP/` (so `DCOLYMP/E1139999.BIN`).
2. In the camera, the `api_firmup` updater mounts the card, scans `DCOLYMP` for `E113????.BIN`, finds
   it ("Binary file Hakken"), reads the 32-byte header, and flashes (see
   `docs/firmware/camera-fw-update.md`).
3. This is an irreversible on-camera flash. **Not performed from here** — the user runs it on the
   real body. The ring-native payload is unverified on hardware; flashing a bad body image can brick.
