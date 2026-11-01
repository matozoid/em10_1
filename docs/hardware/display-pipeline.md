# Display pipeline (from block 0 debug strings, 0x7dc70800-0x7dc72200)

Source: strings in the debug-console region of block 0. Not verified on hardware.

## Structure
- A dedicated **display ASIC / engine** ("I43" driver prefix: `I43_ConfigVideoOutput`, `I43DM_*`) sits behind a
  `DISPLAY` task (0x7dbaa6a0, with `DISPLAY_TIMER`, `DISP_FRAME`, `DISP_ADJ_EXT_PORT`, `DISP_ADJ_OUTPUT_DEVICE_CONTROL`).
  The main CPU posts commands to it; it does not draw pixels itself (see `resources.md`).
- Command set shown by the "display process queue state" dump: FASTBOOT, OPEN, CLOSE, SET_CPDATA, UPD_SCRN, L_CSTM,
  BRIGHTNESS, QUALITY, SET_HISH/EXE_HISH, ADJ_CONTTFT, ADJ_TFT_SET, HIST_SET/START/STOP/CALC_E, **UPD_OSD, UPD_IMG**,
  STATIC_ELEC, ALC/ALC_RUN/ALC_STOP, COLORTEMP, ADJ_EXT, DUMMY_OPEN, TFT_SWIVEL, COLOR_MODE, L_CSTM_V, ADJ_OUT_DEV,
  AUTO_DIMMER, CHG_FAST. Queue stages INIT / EXEC / POST. State dump also prints "last update img hd", "last through
  flg", and update buffer addresses **O1addr / O2addr / O3addr** (one image + OSD layer buffers).
- Debug console commands: `[layer]` (`I43DM_DISABLE=0, IMAGE_ONLY=1, OSD_ONLY=2, ENABLE=3, FREEZE=4, UNFREEZE=5,
  DISPLAY_ON=6, DISPLAY_OFF=7`; OSD 1st layer ("shita", lower) off = 0x10, 2nd ("ue", upper) off = 0x20), `[sio]` (2-byte
  serial I/O to the panel), `[i2c]` (HDMI tx/rx IC), `[histogram]`, `[crot]` (colour rotation matrix, Y/CB/CR),
  `[hd]` HDMI info/CEC, `[powerdown]` (tft/touchpanel), `[DISP]` tft duty, `[GAMMA]`, `[LPF]`.
- **Two OSD planes** (`API_OSD_PLANE_LAYER1/2` strings at 0x7e3a0dc3).
- Output devices: `tft | oled | evf | bievf` (rear LCD, OLED, external EVF, built-in EVF), NTSC/PAL, HDMI
  480p/576p/720p50/60/1080i50/60/1080p50/60. EDID parsing incl. deep colour, 3D, CEC.
- Version queries: "asic gamma ver", "backpanel Version", "vf-2/vf-3 Version", "Built In EVF Version" (R2229-02),
  "automatic dimmer duty<->bl curve version"; commands `boot_exit`, `boot_on`, `get_fwv`, `get_info`, `get_sts`.
  The ASIC (or its sub-ICs) therefore carries its own firmware/config, probably loaded or flashed by the main CPU.

## Implications
- Icon records with `hdr[3]` 2/3 are likely the ASIC's OSD pixel formats; decoding happens in hardware.
- OSD output is two layers + image layer composited by the ASIC; "UPD_OSD" carries the buffer address.
- Next: find where the main CPU writes/loads ASIC firmware or parameter tables (search `boot_on`, `get_fwv`
  handlers) - an ASIC firmware image inside the BIN would explain the format selector.

## Update: debug-console `boot_on/boot_exit/get_fwv` (handler 0x7dbafe95)
These are register-level I2C accessors for a peripheral IC (calls `FUN_7dbbca26(0x48, reg)` / `FUN_7dbbcafe(0x48, ..)`,
register 0x1c "ADDR High 1Ch"), i.e. the HDMI/EVF transceiver, not a loader for the display ASIC. No code found that
uploads firmware to the display ASIC; `FASTBOOT` (0x7dbaf3d3) only posts SET_CPDATA/UPD_OSD style commands. Working
assumption: the ASIC runs mask-ROM or separately stored firmware, so the icon pixel formats are not decodable from
this BIN by code analysis. Remaining route: blind decoding of the second format.
