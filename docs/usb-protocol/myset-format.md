# Myset backup/restore file format (`.myset` / OI.Share share blob)

The on-disk/over-the-wire format of a camera-settings "myset" backup — what the KMP replacement
must read and write to back up and restore E-M10 custom-settings banks. Reverse-engineered
statically (never executed) from OI.Share's native helper `libolytools.so`
(`research/oishare/lib/x86_64/libolytools.so`), functions
`Java_jp_co_olympus_olytools_MysetTools_EncodeMyset` / `DecodeMyset`, plus `ConvertDesEncodeData` /
`EncodeByDES`. Interop RE; the `.so` and jadx/objdump output stay local, not committed.

## Pipeline (Java ⇄ native)

`jp.co.olympus.olytools.MysetTools` (see `MysetTools.java`, `MysetInfoData.java`):

- **Encode** (make a shareable/backup file): camera myset bank bytes land in `MysetInfoData.mSrcData`
  (the raw settings blob, pulled from the camera via `get_partialmysetdata.cgi`); Java metadata
  getters supply Title/Comment/ModelName/SerialNo/SaveDateTime/FirmVersion/IconType/MysetType;
  `EncodeMyset` builds the full file into `mOutData`.
- **Decode** (restore / import a file): the file bytes go in `mSrcData`; `DecodeMyset` validates the
  `OLMY` magic, extracts metadata into the Java fields, and decrypts the raw settings blob into
  `mOutData` (which is then pushed back to the camera via `send_partialmysetdata.cgi`).

(The `MakeBasicHeader`/`MakeCommonHeader`/`MakeCamHeader`/`MakeAppHeader` functions in the same `.so`
are a **different** subsystem — CameraLog telemetry upload, magic `"log\0"`, getters getModelId /
getSelialNo[sic] / getSaveDateTime — not myset. Don't confuse them.)

## File layout

All multi-byte integers **little-endian** (x86/ARM native stores; `movl`/`movw` little-endian).
Fixed header is **0x1120 (4384) bytes**, followed by the encrypted payload.

| offset | size | field | notes |
|---|---|---|---|
| `0x000` | 4 | magic `"OLMY"` | bytes `4F 4C 4D 59`; `DecodeMyset` rejects anything else |
| `0x004` | 4 | header size | always `0x00001120` (4384) |
| `0x008` | 4 | format version | `2` |
| `0x00C` | 32 | ModelName | ASCII, NUL-padded, capped 32 |
| `0x02C` | 32 | SerialNo | ASCII, NUL-padded, capped 32 |
| `0x04C` | 32 | SaveDateTime | ASCII, NUL-padded, capped 32 |
| `0x06C` | 4 | FirmVersion | capped 4 bytes; Java keeps the **last 4** chars of an 8-char version |
| `0x070` | 4 | MysetType | u32 bitmask: `CURRENT=0, MYSET1=1, MYSET2=2, MYSET3=4, MYSET4=8` |
| `0x074` | 4268 | **OISM** inner block | see below (size `0x10AC`) |
| `0x1120` | N | encrypted payload | the settings blob, two-layer DES (below) |

### OISM inner block (at `0x074`, size `0x10AC` = 4268)

Zero-filled then populated; the display-text metadata lives here (so it can be larger than the
fixed-width ASCII fields above).

| rel. offset | size | field | notes |
|---|---|---|---|
| `+0x000` | 4 | magic `"OISM"` | bytes `4F 49 53 4D` |
| `+0x004` | 4 | block size | `0x000010AC` (4268) |
| `+0x008` | 4 | IconType | u32 (`GetIconType`) |
| `+0x00C` | 256 | Title | **UTF-8**, NUL-padded, capped 256 (`0x100`) |
| `+0x10C` | 4000 | Comment | **UTF-8**, NUL-padded, capped 4000 (`0xFA0`) |

(4 + 4 + 4 + 256 + 4000 = 4268 = `0x10AC`, exact. ModelName/SerialNo/SaveDateTime use the platform
default charset in Java; only Title/Comment are UTF-8.)

## Payload encryption — two-layer DES

The settings blob (`SrcData`) is **never stored in clear**. `EncodeMyset`:

1. **Inner DES**: generate a key `K` = **7 random uppercase ASCII letters** (`srand(clock_gettime
   nsec)`, then `rand()%26 + 'A'`, ×7). `C1 = DES_encrypt(key=K, SrcData)`.
2. **Append key**: `blob = C1 ‖ K` (the 7-byte key is concatenated right after the inner
   ciphertext, so the decoder can recover it).
3. **Outer DES**: `payload = DES_encrypt(key="OLmySet", blob)`. `"OLmySet"` = bytes
   `4F 4C 6D 79 53 65 74`, a **fixed hard-coded key** compiled into the `.so`.

The final file is `header(0x1120) ‖ payload`, returned to Java as `mOutData`.

**Decode** reverses it: `DES_decrypt("OLmySet", payload)` → `C1 ‖ K`; split off the trailing 7 bytes
as `K`; `DES_decrypt(K, C1)` → original `SrcData`.

### DES details (`ConvertDesEncodeData` → `EncodeByDES`)

- Cipher is single **DES** (symbols `EncodeByDES` / `DecodeByDES`, key struct `tagDESKEY`). The key
  struct is the ASCII key bytes above fed straight into DES key setup (DES uses an 8-byte key, 56
  effective bits; these keys are 7 ASCII bytes).
- DES is an 8-byte block cipher, so the plaintext is **padded to a multiple of 8 bytes**. The
  padding bytes are **random uppercase ASCII letters** (same `rand()%26+'A'` generator as the key),
  *not* zero- or PKCS-padding. The pre-pad length is tracked separately (the length passed by
  reference, `Rj` in the mangled name), so the decoder trims back to the real length — do not assume
  the decrypted length is a clean multiple of 8.
- Mode: the loop structure around `EncodeByDES` processes the buffer as independent 8-byte blocks
  (ECB-style; no IV observed). Confirm chaining against a real sample before trusting a reimpl.

## For the KMP replacement

- **Restore flow**: read `.myset` → check `OLMY` → parse header fields for display/validation →
  `DES_decrypt("OLmySet")` → strip 7-byte key `K` → `DES_decrypt(K)` → trim to true length →
  `send_partialmysetdata.cgi` (+ `set_mysetdatasize.cgi`) to the camera.
- **Backup flow**: `get_partialmysetdata.cgi` → raw blob → inner-DES with random `K`, append `K`,
  outer-DES with `"OLmySet"` → prepend the 4384-byte header → write `.myset`.
- A pure-Kotlin DES (javax.crypto `DES/ECB/NoPadding` on JVM/Android; a small DES impl or
  platform crypto on iOS/native) covers both layers. The random-uppercase block padding must be
  reproduced on encode and discarded on decode.
- The fixed key `"OLmySet"` and the whole scheme are **obfuscation, not security** — documented here
  only for interoperability (reading/writing the user's own camera backups).

## Open / unverified

- DES block mode (ECB assumed from the per-8-byte loop; no IV seen) — verify against a
  camera-produced `.myset` sample.
- Exact `tagDESKEY` → 56-bit key-schedule mapping (parity-bit handling of the 7 ASCII bytes) — only
  matters if a reimpl must be byte-identical; interop just needs the same key setup DES libraries
  use.
- Whether the camera's `get_partialmysetdata` blob equals `SrcData` verbatim or is itself framed —
  not yet captured live (would need an approved Wi-Fi session).
