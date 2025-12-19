# File: aws_lab_validator.py
# Purpose: Validate AWS_Error_Driven_Troubleshooting_Lab repo structure and content

import os
from datetime import datetime

# ==========================
# CONFIGURATION
# ==========================
REPO_PATH = r"C:\Users\buche\docs\Desktop\REPOS\AWS_Error_Driven_Troubleshooting_Lab"

# Expected structure
EXPECTED = {
    "root_files": ["README.md"],
    "terraform": ["provider.tf", "versions.tf"],
    "scripts": ["error_simulation.py", "remediation.py", "monitoring.py"],
    "lambdas": ["index.py"],
    "docs": ["architecture.md", "deployment.md", "troubleshooting.md", "setup.md"],
    "diagrams": [],
    "screenshots": [],
    "tests": [],
    "ci_cd": []
}

# Points per missing file (optional weighting)
WEIGHTS = {
    "root_files": 3,
    "terraform": 3,
    "scripts": 5,
    "lambdas": 3,
    "docs": 3,
    "diagrams": 2,
    "screenshots": 2,
    "tests": 2,
    "ci_cd": 3
}

# ==========================
# VALIDATOR FUNCTION
# ==========================
def check_files(folder, files):
    warnings = []
    for f in files:
        path = os.path.join(folder, f)
        if not os.path.exists(path):
            warnings.append(f)
    return warnings

# ==========================
# MAIN VALIDATION
# ==========================
def main():
    print("="*80)
    print("🔍 AWS ERROR DRIVEN TROUBLESHOOTING LAB VALIDATOR")
    print("="*80)
    print(f"Repository: {REPO_PATH}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    print()

    total_score = 0
    max_score = 0
    all_warnings = []

    for category, files in EXPECTED.items():
        folder = os.path.join(REPO_PATH, category) if category not in ["root_files"] else REPO_PATH
        warnings = check_files(folder, files)
        points_per_file = WEIGHTS.get(category, 2)
        total_score += points_per_file * (len(files) - len(warnings))
        max_score += points_per_file * len(files)
        if warnings:
            for w in warnings:
                all_warnings.append((category, w, points_per_file))

    percentage = (total_score / max_score) * 100 if max_score > 0 else 100

    print(f"{'SCORE':^80}")
    print("-"*80)
    print(f"  Your Score:        {total_score} / {max_score} points")
    print(f"  Percentage:        {percentage:.1f}%")
    print(f"  Warnings:          {len(all_warnings)}")
    print()
    
    if all_warnings:
        print("Warnings:")
        for category, w, pts in all_warnings:
            print(f"⚠️  [-{pts}pts] {category}/{w} missing")
    else:
        print("✅ No missing files. Repo is complete!")

    print("="*80)
    print("Validation complete.")

# ==========================
# ENTRY POINT
# ==========================
if __name__ == "__main__":
    main()
