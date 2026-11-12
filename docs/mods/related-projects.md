# Related projects (checked 2026-11-12)

Other people's work on Olympus / OM System cameras that bears on this project. Read as references; what
each licence allows is noted. Nothing from them is copied into this repository.

## Caduceus for OM-3 — `github.com/androidfanman/caduceus-om3` (Apache-2.0)
Firmware patches for the OM SYSTEM OM-3 (firmware 1.1): 20 "film" picture modes, an on-camera colour
editor, and a browser tool (the "Control Panel" / Look Lab at
`androidfanman.github.io/caduceus-om3/looklab/`) that designs looks and saves them as a file for the card.
Camera-tested releases, v0.27.1 on 2026-11-11. Built on the sister project below.

Why it matters here:
- **Same processor family and same update mechanism as the E-M10 Mark I.** The OM-3 (2025) still runs
  MN10300 / AM33 code, its update file is the same block container, and it is installed the same way:
  `DCOLYMP/E<model>9999.BIN` on the card, **hold OK while switching on**. Their notes list this as proven
  on the camera, in both directions (patched firmware and back to the official file).
- **What the update looks like on the camera (OM-3):** the light stays on steadily for about two minutes
  while writing, then blinks when finished. If it blinks straight away with no steady phase, the camera
  did not accept the file and nothing changed.
- **A working method for patch code:** MN10300 assembly built with binutils for `mn10300-elf` and a linker
  script, placed in unused space at the end of code sections, entered through short hooks; a user-side
  patcher in plain Python that applies only the project's own bytes to the official file the user
  downloads, refuses any other input, and checks the result against an expected checksum. Extra code and
  data are loaded from files on the card at run time, so most changes need no new flash.
- **A safety practice:** every change is run in an emulator (below) before it goes on a camera, and the
  installer keeps a restore copy of the official firmware.
- **A debugging aid:** an optional file on the card switches on a log that the patched firmware writes back
  to the card.

Limits for us: their addresses, hooks and features are for the OM-3's much newer firmware. The picture
pipeline they edit (colour profiles, grain, split toning) may not exist in the same form on a 2014 body.
The methods transfer; the patches do not.

## Caduceus for E-P7 — `github.com/cakelesscoder/caduceus-ep7` (Apache-2.0)
The original project: firmware mods for the PEN E-P7 (film simulations, HSL, grain, bloom, clarity, log
video, extra aspect ratios). Not examined in detail yet. Closer in age to the E-M10 than the OM-3 is, so
its porting notes may be the better starting point.

## OM-Emu — `github.com/flatpanda/om-emu` (no licence file seen)
An emulator "lab" in JavaScript (Node 26 or a browser) that runs Olympus / OM System MN10300 firmware
outside the camera: it emulates the CPU and the devices the user interface needs, runs the firmware's own
kernel, GUI and camera application, and shows the camera's screens. It does not boot from reset, and the
sensor, autofocus, release and movie modules are stand-ins. It can apply a patch overlay in memory, and has
a debug interface (registers, memory, breakpoints, traces).

- Reference body OM-1; ports for about 20 others, including the **E-M10 II, III and IV** and the E-M5 II.
- **The original E-M10 is listed among "14 older bodies … surveyed, not tried"** (as of 2026-11-02).
- No licence is stated, so its code cannot be reused here, but it can be used as a tool.

Why it matters: it is the missing piece for testing a patch without the camera. A port for the E-M10
Mark I would let menu-level changes be exercised and traced in the emulator. It would not prove the
update process itself or anything involving the sensor, lens or card hardware.

## omcap — `github.com/HolmHaensel/omcap` (GPL-3)
Wi-Fi and USB tethering for the E-M1 Mark I. Covered in `../usb-protocol/wifi-api.md`.

## What this changes for our open questions
- "Is hold-OK-at-power-on a real card update path?" On the OM-3 and E-P7 it is, and publicly documented
  with the same folder and file naming our firmware scans for. Together with the owner's observation that
  only OK delays start-up on the E-M10, the path very likely exists on this body too. It is still untested
  here, and what selects it inside our firmware is still not located.
- "Is recovery possible after a bad patch?" Their experience is that a misbehaving patch is undone by
  flashing the official file the same way, and that an interrupted write can leave a camera unable to start.
  That matches our own analysis and does not remove the risk for a single body.
- The no-flash rule in `STATUS.md` stands. These projects make the research items in `ISSUES.md` (M0, M10,
  M11) more tractable; they do not make a first flash safe.
