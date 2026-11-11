# ORF container + Olympus MakerNote — from `olive.dll`

Reverse-engineered from OM Workspace's `olive.dll` (the file-format/metadata engine; see
`architecture.md`). This is the reader a Workspace replacement must reproduce to open `.ORF`.
Interop RE, kept local (EULA note in `docs/mods/firmware-modding.md`). Decompiles in
`research/decomp/olive_*.txt` (gitignored).

## olive data model (foundational)

`olive.dll` is a **generic TIFF/EXIF engine**, not Olympus-specific by itself: the ORF magic
words and the MakerNote sub-IFD tag list are *registered by the caller* (`OlyImgProc2` / the host)
through the public exports `AddExtendMagicNumber(u16)` / `IsExtendMagicNumber(u16)` (a linked list
of extra accepted TIFF version words, head at `DAT_180097000`) and `SetMakerNoteIFDTags(obj)` /
`IsMakerNoteIFDTag(tag)` (a global int array, `DAT_180097010..018`, of tag IDs whose value is a
nested IFD). The ORF/MakerNote reader *classes*, however, live inside olive.

### `OlyCreateInstance(IID*, void** out)` — COM-style factory

16-byte IID (two 8-byte halves) → concrete class → alloc → set vtable → AddRef (vtbl+0x08).
Creates only the **public data model**: typed EXIF arrays `COlyArray<T>` (`unsigned char`,
`short`, `unsigned short`, `int`, `unsigned int`, `float`, `UnsignedRational`, `SignedRational`,
`RECT`), plus `COlyIFDStore`, `COlyTagCompositor`, `COlyString`, `COlyHeap`,
`COlyStackExifID`/`COlyListExifID`, `COlyImgFileUtility`, `COlyGPSProperty`, `COlyPreference`.
It does **not** build the format readers — those are selected internally by file magic.

### `OlyOpenFile(out, LPCWSTR path, int mode)` — data-source backends

Mode selects an `IOlyDataSrc` backend (abstract vtable: +0x08 init, +0x10 release, +0x20
`SetSize`, +0x40/+0x48 read, +0x50 close), **not** parse depth:

| mode | class | backing | access |
|---|---|---|---|
| 0 | `COlyDataSrcMemory` | whole file → heap buffer | read |
| 1 / 2 / 3 | `COlyDataSrcStdFile` | stdio `FILE*` | `rb` / `r+b` / `wb` |
| 4 / 5 / 6 | `COlyDataSrcWinFile` | Win32 `CreateFileW` HANDLE | read / read-write / write |
| 7 / 8 | `COlyDataSrcMemFile` | `CreateFileMapping`+`MapViewOfFile` | read-only / read-write |

Invalid mode → `0x80070057` (E_INVALIDARG); alloc/open failure → `0x80004005` (E_FAIL);
Win32 errors are wrapped as `GetLastError() | 0x80070000`.

## Image-format class hierarchy

RTTI (resolved manually via the Complete Object Locator — `tools`-side
`tools/rtti_vtables.py`, since Ghidra didn't auto-apply RTTI). Base **`COlyImgFmt`**
(vtable `0x180084528`) with siblings `COlyImgFmtBmp`, `COlyImgFmtJfif`, `COlyImgFmtJpeg`,
`COlyImgFmtExifJpeg`, `COlyImgFmtTiff`, `COlyImgFmtDelegate`, and **`COlyImgFmtOrf`**. All share
inherited slots 5-9; each overrides slot 0 (QueryInterface) and slot 3 (Open/Identify).
**`COlyImgFmtOrf` *is-a* `COlyImgFmtTiff`**: its QI delegates to the TIFF base
(`FUN_180031df0`) and it reuses the TIFF IFD walker (shared slot-4 `0x180035760`); only the
signature check and the MakerNote-generation logic are ORF-specific.

ORF vtables: primary `0x180086cc0`, secondary (adjustor-thunk) `0x180087328`.
Open method = `FUN_180030c80`.

## ORF signature check (`COlyImgFmtOrf::Open`, `FUN_180030c80`)

1. Read **8 bytes** at the base offset (data-source +0x48 `ReadAt`).
2. **Byte-order mark** = first u16: `0x4949` (`"II"`, little-endian) or `0x4d4d` (`"MM"`,
   big-endian). Anything else → `0x80004005` (not ORF). The little-endian flag is stored at
   object `+0xb` / `+0x59`.
3. Second u16 = TIFF "magic/version" word (byte-swapped first if big-endian), switched on:

   | version word | file bytes (LE) | signature | internal subtype (`+0xe`) |
   |---|---|---|---|
   | `0x4f52` | `52 4f` = `RO` | **`IIRO`** | `0x10003` |
   | `0x5352` | `52 53` = `RS` | **`IIRS`** | `0x10003` |
   | `0x4f54` | `54 4f` = `TO` | **`IITO`** | `0x10006` |
   | `0x4f4c` | `4c 4f` = `LO` | **`IILO`** | `0x10007` |

   `IIRO` (magic `0x4f52`) is the standard ORF signature (matches ExifTool's Olympus ORF magic);
   `IIRS` is the known big-magic variant. `IITO`/`IILO` are additional subtypes this engine
   accepts. Unknown word → `0x80004005`.
4. Container parse delegates to the shared TIFF base open (`FUN_180028f50`): standard TIFF header
   (BOM, magic, IFD0 offset) → IFD walk.

## MakerNote location + generation

After the container opens, olive resolves the Olympus MakerNote through the **standard
EXIF/TIFF tag chain** (`FUN_1800320c0`): it builds an ID path **`0x8769`** (ExifIFD pointer) →
**`0x927c`** (MakerNote), navigates the IFD tree (`COlyStackExifID`), reads the MakerNote tag's
value offset as a u32 (byte-swapped per the endian flag), and stores it as the **MakerNote base
offset** at object `+0xc`.

`FUN_180031ea0` is the **recursive IFD walker** reached from the MakerNote base. IFD layout =
`[u16 entryCount][entryCount × 12-byte entries][u32 nextIFDoffset]` (the constant `6` in the code
= 2-byte count + 4-byte next-ptr); every multi-byte field is byte-swapped when the `+0x59`
big-endian flag is set. It records each IFD's `{start,end}` extent in a visited-range vector
(recursion guard), then for every entry whose **TIFF type == 13 (IFD pointer)** *and* whose tag is
present in the `SetMakerNoteIFDTags` registry (`DAT_180097010..018`) it **recurses** into the
sub-IFD at the entry's value offset. That is exactly how the Equipment/CameraSettings/… nested
sub-IFDs (table below) get descended — generically, driven by the registry, not hard-coded.

The header read selects the parser generation — RTTI classes **`COlyMakerNote2`** (vtable `0x180087c48`), **`COlyMakerNote3`**
(`0x180087ca0`), **`COlyMakerNote4`** (`0x180087cf8`), with a shared **`COlyMakerNoteHeader`**
(`0x180087d60`). The generation is gated by a 16-bit value read from the first IFD (object `+0xd`)
against the threshold **`0x300`** (= MakerNote header version 3.00): `< 0x300` takes the simple
MakerNote2 path; `>= 0x300` reads the extended header and resolves the MakerNote base for the
newer (3/4) layout. These correspond to the Olympus MakerNote generations:
`"OLYMP\0"` (gen 1/2, old), `"OLYMPUS\0II/MM\x03\x00"` (gen 3, versioned, relative offsets).
The E-M10 Mark I writes the gen-3 `"OLYMPUS\0"` MakerNote (confirm against a real `.ORF` off the
card — tag chain and header bytes above are what the reader keys on).

## Olympus MakerNote sub-IFD tags (cross-checked vs ExifTool)

The `SetMakerNoteIFDTags` registry (tags whose value is a nested IFD) corresponds to the
documented Olympus gen-3 MakerNote sub-directories. From ExifTool's `Olympus` tag table
(https://exiftool.org/TagNames/Olympus.html):

| MakerNote tag | sub-IFD |
|---|---|
| `0x2010` | Equipment |
| `0x2020` | CameraSettings |
| `0x2030` | RawDevelopment |
| `0x2031` | RawDev2 |
| `0x2040` | ImageProcessing |
| `0x2050` | FocusInfo |
| `0x3000` | RawInfo |
| `0x4000` | MainInfo |

Main-IFD `0x0000` = MakerNoteVersion; each sub-IFD carries its own `0x0000` version
(EquipmentVersion, CameraSettingsVersion, …). Key fields the replacement needs early:
Equipment `0x0100` CameraType2 (string[6]), `0x0101` SerialNumber (string[32]), `0x0201`
LensType (int8u[6]); CameraSettings `0x0200` ExposureMode, `0x0301` FocusMode, `0x0400`
FlashMode, `0x0500` WhiteBalance2, `0x0603` ImageQuality2. (ExifTool does not document the
`OLYMP`/`OLYMPUS` header bytes or the `0x300` version gate — those come from the olive RE above.)

## For the replacement

Reading an E-M10 `.ORF` = a standard little-endian TIFF reader (`"II"`, magic `0x4f52` → IFD0)
plus: EXIF sub-IFD via tag `0x8769`; MakerNote via tag `0x927c`; parse the `OLYMPUS\0` header,
branch on version `>= 3.00`, then treat the registered MakerNote tags (Equipment, CameraSettings,
RawDevelopment, ImageProcessing, FocusInfo) as nested IFDs (the `SetMakerNoteIFDTags` registry).
The RAW pixel decode is **not** in olive — it lives in `OlyImgProc2.dll` (`GetRawDecorder` →
`IOlyImageDecoder`); that is deep-dive #2.
