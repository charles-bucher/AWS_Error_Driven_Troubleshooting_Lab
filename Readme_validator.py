import os
import re

# Repo root
REPO_PATH = "."

# Expected incident structure
EXPECTED_SCRIPTS = ["deploy.py", "break.py", "collect_evidence.py", "teardown.py"]
EXPECTED_EVIDENCE_SUBDIRS = ["screenshots", "logs", "metrics"]

# Keywords for README checks
KEYWORDS = ["EC2", "S3", "Lambda", "VPC", "CloudWatch", "IAM", "troubleshoot", "incident", "root cause"]

def check_readme(path):
    score = 0
    hints = []
    if not os.path.exists(path):
        return 0, ["README.md missing"]

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Section checks
    sections = ["Quick Start", "Incident Scenarios", "Evidence", "Metrics", "Skills Mapped"]
    for sec in sections:
        if sec in content:
            score += 5
        else:
            hints.append(f"Missing section: {sec}")

    # Keyword checks
    found_keywords = sum(1 for kw in KEYWORDS if kw in content)
    score += min(found_keywords, 10)  # cap contribution
    if found_keywords < len(KEYWORDS):
        missing = [kw for kw in KEYWORDS if kw not in content]
        hints.append(f"Missing keywords in README: {missing}")

    return min(score, 25), hints

def check_incident_structure(incident_path):
    score = 0
    hints = []

    # Check scripts
    scripts_path = os.path.join(incident_path, "scripts")
    if os.path.exists(scripts_path):
        scripts = os.listdir(scripts_path)
        for s in EXPECTED_SCRIPTS:
            if s in scripts:
                score += 2
            else:
                hints.append(f"Missing script: {s}")
    else:
        hints.append("Scripts folder missing")

    # Check evidence
    evidence_path = os.path.join(incident_path, "evidence")
    if os.path.exists(evidence_path):
        for sub in EXPECTED_EVIDENCE_SUBDIRS:
            if os.path.exists(os.path.join(evidence_path, sub)):
                score += 2
            else:
                hints.append(f"Missing evidence subfolder: {sub}")
    else:
        hints.append("Evidence folder missing")

    # Check incident README
    incident_readme = os.path.join(incident_path, "README.md")
    r_score, r_hints = check_readme(incident_readme)
    score += r_score
    hints.extend(r_hints)

    return score, hints

def validate_repo(repo_path):
    total_score = 0
    total_possible = 0
    all_hints = []

    # Main README
    r_score, r_hints = check_readme(os.path.join(repo_path, "README.md"))
    total_score += r_score
    total_possible += 25
    all_hints.extend(r_hints)

    # Incidents
    incidents = [d for d in os.listdir(os.path.join(repo_path, "incidents")) if os.path.isdir(os.path.join(repo_path, "incidents", d))]
    for incident in incidents:
        i_score, i_hints = check_incident_structure(os.path.join(repo_path, "incidents", incident))
        total_score += i_score
        total_possible += 25
        all_hints.extend([f"{incident}: {h}" for h in i_hints])

    readiness_percent = (total_score / total_possible) * 100
    return readiness_percent, all_hints

if __name__ == "__main__":
    score, hints = validate_repo(REPO_PATH)
    print(f"\nEntry-Level Cloud Readiness Score: {score:.1f}%")
    print("\nFix Suggestions:")
    for h in hints:
        print(f"- {h}")
