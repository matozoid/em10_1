# Block 0 memory map and analysis setup

**Runtime address = load address + 0x3d691020.** Block 0 is staged at 0x40300000 but runs relocated: file offset 0 = runtime `0x7d991020` (= `runtime_base` in the community profile). VERIFIED: with this base 2315 of 3000 sampled strings have matching absolute pointers in code; with the load address 0 do.
Relative `jmp`/`call` are unaffected. Community patch offsets and addresses in `STATUS.md` hook table are in load space; add 0x3d691020 for Ghidra.

Ghidra project (`research/ghidra_proj`, program `blk00_40300000.bin`) now imported at base `0x7d991020`: 72,580 functions, 10,763 reference strings.

Absolute-address regions seen in code operands (instruction count per 1 MB bucket, `tools/ghidra/ImmHist.java`):
| range | likely |
|---|---|
| 0x7cc00000-0x7e900000 | this image (code, rodata) |
| 0x60400000-0x60a00000 | RAM variables/bss (cached) |
| 0xa0900000-0xa0b00000 | RAM alias (uncached?) e.g. pointer_cell 0xa0a5c970 |
| 0xbd9b.... | I/O registers seen in hook payload (UNVERIFIED) |
| 0x80000000, 0x8ff00000, 0x99400000, 0x9a000000-0x9e000000 | unidentified (peripherals/DMA?) |

## Subsystems by log tag (`tools/subsystems.py`)
GUI, APPEVENT_STATE/CAMST/CAMON/PWR/TIMER (camera state machine), iseq_ps_* (image sequencer: still/through/recview/update/mng), exp (exposure), api_* (layered API: disp, rec, play, picfile, dps, network_Wifi, histogram, tft, oldb, adj, cube), rec_ImgPro*, RecView, CapThr, Cap_PlayMovie, movplay_com, app_panorama, app_background, GuiTouch, DevBlu_Bluetooth, WIFI_REMOCON_CGI/UTL, WIFI_RELEASE, do_cgi_get, AVM_FILE_MAIN/AVM_API, API_MEDIA(_SD), aud_dev_wm8946 (audio codec), PER_ADCONV, FLASH.

## Auto-naming
`tools/ghidra/NameFuncs.java` renamed ~9.3k functions (10k+ with C++ pass) from referenced strings; see `classes.md`. Re-runnable (touches only `FUN_*` and `*_<8hex>` names). Output TSVs in `research/decomp/names_pass*.tsv` (gitignored). The Ghidra project itself is not committed; recreate with the steps in `STATUS.md` + this file.
