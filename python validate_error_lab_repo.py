import os

# Root repo path
ROOT = os.path.dirname(os.path.abspath(__file__))

# List of incidents
INCIDENTS_DIR = os.path.join(ROOT, "incidents")
incidents = [d for d in os.listdir(INCIDENTS_DIR) if os.path.isdir(os.path.join(INCIDENTS_DIR, d))]

# Scripts expected per incident
REQUIRED_SCRIPTS = ["deploy.py", "break.py", "collect_evidence.py", "teardown.py"]
# Evidence subfolders
EVIDENCE_FOLDERS = ["screenshots", "logs", "metrics"]

print("🧪 AWS ERROR-DRIVEN TROUBLESHOOTING LAB – VALIDATOR")
print("="*80)
print("\n🔍 Validating root structure...")

# Root checks
root_checks = ["README.md", "incidents", "scripts", "docs"]
all_root_valid = True
for item in root_checks:
    path = os.path.join(ROOT, item)
    if os.path.exists(path):
        print(f"✅ Found {item}")
    else:
        print(f"❌ Missing {item}")
        all_root_valid = False

print(f"✅ {len(incidents)} incident(s) detected\n")

# Incident validation
all_incidents_valid = True
for inc in sorted(incidents):
    print(f"📂 Validating incident: {inc}")
    inc_path = os.path.join(INCIDENTS_DIR, inc)
    
    # Scripts folder
    scripts_path = os.path.join(inc_path, "scripts")
    if os.path.exists(scripts_path):
        print(f"✅ {inc}: scripts/ present")
    else:
        print(f"❌ {inc}: missing scripts/")
        all_incidents_valid = False
        os.makedirs(scripts_path, exist_ok=True)
    
    # Evidence folder
    evidence_path = os.path.join(inc_path, "evidence")
    if not os.path.exists(evidence_path):
        print(f"❌ {inc}: missing evidence/")
        all_incidents_valid = False
        os.makedirs(evidence_path, exist_ok=True)
    
    # Check scripts
    for s in REQUIRED_SCRIPTS:
        s_path = os.path.join(scripts_path, s)
        if os.path.exists(s_path):
            print(f"✅ {inc}: scripts/{s}")
        else:
            print(f"❌ {inc}: missing script scripts/{s}")
            all_incidents_valid = False
    
    # Check evidence subfolders
    for ef in EVIDENCE_FOLDERS:
        ef_path = os.path.join(evidence_path, ef)
        if os.path.exists(ef_path):
            print(f"✅ {inc}: evidence/{ef}/")
        else:
            print(f"❌ {inc}: missing evidence/{ef}/")
            all_incidents_valid = False
            os.makedirs(ef_path, exist_ok=True)
    
    # README.md
    readme_path = os.path.join(inc_path, "README.md")
    if os.path.exists(readme_path):
        print(f"✅ {inc}: README.md")
    else:
        print(f"❌ {inc}: missing README.md")
        all_incidents_valid = False

print("\n🔐 Scanning for leaked credentials...")
secret_found = False
for root, dirs, files in os.walk(ROOT):
    for file in files:
        if file == os.path.basename(__file__) or file == "PLANNED.txt":
            continue
        path = os.path.join(root, file)
        with open(path, "r", errors="ignore") as f:
            content = f.read()
            if "AKIA" in content or "SECRET" in content or "PASSWORD" in content:
                print(f"🚨 SECRET RISK: {path}")
                secret_found = True

# Final output
if all_root_valid and all_incidents_valid and not secret_found:
    print("\n" + "="*80)
    print("✅ VALIDATION PASSED – All incidents structurally complete.")
else:
    print("\n" + "="*80)
    print("🚫 VALIDATION FAILED – Fix issues before sharing.")
