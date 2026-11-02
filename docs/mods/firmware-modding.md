# Firmware modding: container crypto, repack, and the community tool

## Community tool (`dbfw_0.3.1.b`) — what it actually is

PyInstaller EXE (`research/dbfw_0.3.1.b/db.firmware.0.3.1.b.exe`), unpacked to
`research/dbfw_extracted/`, Python modules disassembled to `research/dbfw_extracted/py/*.dis.txt`
and `*.strings.txt`. It is a **downloader + guarded patcher + repacker**, not a camera dumper:

- `omds_catalog` — resolves the exact stock firmware URL from the public OMDS catalog
  (`text/xml` catalog query).
- `engine` — "Version-bound, guarded firmware patch assembly and OFU firmware downloader."
  Downloads via a provider at `https://ofu.infinityfreeapp.com/` (`api.php?dlinfo=`), solves a
  `toNumbers("…32 hex…")` JS security challenge (CloudFlare-style), checks the download against a
  registered `source_firmware_sha256`, applies selected feature patches, verifies a rebuild hash,
  writes the output `.bin`. The user then flashes it with the **official OM updater (OFU)**.
- `release_policy` — gates which feature profiles are offered per body/version.
- `vendor.container_codec` — the encrypt/decrypt/checksum (below).

Feature patches it carries (UI strings, Korean): aperture-ring native preview (`ring-native`),
shutter sound, font config, Korean localization/translation-override, plus guards
`EXPERIMENTAL_NOT_FLASH_READY` / `EXPERIMENTAL_HARDWARE_UNTESTED`.

> **Correction (2026-11-02):** the full catalog is `profiles.json` (23 bodies) + `compatibility.json`,
> and it **does** include `em10-1.4` — a `ring-native` TEST_CANDIDATE (structural/CPU-verified, not
> hardware-verified) targeting our exact BIN. Its 9 hook offsets match our RE byte-for-byte; see the
> detailed writeup in `docs/firmware/community-dbfw-tool.md`. The container codec is the same across
> the whole Olympus/OM family. Patch mechanics match our `docs/STATUS.md` hook table: `payload_cave`,
> `runtime_base`, jump-hook destinations bounded against the code range.

It has **no memory-read / dump capability**. The tool only pushes firmware to the camera.

## Container crypto (confirmed, implemented in `tools/omfw.py`)

File = sequence of blocks. Each block = **32B header + data + 32B footer**.

- Header: `'OE'`, model id, `@8 load u32`, `@12 dlen u32`, `@16 ver u32`, `@20 u2 u32`, rest 0.
- Data transform, per 16-byte chunk: `encrypted = permute(plain XOR 0xFF)`.
  - `P = [1,3,0,2,6,4,7,5,11,10,9,8,13,14,12,15]`
  - decrypt: `plain[j] = enc[P[j]] XOR 0xFF`
  - encrypt: `enc[P[j]] = plain[j] XOR 0xFF`
- Footer: `header[:28]` echo + `u32 V` at `[28:32]`, where
  `V + sum32LE(plain) + 2*sum32LE(header[:28]) == 0 (mod 2^32)`.

Our E-M10 1.4 `OLY_E_113_1400_0000_0000.BIN`, 3 blocks:

| blk | load | dlen | ver | u2 | footer_ok |
|---|---|---|---|---|---|
| 0 | 0x40300000 | 0x11fffc0 | 0x1400 | 0x100 | yes |
| 1 | 0x41500000 | 0x17fffc0 | 0 | 0x101 | yes |
| 2 | 0x42d00000 | 0x18fffc0 | 0x100 | 0x106 | yes |

**Repack verified (2026-11-01):** `enc(dec(data)) == data` for all three blocks, and
`footer_v(hdr, plain)` reproduces the stored footer checksum exactly. So a patched block can be
re-encrypted into a container the camera's updater accepts. `tools/omfw.py {info|dec} <bin> [out]`.
(`enc` / `footer_v` are module functions; a one-shot `build` subcommand is still TODO.)

## Implication for extracting the ROM pictures

The update/flash path is write-only; neither the stock firmware (no USB memory-read op found, see
`debug-shell.md`) nor the community tool reads camera memory. The remaining in-software route to
get the type-3 ROM pictures at flash 0x46560000 is a **custom firmware patch**: hook a code path
(payload-cave technique from `STATUS.md`) with a routine that calls the existing
`file memdump`/flash-read internals to copy 0x46560000..0x47360000 to the SD card, then flash that
patched firmware. This is the invasive option (a bad flash can brick the body) and the E-M10 is
not a vetted profile in the community tool, so the patch and its hook offsets would be ours to get
right. Not to be attempted without explicit user go-ahead and a recovery plan.

Lower-risk alternative still open: trace the `TSK_PTPCOM` receive loop for a vendor opcode that
reads memory (may not exist), or find UART test pads.

## Design principle: model-agnostic patcher (build for reuse)

**Requirement:** our patching method and tooling must be body-model-agnostic. Others will reuse this
repo for their own Olympus/OM bodies, so the patch *engine* must stay generic and everything
body-specific must live in **data profiles**, never hard-coded in the engine.

This is exactly the shape the community tool already uses (`profiles.json` = per-body data, one
engine) and what our `tools/omfw.py` container codec already is (one codec, works across the whole
OM family). Extend the same discipline to the patcher:

- **Generic engine** (model-independent): container decode/encode + footer checksum (`omfw.py`);
  MN103 hook injection (write a `DC`+rel32 jump at a site, relocate the displaced stock instructions
  into a code cave, append the feature routine, jump back); `0xFF`-cave allocator; bounds-check every
  jump target against the code range; rebuild + verify hash.
- **Per-model profile** (all the variable facts, in a JSON/TOML data file — one per body+version):
  - identity: `model_id`, `ofu_id`, `source_sha256`, block table (`load`/`dlen`/`ver`), `runtime_base`;
  - flash metadata: `flash_dir` / `flash_path` / `cardfile` (e.g. E-M10 = `DCOLYMP/E1139999.BIN`);
  - per-feature: hook **sites** (block0 offsets + the stock `old` bytes to assert before patching),
    `payload_cave` region (offset+length of verified free `0xFF` space), and any
    `descriptor_gate` (pointer cell, flags offset, flag mask, identity pair) the feature reads;
  - a verification manifest (expected post-patch hash, CPU/structural checks).
- **Never in the engine:** absolute addresses, cave locations, gate cells, or body names. The engine
  takes `(stock_bin, profile, selected_features)` and emits a flashable `.bin`.
- **Safety stays generic too:** assert every `old` anchor matches the loaded image before writing
  (as `tools/dbfw_verify_patch.py` does); refuse if any site or the cave doesn't match; never touch
  block 0's loader region. A profile for an unverified body is `TEST_CANDIDATE` until a real-device
  check — surface that state, don't hide it.

The E-M10 Mark I 1.4 profile is just the first instance; adding a new body = writing a new profile
(found via the same RE workflow: decode container → load block 0 at `runtime_base` in Ghidra → find
the feature's code path → pick sites + a cave → fill the profile), with zero engine changes.
