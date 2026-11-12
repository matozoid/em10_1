# Issue list

Everything we could do next for the app, the Wi-Fi client and possible firmware modifications, with a
proposed priority. Reverse-engineering and housekeeping tasks are tracked in `STATUS.md`, not here.

**How to use it:** change the `P` (priority) column to re-rank; set `Status` as work moves; add rows at
the end of a section with the next free id. Ids never change, so commits and notes can refer to them.

| column | values |
|---|---|
| P | 1 = do next, 2 = soon, 3 = later, – = parked |
| Value | high / med / low: how much it improves what the camera owner can do |
| Effort | S = hours, M = a day or two, L = a week or more |
| Risk | what it does to the real camera: **none** (no camera needed), **read** (read-only requests), **state** (changes mode or settings, or takes pictures), **flash** (needs modified firmware on the camera) |
| Status | open, blocked (see Depends), parked, done |

Ground rules that shape the priorities: there is one camera, the body is never opened, and no modified
firmware is flashed. Every **flash** item is therefore parked as an idea; its research steps are not.

## Proposed order

1. **C1, C2** — first live run of the client, read-only. Everything on the Wi-Fi side depends on it.
2. **C3, C5** — live run of the state-changing commands, then "save to computer after each shot".
3. **A8** — show the installed firmware version, so the update flow can say "you are up to date".
4. **C8** — a live-view window; it unlocks most of the tethering features.
5. **A1** — move the Wi-Fi client into the app's shared code once C1–C3 have confirmed the protocol.
6. **M0** — find out on paper whether the firmware already contains unused Wi-Fi features.
7. **A3, A4** — the two big user-facing screens: import and remote control.

## Wi-Fi client (`tools/emcam.py`)

| Id | P | Issue | Value | Effort | Risk | Depends | Status |
|---|---|---|---|---|---|---|---|
| C1 | 1 | Live test of the read-only commands on the E-M10: `info`, `ls -r`, `get`, `thumb`, `resize`, `pull` | high | S | read | camera on Wi-Fi | open |
| C2 | 1 | Capture the real `get_unusedcapacity` reply and parse it into bytes | low | S | read | C1 | open |
| C3 | 1 | Live test of `mode`, `props`, `prop`, `set`, `shoot`, `liveview` | high | S | state | C1 | open |
| C5 | 1 | Save to computer after each shot (`exec_takemisc` `getlastjpg` / `getrecview`) | high | S | state | C3 | open |
| C8 | 2 | Live-view window instead of saving frames (local web page served by the client) | high | M | state | C3 | open |
| C4 | 2 | Touch autofocus: `focus X Y` using `assignafframe` / `takeready`, report focus ok and frame position | med | S | state | C3 | open |
| C18 | 2 | Join the camera's Wi-Fi and return to the home network from the client (today a separate shell script) | med | S | none | – | open |
| C6 | 2 | Time lapse: N shots at an interval, each saved to the computer | med | S | state | C5 | open |
| C7 | 3 | Exposure bracketing from the computer (change `expcomp` between shots) | med | S | state | C3 | open |
| C9 | 3 | Live-view aids computed on the computer: histogram, highlight and shadow warning, focus peaking | med | M | state | C8 | open |
| C17 | 3 | Long exposures through `exec_takemotion` `starttake` / `stoptake` (bulb, live time); parameter values untested | med | M | state | C3 | open |
| C10 | 3 | Draw the AF and face frames carried in the live-view stream (packet types 108–115) | low | M | state | C8 | open |
| C11 | 3 | Limit the aperture list to the attached lens (read from a picture's EXIF) | low | S | read | C1 | open |
| C16 | 3 | Power-zoom control (`ctrlzoom`), for lenses that support it | low | S | state | C3 | open |
| C15 | 3 | Share order: list the pictures marked for transfer, download them, clear the marks | low | S | state | C1 | open |
| C14 | 3 | Set the camera's time zone offset (`set_utctimediff`) | low | S | state | C3 | open |
| C12 | 3 | Second-monitor / webcam output of the live view | low | M | state | C8 | open |
| C13 | 3 | Write GPS positions into pictures (`req_attachexifgps`, `req_storegpsinfo`); field layout not yet decoded | low | M | state | C3 | open |

## App (`app/`, Kotlin Multiplatform)

| Id | P | Issue | Value | Effort | Risk | Depends | Status |
|---|---|---|---|---|---|---|---|
| A0 | – | Milestone 1: query the update server, download, verify, copy the official file to a card (command line) | high | M | none | – | done |
| A8 | 1 | Show the installed firmware version: read it from the EXIF of any picture (downloaded over Wi-Fi or from a card), compare with the server | high | S | read | – | open |
| A1 | 2 | Wi-Fi camera client in the shared core, behind the transport interface; port of `emcam.py` | high | M | none | C1, C3 | blocked |
| A9 | 2 | Find mounted memory cards, check free space and file system before writing the update file | med | M | none | – | open |
| A2 | 2 | Desktop window for the firmware flow (check, download, verify, write to card, on-camera steps) | med | M | none | A8, A9 | open |
| A3 | 2 | Import screen: thumbnail grid, select or "all new", download with progress | high | L | read | A1 | blocked |
| A4 | 2 | Remote-control screen: live view, settings panel, shutter, touch AF | high | L | state | A1, C8 | blocked |
| A10 | 3 | Build on Java 21–25 as well as 27, continuous build, installable packages | low | M | none | – | open |
| A5 | 3 | Android target (needs the Android SDK installed) | med | L | none | A1 | blocked |
| A7 | 3 | USB transport for import and device info (standard PTP/MTP). Camera control over USB is limited on this body to its own 18 vendor operations | med | L | read | – | open |
| A11 | 3 | RAW (ORF) preview and metadata, using `docs/workspace/orf-format.md` | low | L | none | – | open |
| A6 | 3 | iOS target (needs a Mac; Wi-Fi features only) | low | L | none | A1 | blocked |

## Firmware modification ideas

Nothing here is flashed. Rows with risk **flash** are ideas to weigh; rows with risk **none** are the
paper research that would tell us what such a modification would involve.

| Id | P | Issue | Value | Effort | Risk | Depends | Status |
|---|---|---|---|---|---|---|---|
| M0 | 2 | Research: does the E-M10 firmware contain unused Wi-Fi handlers that the E-M1 exposes (movie start/stop, `get_screennail`, more properties)? Decides whether M1–M3 are small switches or new code | high | M | none | – | open |
| M10 | 3 | Research: a build setup for patch code (assembler and linker scripts for code placed in the free area of block 0, checked against the "never patch" list) | med | M | none | – | open |
| M11 | 3 | Research: the open flash-safety questions in `STATUS.md` (what selects the card update at power-on, recovery after a failed write). Prerequisite for ever un-parking a flash item | high | L | none | – | open |
| M1 | – | Movie start and stop over Wi-Fi (the E-M1 has `startmovietake` / `stopmovietake`) | med | ? | flash | M0 | parked |
| M3 | – | More remote properties over Wi-Fi: AF area, picture mode and others the E-M10 leaves out | med | ? | flash | M0 | parked |
| M4 | – | Battery level over Wi-Fi (neither the E-M10 nor the E-M1 offers it) | med | L | flash | M10 | parked |
| M5 | – | Aperture-ring support for lenses with a ring (community "ring-native" patch). Image is built and verified locally; never run on a real E-M10 | med | S | flash | M11 | parked |
| M2 | – | Screen-size previews (`get_screennail`) for faster browsing | low | ? | flash | M0 | parked |
| M6 | – | Community feature patches: shutter sound, fonts, language | low | S | flash | M11 | parked |
| M7 | – | Copy the factory pictures stored in flash to the memory card | low | L | flash | M10, M11 | parked |
| M9 | – | Offer patched-firmware builds in the app (port of `tools/fwpatch.py`), only after a patched image has been proven on the real camera | low | M | flash | M5 | parked |
