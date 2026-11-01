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
