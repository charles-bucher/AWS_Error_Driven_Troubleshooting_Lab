import os
from pathlib import Path
import shutil

# Base path to incidents
INCIDENTS_PATH = Path(r"C:\Users\buche\docs\Desktop\REPOS\AWS_Error_Driven_Troubleshooting_Lab\incidents")

def normalize_incident_folders():
    for folder in INCIDENTS_PATH.iterdir():
        if folder.is_dir():
            # Ensure folder name starts with 3-digit number
            parts = folder.name.split('-', 1)
            if len(parts[0]) != 3 or not parts[0].isdigit():
                print(f"⚠️  Folder '{folder.name}' does not start with a 3-digit number. Skipping rename.")
            
            # Check for nested scripts or misplaced files
            nested_scripts = folder / "scripts"
            if nested_scripts.exists() and nested_scripts.is_dir():
                for item in nested_scripts.iterdir():
                    shutil.move(str(item), str(folder))
                nested_scripts.rmdir()
                print(f"✅ Moved contents of '{nested_scripts}' up to '{folder.name}'")

            # Check required files
            required_files = ["README.md", "problem.py", "solution.py"]
            for f in required_files:
                f_path = folder / f
                if not f_path.exists():
                    print(f"⚠️  Missing '{f}' in {folder.name}")
                else:
                    print(f"✓ Found {f} in {folder.name}")

if __name__ == "__main__":
    normalize_incident_folders()
    print("\n🎯 Finished scanning and normalizing incident folders.")
