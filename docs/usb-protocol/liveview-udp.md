# Wi-Fi live-view UDP stream format

The wire format of the OI.Share live-view stream — the one gap in the Wi-Fi remote-control plane
(`wifi-api.md`). Reverse-engineered from the OI.Share Android app (`research/oishare`, class
`e.b.a.d.b` = "OlyPare" parser; jadx decompile kept local in the scratchpad, not committed —
interop RE, Olympus-app code). This is what the KMP replacement needs to render live view.

## Transport

1. Client opens a UDP socket on a local port P.
2. Client sends `GET http://192.168.0.10/exec_takemisc.cgi?com=startliveview&port=P`
   (optionally `&lvqty=0640x0480` or `0320x0240`).
3. Camera streams MJPEG to `clientIP:P` as a sequence of UDP datagrams. Each JPEG frame is split
   across one or more datagrams; the app reassembles, verifies, and hands the complete JPEG up.
4. `GET …?com=stopliveview` ends the stream.

Receive buffer is 65536 bytes (one datagram ≤ 64 KiB). All multi-byte header fields are
**big-endian**.

## Datagram header

Fixed **12-byte base header** on every datagram:

| offset | size | field | notes |
|---|---|---|---|
| 0 | u8  | flags0 | bit `0x10` set = **first** datagram of a frame |
| 1 | u8  | flags1 | bit `0x80` set = **last** datagram of a frame |
| 2 | u16 | sequence | per-datagram counter, wraps at 65535; first datagram seeds it, each next must be `prev+1` (else the datagram is dropped as out-of-order) |
| 4 | u32 | timestamp | 90 kHz clock (RTP-style); frame PTS in ms = `timestamp / 90000 * 1000`; constant across a frame's datagrams |
| 8 | u32 | reserved | not consumed by the parser |

**First datagram of a frame** (flags0 `0x10`) carries an extra sub-header after the base 12 bytes:

| offset | size | field |
|---|---|---|
| 12 | u16 | reserved / unused by parser |
| 14 | u16 | `extCount` N = number of 4-byte words in the extension block |
| 16 | N×4 bytes | extension TLV block (overlay metadata, see below) |
| 16 + N×4 | … | JPEG data — must begin `FF D8` (SOI) |

**Continuation / last datagrams** (flags0 clear): JPEG payload starts immediately at **offset 12**
(no extension block). The last datagram (flags1 `0x80`) must end `FF D9` (EOI); the parser also
length-checks the reassembled image before firing its frame callback.

So: concatenate `payload(firstPkt)[16+N*4:] + payload(contPkt)[12:] + …` → one JPEG per frame.

## Extension TLV block (first datagram)

Starts at offset 16, runs for `N×4` bytes. Each entry:

```
u16 type
u16 lenWords          // number of 4-byte values that follow
lenWords × u32        // big-endian values
```

Next entry at `+4 + lenWords*4`. Observed types (names from the parser's effect on the frame
object; `g` big-endian u16, `h` big-endian u32):

| type | lenWords | meaning (inferred) |
|---|---|---|
| 1  | 1 | image size / data length |
| 3  | 1 | frame param |
| 4  | 1 | frame param |
| 5  | 1 | frame param |
| 6  | 1 | frame param |
| 7  | 1 | frame param |
| 8  | 3 | triple (x, y, size) — overlay frame |
| 9  | 3 | triple — overlay frame |
| 10 | 3 or 4 | triple — overlay frame (AF/face) |
| 11 | 2 | pair |
| 12+ | … | further overlay metadata |

The sibling parser (`e.b.b.g.a`, a second/newer stream variant) decodes some of these triples as
screen rectangles: `Rect(x = v>>16, y = v&0xFFFF, …)` — i.e. the AF/face-detection frames and
on-screen indicators the app overlays on live view. The replacement can ignore the TLV block and
still get video; parse it only to draw AF/face boxes and status.

## Full TLV table — newer stream variant

The newer receiver (`e.b.b.g.a` = `JpegUdpReceiver`; frame object `e.b.b.b` = `OlyLiveviewData`;
helper `e.b.b.g.c` = big-endian `a`=u16/`b`=u32 readers — jadx decompile kept local) carries a
much larger type set than the table above. Its `d()` method walks the same `[u16 type][u16
lenWords][lenWords × u32-BE]` entries from offset 16 and dispatches on `type`. Field names in
`OlyLiveviewData` are obfuscated single letters, so meanings below are from each field's *use*, not
a label. Values are big-endian; a "packed pair" is one u32 read as `hi = v>>16, lo = v&0xFFFF`.

| type | lenWords | decode | inferred meaning |
|---|---|---|---|
| 1   | 1 | `f3624b` (via `v()`, also allocates the frame byte buffer) | **primary JPEG total size** |
| 200 | 1 | `H` (via `B()`), only if `>0` | **alternate JPEG total size**; its presence flips the frame's `K` flag |
| 3   | 1 | `f3627e` | scalar param |
| 4   | 1 | `f3625c` | scalar param |
| 5   | 1 | `f3626d` | scalar param |
| 16  | 1 | `r` | scalar param |
| 17  | 1 | `s` | scalar param |
| 8   | 3 | `f3628f,g,h` | int triple (overlay/coord group) |
| 9   | 3 | `i,j,k` | int triple |
| 10  | 3 | `l,m,n` | int triple |
| 12  | 3 | `o,p,q` | int triple |
| 18  | 3 | 3 packed pairs → `t,u` / `v,w` / `x,y` | 3 coordinate pairs (6 values) |
| 106 | 2 | u32 `z` (long), then packed pair → `A,B` | long + pair |
| 107 | 3 | packed pair → `C,D`, then `E`, then `F` | pair + 2 scalars |
| 108–115 | 2 | `Rect(x=v0>>16, y=v0&0xFFFF, right=x+(v1>>16), bottom=y+(v1&0xFFFF))`, keyed 1–8 | **8 on-screen overlay rectangles** (AF-point / face-detection frames), stored in a `LinkedHashMap<Integer,Rect>` |

So the AF/face boxes are types **108–115** (`g(index, offset)` → `Rect`), up to 8 simultaneously;
the len-3 triples (8/9/10/12/18) are additional coordinate/indicator groups the newer app overlays.
Entry advance is `i = i + 4 + lenWords*4`; an unknown type is skipped by its `lenWords`.

### Reassembly refinements (newer variant)

- **First packet** (`flags0 & 0x10`): allocates a fresh `OlyLiveviewData`. If its sequence `< `
  the running counter it is a late/duplicate first packet — retried (ignored) up to **4 times**
  before the parser resyncs to it, rather than a strict `prev+1` drop.
- **Continuation**: requires `sequence == runningCounter` exactly; a mismatch is treated as a frame
  boundary (timestamp change), not appended.
- **Last packet** (`flags1 & 0x80`): fires the frame callback only when the accumulated byte count
  equals **either** the type-1 size **or** the type-200 size; the `K` flag records which matched
  (type-200 ⇒ `K=true`), and `FF D8 … FF D9` bounds are still verified.

## Minimal client (replacement)

1. Bind UDP port P, send `startliveview&port=P`.
2. Per datagram: read 12-byte header; if flags0&0x10, skip extension (`16 + be16(buf,14)*4`) and
   start a new frame buffer, else append from offset 12; track sequence continuity.
3. On flags1&0x80: verify `FF D8 … FF D9`, decode JPEG, display. Use the 90 kHz timestamp for
   frame pacing.
4. `stopliveview` on teardown.
