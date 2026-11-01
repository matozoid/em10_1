#!/usr/bin/env bash
# Query OM firmware server for a camera code and (optionally) download the BIN.
# usage: tools/fetch-firmware.sh [CODE=E113] [--download]
# Request body format taken from the community script by M. Selig (Feb 2026, mu-43).
set -euo pipefail
CODE="${1:-E113}"; DL="${2:-}"
SERIAL="${CAM_SERIAL:-V5PF30000}"
URL=https://fw01.om-digitalsolutions.net/ww_inform/fcache.do
OUT="$(dirname "$0")/../firmware/stock"; mkdir -p "$OUT"
REPLY="$OUT/reply-$CODE.xml"
curl -sS --user-agent Olympus -H 'Content-Type: text/xml; Charset=UTF-8' --data-binary @- "$URL" -o "$REPLY" <<EOF
<?xml version="1.0"?>
<firmware_demand>
<revision>0001</revision>
<mac_address>00-00-00-00-80-D6</mac_address>
<time>$(date +%Y%m%d%H%M%S)</time>
<language>ENU</language>
<application>FWUT</application>
<type>0000</type>
<version>00005000</version>
<os>WIN</os>
<country_code>0001</country_code>
<hardwares>
<firmup_mode>0</firmup_mode>
<hardware_info>
<hard_code>OLY${CODE}000000000</hard_code>
<firmware_version>00001000</firmware_version>
<serial_no>$SERIAL</serial_no>
<default_languages><code>ENU</code></default_languages>
</hardware_info>
</hardwares>
</firmware_demand>
EOF
cat "$REPLY"; echo
[ "$DL" = "--download" ] || exit 0
u=$(xmllint --xpath 'string(//url)' "$REPLY"); f=$(xmllint --xpath 'string(//file_name)' "$REPLY"); s=$(xmllint --xpath 'string(//file_size)' "$REPLY")
[ -n "$u" ] && [ -n "$f" ] || { echo "no firmware in reply" >&2; exit 1; }
curl -sS -o "$OUT/$f" "$u"
[ "$(stat -c%s "$OUT/$f")" = "$s" ] || { echo "size mismatch (want $s)" >&2; exit 1; }
sha256sum "$OUT/$f"
