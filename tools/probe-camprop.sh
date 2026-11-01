#!/usr/bin/env bash
# Read-only live test of camprop CGIs. Joins camera AP, queries, rejoins home Wi-Fi.
# Needs a real terminal for the password prompt, or CAM_PASS=... in the environment.
# SWITCH=1 additionally calls switch_cammode?mode=rec (changes camera mode, no writes to card/settings), then back to the original mode.
set -u
SSID="${CAM_SSID:-E-M10-P-<serial>}"; HOME_CON="${HOME_CON:-<home-connection>}"; H=192.168.0.10
OUT="$(dirname "$0")/../research/camera-probe-camprop-$(date +%Y%m%d-%H%M%S).txt"
if [ -z "${CAM_PASS:-}" ]; then read -rsp "Camera Wi-Fi password: " CAM_PASS </dev/tty; echo; fi
g(){ echo "== GET $1"; curl -s -m 8 -i "http://$H/$1" | head -c 6000; echo; }
{
nmcli dev wifi rescan 2>/dev/null; sleep 3
nmcli dev wifi connect "$SSID" password "$CAM_PASS" ifname wlp4s0 || echo "JOIN FAILED"
sleep 5
g get_connectmode.cgi
g get_caminfo.cgi
for p in desclist takemode drivemode focalvalue expcomp shutspeedvalue isospeedvalue wbvalue noisereduction lowvibtime bulbtimelimit artfilter digitaltelecon touchactiveframe; do
  g "get_camprop.cgi?com=get&propname=$p"
  g "get_camprop.cgi?com=desc&propname=$p"
done
if [ "${SWITCH:-0}" = 1 ]; then
  g "switch_cammode.cgi?mode=rec&lvqty=0320x0240"; sleep 2
  for p in desclist takemode wbvalue isospeedvalue; do g "get_camprop.cgi?com=get&propname=$p"; g "get_camprop.cgi?com=desc&propname=$p"; done
  g "switch_cammode.cgi?mode=play"
fi
nmcli con up "$HOME_CON"
} 2>&1 | tee "$OUT"
echo "saved $OUT"
