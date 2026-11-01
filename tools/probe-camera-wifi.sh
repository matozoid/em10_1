#!/usr/bin/env bash
# Join camera AP, probe read-only CGI endpoints, rejoin home Wi-Fi. No writes to the camera.
# usage: tools/probe-camera-wifi.sh   (prompts for password; or set CAM_PASS)
set -u
SSID="${CAM_SSID:-E-M10-P-V5PG20539}"
HOME_CON="${HOME_CON:-pororoca}"
OUT="$(dirname "$0")/../research/camera-probe-$(date +%Y%m%d-%H%M%S).txt"
if [ -z "${CAM_PASS:-}" ]; then [ -r /dev/tty ] && [ -t 0 -o -e /dev/tty ] && { read -rsp "Camera Wi-Fi password: " CAM_PASS </dev/tty || true; echo; }; fi
: "${CAM_PASS:?no TTY: run in a real terminal, or CAM_PASS=... $0}"
{
echo "== join $SSID"
nmcli dev wifi rescan 2>/dev/null; sleep 3
nmcli dev wifi connect "$SSID" password "$CAM_PASS" ifname wlp4s0 || echo "JOIN FAILED"
sleep 5
echo "== addr/route"; ip -4 addr show wlp4s0 | grep inet; ip route show dev wlp4s0
GW=$(ip route show dev wlp4s0 | awk '/default/{print $3}')
echo "gateway: ${GW:-none}"
for h in 192.168.0.10 ${GW:-}; do
  [ -z "$h" ] && continue
  echo "== ping $h"; ping -c2 -W2 "$h" | tail -2
  for p in get_connectmode get_caminfo get_commandlist fwup_getversions; do
    echo "== GET http://$h/$p.cgi"
    curl -s -m 8 -i "http://$h/$p.cgi" | head -c 20000; echo
  done
done
echo "== rejoin $HOME_CON"
nmcli con up "$HOME_CON"
} 2>&1 | tee "$OUT"
echo "saved $OUT"
