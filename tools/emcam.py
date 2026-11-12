#!/usr/bin/env python3
"""Command-line client for the E-M10 Mark I Wi-Fi interface (stdlib only).

Connect the computer to the camera's own Wi-Fi network (E-M10-P-<serial>) first; the camera is then at
192.168.0.10 and speaks plain HTTP. Protocol reference: docs/firmware/wifi-cgi.md,
docs/usb-protocol/wifi-api.md, docs/usb-protocol/liveview-udp.md.

Read-only commands (do not change anything on the camera):
  info                         connect mode, model, free space, file count, advertised commands
  commands                     print the camera's raw command list (XML)
  ls [DIR] [-r]                list a card directory (default /DCIM); -r descends
  get PATH [-o FILE]           download one file, e.g. /DCIM/100OLYMP/P1010001.JPG
  pull DEST [DIR]              download every file under DIR (default /DCIM) that DEST does not have yet
  thumb PATH [-o FILE]         download the thumbnail of a picture or movie
  resize PATH SIZE [-o FILE]   download a resized JPEG; SIZE is 1024, 1600, 1920 or 2048
  props                        list remote-control properties with value and allowed values (rec mode)
  prop NAME                    show one property (rec mode)
  raw PATH                     GET any path, e.g. raw 'get_activate.cgi'

Commands that change camera state (mode, settings, or take pictures):
  mode rec|play|shutter [--lvqty 0320x0240|0640x0480]
                               (--lvqty applies to rec; the camera only accepts it coming from play,
                               so the client switches to play first)
  set NAME VALUE               set a property (rec mode), e.g. set isospeedvalue 400
  shoot [--focus-wait SECONDS] take one picture: switches to shutter mode, half-press, waits for
                               focus, full press, releases both stages, returns to rec mode
  shutter ACTION               one raw shutter-button step (shutter mode): half, release-half, full,
                               release-full, press, release-keep-half. A press without its release
                               leaves the button held; prefer `shoot`
  liveview [--frames N] [--out DIR] [--port P]
                               receive the live-view stream and save JPEG frames (rec mode; the
                               stream size is the --lvqty given to `mode rec`)
  poweroff                     switch the camera off

options: --host ADDRESS (default 192.168.0.10), --timeout SECONDS (default 10)

Errors: the camera answers HTTP 520 with a code: 1001 not available in the current mode, 1002 required
parameter missing, 1004 bad value, 1005 resource or card I/O error.
"""
import argparse, os, re, socket, struct, sys, time, urllib.error, urllib.parse, urllib.request

ERRORS = {"1001": "not available in the current mode (try `mode rec`, `mode play` or `mode shutter`)",
          "1002": "required parameter missing", "1004": "bad value", "1005": "resource or card I/O error"}
SHUTTER = {"half": "1stpush", "release-half": "1strelease", "full": "2ndpush", "release-full": "2ndrelease",
           "press": "1st2ndpush", "release-keep-half": "2nd1strelease"}
RESIZE = ("1024", "1600", "1920", "2048")
DIR_ATTR = 0x10


class CameraError(Exception):
    def __init__(self, message, status=None):
        super().__init__(message)
        self.status = status


class Camera:
    def __init__(self, host="192.168.0.10", timeout=10.0):
        self.base, self.timeout = "http://%s/" % host, timeout

    def request(self, path, data=None):
        """GET (or POST when data is given). Returns the body as bytes."""
        req = urllib.request.Request(self.base + path.lstrip("/"), data=data,
                                     headers={"User-Agent": "OI.Share v2", "Content-Type": "text/plain;charset=utf-8"})
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")
            m = re.search(r"<errorcode>\s*(\d+)\s*</errorcode>", body)
            code = m.group(1) if m else None
            raise CameraError("HTTP %d%s for %s" % (e.code, (" error %s: %s" % (code, ERRORS.get(code, "unknown")))
                                                    if code else "", path), e.code) from None
        except (urllib.error.URLError, socket.timeout, ConnectionError) as e:
            raise CameraError("cannot reach the camera at %s (%s). Is this computer on the camera's Wi-Fi?"
                              % (self.base, getattr(e, "reason", e))) from None

    def text(self, path, data=None):
        return self.request(path, data).decode("utf-8", "replace")

    def tag(self, path, name):
        m = re.search(r"<%s>(.*?)</%s>" % (name, name), self.text(path), re.S)
        return m.group(1).strip() if m else None

    # --- browsing ---
    def listdir(self, directory):
        """Entries of one card directory: dicts with path, name, size, is_dir, date, time."""
        out = []
        for attempt in range(7):               # right after a shot the camera is still writing and answers 520
            try:
                listing = self.text("get_imglist.cgi?DIR=" + urllib.parse.quote(directory))
                break
            except CameraError as e:
                if e.status != 520 or attempt == 6:
                    raise
                time.sleep(1.0)
        for line in listing.splitlines():
            p = line.strip().split(",")
            if len(p) < 6 or not p[0].startswith("/"):
                continue                       # skips the VER_100 header line
            try:
                size, attr, d, t = int(p[2]), int(p[3]), int(p[4]), int(p[5])
            except ValueError:
                continue
            out.append({"dir": p[0], "name": p[1], "path": p[0].rstrip("/") + "/" + p[1], "size": size,
                        "is_dir": bool(attr & DIR_ATTR), "date": fat_date(d), "time": fat_time(t)})
        return out

    def walk(self, directory):
        for e in self.listdir(directory):
            if e["is_dir"]:
                yield from self.walk(e["path"])
            else:
                yield e

    # --- mode and shutter ---
    def set_mode(self, mode, lvqty=None):
        """Switch camera mode. The live-view size is only taken on a switch from play to rec, so a rec
        request with a size goes through play first."""
        if mode == "rec" and lvqty:
            self.request("switch_cammode.cgi?mode=play")
            self.request("switch_cammode.cgi?mode=rec&lvqty=" + lvqty)
        else:
            self.request("switch_cammode.cgi?mode=" + mode)

    def shoot(self, focus_wait=2.0, save_wait=1.5):
        """Take one picture and leave the camera in rec mode with the shutter button released."""
        self.set_mode("shutter")               # exec_shutter is only accepted in shutter mode
        pressed = []
        try:
            self.request("exec_shutter.cgi?com=1stpush"); pressed.append("1strelease")
            time.sleep(focus_wait)
            self.request("exec_shutter.cgi?com=2ndpush"); pressed.append("2nd1strelease")
            time.sleep(0.5)
        finally:
            for step in reversed(pressed):     # always release what was pressed, full stage first
                try:
                    self.request("exec_shutter.cgi?com=" + step)
                except CameraError as e:
                    print("warning: %s" % e, file=sys.stderr)
            time.sleep(save_wait)
            self.set_mode("rec")               # in shutter mode the camera rejects the get_* commands

    # --- properties ---
    def prop_desc(self, name):
        """Parse a com=desc reply into a list of {name, attribute, value, enum}."""
        xml = self.text("get_camprop.cgi?com=desc&propname=" + name)
        out = []
        for d in re.findall(r"<desc>(.*?)</desc>", xml, re.S):
            f = lambda t: (re.search(r"<%s>(.*?)</%s>" % (t, t), d, re.S) or [None, ""])[1].strip()
            out.append({"name": f("propname"), "attribute": f("attribute"), "value": f("value"),
                        "enum": f("enum").split()})
        return out


def fat_date(d):
    return "%04d-%02d-%02d" % (1980 + (d >> 9), (d >> 5) & 15, d & 31)


def fat_time(t):
    return "%02d:%02d:%02d" % (t >> 11, (t >> 5) & 63, (t & 31) * 2)


def save(data, path):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    print("saved %s (%d bytes)" % (path, len(data)))


class FrameAssembler:
    """Rebuild JPEG frames from live-view datagrams (docs/usb-protocol/liveview-udp.md)."""

    def __init__(self):
        self.parts, self.seq = None, None

    def feed(self, dg):
        """Feed one datagram; returns a complete JPEG (bytes) when a frame ends, else None."""
        if len(dg) < 12:
            return None
        first, last = dg[0] & 0x10, dg[1] & 0x80
        seq = struct.unpack(">H", dg[2:4])[0]
        if first:
            if len(dg) < 16:
                return None
            ext_words = struct.unpack(">H", dg[14:16])[0]
            self.parts, payload = [], dg[16 + ext_words * 4:]
        elif self.parts is None or seq != (self.seq + 1) & 0xffff:
            self.parts = None                  # lost or out-of-order datagram: drop this frame
            return None
        else:
            payload = dg[12:]
        self.seq = seq
        self.parts.append(payload)
        if not last:
            return None
        jpeg, self.parts = b"".join(self.parts), None
        return jpeg if jpeg[:2] == b"\xff\xd8" and jpeg[-2:] == b"\xff\xd9" else None


def liveview(cam, frames, out, port, host_timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1 << 20)
    sock.bind(("", port))
    port = sock.getsockname()[1]
    sock.settimeout(host_timeout)
    os.makedirs(out, exist_ok=True)
    cam.request("exec_takemisc.cgi?com=startliveview&port=%d" % port)
    asm, n, dropped = FrameAssembler(), 0, 0
    try:
        while n < frames:
            try:
                dg = sock.recv(65536)
            except socket.timeout:
                raise CameraError("no live-view data received on UDP port %d (firewall? camera not in rec mode?)" % port)
            was_open = asm.parts is not None
            jpeg = asm.feed(dg)
            if jpeg:
                n += 1
                with open(os.path.join(out, "frame%05d.jpg" % n), "wb") as f:
                    f.write(jpeg)
            elif was_open and asm.parts is None:
                dropped += 1
    finally:
        try:
            cam.request("exec_takemisc.cgi?com=stopliveview")
        except CameraError as e:
            print("warning: could not stop live view: %s" % e, file=sys.stderr)
        sock.close()
    print("saved %d frames to %s (%d incomplete frames dropped)" % (n, out, dropped))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--host", default="192.168.0.10")
    ap.add_argument("--timeout", type=float, default=10.0)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("info"); sub.add_parser("commands"); sub.add_parser("props"); sub.add_parser("poweroff")
    p = sub.add_parser("ls"); p.add_argument("dir", nargs="?", default="/DCIM"); p.add_argument("-r", action="store_true")
    for name in ("get", "thumb"):
        p = sub.add_parser(name); p.add_argument("path"); p.add_argument("-o")
    p = sub.add_parser("resize"); p.add_argument("path"); p.add_argument("size", choices=RESIZE); p.add_argument("-o")
    p = sub.add_parser("pull"); p.add_argument("dest"); p.add_argument("dir", nargs="?", default="/DCIM")
    p = sub.add_parser("prop"); p.add_argument("name")
    p = sub.add_parser("raw"); p.add_argument("path")
    p = sub.add_parser("mode"); p.add_argument("mode", choices=("rec", "play", "shutter"))
    p.add_argument("--lvqty", choices=("0320x0240", "0640x0480"))
    p = sub.add_parser("set"); p.add_argument("name"); p.add_argument("value")
    p = sub.add_parser("shutter"); p.add_argument("action", choices=sorted(SHUTTER))
    p = sub.add_parser("shoot"); p.add_argument("--focus-wait", type=float, default=2.0)
    p = sub.add_parser("liveview"); p.add_argument("--frames", type=int, default=30)
    p.add_argument("--out", default="liveview"); p.add_argument("--port", type=int, default=0)
    a = ap.parse_args(argv)
    cam = Camera(a.host, a.timeout)
    try:
        run(cam, a)
    except CameraError as e:
        sys.exit("error: %s" % e)


def run(cam, a):
    if a.cmd == "info":
        print("connect mode :", cam.tag("get_connectmode.cgi", "connectmode"))
        print("model        :", cam.tag("get_caminfo.cgi", "model"))
        for label, path in (("free space   :", "get_unusedcapacity.cgi"), ("picture files:", "get_dcffilenum.cgi")):
            try:                               # print the reply's text content; tag names differ per CGI
                print(label, " ".join(re.sub(r"<[^>]+>", " ", cam.text(path)).split()))
            except CameraError as e:
                print(label, "(%s)" % e)
        xml = cam.text("get_commandlist.cgi")
        print("api version  :", (re.search(r"<version>(.*?)</version>", xml) or [0, "?"])[1])
        print("commands     :", " ".join(sorted(set(re.findall(r'<cgi name="([^"]+)"', xml)))))
    elif a.cmd == "commands":
        print(cam.text("get_commandlist.cgi"))
    elif a.cmd == "ls":
        for e in (cam.walk(a.dir) if a.r else cam.listdir(a.dir)):
            print("%s %s %10s  %s" % (e["date"], e["time"], "<dir>" if e["is_dir"] else e["size"], e["path"]))
    elif a.cmd == "get":
        save(cam.request(a.path), a.o or os.path.basename(a.path))
    elif a.cmd == "thumb":
        save(cam.request("get_thumbnail.cgi?DIR=" + urllib.parse.quote(a.path)),
             a.o or "thumb_" + os.path.splitext(os.path.basename(a.path))[0] + ".jpg")
    elif a.cmd == "resize":
        save(cam.request("get_resizeimg.cgi?DIR=%s&size=%s" % (urllib.parse.quote(a.path), a.size)),
             a.o or "%s_%s.jpg" % (os.path.splitext(os.path.basename(a.path))[0], a.size))
    elif a.cmd == "pull":
        got = skipped = 0
        for e in cam.walk(a.dir):
            local = os.path.join(a.dest, e["path"].lstrip("/"))
            if os.path.exists(local) and os.path.getsize(local) == e["size"]:
                skipped += 1
                continue
            save(cam.request(e["path"]), local)
            got += 1
        print("downloaded %d, already present %d" % (got, skipped))
    elif a.cmd == "props":
        for d in cam.prop_desc("desclist"):
            print("%-18s %-6s %-22s %s" % (d["name"], d["attribute"], d["value"], " ".join(d["enum"])))
    elif a.cmd == "prop":
        for d in cam.prop_desc(a.name):
            print("%s = %s  (%s)\nallowed: %s" % (d["name"], d["value"], d["attribute"], " ".join(d["enum"])))
    elif a.cmd == "raw":
        sys.stdout.buffer.write(cam.request(a.path)); print()
    elif a.cmd == "mode":
        cam.set_mode(a.mode, a.lvqty)
        print("camera mode set to %s" % a.mode)
    elif a.cmd == "set":
        body = '<?xml version="1.0"?>\r\n<set>\r\n<value>%s</value>\r\n</set>\r\n' % a.value
        cam.request("set_camprop.cgi?com=set&propname=" + a.name, body.encode())
        print("%s set to %s; now reads %s" % (a.name, a.value,
                                               cam.tag("get_camprop.cgi?com=get&propname=" + a.name, "value")))
    elif a.cmd == "shutter":
        cam.request("exec_shutter.cgi?com=" + SHUTTER[a.action])
        print("sent %s" % SHUTTER[a.action])
    elif a.cmd == "shoot":
        cam.shoot(a.focus_wait)
        print("picture taken; camera is back in rec mode")
    elif a.cmd == "liveview":
        liveview(cam, a.frames, a.out, a.port, cam.timeout)
    elif a.cmd == "poweroff":
        cam.request("exec_pwoff.cgi")
        print("power-off sent")


if __name__ == "__main__":
    main()
