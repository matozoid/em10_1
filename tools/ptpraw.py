#!/usr/bin/env python3
# Minimal raw PTP/USB client via libusb-1.0 ctypes. Read-only PTP ops only.
# Sends: OpenSession, GetDeviceInfo, and optional Olympus unlock (0x9481/0x9482).
# No capture/format/delete/property-write is ever issued.
import ctypes as C, struct, sys

VID, PID = 0x07b4, 0x012f
lib = C.CDLL("libusb-1.0.so.0")

# --- libusb prototypes we need ---
lib.libusb_init.argtypes = [C.POINTER(C.c_void_p)]
lib.libusb_open_device_with_vid_pid.restype = C.c_void_p
lib.libusb_open_device_with_vid_pid.argtypes = [C.c_void_p, C.c_uint16, C.c_uint16]
lib.libusb_get_device.restype = C.c_void_p
lib.libusb_get_device.argtypes = [C.c_void_p]
lib.libusb_kernel_driver_active.argtypes = [C.c_void_p, C.c_int]
lib.libusb_detach_kernel_driver.argtypes = [C.c_void_p, C.c_int]
lib.libusb_claim_interface.argtypes = [C.c_void_p, C.c_int]
lib.libusb_release_interface.argtypes = [C.c_void_p, C.c_int]
lib.libusb_close.argtypes = [C.c_void_p]
lib.libusb_bulk_transfer.argtypes = [C.c_void_p, C.c_ubyte, C.c_void_p, C.c_int,
                                     C.POINTER(C.c_int), C.c_uint]
lib.libusb_clear_halt.argtypes = [C.c_void_p, C.c_ubyte]

class EP_DESC(C.Structure):
    _fields_ = [("bLength", C.c_ubyte), ("bDescriptorType", C.c_ubyte),
                ("bEndpointAddress", C.c_ubyte), ("bmAttributes", C.c_ubyte),
                ("wMaxPacketSize", C.c_uint16), ("bInterval", C.c_ubyte),
                ("bRefresh", C.c_ubyte), ("bSynchAddress", C.c_ubyte),
                ("extra", C.c_void_p), ("extra_length", C.c_int)]
class IF_DESC(C.Structure):
    _fields_ = [("bLength", C.c_ubyte), ("bDescriptorType", C.c_ubyte),
                ("bInterfaceNumber", C.c_ubyte), ("bAlternateSetting", C.c_ubyte),
                ("bNumEndpoints", C.c_ubyte), ("bInterfaceClass", C.c_ubyte),
                ("bInterfaceSubClass", C.c_ubyte), ("bInterfaceProtocol", C.c_ubyte),
                ("iInterface", C.c_ubyte), ("endpoint", C.POINTER(EP_DESC)),
                ("extra", C.c_void_p), ("extra_length", C.c_int)]
class IF(C.Structure):
    _fields_ = [("altsetting", C.POINTER(IF_DESC)), ("num_altsetting", C.c_int)]
class CONF(C.Structure):
    _fields_ = [("bLength", C.c_ubyte), ("bDescriptorType", C.c_ubyte),
                ("wTotalLength", C.c_uint16), ("bNumInterfaces", C.c_ubyte),
                ("bConfigurationValue", C.c_ubyte), ("iConfiguration", C.c_ubyte),
                ("bmAttributes", C.c_ubyte), ("MaxPower", C.c_ubyte),
                ("interface", C.POINTER(IF)), ("extra", C.c_void_p),
                ("extra_length", C.c_int)]
lib.libusb_get_active_config_descriptor.argtypes = [C.c_void_p, C.POINTER(C.POINTER(CONF))]

ctx = C.c_void_p()
assert lib.libusb_init(C.byref(ctx)) == 0, "libusb_init failed"
h = lib.libusb_open_device_with_vid_pid(ctx, VID, PID)
if not h:
    print("open failed (device gone, or interface busy). free gvfs then retry."); sys.exit(2)
dev = lib.libusb_get_device(h)

# discover bulk IN/OUT + interrupt endpoints on interface 0
confp = C.POINTER(CONF)()
assert lib.libusb_get_active_config_descriptor(dev, C.byref(confp)) == 0
conf = confp.contents
iface0 = conf.interface[0].altsetting[0]
IFNUM = iface0.bInterfaceNumber
ep_in = ep_out = None
for i in range(iface0.bNumEndpoints):
    e = iface0.endpoint[i]
    addr, attr = e.bEndpointAddress, e.bmAttributes & 3
    if attr == 2:  # bulk
        if addr & 0x80: ep_in = addr
        else: ep_out = addr
print(f"iface={IFNUM} class={iface0.bInterfaceClass:#x} proto={iface0.bInterfaceProtocol} "
      f"bulk_in={ep_in:#x} bulk_out={ep_out:#x}")

try:
    if lib.libusb_kernel_driver_active(h, IFNUM) == 1:
        lib.libusb_detach_kernel_driver(h, IFNUM)
except Exception: pass
rc = lib.libusb_claim_interface(h, IFNUM)
if rc != 0:
    print(f"claim_interface failed rc={rc} (gvfs still holds it?)"); sys.exit(3)
# clear any left-over endpoint halt from a prior stalled op
lib.libusb_clear_halt(h, ep_in); lib.libusb_clear_halt(h, ep_out)

TID = 0
def bulk_out(data, to=4000):
    buf = (C.c_ubyte * len(data)).from_buffer_copy(data); n = C.c_int(0)
    rc = lib.libusb_bulk_transfer(h, ep_out, buf, len(data), C.byref(n), to)
    if rc != 0: raise RuntimeError(f"bulk_out rc={rc}")
    return n.value
def bulk_in(nbytes=65536, to=4000):
    buf = (C.c_ubyte * nbytes)(); n = C.c_int(0)
    rc = lib.libusb_bulk_transfer(h, ep_in, buf, nbytes, C.byref(n), to)
    if rc != 0: raise RuntimeError(f"bulk_in rc={rc}")
    return bytes(buf[:n.value])

def cmd(code, params=(), data_in=False):
    """Issue a PTP operation. Returns (resp_code, data_bytes|None)."""
    global TID; TID += 1; tid = TID
    pl = b"".join(struct.pack("<I", p) for p in params)
    hdr = struct.pack("<IHHI", 12 + len(pl), 1, code, tid) + pl
    bulk_out(hdr)
    data = None
    if data_in:
        first = bulk_in()
        ln, typ, c, t = struct.unpack("<IHHI", first[:12])
        if typ == 2:  # data phase
            data = first[12:]
            while len(data) + 12 < ln:
                data += bulk_in()
            data = data[:ln - 12]
            resp = bulk_in()
        else:
            resp = first  # was actually the response (no data)
    else:
        resp = bulk_in()
    rln, rtyp, rcode, rtid = struct.unpack("<IHHI", resp[:12])
    return rcode, data

def rd_str(b, o):
    n = b[o]; o += 1
    s = b[o:o + n*2].decode("utf-16-le").rstrip("\x00"); return s, o + n*2
def rd_au16(b, o):
    (cnt,) = struct.unpack_from("<I", b, o); o += 4
    arr = list(struct.unpack_from("<%dH" % cnt, b, o)); return arr, o + cnt*2

def parse_devinfo(b):
    o = 0
    (std,) = struct.unpack_from("<H", b, o); o += 2
    (vext,) = struct.unpack_from("<I", b, o); o += 4
    (vver,) = struct.unpack_from("<H", b, o); o += 2
    vdesc, o = rd_str(b, o)
    (fmode,) = struct.unpack_from("<H", b, o); o += 2
    ops, o = rd_au16(b, o); evts, o = rd_au16(b, o); props, o = rd_au16(b, o)
    capf, o = rd_au16(b, o); imgf, o = rd_au16(b, o)
    mfr, o = rd_str(b, o); model, o = rd_str(b, o); dver, o = rd_str(b, o); serial, o = rd_str(b, o)
    return dict(std=std, vext=vext, vver=vver, vdesc=vdesc, fmode=fmode, ops=ops,
                evts=evts, props=props, capf=capf, imgf=imgf,
                mfr=mfr, model=model, dver=dver, serial=serial)

def hx(a): return " ".join(f"{x:#06x}" for x in a)
def show(tag, d):
    print(f"\n===== DeviceInfo [{tag}] =====")
    print(f"StandardVersion={d['std']} VendorExtID={d['vext']:#06x} VendorExtVer={d['vver']} "
          f"FunctionalMode={d['fmode']:#x} desc={d['vdesc']!r}")
    print(f"Mfr={d['mfr']!r} Model={d['model']!r} DeviceVersion={d['dver']!r} Serial={d['serial']!r}")
    print(f"OperationsSupported ({len(d['ops'])}): {hx(d['ops'])}")
    print(f"EventsSupported ({len(d['evts'])}): {hx(d['evts'])}")
    print(f"DevicePropsSupported ({len(d['props'])}): {hx(d['props'])}")
    print(f"CaptureFormats ({len(d['capf'])}): {hx(d['capf'])}")
    print(f"ImageFormats ({len(d['imgf'])}): {hx(d['imgf'])}")

try:
    # 1. OpenSession (safe; session id 1)
    r, _ = cmd(0x1002, (1,)); print(f"OpenSession -> resp={r:#06x}")
    # 2. GetDeviceInfo (verbatim) in current MTP mode
    r, d = cmd(0x1001, (), data_in=True); print(f"GetDeviceInfo -> resp={r:#06x}")
    if d: show("MTP / pre-unlock", parse_devinfo(d)); mtp_ops = parse_devinfo(d)['ops']
    else: mtp_ops = []
    # 3. Olympus unlock attempts (approved: 0x9481, 0x9482). Non-destructive session ops.
    for oc in (0x9481, 0x9482):
        try:
            r, dd = cmd(oc, (1,), data_in=False)
            print(f"unlock {oc:#06x} -> resp={r:#06x}")
        except Exception as e:
            print(f"unlock {oc:#06x} -> STALL/err ({e}) = op rejected; clearing halt")
            lib.libusb_clear_halt(h, ep_out); lib.libusb_clear_halt(h, ep_in)
    # 4. Re-read DeviceInfo; detect whether op set changed (= entered control mode)
    r, d2 = cmd(0x1001, (), data_in=True); print(f"\nGetDeviceInfo(post-unlock) -> resp={r:#06x}")
    if d2:
        di2 = parse_devinfo(d2); show("post-unlock", di2)
        print("\nMODE CHANGE:" , "YES (op set differs)" if di2['ops'] != mtp_ops else "NO (identical op set)")
    # 5. Close session
    cmd(0x1003, (1,))
finally:
    lib.libusb_release_interface(h, IFNUM)
    lib.libusb_close(h)
