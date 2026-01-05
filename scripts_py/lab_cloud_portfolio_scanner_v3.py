#!/usr/bin/env python3
"""
Cloud Portfolio Scanner - Profile & Portfolio Aware Version
Scans GitHub repos for cloud content, documentation quality, README completeness,
and provides Job & Certification alignment scores, treating profile and portfolio separately.
"""

import os
import json
import re
from datetime import datetime

# =============================
# CONFIG
# =============================
REPOS_ROOT = os.getcwd()

IGNORE_NAMES = {
    "AWS Cloud Scripts",
    "CloudSnippets",
    "cloud_portfolio_report.json",
    "cloud_portfolio_report",
    ".git",
    ".github",
    "node_modules",
    "__pycache__",
    "venv",
    ".venv"
}

AWS_KEYWORDS = {
    "aws", "ec2", "s3", "lambda", "iam", "cloudwatch",
    "terraform", "cdk", "boto3", "vpc", "rds",
    "autoscaling", "cloudformation", "dynamodb", "sns",
    "sqs", "elasticache", "route53", "elb", "alb"
}

JOB_KEYWORDS = {
    "automation", "monitoring", "incident", "troubleshoot", "ci/cd",
    "pipeline", "lambda", "cloudwatch", "s3", "ec2", "vpc", "rds", "sns", "sqs"
}

REQUIRED_README_SECTIONS = [
    "Overview",
    "Architecture",
    "Features",
    "Setup",
    "Usage",
    "Skills Demonstrated",
    "License"
]

REPORT_PATH = os.path.join(REPOS_ROOT, "cloud_portfolio_report.json")

# =============================
# ANSI COLORS
# =============================
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# =============================
# HELPERS
# =============================
def safe_read(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception:
        return ""

def detect_repo_type(repo_name):
    # Explicitly handle profile and portfolio
    if repo_name == "charles-bucher":
        return "profile-repo"
    if repo_name.endswith(".github.io"):
        return "portfolio-site"
    repo_lower = repo_name.lower()
    if "lab" in repo_lower or "sim" in repo_lower:
        return "training-lab"
    if "tool" in repo_lower or "optimizer" in repo_lower:
        return "automation-tool"
    return "cloud-project"

def score_readme(readme_text):
    if not readme_text:
        return 0.0, REQUIRED_README_SECTIONS.copy()
    found = []
    for section in REQUIRED_README_SECTIONS:
        patterns = [rf"#+\s*{re.escape(section)}", rf"\b{re.escape(section)}\b"]
        if any(re.search(p, readme_text, re.I) for p in patterns):
            found.append(section)
    score = round((len(found)/len(REQUIRED_README_SECTIONS))*100, 1)
    missing = [s for s in REQUIRED_README_SECTIONS if s not in found]
    return score, missing

def score_cloud_relevance(text):
    if not text:
        return 0.0
    text_lower = text.lower()
    hits = sum(1 for kw in AWS_KEYWORDS if kw in text_lower)
    total_mentions = sum(text_lower.count(kw) for kw in AWS_KEYWORDS)
    unique_score = (hits / len(AWS_KEYWORDS)) * 70
    frequency_bonus = min((total_mentions / 50) * 30, 30)
    return round(unique_score + frequency_bonus, 1)

def score_job_alignment(text):
    if not text:
        return 0.0
    text_lower = text.lower()
    hits = sum(1 for kw in JOB_KEYWORDS if kw in text_lower)
    total_mentions = sum(text_lower.count(kw) for kw in JOB_KEYWORDS)
    unique_score = (hits / len(JOB_KEYWORDS)) * 70
    frequency_bonus = min((total_mentions / 50) * 30, 30)
    return round(unique_score + frequency_bonus, 1)

def score_documentation(repo_path):
    total_files, documented = 0, 0
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_NAMES]
        for f in files:
            if f.endswith((".py", ".sh", ".ps1", ".js", ".ts")):
                total_files += 1
                content = safe_read(os.path.join(root, f))
                has_docstring = '"""' in content or "'''" in content
                has_comments = content.count("#") > 2 or content.count("//") > 2
                has_jsdoc = "/**" in content
                if has_docstring or has_comments or has_jsdoc:
                    documented += 1
    if total_files == 0:
        return 100.0
    return round((documented / total_files) * 100, 1)

def count_files_by_type(repo_path):
    counts = {"Python":0,"Shell":0,"Terraform":0,"YAML":0,"Markdown":0,"JavaScript":0,"Other":0}
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_NAMES]
        for f in files:
            if f.endswith(".py"): counts["Python"] += 1
            elif f.endswith((".sh",".bash")): counts["Shell"] += 1
            elif f.endswith((".tf",".tfvars")): counts["Terraform"] += 1
            elif f.endswith((".yml",".yaml")): counts["YAML"] += 1
            elif f.endswith(".md"): counts["Markdown"] += 1
            elif f.endswith((".js",".jsx",".ts",".tsx")): counts["JavaScript"] += 1
            else: counts["Other"] += 1
    return {k:v for k,v in counts.items() if v>0}

def auto_fix_empty_files(repo_path):
    fixes = []
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_NAMES]
        for f in files:
            full = os.path.join(root, f)
            if f.endswith((".py", ".sh", ".ps1")) and os.path.getsize(full) == 0:
                try:
                    with open(full, "w") as w:
                        w.write('"""\nPlaceholder file\n"""\n' if f.endswith(".py") else "# Placeholder file\n")
                    fixes.append(f)
                except: pass
    return fixes

def get_readme_stats(readme_text):
    if not readme_text: return {"lines":0,"words":0,"chars":0,"has_badges":False,"has_toc":False}
    return {
        "lines": readme_text.count('\n'),
        "words": len(readme_text.split()),
        "chars": len(readme_text),
        "has_badges": bool(re.search(r'!\[.*?\]\(.*?badge.*?\)', readme_text,re.I)),
        "has_toc": bool(re.search(r'table of contents|toc', readme_text,re.I))
    }

# =============================
# SCAN REPO
# =============================
def scan_repository(repo_path, repo_name):
    readme_path = os.path.join(repo_path, "README.md")
    readme_text = safe_read(readme_path)
    repo_type = detect_repo_type(repo_name)
    
    readme_score, missing_sections = score_readme(readme_text)
    cloud_score = score_cloud_relevance(readme_text)
    job_score = score_job_alignment(readme_text)
    doc_score = score_documentation(repo_path)
    fixes = auto_fix_empty_files(repo_path)
    file_counts = count_files_by_type(repo_path)
    readme_stats = get_readme_stats(readme_text)
    
    # Adjust scoring weights for profile and portfolio
    if repo_type == "profile-repo":
        total_score = round((job_score*0.35)+(cloud_score*0.35)+(readme_score*0.25)+(doc_score*0.05), 1)
    elif repo_type == "portfolio-site":
        total_score = round((job_score*0.25)+(cloud_score*0.35)+(readme_score*0.25)+(doc_score*0.15), 1)
    else:
        total_score = round((job_score*0.35)+(cloud_score*0.35)+(readme_score*0.15)+(doc_score*0.15), 1)
    
    suggestions = []
    for sec in missing_sections: suggestions.append(f"Add README section: {sec}")
    if cloud_score < 50: suggestions.append("Increase AWS/cloud keywords and examples")
    if job_score < 50: suggestions.append("Highlight practical skills relevant to CloudOps/DevOps jobs")
    if doc_score < 70: suggestions.append("Add more inline comments and docstrings")
    if readme_stats["words"] < 100: suggestions.append("Expand README with more details")
    if not readme_stats["has_badges"]: suggestions.append("Consider adding status badges")
    for f in fixes: suggestions.append(f"Auto-filled empty file: {f}")
    
    return {
        "Type": repo_type,
        "README Score": readme_score,
        "Cloud (Cert) Score": cloud_score,
        "Job Alignment Score": job_score,
        "Documentation Score": doc_score,
        "TOTAL SCORE": total_score,
        "Suggestions": suggestions if suggestions else ["No suggestions - repo looks solid!"],
        "File Counts": file_counts,
        "README Stats": readme_stats
    }

# =============================
# MAIN
# =============================
def main():
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}")
    print("🚀 Cloud Portfolio Scanner v3.1")
    print(f"{'='*60}{Colors.ENDC}")
    print(f"Scanning directory: {Colors.OKCYAN}{REPOS_ROOT}{Colors.ENDC}\n")
    
    results = {}
    scanned_count, skipped_count = 0, 0
    
    for item in os.listdir(REPOS_ROOT):
        if item in IGNORE_NAMES or item.startswith("."):
            print(f"{Colors.WARNING}[SKIP] {item}{Colors.ENDC}")
            skipped_count += 1
            continue
        repo_path = os.path.join(REPOS_ROOT, item)
        if not os.path.isdir(repo_path): continue
        
        scanned_count += 1
        print(f"\n{Colors.OKBLUE}{'='*60}")
        print(f"📂 Scanning: {Colors.BOLD}{item}{Colors.ENDC}")
        print(f"{Colors.OKBLUE}{'='*60}{Colors.ENDC}")
        
        result = scan_repository(repo_path, item)
        results[item] = result
        
        print(f"{Colors.OKCYAN}Type:{Colors.ENDC} {result['Type']}")
        print(f"{Colors.OKCYAN}README Score:{Colors.ENDC} {result['README Score']}%")
        print(f"{Colors.OKCYAN}Cloud (Cert) Score:{Colors.ENDC} {result['Cloud (Cert) Score']}%")
        print(f"{Colors.OKCYAN}Job Alignment Score:{Colors.ENDC} {result['Job Alignment Score']}%")
        print(f"{Colors.OKCYAN}Documentation Score:{Colors.ENDC} {result['Documentation Score']}%")
        
        score = result['TOTAL SCORE']
        if score >= 90: score_color = Colors.OKGREEN
        elif score >= 70: score_color = Colors.OKCYAN
        elif score >= 50: score_color = Colors.WARNING
        else: score_color = Colors.FAIL
        print(f"{Colors.BOLD}TOTAL SCORE: {score_color}{score}%{Colors.ENDC}")
        
        if result['File Counts']:
            print(f"\n{Colors.OKCYAN}📊 File Breakdown:{Colors.ENDC}")
            for ftype, count in result['File Counts'].items():
                print(f"  • {ftype}: {count}")
        
        if result['Suggestions']:
            print(f"\n{Colors.WARNING}💡 Suggestions:{Colors.ENDC}")
            for s in result['Suggestions']:
                if "solid" in s.lower(): print(f"  {Colors.OKGREEN}✅ {s}{Colors.ENDC}")
                else: print(f"  • {s}")
    
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}")
    print("📊 SCAN SUMMARY")
    print(f"{'='*60}{Colors.ENDC}")
    print(f"Total Repos Scanned: {Colors.OKGREEN}{scanned_count}{Colors.ENDC}")
    print(f"Total Repos Skipped: {Colors.WARNING}{skipped_count}{Colors.ENDC}")
    
    if results:
        sorted_repos = sorted(results.items(), key=lambda x:x[1]["TOTAL SCORE"], reverse=True)
        top = sorted_repos[0]
        print(f"\n{Colors.OKGREEN}🏆 Top Performing Repo:{Colors.ENDC}")
        print(f"  {Colors.BOLD}{top[0]}{Colors.ENDC} - {Colors.OKGREEN}{top[1]['TOTAL SCORE']}%{Colors.ENDC}")
        if len(sorted_repos) > 1:
            bottom = sorted_repos[-1]
            print(f"\n{Colors.WARNING}📈 Needs Improvement:{Colors.ENDC}")
            print(f"  {Colors.BOLD}{bottom[0]}{Colors.ENDC} - {Colors.WARNING}{bottom[1]['TOTAL SCORE']}%{Colors.ENDC}")
        avg_score = round(sum(r["TOTAL SCORE"] for r in results.values())/len(results),1)
        print(f"\n{Colors.OKCYAN}📊 Portfolio Average:{Colors.ENDC} {avg_score}%")
    
    print(f"{Colors.HEADER}{'='*60}{Colors.ENDC}")
    
    report = {
        "scan_date": datetime.now().isoformat(),
        "scan_location": REPOS_ROOT,
        "repos_scanned": scanned_count,
        "repos_skipped": skipped_count,
        "results": results
    }
    
    with open(REPORT_PATH, "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"\n{Colors.OKGREEN}✅ Full report saved to:{Colors.ENDC} {REPORT_PATH}\n")

if __name__ == "__main__":
    main()
