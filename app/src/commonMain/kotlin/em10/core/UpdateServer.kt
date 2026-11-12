package em10.core

/** The transport the core needs. Each platform supplies one (the JVM uses java.net.http). */
interface HttpTransport {
    fun post(url: String, body: String, headers: Map<String, String>): String

    /** Download [url] and return its bytes; [progress] is called with (received, total or -1). */
    fun download(url: String, progress: (Long, Long) -> Unit = { _, _ -> }): ByteArray
}

/** One firmware offered by the vendor's update server. */
data class FirmwareInfo(
    val modelName: String,
    val modelId: String,
    /** Version as the server sends it, e.g. "1400". */
    val version: String,
    val fileName: String,
    val fileSize: Long,
    val url: String,
    val releaseDate: String,
    val detailUrl: String,
) {
    /** "1400" -> "1.4" (major, minor, then a two-digit revision that is shown only when it is not 00). */
    val displayVersion: String
        get() = if (version.length == 4 && version.all { it.isDigit() }) {
            "${version[0]}.${version[1]}" + if (version.substring(2) != "00") ".${version.substring(2)}" else ""
        } else version
}

class UpdateServerException(message: String) : Exception(message)

/**
 * Client for the OM Digital Solutions firmware server (docs/firmware/update-server.md).
 * The request carries a model code and placeholder identifiers only; no real serial number is sent.
 */
class UpdateServer(private val http: HttpTransport, private val url: String = DEFAULT_URL) {

    /** Ask for the latest firmware of [modelCode], e.g. "E113" for the E-M10 Mark I. */
    fun latest(modelCode: String, timestamp: String = "20260101000000"): FirmwareInfo {
        val reply = http.post(
            url, requestBody(modelCode, timestamp),
            mapOf("User-Agent" to "Olympus", "Content-Type" to "text/xml; Charset=UTF-8"),
        )
        return parseReply(reply)
    }

    companion object {
        const val DEFAULT_URL = "https://fw01.om-digitalsolutions.net/ww_inform/fcache.do"
        const val E_M10_MARK_I = "E113"

        fun requestBody(modelCode: String, timestamp: String): String {
            require(Regex("[A-Z][0-9]{3}").matches(modelCode)) { "model code must look like E113" }
            return """<?xml version="1.0"?>
<firmware_demand>
<revision>0001</revision>
<mac_address>00-00-00-00-00-00</mac_address>
<time>$timestamp</time>
<language>ENU</language>
<application>FWUT</application>
<type>0000</type>
<version>00005000</version>
<os>WIN</os>
<country_code>0001</country_code>
<hardwares>
<firmup_mode>0</firmup_mode>
<hardware_info>
<hard_code>OLY${modelCode}000000000</hard_code>
<firmware_version>00001000</firmware_version>
<serial_no>000000000</serial_no>
<default_languages><code>ENU</code></default_languages>
</hardware_info>
</hardwares>
</firmware_demand>
"""
        }

        fun parseReply(xml: String): FirmwareInfo {
            val info = Regex("<firmware_info>(.*?)</firmware_info>", RegexOption.DOT_MATCHES_ALL).find(xml)?.groupValues?.get(1)
                ?: throw UpdateServerException("the server reply contains no firmware (unknown model code, or the service changed)")
            fun field(name: String): String =
                Regex("<$name>(.*?)</$name>", RegexOption.DOT_MATCHES_ALL).find(info)?.groupValues?.get(1)?.let(::unescape)?.trim() ?: ""
            val url = field("url")
            val size = field("file_size").toLongOrNull()
            if (url.isEmpty() || size == null) throw UpdateServerException("the server reply has no download URL or file size")
            return FirmwareInfo(
                modelName = field("model_name"), modelId = field("model_id"), version = field("version"),
                fileName = field("file_name"), fileSize = size, url = url,
                releaseDate = field("up_date"), detailUrl = field("detail_url"),
            )
        }

        private fun unescape(s: String): String =
            s.replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", "\"").replace("&apos;", "'").replace("&amp;", "&")
    }
}
