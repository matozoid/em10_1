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

TODO: decompile handlers, document request parsing (cmd1/param1/cmd2), the exec_shutter state machine, and the set_camprop property table.

## Dispatch tables (static RE; runtime addresses; name/handler pairs of 8 bytes)
The httpd selects a CGI table by connection mode, then calls the handler. Several modes share handlers.
| table | contents |
|---|---|
| 0x7e771e68 | get_connectmode, switch_cammode, get_caminfo, get_commandlist, get_resizeimg, get_movplaytime, get_rsvimglist, get_imglist, get_thumbnail (browse-only set) |
| 0x7e771f60 | full browse/private set: adds exec_pwoff, clear_resvflg, get_activate, set_utctimediff, get_gpsdivunit, get_unusedcapacity, get_dcffilenum, req_attachexifgps, req_storegpsinfo |
| 0x7e772048 | remote (rec) set: get_connectmode, switch_cammode, get_caminfo, exec_pwoff, get_commandlist, get_imglist, get_thumbnail, + set_takemode, exec_takemotion, exec_takemisc, get_camprop, set_camprop (these five all enter the rec dispatcher 0x7e70b5a8) |
| 0x7e7720d0 | shutter set: get_connectmode, switch_cammode, get_caminfo, exec_pwoff, get_commandlist, exec_shutter, exec_shuttermisc (both enter 0x7e70a0b5) |
Second-level tables: shutter 0x7e780c10 (exec_shutter -> 0x7e70a1be, exec_shuttermisc -> 0x7e70a292); rec 0x7e781500 (set_takemode 0x7e70c0c4, exec_takemotion 0x7e70c17c, exec_takemisc 0x7e70c245, get_camprop 0x7e70bd3c, set_camprop 0x7e70be2a, switch_cammode 0x7e70bef7).

## Errors
`respond_error(0x208, 0x3ec)` = HTTP 520 + `errorcode` 1004 when a command argument is missing/unknown (static RE; not yet seen live).
LIVE (2026-11-01, camera in `private` connect mode): every `get_camprop.cgi?com=get|desc&propname=<any of the 14>` returns HTTP 520 `errorcode` 1001, same as an unknown CGI (`fwup_getversions`). So 1001 = CGI not available in the current connect mode / unsupported; the camprop CGIs are in the rec-mode table (0x7e772048) and need the camera switched to remote/rec mode first (`switch_cammode.cgi?mode=rec`). Confirms the per-mode table design. Later calls in that run got empty replies (camera or link dropped), so only the first 11 properties were queried.

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

## exec_shutter
First level `exec_shutter`/`exec_shuttermisc` wrap the handler in `WIFI_RELEASE_CGI(1)...(0)`. Leaf 0x7e70a1be maps the `com` value (6 strcmp branches) to app events 0x41b0024..0x41b0029 and posts it; HTTP 200 on success. Exact strings per branch not yet resolved (decompiler hides the string args).
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
