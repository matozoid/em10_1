# Vendor firmware update server (static RE of OM Workspace 2.5.0.11)

## Endpoints (plain strings in `plugins/FNP_OlySupport.ofnp`)
- prod: `https://fw01.om-digitalsolutions.net/ww_inform/flist.do`
- staging: `https://fw01-stg.om-digitalsolutions.net/ww_inform/flist.do`
- VERIFIED 2026-11-01: prod resolves (52.199.84.231, 3.115.232.26, AWS), GET -> `405`, `Allow: OPTIONS, POST`, nginx.
- Old `dl01.olympus-imaging.com` is dead.

## Community confirmation (marcrphoto.wordpress.com, 2026-05-11)
- A community bash script (credited to Mike S, mu-43 thread) POSTs XML to **`https://fw01.om-digitalsolutions.net/ww_inform/fcache.do`**
  (NOT `flist.do`; the 2014 blog also names `fw01.olympus-imaging.com/ww_inform/fcache.do` and `.../firmware2.do`).
- Per model it sends hardware code + placeholder serial, User-Agent `Olympus`; reply XML has firmware URL + filename.
  Model code for original E-M10 = **`E113`** ("EM10_MK1"), matching old BIN name `OLY_E_113_...`. => `hard_code` = `E113`.
- Needs curl, wget, xmllint. Author says direct links in older spreadsheets mostly broke; official route = OM Workspace/OI.Share.
- Author keeps a small firmware archive (contact via his blog). Third-party offline updater site: ofu.infinityfreeapp.com (untrusted).
- Exact XML body of the script NOT yet seen (page text flattened, copyrighted). Mu-43 thread has the original.

## Request XML (from `OlyWebXMLMgr.dll` strings; element nesting/exact format NOT yet verified)
Tags: `revision, mac_address, time, application, version, language, country_code, type, request_kind, install,
package_id, hardwares, firmup_mode, hardware_info, hard_code, firmware_version, serial_no, default_languages,
additional_language, code, constellation, os_version, region, macaddr, setting, other`.
Defaults seen: type `0001`, mac `00-00-00-00-00-00`, firmware_version `000000000`.
Library uses MSXML 6 (`Msxml2.DOMDocument.6.0`). Class names: `CameraFirmup`.

## Response XML tags
`firmware_result, firmwares, firmware_info, firmware_demand, firmware_version, serial_no, errors,
contents, content_info, license_agreement, preview_data`.
The BIN URL is expected inside `firmware_info`/`content_info` (unverified).

## Builder RE (Ghidra, `research/decomp/OlyWebXMLMgr.c`; DOM via MSXML, root created by FUN_10009100(name))
- `FUN_10009100(root,"firmware_demand")` creates the root; `FUN_10009400` appends the common header:
  `revision, mac_address, time, language, application, type, version, <unnamed DAT_1000b1f0 tag>, country_code`
  (call order; nesting not resolved, `type`/`version` likely under `application`).
- Firmware request body (FUN_10007xxx @ ~line 6220): `firmup_mode` (text from caller), then per hardware:
  `hard_code`, `firmware_version`, `serial_no` (default `000000000`), then a list of `code` elements (language codes).
- Content request (line ~5848) uses root `contents_demand` + `request_kind` + repeated `package_id`.
- Skeleton guess (UNVERIFIED):
  firmware_demand > [header..., firmup_mode, hardwares > hardware_info > {hard_code, firmware_version, serial_no}, default_languages > code*]
- Server schema errors from a trial POST would reveal the missing/wrong tags.

## TODO
- Recover exact XML skeleton (decompile OlyWebXMLMgr builder functions) before any live request.
- `hard_code` for E-M10 Mark I unknown (old blog: update ID 1130; maybe unrelated).


## VERIFIED 2026-11-02: working query (tools/fetch-firmware.sh)
- POST `fcache.do`, UA `Olympus`, `Content-Type: text/xml`, body `<firmware_demand>` with header
  `revision=0001, mac_address, time, language=ENU, application=FWUT, type=0000, version=00005000, os=WIN, country_code=0001`
  then `<hardwares><firmup_mode>0</firmup_mode><hardware_info><hard_code>OLY{CODE}000000000</hard_code>
  <firmware_version>00001000</firmware_version><serial_no>…</serial_no><default_languages><code>ENU</code>…`.
  Serial ignored by server (dummy accepted). Source of format: M. Selig bash script (mu-43, Feb 2026).
- Reply `<firmware_result>`: `license_agreement`, `firmwares/firmware_info{maker_code, model_name, model_id(1130),
  hardware_kind, version(1400), file_name, file_size, url(CloudFront signed, Expires ~1y), up_date, detail_url}`.
- E-M10 Mark I: `OLY_E_113_1400_0000_0000.BIN`, 70,254,592 bytes, 2018/12/18,
  sha256 `84d81b2dbd80ea2e94ec70e35acbba0e3193ccee8b51db14976fd0d9c4e3590c`. Stored in `firmware/stock/` (gitignored).
- Header: `4f 45 11 30 ...` = "OE" + model id 1130. Body looks scrambled/compressed (not yet analyzed).
- **SD-card update path (from community script):** copy as `E1139999.BIN` (code+`9999.BIN`) into `DCOLYMP/` on SD card,
  power on holding OK. No USB/PTP needed. (UNVERIFIED for E-M10 Mark I; check.)
- EULA in reply forbids copying beyond backup, redistribution, modification, reverse engineering of the Software.
  => keep BINs out of the repo (gitignored), do not redistribute; hobbyist analysis is at user's own risk/jurisdiction.

## Version history (public release notes, saved in research/sources/em10-fwnotes-0N.html)
| Ver | Date | Change |
|---|---|---|
| 1.0 | 2014-02 | launch |
| 1.1 | 2014-05-21 | video IS stabilised; Anti-Shock 0 s added |
| 1.2 | 2014-11-13 | AF precision with M.Zuiko 40-150 f/2.8 PRO |
| 1.3 | 2016-01-28 | support for in-lens IS (not 5-axis Sync IS); Win10 |
| 1.4 | 2018-12-18 | AF fix with Panasonic H-ES200 / H-ES50200 |

## Older BINs: NOT obtainable from vendor (checked 2026-11-02)
- Server returns only the latest (asked with firmware_version 1.0 -> got 1.4).
- Unsigned `dl01.om-digitalsolutions.net/OMDS/FIRMWARES/0001/1130/OLY_E_113_{1000..1400}_0000_0000.BIN` -> 403 for all (incl. 1.4);
  CDN requires a CloudFront signed URL. Not bypassed.
- Other sources: Marc R's small archive, mu-43/DPReview threads, personal archives, the community fw exe (not unpacked). 1.1 BIN name known: OLY_E_113_1100_0000_0000.BIN.
