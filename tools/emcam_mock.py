#!/usr/bin/env python3
"""Fake E-M10 Mark I Wi-Fi server for developing and testing clients without the camera.

Implements the subset of the CGI interface that tools/emcam.py uses, following
docs/firmware/wifi-cgi.md: per-mode command availability (HTTP 520 + errorcode 1001 outside the right
mode), a small fake card, properties with allowed values, and a live-view stream of tiny JPEG frames
split over several datagrams as in docs/usb-protocol/liveview-udp.md.

usage: emcam_mock.py [PORT=8010]      then:  emcam.py --host 127.0.0.1:8010 info
"""
import socket, struct, sys, threading, time, urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

JPEG = b"\xff\xd8" + b"\xff\xdb" + bytes(range(64)) * 40 + b"\xff\xd9"      # not decodable, but framed like one
CARD = {"/DCIM": [("100OLYMP", 0, 16)],
        "/DCIM/100OLYMP": [("P1010001.JPG", len(JPEG), 32), ("P1010002.ORF", 5000, 32), ("P1010003.MOV", 9000, 32)]}
FILES = {"/DCIM/100OLYMP/P1010001.JPG": JPEG, "/DCIM/100OLYMP/P1010002.ORF": b"R" * 5000,
         "/DCIM/100OLYMP/P1010003.MOV": b"M" * 9000}
PROPS = {"takemode": ["getset", "P", "iAuto P A S M ART"], "isospeedvalue": ["getset", "Auto", "Auto Low 200 400 800"],
         "noisereduction": ["get", "off", "off on auto"]}
STATE = {"mode": "play", "lv": None, "shots": []}
COMMANDS = ["get_connectmode", "switch_cammode", "get_caminfo", "exec_pwoff", "get_resizeimg", "get_imglist",
            "get_thumbnail", "exec_takemisc", "get_camprop", "set_camprop", "exec_shutter"]
FATDATE, FATTIME = (2026 - 1980) << 9 | 11 << 5 | 12, 10 << 11 | 30 << 5 | 5


def desc(name):
    a, v, e = PROPS[name]
    return "<desc><propname>%s</propname><attribute>%s</attribute><value>%s</value><enum>%s</enum></desc>" % (name, a, v, e)


def stream(addr):
    s, seq, ts = socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 0, 0
    while STATE["lv"] == addr:
        chunks = [JPEG[i:i + 900] for i in range(0, len(JPEG), 900)]
        for i, c in enumerate(chunks):
            first, last = i == 0, i == len(chunks) - 1
            hdr = struct.pack(">BBHII", 0x10 if first else 0, 0x80 if last else 0, seq, ts, 0)
            if first:                              # one TLV: type 1, 1 word = JPEG size
                hdr += struct.pack(">HH", 0, 2) + struct.pack(">HHI", 1, 1, len(JPEG))
            s.sendto(hdr + c, addr)
            seq = (seq + 1) & 0xffff
        ts += 3000
        time.sleep(0.03)


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def reply(self, body=b"", code=200, ctype="text/xml"):
        if isinstance(body, str):
            body = body.encode()
        self.send_response(code); self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)

    def error(self, code):
        self.reply("<?xml version=\"1.0\"?><response><errorcode>%d</errorcode></response>" % code, 520)

    def do_POST(self):
        self.body = self.rfile.read(int(self.headers.get("Content-Length", 0))).decode()
        self.handle_cgi()

    def do_GET(self):
        self.body = ""
        self.handle_cgi()

    def handle_cgi(self):
        u = urllib.parse.urlparse(self.path)
        q = {k: v[0] for k, v in urllib.parse.parse_qs(u.query).items()}
        name, mode = u.path.lstrip("/").replace(".cgi", ""), STATE["mode"]
        if u.path in FILES:
            return self.reply(FILES[u.path], ctype="image/jpeg")
        if name == "get_connectmode":
            return self.reply("<connectmode>private</connectmode>")
        if name == "get_caminfo":
            return self.reply("<caminfo><model>E-M10</model></caminfo>")
        if name == "get_commandlist":
            return self.reply("<oishare><version>2.20</version>%s</oishare>" % "".join('<cgi name="%s"/>' % c for c in COMMANDS))
        if name == "switch_cammode":
            if q.get("mode") not in ("rec", "play", "shutter"):
                return self.error(1004)
            STATE["mode"] = q["mode"]
            return self.reply(ctype="www/unknown")
        if name == "exec_pwoff":
            return self.reply()
        if name in ("get_unusedcapacity", "get_dcffilenum"):
            if mode != "play":
                return self.error(1001)
            return self.reply("<unused>1234567</unused>" if name == "get_unusedcapacity" else "<dcffile>3</dcffile>")
        if name == "get_imglist":
            d = q.get("DIR")
            if d is None:
                return self.error(1002)
            if d not in CARD:
                return self.error(1005)
            return self.reply("VER_100\r\n" + "".join("%s,%s,%d,%d,%d,%d\r\n" % (d, n, s, a, FATDATE, FATTIME) for n, s, a in CARD[d]),
                              ctype="text/plain")
        if name in ("get_thumbnail", "get_resizeimg"):
            if q.get("DIR") not in FILES:
                return self.error(1005)
            return self.reply(JPEG, ctype="image/jpeg")
        if name in ("get_camprop", "set_camprop", "exec_takemisc"):
            if mode != "rec":
                return self.error(1001)
            if name == "exec_takemisc":
                if q.get("com") == "startliveview" and "port" in q:
                    STATE["lv"] = (self.client_address[0], int(q["port"]))
                    threading.Thread(target=stream, args=(STATE["lv"],), daemon=True).start()
                elif q.get("com") == "stopliveview":
                    STATE["lv"] = None
                else:
                    return self.error(1004)
                return self.reply()
            p = q.get("propname")
            if name == "get_camprop":
                if p == "desclist" and q.get("com") == "desc":
                    return self.reply("<desclist>%s</desclist>" % "".join(desc(n) for n in PROPS))
                if p not in PROPS or q.get("com") not in ("get", "desc"):
                    return self.error(1004)
                return self.reply(desc(p) if q["com"] == "desc" else "<get><value>%s</value></get>" % PROPS[p][1])
            import re
            m = re.search(r"<value>(.*?)</value>", self.body)
            if p not in PROPS or PROPS[p][0] != "getset" or not m or m.group(1) not in PROPS[p][2].split():
                return self.error(1004)
            PROPS[p][1] = m.group(1)
            return self.reply()
        if name == "exec_shutter":
            if mode != "shutter":
                return self.error(1001)
            STATE["shots"].append(q.get("com"))
            return self.reply()
        self.error(1001)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8010
    print("fake camera on http://127.0.0.1:%d/" % port)
    ThreadingHTTPServer(("127.0.0.1", port), H).serve_forever()
