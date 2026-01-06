import os
import re
from pathlib import Path
from prettytable import PrettyTable

# ---------------- CONFIG ----------------
AUTO_FIX = True  # True = auto-fix missing sections, False = just rate
SKIP_REPOS = ["AWS_Cloud_Scripts", "terraform"]  # repos to skip
PORTFOLIO_REPO = "charles-bucher.github.io"
PROFILE_REPO = "charles-bucher"

# ---------------- HELPER FUNCTIONS ----------------

def scan_readme(repo_path, repo_name):
    """
    Enhanced README scanner:
    - Gives up to 100% for rich lab READMEs
    - Checks for title, description, usage, diagrams, scenario walkthrough, skills, IaC mentions, monitoring/logging
    - Auto-fix: writes minimal sections if missing
    """
    readme_path = Path(repo_path) / "README.md"
    score = 0
    fixes = []

    # Portfolio/Profile repos assumed complete
    if repo_name in [PORTFOLIO_REPO, PROFILE_REPO]:
        return (100 if readme_path.exists() else 0, fixes)

    sections = {
        "title": "# Project Title\n",
        "description": "## Description\nDescription here...\n",
        "usage": "## Usage\nInstructions here...\n",
        "diagram": "![Diagram](diagram.png)\n",
        "scenario": "## Scenario Walkthrough\nDetails here...\n",
        "skills": "## Skills Demonstrated\nList skills here...\n",
        "iac": "## Infrastructure as Code\nTerraform/CloudFormation usage...\n",
        "monitoring": "## Monitoring / Operational Signals\nInclude logs/metrics...\n"
    }

    text = ""
    if readme_path.exists():
        text = readme_path.read_text(errors='ignore')

    # Track missing sections
    missing = {}
    for key, content in sections.items():
        if not re.search(re.escape(content.splitlines()[0]), text, re.I):
            missing[key] = content

    # Apply auto-fix once if needed
    if AUTO_FIX and missing:
        new_text = text.strip() + "\n\n" + "\n".join(missing.values())
        readme_path.write_text(new_text)
        fixes.extend([f"Added {key.replace('_', ' ').title()} section" for key in missing.keys()])

    # Scoring
    # Basic sections (title, description, usage, diagram)
    score += 10 if "title" not in missing else 0
    score += 10 if "description" not in missing else 0
    score += 10 if "usage" not in missing else 0
    score += 10 if "diagram" not in missing else 0

    # Advanced lab sections
    score += 20 if "scenario" not in missing else 0
    score += 20 if "skills" not in missing else 0
    score += 10 if "iac" not in missing else 0
    score += 10 if "monitoring" not in missing else 0

    return min(score, 100), fixes

def scan_code(repo_path):
    """
    Code scanner:
    - Looks for .py, .sh, .ps1 files
    - Base 30 pts for having code
    - +10 pts if any file has try/except or main guard
    """
    score = 0
    code_files = [f for f in Path(repo_path).rglob("*.*")
                  if not any(part.startswith('.') for part in f.parts) and f.suffix in ('.py', '.sh', '.ps1')]
    if code_files:
        score += 30
        for f in code_files:
            try:
                content = f.read_text(errors='ignore')
            except PermissionError:
                continue
            if "try:" in content or "except" in content or "if __name__ == '__main__':" in content:
                score += 10
                break
    return min(score, 40)

def scan_iac(repo_path):
    """
    IaC scanner:
    - Checks for Terraform/YAML/CloudFormation
    - Base 20 pts if found
    """
    score = 0
    iac_files = [f for f in Path(repo_path).rglob("*.*")
                 if not any(part.startswith('.') for part in f.parts) and f.suffix in ('.tf', '.yaml', '.yml')]
    if iac_files:
        score += 20
    return score

def scan_security(repo_path):
    """
    Security scanner:
    - Scans all files for hardcoded secrets
    - +10 pts if none found
    """
    score = 0
    code_files = [f for f in Path(repo_path).rglob("*.*") if not any(part.startswith('.') for part in f.parts)]
    insecure = False
    for f in code_files:
        try:
            content = f.read_text(errors='ignore')
        except PermissionError:
            continue
        if re.search(r'AKIA|SECRET|password|access_key', content, re.I):
            insecure = True
            break
    if not insecure:
        score += 10
    return score

# ---------------- MAIN ----------------

def main():
    REPO_BASE = Path.cwd()
    repos = [f for f in os.listdir(REPO_BASE) if Path(REPO_BASE, f).is_dir()]
    table = PrettyTable()
    table.field_names = ["Repo", "README", "Code", "IaC", "Security", "Portfolio Bonus", "Total %"]

    print("\n🔍 Cloud Portfolio Validator Results\n")

    for repo in repos:
        if repo in SKIP_REPOS:
            print(f"⏭ Skipping {repo}")
            continue

        path = Path(REPO_BASE) / repo

        readme_score, fixes = scan_readme(path, repo)
        code_score = scan_code(path)
        iac_score = scan_iac(path)
        security_score = scan_security(path)
        portfolio_bonus = 10 if repo == PORTFOLIO_REPO else 0

        total_score = readme_score + code_score + iac_score + security_score + portfolio_bonus
        total_score = min(total_score, 100)

        label = repo
        if repo == PORTFOLIO_REPO: label += " (PORTFOLIO)"
        elif repo == PROFILE_REPO: label += " (PROFILE)"

        table.add_row([
            label,
            f"{readme_score}%",
            f"{code_score}%",
            f"{iac_score}%",
            f"{security_score}%",
            f"{portfolio_bonus}%",
            f"{total_score:.1f}%"
        ])

        if fixes:
            print(f"📁 {label} - Auto-fixes applied: {', '.join(fixes)}")

    print(table)
    print("\n✅ Scan Complete\n")

if __name__ == "__main__":
    main()
