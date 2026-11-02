#!/usr/bin/env python3 -I
"""Model-agnostic firmware patcher for the OM/Olympus container.

Generic engine only: every body-specific fact (source hash, patch offsets, bytes, SD filename)
lives in an external *profile* JSON, NOT in this file. Profiles that embed community-authored patch
bytes are kept out of the repo by policy; this tool just consumes whatever profile path you pass.

Profile schema (per entry; a file may hold one object or a list — pick with --id):
  {
    "id": "em10-1.4",
    "source_sha256": "<hex of the untouched stock .BIN>",
    "cardfile": "E1139999.BIN",            # name to write on the SD card
    "flash_path": "DCOLYMP/E1139999.BIN",  # full SD path (informational)
    "features": [ { "name": "...", "patches": [
        { "block": 0, "offset": <int, block-relative into DECODED data>,
          "old": "<base64>", "new": "<base64>", "label": "..." } ] } ]
  }
A patch is applied to the DECODED block; new must equal old in length (in-place), and old must match
the current bytes (unless --force) so a patch can never be silently mis-applied to the wrong image.

usage:
  fwpatch.py plan   STOCK.BIN PROFILE.json [--id ID]            verify + list patches, apply nothing
  fwpatch.py build  STOCK.BIN PROFILE.json OUT.BIN [--id ID] [--features a,b] [--force]
                                                               apply, reseal, write OUT.BIN
"""
import sys, os, json, base64, hashlib, struct, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import omfw  # reuse the verified container codec (dec/enc/footer_v/blocks/rebuild)

def load_profile(path, want_id):
    obj = json.load(open(path, encoding="utf-8", errors="replace"))
    profs = obj if isinstance(obj, list) else [obj]
    if want_id is not None:
        profs = [p for p in profs if p.get("id") == want_id]
        if not profs: sys.exit("no profile with id %r in %s" % (want_id, path))
    elif len(profs) != 1:
        ids = [p.get("id") for p in profs]
        sys.exit("profile file holds %d entries; pass --id (one of %s)" % (len(profs), ids))
    return profs[0]

def iter_patches(prof, want_features):
    for feat in prof.get("features", []):
        fname = feat.get("name") or feat.get("id")
        if want_features and (fname not in want_features): continue
        for p in feat.get("patches", []):
            yield fname, p

def main():
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("cmd", choices=["plan", "build"])
    ap.add_argument("stock"); ap.add_argument("profile")
    ap.add_argument("out", nargs="?")
    ap.add_argument("--id"); ap.add_argument("--features"); ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    raw = open(a.stock, "rb").read()
    prof = load_profile(a.profile, a.id)
    want_features = set(a.features.split(",")) if a.features else None

    # 1. source-image identity
    sha = hashlib.sha256(raw).hexdigest()
    want = (prof.get("source_sha256") or "").lower()
    src_ok = (sha == want)
    print("profile id   : %s   body: %s   version: %s" % (prof.get("id"), prof.get("body"), prof.get("version")))
    print("source sha256: %s  (%s)" % (sha, "MATCH" if src_ok else "MISMATCH vs profile %s" % want))
    if not src_ok and not a.force:
        sys.exit("refusing: stock image does not match profile source_sha256 (use --force to override)")

    # 2. decode blocks once
    decoded = {b["idx"]: bytearray(omfw.dec(b["data"])) for b in omfw.blocks(raw)}

    # 3. apply (or just report) each patch
    applied = 0
    for feat, p in iter_patches(prof, want_features):
        blk, off = p["block"], p["offset"]
        old = base64.b64decode(p.get("old", "")); new = base64.b64decode(p["new"])
        lab = p.get("label") or p.get("name")
        if blk not in decoded: sys.exit("patch %r: block %d not in image" % (lab, blk))
        if len(new) != len(old) and old: sys.exit("patch %r: new len %d != old len %d (must be in-place)" % (lab, len(new), len(old)))
        cur = bytes(decoded[blk][off:off+len(new)])
        match = (not old) or (cur == old)
        print("  [%s] blk%d off=%d len=%d %-14s old_matches=%s" % (feat, blk, off, len(new), lab, match if old else "n/a"))
        if a.cmd == "build":
            if old and not match and not a.force:
                sys.exit("patch %r: current bytes != expected old at blk%d off=%d (use --force)" % (lab, blk, off))
            decoded[blk][off:off+len(new)] = new
            applied += 1
    if a.cmd == "plan":
        print("plan only — nothing written"); return

    # 4. reseal via the verified rebuild path (dec dir in memory -> re-encode -> footer)
    out = bytearray()
    for b in omfw.blocks(raw):
        pdata = bytes(decoded[b["idx"]])
        assert len(pdata) == b["dlen"]
        out += b["hdr"] + omfw.enc(pdata) + b["hdr"][:28] + struct.pack("<I", omfw.footer_v(b["hdr"], pdata))
    # 5. verify every footer re-parses clean
    for b in omfw.blocks(bytes(out)):
        v = omfw.footer_v(b["hdr"], omfw.dec(b["data"]))
        if not (b["ftr"][:28] == b["hdr"][:28] and struct.unpack("<I", b["ftr"][28:])[0] == v):
            sys.exit("INTERNAL: footer verify failed on block %d" % b["idx"])
    open(a.out, "wb").write(out)
    print("applied %d patch(es); wrote %s  %d bytes  sha=%s" % (
        applied, a.out, len(out), hashlib.sha256(out).hexdigest()[:12]))
    print("SD target: %s" % (prof.get("flash_path") or prof.get("cardfile") or "DCOLYMP/<cardfile>"))

if __name__ == "__main__":
    main()
