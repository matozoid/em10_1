# Trace catalog: API names by trace id (E-M10 Mark I, body fw 1.4)

The API layer of the firmware logs every call as `Name(args)` and `RET: …`. The name comes from
`trace_catalog_lookup` `0x7dfc7272`, which splits a three-byte id into category, group and item and walks
three pointer tables starting at RAM `0x6044e518`. Earlier notes called this a dead end because the tables
are in RAM. They are, but RAM is filled at start-up from an image inside the code block, and the image can
be read directly:

- image address = RAM address + `0x1d8b5ec0` (found by matching the first group table pointer `0x6044d158`
  to the name-pointer list at `0x7dd03018`, and confirmed: the top table then lands on `0x7dd043d8` and
  its first entry points at the group table that follows the name lists);
- `name(id) = string(image[image[image[top + 4·(cat−1)] + 4·(group−1)] + 4·(item−1)])`.

Category 1 is common services, 2 shooting, 3 playback, 4 adjustment and maintenance, 5 connectivity and
printing (from the classes found in each). 1195 names in 70 classes are listed below. The address column gives
the function that logs the id, where one was found. Most ids have two: the public entry function and the implementation behind it, both of which log the call (876 ids); the others are
not logged from a place the scan recognised (id not loaded as a constant right before the call), or are unused.
Names that concern firmware update or the debug channel are left out of this list, as are `T.B.D.` placeholders.

Regenerate with the scan described in `symbol-strings.md` (Pass 4); the numbers come from block 0 only.

## API class vtables

The public entry functions of one API class are the members of one vtable. Matching the names above against
the vtable member rows in `symbol-families.md` (`cls_<vtable>__vfn<N>_…`) gives the class of 47 vtables;
every one of them has members of a single class only. `named` counts the members that log a trace id.

| vtable | API class | members | named |
|---|---|---|---|
| `0x7e3a3b60` | `BackGroundCtrl` | 6 | 4 |
| `0x7e3a3b90` | `Bluetooth` | 35 | 34 |
| `0x7e3860a0` | `CameraCommon` | 72 | 70 |
| `0x7e3a3c30` | `CustomPrint` | 36 | 32 |
| `0x7e3a3cd0` | `DateCtrl` | 13 | 12 |
| `0x7e3a3d0c` | `DeviceLink` | 5 | 4 |
| `0x7e3a3d28` | `EasyPrint` | 11 | 10 |
| `0x7e3a3d5c` | `EditAspect` | 8 | 7 |
| `0x7e3a3d88` | `EditBeautyAdjust` | 7 | 6 |
| `0x7e3a3dbc` | `EditColor` | 6 | 4 |
| `0x7e3a3de8` | `EditImageOverlay` | 15 | 12 |
| `0x7e3a3e48` | `EditRaw` | 14 | 13 |
| `0x7e3a3e88` | `EditRedEyeAdjust` | 6 | 5 |
| `0x7e3a3ea8` | `EditResize` | 6 | 5 |
| `0x7e3a3ec8` | `EditShadowAdjust` | 6 | 5 |
| `0x7e3a3ee8` | `EditTrimming` | 10 | 9 |
| `0x7e3a3f3c` | `FlashAir` | 13 | 12 |
| `0x7e3a3f78` | `GpsCtrl` | 32 | 18 |
| `0x7e3a4010` | `InternalWiFi` | 12 | 10 |
| `0x7e3a4078` | `KeyCtrl` | 11 | 9 |
| `0x7e3a40c4` | `LevelCtrl` | 7 | 6 |
| `0x7e3a40f0` | `LifeTest` | 6 | 4 |
| `0x7e3a4108` | `LogoScreen` | 5 | 4 |
| `0x7e3861c8` | `Maintenance` | 6 | 5 |
| `0x7e386238` | `MediaCtrl` | 22 | 21 |
| `0x7e3a411c` | `OnetouchLightCtrl` | 4 | 3 |
| `0x7e3a414c` | `PlayCalendar` | 10 | 6 |
| `0x7e3a4194` | `PlayCommon` | 19 | 18 |
| `0x7e3a4214` | `PlayEventView` | 7 | 5 |
| `0x7e3a4254` | `PlayIndex` | 21 | 15 |
| `0x7e3a42bc` | `PlayLightBox` | 17 | 15 |
| `0x7e3a4308` | `PlayMovie` | 11 | 10 |
| `0x7e3a4334` | `PlayPanorama` | 10 | 8 |
| `0x7e3a435c` | `PlayRecord` | 6 | 5 |
| `0x7e3a4388` | `PlaySelect` | 14 | 11 |
| `0x7e3a43e4` | `PlaySingleFrame` | 30 | 27 |
| `0x7e3a4490` | `PlaySlideShow` | 10 | 9 |
| `0x7e3a44cc` | `PlaySound` | 5 | 4 |
| `0x7e3862d0` | `PowerSupplyControl` | 8 | 7 |
| `0x7e3a4500` | `ReservePrint` | 16 | 15 |
| `0x7e3a4544` | `ReserveTransfer` | 13 | 10 |
| `0x7e3a4578` | `ReserveUpload` | 4 | 3 |
| `0x7e3a459c` | `SelectOverlay` | 9 | 7 |
| `0x7e3a45d4` | `SelfAdjust` | 24 | 21 |
| `0x7e3a472c` | `SettingController` | 34 | 30 |
| `0x7e3a4b7c` | `SoundCtrl` | 12 | 11 |
| `0x7e3a4bc0` | `TouchPanel` | 8 | 7 |

`Shooting`, the largest class, is not in this list: its entry functions are not members of one such vtable
(only one member of `0x7e3a4890` logs a `Shooting` id).

## Names by id

| id | name | entry function |
|---|---|---|
| `0x10101` | `CameraCommon::initializeApi` | `0x7dff5ac5`, `0x7dffcd9b` |
| `0x10102` | `CameraCommon::shutDown` | `0x7dff5c1b`, `0x7dffcdd0` |
| `0x10103` | `CameraCommon::startSleep` | `0x7dff5cf0`, `0x7dffced4` |
| `0x10104` | `CameraCommon::retractLens` | `0x7dff5bae`, `0x7dffcf03` |
| `0x10105` | `CameraCommon::changeOutLine` | `0x7dff57b0`, `0x7dffcf4d` |
| `0x10106` | `CameraCommon::getDisplayDeviceState` | `0x7dff5877`, `0x7dffcff8` |
| `0x10107` | `CameraCommon::setTapDetect` | `0x7dff6b99` |
| `0x10108` | `CameraCommon::getWakeUpIssue` | `0x7dff5a67`, `0x7dffd181` |
| `0x10109` | `CameraCommon::getUsbState` | `0x7dff5a09`, `0x7dffd561` |
| `0x1010a` | `CameraCommon::getCompositeState` | `0x7dff5819`, `0x7dffd5ab` |
| `0x1010b` | `CameraCommon::getHdmiState` | `0x7dff58e4`, `0x7dffd5f5` |
| `0x1010c` | `CameraCommon::getCardCoverState` | — |
| `0x1010d` | `CameraCommon::getFlashInfo` | `0x7dff5f4f`, `0x7dffd7d7` |
| `0x1010e` | `CameraCommon::getKeyState` | `0x7dff5942` |
| `0x1010f` | `CameraCommon::getModeDialState` | `0x7dff59ab`, `0x7dffd913` |
| `0x10110` | `CameraCommon::isDepthWarningState` | `0x7dff6a6f` |
| `0x10111` | `CameraCommon::getPressureState` | `0x7dff6a26` |
| `0x10112` | `CameraCommon::startSaveLcd` | `0x7dff5c84`, `0x7dffd404` |
| `0x10113` | `CameraCommon::endSaveLcd` | `0x7dff5d4e`, `0x7dffd493` |
| `0x10114` | `CameraCommon::isMirrorSetup` | `0x7dff5b32`, `0x7dffdb6d` |
| `0x10115` | `CameraCommon::getSleepWakeupIssue` | `0x7dff5dac`, `0x7dffd25c` |
| `0x10116` | `CameraCommon::getSlopeState` | `0x7dff6b51` |
| `0x10117` | `CameraCommon::ctrlLcdBoost` | `0x7dff663c` |
| `0x10118` | `CameraCommon::isCecConnect` | `0x7dff5e17`, `0x7dffd771` |
| `0x10119` | `CameraCommon::getDisplaySupport3D` | `0x7dff61fe`, `0x7dffd7a4` |
| `0x1011a` | `CameraCommon::startPressureAdjust` | `0x7dff6846` |
| `0x1011b` | `CameraCommon::getPressureAdjustValue` | `0x7dff6982` |
| `0x1011c` | `CameraCommon::upPressureAdjustValue` | `0x7dff65e7` |
| `0x1011d` | `CameraCommon::downPressureAdjustValue` | `0x7dff6756` |
| `0x1011e` | `CameraCommon::setPressureAdjustValue` | `0x7dff689a` |
| `0x1011f` | `CameraCommon::turnOnSlopeSensor` | `0x7dff6b07` |
| `0x10120` | `CameraCommon::turnOffSlopeSensor` | `0x7dff6abe` |
| `0x10121` | `CameraCommon::getAltitudeDepth` | `0x7dff66ee` |
| `0x10122` | `CameraCommon::getEvfState` | `0x7dff5ee5`, `0x7dffd63f` |
| `0x10123` | `CameraCommon::getJogDialState` | `0x7dff5e7a`, `0x7dffda2c` |
| `0x10124` | `CameraCommon::getCtrlRingState` | — |
| `0x10125` | `CameraCommon::getEyeFiStatus` | `0x7dff5fb9`, `0x7dffdbdd` |
| `0x10126` | `CameraCommon::startHighlightShadow` | `0x7dff613c`, `0x7dffdc65` |
| `0x10127` | `CameraCommon::endHighlightShadow` | `0x7dff60de`, `0x7dffddb3` |
| `0x10128` | `CameraCommon::getTemperatureState` | `0x7dff61a0`, `0x7dffdde6` |
| `0x10129` | `CameraCommon::ctrlLcdBacklight` | `0x7dff6017`, `0x7dffd4c2` |
| `0x1012a` | `CameraCommon::setSleepTimer` | — |
| `0x1012b` | `CameraCommon::getSleepTimer` | — |
| `0x1012c` | `CameraCommon::getPenpalState` | `0x7dff6080`, `0x7dffd727` |
| `0x1012d` | `CameraCommon::setDispSync` | `0x7dff6261`, `0x7dffde4a` |
| `0x1012e` | `CameraCommon::getISStatus` | `0x7dff62ca`, `0x7dffdeee` |
| `0x1012f` | `CameraCommon::setModeDialState` | `0x7dff6328`, `0x7dffdf46` |
| `0x10130` | `CameraCommon::getHlsStateS32S38S39` | — |
| `0x10131` | `CameraCommon::setHlsStateS32S38S39` | — |
| `0x10132` | `CameraCommon::getDispSync` | `0x7dff6391`, `0x7dffdfc0` |
| `0x10133` | `CameraCommon::cancelDispSync` | `0x7dff63f4`, `0x7dffdff3` |
| `0x10134` | `CameraCommon::getEyeSensorState` | `0x7dff6522`, `0x7dffe026` |
| `0x10135` | `CameraCommon::ctrlAutoThrough` | `0x7dff64ba`, `0x7dffe05a` |
| `0x10136` | `CameraCommon::ctrlEyeSensor` | `0x7dff6452`, `0x7dffe0d7` |
| `0x10137` | `CameraCommon::getHlsStateS0036` | — |
| `0x10138` | `CameraCommon::setHlsStateS0036` | — |
| `0x10139` | `CameraCommon::getMonitorRotateStatus` | `0x7dff6585`, `0x7dff67f5`, `0x7dffe154` |
| `0x1013a` | `CameraCommon::startPressureSensor` | `0x7dff6938` |
| `0x1013b` | `CameraCommon::endPressureSensor` | `0x7dff66a5` |
| `0x1013c` | `CameraCommon::startRotateSensor` | `0x7dff67ab` |
| `0x1013d` | `CameraCommon::endRotateSensor` | `0x7dff68ef` |
| `0x1013e` | `CameraCommon::canCoverOpenWarning` | `0x7dff69d7` |
| `0x1013f` | `CameraCommon::isWaterIn` | `0x7dff6bee` |
| `0x10140` | `CameraCommon::getLeverSwitchState` | `0x7dff6c9e`, `0x7dffe27f` |
| `0x10141` | `CameraCommon::changeFunctionButton` | `0x7dff6cfc`, `0x7dffe2d4` |
| `0x10142` | `CameraCommon::getChangeFunctionButton` | `0x7dff6d65`, `0x7dffe368` |
| `0x10143` | `CameraCommon::getDepthStatus` | `0x7dff6c3d` |
| `0x10144` | `CameraCommon::getMonitorLiftStatus` | `0x7dff6e2e`, `0x7dffe81b` |
| `0x10145` | `CameraCommon::getRCCommanderInfo` | `0x7dff6dce`, `0x7dffe75b` |
| `0x10146` | `CameraCommon::getEyeSensorExternalState` | `0x7dff6e8e`, `0x7dffe6aa` |
| `0x10147` | `CameraCommon::ctrlExternalEyeSensor` | `0x7dff6ef1`, `0x7dffe6de` |
| `0x10148` | `CameraCommon::getLensMfSwitchState` | `0x7dff6f5e`, `0x7dffe8ac` |
| `0x10149` | `CameraCommon::getCtrlAutoThrough` | `0x7dff6fbc`, `0x7dffe878` |
| `0x1014a` | `CameraCommon::isEZoomEnable` | `0x7dff701f`, `0x7dffe8da` |
| `0x1014b` | `CameraCommon::isChangeOutLineEnable` | `0x7dff7082`, `0x7dffe956` |
| `0x1014c` | `CameraCommon::getMicType` | — |
| `0x1014d` | `CameraCommon::isGpsProcessing` | `0x7dff70e0`, `0x7dffe984` |
| `0x1014e` | `CameraCommon::isOwnEZoomLens` | `0x7dff7143`, `0x7dffe90e` |
| `0x10201` | `SettingController::registerConflictTable` | — |
| `0x10202` | `SettingController::setSetting` | `0x7dffe9b2`, `0x7e02f92b` |
| `0x10203` | `SettingController::getSetting` | `0x7dffeaa0` |
| `0x10204` | `SettingController::isEnabled` | `0x7dffedab`, `0x7e02f2de` |
| `0x10205` | `SettingController::getSettingCount` | `0x7dffee2a`, `0x7e02f05e` |
| `0x10206` | `SettingController::getSettingValue` | `0x7dffeea4`, `0x7e02f287` |
| `0x10207` | `SettingController::getSettingIndex` | `0x7dffef34`, `0x7e02f1a6` |
| `0x10208` | `SettingController::canSettingValue` | `0x7dffefc4`, `0x7e02ece4` |
| `0x10209` | `SettingController::resetSetting` | `0x7dfff059`, `0x7e02f762` |
| `0x1020a` | `SettingController::resetFactorySetting` | `0x7dfff0eb`, `0x7e02f658` |
| `0x1020b` | `SettingController::loadLanguageData` | `0x7dfff252`, `0x7e02f3fd` |
| `0x1020c` | `SettingController::loadLanguageHeader` | `0x7dfff114`, `0x7e02f473` |
| `0x1020d` | `SettingController::setSettingDetail` | `0x7dffeb32`, `0x7e02fb10` |
| `0x1020e` | `SettingController::getSettingDetail` | `0x7dffebcd`, `0x7e02f0e0`, `0x7e02f12b` |
| `0x1020f` | `SettingController::registerCallback` | `0x7dfff37a`, `0x7e02f5f3` |
| `0x10210` | `SettingController::notifyCurrentLanguage` | `0x7dfff3b4`, `0x7e02f4e9` |
| `0x10211` | `SettingController::notifySupportLanguage` | `0x7dfff637`, `0x7e02f553` |
| `0x10212` | `SettingController::saveCustom` | `0x7dfff800`, `0x7e02f7da` |
| `0x10213` | `SettingController::clearCustom` | `0x7dfff897`, `0x7e02ed92` |
| `0x10214` | `SettingController::loadCustom` | `0x7dfff92e`, `0x7e02f383` |
| `0x10215` | `SettingController::getCustomState` | `0x7dfffa2b`, `0x7e02ee86` |
| `0x10216` | `SettingController::changeMode` | `0x7dfffac2`, `0x7e02ed29` |
| `0x10217` | `SettingController::getSettingUser` | `0x7dffec60`, `0x7e02f1f4` |
| `0x10218` | `SettingController::setSettingUser` | — |
| `0x10219` | `SettingController::getSettingDetailUser` | `0x7dffed1e` |
| `0x1021a` | `SettingController::setSettingWork` | — |
| `0x1021b` | `SettingController::getSettingWork` | — |
| `0x1021c` | `SettingController::setSettingDetailWork` | — |
| `0x1021d` | `SettingController::getSettingDetailWork` | — |
| `0x1021e` | `SettingController::isMFsetting` | `0x7dfffca1`, `0x7e02f320` |
| `0x1021f` | `SettingController::startMFsetting` | `0x7dfffce1`, `0x7e02fb9a` |
| `0x10220` | `SettingController::endMFsetting` | `0x7dfffd21`, `0x7e02ee0c` |
| `0x10221` | `SettingController::getExposeMode` | `0x7dfffde2`, `0x7e02eef4` |
| `0x10222` | `SettingController::getHebrewEnable` | `0x7e02ef52` |
| `0x10223` | `SettingController::setHebrewEnable` | `0x7e02f854` |
| `0x10224` | `SettingController::getLanguageList` | `0x7e02efa0` |
| `0x10225` | `SettingController::resetIntervalShooting` | `0x7e02f704` |
| `0x10226` | `SettingController::setLensMfMode` | `0x7dffffe8`, `0x7e02f8c2` |
| `0x10227` | `SettingController::getLensMfMode` | `0x7dffffba`, `0x7e02efeb` |
| `0x10228` | `SettingController::getSettingDefault` | `0x7dffff26`, `0x7e02f099` |
| `0x10301` | `BackGroundCtrl::draw` | `0x7e000080` |
| `0x10302` | `BackGroundCtrl::paint` | `0x7e0002f9`, `0x7e021edc` |
| `0x10303` | `BackGroundCtrl::setMenuArea` | `0x7e00039e`, `0x7e021fce` |
| `0x10304` | `BackGroundCtrl::drawAsync` | — |
| `0x10305` | `BackGroundCtrl::setImageAreas` | `0x7e000745`, `0x7e021f61` |
| `0x10306` | `BackGroundCtrl::getDrawState` | `0x7e00082e`, `0x7e021e6d` |
| `0x10307` | `BackGroundCtrl::drawQR` | `0x7e000230`, `0x7e021d89` |
| `0x10308` | `BackGroundCtrl::startVariousDraw` | `0x7e00097d`, `0x7e0220b2` |
| `0x10309` | `BackGroundCtrl::endVariousDraw` | `0x7e000a02`, `0x7e021e01` |
| `0x10401` | `OnetouchLightCtrl::turnOn` | `0x7e01fc9c`, `0x7e028c8c` |
| `0x10402` | `OnetouchLightCtrl::turnOff` | `0x7e01fccf`, `0x7e028c42` |
| `0x10403` | `OnetouchLightCtrl::getStatus` | `0x7e01fcfc`, `0x7e028bf8` |
| `0x10501` | `SoundCtrl::play` | `0x7e000a87`, `0x7e034082` |
| `0x10502` | `SoundCtrl::stop` | `0x7e000b5b`, `0x7e034382` |
| `0x10503` | `SoundCtrl::setVolume` | `0x7e000b8e`, `0x7e034242` |
| `0x10504` | `SoundCtrl::startImportSound` | `0x7e000c0f`, `0x7e0342ae` |
| `0x10505` | `SoundCtrl::getSoundName` | `0x7e000c49`, `0x7e033ffd` |
| `0x10506` | `SoundCtrl::getImportSoundCount` | `0x7e000ce1`, `0x7e033e4b` |
| `0x10507` | `SoundCtrl::getImportSoundName` | `0x7e000d22`, `0x7e033eac` |
| `0x10508` | `SoundCtrl::registImportSound` | `0x7e000dba`, `0x7e0341df` |
| `0x10509` | `SoundCtrl::endImportSound` | `0x7e000e41`, `0x7e033d89` |
| `0x1050a` | `SoundCtrl::playImportSound` | `0x7e000e74`, `0x7e034103` |
| `0x1050b` | `SoundCtrl::stopImportSound` | `0x7e000f49`, `0x7e0343e3` |
| `0x1050c` | `SoundCtrl::startLevel` | `0x7e000fc9`, `0x7e034313` |
| `0x1050d` | `SoundCtrl::getLevel` | `0x7e001003`, `0x7e033f31` |
| `0x1050e` | `SoundCtrl::endLevel` | `0x7e0010dc`, `0x7e033dea` |
| `0x1050f` | `SoundCtrl::getMicDevice` | `0x7e00110f`, `0x7e033f9c` |
| `0x10601` | `LogoScreen::drawImage` | `0x7e020fcc`, `0x7e028a5a` |
| `0x10602` | `LogoScreen::existImage` | `0x7e021044`, `0x7e028aa9` |
| `0x10603` | `LogoScreen::regist` | `0x7e02106f`, `0x7e028af3` |
| `0x10604` | `LogoScreen::unregist` | `0x7e02109a`, `0x7e028b3d` |
| `0x10701` | `DateCtrl::getCurrentDateTime` | `0x7e00116f`, `0x7e023f0b` |
| `0x10702` | `DateCtrl::getDateCount` | `0x7e023ff9` |
| `0x10703` | `DateCtrl::getWday` | `0x7e024392` |
| `0x10704` | `DateCtrl::setDateTime` | `0x7e00128c`, `0x7e0243e0` |
| `0x10705` | `DateCtrl::setDualDateTime` | — |
| `0x10706` | `DateCtrl::canPopup` | `0x7e0013a5`, `0x7e023e66` |
| `0x10707` | `DateCtrl::startAreaSetting` | `0x7e02446a` |
| `0x10708` | `DateCtrl::endAreaSetting` | `0x7e023eca` |
| `0x10709` | `DateCtrl::getHomeTime` | `0x7e02415c` |
| `0x1070a` | `DateCtrl::getVisitTime` | `0x7e0242e6` |
| `0x1070b` | `DateCtrl::getDefaultDateTime` | `0x7e0013d2`, `0x7e02406e` |
| `0x1070c` | `DateCtrl::getTimeValueToSerial` | `0x7e0014aa`, `0x7e024275` |
| `0x1070d` | `DateCtrl::getSerialToTimeValue` | `0x7e001618`, `0x7e024208` |
| `0x10801` | `PixelMapping::execute` | `0x7e002472`, `0x7e028db1` |
| `0x10802` | `PixelMapping::canPixelMapping` | `0x7e002524`, `0x7e028d4b` |
| `0x10901` | `ModeCheck::canExecute` | `0x7dff8452`, `0x7e002551` |
| `0x10a01` | `PowerSupplyControl::startMonitor` | `0x7dff9391`, `0x7e0025d0` |
| `0x10a02` | `PowerSupplyControl::getBatteryState` | `0x7dff91f3`, `0x7e002687` |
| `0x10a03` | `PowerSupplyControl::getAcAdapterInfo` | `0x7dff91ae`, `0x7e002726` |
| `0x10a04` | `PowerSupplyControl::startCharging` | `0x7dff9350`, `0x7e00278f` |
| `0x10a05` | `PowerSupplyControl::stopCharging` | `0x7dff93fa`, `0x7e0027bc` |
| `0x10a06` | `PowerSupplyControl::getChargeState` | `0x7dff9297`, `0x7e0027e9` |
| `0x10a07` | `PowerSupplyControl::startChargeSleep` | `0x7dff9308`, `0x7e002865` |
| `0x10b01` | `OLDBControl::create` | — |
| `0x10b02` | `OLDBControl::abortCreate` | — |
| `0x10b03` | `OLDBControl::existsOLDB` | — |
| `0x10c01` | `MediaCtrl::getExistMedia` | `0x7dff7f24`, `0x7e001744` |
| `0x10c02` | `MediaCtrl::getCurrentMedia` | `0x7dff7ec3`, `0x7e0017a6` |
| `0x10c03` | `MediaCtrl::getMediaStateInfo` | `0x7dff80cf`, `0x7e001809` |
| `0x10c04` | `MediaCtrl::mountMedia` | — |
| `0x10c05` | `MediaCtrl::unmountMedia` | — |
| `0x10c06` | `MediaCtrl::isMediaAccess` | `0x7dff81fa`, `0x7e00189e` |
| `0x10c07` | `MediaCtrl::formatMedia` | `0x7dff7d7b`, `0x7e00193f` |
| `0x10c08` | `MediaCtrl::canFormat` | `0x7dff7b68`, `0x7e0019e7` |
| `0x10c09` | `MediaCtrl::isFormatWarning` | `0x7dff81a9` |
| `0x10c0a` | `MediaCtrl::copyMedia` | — |
| `0x10c0b` | `MediaCtrl::abortCopy` | — |
| `0x10c0c` | `MediaCtrl::canCopy` | `0x7dff7af7`, `0x7e001a82` |
| `0x10c0d` | `MediaCtrl::eraseAll` | `0x7dff7ca6`, `0x7e001b3e` |
| `0x10c0e` | `MediaCtrl::getImageCount` | `0x7dff7f85`, `0x7dff7ff3`, `0x7e001ce2` |
| `0x10c0f` | `MediaCtrl::getMediaConsumeRate` | `0x7dff8061`, `0x7e001c21` |
| `0x10c10` | `MediaCtrl::getAvailableShootCount` | `0x7dff7e55`, `0x7e001eac` |
| `0x10c11` | `MediaCtrl::unlockProtectAll` | `0x7dff836d`, `0x7e001f95` |
| `0x10c12` | `MediaCtrl::transferImageAll` | `0x7dff82dc`, `0x7e002078` |
| `0x10c13` | `MediaCtrl::cancelTransferImageAll` | `0x7dff7bd9`, `0x7e0021ac` |
| `0x10c14` | `MediaCtrl::changeMedia` | `0x7dff7c3a` |
| `0x10c15` | `MediaCtrl::getAVCHDstate` | `0x7dff7def`, `0x7e00227e` |
| `0x10c16` | `MediaCtrl::getMountState` | `0x7dff813d`, `0x7e0022b1` |
| `0x10c17` | `MediaCtrl::isMediaWriting` | `0x7dff826b`, `0x7e00239e` |
| `0x10c18` | `MediaCtrl::eraseReserveWiFiTransfer` | `0x7dff7d1a`, `0x7e00243f` |
| `0x10d01` | `GpsCtrl::startGPS` | `0x7e01fdd5`, `0x7e027932` |
| `0x10d02` | `GpsCtrl::endGPS` | `0x7e01fe06`, `0x7e02737b` |
| `0x10d03` | `GpsCtrl::getGPSState` | `0x7e01fe38`, `0x7e0274c8` |
| `0x10d04` | `GpsCtrl::getGPSdata` | `0x7e01fea6`, `0x7e0275ac` |
| `0x10d05` | `GpsCtrl::updateGPS` | `0x7e01ff5a`, `0x7e027a6a` |
| `0x10d06` | `GpsCtrl::getGPSUpdateTime` | `0x7e01ff85`, `0x7e027512`, `0x7e02755e` |
| `0x10d07` | `GpsCtrl::getLandMarkList` | `0x7e020088`, `0x7e0275f8` |
| `0x10d08` | `GpsCtrl::getOrientation` | `0x7e02016a` |
| `0x10d09` | `GpsCtrl::startCompass` | `0x7e02010d`, `0x7e0278e4` |
| `0x10d0a` | `GpsCtrl::endCompass` | `0x7e02013f`, `0x7e02732c` |
| `0x10d0b` | `GpsCtrl::getPositionCandidate` | `0x7e0201ab` |
| `0x10d0c` | `GpsCtrl::optimizeGpsUpdate` | `0x7e020285`, `0x7e027774` |
| `0x10d0d` | `GpsCtrl::startToughGear` | `0x7e020311`, `0x7e027a03` |
| `0x10d0e` | `GpsCtrl::endToughGear` | `0x7e0203a7`, `0x7e027432` |
| `0x10d0f` | `GpsCtrl::getSatelliteData` | `0x7e0276d0` |
| `0x10d10` | `GpsCtrl::getCurrentLandMarkData` | `0x7e02044b`, `0x7e02747c` |
| `0x10d11` | `GpsCtrl::setKeyState` | `0x7e02052d`, `0x7e027835` |
| `0x10d12` | `GpsCtrl::setTimeCorrection` | `0x7e0205e3`, `0x7e02788a` |
| `0x10d13` | `GpsCtrl::startLogger` | `0x7e02066f`, `0x7e027996` |
| `0x10d14` | `GpsCtrl::endLogger` | `0x7e02071f`, `0x7e0273d9` |
| `0x10d15` | `GpsCtrl::isAssistGpsData` | `0x7e020751`, `0x7e02772a` |
| `0x10d16` | `GpsCtrl::canSaveLog` | `0x7e0272e2` |
| `0x10d17` | `GpsCtrl::saveLog` | `0x7e02077c`, `0x7e0277ce` |
| `0x10d18` | `GpsCtrl::abortUpdateGPS` | `0x7e020812`, `0x7e027298` |
| `0x10e01` | `KeyCtrl::setLongPressKey` | `0x7e00300d`, `0x7e0281bc` |
| `0x10e02` | `KeyCtrl::setRepeatKey` | `0x7e002ad4` |
| `0x10e03` | `KeyCtrl::unsetAllLongPressKey` | `0x7e0034d2`, `0x7e0282b2` |
| `0x10e04` | `KeyCtrl::unsetAllRepeatKey` | `0x7e002fda`, `0x7e028313` |
| `0x10e05` | `KeyCtrl::unsetLongPressKey` | `0x7e003280`, `0x7e028374` |
| `0x10e06` | `KeyCtrl::unsetRepeatKey` | `0x7e002d88`, `0x7e0283e0` |
| `0x10e07` | `KeyCtrl::setExclusion` | `0x7e003505`, `0x7e0280c6`, `0x7e028159` |
| `0x10e08` | `KeyCtrl::cancelKeyEvent` | `0x7e0037ae`, `0x7e027ff4` |
| `0x10e09` | `KeyCtrl::resetKeyEvent` | `0x7e003f48`, `0x7e028065` |
| `0x10f01` | `LevelCtrl::startLevel` | `0x7e002892`, `0x7e028714` |
| `0x10f02` | `LevelCtrl::endLevel` | `0x7e002945`, `0x7e028575` |
| `0x10f03` | `LevelCtrl::getSlope` | `0x7e002977` |
| `0x10f04` | `LevelCtrl::reset` | `0x7e002a08`, `0x7e028652` |
| `0x10f05` | `LevelCtrl::calibration` | `0x7e002a3b`, `0x7e0284b3` |
| `0x10f06` | `LevelCtrl::getMaxSlope` | — |
| `0x10f07` | `LevelCtrl::start3DLevel` | `0x7e002a6e`, `0x7e0286b3` |
| `0x10f08` | `LevelCtrl::end3DLevel` | `0x7e002aa1`, `0x7e028514` |
| `0x11001` | `SystemCommon::scSetTimer` | `0x7dff943b`, `0x7e01b879` |
| `0x11002` | `SystemCommon::scStartTimer` | `0x7dff94bd`, `0x7e01b9b1` |
| `0x11003` | `SystemCommon::scStopTimer` | `0x7dff9536`, `0x7e01ba40` |
| `0x11004` | `SystemCommon::scKillTimer` | `0x7dff95af`, `0x7e01bacf` |
| `0x11005` | `SystemCommon::scStrncpy` | `0x7e01bb5e`, `0x7e01c976` |
| `0x11006` | `SystemCommon::scWcsncpy` | `0x7e01bc86` |
| `0x11007` | `SystemCommon::scStrncat` | `0x7e01bdd5` |
| `0x11008` | `SystemCommon::scWcsncat` | `0x7e01bf31` |
| `0x11009` | `SystemCommon::scStrncmp` | `0x7e01c064` |
| `0x1100a` | `SystemCommon::scWcsncmp` | `0x7e01c177` |
| `0x1100b` | `SystemCommon::scStrlen` | `0x7e01c28a` |
| `0x1100c` | `SystemCommon::scWcslen` | `0x7e01c312` |
| `0x1100d` | `SystemCommon::scStrupr` | `0x7e01c3cc` |
| `0x1100e` | `SystemCommon::scWcsupr` | `0x7e01c4c6` |
| `0x1100f` | `SystemCommon::scWcstol` | `0x7e01c5c4` |
| `0x11010` | `SystemCommon::scSprintf` | `0x7e01c64c` |
| `0x11011` | `SystemCommon::scWcsprintf` | `0x7e01c76b` |
| `0x11012` | `SystemCommon::scMalloc` | — |
| `0x11013` | `SystemCommon::scFree` | — |
| `0x11014` | `SystemCommon::scMemcpy` | `0x7e01ca96` |
| `0x11015` | `SystemCommon::scMemset` | `0x7e01cb99` |
| `0x11018` | `SystemCommon::scOsCreateTask` | `0x7dff84cb`, `0x7e01ce49` |
| `0x11019` | `SystemCommon::scOsDeleteTask` | `0x7dff854a`, `0x7e01cfcd` |
| `0x1101a` | `SystemCommon::scOsStartTask` | `0x7dff85c3`, `0x7e01d05c` |
| `0x1101b` | `SystemCommon::scOsIStartTask` | `0x7dff863c`, `0x7e01d0eb` |
| `0x1101c` | `SystemCommon::scOsStopTask` | `0x7dff86b5`, `0x7e01d17a` |
| `0x1101d` | `SystemCommon::scOsWakeupTask` | `0x7dff872e`, `0x7e01d209` |
| `0x1101e` | `SystemCommon::scOsIWakeupTask` | `0x7dff87a7`, `0x7e01d298` |
| `0x1101f` | `SystemCommon::scOsSelfEndTask` | `0x7dff8820`, `0x7e01d327` |
| `0x11020` | `SystemCommon::scOsSleepTask` | `0x7dff888c`, `0x7e01d349` |
| `0x11021` | `SystemCommon::scOsSelfSleepTask` | `0x7dff8905`, `0x7e01d3d8` |
| `0x11022` | `SystemCommon::scOsCreateEvent` | `0x7dff897e`, `0x7e01d467` |
| `0x11023` | `SystemCommon::scOsDeleteEvent` | `0x7dff89f9`, `0x7e01d590` |
| `0x11024` | `SystemCommon::scOsSetEvent` | `0x7dff8a72`, `0x7e01d61f` |
| `0x11025` | `SystemCommon::scOsISetEvent` | `0x7dff8aeb`, `0x7e01d6dc` |
| `0x11026` | `SystemCommon::scOsWaitEvent` | `0x7dff8b64`, `0x7e01d799` |
| `0x11027` | `SystemCommon::scOsClearEvent` | `0x7dff8bfc`, `0x7e01d8ef` |
| `0x11028` | `SystemCommon::scOsCreateQueue` | `0x7dff8c74`, `0x7e01d9ac` |
| `0x11029` | `SystemCommon::scOsDeleteQueue` | `0x7dff8cf4`, `0x7e01db34` |
| `0x1102a` | `SystemCommon::scOsWriteQueue` | `0x7dff8d6d`, `0x7e01dbc3` |
| `0x1102b` | `SystemCommon::scOsReadQueue` | `0x7dff8de8`, `0x7e01dcb4` |
| `0x1102c` | `SystemCommon::scOsCreateSemaphore` | `0x7dff8e62`, `0x7e01dd90` |
| `0x1102d` | `SystemCommon::scOsDeleteSemaphore` | `0x7dff8ee2`, `0x7e01df18` |
| `0x1102e` | `SystemCommon::scOsWaitSemaphore` | `0x7dff8f5b`, `0x7e01dfa7` |
| `0x1102f` | `SystemCommon::scOsSignalSemaphore` | `0x7dff8fd4`, `0x7e01e07e` |
| `0x11030` | `SystemCommon::scOsISignalSemaphore` | `0x7dff904d`, `0x7e01e10d` |
| `0x11031` | `SystemCommon::scTimeMinit` | `0x7e01e273` |
| `0x11032` | `SystemCommon::scTimeMset` | `0x7e01e2a1` |
| `0x11033` | `SystemCommon::scTimeMshow` | `0x7e01e331` |
| `0x11034` | `SystemCommon::scTimeMwrite` | `0x7e01e35f` |
| `0x11035` | `SystemCommon::scUsrTimeMeasurementStart` | `0x7e01e38d` |
| `0x11036` | `SystemCommon::scProcLogStart` | `0x7e01e41d` |
| `0x11037` | `SystemCommon::scProcLogStop` | `0x7e01e44b` |
| `0x11038` | `SystemCommon::scOsChangePriority` | `0x7dff90cf`, `0x7e01e19c` |
| `0x11101` | `OSDControl::initOsdControl` | `0x7e01e479` |
| `0x11102` | `OSDControl::drawOsdStart` | `0x7e01e49b` |
| `0x11103` | `OSDControl::drawOsdEnd` | `0x7e01e4bd` |
| `0x11104` | `OSDControl::setOsdOrder` | — |
| `0x11105` | `OSDControl::setFrameSize` | `0x7e01e5d5` |
| `0x11106` | `OSDControl::drawDot` | `0x7e01e6cc` |
| `0x11107` | `OSDControl::drawLine` | `0x7e01e782` |
| `0x11108` | `OSDControl::drawRect` | `0x7e01e838` |
| `0x11109` | `OSDControl::drawFont` | `0x7e01e8ee` |
| `0x1110a` | `OSDControl::drawBitmap` | `0x7e01e9a4` |
| `0x1110b` | `OSDControl::copyFrame` | `0x7e01ea5a` |
| `0x1110c` | `OSDControl::copyAreaBlock` | `0x7e01eb15` |
| `0x1110d` | `OSDControl::customDisplay` | `0x7e01ebcb` |
| `0x1110e` | `OSDControl::updateDisplay` | `0x7e01ec81` |
| `0x1110f` | `OSDControl::updateImageLayer` | `0x7e01ed37` |
| `0x11110` | `OSDControl::setColorPalette` | `0x7e01edf3` |
| `0x11111` | `OSDControl::setTransparent` | `0x7e01eeb4` |
| `0x11112` | `OSDControl::resetTransparent` | `0x7e01ef60` |
| `0x11113` | `OSDControl::getVramInfo` | `0x7e01f007` |
| `0x11114` | `OSDControl::freeVramInfo` | `0x7e01f1df` |
| `0x11115` | `OSDControl::setDispInfo` | `0x7e01f26e` |
| `0x11201` | `OSDEffect::LVControlBase` | `0x7e01f318` |
| `0x11202` | `OSDEffect::LVControlDirect` | `0x7e01f4ff` |
| `0x11203` | `OSDEffect::LVguidePlate` | `0x7e01f6b4` |
| `0x11301` | `SystemStart::rhpinit` | — |
| `0x11302` | `SystemStart::rhpstart` | — |
| `0x11303` | `SystemStart::rhptakeover` | — |
| `0x11304` | `SystemStart::rhpfastend` | — |
| `0x11305` | `SystemStart::rhpthroughover` | — |
| `0x20101` | `Shooting::startShootingService` | `0x7e00492c`, `0x7e031e08` |
| `0x20102` | `Shooting::endShootingService` | `0x7e004afb`, `0x7e030600` |
| `0x20103` | `Shooting::canEndShootingService` | `0x7e004b31`, `0x7e03124b` |
| `0x20104` | `Shooting::setShootingType` | `0x7e004b67`, `0x7e030a25` |
| `0x20105` | `Shooting::setRecViewArea` | `0x7e004c98` |
| `0x20106` | `Shooting::ctrlRelease` | `0x7e0315cc` |
| `0x20107` | `Shooting::reserve1` | — |
| `0x20108` | `Shooting::reserve2` | — |
| `0x20109` | `Shooting::getThroughState` | — |
| `0x2010a` | `Shooting::startHistogram` | `0x7e005130`, `0x7e0303d0` |
| `0x2010b` | `Shooting::stopHistogram` | `0x7e005279`, `0x7e03046a` |
| `0x2010c` | `Shooting::getCondition` | `0x7e0052ae`, `0x7e02ff88` |
| `0x2010d` | `Shooting::getLiveCondition` | — |
| `0x2010e` | `Shooting::getFlashChargeStatus` | `0x7e00573a`, `0x7e03007b` |
| `0x2010f` | `Shooting::getShakeWarning` | `0x7e0302f3` |
| `0x20110` | `Shooting::getHistogramData` | `0x7e005828`, `0x7e0300e8` |
| `0x20111` | `Shooting::getRecViewInfo` | `0x7e005a79`, `0x7e030b09` |
| `0x20112` | `Shooting::getAspectFrame` | `0x7e0068d3`, `0x7e0309b8` |
| `0x20113` | `Shooting::getFocusPosition` | `0x7e006aab`, `0x7e030b76` |
| `0x20114` | `Shooting::getRecViewHistogram` | `0x7e006c44`, `0x7e030225` |
| `0x20115` | `Shooting::getProgress` | `0x7e006e18`, `0x7e0301c2` |
| `0x20116` | `Shooting::getAvailableShootCount` | `0x7e006e4f`, `0x7e02feef` |
| `0x20117` | `Shooting::startZoomFrame` | `0x7e006ec9`, `0x7e030be3` |
| `0x20118` | `Shooting::endZoomFrame` | `0x7e006eff`, `0x7e030c44` |
| `0x20119` | `Shooting::getZoomFrame` | `0x7e006f35`, `0x7e030ca5`, `0x7e033832` |
| `0x2011a` | `Shooting::moveZoomFrame` | `0x7e007162`, `0x7e030d43` |
| `0x2011b` | `Shooting::zoomThrough` | `0x7e0072af`, `0x7e030daf` |
| `0x2011c` | `Shooting::scrollThrough` | `0x7e008604`, `0x7e030e1b` |
| `0x2011d` | `Shooting::getEnlargeInfo` | `0x7e00738a`, `0x7e030e87` |
| `0x2011e` | `Shooting::setMultiThroughMode` | `0x7e00747a`, `0x7e030364` |
| `0x2011f` | `Shooting::startMultiThrough` | `0x7e007510` |
| `0x20120` | `Shooting::canMultiThrough` | — |
| `0x20121` | `Shooting::moveCurrent` | `0x7e007576` |
| `0x20122` | `Shooting::startWBdetect` | `0x7e009f7d` |
| `0x20123` | `Shooting::apertureDown` | `0x7e007644`, `0x7e030eea` |
| `0x20124` | `Shooting::changeDirection` | `0x7e0076dc`, `0x7e02fe22` |
| `0x20125` | `Shooting::getDirection` | `0x7e007784`, `0x7e03001a` |
| `0x20126` | `Shooting::endPanoramaShooting` | `0x7e0077b1`, `0x7e02fe8e` |
| `0x20127` | `Shooting::getPanoramaCount` | `0x7e0077e6`, `0x7e03015f` |
| `0x20128` | `Shooting::getPanoramaCountMax` | `0x7e00781d`, `0x7e03059d` |
| `0x20129` | `Shooting::abort3DShooting` | — |
| `0x2012a` | `Shooting::getScene` | `0x7e007906`, `0x7e030292` |
| `0x2012b` | `Shooting::setAflState` | `0x7e007acd`, `0x7e0304cb` |
| `0x2012c` | `Shooting::getAflState` | `0x7e007b62`, `0x7e030537` |
| `0x2012d` | `Shooting::setAelState` | `0x7e007b8f`, `0x7e03094c` |
| `0x2012e` | `Shooting::getAelState` | `0x7e007c8e`, `0x7e030820` |
| `0x2012f` | `Shooting::saveWBdetect` | `0x7e007d14`, `0x7e0307b0` |
| `0x20130` | `Shooting::sampleWBadjust` | `0x7e007d9f`, `0x7e030f56` |
| `0x20131` | `Shooting::startMFAssist` | `0x7e007f8d`, `0x7e03073a`, `0x7e0332db` |
| `0x20132` | `Shooting::endMFAssist` | `0x7e0080d6`, `0x7e0306d9` |
| `0x20133` | `Shooting::startMultiExposure` | `0x7e0081f2`, `0x7e0308eb` |
| `0x20134` | `Shooting::endMultiExposure` | `0x7e00760e`, `0x7e008227`, `0x7e03088a` |
| `0x20135` | `Shooting::overlay` | `0x7e030fe0` |
| `0x20136` | `Shooting::saveMultiExposure` | `0x7e00825c`, `0x7e03104c` |
| `0x20137` | `Shooting::getMultiExposureCount` | `0x7e008292`, `0x7e0310ad` |
| `0x20138` | `Shooting::deleteMultiExposure` | `0x7e0082de`, `0x7e03111a` |
| `0x20139` | `Shooting::getMovieTime` | `0x7e008314`, `0x7e03117b` |
| `0x2013a` | `Shooting::abortSelfTimer` | `0x7e0311ea` |
| `0x2013b` | `Shooting::preSampleWBadjust` | — |
| `0x2013c` | `Shooting::postSampleWBadjust` | — |
| `0x2013d` | `Shooting::getFaceInfo` | `0x7e03066c` |
| `0x2013e` | `Shooting::setShootingType_Nomal` | — |
| `0x2013f` | `Shooting::setShootingType_Test` | — |
| `0x20140` | `Shooting::setShootingType_OneTouchWB` | — |
| `0x20141` | `Shooting::readyShooting` | — |
| `0x20142` | `Shooting::setShutterSound` | — |
| `0x20143` | `Shooting::setPrecedenceShooting` | — |
| `0x20144` | `Shooting::changeMode` | — |
| `0x20145` | `Shooting::getRecViewState` | `0x7e0084b4`, `0x7e0312b1` |
| `0x20146` | `Shooting::touchTargetAf` | `0x7e008515` |
| `0x20147` | `Shooting::touchShoot` | — |
| `0x20148` | `Shooting::stopTouchShoot` | — |
| `0x20149` | `Shooting::getTouchAction` | `0x7e008751`, `0x7e032151` |
| `0x2014a` | `Shooting::notifyGesture` | `0x7e008856`, `0x7e0314ed`, `0x7e033206` |
| `0x2014b` | `Shooting::getMovableArea` | `0x7e0088fa`, `0x7e03155e` |
| `0x2014c` | `Shooting::getFPNexposureStatus` | `0x7e008a39`, `0x7e031662` |
| `0x2014d` | `Shooting::setThroughType` | `0x7e008a6f`, `0x7e0316c8` |
| `0x2014e` | `Shooting::ctrlZoomExposure` | `0x7e008b13`, `0x7e031795` |
| `0x2014f` | `Shooting::getSlideRecView` | `0x7e008b90`, `0x7e031874` |
| `0x20150` | `Shooting::getLiveBulbInfo` | `0x7e008c80`, `0x7e031801`, `0x7e031b2b`, `0x7e031ba2`, `0x7e033b0e` |
| `0x20151` | `Shooting::updateLiveBulb` | `0x7e008d10`, `0x7e031734` |
| `0x20152` | `Shooting::ctrlMovieEffect` | `0x7e008de0`, `0x7e0319f8` |
| `0x20153` | `Shooting::start3DLensShooting` | `0x7e008daa`, `0x7e031997` |
| `0x20154` | `Shooting::end3DLensShooting` | `0x7e008d46`, `0x7e0318d5` |
| `0x20155` | `Shooting::getReleaseSetting` | `0x7e008d7c`, `0x7e031936` |
| `0x20156` | `Shooting::cancelRecview` | `0x7e008ec4`, `0x7e031a64` |
| `0x20157` | `Shooting::isLiveBulbShooting` | `0x7e008efa`, `0x7e031ac5` |
| `0x20158` | `Shooting::getShootingState` | `0x7e008f30`, `0x7e031c19` |
| `0x20159` | `Shooting::resetTouchScrollPosition` | `0x7e008f66`, `0x7e031c7f` |
| `0x2015a` | `Shooting::getShootingType` | `0x7e004c2b`, `0x7e031ce0` |
| `0x2015b` | `Shooting::getZoomFrameState` | `0x7e008f9c`, `0x7e031da2` |
| `0x2015c` | `Shooting::getThroughZoomRate` | `0x7e008fd2`, `0x7e031d41` |
| `0x2015d` | `Shooting::startLiveGuide` | `0x7e00912a`, `0x7e031fac` |
| `0x2015e` | `Shooting::startLiveGuideLevel` | `0x7e009215`, `0x7e032281` |
| `0x2015f` | `Shooting::getLiveGuideLevel` | `0x7e031e7c` |
| `0x20160` | `Shooting::changeLiveGuideLevel` | `0x7e0093ea`, `0x7e0321b4` |
| `0x20161` | `Shooting::endLiveGuideLevel` | `0x7e0095bf`, `0x7e0322ed` |
| `0x20162` | `Shooting::endLiveGuide` | `0x7e0096ab`, `0x7e031ee8` |
| `0x20163` | `Shooting::startIntervalShooting` | `0x7e0320e5` |
| `0x20164` | `Shooting::oneShotTakingPicture` | `0x7e032220` |
| `0x20165` | `Shooting::endIntervalShooting` | `0x7e0323cb` |
| `0x20166` | `Shooting::oneShotTapShooting` | `0x7e032a8b` |
| `0x20167` | `Shooting::getSelfRemainTime` | `0x7e0096e1`, `0x7e032947` |
| `0x20168` | `Shooting::zoomIn` | `0x7e009d12`, `0x7e03286d` |
| `0x20169` | `Shooting::zoomOut` | `0x7e009d7d`, `0x7e0328da` |
| `0x2016a` | `Shooting::stopZooming` | `0x7e009dda`, `0x7e032804` |
| `0x2016b` | `Shooting::getMaxZoomMagnification` | `0x7e009e08`, `0x7e032561` |
| `0x2016c` | `Shooting::getCurrentZoomMagnification` | `0x7e009f1d`, `0x7e032511` |
| `0x2016d` | `Shooting::getShootingTargetPos` | `0x7e0325c1` |
| `0x2016e` | `Shooting::lightThrough` | `0x7e008405`, `0x7e0326c6` |
| `0x2016f` | `Shooting::getTargetAfState` | `0x7e007cbb`, `0x7e032643` |
| `0x20170` | `Shooting::startTargetAf` | `0x7e007c24`, `0x7e03277d` |
| `0x20171` | `Shooting::endTargetAf` | `0x7e007c59`, `0x7e032486` |
| `0x20172` | `Shooting::startAfl` | `0x7e009057`, `0x7e0329b3` |
| `0x20173` | `Shooting::endAfl` | `0x7e009085`, `0x7e032a14` |
| `0x20174` | `Shooting::applyChangeSetting` | `0x7e03242c` |
| `0x20175` | `Shooting::endMultiThrough` | — |
| `0x20176` | `Shooting::startCombine` | `0x7e00a136`, `0x7e032718` |
| `0x20177` | `Shooting::ctrlMovieTelecon` | `0x7e009843`, `0x7e032079` |
| `0x20178` | `Shooting::getMovieTeleconFrame` | `0x7e0098f5`, `0x7e031f49` |
| `0x20179` | `Shooting::moveMovieTeleconFrame` | `0x7e0099c0`, `0x7e032359` |
| `0x2017a` | `Shooting::isLiveGuide` | `0x7e009b0e`, `0x7e032af0` |
| `0x2017b` | `Shooting::createTimeLapseMovie` | `0x7e032018` |
| `0x2017c` | `Shooting::getTouchTrackingAfl` | `0x7e032b56` |
| `0x2017d` | `Shooting::changeZoomFrameRate` | `0x7e032bbc` |
| `0x2017e` | `Shooting::getZoomMagnification` | `0x7e009e68`, `0x7e032c28` |
| `0x2017f` | `Shooting::getLiveBulbSetting` | `0x7e032ce2` |
| `0x20180` | `Shooting::setLiveBulbSetting` | `0x7e032c76` |
| `0x20181` | `Shooting::getLiveBulbHistogram` | `0x7e032d50` |
| `0x20182` | `Shooting::setFocusModeChange` | `0x7e00a906`, `0x7e032dbd` |
| `0x20183` | `Shooting::getFocusModeChange` | `0x7e00a9ad`, `0x7e032e26` |
| `0x20184` | `Shooting::getMFAssist` | `0x7e00810b`, `0x7e033276` |
| `0x20185` | `Shooting::startPhotoSession` | `0x7e033019` |
| `0x20186` | `Shooting::endPhotoSession` | `0x7e033141` |
| `0x20187` | `Shooting::savePhotoSession` | `0x7e032eef` |
| `0x20188` | `Shooting::getPhotoSessionTakeCount` | `0x7e03307a` |
| `0x20189` | `Shooting::deletePhotoSession` | `0x7e0331a2` |
| `0x2018a` | `Shooting::resetPhotoSession` | `0x7e032fb8` |
| `0x2018b` | `Shooting::updatePhotoSession` | `0x7e0330dd` |
| `0x2018c` | `Shooting::getPhotoSessionStateArea` | `0x7e032e84` |
| `0x2018d` | `Shooting::getPhotoSessionLastArea` | `0x7e032f50` |
| `0x2018e` | `Shooting::photoSessionSpeedTouch` | `0x7e00a414`, `0x7e033347` |
| `0x2018f` | `Shooting::photoSessionSpeedRelease` | `0x7e00a492`, `0x7e0333b3` |
| `0x20190` | `Shooting::photoSessionSpeedTakePicture` | `0x7e00a4bd`, `0x7e0333fd` |
| `0x20191` | `Shooting::zoomRecView` | — |
| `0x20192` | `Shooting::isMFtsLensMount` | `0x7dffe407`, `0x7e033503` |
| `0x20193` | `Shooting::isAfEnable` | `0x7dffe448` |
| `0x20194` | `Shooting::setAfAreaType` | `0x7dffe4f4`, `0x7e0335cc` |
| `0x20195` | `Shooting::getAfAreaType` | `0x7dffe599`, `0x7e033569` |
| `0x20196` | `Shooting::getRecViewZoomRate` | — |
| `0x20197` | `Shooting::stopCreateTimeLapseMovie` | `0x7e03369f` |
| `0x20198` | `Shooting::isFtsLensMount` | `0x7dffe669`, `0x7e033639` |
| `0x20199` | `Shooting::isZoomRecView` | `0x7e00aa30`, `0x7e033700` |
| `0x2019a` | `Shooting::isZoomThrough` | `0x7e00aa66`, `0x7e033766` |
| `0x2019b` | `Shooting::isLiveBulbHistogramEnable` | `0x7e00aa9c`, `0x7e0337cc` |
| `0x2019c` | `Shooting::startFrameAssist` | `0x7e00aad2`, `0x7e0338a6` |
| `0x2019d` | `Shooting::endFrameAssist` | `0x7e00ab08`, `0x7e033907` |
| `0x2019e` | `Shooting::getSubjectDistance` | `0x7e00abac`, `0x7e033973` |
| `0x2019f` | `Shooting::ctrlMonitoringState` | `0x7e00abe2`, `0x7e0339d4` |
| `0x201a0` | `Shooting::getDarkFrameState` | `0x7e00accd`, `0x7e033aa1` |
| `0x201a1` | `Shooting::cancelDarkFrame` | `0x7e00ad30`, `0x7e033a40` |
| `0x201a2` | `Shooting::getMovieState` | `0x7e00ad66`, `0x7e033b99` |
| `0x201a3` | `Shooting::changeLiveGuide` | `0x7e00ad9c` |
| `0x201a4` | `Shooting::getLiveGuideInfo` | `0x7e00ae87` |
| `0x201a5` | `Shooting::getApertureDownState` | `0x7e00aebf`, `0x7e033c11` |
| `0x201a6` | `Shooting::getCustomSelfShootingCount` | `0x7e00aef5`, `0x7e033c77` |
| `0x201a7` | `Shooting::getSelfTimerCount` | `0x7e00af24`, `0x7e033cc7` |
| `0x20201` | `ShootingMovie::execute` | — |
| `0x20202` | `ShootingMovie::stop` | — |
| `0x20203` | `ShootingMovie::getTime` | — |
| `0x20204` | `ShootingMovie::ready` | — |
| `0x20205` | `ShootingMovie::unready` | — |
| `0x20301` | `ShootingBeautyMake::startBeautySet` | — |
| `0x20302` | `ShootingBeautyMake::endBeautySet` | — |
| `0x20303` | `ShootingBeautyMake::saveImage` | — |
| `0x20304` | `ShootingBeautyMake::abort` | — |
| `0x20305` | `ShootingBeautyMake::makepPeview` | — |
| `0x20306` | `ShootingBeautyMake::makeFacePreview` | — |
| `0x20307` | `ShootingBeautyMake::makeComparePreview` | — |
| `0x20308` | `ShootingBeautyMake::setParam` | — |
| `0x20309` | `ShootingBeautyMake::getParam` | — |
| `0x2030a` | `ShootingBeautyMake::loadParam` | — |
| `0x2030b` | `ShootingBeautyMake::saveParam` | — |
| `0x2030c` | `ShootingBeautyMake::isEnlarge` | — |
| `0x2030d` | `ShootingBeautyMake::getEnlargeInfo` | — |
| `0x2030e` | `ShootingBeautyMake::enlargeImage` | — |
| `0x2030f` | `ShootingBeautyMake::reduceImage` | — |
| `0x20310` | `ShootingBeautyMake::scrollImage` | — |
| `0x20401` | `AfFinetune::startTune` | `0x7e00bcce` |
| `0x20402` | `AfFinetune::endTune` | `0x7e00b128` |
| `0x20403` | `AfFinetune::deleteRecord` | `0x7e00af53` |
| `0x20404` | `AfFinetune::getRecordLens` | `0x7e00b294` |
| `0x20405` | `AfFinetune::getTemporaryRecord` | `0x7e00b489` |
| `0x20406` | `AfFinetune::getCurrentTarget` | `0x7e00b1ce` |
| `0x20407` | `AfFinetune::setCurrentTarget` | `0x7e00b92e` |
| `0x20408` | `AfFinetune::getFinetuneValue` | `0x7e00b1fc` |
| `0x20409` | `AfFinetune::setFinetuneValue` | `0x7e00bbf3` |
| `0x2040a` | `AfFinetune::setCheckMark` | `0x7e00b669` |
| `0x2040b` | `AfFinetune::upFinetuneValue` | `0x7e00bea2` |
| `0x2040c` | `AfFinetune::downFinetuneValue` | `0x7e00bf48` |
| `0x30101` | `PlayCommon::startPlayService` | `0x7e00bfee`, `0x7e029ae4` |
| `0x30102` | `PlayCommon::getImageType` | `0x7e00c05e`, `0x7e02973a` |
| `0x30103` | `PlayCommon::getStillInfo` | `0x7e00c14a`, `0x7e0298c6` |
| `0x30104` | `PlayCommon::getMovieInfo` | `0x7e00cd69`, `0x7e02979b` |
| `0x30105` | `PlayCommon::getNumber` | `0x7e00cef0`, `0x7e0297fe` |
| `0x30106` | `PlayCommon::getImageCount` | — |
| `0x30107` | `PlayCommon::getHistogram` | `0x7e00cf5d`, `0x7e0296c1` |
| `0x30108` | `PlayCommon::expandContinuousShots` | — |
| `0x30109` | `PlayCommon::editLandmark` | — |
| `0x3010a` | `PlayCommon::endPlayService` | `0x7e00c029`, `0x7e0295fb` |
| `0x3010b` | `PlayCommon::changeProtect` | `0x7e00d623`, `0x7e029419` |
| `0x3010c` | `PlayCommon::canProtect` | `0x7e00d650`, `0x7e0292ec` |
| `0x3010d` | `PlayCommon::changeProtectSelected` | `0x7e00d67d`, `0x7e02947f` |
| `0x3010e` | `PlayCommon::erase` | `0x7e00d5ee`, `0x7e02965c` |
| `0x3010f` | `PlayCommon::isReservePrint` | `0x7e00d6b2`, `0x7e0299f5` |
| `0x30110` | `PlayCommon::isProtect` | `0x7e00d6e7`, `0x7e029929` |
| `0x30111` | `PlayCommon::isRecording` | `0x7e00d71c`, `0x7e02998f` |
| `0x30112` | `PlayCommon::selectCurrent` | `0x7e00d57b`, `0x7e029a5b` |
| `0x30113` | `PlayCommon::getSelectPicNumber` | `0x7e00d5c1`, `0x7e029865` |
| `0x30114` | `PlayCommon::transferImage` | `0x7e00d751`, `0x7e029b49` |
| `0x30115` | `PlayCommon::cancelSelectedAll` | `0x7e00d87c`, `0x7e0293b8` |
| `0x30116` | `PlayCommon::selectPic` | `0x7e00d8b1` |
| `0x30117` | `PlayCommon::changeReserveWiFiTransfer` | `0x7e00d8ea`, `0x7e0294e0` |
| `0x30118` | `PlayCommon::changeReserveWiFiTransferSelected` | `0x7e00d917`, `0x7e029546` |
| `0x30119` | `PlayCommon::canReserveWiFiTransfer` | `0x7e00d94c`, `0x7e029352` |
| `0x30201` | `PlaySingleFrame::startSingleFrame` | `0x7e00d979` |
| `0x30202` | `PlaySingleFrame::moveCurrent` | `0x7e00dba7`, `0x7e02c52f` |
| `0x30203` | `PlaySingleFrame::canMoveCurrent` | `0x7e00dabb`, `0x7e02bf4b` |
| `0x30204` | `PlaySingleFrame::isReservePrint` | — |
| `0x30205` | `PlaySingleFrame::isProtect` | — |
| `0x30206` | `PlaySingleFrame::isRecording` | — |
| `0x30207` | `PlaySingleFrame::updateImage` | `0x7e00dce4`, `0x7e02c9ac` |
| `0x30208` | `PlaySingleFrame::enlargeImage` | — |
| `0x30209` | `PlaySingleFrame::reduceImage` | — |
| `0x3020a` | `PlaySingleFrame::scrollImage` | `0x7e00dedc`, `0x7e02c69c` |
| `0x3020b` | `PlaySingleFrame::isEnlarge` | `0x7e00df99`, `0x7e02c4c9` |
| `0x3020c` | `PlaySingleFrame::canPanoramaScroll` | `0x7e02bfbf` |
| `0x3020d` | `PlaySingleFrame::eraseCurrent` | `0x7e00e58c`, `0x7e02c2c0` |
| `0x3020e` | `PlaySingleFrame::eraseAll` | — |
| `0x3020f` | `PlaySingleFrame::eraseEvent` | — |
| `0x30210` | `PlaySingleFrame::startEffect` | — |
| `0x30211` | `PlaySingleFrame::endEffect` | — |
| `0x30212` | `PlaySingleFrame::canPrint` | `0x7e00e557`, `0x7e02c009` |
| `0x30213` | `PlaySingleFrame::getEnlargeInfo` | `0x7e00dfc6`, `0x7e02c386` |
| `0x30214` | `PlaySingleFrame::rotateImage` | `0x7e02c628` |
| `0x30215` | `PlaySingleFrame::getAspectFrame` | `0x7e00e5c1`, `0x7e02c321` |
| `0x30216` | `PlaySingleFrame::zoomImage` | `0x7e00dde7`, `0x7e02ca94` |
| `0x30217` | `PlaySingleFrame::getZoomFrame` | `0x7e00e164` |
| `0x30218` | `PlaySingleFrame::moveZoomFrame` | `0x7e00e347`, `0x7e02c5bc` |
| `0x30219` | `PlaySingleFrame::getFocusPosition` | `0x7e00e725`, `0x7e02c3e9` |
| `0x3021a` | `PlaySingleFrame::canRotate` | `0x7e00e404`, `0x7e02c06f` |
| `0x3021b` | `PlaySingleFrame::startSlide` | `0x7e00e898`, `0x7e02c93e` |
| `0x3021c` | `PlaySingleFrame::endSlide` | `0x7e00e98f`, `0x7e02c25f` |
| `0x3021d` | `PlaySingleFrame::startMoveCurrentContinuous` | `0x7e00e9c4`, `0x7e02c793` |
| `0x3021e` | `PlaySingleFrame::endMoveCurrentContinuous` | `0x7e00ead7`, `0x7e02c13a` |
| `0x3021f` | `PlaySingleFrame::startFastZoom` | `0x7e00eb0e`, `0x7e02c724` |
| `0x30220` | `PlaySingleFrame::zoomImageFast` | `0x7e00eba9`, `0x7e02cb02` |
| `0x30221` | `PlaySingleFrame::endFastZoom` | `0x7e00ec44`, `0x7e02c0d9` |
| `0x30222` | `PlaySingleFrame::startScrollFast` | `0x7e00ec79`, `0x7e02c7ff` |
| `0x30223` | `PlaySingleFrame::endScrollFast` | `0x7e00ed9e`, `0x7e02c19d` |
| `0x30224` | `PlaySingleFrame::startScrollZoomFrame` | `0x7e00edd3`, `0x7e02c86c` |
| `0x30225` | `PlaySingleFrame::endScrollZoomFrame` | `0x7e00ee0a`, `0x7e02c1fe` |
| `0x30226` | `PlaySingleFrame::updateImageSync` | `0x7e00ee3f`, `0x7e02ca20` |
| `0x30301` | `PlayIndex::startIndex` | `0x7e00ef09` |
| `0x30302` | `PlayIndex::getPageInfo` | `0x7e00f0c7` |
| `0x30303` | `PlayIndex::getCurrentInfo` | `0x7e00f11e`, `0x7e02a139` |
| `0x30304` | `PlayIndex::changeIndexNumber` | `0x7e00f183` |
| `0x30305` | `PlayIndex::updateImage` | `0x7e00f337`, `0x7e02a759` |
| `0x30306` | `PlayIndex::moveCurrent` | `0x7e00f492` |
| `0x30307` | `PlayIndex::canMoveCurrent` | `0x7e00f36c`, `0x7e029f02` |
| `0x30308` | `PlayIndex::startExpandAnimation` | `0x7e00f645`, `0x7e02a554` |
| `0x30309` | `PlayIndex::getTitleInfo` | — |
| `0x3030a` | `PlayIndex::drawTitle` | — |
| `0x3030b` | `PlayIndex::canCollage` | — |
| `0x3030c` | `PlayIndex::rotateImage` | `0x7e00f5a2`, `0x7e02a482` |
| `0x3030d` | `PlayIndex::canRotate` | `0x7e00f575`, `0x7e029fe1` |
| `0x3030e` | `PlayIndex::moveCurrentDirect` | `0x7e00f67a`, `0x7e02a3a8` |
| `0x3030f` | `PlayIndex::canMovePage` | `0x7e00f704`, `0x7e029f76` |
| `0x30310` | `PlayIndex::movePage` | `0x7e00f7b3`, `0x7e02a417` |
| `0x30311` | `PlayIndex::getIndexInfo` | `0x7e00f860`, `0x7e02a19e` |
| `0x30312` | `PlayIndex::startSlide` | `0x7e00f8ad`, `0x7e02a6eb` |
| `0x30313` | `PlayIndex::endSlide` | `0x7e00f8f8`, `0x7e02a0d8` |
| `0x30314` | `PlayIndex::getMaxRow` | `0x7e00f92d`, `0x7e02a201` |
| `0x30315` | `PlayIndex::getShowedRow` | `0x7e00f95a`, `0x7e02a2cf` |
| `0x30316` | `PlayIndex::selectPic` | `0x7e00f996`, `0x7e02a4ee` |
| `0x30401` | `EraseSelectedPic::canMoveCurrent` | `0x7e020e98` |
| `0x30402` | `EraseSelectedPic::erase` | `0x7e020eb4` |
| `0x30403` | `EraseSelectedPic::getCurrentInfo` | `0x7e020ed0` |
| `0x30404` | `EraseSelectedPic::getPageInfo` | `0x7e020eec` |
| `0x30405` | `EraseSelectedPic::getSelectedPicNumber` | `0x7e020f08` |
| `0x30406` | `EraseSelectedPic::indexMode` | `0x7e020f24` |
| `0x30407` | `EraseSelectedPic::moveCurrent` | `0x7e020f40` |
| `0x30408` | `EraseSelectedPic::selectCurrent` | `0x7e020f5c` |
| `0x30409` | `EraseSelectedPic::singleMode` | `0x7e020f78` |
| `0x3040a` | `EraseSelectedPic::start` | `0x7e020f94` |
| `0x3040b` | `EraseSelectedPic::startExpandAnimation` | `0x7e020fb0` |
| `0x30501` | `PlayMovie::startMovieService` | `0x7e01021b`, `0x7e02b290` |
| `0x30502` | `PlayMovie::play` | `0x7e0102aa`, `0x7e02b057` |
| `0x30503` | `PlayMovie::reversePlay` | `0x7e0102df`, `0x7e02b0b8` |
| `0x30504` | `PlayMovie::stop` | `0x7e0105ea`, `0x7e02b304` |
| `0x30505` | `PlayMovie::fastForward` | `0x7e010314`, `0x7e02af29` |
| `0x30506` | `PlayMovie::rewind` | `0x7e0103d1`, `0x7e02b119` |
| `0x30507` | `PlayMovie::pause` | `0x7e01048e`, `0x7e02aff6` |
| `0x30508` | `PlayMovie::forwardFrame` | `0x7e010580`, `0x7e02af95` |
| `0x30509` | `PlayMovie::rewindFrame` | `0x7e0105b5`, `0x7e02b185` |
| `0x3050a` | `PlayMovie::seek` | `0x7e0104c3`, `0x7e02b1e6` |
| `0x3050b` | `PlayMovie::endMovieService` | — |
| `0x30601` | `PlayRecord::start` | `0x7e010617`, `0x7e02b818` |
| `0x30602` | `PlayRecord::singleMode` | — |
| `0x30603` | `PlayRecord::record` | `0x7e010654`, `0x7e02b7b7` |
| `0x30604` | `PlayRecord::canRecord` | `0x7e010689`, `0x7e02b6f0` |
| `0x30605` | `PlayRecord::erase` | `0x7e0106b6`, `0x7e02b756` |
| `0x30606` | `PlayRecord::stop` | `0x7e0106e3`, `0x7e02b87d` |
| `0x30701` | `EditResize::start` | `0x7e01253e`, `0x7e02646e` |
| `0x30702` | `EditResize::getPossibleSize` | `0x7e012611`, `0x7e0262ef` |
| `0x30703` | `EditResize::moveCurrent` | — |
| `0x30704` | `EditResize::save` | `0x7e01278a`, `0x7e026402` |
| `0x30705` | `EditResize::makePreview` | `0x7e012688`, `0x7e026352` |
| `0x30706` | `EditResize::preCheck` | `0x7e012854`, `0x7e0263b7` |
| `0x30801` | `EditTrimming::start` | `0x7e012922`, `0x7e026a65` |
| `0x30802` | `EditTrimming::singleMode` | — |
| `0x30803` | `EditTrimming::indexMode` | — |
| `0x30804` | `EditTrimming::canTrimming` | `0x7e012955`, `0x7e0267a1` |
| `0x30805` | `EditTrimming::moveCurrent` | — |
| `0x30806` | `EditTrimming::getPageInfo` | — |
| `0x30807` | `EditTrimming::getCurrentInfo` | — |
| `0x30808` | `EditTrimming::trimmingMode` | `0x7e0129a1`, `0x7e026aca` |
| `0x30809` | `EditTrimming::changeSize` | `0x7e012c12`, `0x7e026875` |
| `0x3080a` | `EditTrimming::changePosition` | `0x7e012cb5`, `0x7e026807` |
| `0x3080b` | `EditTrimming::save` | `0x7e012eae`, `0x7e026a04` |
| `0x3080c` | `EditTrimming::startExpandAnimation` | — |
| `0x3080d` | `EditTrimming::getTrimmingInfo` | `0x7e012ad9`, `0x7e0268e3` |
| `0x3080e` | `EditTrimming::makePreview` | `0x7e012d72`, `0x7e026946` |
| `0x3080f` | `EditTrimming::preCheck` | `0x7e012ee3`, `0x7e0269ba` |
| `0x30901` | `EditColor::start` | `0x7e01347a`, `0x7e02539c` |
| `0x30902` | `EditColor::singleMode` | — |
| `0x30903` | `EditColor::indexMode` | — |
| `0x30904` | `EditColor::canColor` | `0x7e0134ad`, `0x7e0251c6` |
| `0x30905` | `EditColor::moveCurrent` | — |
| `0x30906` | `EditColor::getPageInfo` | — |
| `0x30907` | `EditColor::getCurrentInfo` | — |
| `0x30908` | `EditColor::colorEditMode` | — |
| `0x30909` | `EditColor::changeColor` | — |
| `0x3090a` | `EditColor::save` | `0x7e0137d9`, `0x7e02533b` |
| `0x3090b` | `EditColor::startExpandAnimation` | — |
| `0x3090c` | `EditColor::makePreview` | `0x7e0134da`, `0x7e0252a8` |
| `0x3090d` | `EditColor::makeComparePreview` | `0x7e013699` |
| `0x30a01` | `EditImageOverlay::adjustGain` | `0x7e014a25`, `0x7e025472` |
| `0x30a02` | `EditImageOverlay::canMoveCurrent` | `0x7e014569`, `0x7e0254e2` |
| `0x30a03` | `EditImageOverlay::getCurrentInfo` | `0x7e014528`, `0x7e0255b7` |
| `0x30a04` | `EditImageOverlay::getPageInfo` | `0x7e0144d3`, `0x7e025685` |
| `0x30a05` | `EditImageOverlay::index` | `0x7e0143d2`, `0x7e0256e8` |
| `0x30a06` | `EditImageOverlay::makeAdjustPreview` | `0x7e014880` |
| `0x30a07` | `EditImageOverlay::makePreview` | `0x7e014af2`, `0x7e0257dc` |
| `0x30a08` | `EditImageOverlay::moveCurrent` | `0x7e0146cf` |
| `0x30a09` | `EditImageOverlay::save` | `0x7e014bc0`, `0x7e025922` |
| `0x30a0a` | `EditImageOverlay::selectCurrent` | `0x7e014816`, `0x7e025983` |
| `0x30a0b` | `EditImageOverlay::start` | `0x7e01439f`, `0x7e0259e6` |
| `0x30a0c` | `EditImageOverlay::moveCurrentDirect` | `0x7e014bf5`, `0x7e0258b3` |
| `0x30a0d` | `EditImageOverlay::canOverlay` | `0x7e014c88`, `0x7e025556` |
| `0x30a0e` | `EditImageOverlay::getIndexInfo` | `0x7e014cb5`, `0x7e025618` |
| `0x30b01` | `EditRedEyeAdjust::start` | `0x7e013806`, `0x7e026219` |
| `0x30b02` | `EditRedEyeAdjust::singleMode` | — |
| `0x30b03` | `EditRedEyeAdjust::indexMode` | — |
| `0x30b04` | `EditRedEyeAdjust::canAdjust` | `0x7e013839`, `0x7e026094` |
| `0x30b05` | `EditRedEyeAdjust::moveCurrent` | — |
| `0x30b06` | `EditRedEyeAdjust::getPageInfo` | — |
| `0x30b07` | `EditRedEyeAdjust::getCurrentInfo` | — |
| `0x30b08` | `EditRedEyeAdjust::makePreview` | `0x7e013866`, `0x7e0260fa` |
| `0x30b09` | `EditRedEyeAdjust::save` | `0x7e0139a2`, `0x7e0261b8` |
| `0x30b0a` | `EditRedEyeAdjust::startExpandAnimation` | — |
| `0x30b0b` | `EditRedEyeAdjust::preCheck` | `0x7e0139d7`, `0x7e02616e` |
| `0x30c01` | `EditShadowAdjust::start` | `0x7e013a04`, `0x7e0266cb` |
| `0x30c02` | `EditShadowAdjust::singleMode` | — |
| `0x30c03` | `EditShadowAdjust::indexMode` | — |
| `0x30c04` | `EditShadowAdjust::canAdjust` | `0x7e013a37`, `0x7e026546` |
| `0x30c05` | `EditShadowAdjust::moveCurrent` | — |
| `0x30c06` | `EditShadowAdjust::getPageInfo` | — |
| `0x30c07` | `EditShadowAdjust::getCurrentInfo` | — |
| `0x30c08` | `EditShadowAdjust::save` | `0x7e013ba0`, `0x7e02666a` |
| `0x30c09` | `EditShadowAdjust::startExpandAnimation` | — |
| `0x30c0a` | `EditShadowAdjust::makePreview` | `0x7e013a64`, `0x7e0265ac` |
| `0x30c0b` | `EditShadowAdjust::preCheck` | `0x7e013bd5`, `0x7e026620` |
| `0x30d01` | `EditBeautyAdjust::start` | `0x7e013c02`, `0x7e024ef7` |
| `0x30d02` | `EditBeautyAdjust::singleMode` | — |
| `0x30d03` | `EditBeautyAdjust::indexMode` | — |
| `0x30d04` | `EditBeautyAdjust::canAdjust` | `0x7e013cc6`, `0x7e025037` |
| `0x30d05` | `EditBeautyAdjust::moveCurrent` | — |
| `0x30d06` | `EditBeautyAdjust::getPageInfo` | — |
| `0x30d07` | `EditBeautyAdjust::getCurrentInfo` | — |
| `0x30d08` | `EditBeautyAdjust::makeClearSkinPreview` | — |
| `0x30d09` | `EditBeautyAdjust::selectClearSkinPreview` | — |
| `0x30d0a` | `EditBeautyAdjust::executeAdjust` | `0x7e013d20`, `0x7e024fd6` |
| `0x30d0b` | `EditBeautyAdjust::save` | `0x7e013d55`, `0x7e024f6b` |
| `0x30d0c` | `EditBeautyAdjust::startExpandAnimation` | — |
| `0x30d0d` | `EditBeautyAdjust::startAdjustAnimation` | — |
| `0x30d0e` | `EditBeautyAdjust::endAdjustAnimation` | — |
| `0x30d0f` | `EditBeautyAdjust::startCompare` | `0x7e013d8a`, `0x7e0250fe` |
| `0x30d10` | `EditBeautyAdjust::getFaceInfo` | — |
| `0x30d11` | `EditBeautyAdjust::ready` | `0x7e013cf3`, `0x7e02509d` |
| `0x30e01` | `PlayPanorama::start` | `0x7e0210c5` |
| `0x30e02` | `PlayPanorama::getIndexPosition` | `0x7e021119`, `0x7e02b46c` |
| `0x30e03` | `PlayPanorama::startScroll` | `0x7e0211cd`, `0x7e02b5eb` |
| `0x30e04` | `PlayPanorama::getDisplayPosition` | `0x7e0211fa`, `0x7e02b420` |
| `0x30e05` | `PlayPanorama::stopScroll` | `0x7e02134b`, `0x7e02b635` |
| `0x30e06` | `PlayPanorama::manualScroll` | `0x7e021378`, `0x7e02b502` |
| `0x30e07` | `PlayPanorama::enlargeImage` | `0x7e021420`, `0x7e02b3d6` |
| `0x30e08` | `PlayPanorama::reduceImage` | `0x7e02144d`, `0x7e02b54d` |
| `0x30e09` | `PlayPanorama::getScrollDirection` | `0x7e02147a`, `0x7e02b4b8` |
| `0x30f01` | `PlaySlideShow::start` | `0x7e010dcc`, `0x7e02ce22` |
| `0x30f02` | `PlaySlideShow::startSlideShow` | `0x7e010e00`, `0x7e02ce87` |
| `0x30f03` | `PlaySlideShow::moveCurrent` | `0x7e010efd`, `0x7e02cd0b` |
| `0x30f04` | `PlaySlideShow::endSlideShow` | `0x7e010f8b`, `0x7e02cc48` |
| `0x30f05` | `PlaySlideShow::hasEvent` | — |
| `0x30f06` | `PlaySlideShow::hasCollection` | — |
| `0x30f07` | `PlaySlideShow::hasMyCinema` | — |
| `0x30f08` | `PlaySlideShow::collectionMode` | — |
| `0x30f09` | `PlaySlideShow::getCurrentPosition` | — |
| `0x30f0a` | `PlaySlideShow::getCollectionCount` | — |
| `0x30f0b` | `PlaySlideShow::moveCurrentCollection` | — |
| `0x30f0c` | `PlaySlideShow::selectCollection` | — |
| `0x30f0d` | `PlaySlideShow::startExpandAnimation` | — |
| `0x30f0e` | `PlaySlideShow::getCollectionPageInfo` | — |
| `0x30f0f` | `PlaySlideShow::canSlideShowGPU` | `0x7e010fb8`, `0x7e02cbe2` |
| `0x30f10` | `PlaySlideShow::startSlideShowGPU` | `0x7e010fe4`, `0x7e02cf1d` |
| `0x30f11` | `PlaySlideShow::skipPage` | `0x7e011015`, `0x7e02cdc1` |
| `0x30f12` | `PlaySlideShow::endSlideShowGPU` | `0x7e011042`, `0x7e02cca9` |
| `0x30f13` | `PlaySlideShow::setSelectPicDisable` | `0x7e011070`, `0x7e02cd77` |
| `0x31001` | `ReservePrint::start` | `0x7e010710`, `0x7e02d870` |
| `0x31002` | `ReservePrint::hasReservation` | `0x7e0107a4`, `0x7e02d6d6` |
| `0x31003` | `ReservePrint::eraseReservation` | `0x7e0107d1`, `0x7e02d5b2` |
| `0x31004` | `ReservePrint::singleMode` | `0x7e0107fa`, `0x7e02d80b` |
| `0x31005` | `ReservePrint::moveCurrent` | `0x7e0109c9`, `0x7e02d73c` |
| `0x31006` | `ReservePrint::canMoveCurrent` | `0x7e0108fb`, `0x7e02d3a2` |
| `0x31007` | `ReservePrint::changePrintCount` | `0x7e010ae6`, `0x7e02d4e5` |
| `0x31008` | `ReservePrint::hasPrintCount` | `0x7e010b8f`, `0x7e02d670` |
| `0x31009` | `ReservePrint::changeDatePrint` | `0x7e010bbc`, `0x7e02d47b` |
| `0x3100a` | `ReservePrint::reservePrint` | `0x7e010c77`, `0x7e02d7aa` |
| `0x3100b` | `ReservePrint::getPrintCount` | `0x7e010c4e`, `0x7e02d611` |
| `0x3100c` | `ReservePrint::canChangePrintCount` | `0x7e010ab9`, `0x7e02d33c` |
| `0x3100d` | `ReservePrint::end` | `0x7e010cac`, `0x7e02d553` |
| `0x3100e` | `ReservePrint::updateImageSync` | `0x7e010cd5`, `0x7e02d8e4` |
| `0x3100f` | `ReservePrint::canReserve` | `0x7e010d9f`, `0x7e02d416` |
| `0x31101` | `EditRotate::rotate` | — |
| `0x31102` | `EditRotate::canRotate` | — |
| `0x31201` | `EditProtect::changeProtect` | — |
| `0x31202` | `EditProtect::canProtect` | — |
| `0x31301` | `PlayCollage::start` | — |
| `0x31302` | `PlayCollage::moveCurrent` | — |
| `0x31303` | `PlayCollage::getCountInfo` | — |
| `0x31401` | `CopyPicture::start` | — |
| `0x31402` | `CopyPicture::moveCurrent` | — |
| `0x31403` | `CopyPicture::copy` | — |
| `0x31404` | `CopyPicture::end` | — |
| `0x31405` | `CopyPicture::copyAll` | — |
| `0x31501` | `PlayPhotoSurfing::registerCallback` | — |
| `0x31502` | `PlayPhotoSurfing::startPhotoSurfing` | — |
| `0x31503` | `PlayPhotoSurfing::getCurrentKeyword` | — |
| `0x31504` | `PlayPhotoSurfing::getRelevantPicNumber` | — |
| `0x31505` | `PlayPhotoSurfing::changeKeyword` | — |
| `0x31506` | `PlayPhotoSurfing::moveCurrent` | — |
| `0x31507` | `PlayPhotoSurfing::canMoveCurrent` | — |
| `0x31508` | `PlayPhotoSurfing::startSelectDate` | — |
| `0x31509` | `PlayPhotoSurfing::getDateArrow` | — |
| `0x3150a` | `PlayPhotoSurfing::changeDate` | — |
| `0x3150b` | `PlayPhotoSurfing::startSelectEvent` | — |
| `0x3150c` | `PlayPhotoSurfing::getDayTable` | — |
| `0x3150d` | `PlayPhotoSurfing::selectDate` | — |
| `0x3150e` | `PlayPhotoSurfing::startSelectSCN` | — |
| `0x3150f` | `PlayPhotoSurfing::canSCN` | — |
| `0x31510` | `PlayPhotoSurfing::displaySCNPic` | — |
| `0x31511` | `PlayPhotoSurfing::selectSCN` | — |
| `0x31512` | `PlayPhotoSurfing::startSelectPerson` | — |
| `0x31513` | `PlayPhotoSurfing::startSelectCollection` | — |
| `0x31514` | `PlayPhotoSurfing::getPageInfo` | — |
| `0x31515` | `PlayPhotoSurfing::getCursorPosition` | — |
| `0x31516` | `PlayPhotoSurfing::moveCurrentItem` | — |
| `0x31517` | `PlayPhotoSurfing::canMoveCurrentItem` | — |
| `0x31518` | `PlayPhotoSurfing::selectItem` | — |
| `0x31519` | `PlayPhotoSurfing::containsPicture` | — |
| `0x3151a` | `PlayPhotoSurfing::getPositionCandidate` | — |
| `0x3151b` | `PlayPhotoSurfing::setPosition` | — |
| `0x3151c` | `PlayPhotoSurfing::displayPositionPic` | — |
| `0x3151d` | `PlayPhotoSurfing::startExpandIcon` | — |
| `0x3151e` | `PlayPhotoSurfing::endExpandIcon` | — |
| `0x3151f` | `PlayPhotoSurfing::getPersonCount` | — |
| `0x31520` | `PlayPhotoSurfing::getCollectionCount` | — |
| `0x31601` | `PlayEventCollection::start` | — |
| `0x31602` | `PlayEventCollection::getCollectionNumber` | — |
| `0x31603` | `PlayEventCollection::getEventNumber` | — |
| `0x31604` | `PlayEventCollection::eventMode` | — |
| `0x31605` | `PlayEventCollection::collectionMode` | — |
| `0x31606` | `PlayEventCollection::getCurrentItemInfo` | — |
| `0x31607` | `PlayEventCollection::getItemPageInfo` | — |
| `0x31608` | `PlayEventCollection::moveCurrentItem` | — |
| `0x31609` | `PlayEventCollection::setItem` | — |
| `0x3160a` | `PlayEventCollection::singleMode` | — |
| `0x3160b` | `PlayEventCollection::updateImage` | — |
| `0x3160c` | `PlayEventCollection::enlargeImage` | — |
| `0x3160d` | `PlayEventCollection::reduceImage` | — |
| `0x3160e` | `PlayEventCollection::scrollImage` | — |
| `0x3160f` | `PlayEventCollection::isEnlarge` | — |
| `0x31610` | `PlayEventCollection::getEnlargeInfo` | — |
| `0x31611` | `PlayEventCollection::indexMode` | — |
| `0x31612` | `PlayEventCollection::getCurrentIndexInfo` | — |
| `0x31613` | `PlayEventCollection::getIndexPageInfo` | — |
| `0x31614` | `PlayEventCollection::moveCurrent` | — |
| `0x31615` | `PlayEventCollection::startExpandAnimation` | — |
| `0x31616` | `PlayEventCollection::endExpand` | — |
| `0x31617` | `PlayEventCollection::eraseTitle` | — |
| `0x31618` | `PlayEventCollection::getTitleInfo` | — |
| `0x31701` | `PlaySound::start` | `0x7e011099`, `0x7e02d066` |
| `0x31702` | `PlaySound::startPlay` | `0x7e0110cc`, `0x7e02d0cb` |
| `0x31703` | `PlaySound::stopPlay` | `0x7e011155`, `0x7e02d137` |
| `0x31704` | `PlaySound::setVolume` | `0x7e01118a`, `0x7e02cffa` |
| `0x31705` | `PlaySound::setSounds` | — |
| `0x31801` | `PlayEventView::initialize` | `0x7e0214a7`, `0x7e029db2` |
| `0x31802` | `PlayEventView::startEventView` | `0x7e0214da`, `0x7e029e00`, `0x7e029e50` |
| `0x31803` | `PlayEventView::endEventView` | `0x7e0216b4`, `0x7e029d0d` |
| `0x31804` | `PlayEventView::getCurrentInfo` | `0x7e029d58` |
| `0x31901` | `PlayContinuousShots::start` | `0x7e02083d` |
| `0x31902` | `PlayContinuousShots::play` | `0x7e020870` |
| `0x31903` | `PlayContinuousShots::pause` | `0x7e02089d` |
| `0x31904` | `PlayContinuousShots::seek` | `0x7e0208ca` |
| `0x31905` | `PlayContinuousShots::getPlayInfo` | `0x7e020982` |
| `0x31906` | `PlayContinuousShots::end` | `0x7e0209bd` |
| `0x31a01` | `EditAspect::start` | `0x7e012f10`, `0x7e024e21` |
| `0x31a02` | `EditAspect::canAspect` | `0x7e012f43`, `0x7e024c13` |
| `0x31a03` | `EditAspect::aspectMode` | `0x7e012f70`, `0x7e024b9f` |
| `0x31a04` | `EditAspect::changePosition` | `0x7e01322e`, `0x7e024c79` |
| `0x31a05` | `EditAspect::save` | `0x7e013445`, `0x7e024dc0` |
| `0x31a06` | `EditAspect::getAspectInfo` | `0x7e0130c3`, `0x7e024ce9` |
| `0x31a07` | `EditAspect::makePreview` | `0x7e0132eb`, `0x7e024d4c` |
| `0x31a08` | `EditAspect::end` | — |
| `0x31b01` | `EditRaw::save` | `0x7e013deb`, `0x7e025d40` |
| `0x31b02` | `EditRaw::canRaw` | `0x7e013db6`, `0x7e025abc` |
| `0x31b03` | `EditRaw::startCurrentModeEdit` | `0x7e013e26`, `0x7e025f39` |
| `0x31b04` | `EditRaw::previewCurrentModeEdit` | `0x7e013e62`, `0x7e025c5e` |
| `0x31b05` | `EditRaw::saveCurrentModeEdit` | `0x7e013f63`, `0x7e025e06` |
| `0x31b06` | `EditRaw::endCurrentModeEdit` | `0x7e013f98`, `0x7e025b88` |
| `0x31b07` | `EditRaw::startCustomEdit` | `0x7e01402a`, `0x7e025faa` |
| `0x31b08` | `EditRaw::previewCustomEdit` | `0x7e0140d4`, `0x7e025ccf` |
| `0x31b09` | `EditRaw::saveCustomEdit` | `0x7e0141d5`, `0x7e025e67` |
| `0x31b0a` | `EditRaw::endCustomEdit` | `0x7e01420a`, `0x7e025bf3` |
| `0x31b0b` | `EditRaw::startArtBktEdit` | `0x7e01429c`, `0x7e025ec8` |
| `0x31b0c` | `EditRaw::saveArtBktEdit` | `0x7e0142d8`, `0x7e025da5` |
| `0x31b0d` | `EditRaw::endArtBktEdit` | `0x7e01430d`, `0x7e025b1d` |
| `0x31c01` | `PlaySelect::start` | `0x7e00f9cf`, `0x7e02be01` |
| `0x31c02` | `PlaySelect::singleMode` | `0x7e00fac9`, `0x7e02bd8d` |
| `0x31c03` | `PlaySelect::indexMode` | `0x7e00fbe7`, `0x7e02bc28` |
| `0x31c04` | `PlaySelect::getPageInfo` | `0x7e00fd63` |
| `0x31c05` | `PlaySelect::getCurrentInfo` | `0x7e00fdba`, `0x7e02baeb` |
| `0x31c06` | `PlaySelect::moveCurrent` | `0x7e00ff0e` |
| `0x31c07` | `PlaySelect::canMoveCurrent` | `0x7e00fde8`, `0x7e02b94f` |
| `0x31c08` | `PlaySelect::expandAnimation` | `0x7e0100fd`, `0x7e02ba8a` |
| `0x31c09` | `PlaySelect::canRotate` | `0x7e02b9c3` |
| `0x31c0a` | `PlaySelect::rotateImage` | `0x7e02bd19` |
| `0x31c0b` | `PlaySelect::getIndexInfo` | `0x7e010132`, `0x7e02bb4e` |
| `0x31c0c` | `PlaySelect::changeSelectedFrame` | `0x7e01017f`, `0x7e02ba29` |
| `0x31c0d` | `PlaySelect::updateImageSync` | `0x7e0101b4`, `0x7e02be75` |
| `0x31d01` | `PlayLightBox::start` | `0x7e0118f2` |
| `0x31d02` | `PlayLightBox::setScrollTarget` | `0x7e011963`, `0x7e02ac31` |
| `0x31d03` | `PlayLightBox::scrollImage` | `0x7e011e75`, `0x7e02ab64` |
| `0x31d04` | `PlayLightBox::setBase` | `0x7e011e48`, `0x7e02abd0` |
| `0x31d05` | `PlayLightBox::canMoveCurrent` | `0x7e011f32`, `0x7e02a82b` |
| `0x31d06` | `PlayLightBox::moveCurrent` | `0x7e012037`, `0x7e02aaf6` |
| `0x31d07` | `PlayLightBox::getEnlargeInfo` | `0x7e011a0b`, `0x7e02a9c6` |
| `0x31d08` | `PlayLightBox::zoomImage` | `0x7e0121ab`, `0x7e02ae49` |
| `0x31d09` | `PlayLightBox::updateImage` | `0x7e012144`, `0x7e02ade4` |
| `0x31d0a` | `PlayLightBox::isSameNumber` | `0x7e012242`, `0x7e02aa90` |
| `0x31d0b` | `PlayLightBox::singleMode` | `0x7e012277`, `0x7e02ac9d` |
| `0x31d0c` | `PlayLightBox::singleModeUpdate` | `0x7e012302`, `0x7e02ad0b` |
| `0x31d0d` | `PlayLightBox::eraseCurrent` | `0x7e01238d`, `0x7e02a900` |
| `0x31d0e` | `PlayLightBox::erase` | `0x7e0123c2`, `0x7e02a89f` |
| `0x31d0f` | `PlayLightBox::getNumber` | `0x7e0123f7`, `0x7e02aa2b` |
| `0x31d10` | `PlayLightBox::getAFFineTuneValue` | `0x7e012456`, `0x7e02a961` |
| `0x31e01` | `PlayCalendar::start` | `0x7e011350` |
| `0x31e02` | `PlayCalendar::getDateRange` | `0x7e011457` |
| `0x31e03` | `PlayCalendar::getCursorPosition` | `0x7e01151d`, `0x7e028f5c` |
| `0x31e04` | `PlayCalendar::getPresenceImage` | `0x7e01155c`, `0x7e02902a` |
| `0x31e05` | `PlayCalendar::MoveCursor` | `0x7e011605`, `0x7e02909b` |
| `0x31e06` | `PlayCalendar::canMovePage` | `0x7e01171f`, `0x7e028e87` |
| `0x31e07` | `PlayCalendar::movePage` | `0x7e0117c1`, `0x7e02911e` |
| `0x31e08` | `PlayCalendar::end` | `0x7e029206` |
| `0x31f01` | `SelectOverlay::start` | `0x7e014d02`, `0x7e02e233` |
| `0x31f02` | `SelectOverlay::index` | `0x7e014d3d`, `0x7e02e0df` |
| `0x31f03` | `SelectOverlay::getPageInfo` | `0x7e014e50`, `0x7e02e07c` |
| `0x31f04` | `SelectOverlay::getCurrentInfo` | `0x7e014ea6`, `0x7e02dfae` |
| `0x31f05` | `SelectOverlay::canMoveCurrent` | `0x7e014ee7`, `0x7e02df3a` |
| `0x31f06` | `SelectOverlay::moveCurrent` | `0x7e015016` |
| `0x31f07` | `SelectOverlay::selectCurrent` | `0x7e01515d`, `0x7e02e1cb` |
| `0x31f08` | `SelectOverlay::scaleCreate` | — |
| `0x31f09` | `SelectOverlay::getIndexInfo` | `0x7e015192`, `0x7e02e00f` |
| `0x32001` | `ReserveUpload::changeUpload` | `0x7e01fd48`, `0x7e02de31` |
| `0x32002` | `ReserveUpload::isUpload` | `0x7e01fd7b`, `0x7e02de7f` |
| `0x32003` | `ReserveUpload::canUpload` | `0x7e01fda8`, `0x7e02dde7` |
| `0x32101` | `ReserveTransfer::start` | `0x7e0209ea`, `0x7e02dcde` |
| `0x32102` | `ReserveTransfer::singleMode` | `0x7e020a1d`, `0x7e02dc91` |
| `0x32103` | `ReserveTransfer::indexMode` | `0x7e020abe` |
| `0x32104` | `ReserveTransfer::getPageInfo` | `0x7e020b39`, `0x7e02da6c` |
| `0x32105` | `ReserveTransfer::getCurrentInfo` | `0x7e020b89`, `0x7e02da1c` |
| `0x32106` | `ReserveTransfer::canMoveCurrent` | `0x7e020bed`, `0x7e02d9c9` |
| `0x32107` | `ReserveTransfer::moveCurrent` | `0x7e020cbb` |
| `0x32108` | `ReserveTransfer::selectCurrent` | `0x7e020d9e`, `0x7e02dc45` |
| `0x32109` | `ReserveTransfer::getSelectPicNumber` | `0x7e020ddc`, `0x7e02daba` |
| `0x3210a` | `ReserveTransfer::startExpandAnimation` | `0x7e020e0a`, `0x7e02dd2c` |
| `0x3210b` | `ReserveTransfer::reserveTransferSelected` | `0x7e020e37`, `0x7e02dbfb` |
| `0x3210c` | `ReserveTransfer::reserveTransferAll` | `0x7e020e64`, `0x7e02dbad` |
| `0x32201` | `EditBeautyMake::canAdjust` | — |
| `0x32202` | `EditBeautyMake::start` | — |
| `0x32203` | `EditBeautyMake::getFaceInfo` | — |
| `0x32204` | `EditBeautyMake::makePreview` | — |
| `0x32205` | `EditBeautyMake::makeFacePreview` | — |
| `0x32206` | `EditBeautyMake::makeComparePreview` | — |
| `0x32207` | `EditBeautyMake::setParam` | — |
| `0x32208` | `EditBeautyMake::getParam` | — |
| `0x32209` | `EditBeautyMake::loadParam` | — |
| `0x3220a` | `EditBeautyMake::saveParam` | — |
| `0x3220b` | `EditBeautyMake::preCheck` | — |
| `0x3220c` | `EditBeautyMake::executeAdjust` | — |
| `0x3220d` | `EditBeautyMake::isEnlarge` | — |
| `0x3220e` | `EditBeautyMake::getEnlargeInfo` | — |
| `0x3220f` | `EditBeautyMake::enlargeImage` | — |
| `0x32210` | `EditBeautyMake::reduceImage` | — |
| `0x32211` | `EditBeautyMake::scrollImage` | — |
| `0x40101` | `SelfAdjust::readyExecuteSelfAdjust` | `0x7e0151df`, `0x7e02ea8e` |
| `0x40102` | `SelfAdjust::execute` | `0x7e01526c` |
| `0x40103` | `SelfAdjust::getMode` | `0x7e01570c`, `0x7e02e714` |
| `0x40104` | `SelfAdjust::getMenuItemNumber` | `0x7e01577e`, `0x7e02e6b3` |
| `0x40105` | `SelfAdjust::getMenuItem` | `0x7e0157ab`, `0x7e02e645` |
| `0x40106` | `SelfAdjust::getDefaultItem` | `0x7e015adc`, `0x7e02e4e5` |
| `0x40107` | `SelfAdjust::getSelectItemNumber` | `0x7e015d8c`, `0x7e02e9b2` |
| `0x40108` | `SelfAdjust::getSelectItem` | `0x7e016036`, `0x7e02e944` |
| `0x40109` | `SelfAdjust::getBeforeAction` | `0x7e01670c`, `0x7e02e3a8` |
| `0x4010a` | `SelfAdjust::getString` | `0x7e016fb2`, `0x7e02ea1e` |
| `0x4010b` | `SelfAdjust::getLineInfo` | `0x7e0172a2`, `0x7e02e5d7` |
| `0x4010c` | `SelfAdjust::getErrorStatus` | `0x7e02e548` |
| `0x4010d` | `SelfAdjust::startThrough` | `0x7e017627`, `0x7e02eafa` |
| `0x4010e` | `SelfAdjust::stopThrough` | `0x7e017654`, `0x7e02eb44` |
| `0x4010f` | `SelfAdjust::turnOnTFT` | `0x7e0175cd`, `0x7e02ebef` |
| `0x40110` | `SelfAdjust::turnOffTFT` | `0x7e0175fa`, `0x7e02eb8e` |
| `0x40111` | `SelfAdjust::getResultInfo` | `0x7e017681`, `0x7e02e83c` |
| `0x40112` | `SelfAdjust::getResultString` | `0x7e0176e8`, `0x7e02e8b3` |
| `0x40113` | `SelfAdjust::getNextMenuItem` | `0x7e0177a8`, `0x7e02e775` |
| `0x40114` | `SelfAdjust::getResolutionInfo` | `0x7e0177d5`, `0x7e02e7bf` |
| `0x40115` | `SelfAdjust::getContentsNumber` | `0x7e017958`, `0x7e02e484` |
| `0x40116` | `SelfAdjust::getContentsItem` | `0x7e017985`, `0x7e02e416` |
| `0x40201` | `LifeTest::execute` | `0x7e017a78` |
| `0x40202` | `LifeTest::getLifeTestMode` | `0x7e017c78`, `0x7e028926` |
| `0x40203` | `LifeTest::getLifeTestCount` | `0x7e017caf`, `0x7e0288c1` |
| `0x40204` | `LifeTest::abortLifeTest` | `0x7e017d0e`, `0x7e0287ea` |
| `0x40205` | `LifeTest::reset` | `0x7e017d37`, `0x7e028989` |
| `0x40301` | `Relocate::registerCode` | `0x7e017d60`, `0x7e02d26a` |
| `0x40302` | `Relocate::eraseCode` | `0x7e017d94`, `0x7e02d209` |
| `0x40401` | `Maintenance::getApiVersion` | `0x7dff73ef`, `0x7e017dc9` |
| `0x40402` | `Maintenance::getNumberOfSystemName` | `0x7dff76e6`, `0x7e017e27` |
| `0x40403` | `Maintenance::getSystemName` | `0x7dff7839`, `0x7e017e55` |
| `0x40404` | `Maintenance::getShippingInfo` | `0x7dff77c7`, `0x7e017f89` |
| `0x40405` | `Maintenance::getSystemVersion` | `0x7dff78ab`, `0x7e017ff3` |
| `0x40406` | `Maintenance::getMaintenanceData` | `0x7dff7674`, `0x7e018073` |
| `0x40407` | `Maintenance::getSerialNumber` | `0x7dff7756` |
| `0x40408` | `Maintenance::getDamageInfo` | `0x7dff74db`, `0x7e018188` |
| `0x40409` | `Maintenance::clearDamageInfo` | `0x7dff7382`, `0x7e018247` |
| `0x4040d` | `Maintenance::getGpsModuleVersion` | `0x7dff7617` |
| `0x4040e` | `Maintenance::getDestinationArea` | `0x7dff754d` |
| `0x4040f` | `Maintenance::setDestinationArea` | `0x7dff791d` |
| `0x40410` | `Maintenance::getChangeDestinationArea` | `0x7dff745f` |
| `0x40411` | `Maintenance::getDestinationString` | `0x7dff75b1`, `0x7e01842f` |
| `0x50101` | `DeviceLink::connect` | `0x7e019f92`, `0x7e02451f` |
| `0x50102` | `DeviceLink::disconnect` | `0x7e01a055`, `0x7e024593` |
| `0x50103` | `DeviceLink::getStatus` | `0x7e01a08a`, `0x7e0245f4` |
| `0x50104` | `DeviceLink::isCommunication` | `0x7e01a246`, `0x7e024657` |
| `0x50201` | `EasyPrint::startEasyPrintService` | `0x7e0184bb`, `0x7e02472e` |
| `0x50202` | `EasyPrint::select` | `0x7e018565`, `0x7e0247a2` |
| `0x50203` | `EasyPrint::canMoveCurrent` | `0x7e0185a5`, `0x7e024a61` |
| `0x50204` | `EasyPrint::moveCurrent` | `0x7e018688`, `0x7e024805` |
| `0x50205` | `EasyPrint::print` | `0x7e018785`, `0x7e024873` |
| `0x50206` | `EasyPrint::abortPrint` | `0x7e0187ef`, `0x7e0248d4` |
| `0x50207` | `EasyPrint::continuePrint` | `0x7e0187ba`, `0x7e02493f` |
| `0x50208` | `EasyPrint::endEasyPrintService` | `0x7e0189b8`, `0x7e0249a0` |
| `0x50209` | `EasyPrint::getStillImageCount` | `0x7e018757`, `0x7e0249ff` |
| `0x5020a` | `EasyPrint::getFrameInfo` | `0x7e018824`, `0x7e024ad5` |
| `0x50301` | `CustomPrint::startCustomPrintService` | `0x7e018cf9`, `0x7e0238cc` |
| `0x50302` | `CustomPrint::setPrintMode` | `0x7e018dbd`, `0x7e02379c` |
| `0x50303` | `CustomPrint::getPaperSetting` | `0x7e018e87`, `0x7e0234c6` |
| `0x50304` | `CustomPrint::changePaperSize` | `0x7e018ecd`, `0x7e02322e` |
| `0x50305` | `CustomPrint::changeBorderSetting` | `0x7e018f9a`, `0x7e023058` |
| `0x50306` | `CustomPrint::changeMultiCount` | `0x7e019067`, `0x7e0231a9` |
| `0x50307` | `CustomPrint::setPaperSetting` | `0x7e019134`, `0x7e02373b` |
| `0x50308` | `CustomPrint::singleMode` | `0x7e019169`, `0x7e023869` |
| `0x50309` | `CustomPrint::indexMode` | `0x7e019249`, `0x7e02358c` |
| `0x5030a` | `CustomPrint::detailMode` | `0x7e01940f`, `0x7e0233fa` |
| `0x5030b` | `CustomPrint::canMoveCurrent` | `0x7e0194b7`, `0x7e023be4` |
| `0x5030c` | `CustomPrint::moveCurrent` | `0x7e0195dd` |
| `0x5030d` | `CustomPrint::changePrintCount` | `0x7e0197f8`, `0x7e02331f` |
| `0x5030e` | `CustomPrint::changeDatePrint` | `0x7e0198ae`, `0x7e0230dd` |
| `0x5030f` | `CustomPrint::changeFileNamePrint` | `0x7e0198db`, `0x7e023143` |
| `0x50310` | `CustomPrint::setPrintSetting` | `0x7e019908`, `0x7e023808` |
| `0x50311` | `CustomPrint::resetPrintSetting` | `0x7e01993d`, `0x7e0236da` |
| `0x50312` | `CustomPrint::canDetailSetting` | `0x7e019972` |
| `0x50313` | `CustomPrint::trimmingMode` | `0x7e019a6e`, `0x7e023d83` |
| `0x50314` | `CustomPrint::changeSize` | `0x7e019caf`, `0x7e02338e` |
| `0x50315` | `CustomPrint::changePosition` | `0x7e019d45`, `0x7e0232b3` |
| `0x50316` | `CustomPrint::setTrimming` | `0x7e019e02`, `0x7e023cbb` |
| `0x50317` | `CustomPrint::print` | `0x7e019e7a`, `0x7e023679` |
| `0x50318` | `CustomPrint::abortPrint` | `0x7e019ee4`, `0x7e022f8e` |
| `0x50319` | `CustomPrint::getSupportedPrintMode` | `0x7e018d34`, `0x7e023529` |
| `0x5031a` | `CustomPrint::endCustomPrintService` | `0x7e019f19`, `0x7e02345d` |
| `0x5031b` | `CustomPrint::getPageInfo` | `0x7e019746`, `0x7e023992` |
| `0x5031c` | `CustomPrint::startExpandAnimation` | `0x7e019796`, `0x7e023931` |
| `0x5031d` | `CustomPrint::canPrint` | `0x7e0197cb`, `0x7e0239f5` |
| `0x5031e` | `CustomPrint::continuePrint` | `0x7e019eaf`, `0x7e023a5b` |
| `0x5031f` | `CustomPrint::getStillImageCount` | `0x7e019718`, `0x7e023b1f` |
| `0x50320` | `CustomPrint::getPrintCount` | `0x7e019f42`, `0x7e023abc` |
| `0x50321` | `CustomPrint::getTrimmingInfo` | `0x7e019b76`, `0x7e023b81` |
| `0x50322` | `CustomPrint::makePreview` | `0x7e019e37`, `0x7e023c58` |
| `0x50401` | `Bluetooth::startCommunication` | `0x7e01a375`, `0x7e022dee` |
| `0x50402` | `Bluetooth::stopCommunication` | `0x7e01a3ae`, `0x7e022e53` |
| `0x50403` | `Bluetooth::requestConnection` | `0x7e01a3e8`, `0x7e022a4d` |
| `0x50404` | `Bluetooth::cancelConnection` | `0x7e01a5a0`, `0x7e0222c0` |
| `0x50405` | `Bluetooth::searchDevice` | `0x7e01a5da`, `0x7e022b1b` |
| `0x50406` | `Bluetooth::cancelSearchDevice` | `0x7e01a677`, `0x7e0223ef` |
| `0x50407` | `Bluetooth::sendImage` | `0x7e01a6b1`, `0x7e022b90` |
| `0x50408` | `Bluetooth::cancelSendImage` | `0x7e01a6eb`, `0x7e022454` |
| `0x50409` | `Bluetooth::requestPairing` | `0x7e01a725`, `0x7e022ab4` |
| `0x5040a` | `Bluetooth::cancelPairing` | `0x7e01a8ca`, `0x7e022325` |
| `0x5040b` | `Bluetooth::waitRequest` | `0x7e01a904`, `0x7e022eb8` |
| `0x5040c` | `Bluetooth::abortWaitRequest` | `0x7e01a93e`, `0x7e02218f` |
| `0x5040d` | `Bluetooth::acceptPairing` | `0x7e01a978`, `0x7e022259` |
| `0x5040e` | `Bluetooth::rejectPairing` | `0x7e01aabb`, `0x7e022985` |
| `0x5040f` | `Bluetooth::acceptConnection` | `0x7e01aaf5`, `0x7e0221f4` |
| `0x50410` | `Bluetooth::rejectConnection` | `0x7e01ab2f`, `0x7e022920` |
| `0x50411` | `Bluetooth::receiveImage` | `0x7e01ab69`, `0x7e022856` |
| `0x50412` | `Bluetooth::cancelReceiveImage` | `0x7e01acac`, `0x7e02238a` |
| `0x50413` | `Bluetooth::removePairingDevice` | `0x7e01ace6`, `0x7e0229ea` |
| `0x50414` | `Bluetooth::sendPinCode` | `0x7e01ad97`, `0x7e022bf5` |
| `0x50415` | `Bluetooth::createSendImage` | `0x7e01ae83`, `0x7e0224b9` |
| `0x50416` | `Bluetooth::getSearchDeviceCount` | `0x7e01aeb6`, `0x7e02277e` |
| `0x50417` | `Bluetooth::getSearchDeviceList` | `0x7e01aefb`, `0x7e0227e1` |
| `0x50418` | `Bluetooth::getPairingDeviceCount` | `0x7e01afd5`, `0x7e022643` |
| `0x50419` | `Bluetooth::getPairingDeviceList` | `0x7e01b01a`, `0x7e0226a6` |
| `0x5041a` | `Bluetooth::getPairingResult` | `0x7e01b0f4`, `0x7e02271b` |
| `0x5041b` | `Bluetooth::getCommingDeviceInfo` | `0x7e01b139`, `0x7e02257d` |
| `0x5041c` | `Bluetooth::recordReceiveImage` | `0x7e01b17e`, `0x7e0228bd` |
| `0x5041d` | `Bluetooth::getMyDeviceInfo` | `0x7e01b22c`, `0x7e0225e0` |
| `0x5041e` | `Bluetooth::setMyDeviceName` | `0x7e01b271`, `0x7e022c58` |
| `0x5041f` | `Bluetooth::setPairingDeviceName` | `0x7e01b399`, `0x7e022cbb` |
| `0x50420` | `Bluetooth::showSendImage` | `0x7e01b4d5`, `0x7e022d87` |
| `0x50421` | `Bluetooth::showReceiveImage` | `0x7e01b632`, `0x7e022d20` |
| `0x50422` | `Bluetooth::getAuthNumber` | `0x7e01b790`, `0x7e02251a` |
| `0x50501` | `TouchPanel::startTouchPanel` | `0x7e003f7b`, `0x7e0348c1` |
| `0x50502` | `TouchPanel::endTouchPanel` | `0x7e004032`, `0x7e0346c9` |
| `0x50503` | `TouchPanel::ctrlTouchPanelEvent` | `0x7e004065`, `0x7e034666` |
| `0x50504` | `TouchPanel::getTouchPanelState` | `0x7e00419e`, `0x7e0347f5` |
| `0x50505` | `TouchPanel::getTouchNumber` | `0x7e0041d1`, `0x7e03472a` |
| `0x50506` | `TouchPanel::getTouchPanelHistory` | `0x7e0041ff`, `0x7e03478d` |
| `0x50507` | `TouchPanel::isTouchDetection` | `0x7e0043f0`, `0x7e03485b` |
| `0x50601` | `FlashAir::isFlashAir` | `0x7e01f8ab`, `0x7e027043` |
| `0x50602` | `FlashAir::getSettingStatus` | `0x7e01f8e2`, `0x7e026f27` |
| `0x50603` | `FlashAir::getWifiSetting` | `0x7e01f93a`, `0x7e026f88` |
| `0x50604` | `FlashAir::getWifiStatus` | `0x7e01f974`, `0x7e026fdd` |
| `0x50605` | `FlashAir::setWifiSSID` | `0x7e01f9ac`, `0x7e0271c4` |
| `0x50606` | `FlashAir::setWifiPassword` | `0x7e01f9fb`, `0x7e027161` |
| `0x50607` | `FlashAir::getOneTimePassword` | `0x7e01fa4b`, `0x7e026e7c` |
| `0x50608` | `FlashAir::setOneTimePassword` | `0x7e01fa8b`, `0x7e0270a9` |
| `0x50609` | `FlashAir::connect` | `0x7e01fadf`, `0x7e026ddd` |
| `0x5060a` | `FlashAir::disconnect` | `0x7e01fb93`, `0x7e026e32` |
| `0x5060b` | `FlashAir::getSettingMode` | `0x7e01fbc8`, `0x7e026ec6` |
| `0x5060c` | `FlashAir::setSettingMode` | `0x7e01fc00`, `0x7e0270f5` |
| `0x50701` | `InternalWiFi::connect` | `0x7e0217f2`, `0x7e027b91` |
| `0x50702` | `InternalWiFi::disconnect` | `0x7e021888`, `0x7e027be6` |
| `0x50703` | `InternalWiFi::changePassword` | `0x7e021752`, `0x7e027b25` |
| `0x50704` | `InternalWiFi::getWiFiSetting` | `0x7e0218b3` |
| `0x50705` | `InternalWiFi::getWiFiStatus` | `0x7e0219ff`, `0x7e027cd0` |
| `0x50706` | `InternalWiFi::notifyReleaseModeStartComplete` | `0x7e021af5`, `0x7e027ec1` |
| `0x50707` | `InternalWiFi::notifyReleaseModeEndComplete` | `0x7e021b4b`, `0x7e027dff` |
| `0x50708` | `InternalWiFi::notifyReleaseModeEndStart` | `0x7e021b20`, `0x7e027e60` |
| `0x50709` | `InternalWiFi::notifyStartWiFiRemoteTake` | `0x7e021b76`, `0x7e027f22` |
| `0x5070a` | `InternalWiFi::notifyEndWiFiRemoteTake` | `0x7e021ba9`, `0x7e027d9e` |
| `0x5070b` | `InternalWiFi::notifyChangeWiFiModeDial` | `0x7e021bdc`, `0x7e027d3d` |
| `0x60101` | `YCameraGuide::getHeadword` | — |
| `0x60102` | `YCameraGuide::getKeyword` | — |
| `0x60103` | `YCameraGuide::getWordList` | — |
| `0x60104` | `YCameraGuide::getContents` | — |
| `0x60105` | `YCameraGuide::getFuncList` | — |
| `0x60106` | `YCameraGuide::getNodeList` | — |
| `0x60107` | `YCameraGuide::getHistList` | — |
| `0x60108` | `YCameraGuide::getRelInfo` | — |
| `0x60109` | `YCameraGuide::deleteHist` | — |
| `0x6010a` | `YCameraGuide::deleteAllHist` | — |
| `0x6010b` | `YCameraGuide::resetHist` | — |
| `0x6010c` | `YCameraGuide::queryFreq` | — |
| `0x6010d` | `YCameraGuide::startGuideService` | — |
| `0x6010e` | `YCameraGuide::endGuideService` | — |
| `0x6010f` | `YCameraGuide::getFreqInfoCnt` | — |
| `0x60110` | `YCameraGuide::getHistInfoCnt` | — |
| `0x60111` | `YCameraGuide::setResultBuffer` | — |
| `0x60112` | `YCameraGuide::hasWriteBackData` | — |
| `0x60113` | `YCameraGuide::isInitialPopup` | — |
| `0x60114` | `YCameraGuide::isWriteBackDataPopup` | — |

## API result codes

The trace line `RET: %s` prints a result code by name. The names come from a table of `{name, code}` pairs at
`0x7e361558` (108 entries, read by the function at `0x7dfc717c`). Success codes are small numbers; error codes
are `0xf00000NN`.

| code | name | code | name |
|---|---|---|---|
| `0x1` | `API_SUCCESS` | `0x2` | `API_SUCCESS_CONF_COMPLETE` |
| `0x3` | `API_SUCCESS_DELETE_COMPLETE` | `0x4` | `API_SUCCESS_DISP_COMPLETE` |
| `0x5` | `API_SUCCESS_EDIT_COMPLETE` | `0x6` | `API_SUCCESS_ERASE_COMPLETE` |
| `0x7` | `API_SUCCESS_READ_COMPLETE` | `0x8` | `API_SUCCESS_RECORDING_COMPLETE` |
| `0x9` | `API_SUCCESS_SEARCH_COMPLETE` | `0xa` | `API_SUCCESS_SLIDE_SHOW` |
| `0xb` | `API_SUCCESS_SOUND_COMPLETE` | `0xc` | `API_SUCCESS_STOP` |
| `0xd` | `API_SUCCESS_NO_IMAGE` | `0xf1000001` | `API_SUCCESS_NO_PAINT` |
| `0xf1000002` | `API_ENLARGE_MAX` | `0xf1000003` | `API_REDUCE_MIN` |
| `0xf1000004` | `API_SCROLL_MAX` | `0xf1000005` | `API_NO_MAIN_IMAGE` |
| `0xf1000006` | `API_NO_SOUND_DATA` | `0xf0000001` | `API_NO_SOUND_PLAY` |
| `0xf0000002` | `API_ERROR_FAIL` | `0xf0000003` | `API_ERROR_BEGIN_SELECTION` |
| `0xf0000004` | `API_ERROR_CANCEL` | `0xf0000005` | `API_ERROR_CANNOT_PRINT` |
| `0xf0000006` | `API_ERROR_CANNOT_READY` | `0xf0000007` | `API_ERROR_CANT_PRINT` |
| `0xf0000008` | `API_ERROR_CARD_PROTECTED` | `0xf0000009` | `API_ERROR_COMM_FAULT` |
| `0xf000000a` | `API_ERROR_CONNECTED` | `0xf000000b` | `API_ERROR_CONNECTING` |
| `0xf000000c` | `API_ERROR_DEVICE_CHECK` | `0xf000000d` | `API_ERROR_DISCONNECT` |
| `0xf000000e` | `API_ERROR_DISP_FAIL` | `0xf000000f` | `API_ERROR_END_SELECTION` |
| `0xf0000010` | `API_ERROR_ENDED_PANORAMA` | `0xf0000011` | `API_ERROR_EXECUTE_SHOOTING` |
| `0xf0000012` | `API_ERROR_FILE_NOT_FOUND` | `0xf0000013` | `API_ERROR_FIRST_FRAME` |
| `0xf0000014` | `API_ERROR_IMPOSSIBLE` | `0xf0000015` | `API_ERROR_INIT_HIST` |
| `0xf0000016` | `API_ERROR_INIT_TERM` | `0xf0000017` | `API_ERROR_INVALID_ARG` |
| `0xf0000018` | `API_ERROR_INVALID_CALL` | `0xf0000019` | `API_ERROR_LAST_FRAME` |
| `0xf000001a` | `API_ERROR_LINK_CONNECTED` | `0xf000001b` | `API_ERROR_LINK_CONNECTING` |
| `0xf000001c` | `API_ERROR_LINK_DISCONNECT` | `0xf000001d` | `API_ERROR_LIST_OVER` |
| `0xf000001e` | `API_ERROR_MAX_PRINT` | `0xf000001f` | `API_ERROR_MAX_SHOOT_COUNT` |
| `0xf0000021` | `API_ERROR_MEDIA_FORMAT` | `0xf0000022` | `API_ERROR_MOVE_CURSOR` |
| `0xf0000023` | `API_ERROR_MULTI_THROUGH` | `0xf0000024` | `API_ERROR_NO_FACE` |
| `0xf0000025` | `API_ERROR_NO_IMAGE` | `0xf0000026` | `API_ERROR_NO_PICTURE` |
| `0xf0000028` | `API_ERROR_NO_PRINT_TARGET` | `0xf0000029` | `API_ERROR_NO_SUPPORT` |
| `0xf000002a` | `API_ERROR_NO_SUPPORT_CONFLICT` | `0xf000002b` | `API_ERROR_NO_WINDOW` |
| `0xf000002c` | `API_ERROR_NOT_MULTI_THROUGH` | `0xf000002d` | `API_ERROR_NOT_PRINTING` |
| `0xf000002e` | `API_ERROR_NOT_PROCESS` | `0xf000002f` | `API_ERROR_NOT_RECVIEW_READY` |
| `0xf0000030` | `API_ERROR_NOT_SELF_TIMER` | `0xf0000031` | `API_ERROR_NOT_STOP` |
| `0xf0000032` | `API_ERROR_NOT_SUPPORT` | `0xf0000033` | `API_ERROR_NOT_ZOOMING` |
| `0xf0000034` | `API_ERROR_NULL_POINTER_ARG` | `0xf0000035` | `API_ERROR_OUT_OF_RANGE` |
| `0xf0000036` | `API_ERROR_PANORAMA_SETTING` | `0xf0000037` | `API_ERROR_PAPER_EDGE` |
| `0xf0000039` | `API_ERROR_PAPER_SIZE` | `0xf000003a` | `API_ERROR_PRINTING` |
| `0xf000003b` | `API_ERROR_PROTECTED` | `0xf000003c` | `API_ERROR_READ_FAIL` |
| `0xf000003d` | `API_ERROR_READY_SHOOTING` | `0xf000003f` | `API_ERROR_RESERVE_MAX` |
| `0xf0000040` | `API_ERROR_RESTRICTION` | `0xf0000041` | `API_ERROR_SHOOTING_MODE` |
| `0xf0000042` | `API_ERROR_SIZE_OVER` | `0xf0000043` | `API_ERROR_STOP_THROUGH` |
| `0xf0000044` | `API_ERROR_TIMEOUT` | `0xf0000045` | `API_ERROR_UNKNOWN_MODE` |
| `0xf0000046` | `API_ERROR_W_NOTFOUND` | `0xf0000047` | `API_ERROR_ZOOM_END` |
| `0xf0000048` | `API_ERROR_ZOOMING` | `0xf0000049` | `API_ERROR_FILE_CHECK` |
| `0xf000004a` | `API_ERROR_DISABLE_FUNCTION` | `0xf000004b` | `API_ERROR_NO_DPOF` |
| `0xf000004c` | `API_ERROR_PRINT_PAPER` | `0xf000004d` | `API_ERROR_PRINT_INK` |
| `0xf000004e` | `API_ERROR_PRINT_JAMMING` | `0xf000004f` | `API_ERROR_PRINTER` |
| `0xf0000050` | `API_ERROR_CARD_FULL` | `0xf0000051` | `API_ERROR_NO_DATABASE` |
| `0xf0000052` | `API_ERROR_NO_ANIMATION` | `0xf0000053` | `API_ERROR_CONNECT_PRINTER` |
| `0xf0000054` | `API_ERROR_ENLARGE_THUMBNAIL` | `0xf0000055` | `API_ERROR_NO_SELECT_PIC` |
| `0xf0000056` | `API_ERROR_ZOOM` | `0xf0000057` | `API_ERROR_LENS_SETUP` |
| `0xf0000058` | `API_ERROR_NOT_ORIGINAL` | `0xf0000059` | `API_ERROR_UNRESPONSIVE` |
| `0xf000005a` | `API_ERROR_AVCHD` | `0xf000005b` | `API_ERROR_BAD_IMAGE` |
| `0xf000005c` | `API_ERROR_MEDIA_SHORTAGE` | `0xffff` | `API_ERROR_WB_SAVE_FAIL` |

## API key names

A list of 41 key names with their numbers, as text, at `0x7e38eb78`: `API_NO_KEY 0`, `API_POWER_KEY 1`, `API_1ST_RELEASE 2`, `API_2ND_RELEASE 3`, `API_UP_KEY 4`, `API_DOWN_KEY 5`, `API_LEFT_KEY 6`, `API_RIGHT_KEY 7`, `API_OK_KEY 8`, `API_MENU_KEY 9`, `API_PLAY_KEY 10`, `API_MOVIE_KEY 11`, `API_INFO_KEY 12`, `API_EVFSW_KEY 13`, `API_DEL_KEY 14`, `API_CUSTOM_KEY 15`, `API_CUSTOM2_KEY 16`, `API_CUSTOM3_KEY 17`, `API_CUSTOM4_KEY 18`, `API_CUSTOM5_KEY 19`, `API_CUSTOM6_KEY 20`, `API_CUSTOM7_KEY 21`, `API_CUSTOM8_KEY 22`, `API_CUSTOM9_KEY 23`, `API_CUSTOM10_KEY 24`, `API_EXPAND_KEY 25`, `API_LLPSW 26`, `API_INTERNAL_EVFSW_KEY 27`, `API_GRIP_CUSTOM1_KEY 28`, `API_GRIP_CUSTOM2_KEY 29`, `API_LENS_KEY 30`, `API_POWER_SLIDE_SW 31`, `API_ZOOMUP_KEY 32`, `API_ZOOMDOWN_KEY 33`, `API_HELP_KEY 34`, `API_LED_KEY 35`, `API_LENS_MF_SW 36`, `API_LENS_ZOOMUP_KEY 37`, `API_LENS_ZOOMDOWN_KEY 38`, `API_WIFI_1ST_RELEASE 39`, `API_WIFI_2ND_RELEASE 40`.
