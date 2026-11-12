package em10.core

/**
 * Olympus / OM firmware container (clean-room, same format as tools/omfw.py; see
 * docs/firmware/container-format.md).
 *
 * A file is a sequence of blocks. Each block is a 32-byte header, `dataLength` bytes of scrambled
 * data and a 32-byte footer. The footer repeats the first 28 header bytes and ends with a checksum V
 * such that  V + sum32(plain data) + 2 * sum32(header[0..28)) == 0  (mod 2^32, little-endian words).
 */
class FirmwareBlock(
    val index: Int,
    /** Offset of the block header in the file. */
    val offset: Int,
    val header: ByteArray,
    val loadAddress: Long,
    val dataLength: Int,
    val version: Long,
    val kind: Long,
    /** True when the footer repeats the header and its checksum matches the data. */
    val footerOk: Boolean,
) {
    /** Model id as printed in the file name, e.g. "1130" for the E-M10 Mark I. */
    val modelId: String get() = hex(header[2]) + hex(header[3])
}

class ContainerException(message: String) : Exception(message)

object FirmwareContainer {
    private const val HEADER = 32
    private const val FOOTER = 32
    private val PERMUTATION = intArrayOf(1, 3, 0, 2, 6, 4, 7, 5, 11, 10, 9, 8, 13, 14, 12, 15)

    /** Parse and verify every block. Throws [ContainerException] when the structure is not a container. */
    fun parse(file: ByteArray): List<FirmwareBlock> {
        val blocks = ArrayList<FirmwareBlock>()
        var offset = 0
        while (offset < file.size) {
            if (file.size - offset < HEADER + FOOTER) throw ContainerException("truncated block header at offset $offset")
            if (file[offset] != 'O'.code.toByte() || file[offset + 1] != 'E'.code.toByte()) {
                throw ContainerException("no 'OE' block signature at offset $offset")
            }
            val dataLength = u32(file, offset + 12)
            if (dataLength < 0 || dataLength % 16 != 0L || offset + HEADER + dataLength + FOOTER > file.size) {
                throw ContainerException("block ${blocks.size} at offset $offset has an impossible length $dataLength")
            }
            val length = dataLength.toInt()
            val dataStart = offset + HEADER
            val footerStart = dataStart + length
            var echo = true
            for (i in 0 until 28) if (file[footerStart + i] != file[offset + i]) echo = false
            val expected = (-(sumPlain(file, dataStart, length) + 2 * sumWords(file, offset, 28))) and 0xffffffffL
            blocks += FirmwareBlock(
                index = blocks.size,
                offset = offset,
                header = file.copyOfRange(offset, offset + HEADER),
                loadAddress = u32(file, offset + 8),
                dataLength = length,
                version = u32(file, offset + 16),
                kind = u32(file, offset + 20),
                footerOk = echo && u32(file, footerStart + 28) == expected,
            )
            offset = footerStart + FOOTER
        }
        if (blocks.isEmpty()) throw ContainerException("empty file")
        return blocks
    }

    /** Descramble one block's data: plain[j] = scrambled[P[j]] xor 0xFF within each 16-byte chunk. */
    fun decode(file: ByteArray, block: FirmwareBlock): ByteArray {
        val out = ByteArray(block.dataLength)
        val start = block.offset + HEADER
        var i = 0
        while (i < block.dataLength) {
            for (j in 0 until 16) out[i + j] = (file[start + i + PERMUTATION[j]].toInt() xor 0xff).toByte()
            i += 16
        }
        return out
    }

    /** Sum of the little-endian 32-bit words of the *descrambled* data, without allocating it. */
    private fun sumPlain(file: ByteArray, start: Int, length: Int): Long {
        var sum = 0L
        var i = 0
        while (i < length) {
            var w = 0
            while (w < 16) {
                val b0 = (file[start + i + PERMUTATION[w]].toInt() xor 0xff) and 0xff
                val b1 = (file[start + i + PERMUTATION[w + 1]].toInt() xor 0xff) and 0xff
                val b2 = (file[start + i + PERMUTATION[w + 2]].toInt() xor 0xff) and 0xff
                val b3 = (file[start + i + PERMUTATION[w + 3]].toInt() xor 0xff) and 0xff
                sum += b0.toLong() or (b1.toLong() shl 8) or (b2.toLong() shl 16) or (b3.toLong() shl 24)
                w += 4
            }
            i += 16
        }
        return sum and 0xffffffffL
    }

    private fun sumWords(b: ByteArray, start: Int, length: Int): Long {
        var sum = 0L
        var i = 0
        while (i < length) {
            sum += u32(b, start + i)
            i += 4
        }
        return sum and 0xffffffffL
    }

    internal fun u32(b: ByteArray, o: Int): Long =
        (b[o].toLong() and 0xff) or ((b[o + 1].toLong() and 0xff) shl 8) or
            ((b[o + 2].toLong() and 0xff) shl 16) or ((b[o + 3].toLong() and 0xff) shl 24)
}

internal fun hex(b: Byte): String {
    val v = b.toInt() and 0xff
    return "0123456789abcdef"[v shr 4].toString() + "0123456789abcdef"[v and 15]
}

fun ByteArray.toHex(): String = buildString(size * 2) { for (b in this@toHex) append(hex(b)) }
