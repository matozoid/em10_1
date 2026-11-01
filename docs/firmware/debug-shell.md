# Debug shell and memory/flash extraction (block 0)

The firmware contains a full interactive debug shell. It is the practical route to read the
factory flash regions that the update BIN never contains (notably the type-3 ROM pictures at
0x46560000, see `resources.md`).

## Shell command tables

Master command dispatch table at **0x7dbbecec** (and a duplicate at 0x7dbbfa80), 59 entries of
`{char* name, void* handler}` (8 B each). Names and handler runtime addresses:

```
shell=7dbbdb20 echo=7da86a8b help=7da86ac4 lens=7daae6b7 aud=7dd42ad2 cam=7db19d78
bas=7e6a1f6a pwr=7d9d45b9 bc=7dacd8db take=7dadcec6 stbd=7db7754f per=7d9dd66b
tm=7d9edcc6 res=7db67656 app=7db8b331 usb=7e7db895 prm=7d9d2152 flash=7d9cc5d9
rec=7de3e437 file=7de9a83c sc=7da88981 exp=7dec6412 dbg=7dacc9a7 ui=7da8a588
mec=7da91fa2 fcs=7dd85e5b dbgall=7da84cb9 sdet=7deb3917 movp=7dd6d6b4 osd=7e6a3bae
mdet=7de1adb1 face=7de4afcc play=7dd5981a bt=7e6b68ce obex=7e6ac515 acp=7e6aa18e
mddyna=7e716bd0 disp=7dbae826 tpc=7e7ca823 sdk=7dfc0823 efct=7dd767f3 buff=7de53c3f
api=7db8b384 c3d=7e7dda91 sync=7ddd6a5a usr=7da84f01 damage=7dacc6fb spc=7e7e3245
mcon=7db69ce6 wifi=7e706e74 qr=7e70699a olis=7de2caa0 mvr=7de5ea15 pos=7e70442c
avm=7ddcf5d8 iseq=7de2d30c img=7dde43c8 md_sve=7e716c4d digizoom=7de5dd0d
```

Shell tasks: `S_SHELL` (system) and `U_SHELL` (user, task `Tsk_USHL`, prompt `USR> `). Banner
`USF debugging shell Version 1.10 / Copyright (c) 2004-2005 OLYMPUS IMAGING CO.,LTD.`

## Memory/flash read commands (confirmed by help strings)

**`flash` subcommand** (handler `flash_7d9cc5d9` = `ram_addr_7d9cc5d9`), help text at 0x7d9f9472:
```
addr                            : Show Major Base Adress
dump [fmem_addr(HEX(80000000))] : dump 1KB
oly fmem [fmem_addr] [size(DEC)] [mode]
p read  [dram_addr(HEX)] [fmem_addr(HEX)] [size(HEX)]   (PURNAND read into DRAM)
p write [dram_addr(HEX)]
p erase [dram_addr(HEX)]
```
`addr` prints the "Major ROM Address" table: `adj_addr / mode0_addr / mode1_addr / param0_addr /
param1_addr / lensfav_addr / usr_addr / pict_addr / osd_addr / sound_addr`. **`pict_addr` is the
ROM-picture base** (type-3 dir, expected 0x46560000); running `flash addr` on the camera prints
the live value and confirms it.

**`file` subcommand** (handler `file_7de9a83c`) opens the FileSystem Debug Command set (help at
0x7df55f37). Key command:
```
memdump NAME ADR LEN   - dump memory into file (ADR:hex, LEN:dec)
memload NAME ADR [LEN] - load memory from file
rawread LBA / rawread -c CLS SCT
cat / ls / cp etc.
```
**`file memdump rompics 46560000 14680064`** (0xE00000 = 14 MB) writes the entire ROM-picture
region to a file on the mounted card. This is the cleanest extraction: output lands on the SD
card, no host-side transport needed — pull the card afterward. Carve JPEGs using the 512-slot
`{addr,size,0,0}` directory in the first 0x2000 bytes (see `resources.md` type 3).

Other mem commands seen: `mem_get1/2/4 <address>` (byte/half/word peek), `oly fmem` (flash dump
with mode), and the C3D/AVM `memdump` debug variants (GPU/coprocessor).

## Reaching the shell — transports

- **Wi-Fi (confirmed):** TCP socket shell. `FUN_7e712f65` creates a socket (`FUN_7e6ed41b(2,1)` =
  AF/stream), binds (struct at SP+0x14 holds port bytes `0x1700` big-endian = **port 23**,
  i.e. telnet), listens. Driver `FUN_7e7131b4` has subcommands init/start/`listen_sock`/config;
  `remocon_7e706e74` (the `wifi` shell command) invokes it. Gated by global flag at **0x8050**
  (`_DAT_00008050 == 1`); when clear it falls back to the Wi-Fi remocon XML proxy. The socket
  bind/accept path (`_DAT_a0a929ac` listen fd, `_DAT_a0a929b0` accept fd) is real TCP.
  Connecting a telnet client to 192.168.0.10:23 while on the camera AP is the likely route, if
  flag 0x8050 is set in the shipping build (untested; needs live check).
- **USB:** the USB interface enumerates as **PTP/MTP** (tasks `TSK_PTPCOM`/`TSK_PTPACY`,
  `PC_PTP`, `api_comm_Start_Communication_PTP/MTP`, `start_usb_firmup`). Standard PTP op table at
  0x7d9ad28c (0x1001-0x100f). A large **vendor opcode set 0x9001-0x93f3** exists (dispatch tables
  around 0x7e45c0xx / 0x7e5dd1xx). No string evidence of a USB CDC/ACM serial console or a
  generic "read memory" PTP op was found yet; `DOSMEM_READ`/`DOSFSTRM_*` are internal
  DOS-filesystem API tags, not USB operations. So there is **no confirmed shell-over-USB path**;
  mapping a vendor PTP opcode to a memory read (or to firmware-update flashing) is the open USB
  lead. `usb` is also a master shell command (handler 0x7e7db895).
- **UART:** the "USF debugging shell" and `DBG_OUT` task strongly imply a hardware serial console
  on internal test pads (standard for this Olympus platform). Not accessible without opening the
  body.

## Recommendation for extraction

Easiest with no cable at all: get shell access (Wi-Fi telnet if flag 0x8050 permits, else UART),
run `file memdump rompics 46560000 14680064` (ADR hex, LEN decimal = 0xE00000), then read the
file off the SD card. All of this is a
live camera action and must be confirmed with the user before running; only reads so far.
Open item: whether the shipping 1.4 build leaves the telnet flag (0x8050) enabled, and whether a
vendor PTP opcode gives a USB-only memory read.
