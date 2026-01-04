#!/bin/bash
Automated remediation for broken myapp.service due to incorrect ExecStart path
SERVICE="myapp.service" UNIT_FILE="/etc/systemd/system/$SERVICE" OLD_PATH="/usr/local/bin/myapp" NEW_PATH="/opt/myapp/myapp"
echo "[+] Checking systemd unit file for incorrect ExecStart path..."
if grep -q "$OLD_PATH" "$UNIT_FILE"; then echo "[+] Incorrect ExecStart path found. Updating to correct path..." sudo sed -i "s|$OLD_PATH|$NEW_PATH|g" "$UNIT_FILE" else echo "[!] No incorrect ExecStart path found. Nothing to update." exit 1 fi
echo "[+] Reloading systemd daemon..." sudo systemctl daemon-reload
echo "[+] Restarting service..." sudo systemctl restart $SERVICE
echo "[+] Checking service status..." sudo systemctl status $SERVICE --no-pager
echo "[+] Remediation complete."


