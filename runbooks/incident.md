Broken systemd Service — myapp.service Fails to Start

Hands-on Linux troubleshooting scenario for Cloud Support workflows. This incident simulates a real-world failure where a systemd service cannot start due to an incorrect ExecStart path.



🧭 OverviewBroken systemd Service — myapp.service Fails to Start

Hands-on Linux troubleshooting scenario for Cloud Support workflows. This incident simulates a real-world failure where a systemd service cannot start due to an incorrect ExecStart path.



🧭 Overview

A Linux EC2 instance is reporting that the application service myapp.service is failing to start. The customer reports 503 errors from the application endpoint, and CloudWatch alarms are firing due to failed health checks.

This incident demonstrates:

\- Linux service troubleshooting

\- systemd debugging

\- Log analysis

\- Root cause analysis (RCA)

\- Automated remediation



🚨 Impact

\- Application unavailable

\- Load balancer health checks failing

\- Service stuck in restart loop

\- CloudWatch alarm: EC2StatusCheckFailed\_System



🔍 Initial Findings

Checking the service status:

sudo systemctl status myapp.service

Output shows:

ExecStart=/usr/local/bin/myapp: No such file or directory

Journal logs confirm repeated failures:

sudo journalctl -u myapp.service --no-pager



🛠 Troubleshooting Steps

\- Inspect systemd unit file:

sudo cat /etc/systemd/system/myapp.service

\- Locate the actual binary:

sudo find / -name myapp

\- Verified binary exists at:

/opt/myapp/myapp

\- Compared expected vs actual paths.

\- Attempted manual start:

sudo systemctl start myapp.service

→ Failed due to incorrect ExecStart path.



🧩 Root Cause Analysis (RCA)

Root Cause

The systemd unit file referenced a non-existent binary path:

ExecStart=/usr/local/bin/myapp

The actual binary was located at:

/opt/myapp/myapp

Why It Happened

\- Deployment script updated the binary but not the systemd unit file

\- No validation step in CI/CD

\- No monitoring on systemd service failures

Severity

Medium — service outage but quick recovery possible.



✅ Resolution

\- Update the systemd unit file:

sudo sed -i 's|/usr/local/bin/myapp|/opt/myapp/myapp|g' /etc/systemd/system/myapp.service

\- Reload systemd:

sudo systemctl daemon-reload

\- Restart the service:

sudo systemctl restart myapp.service

\- Verify:

sudo systemctl status myapp.service

\- Confirm application endpoint returns 200 OK.



🔧 Automated Fix Script

\#!/bin/bash

Automated remediation for broken myapp.service due to incorrect ExecStart path

SERVICE="myapp.service" UNIT\_FILE="/etc/systemd/system/$SERVICE" OLD\_PATH="/usr/local/bin/myapp" NEW\_PATH="/opt/myapp/myapp"

echo "\[+] Checking systemd unit file for incorrect ExecStart path..."

if grep -q "$OLD\_PATH" "$UNIT\_FILE"; then echo "\[+] Incorrect ExecStart path found. Updating to correct path..." sudo sed -i "s|$OLD\_PATH|$NEW\_PATH|g" "$UNIT\_FILE" else echo "\[!] No incorrect ExecStart path found. Nothing to update." exit 1 fi

echo "\[+] Reloading systemd daemon..." sudo systemctl daemon-reload

echo "\[+] Restarting service..." sudo systemctl restart $SERVICE

echo "\[+] Checking service status..." sudo systemctl status $SERVICE --no-pager

echo "\[+] Remediation complete."



📁 Logs

Place any relevant logs here:

\- journalctl-output.txt

\- systemctl-status.txt

\- Application logs (if applicable)

Example command to export logs:

sudo journalctl -u myapp.service --no-pager > logs/journalctl-output.txt



🛡 Prevention

\- Add CI/CD validation to confirm binary paths

\- Add CloudWatch alarm for systemd service failures

\- Implement automated rollback on failed service start

\- Add post-deployment smoke tests



📌 Summary

This incident demonstrates a realistic Linux/systemd failure commonly seen in Cloud Support roles. It highlights your ability to:

\- Diagnose service failures

\- Analyze logs

\- Perform root cause analysis

\- Apply fixes manually and via automation

\- Document incidents in a professional, AWS-style format

Broken systemd Service — myapp.service Fails to Start

Hands-on Linux troubleshooting scenario for Cloud Support workflows. This incident simulates a real-world failure where a systemd service cannot start due to an incorrect ExecStart path.



🧭 Overview

A Linux EC2 instance is reporting that the application service myapp.service is failing to start. The customer reports 503 errors from the application endpoint, and CloudWatch alarms are firing due to failed health checks.

This incident demonstrates:

\- Linux service troubleshooting

\- systemd debugging

\- Log analysis

\- Root cause analysis (RCA)

\- Automated remediation



🚨 Impact

\- Application unavailable

\- Load balancer health checks failing

\- Service stuck in restart loop

\- CloudWatch alarm: EC2StatusCheckFailed\_System



🔍 Initial Findings

Checking the service status:

sudo systemctl status myapp.service

Output shows:

ExecStart=/usr/local/bin/myapp: No such file or directory

Journal logs confirm repeated failures:

sudo journalctl -u myapp.service --no-pager



🛠 Troubleshooting Steps

\- Inspect systemd unit file:

sudo cat /etc/systemd/system/myapp.service

\- Locate the actual binary:

sudo find / -name myapp

\- Verified binary exists at:

/opt/myapp/myapp

\- Compared expected vs actual paths.

\- Attempted manual start:

sudo systemctl start myapp.service

→ Failed due to incorrect ExecStart path.



🧩 Root Cause Analysis (RCA)

Root Cause

The systemd unit file referenced a non-existent binary path:

ExecStart=/usr/local/bin/myapp

The actual binary was located at:

/opt/myapp/myapp

Why It Happened

\- Deployment script updated the binary but not the systemd unit file

\- No validation step in CI/CD

\- No monitoring on systemd service failures

Severity

Medium — service outage but quick recovery possible.



✅ Resolution

\- Update the systemd unit file:

sudo sed -i 's|/usr/local/bin/myapp|/opt/myapp/myapp|g' /etc/systemd/system/myapp.service

\- Reload systemd:

sudo systemctl daemon-reload

\- Restart the service:

sudo systemctl restart myapp.service

\- Verify:

sudo systemctl status myapp.service

\- Confirm application endpoint returns 200 OK.



🔧 Automated Fix Script

\#!/bin/bash

Automated remediation for broken myapp.service due to incorrect ExecStart path

SERVICE="myapp.service" UNIT\_FILE="/etc/systemd/system/$SERVICE" OLD\_PATH="/usr/local/bin/myapp" NEW\_PATH="/opt/myapp/myapp"

echo "\[+] Checking systemd unit file for incorrect ExecStart path..."

if grep -q "$OLD\_PATH" "$UNIT\_FILE"; then echo "\[+] Incorrect ExecStart path found. Updating to correct path..." sudo sed -i "s|$OLD\_PATH|$NEW\_PATH|g" "$UNIT\_FILE" else echo "\[!] No incorrect ExecStart path found. Nothing to update." exit 1 fi

echo "\[+] Reloading systemd daemon..." sudo systemctl daemon-reload

echo "\[+] Restarting service..." sudo systemctl restart $SERVICE

echo "\[+] Checking service status..." sudo systemctl status $SERVICE --no-pager

echo "\[+] Remediation complete."



📁 Logs

Place any relevant logs here:

\- journalctl-output.txt

\- systemctl-status.txt

\- Application logs (if applicable)

Example command to export logs:

sudo journalctl -u myapp.service --no-pager > logs/journalctl-output.txt



🛡 Prevention

\- Add CI/CD validation to confirm binary paths

\- Add CloudWatch alarm for systemd service failures

\- Implement automated rollback on failed service start

\- Add post-deployment smoke tests



📌 Summary

This incident demonstrates a realistic Linux/systemd failure commonly seen in Cloud Support roles. It highlights your ability to:

\- Diagnose service failures

\- Analyze logs

\- Perform root cause analysis

\- Apply fixes manually and via automation

\- Document incidents in a professional, AWS-style format



A Linux EC2 instance is reporting that the application service myapp.service is failing to start. The customer reports 503 errors from the application endpoint, and CloudWatch alarms are firing due to failed health checks.

This incident demonstrates:

\- Linux service troubleshooting

\- systemd debugging

\- Log analysis

\- Root cause analysis (RCA)

\- Automated remediation



🚨 Impact

\- Application unavailable

\- Load balancer health checks failing

\- Service stuck in restart loop

\- CloudWatch alarm: EC2StatusCheckFailed\_System



🔍 Initial Findings

Checking the service status:

sudo systemctl status myapp.service

Output shows:

ExecStart=/usr/local/bin/myapp: No such file or directory

Journal logs confirm repeated failures:

sudo journalctl -u myapp.service --no-pager



🛠 Troubleshooting Steps

\- Inspect systemd unit file:

sudo cat /etc/systemd/system/myapp.service

\- Locate the actual binary:

sudo find / -name myapp

\- Verified binary exists at:

/opt/myapp/myapp

\- Compared expected vs actual paths.

\- Attempted manual start:

sudo systemctl start myapp.service

→ Failed due to incorrect ExecStart path.



🧩 Root Cause Analysis (RCA)

Root Cause

The systemd unit file referenced a non-existent binary path:

ExecStart=/usr/local/bin/myapp

The actual binary was located at:

/opt/myapp/myapp

Why It Happened

\- Deployment script updated the binary but not the systemd unit file

\- No validation step in CI/CD

\- No monitoring on systemd service failures

Severity

Medium — service outage but quick recovery possible.



✅ Resolution

\- Update the systemd unit file:

sudo sed -i 's|/usr/local/bin/myapp|/opt/myapp/myapp|g' /etc/systemd/system/myapp.service

\- Reload systemd:

sudo systemctl daemon-reload

\- Restart the service:

sudo systemctl restart myapp.service

\- Verify:

sudo systemctl status myapp.service

\- Confirm application endpoint returns 200 OK.



🔧 Automated Fix Script

\#!/bin/bash

Automated remediation for broken myapp.service due to incorrect ExecStart path

SERVICE="myapp.service" UNIT\_FILE="/etc/systemd/system/$SERVICE" OLD\_PATH="/usr/local/bin/myapp" NEW\_PATH="/opt/myapp/myapp"

echo "\[+] Checking systemd unit file for incorrect ExecStart path..."

if grep -q "$OLD\_PATH" "$UNIT\_FILE"; then echo "\[+] Incorrect ExecStart path found. Updating to correct path..." sudo sed -i "s|$OLD\_PATH|$NEW\_PATH|g" "$UNIT\_FILE" else echo "\[!] No incorrect ExecStart path found. Nothing to update." exit 1 fi

echo "\[+] Reloading systemd daemon..." sudo systemctl daemon-reload

echo "\[+] Restarting service..." sudo systemctl restart $SERVICE

echo "\[+] Checking service status..." sudo systemctl status $SERVICE --no-pager

echo "\[+] Remediation complete."



📁 Logs

Place any relevant logs here:

\- journalctl-output.txt

\- systemctl-status.txt

\- Application logs (if applicable)

Example command to export logs:

sudo journalctl -u myapp.service --no-pager > logs/journalctl-output.txt



🛡 Prevention

\- Add CI/CD validation to confirm binary paths

\- Add CloudWatch alarm for systemd service failures

\- Implement automated rollback on failed service start

\- Add post-deployment smoke tests



📌 Summary

This incident demonstrates a realistic Linux/systemd failure commonly seen in Cloud Support roles. It highlights your ability to:

\- Diagnose service failures

\- Analyze logs

\- Perform root cause analysis

\- Apply fixes manually and via automation

\- Document incidents in a professional, AWS-style format




## Skills Demonstrated
Automation, monitoring, incident response, troubleshooting, and Infrastructure as Code using Terraform/CloudFormation.

## Usage
Clone the repo and follow the scripts or Terraform configurations to deploy and test resources. Designed to simulate realistic AWS cloud incidents.

## What I Learned
Hands-on experience troubleshooting AWS incidents, applying automation, monitoring with CloudWatch, and ensuring cloud reliability.
