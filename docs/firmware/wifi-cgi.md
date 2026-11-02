# Wi-Fi CGI handlers in firmware 1.4 (block 0)

Source: static RE of block 0 (runtime addr = load + 0x3d691020). The camera embeds its own oishare command-list XML (v2.20, 23 CGIs, at runtime 0x7e7707d0, 5614 B) that matches the live `get_commandlist.cgi` reply (compared as CGI-name sets). `get_commandlist` itself is handled in code but not listed in the XML.

**No `fwup` string exists anywhere in block 0**: confirms the E-M10 Mark I has no Wi-Fi firmware update (matches the live HTTP 520 probe).

Embedded CGIs: get_connectmode, switch_cammode, get_caminfo, exec_pwoff, get_resizeimg, get_movplaytime, clear_resvflg, get_rsvimglist, get_imglist, get_thumbnail, exec_takemotion, exec_takemisc, get_camprop, set_camprop, get_activate, set_utctimediff, get_gpsdivunit, get_unusedcapacity, get_dcffilenum, req_attachexifgps, req_storegpsinfo, exec_shutter, exec_shuttermisc.

## Handler functions (found via `do_cgi_*` log strings)

| handler | runtime addr | size |
|---|---|---|
| do_cgi_not_support_cgi | 0x7e6f9a26 | 95 |
| do_cgi_get_connectmode | 0x7e6f9a85 | 268 |
| do_cgi_get_caminfo | 0x7e6f9b91 | 473 |
| do_cgi_exec_pwoff | 0x7e6f9d6a | 195 |
| do_cgi_get_commandlist | 0x7e6f9e2d | 222 |
| do_cgi_get_movplaytime | 0x7e6fa1f9 | 445 |
| do_cgi_clear_resvflg | 0x7e6fa3b6 | 174 |
| do_cgi_get_rsvimglist | 0x7e6fa464 | 543 |
| do_cgi_get_imglist | 0x7e6fa683 | 390 |
| do_cgi_get_activate | 0x7e6faa71 | 286 |
| do_cgi_set_utctimediff | 0x7e6fab8f | 377 |
| do_cgi_get_gpsdivunit | 0x7e6fad08 | 298 |
| do_cgi_get_dcffilenum | 0x7e6fafcc | 335 |

Remote-control events go through `WIFI_REMOCON_CGI` (appevent callback/message, GET POINT, REC COMP, RECVIEW COMP, shooting type/mode/exposure-time/continuous-limit getters). The HTTP server task is `WIFI_HTTPD`; `wifi_mngr_*` and `ol_imageshare_*` back the browse/transfer calls.

TODO: document the rec-mode request parsing (cmd1/param1/cmd2) and the per-property get/desc/set leaf
value encodings. (DONE 2026-11-02: exec_shutter com→event map and exec_shuttermisc subcommands — see
below; set_camprop property table — see "Camera properties".)

## Dispatch tables (static RE; runtime addresses; name/handler pairs of 8 bytes)
The httpd selects a CGI table by connection mode, then calls the handler. Several modes share handlers.
| table | contents |
|---|---|
| 0x7e771e68 | get_connectmode, switch_cammode, get_caminfo, get_commandlist, get_resizeimg, get_movplaytime, get_rsvimglist, get_imglist, get_thumbnail (browse-only set) |
| 0x7e771f60 | full browse/private set: adds exec_pwoff, clear_resvflg, get_activate, set_utctimediff, get_gpsdivunit, get_unusedcapacity, get_dcffilenum, req_attachexifgps, req_storegpsinfo |
| 0x7e772048 | remote (rec) set: get_connectmode, switch_cammode, get_caminfo, exec_pwoff, get_commandlist, get_imglist, get_thumbnail, + set_takemode, exec_takemotion, exec_takemisc, get_camprop, set_camprop (these five all enter the rec dispatcher 0x7e70b5a8) |
| 0x7e7720d0 | shutter set: get_connectmode, switch_cammode, get_caminfo, exec_pwoff, get_commandlist, exec_shutter, exec_shuttermisc (both enter 0x7e70a0b5) |
Second-level tables: shutter 0x7e780c10 (exec_shutter -> 0x7e70a1be, exec_shuttermisc -> 0x7e70a292); rec 0x7e781500 (set_takemode 0x7e70c0c4, exec_takemotion 0x7e70c17c, exec_takemisc 0x7e70c245, get_camprop 0x7e70bd3c, set_camprop 0x7e70be2a, switch_cammode 0x7e70bef7).

### Rec dispatcher internals (RESOLVED 2026-11-02, mn10300 objdump of 0x7e70b5a8)

The rec dispatcher is the common front-end for all six rec CGIs. Steps:

1. **Tokenize the request** — split on a delimiter via helper 0x7da83862 + length via 0x7d99779f;
   copy the leading command token into a freshly allocated **128-byte** buffer (`[4,sp]`, alloc
   0x7e7116e2) and a **202-byte** response/work buffer (`[8,sp]`). A token longer than **127 bytes
   → error** (status −1), never dispatched. A buffer-alloc failure → status −2.
2. **Name lookup** — linear scan of the 6-entry, 8-byte-record table **0x7e781500**
   (`{name_ptr, handler}`), `strcmp` (0x7d997773) of the token against each name. Records (verified,
   decode clean):

   | # | name | handler |
   |---|---|---|
   | 0 | `set_takemode.cgi` | 0x7e70c0c4 |
   | 1 | `exec_takemotion.cgi` | 0x7e70c17c |
   | 2 | `exec_takemisc.cgi` | 0x7e70c245 |
   | 3 | `get_camprop.cgi` | 0x7e70bd3c |
   | 4 | `set_camprop.cgi` | 0x7e70be2a |
   | 5 | `switch_cammode.cgi` | 0x7e70bef7 |

   The selected handler cell (`[12,sp]`) is **pre-seeded** with the default handler **0x7e70c298**
   before the scan, so an unknown token keeps the default.
3. **Mode gate** — call 0x7e70f076, a critical-section (lock pair 0x7e710577 / 0x7e71060a) read of
   the rec-mode state flag at RAM **0xa0a9257e**; returns the flag. If `!= 1` (camera not actually in
   rec mode), two commands are still allowed through — `get_camcapa.cgi` (string @0x7e781b9b) and
   `switch_cammode.cgi` (@0x7e7814eb); **any other** token has its handler forced to the default
   0x7e70c298.
4. **Default handler 0x7e70c298** = immediate `respond_error(520, 1004)` (0x7e7074e6) — HTTP 520,
   `errorcode` 1004. So a wrong-mode or unknown rec command returns 520/1004.
5. **Invoke** — acquire (0x7e70efbe), `calls (handler)` with `a0` = saved arg, `a1` = response
   buffer; release (0x7e70efbe) after. This 0x7e70efbe pair is the per-request lock around the real
   CGI body (`WIFI_REMOCO…` locked section).

So the two gates a rec CGI passes: (a) its presence in the mode's top-level table (0x7e772048),
which yields the 1001 "not available in this mode" error seen live; (b) this dispatcher's own rec-mode
flag gate, which yields 520/1004 for everything except `get_camcapa`/`switch_cammode` when the flag
isn't set.

**`get_camcapa.cgi` dead end (2026-11-02):** the string 0x7e781b9b has exactly ONE reference in all
of block 0 — the gate-bypass `strcmp` immediate above. It is in **no dispatch table** (neither the
four top-level tables 0x7e771e68/0x7e771f60/0x7e772048/0x7e7720d0 nor the rec/shutter second-level
tables), so no handler is bound to it. After passing the gate it still misses the 0x7e781500 scan and
runs the pre-seeded default handler → **HTTP 520 / errorcode 1004**. It is also absent from the
OI.Share 4.6.0 endpoint list. Conclusion: `get_camcapa.cgi` is a **vestigial / other-model command
name** on the E-M10 Mark I — the firmware knows the name well enough to let it through the rec-mode
gate, but has no implementation, so it always errors. Not usable by the KMP client; capability
discovery must come from `get_caminfo` + `get_commandlist` + per-prop `get_camprop?com=desc`.

## Errors
`respond_error(0x208, 0x3ec)` = HTTP 520 + `errorcode` 1004 when a command argument is missing/unknown (static RE; not yet seen live).
LIVE (2026-11-01, camera in `private` connect mode): every `get_camprop.cgi?com=get|desc&propname=<any of the 14>` returns HTTP 520 `errorcode` 1001, same as an unknown CGI (`fwup_getversions`). So 1001 = CGI not available in the current connect mode / unsupported; the camprop CGIs are in the rec-mode table (0x7e772048) and need the camera switched to remote/rec mode first (`switch_cammode.cgi?mode=rec`). Confirms the per-mode table design. Later calls in that run got empty replies (camera or link dropped), so only the first 11 properties were queried.

## get_commandlist — self-describing command grammar (RESOLVED 2026-11-02)

`get_commandlist.cgi` returns the camera's **own** command grammar as XML (content-type `text/xml`).
Handler **0x7e6f9e2d**, present in all four top-level tables (0x7e771e68 / 0x7e771f60 / 0x7e772048 /
0x7e7720d0) — a universal CGI available in every connect mode. It emits a **static 5616-byte XML
template at 0x7e7707d0** (copied via 0x7e6fd474 into a 5616-byte buffer; a mode-indexed table at
0xa0a92720, index cell 0x608e9210, selects the buffer). The template:

```
<?xml version="1.0"?>
<oishare>
 <version>2.20</version>
 <support func="web"/> <support func="remote"/> <support func="gps"/> <support func="release"/>
 <cgi name="..."> <http_method type="get|post"> <cmd1 name="..."> <param1 name="...">
   <cmd2 name="..."> <param2 name="..."/> ... </cmd2> </param1> </cmd1> </http_method> </cgi>
 ... (23 <cgi> entries)
</oishare>
```

This **is** the `cmd1`/`param1`/`cmd2`/`param2` grammar (the open "rec-mode request parsing" thread):
a self-describing schema the client fetches to learn the legal CGI/argument tree. The 23 `<cgi>`
entries equal the embedded CGI set exactly. `switch_cammode` shows `cmd1=mode` →
`param1={rec,play,shutter}`, with `rec`/`shutter` carrying `cmd2=lvqty` → `param2={0320x0240,
0640x0480}` (confirms the live-tested `switch_cammode.cgi?mode=rec&lvqty=0320x0240`).

**Independent corroboration of the camprop RE** — the template's `get_camprop`/`set_camprop` grammar
matches the disassembly-derived property tables exactly:
- `get_camprop` `com=get` and `com=desc` (both HTTP GET) each enumerate **14** `propname` values:
  touchactiveframe, takemode, drivemode, focalvalue, expcomp, shutspeedvalue, isospeedvalue, wbvalue,
  noisereduction, lowvibtime, bulbtimelimit, artfilter, digitaltelecon, desclist.
- `set_camprop` `com=set` (HTTP **POST**) enumerates exactly the **8 settable** props: takemode,
  drivemode, focalvalue, expcomp, shutspeedvalue, isospeedvalue, wbvalue, artfilter — identical to
  the settable set found in the set-leaf disassembly. So the five read-only props (touchactiveframe,
  noisereduction, lowvibtime, bulbtimelimit, digitaltelecon) are read-only by design, confirmed from
  two independent sources.

**For the KMP client:** fetch `get_commandlist.cgi` once after connect to get the full legal
command/argument tree and the firmware's oishare version (`2.20`), rather than hard-coding endpoints.
This is the correct capability-discovery entry point (`get_camcapa.cgi` does not exist on this body —
see its dead-end note above).

## Image / playback browse CGIs (RESOLVED 2026-11-02)

| CGI | handler | returns |
|---|---|---|
| get_imglist | 0x7e6fa683 | `text/plain` directory listing |
| get_thumbnail | 0x7e6fa809 | thumbnail JPEG bytes |
| get_resizeimg | 0x7e6f9f0b | resized full-frame JPEG (companion; not disassembled in detail) |

**get_imglist.cgi?DIR=`<path>`** — takes a required `DIR=` query param (parsed via tokenizer
0x7da83862; missing → error, debug `"no ?DIR= : (do_cgi_get_imglist)"`). Walks the directory with
the card/file enumerators 0x7de9e636 / 0x7de9e64e and emits a `text/plain` body of per-file records
(debug fields `dir_type=`, `file_path:`, `directory_no_exists`). This is the standard OI.Share
directory-listing protocol (one CSV-ish line per entry: path, name, size, attribute, date, time). The
client walks `/DCIM` top-down using `DIR=` to descend.

**get_thumbnail.cgi** — parses file params via 0x7da83862, then **branches on file extension**: for
video (`.MOV` / `.AVI`, strings @0x7e77263e) it extracts a poster frame via
`play_load_get_mov_info` (0x7dd…); for stills it pulls the embedded EXIF thumbnail through the JPEG
helpers 0x7dd62b59 / 0x7dd69e07 / 0x7dd5c812. Response body = the thumbnail JPEG. (Mirrors the
`get_movplaytime` / `get_rsvimglist` playback group.)

For the KMP client these three cover remote image browse: `get_imglist` to enumerate, `get_thumbnail`
for previews, `get_resizeimg` for a downscaled full image, and the raw file over the normal file path.

## get_activate — time-sync activation status (RESOLVED 2026-11-02)

`get_activate.cgi` handler **0x7e6faa71** returns `<?xml version="1.0"?>\r\n<activate>STATE</activate>`
where STATE is **`notyet`** or **`done`**. It reads registry key **36084 (0x8CF4)** via getter
0x7d9d36c4 (debug string `"timegap ="` @0x7e772aef): if the getter returns **-1** (no stored value)
→ `notyet`, otherwise → `done`.

So "activate" here is **not** licensing/DRM — it is whether the camera's **UTC time offset
("timegap")** has been configured, i.e. whether the client has called `set_utctimediff.cgi` this
session. A fresh connection reports `notyet`; after the app pushes the phone's UTC offset it reports
`done`. This pairs with `set_utctimediff` / `get_gpsdivunit` / `req_storegpsinfo` (the GPS/geotag
support group) — the app is expected to sync time before geotagging. For the KMP client: call
`set_utctimediff` early, then `get_activate` should read `done`.

## Camera-mode state machine (switch_cammode / get_connectmode) (RESOLVED 2026-11-02)

Two distinct state concepts, two RAM cells:

| cell | meaning |
|---|---|
| 0x608e9210 | **connection index** — selects the per-connection context/CGI-table and buffer (indexes table 0xa0a92720, `asl2` → ×4). Used by every CGI handler. |
| 0xa0a9257e | **current cammode** — `0`/`1`/`2`. Read through critical-section helper **0x7e70f076** (the "gate" in the rec dispatcher). `1` = **rec** (so the rec dispatcher's "flag == 1" test = "camera is in rec mode"). The other two are play/browse and shutter. |
| 0xa0a9258c | **lvqty** (live-view quality) — set `1` for `0640x0480`, else `0`, from the `lvqty` param. |

`switch_cammode.cgi` enters via the rec dispatcher 0x7e70b5a8 (its top-level handler in all four
tables **is** 0x7e70b5a8), bypasses the cammode gate (it is one of the two gate-bypass names), and is
dispatched to leaf **0x7e70bef7**. The leaf:
1. Requires at least the `mode` arg (`movhu (a3)` count `< 1` → error 0x7e70c0b5).
2. Parses `lvqty` (strings `0320x0240` / `0640x0480` @0x7e781d33) → writes 0xa0a9258c.
3. Parses `mode` against the null-separated list `rec\0play\0shutter` (@0x7e781d47) and, combined with
   the **current** cammode from 0x7e70f076, posts a camera-task **transition app-event** via
   0x7e70e0c3. Events observed in the transition matrix: **0x41b0001, 0x41b0002, 0x41b0020,
   0x41b0022, 0x41b0023** (= 68878337/338/368/370/371). The exact (current → target) → event mapping
   is only partially traced (see dead end).

`get_connectmode.cgi` handler **0x7e6f9a85**: reads the connection context (0x608e9210 → 0xa0a92720),
calls 0x7e7078d1 to fetch the current connect-mode value, and returns it as a small
`connect mode` / `text/xml` document (templates @0x7e7721e9 / 0x7e772205). Note **connect mode**
(web/private/etc., per the top-level table selection) is a separate axis from **cammode**
(rec/play/shutter) handled by switch_cammode.

**Dead end / partial:** the full switch_cammode transition matrix — which of the five 0x41b00xx events
fires for each (current cammode, requested mode, lvqty) combination — was not exhaustively traced; the
branch tree at 0x7e70bf3f–0x7e70c0c8 is large and the event semantics live in the camera task (not
block-0 resident). Enough is known for the client: send `switch_cammode.cgi?mode=rec&lvqty=0320x0240`
to enter rec mode (live-verified earlier), `?mode=play` to leave it. The precise event ids are
recorded above for any future live correlation.

## get_caminfo — model name only (RESOLVED 2026-11-02)

`get_caminfo.cgi` handler **0x7e6f9b91** (universal — in all four top-level tables) returns a tiny XML
document:

```
<?xml version="1.0"?>
<caminfo>
<model>%s</model>
</caminfo>
```

(templates at 0x7e77231d + 0x7e772347; built into the shared response buffer via 0x7e6fd474.) The
`%s` model-name string is fetched at runtime from the camera's property registry: getter 0x7d9d3769
with key **25329 (0x62F1)** into a 128-byte buffer (debug string `"model name : %s"` @0x7e77230c).

**Limitation / dead end for the app:** `get_caminfo` exposes **only the model name** — no firmware
version, no serial number, no capability flags. The registry value for key 0x62F1 is not statically
resolvable from block 0 (it comes from the runtime property DB), but OI.Share shows it as the short
model string (e.g. `E-M10`). So over Wi-Fi:
- **Model name** → `get_caminfo`.
- **Firmware version** → NOT available over Wi-Fi (consistent with the no-Wi-Fi-fwup finding; version
  is read over USB/PTP or shown in the body menu only).
- **Serial** → NOT in any CGI; only surfaced in the AP SSID `E-M10-P-<serial>`.

The firmware's own error-log strings here contain a typo, `get_cominfo.cgi` (@0x7e772377/0x7e77239b) —
cosmetic, the live CGI name is `get_caminfo.cgi`.

## Camera properties (get_camprop / set_camprop)
Table `desclist` at 0x7e7816b0, 16-byte records `{name, get, desc, set}`; 0 = not available. `com=get` -> slot 1, `com=desc` -> slot 2, set_camprop `com=set` -> slot 3.
| prop | get | desc | set |
|---|---|---|---|
| desclist | y | - | - |
| touchactiveframe | y | y | - |
| takemode | y | y | y |
| drivemode | y | y | y |
| focalvalue | y | y | y |
| expcomp | y | y | y |
| shutspeedvalue | y | y | y |
| isospeedvalue | y | y | y |
| wbvalue | y | y | y |
| noisereduction | y | y | - |
| lowvibtime | y | y | - |
| bulbtimelimit | y | y | - |
| artfilter | y | y | y |
| digitaltelecon | y | y | - |
So noisereduction, lowvibtime, bulbtimelimit, digitaltelecon are read-only over Wi-Fi.

Per-property leaf handler addresses (get / desc / set), dumped from the table 2026-11-02 for the
next decompile pass on the value encodings:

| prop | get | desc | set |
|---|---|---|---|
| desclist | 7e70cf89 | - | - |
| touchactiveframe | 7e70d09d | 7e70d0e9 | - |
| takemode | 7e70d17f | 7e70d1cc | 7e70d251 |
| drivemode | 7e70d31b | 7e70d379 | 7e70d3c3 |
| focalvalue | 7e70d478 | 7e70d4d5 | 7e70d51e |
| expcomp | 7e70d5c4 | 7e70d621 | 7e70d66a |
| shutspeedvalue | 7e70d710 | 7e70d76d | 7e70d7b6 |
| isospeedvalue | 7e70d898 | 7e70d8f5 | 7e70d93e |
| wbvalue | 7e70d9e3 | 7e70da40 | 7e70da89 |
| noisereduction | 7e70db2e | 7e70db7b | - |
| lowvibtime | 7e70dbf2 | 7e70dc3f | - |
| bulbtimelimit | 7e70dcae | 7e70dcfb | - |
| artfilter | 7e70dd56 | 7e70ddb4 | 7e70ddfe |
| digitaltelecon | 7e70deaa | 7e70def7 | - |

### set_camprop value encoding (RESOLVED 2026-11-02, mn10300 objdump of the set leaves)
Every settable property's `com=set` leaf follows the same shape (verified on all 8):

1. Get the session/arg object (`0x7d996faa`); null → HTTP 520 `errorcode` **1005** (no session/context).
2. Parse the `value` to a numeric and **range-check `value < 0x4000` (16384)**; out of range → the fail path.
3. Validate the value against the property's current allowed set via the shared helpers
   `0x7e711742` then `0x7e71278d` (the same list the `get`/`desc` leaves emit); reject → fail.
4. Encode the value through a per-property encoder (`0x7e712228` / `0x7e7122d4` / `0x7e711e80` …) into a
   stack buffer, then write a 3-word command block to RAM **0xa0a925c0**:
   `[0xa0a925c0] = sub-id`, `[0xa0a925c4] = 0`, `[0xa0a925c8] = encoded value`.
5. Post an app event (`0x7e70e0c3`) to apply it; event return non-zero → fail.
6. Success → HTTP 200; value rejected at any step → HTTP 520 `errorcode` **3001** (bad/!settable value).

The property is selected by the **(event id, sub-id)** pair in the command block, not by a per-property
handler — all but `takemode` share event **0x41b0011**:

| prop | app event | sub-id `[0xa0a925c0]` | value range |
|---|---|---|---|
| takemode | 0x41b0014 | 0 | < 0x4000 |
| expcomp | 0x41b0011 | 2 | < 0x4000 |
| focalvalue (aperture) | 0x41b0011 | 3 | < 0x4000 |
| shutspeedvalue | 0x41b0011 | 4 | < 0x4000 |
| isospeedvalue | 0x41b0011 | 6 | < 0x4000 |
| wbvalue | 0x41b0011 | 9 | < 0x4000 |
| drivemode | 0x41b0011 | 0x81b (2075) | < 0x4000 |
| artfilter | 0x41b0011 | (0x41b0011 path) | < 0x4000 |

So the Wi-Fi property-set path is: HTTP `value` → range/allowed-list check → encode → write
`{sub-id, 0, value}` at 0xa0a925c0 → post event 0x41b0011/0x41b0014. The encoded value's exact units
(the per-property encoder output) are not yet decoded — `get`/`desc` return the enumerated legal
values, so the KMP client should pick from the `desc` list rather than compute an encoding. drivemode's
sub-id 0x81b sits in a different numeric space than the others (confirmed, not a misparse).

### get_camprop / desc value-list path (RESOLVED 2026-11-02, mn10300 objdump)

`com=get` (read current value) and `com=desc` (enumerate legal values) share **one app event,
`0x41b0012` (= 68878354)** — a generic *camprop-query* event. They are told apart by the command
block written to RAM `0xa0a925c0`, not by the event id:

| path | builder | `[0xa0a925c0]` | `[0xa0a925c4]` | `[0xa0a925d0]` | event |
|---|---|---|---|---|---|
| get-value | 0x7e70e3ed | `a3` (ptr) | `d0` | `d0` (movhu) | 0x41b0012 |
| get-desc | 0x7e70e88e | sub-id | 0 | 0 | 0x41b0012 |

Both post via 0x7e70e0c3, then read the result buffer at `a3 = [0xa0a925d4]` and the status/count
word at `[0xa0a925d0]`.

The **desc builder 0x7e70e88e** then switches on sub-id to a per-property desc formatter that turns
the returned buffer into the enumerated legal-value list:

| sub-id | property | formatter |
|---|---|---|
| 2 | expcomp | 0x7e7120c8 |
| 3 | focalvalue | 0x7e7121b6 |
| 4 | shutspeedvalue | 0x7e711f65 |
| 6 | isospeedvalue | 0x7e711ec1 |
| 9 | wbvalue | 0x7e712053 |
| 2075 (0x81b) | drivemode | 0x7e711e50 |
| 280 (0x118) | artfilter | 0x7e7123ff |
| 10032 (0x2730) | **unidentified** | 0x7e7124e9 |
| default | error | log string @0x7e78… |

**takemode is special:** its desc leaf 0x7e70d1cc does NOT go through the 0x7e70e88e switch. It
gets its own session (0x7d996fe2), writes `0xa0a925c0/c4/d0`, posts its own event **`0x41b0015`
(= 68878357)**, reads `[0xa0a925d0]`, calls 0x7e7122a4, then response-builder 0x7e711d09.

So the camprop event map is:

| event | meaning |
|---|---|
| 0x41b0011 | set value (all settable props except takemode) |
| 0x41b0012 | get value **and** get desc (query), per command block |
| 0x41b0014 | set takemode |
| 0x41b0015 | get/desc takemode |

Shared helpers: 0x7d996fe2 = get-session (get/desc), 0x7d996faa = get-session (set),
0x7d996ff0 / 0x7d996fb8 = release-session, 0x7e7074a1 = HTTP-200 respond, 0x7e7074e6 = HTTP-520
error respond, 0x7e711d09 = response-list builder, 0x7d9999f9 = error/log formatter.

**Dead ends logged:** (1) sub-id `10032` (0x2730) has a real desc formatter (0x7e7124e9) in the
switch but is an **orphan case**: exactly 7 Wi-Fi desc leaves call 0x7e70e88e (expcomp 2, focalvalue
3, shutspeedvalue 4, isospeedvalue 6, wbvalue 9, drivemode 2075, artfilter 280), and none passes
10032 — so no Wi-Fi desclist property drives it. It is reachable only by some non-Wi-Fi caller of
0x7e70e88e (internal camprop query), not through the 14-entry desclist. (2) The read-only simple
props (touchactiveframe, noisereduction, lowvibtime, bulbtimelimit, digitaltelecon) **bypass
0x7e70e88e entirely** — each desc leaf does get-session 0x7d996fe2 → a per-prop helper (e.g.
touchactiveframe 0x7da82515; noisereduction/lowvib/bulb/telecon via 0x7db93fb8 + 0x7e712315 /
0x7e71238a) → response-builder 0x7e711d09, with no 0x41b0012 query event at all. The earlier
"280-repeat" heuristic for identifying them was noise, not reliable.
(3) Encoded-value units still not decoded — `desc` enumerates the legal values, so the KMP client
picks from that list rather than computing an encoding.

## exec_shutter (RESOLVED 2026-11-02, mn10300 objdump of leaf 0x7e70a1be)
First level `exec_shutter`/`exec_shuttermisc` wrap the handler in `WIFI_RELEASE_CGI(1)...(0)`.

Leaf 0x7e70a1be: reads the arg count (`movhu (a1),d1`); if `<=0` → HTTP 520 `errorcode` 1004 via
0x7e7074e6. Otherwise matches the `com` arg against 6 string constants (strcmp helper 0x7d997773,
strings at 0x7e780c-xx) and loads an app-event id into d2; on a match it posts the event via
0x7d9b12a2, then always returns **HTTP 200** (0x7e7074a1). Unknown `com` → d2 stays 0 → no event
posted, still HTTP 200. The complete `com` → event map (strcmp order):

| `com` | app event | meaning |
|---|---|---|
| `1stpush` | 0x41b0024 | half-press down (AF + meter) |
| `1strelease` | 0x41b0025 | half-press up |
| `2ndpush` | 0x41b0026 | full-press down (release shutter) |
| `2ndrelease` | 0x41b0027 | full-press up |
| `1st2ndpush` | 0x41b0028 | full press in one step (AF + shutter) |
| `2nd1strelease` | 0x41b0029 | release shutter but keep half-press held |

These six are exactly the `exec_shutter.cgi?com=` values seen in the OI.Share capture
(`../usb-protocol/wifi-cgi-endpoints-oishare-4.6.0.txt`). So the Wi-Fi shutter control is a thin
HTTP→app-event shim: each `com` posts one key-state event (events 0x41b0024..29) into the body's
normal shutter-button event path.

### exec_shuttermisc (leaf 0x7e70a292)
Arg-indexed dispatch through an 8-byte `{strptr, handler}` table at **0x7e780c3c** (helper
0x7da836f1):

| `com` | handler |
|---|---|
| `startliveview` | 0x7e70a2f3 |
| `stopliveview` | 0x7e70a36d |

So **live-view start/stop is also reachable from the shutter-mode dispatcher** (table 0x7e7720d0),
not only via `exec_takemisc` in rec mode — the shutter personality can both drive the shutter and
open the MJPEG-over-UDP stream (`../usb-protocol/liveview-udp.md`).

set_takemode 0x7e70c0c4: maps `com` to a mode id 0..3 or 0xffff, calls WIFI_REMOCON_CGI + a state setter.

Ghidra decompiler caveat: MN103 calling convention (A0 = this/ctx, A1 = args) is not modelled, so params show as `in_A0/in_A1`. Auto-names like `version_7e70bd3c` come from a nearby string, not the real function role.

## LIVE verification (2026-11-01, after `switch_cammode.cgi?mode=rec&lvqty=0320x0240`, then back with `mode=play`)
Static prediction confirmed: the `getset`/`get` attributes from `desclist` match the firmware table exactly (read-only: touchactiveframe, noisereduction, lowvibtime, bulbtimelimit, digitaltelecon).
- `switch_cammode` replies `200` with empty body (`Content-Type: www/unknown`).
- `get_camprop?com=get&propname=desclist` -> HTTP 520 `errorcode` 1004 (bad argument: desclist only supports `com=desc`). This is the first live 1004, confirming its meaning.
- `com=desc&propname=desclist` returns all 13 descs in one XML (2322 B); per-property `desc` and `get` also work.

Values at probe time and value domains (`enum`):
| prop | attr | value | enum |
|---|---|---|---|
| takemode | getset | P | iAuto P A S M ART |
| drivemode | getset | continuous-L | normal continuous-H continuous-L selftimer customselftimer |
| focalvalue | getset | 5.6 | 1.0 .. 91 (1/3-stop steps; list is lens-independent here) |
| expcomp | getset | +0.3 | -5.0 .. +5.0 in 1/3 steps |
| shutspeedvalue | getset | 250 | livetime livebulb 60" .. 1.3 .. 8000 |
| isospeedvalue | getset | Auto | Auto Low 200 .. 25600 |
| wbvalue | getset | 0 | 0 18 16 17 20 35 64 23 256 257 258 259 512 |
| artfilter | getset | ART01 | ART01 .. ART12 ARTBKT |
| noisereduction | get | off | off on auto |
| lowvibtime | get | 0 | 0 1 125 250 500 1000 2000 4000 8000 15000 30000 |
| bulbtimelimit | get | 8 | 1 2 4 8 15 20 25 30 |
| digitaltelecon | get | off | on off |
| touchactiveframe | get | 0054-0040_0211x0159 | (position-size string) |
Only read calls were made against these properties; no property was set. The camera was returned to `play` mode. Raw capture: `research/camera-probe-camprop-*.txt` (gitignored).
