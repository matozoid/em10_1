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

## Minimal client (replacement)

1. Bind UDP port P, send `startliveview&port=P`.
2. Per datagram: read 12-byte header; if flags0&0x10, skip extension (`16 + be16(buf,14)*4`) and
   start a new frame buffer, else append from offset 12; track sequence continuity.
3. On flags1&0x80: verify `FF D8 … FF D9`, decode JPEG, display. Use the 90 kHz timestamp for
   frame pacing.
4. `stopliveview` on teardown.
