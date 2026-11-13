# Initialised-data image in block 0 (E-M10 Mark I, body fw 1.4)

The firmware's initialised variables live in RAM around `0x6044xxxx`–`0x6045xxxx`. Their start-up values are
stored inside block 0 and copied to RAM at start-up, so tables that the code reads "from RAM" can be read
from the firmware file:

**image address = RAM address + `0x1d8b5ec0`**

Found 2026-11-13 from the trace catalog (see [`trace-catalog.md`](trace-catalog.md)): the lookup's top table
at RAM `0x6044e518` maps to image `0x7dd043d8`, whose entries are RAM pointers to group tables that sit in
the image directly after the name lists they index. The relation was checked along that three-level chain
and by the tables below, which all decode to sensible text; it has not been checked for the whole data
section, and the copy routine itself was not looked for. Addresses of the image are runtime addresses of
block 0 (base `0x7d991020`).

## Name tables found in the image

| image | RAM | entries | content | used by |
|---|---|---|---|---|
| `0x7dd03018` | `0x6044d158` | 1195 | API names, see `trace-catalog.md` | `trace_catalog_lookup` `0x7dfc7272` |
| `0x7dd04600` | `0x6044e740` | 57 | state and device words (`START`, `STOP`, `HDMI`, …), listed below | `Execute_7dff2a5d` |
| `0x7dd046e8` | `0x6044e828` | 68 | media and mount-state words (`SD`, `NO_MOUNT`, `PROTECT`, …), listed below | `consume_7dff44e5` |
| `0x7dd04858` | `0x6044e998` | 57 | API class tags (`A**: CameraCommon`, …), listed below | `initializeApi_7dffbd9a` |
| `0x7dd08940` | `0x60452a80` | 185 | GUI event names `ID_EV_*`, listed below | not referenced by address in the code; reached through another pointer |

## GUI event names (`0x7dd08940`)

Index in the table, then the name. Whether the index equals the event code used elsewhere in the GUI was not
established.

| index | name | index | name | index | name |
|---|---|---|---|---|---|
| 0 | `NULL` | 1 | `ID_EV_KEY_UP_ON` | 2 | `ID_EV_KEY_DOWN_ON` |
| 3 | `ID_EV_KEY_LEFT_ON` | 4 | `ID_EV_KEY_RIGHT_ON` | 5 | `ID_EV_KEY_OK_ON` |
| 6 | `ID_EV_KEY_MENU_ON` | 7 | `ID_EV_KEY_DISP_ON` | 8 | `ID_EV_KEY_DISP_OFF` |
| 9 | `ID_EV_SCR_1ST_RELEASE` | 10 | `ID_EV_SCR_2ND_RELEASE` | 11 | `ID_EV_KEY_QV_ON` |
| 12 | `ID_EV_SST_STILL_NORMAL` | 13 | `ID_EV_SST_STILL_PANO` | 14 | `ID_EV_SST_HDMI_DISCONT` |
| 15 | `ID_EV_SST_COMMON` | 16 | `ID_EV_SCR_HISTO_UPDATE` | 17 | `ID_EV_SCR_LOCK_CONDI` |
| 18 | `ID_EV_SCR_REC_START` | 19 | `ID_EV_SCR_ZOOM_BAR` | 20 | `ID_EV_SST_BULB_PROCESS` |
| 21 | `ID_EV_SST_BGN_FUNC_MENU` | 22 | `ID_EV_SST_END_FUNC_MENU` | 23 | `ID_EV_SST_MOVIE_SELF_ST` |
| 24 | `ID_EV_SST_AE_LOCK_END` | 25 | `ID_EV_SST_END_MENU` | 26 | `ID_EV_SCR_UPDATE` |
| 27 | `ID_EV_SCR_BGN_ST_CHARGE` | 28 | `ID_EV_SCR_END_ST_CHARGE` | 29 | `ID_EV_SST_PLAY_SINGLE` |
| 30 | `ID_EV_SST_PLAY_INDEX` | 31 | `ID_EV_SST_PLAY_ENLARGE` | 32 | `ID_EV_SCR_DISPLAY_OFF` |
| 33 | `ID_EV_SST_CARDCOV_OPEN` | 34 | `ID_EV_SST_POWON_DISP` | 35 | `ID_EV_KEY_UP_OFF` |
| 36 | `ID_EV_KEY_DOWN_OFF` | 37 | `ID_EV_KEY_LEFT_OFF` | 38 | `ID_EV_KEY_RIGHT_OFF` |
| 39 | `ID_EV_KEY_OK_OFF` | 40 | `ID_EV_KEY_MENU_OFF` | 41 | `ID_EV_KEY_QV_OFF` |
| 42 | `ID_EV_SCR_BATTERY_CHAN` | 43 | `ID_EV_SCR_CARD_FULL` | 44 | `ID_EV_SCR_SELFTIME` |
| 45 | `ID_EV_KEY_ZOOM_UP_ON` | 46 | `ID_EV_KEY_ZOOM_UP_OFF` | 47 | `ID_EV_KEY_ZOOM_DOWN_ON` |
| 48 | `ID_EV_KEY_ZOOM_DOWN_OFF` | 49 | `ID_EV_SCR_DISP_TIME` | 50 | `ID_EV_SST_SELF_ADJUST` |
| 51 | `ID_EV_SCR_BATTERY_EMP` | 52 | `ID_EV_SCR_DAMAGE` | 53 | `ID_EV_KEY_1ST_RLS_ON` |
| 54 | `ID_EV_KEY_1ST_RLS_OFF` | 55 | `ID_EV_KEY_2ND_RLS_ON` | 56 | `ID_EV_KEY_2ND_RLS_OFF` |
| 57 | `ID_EV_SCR_ONE_MOMENT` | 58 | `ID_EV_SCR_IAUTO_SCN_CHG` | 59 | `ID_EV_SCR_BATTERY` |
| 60 | `ID_EV_SCR_AC_ADPT_CNCT` | 61 | `ID_EV_SCR_AC_ADPT_DCNCT` | 62 | `ID_EV_SST_SPEC_MODE` |
| 63 | `ID_EV_SCR_CARD_SETUP` | 64 | `ID_EV_SST_BGN_LIST_MENU` | 65 | `ID_EV_SST_WZD_SET_TIME` |
| 66 | `ID_EV_SCR_N_AV_WARNING` | 67 | `ID_EV_SCR_USB_SEL` | 68 | `ID_EV_SCR_PRINT_MODE` |
| 69 | `ID_EV_SST_SIMPLE_PRINT` | 70 | `ID_EV_SST_CUSTOM_PRINT` | 71 | `ID_EV_SST_CNCT_FAILED` |
| 72 | `ID_EV_SST_MOVIE_REC` | 73 | `ID_EV_KEY_HELP_ON` | 74 | `ID_EV_KEY_HELP_OFF` |
| 75 | `ID_EV_SST_EXE_STOP` | 76 | `ID_EV_SCR_FC_CHECK_DISP` | 77 | `ID_EV_SST_DISP_MODE_CHG` |
| 78 | `ID_EV_SST_PROGRESS_CHG` | 79 | `ID_EV_SST_PROGRESS_END` | 80 | `ID_EV_SST_MULTI_STA_FSH` |
| 81 | `ID_EV_SST_MULTI_END_FSH` | 82 | `ID_EV_SST_MULTI_MOV_FSH` | 83 | `ID_EV_SCR_ZOOM_BAR_HIDE` |
| 84 | `ID_EV_SCR_PNRM_FRMNG_AT` | 85 | `ID_EV_SCR_JUDGE_DIR` | 86 | `ID_EV_SCR_PNRM_LOCK_TG` |
| 87 | `ID_EV_SCR_PNRM_COMBINE` | 88 | `ID_EV_SCR_PNRM_GUIDE` | 89 | `ID_EV_SCR_PNRM_FRMNG_MN` |
| 90 | `ID_EV_SCR_BT_ANIMA_STA` | 91 | `ID_EV_SCR_BT_ANIMA_END` | 92 | `ID_EV_SCR_BEAUTY_FAIL` |
| 93 | `ID_EV_SCR_SOUND_REC` | 94 | `ID_EV_SST_CHG_OP_HDMI` | 95 | `ID_EV_SST_CHG_OP_VIDEO` |
| 96 | `ID_EV_SST_FACE_CHECK_F` | 97 | `ID_EV_SST_CONTROL_RQST` | 98 | `ID_EV_SST_SAVE_START` |
| 99 | `ID_EV_SST_SAVE_END` | 100 | `ID_EV_SCR_MOVIE_ICON` | 101 | `ID_EV_SCR_STILL_ICON` |
| 102 | `ID_EV_SCR_ATT_INIT` | 103 | `ID_EV_SCR_ATT_WRT_BACK` | 104 | `ID_EV_KEY_MOVIE_ON` |
| 105 | `ID_EV_KEY_MOVIE_OFF` | 106 | `ID_EV_SCR_PC_CONNECTED` | 107 | `ID_EV_SCR_PNRM_DIR_CHG` |
| 108 | `ID_EV_SCR_FLASH_CHARGE` | 109 | `ID_EV_SCR_PNRM_SCRL_STA` | 110 | `ID_EV_SCR_PNRM_SCRL_END` |
| 111 | `ID_EV_SCR_PANO_RCV_STA` | 112 | `ID_EV_SCR_AF_LOCK` | 113 | `ID_EV_SCR_TARGET_AF_STA` |
| 114 | `ID_EV_SCR_USB_DISCNCT` | 115 | `ID_EV_SCR_BTY_CHARGE_CH` | 116 | `ID_EV_KEY_CEC_BLUE` |
| 117 | `ID_EV_KEY_CEC_RED` | 118 | `ID_EV_KEY_CEC_GREEN` | 119 | `ID_EV_KEY_CEC_YELLOW` |
| 120 | `ID_EV_SCR_FORCE_UPDATE` | 121 | `ID_EV_SCR_TARGET_AF_END` | 122 | `ID_EV_SCR_AF_LOCK_FAIL` |
| 123 | `ID_EV_SST_S_F_EV_CHANGE` | 124 | `ID_EV_KEY_CEC_UP` | 125 | `ID_EV_KEY_CEC_DOWN` |
| 126 | `ID_EV_KEY_CEC_LEFT` | 127 | `ID_EV_KEY_CEC_RIGHT` | 128 | `ID_EV_KEY_CEC_OK` |
| 129 | `ID_EV_SCR_BTY_CHARGE_FL` | 130 | `ID_EV_SCR_CARD_PROTECT` | 131 | `ID_EV_SCR_CARD_CANT_USE` |
| 132 | `ID_EV_SST_THROUGH_OK` | 133 | `ID_EV_SST_CEC_START` | 134 | `ID_EV_SST_USB_CNCT` |
| 135 | `ID_EV_SST_FORCE_CHG_OP` | 136 | `ID_EV_SCR_OSD_OFF` | 137 | `ID_EV_SST_TAP_TOP_S` |
| 138 | `ID_EV_SST_TAP_BOTTOM_S` | 139 | `ID_EV_SST_TAP_LEFT_S` | 140 | `ID_EV_SST_TAP_RIGHT_S` |
| 141 | `ID_EV_SST_TAP_BACK_S` | 142 | `ID_EV_SST_TAP_TOP_D` | 143 | `ID_EV_SST_TAP_BOTTOM_D` |
| 144 | `ID_EV_SST_TAP_LEFT_D` | 145 | `ID_EV_SST_TAP_RIGHT_D` | 146 | `ID_EV_SST_TAP_BACK_D` |
| 147 | `ID_EV_SST_TAP_TOP_M` | 148 | `ID_EV_SST_TAP_BOTTOM_M` | 149 | `ID_EV_SST_TAP_LEFT_M` |
| 150 | `ID_EV_SST_TAP_RIGHT_M` | 151 | `ID_EV_SST_TAP_BACK_M` | 152 | `ID_EV_SST_SLOP_DETECT` |
| 153 | `ID_EV_SST_POWER_OFF` | 154 | `ID_EV_SST_PRESSURE_CHG` | 155 | `ID_EV_SST_DEEP_WATER_W` |
| 156 | `ID_EV_SST_HDMI_CNNCT_ER` | 157 | `ID_EV_SST_WIZ_SET_LANG` | 158 | `ID_EV_SST_LV_CTRL_BEG` |
| 159 | `ID_EV_SST_LV_GUIDE_BEG` | 160 | `ID_EV_SST_CR_MENU_BEG` | 161 | `ID_EV_SST_AF_TARGET_SEL` |
| 162 | `ID_EV_SST_STB_SET_D` | 163 | `ID_EV_SST_DRIVE_SET_D` | 164 | `ID_EV_SST_MODE_DIAL_CHG` |
| 165 | `ID_EV_SST_SCN_SEL_WIZ` | 166 | `ID_EV_SST_ART_SEL_WIZ` | 167 | `ID_EV_KEY_JOG_DIAL_CHG` |
| 168 | `ID_EV_KEY_CTRL_RING_CHG` | 169 | `ID_EV_KEY_INFO_ON` | 170 | `ID_EV_KEY_INFO_OFF` |
| 171 | `ID_EV_SST_A_S_E_MENU` | 172 | `ID_EV_SST_STILL_WAIT` | 173 | `ID_EV_SST_EV_SETTING` |
| 174 | `ID_EV_SST_SHUT_SETTING` | 175 | `ID_EV_SST_LENS_CAP_WARN` | 176 | `ID_EV_SST_STILL_MF` |
| 177 | `ID_EV_SST_THROUGH_STOP` | 178 | `ID_EV_SST_JOG_MENU_BGN` | 179 | `ID_EV_SST_ONETOUCH_SHT` |
| 180 | `ID_EV_SST_ONETOUCH_SUC` | 181 | `ID_EV_SST_ONETOUCH_FL` | 182 | `ID_EV_SST_DISA_3S_INFO` |
| 183 | `ID_EV_SST_TAKE_INFO_OFF` | 184 | `ID_EV_SST_CHG_OP_TO_TFT` |  |  |

## API class tags (`0x7dd04858`)

0 `A**: CameraCommon`, 1 `B**: SettingController`, 2 `C**: BackGroundCtrl`, 3 `D**: SoundCtrl`, 4 `E**: DateCtrl`, 5 `F**: MediaCtrl`, 6 `G**: PixelMapping`, 7 `H**: ModeCheck`, 8 `I**: PowerSupplyControl`, 9 `J**: LevelCtrl`, 10 `K**: KeyCtrl`, 11 `L**: TouchPanel`, 12 `M**: Shooting`, 13 `N**: PlayCommon`, 14 `O**: PlaySingleFrame`, 15 `P**: PlayIndex`, 16 `Q**: PlaySelect`, 17 `R**: PlayMovie`, 18 `S**: PlayRecord`, 19 `T**: ReservePrint`, 20 `U**: PlaySlideShow`, 21 `V**: PlaySound`, 22 `W**: PlayCalendar`, 23 `X**: PlayLightBox`, 24 `Y**: EditResize`, 25 `Z**: EditTrimming`, 26 `a**: EditAspect`, 27 `b**: EditColor`, 28 `c**: EditRedEyeAdjust`, 29 `d**: EditShadowAdjust`, 30 `e**: EditBeautyAdjust`, 31 `f**: EditRaw`, 32 `g**: EditImageOverlay`, 33 `h**: SelectOverlay`, 34 `i**: SelfAdjust`, 35 `j**: LifeTest`, 36 `k**: Relocate`, 37 `l**: Maintenance`, 38 `m**: EasyPrint`, 39 `n**: CustomPrint`, 40 `o**: DeviceLink`, 41 `p**: Bluetooth`, 42 `q**: SyetemCommon`, 43 `r**: OSDControl`, 44 `s**: Effect`, 45 `t**: FlashAir`, 46 `u**: OneTouchLight`, 47 `v**: ReserveUpload`, 48 `w**: GpsCtrl`, 49 `x**: PlayContinuousShots`, 50 `y**: ReserveTransfer`, 51 `AB**: LogoScreen`, 52 `AC**: EraseSelectedPic`, 53 `AD**: PlayPanorama`, 54 `AE**: PlayEventView`, 55 `AF**: InternalWiFi`, 56 `AG**: AfFineTune`

## State and device words (`0x7dd04600`)

0 `START`, 1 `STOP`, 2 `UNDEF`, 3 `NORMAL`, 4 `RELEASE`, 5 `RELEASE2`, 6 `WARNING`, 7 `LOCK`, 8 `UNKNOWN`, 9 `UNDEF`, 10 `COMPOSI`, 11 `HDMI`, 12 `EVF_VF2`, 13 `EVF_VF3`, 14 `EVF`, 15 `USB`, 16 `PENPAL`, 17 `EXFLASH`, 18 `MCPHONE`, 19 `PBH`, 20 `CONNECTED`, 21 `DISCONENCTED`, 22 `AUTO `, 23 `INTERNAL `, 24 `EXTERNAL `, 25 `GENERAL `, 26 `GENE2 `, 27 `RC `, 28 `NON `, 29 `UNDEF `, 30 `NO`, 31 `OK`, 32 `UNDEF`, 33 `NONE`, 34 `UNDER`, 35 `OVER`, 36 `NORMAL`, 37 `UNDEF`, 38 `NO`, 39 `OK`, 40 `UNDEF`, 41 `END`, 42 `START`, 43 `UNDEF`, 44 `TAKE_NG `, 45 `MANUAL_SINK `, 46 `ELECTR_SINK `, 47 `STEP_OUT `, 48 `ACTUATOR `, 49 `LV_BAN `, 50 `3D_LENS `, 51 `3D_DISABLE `, 52 `UNDEF`, 53 `ERROR`, 54 `SINGLE`, 55 `ZOOM`, 56 `UNDEF`

## Media and mount-state words (`0x7dd046e8`)

0 `SD`, 1 `CUBE`, 2 `IN`, 3 `UNDEF`, 4 `MEDIA_SD_CARD`, 5 `MEDIA_EXTERNAL`, 6 `MEDIA_INTERNAL`, 7 `UNDEF`, 8 `NO_MOUNT`, 9 `COVER_OPEN`, 10 `NOT_PRESENT`, 11 `UNFORMAT`, 12 `ERROR`, 13 `PROTECT`, 14 `DATA_PROTECT`, 15 `OK`, 16 `UNKNOWN`, 17 `UNMOUNTED`, 18 `MOUNTING`, 19 `REC`, 20 `PLAY`, 21 `MOUNTED`, 22 `NON`, 23 `JPEG`, 24 `TIFF`, 25 `RAW`, 26 `MOVIE`, 27 `RAW_JPEG`, 28 `DPS`, 29 `SLPIC`, 30 `MPO_JPEG`, 31 `MPO`, 32 `AVCHD`, 33 `UNDEF`, 34 `NON`, 35 `JPEG`, 36 `TIFF`, 37 `RAW`, 38 `MOVIE`, 39 `RAW_JPEG`, 40 `DPS`, 41 `SLPIC`, 42 `MPO_JPEG`, 43 `MPO`, 44 `AVCHD`, 45 `UNDEF`, 46 `BODY`, 47 `PBH`, 48 `AC`, 49 `UNDEF`, 50 `UNKNOWN`, 51 `HIGH`, 52 `MIDDLE`, 53 `LOW`, 54 `EMPTY`, 55 `UNDEF`, 56 `UNKNOWN`, 57 `BODY->PBH`, 58 `PBH->BODY`, 59 `UNDEF`, 60 `END`, 61 `RECORD`, 62 `PLAY`, 63 `PRINT`, 64 `PC`, 65 `MOVIE`, 66 `BTRECOVER`, 67 `UNDEF`
