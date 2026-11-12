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
  probe [-o FILE]              run every read-only check once and write the raw replies to FILE
                               (default emcam-probe.txt); the file to send back after a live test

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
  livetest [--out DIR] [--yes] guided test of the state-changing commands: asks before each step
                               (rec mode, properties, live view, set a property to its current value,
                               take one picture, fetch it, back to play mode) and writes a report and
                               sample files into DIR (default emcam-livetest)

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

    def free_bytes(self):
        """Free card space in bytes, or None when the camera reports its 32-bit maximum (4 GB or more)."""
        v = int(self.tag("get_unusedcapacity.cgi", "unused"))
        return None if v >= 0xffffffff else v

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


def tlv_types(dg):
    """Extension entries of a first live-view datagram as [(type, words)]."""
    out, n = [], struct.unpack(">H", dg[14:16])[0] * 4
    i, end = 16, min(len(dg), 16 + n)
    while i + 4 <= end:
        t, words = struct.unpack(">HH", dg[i:i + 4])
        out.append((t, words))
        i += 4 + words * 4
    return out


def liveview(cam, frames, out, port, host_timeout, stats=None):
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
            if stats is not None:
                stats["datagrams"] = stats.get("datagrams", 0) + 1
                stats["max_datagram"] = max(stats.get("max_datagram", 0), len(dg))
                if len(dg) >= 16 and dg[0] & 0x10 and "first_header" not in stats:
                    stats["first_header"], stats["tlv"] = dg[:16].hex(), tlv_types(dg)
            jpeg = asm.feed(dg)
            if jpeg:
                n += 1
                if stats is not None:
                    stats.setdefault("frame_sizes", []).append(len(jpeg))
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
    if stats is not None:
        stats["frames"], stats["dropped"] = n, dropped
    print("saved %d frames to %s (%d incomplete frames dropped)" % (n, out, dropped))


def livetest(cam, out, assume_yes):
    """Guided test of the state-changing commands. Every step asks first; the camera is put back in play mode."""
    os.makedirs(out, exist_ok=True)
    report, summary = [], []

    def log(title, body):
        report.append("== %s\n%s\n" % (title, body))

    def ask(what):
        if assume_yes:
            return True
        a = input("\n%s\n  [Enter] run   [s] skip   [q] stop the test > " % what).strip().lower()
        if a == "q":
            raise KeyboardInterrupt
        return a != "s"

    def step(name, what, fn):
        if not ask(what):
            summary.append((name, "skipped", ""))
            return None
        t0 = time.time()
        try:
            result = fn()
            summary.append((name, "ok", "%.1f s" % (time.time() - t0)))
            return result if result is not None else True
        except CameraError as e:
            summary.append((name, "FAILED", str(e)))
            log(name + " FAILED", str(e))
            print("  failed: %s" % e)
            return None

    def own_folder():
        dirs = [e for e in cam.listdir("/DCIM") if e["is_dir"]]
        mine = [e for e in dirs if "OLYMP" in e["name"]] or dirs
        return sorted(mine, key=lambda e: e["name"])[-1]["path"] if mine else None

    print("Guided live test. It switches the camera to rec mode, reads its settings, receives live view,\n"
          "writes one setting back unchanged, takes ONE picture and returns to play mode.\n"
          "Point the camera at something it can focus on. Files go to %s/." % out)
    changed_mode = False
    try:
        log("start", "connect mode %s, model %s" % (cam.tag("get_connectmode.cgi", "connectmode"),
                                                    cam.tag("get_caminfo.cgi", "model")))
        folder = own_folder()
        before = {e["name"] for e in cam.listdir(folder)} if folder else set()
        log("card before", "folder %s, %d entries" % (folder, len(before)))

        def to_rec():
            cam.set_mode("rec", "0640x0480")
        if step("rec mode", "1/7  Switch the camera to rec mode (live view 640x480).", to_rec) is None:
            raise CameraError("without rec mode the remaining steps cannot run")
        changed_mode = True

        def read_props():
            raw = cam.text("get_camprop.cgi?com=desc&propname=desclist")
            log("desclist raw", raw)
            ds = cam.prop_desc("desclist")
            log("properties", "\n".join("%-18s %-6s %-22s %s" % (d["name"], d["attribute"], d["value"], " ".join(d["enum"]))
                                        for d in ds))
            log("get takemode raw", cam.text("get_camprop.cgi?com=get&propname=takemode"))
            return ds
        props = step("properties", "2/7  Read the remote-control properties (read-only).", read_props) or []

        def live():
            stats = {}
            liveview(cam, 20, os.path.join(out, "liveview"), 0, cam.timeout, stats)
            sizes = stats.get("frame_sizes", [])
            log("live view", "frames %s, dropped %s, datagrams %s, largest datagram %s bytes\n"
                             "frame sizes min/avg/max %s\nfirst header %s\nextension entries (type, words) %s"
                % (stats.get("frames"), stats.get("dropped"), stats.get("datagrams"), stats.get("max_datagram"),
                   ("%d / %d / %d" % (min(sizes), sum(sizes) // len(sizes), max(sizes))) if sizes else "-",
                   stats.get("first_header"), stats.get("tlv")))
        step("live view", "3/7  Receive 20 live-view frames (the camera's screen may go dark meanwhile).", live)

        def set_same():
            d = next((d for d in props if d["name"] == "isospeedvalue" and d["attribute"] == "getset"), None) or \
                next((d for d in props if d["attribute"] == "getset"), None)
            if d is None:
                raise CameraError("no settable property was read in step 2")
            body = '<?xml version="1.0"?>\r\n<set>\r\n<value>%s</value>\r\n</set>\r\n' % d["value"]
            reply = cam.text("set_camprop.cgi?com=set&propname=" + d["name"], body.encode())
            after = cam.tag("get_camprop.cgi?com=get&propname=" + d["name"], "value")
            log("set %s to its current value %r" % (d["name"], d["value"]), "reply %r\nreads back %r" % (reply, after))
            if after != d["value"]:
                raise CameraError("%s read back %r after writing %r" % (d["name"], after, d["value"]))
        step("set (unchanged value)", "4/7  Write one property back with the value it already has (no visible change).", set_same)

        shot = step("shoot", "5/7  Take ONE picture (half-press, 2 s for focus, full press, release).", lambda: cam.shoot())

        def fetch_last():
            for com in ("getlastjpg", "getrecview"):
                try:
                    data = cam.request("exec_takemisc.cgi?com=" + com)
                    log("exec_takemisc %s" % com, "%d bytes, starts %s" % (len(data), data[:4].hex()))
                    if data[:2] == b"\xff\xd8":
                        with open(os.path.join(out, com + ".jpg"), "wb") as f:
                            f.write(data)
                except CameraError as e:
                    log("exec_takemisc %s" % com, "ERROR %s" % e)
        if shot:
            step("last picture", "6/7  Ask the camera for the picture it just took (two commands, read-only).", fetch_last)

        def new_files():
            f = own_folder()
            now = cam.listdir(f) if f else []
            new = [e for e in now if e["name"] not in before]
            log("card after", "folder %s, %d entries, new: %s" % (f, len(now), [(e["name"], e["size"]) for e in new]))
            jpg = next((e for e in new if e["name"].upper().endswith(".JPG")), None)
            if jpg:
                with open(os.path.join(out, "thumb_" + jpg["name"]), "wb") as fh:
                    fh.write(cam.request("get_thumbnail.cgi?DIR=" + urllib.parse.quote(jpg["path"])))
            if shot and not new:
                raise CameraError("a picture was taken but no new file appears in %s" % f)
        step("new files", "7/7  List the card again to find the new picture and fetch its thumbnail (read-only).", new_files)
    except KeyboardInterrupt:
        summary.append(("test", "stopped by you", ""))
    except CameraError as e:
        summary.append(("test", "FAILED", str(e)))
    finally:
        if changed_mode:
            try:
                cam.set_mode("play")
                summary.append(("back to play mode", "ok", ""))
            except CameraError as e:
                summary.append(("back to play mode", "FAILED", str(e)))
        text = "emcam live test\n\nSUMMARY\n" + "\n".join("  %-24s %-16s %s" % r for r in summary) + "\n\n" + "\n".join(report)
        with open(os.path.join(out, "report.txt"), "w", encoding="utf-8") as f:
            f.write(text)
        print("\nSUMMARY")
        for r in summary:
            print("  %-24s %-16s %s" % r)
        print("\nReport and sample files are in %s/ ; copy that whole folder back." % out)


def probe(cam, out):
    """Read-only live check. Records raw replies so parsing assumptions can be verified afterwards."""
    lines = []

    def step(title, fn):
        try:
            result = fn()
        except CameraError as e:
            result = "ERROR: %s" % e
        lines.append("== %s\n%s\n" % (title, result))
        print("%-40s %s" % (title, "failed" if str(result).startswith("ERROR") else "ok"))
        return None if str(result).startswith("ERROR") else result

    def raw(path, limit=1500):
        return lambda: cam.request(path)[:limit].decode("latin-1")

    for path in ("get_connectmode.cgi", "get_caminfo.cgi", "get_unusedcapacity.cgi", "get_dcffilenum.cgi",
                 "get_activate.cgi", "get_gpsdivunit.cgi", "get_rsvimglist.cgi"):
        step("GET " + path, raw(path))
    step("GET get_commandlist.cgi (length, names)", lambda: "%d bytes: %s" % (
        len(cam.request("get_commandlist.cgi")), " ".join(re.findall(r'<cgi name="([^"]+)"', cam.text("get_commandlist.cgi")))))
    step("GET get_imglist.cgi?DIR=/DCIM (raw)", raw("get_imglist.cgi?DIR=/DCIM"))
    dirs = step("parsed /DCIM", lambda: cam.listdir("/DCIM")) or []
    first = None
    # the camera's own folders first, so the image checks run on a picture this camera took
    for d in sorted([e for e in dirs if e["is_dir"]], key=lambda e: "OLYMP" not in e["name"])[:2]:
        step("GET get_imglist.cgi?DIR=%s (raw, first 1500 bytes)" % d["path"], raw("get_imglist.cgi?DIR=" + d["path"]))
        entries = step("parsed %s (count, first 3)" % d["path"],
                       lambda d=d: (lambda l: "%d entries: %s" % (len(l), l[:3]))(cam.listdir(d["path"])))
        if first is None:
            try:
                first = next((e for e in cam.listdir(d["path"]) if e["name"].upper().endswith(".JPG")), None)
            except CameraError:
                pass
    if first:
        q = urllib.parse.quote(first["path"])
        for title, path in (("thumbnail", "get_thumbnail.cgi?DIR=" + q), ("resize 1024", "get_resizeimg.cgi?DIR=%s&size=1024" % q),
                            ("file itself", first["path"])):
            step("%s of %s (size, first bytes)" % (title, first["path"]),
                 lambda path=path: (lambda b: "%d bytes, starts %s" % (len(b), b[:4].hex()))(cam.request(path)))
        step("listed size of that file", lambda: first["size"])
    with open(out, "w", encoding="utf-8") as f:
        f.write("emcam probe (read-only requests only)\n\n" + "\n".join(lines))
    print("wrote %s" % out)


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
    p = sub.add_parser("livetest"); p.add_argument("--out", default="emcam-livetest"); p.add_argument("--yes", action="store_true")
    p = sub.add_parser("probe"); p.add_argument("-o", default="emcam-probe.txt")
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
        try:
            free = cam.free_bytes()
            print("free space   :", "4 GB or more (the camera's counter stops at 4294967295 bytes)" if free is None
                  else "%.1f MB" % (free / 1e6))
        except CameraError as e:
            print("free space   : (%s)" % e)
        try:                                   # counts pictures, with a RAW+JPEG pair as one
            print("pictures     :", cam.tag("get_dcffilenum.cgi", "dcffile"))
        except CameraError as e:
            print("pictures     : (%s)" % e)
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
    elif a.cmd == "livetest":
        livetest(cam, a.out, a.yes)
    elif a.cmd == "probe":
        probe(cam, a.o)
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
