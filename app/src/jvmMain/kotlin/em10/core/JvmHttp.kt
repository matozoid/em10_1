package em10.core

import java.io.ByteArrayOutputStream
import java.net.URI
import java.net.http.HttpClient
import java.net.http.HttpRequest
import java.net.http.HttpResponse
import java.time.Duration

/** [HttpTransport] on java.net.http. */
class JvmHttp : HttpTransport {
    private val client = HttpClient.newBuilder().connectTimeout(Duration.ofSeconds(20))
        .followRedirects(HttpClient.Redirect.NORMAL).build()

    override fun post(url: String, body: String, headers: Map<String, String>): String {
        val b = HttpRequest.newBuilder(URI.create(url)).timeout(Duration.ofSeconds(60)).POST(HttpRequest.BodyPublishers.ofString(body))
        headers.forEach { (k, v) -> b.header(k, v) }
        val r = client.send(b.build(), HttpResponse.BodyHandlers.ofString())
        if (r.statusCode() != 200) throw UpdateServerException("the server answered HTTP ${r.statusCode()}")
        return r.body()
    }

    override fun download(url: String, progress: (Long, Long) -> Unit): ByteArray {
        val r = client.send(HttpRequest.newBuilder(URI.create(url)).GET().build(), HttpResponse.BodyHandlers.ofInputStream())
        if (r.statusCode() != 200) throw UpdateServerException("download failed with HTTP ${r.statusCode()}")
        val total = r.headers().firstValueAsLong("Content-Length").orElse(-1)
        val out = ByteArrayOutputStream(if (total > 0) total.toInt() else 1 shl 20)
        val buf = ByteArray(1 shl 16)
        var got = 0L
        r.body().use { input ->
            while (true) {
                val n = input.read(buf)
                if (n < 0) break
                out.write(buf, 0, n)
                got += n
                progress(got, total)
            }
        }
        return out.toByteArray()
    }
}
