package em10.core

import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFailsWith
import kotlin.test.assertTrue

class UpdateServerTest {
    private val reply = """<?xml version="1.0" encoding="UTF-8" ?><firmware_result><revision>0001</revision>
        <license_agreement>terms &amp; conditions</license_agreement><firmwares><firmware_info><maker_code>OLY</maker_code>
        <model_name>E-M10</model_name><model_id>1130</model_id><hardware_kind>E</hardware_kind><version>1400</version>
        <file_name>OLY_E_113_1400_0000_0000.BIN</file_name><file_size>70254592</file_size>
        <url>https://example.invalid/fw.BIN?Expires=1&amp;Signature=a~b&amp;Key-Pair-Id=K</url><up_date>2018/12/18</up_date>
        <detail_url>https://example.invalid/index04a.html</detail_url></firmware_info></firmwares></firmware_result>"""

    @Test
    fun parsesFirmwareInfo() {
        val fw = UpdateServer.parseReply(reply)
        assertEquals("E-M10", fw.modelName)
        assertEquals("1130", fw.modelId)
        assertEquals("1.4", fw.displayVersion)
        assertEquals(70254592, fw.fileSize)
        assertEquals("OLY_E_113_1400_0000_0000.BIN", fw.fileName)
        assertEquals("https://example.invalid/fw.BIN?Expires=1&Signature=a~b&Key-Pair-Id=K", fw.url)
        assertEquals("2018/12/18", fw.releaseDate)
    }

    @Test
    fun replyWithoutFirmwareIsAnError() {
        assertFailsWith<UpdateServerException> { UpdateServer.parseReply("<firmware_result><firmwares/></firmware_result>") }
    }

    @Test
    fun requestCarriesModelCodeAndNoRealIdentifiers() {
        val body = UpdateServer.requestBody("E113", "20261112120000")
        assertTrue("<hard_code>OLYE113000000000</hard_code>" in body)
        assertTrue("<serial_no>000000000</serial_no>" in body)
        assertTrue("<mac_address>00-00-00-00-00-00</mac_address>" in body)
        assertFailsWith<IllegalArgumentException> { UpdateServer.requestBody("x", "0") }
    }

    @Test
    fun latestPostsToTheServerThroughTheTransport() {
        var seenUrl = ""
        var seenHeaders = emptyMap<String, String>()
        val http = object : HttpTransport {
            override fun post(url: String, body: String, headers: Map<String, String>): String {
                seenUrl = url; seenHeaders = headers
                return reply
            }
            override fun download(url: String, progress: (Long, Long) -> Unit) = ByteArray(0)
        }
        assertEquals("1400", UpdateServer(http).latest("E113").version)
        assertEquals(UpdateServer.DEFAULT_URL, seenUrl)
        assertEquals("Olympus", seenHeaders["User-Agent"])
    }

    @Test
    fun displayVersionShowsRevisionOnlyWhenNonZero() {
        assertEquals("1.1", UpdateServer.parseReply(reply.replace("<version>1400</version>", "<version>1100</version>")).displayVersion)
        assertEquals("2.1.30", UpdateServer.parseReply(reply.replace("<version>1400</version>", "<version>2130</version>")).displayVersion)
        assertEquals("abc", UpdateServer.parseReply(reply.replace("<version>1400</version>", "<version>abc</version>")).displayVersion)
    }
}
