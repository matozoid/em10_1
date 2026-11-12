package em10.cli

import em10.core.Firmware
import em10.core.FirmwareCheck
import em10.core.JvmHttp
import em10.core.UpdateServer
import java.io.File
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import kotlin.system.exitProcess

private const val USAGE = """em10 - firmware helper for the Olympus OM-D E-M10 Mark I

  em10 check                    ask the vendor server for the latest firmware
  em10 download [DIR]           download the latest firmware into DIR (default: .) and verify it
  em10 verify FILE              verify a firmware file (structure, checksums, model)
  em10 card FILE CARD_ROOT      verify FILE and copy it to CARD_ROOT/DCOLYMP/E1139999.BIN

Nothing here talks to the camera. `card` only writes a file to a memory card; the camera installs
it itself when it is started with that card and the update is confirmed on the camera.
"""

fun main(args: Array<String>) {
    try {
        when (args.firstOrNull()) {
            "check" -> check()
            "download" -> download(File(args.getOrElse(1) { "." }))
            "verify" -> if (args.size == 2) verify(File(args[1])) else usage()
            "card" -> if (args.size == 3) card(File(args[1]), File(args[2])) else usage()
            else -> usage()
        }
    } catch (e: Exception) {
        System.err.println("error: ${e.message}")
        exitProcess(1)
    }
}

private fun usage(): Nothing {
    print(USAGE)
    exitProcess(2)
}

private fun server() = UpdateServer(JvmHttp())

private fun now() = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMddHHmmss"))

private fun check() {
    val fw = server().latest(UpdateServer.E_M10_MARK_I, now())
    println("model        : ${fw.modelName} (id ${fw.modelId})")
    println("latest       : ${fw.displayVersion}, released ${fw.releaseDate}")
    println("file         : ${fw.fileName}, ${fw.fileSize} bytes")
    println("release notes: ${fw.detailUrl}")
}

private fun download(dir: File) {
    val http = JvmHttp()
    val fw = UpdateServer(http).latest(UpdateServer.E_M10_MARK_I, now())
    println("downloading ${fw.fileName} (version ${fw.displayVersion}, ${fw.fileSize} bytes)")
    var lastShown = -1L
    val data = http.download(fw.url) { got, total ->
        val pct = if (total > 0) got * 100 / total else -1
        if (pct != lastShown && pct % 10 == 0L) {
            lastShown = pct
            println("  $pct %")
        }
    }
    val result = Firmware.check(data, expectedSize = fw.fileSize)
    report(result)
    if (!result.ok) throw IllegalStateException("the download failed verification and was not saved")
    dir.mkdirs()
    val out = File(dir, fw.fileName)
    out.writeBytes(data)
    println("saved ${out.path}")
}

private fun verify(file: File): FirmwareCheck {
    if (!file.isFile) throw IllegalArgumentException("${file.path} is not a file")
    val result = Firmware.check(file.readBytes())
    report(result)
    if (!result.ok) exitProcess(1)
    return result
}

private fun report(r: FirmwareCheck) {
    for (b in r.blocks) {
        println(
            "block ${b.index}: model ${b.modelId}, load 0x${b.loadAddress.toString(16)}, ${b.dataLength} bytes, " +
                "version 0x${b.version.toString(16)}, checksum ${if (b.footerOk) "ok" else "BAD"}"
        )
    }
    println("sha256: ${r.sha256}")
    if (r.sha256 == Firmware.E_M10_MARK_I_V14_SHA256) println("this is the official E-M10 Mark I firmware 1.4")
    if (r.ok) println("verification: ok") else r.problems.forEach { println("PROBLEM: $it") }
}

private fun card(file: File, cardRoot: File) {
    val result = verify(file)
    if (!cardRoot.isDirectory) throw IllegalArgumentException("${cardRoot.path} is not a directory (is the card mounted?)")
    if (result.sha256 != Firmware.E_M10_MARK_I_V14_SHA256) {
        throw IllegalStateException(
            "this file is not the official firmware 1.4, so it is not copied. " +
                "Only the unmodified vendor file is written to a card by this tool."
        )
    }
    val target = File(cardRoot, Firmware.cardPath())
    target.parentFile.mkdirs()
    file.copyTo(target, overwrite = true)
    if (!target.readBytes().contentEquals(file.readBytes())) throw IllegalStateException("the copy on the card differs from the source")
    println("copied to ${target.path} and read back identical")
    println(
        """
        |Next steps, on the camera (not done by this tool):
        |  1. Charge the battery fully.
        |  2. Unmount the card safely and insert it.
        |  3. Hold OK while switching the camera on. On this model that step is observed to be
        |     checked at power-on, but an update from the card has not been tested by this project.
        |  4. Do not switch off or open the card door while the camera is updating.
        """.trimMargin()
    )
}
