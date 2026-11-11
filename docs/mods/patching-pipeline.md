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
> **Superseded 2026-11-11.** `0x7de57532` is the SD scanner *client* (FIRMUP_CLI), not FIRMUP_SRV, and
> no code that starts it at power-on has been found. SD recovery is unproven; the "low brick risk"
> conclusion below does not hold as written. See `docs/firmware/camera-fw-update.md` →
> "Update-flow trace and corrections". The owner has one camera and does not flash.

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

## Safe flashing method — rely on the camera's fail-closed pre-flash gate (2026-11-03)
The lowest-risk way to try a patched body image is to **let the camera's own validator be the gate**,
because `FIRMUP_SRV` validates before it writes and aborts on any failure (see
`docs/firmware/camera-fw-update.md` → "Pre-flash image validation"):
1. **Structural parse** (`0x7de57e24`/`0x7da8883e`): walks the image's ≤32-record region table,
   checks sizes vs file length (error `0x3321`).
2. **Image-id + usr_checksum** (`0x7de58985`/`0x7de573d1`): asserts the id byte `== 'E'` (body) and
   compares a **20-byte (5×u32) internal integrity array** (error `0x3202`), plus a header-flag gate
   (`0x3204`). Mismatch → abort, **no flash**.
3. Only on success → `TYPE_FIRMUP_WRITE_OK` → `SUCCESS_REBOOT`.

So a wrong/corrupt/incompletely-patched image is **rejected, not flashed**. That makes "attempt the
flash and observe" a safe probe: the camera does nothing destructive on a bad image.

**Where our built image stands:**
- Our `fwpatch.py` output reproduces the community tool's **declared expected output hash exactly**
  (`sha256 837ecc9e…` — it matches the profile's stated expected image), so the pipeline is faithful:
  what we build is what the mod author intended to ship.
- But the mod author's own declared verification is **structural + CPU-emulation only, not hardware**
  (`test_candidate`, real-device unverified — same caveat as `ring_summary`). Neither the author's
  tool nor our pipeline writes the camera's internal **20-byte usr_checksum array**; both produce the
  image from the payload patches alone.
- **RESOLVED (2026-11-03):** the `usr_checksum` gate is a **header↔tail duplicate-array consistency
  check**, not a payload hash (full decode in `docs/firmware/camera-fw-update.md` → "RESOLVED"). It
  compares the region header's first 20 bytes against the first 20 of the region's trailing 32-byte
  block. All 9 patches sit mid-payload (0.00–7.31 % of block 0), touching **neither** compared window,
  so the stamps are byte-identical to stock and the gate **passes** (accepting outcome). `fwpatch.py`
  does not need to recompute it. Camera acceptance of the *packaging/integrity gates* is therefore
  statically established; only the **patch's runtime behaviour on real hardware** stays unverified.

**Recommended safe procedure (if the user chooses to try it):** full battery; write only the built
`E1139999.BIN` to `DCOLYMP/`; run the update; watch for `SUCCESS_REBOOT` vs an on-screen checksum/validation
error. A validation error means the image was rejected pre-write (harmless) — not a failed flash. Do
**not** interrupt power/SD once `TYPE_FIRMUP_WRITE_OK` is reached (that is the only truly dangerous
window). Keep a known-good stock `E1139999.BIN` on hand for `FIRMUP_SRV` recovery.

> ~~Open (needs runtime image layout): the exact file offset and coverage of the 20-byte
> `usr_checksum` array.~~ **RESOLVED 2026-11-03** (see the two bullets above): it is a header↔tail
> duplicate-array check, the patches miss both windows, the gate passes, no recompute needed.

### Per-slot header gate + the single remaining reject mechanism (2026-11-03)
Disassembled the inner found-file block of `FIRMUP_SRV` (`0x7de575d6`-loop over the 9-slot component
descriptor, record stride 28, `+24` = component id):
- `0x7de576be` sets read length `32`; `0x7de576df` sets buffer `sp+196`; two reads
  (`0x7d9c1429` seek/prep, then `0x7d9c132d` read 32 B into `sp+196`), each return-checked → error
  close (`0x7dc9cdd5` / `0x7dc9ce19`, `d1=3`) on failure.
- **Validity gate `0x7de57701`:** `movhu (196,sp),d0; cmp 0,d0` — the first halfword of the component's
  32-byte header must read a known value or the slot errors; the loop then advances (`add 28,a3`,
  `0x7de57712`) and the actual flash is dispatched **after** the 9-slot loop (`0x7de57720`: if any
  slot found → `0x7dc9ccc0`, `d0=3,d1=2`).

This gate — and every structural/header/region-table gate found so far — reads **container
metadata**, and the built image's metadata is provably identical to stock: `omfw.py info` + a
block-by-block compare of the current `E1139999.BIN` shows **all three block headers byte-identical to
stock**; only block 0 differs, and only in (i) the recomputed footer and (ii) the 1202 payload bytes
inside declared patch regions (blocks 1 & 2 are byte-for-byte stock). So the camera's metadata gates
see exactly the stock bytes and pass identically.

**Net narrowing:** the *only* pre-flash check that could reject the patched image is one that
checksums the **decoded block-0 payload** (i.e. the `usr_checksum` 20-byte array, if its coverage
includes the patched region). Every other gate is satisfied by construction. That reduces the whole
"will it flash?" question to the single open item above (payload-coverage of `usr_checksum`), which is
the runtime-layout dead-end — not statically resolvable without executing the camera's image loader.

## Applying to the camera (live / hardware — user action)
1. Copy the built `E1139999.BIN` to the SD card root dir `DCOLYMP/` (so `DCOLYMP/E1139999.BIN`).
2. In the camera, the `api_firmup` updater mounts the card, scans `DCOLYMP` for `E113????.BIN`, finds
   it ("Binary file Hakken"), reads the 32-byte header, and flashes (see
   `docs/firmware/camera-fw-update.md`).
3. This is an irreversible on-camera flash. **Not performed from here** — the user runs it on the
   real body. The ring-native payload is unverified on hardware; flashing a bad body image can brick.
