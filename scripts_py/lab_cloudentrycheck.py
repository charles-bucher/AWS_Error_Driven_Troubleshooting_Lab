#!/usr/bin/env python3
"""
Repo & portfolio scanner for Charles Bucher

Usage:
    python repo_portfolio_scanner.py

Configure the paths and project expectations in REPOS_CONFIG and PROJECT_REFERENCES.
"""

import os
import re
import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime, timedelta

import requests

# --------------- CONFIGURATION ---------------

# Paths to your local clones
REPOS_CONFIG = {
    "profile": {
        "name": "GitHub Profile Repo",
        "path": Path(r"./charles-bucher"),  # adjust if needed
    },
    "portfolio": {
        "name": "Portfolio Site Repo",
        "path": Path(r"./charles-bucher.github.io"),  # adjust if needed
    },
}

# Words/phrases that signal "unfinished"
TODO_PATTERNS = [
    r"\bTODO\b",
    r"content to be added",
    r"\bTBD\b",
    r"fill this in later",
]

# Maximum age before a "Last Updated" is considered stale
STALE_MONTHS = 4

# Simple map of project names you *expect* to exist and be referenced
PROJECT_REFERENCES = {
    "AWS_Cloud_Support_Sim": {
        "required": True,
        "expect_in_portfolio": True,
    },
    "AWS_Error_Driven_Troubleshooting_Lab": {
        "required": True,
        "expect_in_portfolio": True,
    },
    "CloudOpsLab": {
        "required": True,
        "expect_in_portfolio": True,
    },
    "Security-Compliance-Guardrail-Lab": {
        "required": False,  # set True if you want to enforce
        "expect_in_portfolio": True,
    },
}

# --------------- UTILITIES ---------------

def print_header(title: str):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80 + "\n")


def find_markdown_files(repo_path: Path):
    return list(repo_path.rglob("*.md"))


def read_text(path: Path):
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="latin-1")
    except Exception as e:
        print(f"[WARN] Could not read {path}: {e}")
        return ""


def collect_links_from_text(text: str):
    # Simple regex for http/https URLs in markdown
    url_pattern = re.compile(r"https?://[^\s)>\]]+")
    return url_pattern.findall(text)


def http_check(url: str, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code
    except requests.RequestException:
        return None


def parse_last_updated(text: str):
    """
    Looks for lines like:
    Last Updated: 2024-10-15
    or
    Last Updated: October 15, 2024
    """
    pattern = re.compile(r"Last Updated:\s*(.+)", re.IGNORECASE)
    match = pattern.search(text)
    if not match:
        return None

    raw = match.group(1).strip()

    # Try a couple of formats
    for fmt in ("%Y-%m-%d", "%B %d, %Y", "%b %d, %Y"):
        try:
            return datetime.strptime(raw, fmt)
        except ValueError:
            continue

    return None


def months_ago(dt: datetime):
    now = datetime.utcnow()
    delta = now - dt
    # approximate months
    return delta.days / 30.0


def find_patterns(text: str, patterns):
    hits = []
    for pat in patterns:
        for m in re.finditer(pat, text, flags=re.IGNORECASE):
            hits.append((pat, m.group(0)))
    return hits


def find_project_mentions(text: str, project_names):
    found = set()
    for proj in project_names:
        if re.search(rf"\b{re.escape(proj)}\b", text):
            found.add(proj)
    return found


# --------------- SCAN FUNCTIONS ---------------

def scan_for_todos(md_files):
    results = []
    for md in md_files:
        text = read_text(md)
        hits = find_patterns(text, TODO_PATTERNS)
        for pattern, fragment in hits:
            # grab a small context
            line_no = text.count("\n", 0, text.find(fragment)) + 1
            results.append({
                "file": str(md),
                "pattern": pattern,
                "fragment": fragment,
                "line": line_no,
            })
    return results


def scan_for_broken_links(md_files):
    all_links = set()
    for md in md_files:
        text = read_text(md)
        links = collect_links_from_text(text)
        all_links.update(links)

    broken = []
    if not all_links:
        return broken

    print_header("Checking external links (this may take a bit)...")
    for url in sorted(all_links):
        status = http_check(url)
        if status is None or status >= 400:
            broken.append({
                "url": url,
                "status": status,
            })
            print(f"[BROKEN] {url} (status={status})")
        else:
            print(f"[OK] {url} (status={status})")
        time.sleep(0.2)  # be polite

    return broken


def scan_last_updated(md_files):
    # We only care about top-level README files for "Last Updated"
    stale = []
    checked = []
    for md in md_files:
        if md.name.lower() != "readme.md":
            continue
        text = read_text(md)
        dt = parse_last_updated(text)
        if dt is None:
            continue
        age_months = months_ago(dt)
        checked.append({"file": str(md), "date": dt.isoformat(), "age_months": age_months})
        if age_months > STALE_MONTHS:
            stale.append({
                "file": str(md),
                "date": dt.isoformat(),
                "age_months": age_months,
            })
    return checked, stale


def scan_project_references(portfolio_repo: Path):
    """
    Check that:
    - Expected project repos exist (under same parent as portfolio/profile).
    - Portfolio README mentions required projects.
    """
    parent = portfolio_repo.parent
    portfolio_readme = portfolio_repo / "README.md"

    existing_repos = {}
    for proj in PROJECT_REFERENCES.keys():
        path = parent / proj
        existing_repos[proj] = path.exists()

    missing_required = [
        proj for proj, meta in PROJECT_REFERENCES.items()
        if meta.get("required", False) and not existing_repos.get(proj, False)
    ]

    missing_in_portfolio = []
    if portfolio_readme.exists():
        text = read_text(portfolio_readme)
        mentioned = find_project_mentions(text, PROJECT_REFERENCES.keys())
        for proj, meta in PROJECT_REFERENCES.items():
            if meta.get("expect_in_portfolio", False) and proj not in mentioned:
                missing_in_portfolio.append(proj)
    else:
        print(f"[WARN] Portfolio README not found at {portfolio_readme}")

    return {
        "existing_repos": existing_repos,
        "missing_required": missing_required,
        "missing_in_portfolio": missing_in_portfolio,
    }


def scan_repo(repo_key: str, repo_conf: dict):
    repo_name = repo_conf["name"]
    repo_path = repo_conf["path"]

    print_header(f"Scanning: {repo_name} ({repo_path})")

    if not repo_path.exists():
        print(f"[ERROR] Path does not exist: {repo_path}")
        return {
            "repo": repo_key,
            "path_exists": False,
        }

    md_files = find_markdown_files(repo_path)
    print(f"[INFO] Found {len(md_files)} markdown files.")

    todos = scan_for_todos(md_files)
    checked_dates, stale_dates = scan_last_updated(md_files)

    return {
        "repo": repo_key,
        "path_exists": True,
        "markdown_files": len(md_files),
        "todos": todos,
        "checked_dates": checked_dates,
        "stale_dates": stale_dates,
    }


# --------------- MAIN ---------------

def main():
    parser = argparse.ArgumentParser(description="Scan Charles's GitHub profile + portfolio repos.")
    parser.add_argument(
        "--skip-links",
        action="store_true",
        help="Skip external link checking (faster, no HTTP requests).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON summary at the end.",
    )
    args = parser.parse_args()

    all_results = {}

    # Scan both repos for TODOs and Last Updated
    for key, conf in REPOS_CONFIG.items():
        res = scan_repo(key, conf)
        all_results[key] = res

    # Scan portfolio-specific details
    portfolio_conf = REPOS_CONFIG["portfolio"]
    portfolio_path = portfolio_conf["path"]

    proj_ref_results = scan_project_references(portfolio_path)
    all_results["project_references"] = proj_ref_results

    # External links: scan across both repos
    if not args.skip_links:
        all_md_files = []
        for conf in REPOS_CONFIG.values():
            if conf["path"].exists():
                all_md_files.extend(find_markdown_files(conf["path"]))
        broken_links = scan_for_broken_links(all_md_files)
        all_results["broken_links"] = broken_links
    else:
        all_results["broken_links"] = []

    # Human-readable summary
    print_header("SUMMARY")

    for key, res in all_results.items():
        if key in ("project_references", "broken_links"):
            continue

        if not res.get("path_exists", False):
            print(f"- {key}: PATH MISSING ({REPOS_CONFIG[key]['path']})")
            continue

        print(f"- {key}: {res['markdown_files']} markdown files")
        print(f"  - TODO-like markers: {len(res['todos'])}")
        if res["todos"]:
            for t in res["todos"][:5]:
                print(f"    * {t['file']} (line {t['line']}): {t['fragment']}")
            if len(res["todos"]) > 5:
                print(f"    ... and {len(res['todos']) - 5} more")

        print(f"  - README 'Last Updated' entries checked: {len(res['checked_dates'])}")
        print(f"  - Stale (> {STALE_MONTHS} months): {len(res['stale_dates'])}")
        for s in res["stale_dates"]:
            print(f"    * {s['file']} -> {s['date']} (~{s['age_months']:.1f} months ago)")

    # Project references summary
    pr = all_results["project_references"]
    print("\nProject references:")
    for proj, exists in pr["existing_repos"].items():
        print(f"  - {proj}: {'FOUND' if exists else 'MISSING'} (required={PROJECT_REFERENCES[proj]['required']})")
    if pr["missing_required"]:
        print("  [!] Missing required repos:", ", ".join(pr["missing_required"]))
    if pr["missing_in_portfolio"]:
        print("  [!] Not mentioned in portfolio README:", ", ".join(pr["missing_in_portfolio"]))

    # Broken links summary
    broken_links = all_results["broken_links"]
    print(f"\nExternal link check: {len(broken_links)} broken/failed links.")
    for bl in broken_links[:10]:
        print(f"  - {bl['url']} (status={bl['status']})")
    if len(broken_links) > 10:
        print(f"    ... and {len(broken_links) - 10} more")

    # JSON output (optional)
    if args.json:
        print_header("JSON OUTPUT")
        print(json.dumps(all_results, indent=2, default=str))


if __name__ == "__main__":
    main()