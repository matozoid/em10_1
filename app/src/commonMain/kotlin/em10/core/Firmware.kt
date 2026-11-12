package em10.core

expect fun sha256(data: ByteArray): ByteArray

/** Result of checking a firmware file before it is offered to the camera. */
class FirmwareCheck(
    val blocks: List<FirmwareBlock>,
    val sha256: String,
    val problems: List<String>,
) {
    val ok: Boolean get() = problems.isEmpty()
}

object Firmware {
    /** Model id inside E-M10 Mark I firmware files. */
    const val E_M10_MARK_I_MODEL_ID = "1130"

    /** sha256 of the official body firmware 1.4 (OLY_E_113_1400_0000_0000.BIN). */
    const val E_M10_MARK_I_V14_SHA256 = "84d81b2dbd80ea2e94ec70e35acbba0e3193ccee8b51db14976fd0d9c4e3590c"

    /**
     * Verify a downloaded file: size against the server's figure (when given), container structure,
     * every block checksum, and that every block belongs to [modelId].
     */
    fun check(file: ByteArray, modelId: String = E_M10_MARK_I_MODEL_ID, expectedSize: Long? = null): FirmwareCheck {
        val problems = ArrayList<String>()
        if (expectedSize != null && file.size.toLong() != expectedSize) {
            problems += "file is ${file.size} bytes, the server announced $expectedSize"
        }
        val blocks = try {
            FirmwareContainer.parse(file)
        } catch (e: ContainerException) {
            problems += "not a firmware container: ${e.message}"
            emptyList()
        }
        for (b in blocks) {
            if (!b.footerOk) problems += "block ${b.index}: checksum does not match (file damaged)"
            if (b.modelId != modelId) problems += "block ${b.index}: is for model ${b.modelId}, expected $modelId"
        }
        return FirmwareCheck(blocks, sha256(file).toHex(), problems)
    }

    /**
     * Path of the update file on the memory card, relative to the card root, for a body firmware of
     * [modelId] ("1130" -> "DCOLYMP/E1139999.BIN"). The camera looks for E<3 digits>????.BIN there.
     */
    fun cardPath(modelId: String = E_M10_MARK_I_MODEL_ID): String {
        require(modelId.length == 4 && modelId.all { it.isDigit() }) { "model id must be four digits" }
        return "DCOLYMP/E${modelId.substring(0, 3)}9999.BIN"
    }
}
