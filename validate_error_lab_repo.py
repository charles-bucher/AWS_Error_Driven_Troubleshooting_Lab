#!/usr/bin/env python3
"""
AWS Error-Driven Troubleshooting Lab – Repository Validator
Author: Charles Bucher
Purpose: Enforce production-grade lab structure and evidence standards
"""

import os
import re
import sys

ROOT_REQUIRED = [
    "README.md",
    "incidents",
    "scripts",
    "docs",
]

INCIDENT_REQUIRED_DIRS = [
    "scripts",
    "evidence",
]

INCIDENT_EVIDENCE_DIRS = [
    "screenshots",
    "logs",
    "metrics",
]

INCIDENT_REQUIRED_SCRIPTS = [
    "deploy.py",
    "break.py",
    "collect_evidence.py",
    "teardown.py",
]

FORBIDDEN_PATTERNS = [
    r"AKIA[0-9A-Z]{16}",        # AWS Access Key
    r"aws_secret_access_key",
    r"BEGIN RSA PRIVATE KEY",
    r"\.pem$",
    r"\.tfstate$",
]

def fail(msg):
    print(f"❌ {msg}")
    return False

def pass_ok(msg):
    print(f"✅ {msg}")
    return True

def scan_for_secrets(root):
    bad = False
    for path, _, files in os.walk(root):
        for f in files:
            full = os.path.join(path, f)
            try:
                with open(full, "r", encoding="utf-8", errors="ignore") as fh:
                    content = fh.read()
                    for pattern in FORBIDDEN_PATTERNS:
                        if re.search(pattern, content):
                            print(f"🚨 SECRET RISK: {full}")
                            bad = True
            except Exception:
                continue
    return not bad

def validate_root(root):
    print("\n🔍 Validating root structure...")
    ok = True
    for item in ROOT_REQUIRED:
        if not os.path.exists(os.path.join(root, item)):
            ok &= fail(f"Missing required root item: {item}")
        else:
            pass_ok(f"Found {item}")
    return ok

def validate_incident(path):
    ok = True
    name = os.path.basename(path)
    print(f"\n📂 Validating incident: {name}")

    for d in INCIDENT_REQUIRED_DIRS:
        if not os.path.isdir(os.path.join(path, d)):
            ok &= fail(f"{name}: missing directory '{d}'")
        else:
            pass_ok(f"{name}: {d}/ present")

    scripts_path = os.path.join(path, "scripts")
    if os.path.isdir(scripts_path):
        for s in INCIDENT_REQUIRED_SCRIPTS:
            if not os.path.isfile(os.path.join(scripts_path, s)):
                ok &= fail(f"{name}: missing script scripts/{s}")
            else:
                pass_ok(f"{name}: scripts/{s}")

    evidence_root = os.path.join(path, "evidence")
    for d in INCIDENT_EVIDENCE_DIRS:
        if not os.path.isdir(os.path.join(evidence_root, d)):
            ok &= fail(f"{name}: missing evidence/{d}/")
        else:
            pass_ok(f"{name}: evidence/{d}/")

    readme = os.path.join(path, "README.md")
    if not os.path.isfile(readme):
        ok &= fail(f"{name}: missing README.md (RCA report)")
    else:
        pass_ok(f"{name}: README.md")

    return ok

def validate_incidents(root):
    incidents_path = os.path.join(root, "incidents")
    if not os.path.isdir(incidents_path):
        return fail("incidents/ directory missing")

    ok = True
    incidents = [
        os.path.join(incidents_path, d)
        for d in os.listdir(incidents_path)
        if os.path.isdir(os.path.join(incidents_path, d))
    ]

    if not incidents:
        ok &= fail("No incidents found")
    else:
        pass_ok(f"{len(incidents)} incident(s) detected")

    for incident in incidents:
        ok &= validate_incident(incident)

    return ok

def main():
    root = os.getcwd()
    print("=" * 80)
    print("🧪 AWS ERROR-DRIVEN TROUBLESHOOTING LAB – VALIDATOR")
    print("=" * 80)

    ok = True
    ok &= validate_root(root)
    ok &= validate_incidents(root)

    print("\n🔐 Scanning for leaked credentials...")
    if scan_for_secrets(root):
        pass_ok("No credential leaks detected")
    else:
        ok = False

    print("\n" + "=" * 80)
    if ok:
        print("🎉 VALIDATION PASSED – Repo is interview-ready.")
        sys.exit(0)
    else:
        print("🚫 VALIDATION FAILED – Fix issues before sharing.")
        sys.exit(1)

if __name__ == "__main__":
    main()
