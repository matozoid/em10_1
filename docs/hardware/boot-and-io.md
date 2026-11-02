# Block-0 reset entry + on-chip I/O registers (2026-11-02)

Static RE, mn10300 objdump of `firmware/stock/dec/blk00_40300000.bin` (runtime base `0x7d991020`).

## Correction: image start is CODE, not junk

Earlier notes called the first bytes of block 0 "junk = vectors/data". That was wrong — they
disassemble cleanly as the **C-runtime / reset entry** at runtime `0x7d991020` (file offset 0). The
false impression came from reading the bytes as a pointer table; as MN103 code they are a normal
startup stub.

### Reset entry 0x7d991020 (sequence)
1. `and 0xF0FF,psw` — clear PSW interrupt-level / flag bits (boot with interrupts masked).
2. `calls 0x7d991104`, `calls 0x7d9910f9` — two early init stubs (see 0x7d9910f9 below).
3. `mov 0x98001000,a2; mov 16,d3; mov d3,(8,a2)` — write `16` to **MMIO 0x98001008**.
4. Three `call 0x7d991452` with `(d0=dst, d1=src/len)` pairs over RAM ranges — C data/bss section
   init (copy/clear of initialised-data and zero regions).
5. `call 0x7d996bc9` — further subsystem init.
6. Programs the interrupt controller (below), then continues into the main OS bring-up.

## On-chip I/O register block at abs16 `0x8000-0x80xx`

MN103/AM33 maps internal peripheral registers in the low `(abs16)` addressing window. Block 0
accesses them with `mov (0x80xx),dN` / `movhu dN,(0x80xx)`. Identified so far:

| reg | evidence | role |
|---|---|---|
| 0x8000, 0x8004, 0x8008, 0x800c, 0x8010, 0x8014, 0x8018 | boot stores `movhu d3,(0x80xx)` the low-16 of 7 values `0x7d9a1920/48/50/58/60/68/70` | interrupt-controller channel setup (7 channels programmed at boot) |
| 0x8050 | `mov (0x8050),d0` at the top of ISR dispatcher 0x7d9a1920 | **active interrupt channel / vector number** (read, then used to index the handler table) |
| 0x8070 | init stub 0x7d9910f9: `movhu (0x8070),d0; movhu d0,(0x8070); rets` | latched status/enable reg (read-writeback clears/arms it) |

So the `0x8000` window = the SoC's **on-chip interrupt controller**. The broader
`0x98000000`/`0x98001000` region (write of 16 to 0x98001008 at boot) is a separate memory-mapped
peripheral — this confirms the previously "unidentified 0x80000000/0x8ff00000" immediate-histogram
bucket is genuine MMIO, not noise.

## ISR dispatcher 0x7d9a1920
Trampoline that services an interrupt:
- reads the active channel from **0x8050**, `asl2` → word index into a dispatch table (base in d3),
- loads a per-source control struct (`(260,a0)` / `(300,a0)` / `(268,a0)` fields),
- fetches the handler pointer and `calls (a0)` it, passing the channel's parameters (`movhu (a2),d0`,
  `mov (8,a3),d1`).

The struct fields at +260/+268/+300 are per-interrupt-source callback slots (handler, arg, and a
completion/next hook) — the same table the boot code seeds via the `0x8000..0x8018` writes.

## Dead ends / limits
- Exact semantics of the 7 boot-programmed channel values (0x1920… are low-16 only; high half is
  implied by hardware) are not pinned to named IRQ sources — no datasheet for this SoC, and the body
  is never opened (no silkscreen/part confirmation). Region *roles* are inferred from access pattern,
  not from a reference manual.
- `0x98001008 = 16` write is an opaque peripheral config (clock/reset-enable shape); peripheral
  identity unknown.
- Cross-ref: `docs/firmware/memory-map.md` (absolute-address region table), `docs/firmware/rtos-tasks.md`.
