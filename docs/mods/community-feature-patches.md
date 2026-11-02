# Community firmware — non-ring feature patches (RE)

Reverse-engineering of the five **non-ring** feature families the community "db firmware" tool
(`research/dbfw_extracted/`) ships. These target bodies **other than** the E-M10 Mark I (the E-M10
only gets `ring-native`, see `docs/mods/ring-cave-disassembly.md`), so they're reference/interop
analysis — not applicable to our stock block 0, and not validated against it. Raw payload bytes and
disassembly stay local (`research/decomp/`, gitignored, EULA); this file is our own spec.

Catalog (from `profiles.json` + the `assets\shutter\` asset set):

| family | bodies | mechanism | block(s) |
|---|---|---|---|
| `shutter-sound` | 6 (om1, om1ii, om3, om5, em1x, em1iii) | PCM asset inject + native menu/producer hooks | asset-set + native |
| `korean` | 5 (om1, om1ii, om3, om5, om5ii) | resource strings + TFT font inject | block 1 |
| `wifi-5ghz` | 5 (om1, om1ii, om3, om5, em1x) | native hook(s) | block 0 (+2) |
| `sh2-four-rates` | 1 (om1) | native, 67 patches | block 0 |
| `ep7-controls` | 1 (ep7) | native + resource, 1021 patches | block 0 + 1 |

All disassembly uses the locally-built `mn10300` objdump (binutils 2.43, `--target=mn10300-elf`).
OM-1-generation bodies are the same AM33/MN103 CPU family, runtime base `0x60000000`.

---

## 1. `shutter-sound` — custom shutter audio (AM33/MN103 native + PCM asset)

A feature that adds a user-selectable **custom shutter sound** played on capture. Two parts:

### Audio asset (`assets\shutter\camera-shutter.json`, `*.wav`)
A shutter WAV is baked in: source `freesound_community-camera-shutter-107889.mp3`
(sha `0f72ed32…`), trimmed 640–820 ms → **180 ms**, peak-normalised 0.75, 2 ms fade-in / 6 ms
fade-out, rendered to **48 kHz / 16-bit / stereo** PCM (output sha `b57d4e2f…`). Other banks:
`full_high.wav`, `full_low.wav`, `meow.wav`.

### Native wiring (`assets\shutter\bank-runtime.json`, `native-commit-v3\<body>.json`)
Per body (OM1 `om1-1.9.json`, source sha `342954a4…`), native code fragments are written into free
RAM/code at `0x6032xxxx` and hooked into the stock sound path. Sections (base64 code, each with its
own sha):

| section | address | size | role |
|---|---|---|---|
| `pcm_copy` | `0x6032d400` | 126 | copy PCM into the play buffer |
| `producer` | `0x6032d800` | 145 | feed samples to the play-body path |
| `worker` | `0x6032dc00` | 95 | sound-bank slot state machine |
| `menu`/`normal`/`fast` | `0x6032…` | 66–242 | menu-option + rate-path shims |

The `worker` reads a selected-slot cell (`0x6032c400`) and a descriptor table (`0x6032dc10`), keyed
by **sentinel values `0x7FFA–0x7FFE`** (32762–32766) that tag the custom bank slots, then dispatches
to the matching descriptor.

### The hook (`native_binding`, site `0x603e6c29`, 24 stock bytes)
Stock code there is a **paired getter/setter**:
```
mov d1,d3 ; mov d0,d2 ; exthu d2 ; mov d2,d0
call 0x6040f8f7,[],4     ; desired getter  (D0=key -> D0=value)
mov d3,d1 ; mov d2,d0
call 0x6040f432,[d2,d3],12  ; active setter (the stock postvalidate write)
```
The feature replaces this with its own paired commit so that selecting the custom sound in the menu
**persists like a stock setting** (desired owner tag `0x8B54` + active value), reusing the stock
"write-mode getter" (`0x6040f434`→`0x6040fea6`) as a gate — if that getter returns `1` the write is
**denied**, so the patch respects the camera's own commit lock. `call_context` is explicitly
**"Menu commit only, never boot/MODE load"** — it never runs on the boot or mode-dial path. ABI:
`D0 = scalar key, D1 = value; CALL [d2,d3],12`.

`physical_camera_verified: false` — like the ring port, structurally/CPU-verified only.

**Takeaway:** a resource(PCM)+native-hook feature that grafts a custom sound bank onto the stock
menu-commit + sound-producer machinery, gated by the stock write-mode lock. E-M10 Mk I is **not** in
the shutter-sound body set.

---

## 2. `korean` — menu language + TFT font injection (block 1 resource)

Pure **resource replacement** in block 1 (the resource/string block, same type decoded in
`docs/firmware/resources.md`). Two patches (om5ii-1.1 labels them explicitly; other bodies carry the
same two unlabeled):

| patch | block | offset | size | content |
|---|---|---|---|---|
| "jpn Korean language resource" | 1 | `0x341de0` | 203 776 B | menu string table |
| "jpn native-location TFT font" | 1 | `0x6eb3e0` | 343 552 B | TFT glyph block |

The string table is **UTF-16LE** menu tokens interleaved with Korean text — e.g. the decoded head
shows menu keys `@A025@`, `RECMFRAW`, `AEL/AFL`, `A01A` next to Korean strings like `미리보기`
("preview"). Same size old↔new, so it's an in-place table overwrite. "native-location" / "jpn"
means Korean **takes over the Japanese language slot**: the patch rewrites the JPN string + font
entries rather than adding a new language, so the camera shows Korean wherever it would show
Japanese. The font patch replaces the TFT glyph bitmap block at the JPN font location with Korean
glyphs (header `d903 6601…`). No code — analogous to editing the Mk I's own 34 UI string tables
(`resources.md`) if relocalization were wanted. Matches `assets\om5ii_language_targets.json`
(see `docs/firmware/community-dbfw-tool.md`).

## 3. `wifi-5ghz` — 5 GHz channel unlock (block 0 native + block 2 Wi-Fi firmware)

Unlocks 5 GHz Wi-Fi on bodies whose radio supports it but whose firmware caps channels to 2.4 GHz.
Two layers (om1-1.9):

### Block 0 — AM33/MN103 app patches (the channel gate)
- **patch @ `0x617f0528` (6 B):** stock compares the channel index to **13** (`… exthu d1; cmp 13,d1`
  — 13 = the top 2.4 GHz channel). The patch prepends `mov 36,d0` so the value flows in as **36** —
  channel **36 is the first 5 GHz UNII-1 channel (5180 MHz)**. This is the direct unlock.
- **patch @ `0x617f04ea` (12 B):** stock loads a const and `call`s a validator (`0x617e88a3`). The
  patch replaces it with a read of a region/mode RAM cell (`0xa33eea9c`); if that cell `== 2` it
  forces the channel param `d3 = 36`. A region-gated force of the 5 GHz channel.

### Block 2 — embedded ARM Wi-Fi-module firmware
`patch @ block2 offset 0x2f10fe0`, ~11.8 MB. Block 2 contains an **embedded ARM Linux image** for
the Wi-Fi coprocessor (`\x7fELF` magic, `/lib/ld-linux-armhf.so.3`, symbols `_ITM_registerTMCloneTable`,
`__gmon_start__`). The patch differs from stock across ~90 000 byte-runs starting at the ELF header
fields — i.e. it swaps in a **wholesale recompiled build** of the radio firmware (a 5 GHz-capable
image), not a small regulatory tweak. The block-0 patches open the UI/channel path; the block-2 blob
is the radio stack that can actually drive 5 GHz. (A full RE of the alternate ARM ELF is out of scope
— it's a different firmware image, not a diffable edit.)

**Note:** the E-M10 Mark I is **not** in the `wifi-5ghz` body set — its radio is 2.4 GHz-only
hardware, so there is nothing to unlock.

## 4. `sh2-four-rates` — OM1 SH2 / ProCap-SH2 extra frame rates (67 block-0 patches)

Adds four high-speed rates — **12.5 · 16.7 · 25 · 50 fps** — to the OM-1's SH2 / ProCapture-SH2
burst modes. `implementation: SH2-R9-OM1II-donor-native-SH1-paths` = the OM-1 **Mark II's** SH2 code
is the donor, grafted onto the OM-1's SH1 paths. Partly **hardware-verified** (`physical_sh2_12_5:
true`), unlike ring/shutter. The detail note adds that on lenses that don't support 50 fps the menu
restriction is relaxed so 12.5/16.7 stay selectable.

67 patches in block 0, three kinds:

**(a) 242 B payload cave** (`sh2_r9_payload` @ `0x602d4560`) — a rate-code translator/validator:
```
exthu d0
cmp 125,d0 ; beq -> mov 12,d0 ; retf   ; rate code 125 (12.5 fps x10) -> engine slot 12
cmp 167,d0 ; beq -> mov 16,d0 ; retf   ; 167 (16.7 fps x10)          -> slot 16
cmp 1200,d0 ; jmp 0x603ba411            ; else back to integer_guard
... movhu (-558,a0),d0 ; cmp 125/167 ... ; mov (a3),d0 ; divu 3,d0  ; cadence = rate/3
```
It maps the new fractional rate codes (125 = 12.5, 167 = 16.7, and the 25/50 integer rates) onto the
engine's internal rate slots and computes the sensor cadence (`divu 3`).

**(b) 7 guard hooks** (`DC`+rel32 `jmp` into the payload): `sh2_r9_integer_guard` (`0x603ba40c`),
`cadence_guard` (`0x603ad311`), `selector_guard` (`0x603b8399`), `budget_guard` (`0x60918b00`),
`limit_a` (`0x60919707`), `limit_b` (`0x60919764`), `format_guard` (`0x6091be40`) — they intercept
the rate-selector, cadence, exposure-budget, rate-limit and readout-format checks so the engine
accepts the new rates. `sh2_r9_loader_end` (`0x60024e18`, `fccc00582f60`) is a loader marker.

**(c) 58 scattered small edits** (1–11 B each, `0x605bf9e4 … 0x6151381c`) — the **rate-table + flag
data**: e.g. at `0x605bf9e4` stock table bytes become `7d`/`a7` (= 125 / 167, the new rate codes)
and count/limit cells are bumped (`0x605c18ac`: `0c`→`14`, 12→20). These write the new rates into the
tables the guards/payload then validate.

## 5. `ep7-controls` — E-P7 button / exposure / menu remap (1021 patches)

The largest feature, E-P7 only. `title` "E-P7 버튼·노출·메뉴 기능", `status`
"버튼 리맵 · AF 홈 이동 · M/Auto ISO 노출보정" = **button remap · AF-home move · M/Auto-ISO exposure
compensation**; the D-pad can be set to ISO/WB/AF-position/Drive as a group or assigned per direction
(`implementation: ep7-native-controls-2026-10-18`, `hardware_verified: false`).

Despite 1021 patches it is overwhelmingly **table-driven config**, not code — only **9 code hooks**
(`DC`+rel32) in the whole feature:

| | count | hooks | shape |
|---|---|---|---|
| block 0 (app) | 640 | 7 | 301 × 1-byte + many 2–8-byte edits, over `0x5e0d0…0x11bcb1c` |
| block 1 (resource) | 381 | 2 | 326 × 1-byte + menu strings |

- **block 0** = the control-assignment tables: hundreds of single-byte flag flips (which button maps
  to which function, per-D-pad-direction assignments, M/Auto-ISO exposure-comp enable bits) plus a
  few multi-byte descriptor records (the "largest" patch @ `0x4aaf0c`, 99 B, is a table of 4-byte
  control-descriptor entries, not executable code), and 7 native hooks that implement the new
  behaviors (AF-home move, exposure comp in M mode, per-direction dispatch).
- **block 1** = resource edits: 326 single-byte table flips to expose the new menu entries, plus the
  new UTF-16LE menu labels — e.g. `기능 할당` ("function assignment") — and 2 resource hooks.

So the mechanism is: unlock/retarget a large set of existing control-table slots by flipping their
flags, add the menu entries that surface them, and bolt on a little native glue for the behaviors
the stock tables can't express. Full byte-level enumeration of 1021 config entries is not
meaningful (it's data, not logic) and is out of scope; the structure above is the RE result.

---

## Summary across the five families

| family | kind | code hooks | key mechanism |
|---|---|---|---|
| shutter-sound | asset + native | ~6 sections | PCM bank + menu-commit paired write |
| korean | resource | 0 | JPN string+font slot overwrite (UTF-16LE + glyphs) |
| wifi-5ghz | native + blob | 2 | channel limit 13→36 + swap ARM Wi-Fi ELF |
| sh2-four-rates | native + table | 7 + payload | rate-code translator + rate-table edits (12.5/16.7/25/50) |
| ep7-controls | table + native | 9 | mass control/menu flag edits + glue |

Two reusable patterns for our own model-agnostic patcher (`docs/mods/firmware-modding.md`):
**(1) native detour → cave** (ring, shutter, wifi, sh2, ep7 glue — same `DC`+rel32 technique we
verified on the E-M10), and **(2) data-table/resource edits** (korean, sh2 rate table, ep7 configs —
in-place same-length overwrites of tables in block 0/1/2, no code). The E-M10 Mark I is in **none**
of these five body sets; only `ring-native` targets it.

