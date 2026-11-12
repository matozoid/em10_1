package em10.core

import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFailsWith
import kotlin.test.assertFalse
import kotlin.test.assertTrue

class ContainerTest {
    private val permutation = intArrayOf(1, 3, 0, 2, 6, 4, 7, 5, 11, 10, 9, 8, 13, 14, 12, 15)

    private fun le32(v: Long) = ByteArray(4) { (v shr (8 * it)).toByte() }

    private fun sum32(b: ByteArray, len: Int = b.size): Long {
        var s = 0L
        for (i in 0 until len step 4) s += FirmwareContainer.u32(b, i)
        return s and 0xffffffffL
    }

    /** Build one valid block the same way tools/omfw.py does. */
    private fun block(plain: ByteArray, load: Long, version: Long, kind: Long): ByteArray {
        val header = ByteArray(32)
        header[0] = 'O'.code.toByte(); header[1] = 'E'.code.toByte(); header[2] = 0x11; header[3] = 0x30
        le32(load).copyInto(header, 8); le32(plain.size.toLong()).copyInto(header, 12)
        le32(version).copyInto(header, 16); le32(kind).copyInto(header, 20)
        val scrambled = ByteArray(plain.size)
        for (i in plain.indices step 16) for (j in 0 until 16) {
            scrambled[i + permutation[j]] = (plain[i + j].toInt() xor 0xff).toByte()
        }
        val v = (-(sum32(plain) + 2 * sum32(header, 28))) and 0xffffffffL
        return header + scrambled + header.copyOf(28) + le32(v)
    }

    private val plainA = ByteArray(64) { (it * 7 + 3).toByte() }
    private val plainB = ByteArray(32) { (200 - it).toByte() }
    private val file = block(plainA, 0x40300000, 0x1400, 0x100) + block(plainB, 0x41500000, 0, 0x101)

    @Test
    fun parsesBlocksAndVerifiesChecksums() {
        val blocks = FirmwareContainer.parse(file)
        assertEquals(2, blocks.size)
        assertEquals(0x40300000, blocks[0].loadAddress)
        assertEquals(64, blocks[0].dataLength)
        assertEquals(0x1400, blocks[0].version)
        assertEquals(0x101, blocks[1].kind)
        assertEquals("1130", blocks[0].modelId)
        assertTrue(blocks.all { it.footerOk })
    }

    @Test
    fun decodeRestoresPlainData() {
        val blocks = FirmwareContainer.parse(file)
        assertTrue(plainA.contentEquals(FirmwareContainer.decode(file, blocks[0])))
        assertTrue(plainB.contentEquals(FirmwareContainer.decode(file, blocks[1])))
    }

    @Test
    fun detectsDamagedData() {
        val damaged = file.copyOf()
        damaged[40] = (damaged[40].toInt() xor 1).toByte()
        val blocks = FirmwareContainer.parse(damaged)
        assertFalse(blocks[0].footerOk)
        assertTrue(blocks[1].footerOk)
        assertFalse(Firmware.check(damaged).ok)
    }

    @Test
    fun rejectsFilesThatAreNotContainers() {
        assertFailsWith<ContainerException> { FirmwareContainer.parse(ByteArray(100)) }
        assertFailsWith<ContainerException> { FirmwareContainer.parse(file.copyOf(file.size - 5)) }
        assertFalse(Firmware.check("hello".encodeToByteArray()).ok)
    }

    @Test
    fun checkReportsWrongModelAndSize() {
        assertTrue(Firmware.check(file, expectedSize = file.size.toLong()).ok)
        assertFalse(Firmware.check(file, modelId = "1090").ok)
        assertFalse(Firmware.check(file, expectedSize = 1).ok)
    }

    @Test
    fun cardPathFollowsTheCameraPattern() {
        assertEquals("DCOLYMP/E1139999.BIN", Firmware.cardPath())
        assertEquals("DCOLYMP/E1099999.BIN", Firmware.cardPath("1090"))
    }

    @Test
    fun sha256MatchesKnownVector() {
        assertEquals("ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad", sha256("abc".encodeToByteArray()).toHex())
    }
}
