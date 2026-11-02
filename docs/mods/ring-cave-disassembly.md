# E-M10 Mark I ring-native payload cave — recovered logic

Disassembly + behavioural analysis of the community `em10-1.4` `ring-native` **TEST_CANDIDATE**
payload cave (Panasonic aperture-ring A/M support). This is our own spec of what the candidate
*does*; the raw disassembly and the payload bytes are a decompile of community code and stay local
(`research/decomp/em10_ring_cave.*`, gitignored, per EULA).

## How this was produced

- Payload = `payload_cave` patch `new` bytes from `research/dbfw_extracted/profiles.json`
  (`features[0]` of `em10-1.4`), base64-decoded: **2201 bytes**, written at block-0 offset
  `0x26ff0` → runtime `0x40326ff0`. sha256 `2078eb4c…bd75e52d` matches the profile's declared
  `payload_sha256`. Last 2 bytes are `0xFF` fill (2199 real).
- Disassembled with a **real `mn10300` objdump** (GNU binutils 2.43 built locally with
  `--target=mn10300-elf`, at `~/dev/binutils-2.43/binutils/objdump`). Ghidra's MN103 extension
  disassembles it too but headless hung on this input (see dead-ends below); binutils is the
  authoritative cross-check.
- Command: `objdump -D -b binary -m mn10300 --adjust-vma=0x40326ff0 <cave.bin>`.
- **Validation** (before trusting any decode): known facts reproduced exactly — `0xDC`+rel32 =
  `jmp`, `0xCB` = `nop`, `0xFF` = `break` (padding); `call 0x403f8408` = the documented `READ_LE16`
  helper; `mov (0xa0a5c970),a0` = the documented `descriptor_gate` pointer cell. All consistent.

## Hook → cave-entry map

Each `*_hook` site in block 0 is overwritten with `DC <rel32> [CB…]` (`jmp` into the cave + `nop`
pad). Decoded destinations (from the patch bytes, confirmed against the disassembly):

| hook | site (runtime) | cave entry | return `jmp` |
|---|---|---|---|
| `parser_hook` | `0x4041b411` | `0x40326ff0` | `0x4041b417` (site+6) |
| `input_hook` | `0x40450b06` | `0x40327048` | via `0x40327810` → `0x40450b0d` |
| `callback_hook` | `0x4042a4a2` | `0x40327178` | `0x4042a4a7` (site+5) |
| `reset_hook` | `0x4041289b` | `0x403271f4` | `0x404128a3` (site+8) |
| `init_hook` | `0x40414daf` | `0x40327208` | `0x40414db7` (site+8) |
| `request_hook` | `0x4042a1ac` | `0x403272e0` | `0x4042a1b6` (site+10) |
| `guard_hook` | `0x4042a71b` | `0x403273e0` | `0x4042a722` (site+7) |
| `loader_patch` | `0x403001ab` | — | no-op (`old == new`) |

Each thunk saves the caller registers (D0–D3, A0–A3) to a fresh stack frame, does its work, restores
them, then `jmp`s back to the displaced instruction + continue address — a standard detour.

## Patch-private RAM scratch (new state cells)

The payload allocates two of its own RAM cells for cross-call state:

| cell | role |
|---|---|
| `0xbd9b8810` | **cached ring value** (u16) — the captured lens aperture-ring field (the "iris snapshot") |
| `0xbd9b8814` | **ready flag** — set `1` when a ring value is captured, cleared `0` on reset/init |

These are *not* stock cells; they are the candidate's own scratch in the `0xbd9b8xxx` RAM window.

## Stock cells / helpers it touches

| address | meaning |
|---|---|
| `0xa0a5c970` | stock **lens-descriptor pointer** cell (the `descriptor_gate` pointer_cell); read 5× |
| `0xa0a5c6ec`, `0xa0a5c974` | neighbour cells in the same descriptor struct (loaded by reset/init) |
| `0x403f8408` | `READ_LE16` — reads a little-endian u16 from a pointer (documented parser helper) |
| `0x403426a4` | stock helper called from `input_hook` (regs `[d2,d3]`, frame 12) |
| `0x4041b35d`, `0x404d71a0`, `0x40451a89` | other stock routines called by cave subroutines |

## Per-hook behaviour

### `parser_hook` → `0x40326ff0` (the ring-value capture)
```
btst 1,d3            ; test descriptor bit 1
bne  take            ; set → capture
bra  skip
take: mov a3,a0      ; a0 = parse cursor
      call 0x403f8408 ; READ_LE16(a0)  -> d0 = u16 ring field
      mov d0,(40,sp)
      movhu d0,(0xbd9b8810)  ; cache ring value
      mov 1,d0
      mov  d0,(0xbd9b8814)   ; ready flag = 1
      mov (36,sp),a3 ; a3 += 2  (consumed a 16-bit field)
      add 2,a3 ...
```
When a specific bit of the lens descriptor is set, it reads the 16-bit ring-aperture field out of
the descriptor stream, caches it in `0xbd9b8810`, raises the ready flag, and advances the parse
cursor by 2. This is where the ring value enters the firmware.

### `request_hook` → `0x403272e0` (descriptor-pointer validation / gate)
```
mov (0xa0a5c970),a0  ; load lens-descriptor pointer
cmp 0,a0 ; beq bail   ; null -> keep body aperture
mov a0,d0 ; and 3,d0 ; bne bail  ; misaligned pointer -> bail
... (then follows flags[+560] & 0x80 ring-capable test, per descriptor_gate)
```
Validates the descriptor pointer (non-null, aligned) before the ring value is allowed to drive AE —
the safety gate. Consistent with the profile `descriptor_gate {pointer_cell 0xa0a5c970,
flags_offset 560, flag_mask 128}`.

### `callback_hook` → `0x40327178`
Small pass-through: zero-extends a 16-bit response value (`exthu`) and returns. Part of the
lens-comm response path (`native-polls-69-81-84`).

### `input_hook` → `0x40327048`
Calls stock helper `0x403426a4`, then jumps to a larger cave subroutine at `0x40327810` that
compares a mode/state value (`cmp 1,d0`) — the A/M-mode decision path that decides whether to
substitute the cached ring value for the body aperture.

### `guard_hook` → `0x403273e0`
Branch guard on saved A1 bit0 and saved D0 == 0 — refuses to act in the wrong state/sequence.

### `reset_hook` → `0x403271f4` and `init_hook` → `0x40327208`
Both clear the ready flag `0xbd9b8814 = 0` at reset / init so a stale ring value is never reused
across a lens detach or power/mode cycle, then load a descriptor-struct neighbour cell
(`0xa0a5c6ec` / `0xa0a5c974`) and return.

## Summary of the mechanism

1. `reset`/`init` clear the ready flag.
2. `parser_hook` captures the lens's ring-aperture u16 from the descriptor stream into
   `0xbd9b8810` and sets the ready flag — only when the descriptor bit is set.
3. `request_hook` + the `descriptor_gate` (`flags[+560] & 0x80`) validate the lens is ring-capable
   and the pointer is sane.
4. `input_hook`/`guard_hook` decide, in A/M modes and the right state, to feed the cached ring value
   into the AE path instead of the body aperture setting; `callback_hook` shuttles the 16-bit
   response.

This matches the profile's `impl` string
(`ring-rom-capability-cache-gate-ring-port-all-113-resident-candidate-native-polls-69-81-84`): a
**capability-cache + descriptor-gate** design. It is still `test_candidate: true`
(`hardware_boot: false`, `physical_camera_verified: false`) — structurally and CPU-emulation
verified only, **never run on a physical E-M10 Mark I**.

## Relevance to our own model-agnostic patcher

- The two scratch cells + ready-flag pattern is the reusable shape: capture → gate → consume, with
  explicit reset so stale state never drives exposure.
- For *our* re-derivation we would re-assemble equivalent thunks in the mn10300 toolchain (now
  available locally) rather than ship their bytes, and verify in Ghidra + emulation. See
  `docs/mods/firmware-modding.md` (model-agnostic design) and `docs/firmware/community-dbfw-tool.md`.
- Tool now available: `~/dev/binutils-2.43/binutils/{objdump,as,...}` with `mn10300` support — our
  assembler/disassembler for any future mod work, no cross-package needed.

## Dead ends logged (document-everything)

- **Ghidra headless hung** disassembling this 2 KB blob (`analyzeHeadless … -processor
  mn10300:LE:32:default -loader BinaryLoader`): ran >13 min with no output and was killed. The
  `mn103.sla` was already compiled (so not first-run sleigh cost); cause unresolved. binutils
  `objdump` disassembles the same bytes in <1 s — use it for small blobs.
- **No prebuilt mn10300 objdump**: Ubuntu `binutils` and `binutils-multiarch` both omit the
  (obsolete-marked) mn10300 target; `apt` gives nothing. Must build from source
  (`./configure --target=mn10300-elf --disable-gdb --disable-nls`).
- **`reference/om-c-firmware-dbv0.3.1.b.zip`** (user-supplied, 2026-11-02) is a repo stub: one
  `README.md` = `# om-c-firmware`, no source. The community app ships only as the PyInstaller
  bundle (`research/dbfw_extracted/`, `app.pyc.raw` frozen). Source not published.
