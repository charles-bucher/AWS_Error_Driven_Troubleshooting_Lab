#!/usr/bin/env python3
"""
README Validator Script - Checks for recruiter scannability and ATS optimization
Run before pushing to GitHub to ensure portfolio quality
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict

class Colors:
    """Terminal color codes"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

class READMEValidator:
    def __init__(self, readme_path: str):
        self.readme_path = Path(readme_path)
        self.content = ""
        self.score = 0
        self.max_score = 0
        self.issues = []
        self.warnings = []
        self.successes = []
        
    def load_readme(self) -> bool:
        """Load README file"""
        try:
            with open(self.readme_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
            return True
        except FileNotFoundError:
            print(f"{Colors.RED}❌ README file not found: {self.readme_path}{Colors.END}")
            return False
        except Exception as e:
            print(f"{Colors.RED}❌ Error reading README: {e}{Colors.END}")
            return False
    
    def check_6_second_scan(self) -> None:
        """Check if critical info appears in first 500 characters (6-second scan zone)"""
        print(f"\n{Colors.BOLD}📊 6-SECOND SCAN TEST{Colors.END}")
        print("─" * 60)
        
        first_500 = self.content[:500].lower()
        
        # Must-haves in first 500 chars
        critical_keywords = {
            'cloud support': 5,
            'aws': 5,
            'portfolio': 3,
            'engineer': 3,
            'troubleshooting': 4,
            'incident': 4,
        }
        
        self.max_score += 24  # Total possible from critical keywords
        
        for keyword, points in critical_keywords.items():
            if keyword in first_500:
                self.score += points
                self.successes.append(f"✅ '{keyword}' found in first 500 chars (+{points})")
            else:
                self.issues.append(f"❌ '{keyword}' NOT in first 500 chars (missed {points} points)")
        
        # Check for badges in first 200 lines
        badge_pattern = r'!\[.*?\]\(https://img\.shields\.io'
        badges_found = len(re.findall(badge_pattern, self.content[:1000]))
        
        self.max_score += 10
        if badges_found >= 3:
            self.score += 10
            self.successes.append(f"✅ Found {badges_found} badges at top (+10)")
        else:
            self.issues.append(f"❌ Only {badges_found} badges found (need 3+, missed 10 points)")
    
    def check_ats_keywords(self) -> None:
        """Check for ATS/recruiter keywords throughout document"""
        print(f"\n{Colors.BOLD}🔍 ATS KEYWORD ANALYSIS{Colors.END}")
        print("─" * 60)
        
        # High-value keywords recruiters search for
        ats_keywords = {
            # AWS Services (must have)
            'ec2': (5, 'critical'),
            's3': (5, 'critical'),
            'lambda': (5, 'critical'),
            'vpc': (4, 'critical'),
            'cloudwatch': (4, 'critical'),
            'iam': (3, 'important'),
            'rds': (3, 'important'),
            
            # Cloud Support Skills (must have)
            'troubleshooting': (6, 'critical'),
            'incident response': (6, 'critical'),
            'root cause analysis': (5, 'critical'),
            'rca': (3, 'important'),
            'mttr': (4, 'important'),
            'monitoring': (4, 'important'),
            
            # Technical Skills (must have)
            'python': (5, 'critical'),
            'boto3': (4, 'critical'),
            'linux': (3, 'important'),
            'bash': (2, 'nice'),
            
            # Soft Skills (good to have)
            'documentation': (3, 'important'),
            'technical writing': (3, 'important'),
            'cost optimization': (3, 'important'),
        }
        
        content_lower = self.content.lower()
        
        for keyword, (points, priority) in ats_keywords.items():
            count = content_lower.count(keyword)
            self.max_score += points
            
            if count >= 3:  # Keyword appears at least 3 times
                self.score += points
                self.successes.append(f"✅ '{keyword}' appears {count}x ({priority}) (+{points})")
            elif count > 0:
                partial = points // 2
                self.score += partial
                self.warnings.append(f"⚠️ '{keyword}' only {count}x ({priority}) (+{partial}/{points})")
            else:
                self.issues.append(f"❌ '{keyword}' missing ({priority}) (missed {points} points)")
    
    def check_quantifiable_metrics(self) -> None:
        """Check for numbers and metrics"""
        print(f"\n{Colors.BOLD}📈 QUANTIFIABLE METRICS{Colors.END}")
        print("─" * 60)
        
        # Look for metrics patterns
        metric_patterns = {
            r'\d+\s*(min|minutes)': ('Time metrics (MTTR)', 5),
            r'\d+\+?\s*(incidents|scenarios)': ('Incident count', 5),
            r'\$\d+': ('Cost/savings metrics', 3),
            r'\d+%': ('Percentage improvements', 3),
            r'<\s*\d+\s*min': ('Performance targets', 4),
        }
        
        for pattern, (desc, points) in metric_patterns.items():
            matches = re.findall(pattern, self.content.lower())
            self.max_score += points
            
            if matches:
                self.score += points
                self.successes.append(f"✅ {desc} found: {len(matches)} instances (+{points})")
            else:
                self.issues.append(f"❌ No {desc} (missed {points} points)")
    
    def check_structure(self) -> None:
        """Check README structure and formatting"""
        print(f"\n{Colors.BOLD}🏗️ STRUCTURE & FORMATTING{Colors.END}")
        print("─" * 60)
        
        # Must-have sections
        required_sections = {
            'skills': 5,
            'experience': 4,
            'projects': 5,
            'contact': 3,
        }
        
        content_lower = self.content.lower()
        
        for section, points in required_sections.items():
            self.max_score += points
            # Look for header patterns
            if re.search(rf'#{1,3}\s+.*{section}', content_lower) or \
               re.search(rf'\*\*.*{section}.*\*\*', content_lower):
                self.score += points
                self.successes.append(f"✅ {section.title()} section found (+{points})")
            else:
                self.issues.append(f"❌ No {section.title()} section (missed {points} points)")
        
        # Check for tables (highly scannable)
        table_pattern = r'\|[^\n]+\|'
        tables = len(re.findall(table_pattern, self.content))
        self.max_score += 10
        
        if tables >= 2:
            self.score += 10
            self.successes.append(f"✅ {tables} tables found (scannable format) (+10)")
        elif tables == 1:
            self.score += 5
            self.warnings.append(f"⚠️ Only 1 table found (add more) (+5/10)")
        else:
            self.issues.append(f"❌ No tables (use for skills/metrics) (missed 10 points)")
    
    def check_visual_elements(self) -> None:
        """Check for visual elements that improve scannability"""
        print(f"\n{Colors.BOLD}🎨 VISUAL ELEMENTS{Colors.END}")
        print("─" * 60)
        
        # Emojis for quick scanning
        emoji_pattern = r'[✅❌⚡📊🚀💼🎯📋🔧💰]'
        emojis = len(re.findall(emoji_pattern, self.content))
        self.max_score += 5
        
        if emojis >= 10:
            self.score += 5
            self.successes.append(f"✅ {emojis} emojis for visual scanning (+5)")
        else:
            self.warnings.append(f"⚠️ Only {emojis} emojis (add more for scan) (+{emojis//2}/5)")
            self.score += emojis // 2
        
        # Bold/emphasis for key terms
        bold_pattern = r'\*\*[^\*]+\*\*'
        bold_count = len(re.findall(bold_pattern, self.content))
        self.max_score += 5
        
        if bold_count >= 10:
            self.score += 5
            self.successes.append(f"✅ {bold_count} bold terms for emphasis (+5)")
        else:
            self.warnings.append(f"⚠️ Only {bold_count} bold terms (add more) (+{bold_count//2}/5)")
            self.score += bold_count // 2
        
        # Lists (bullet points)
        list_pattern = r'^[-*+]\s+.*$'
        lists = len(re.findall(list_pattern, self.content, re.MULTILINE))
        self.max_score += 5
        
        if lists >= 15:
            self.score += 5
            self.successes.append(f"✅ {lists} list items (scannable) (+5)")
        else:
            partial = min(lists // 3, 5)
            self.score += partial
            self.warnings.append(f"⚠️ Only {lists} list items (add more) (+{partial}/5)")
    
    def check_portfolio_proof(self) -> None:
        """Check for evidence of actual work"""
        print(f"\n{Colors.BOLD}📸 PORTFOLIO EVIDENCE{Colors.END}")
        print("─" * 60)
        
        # Screenshot references
        screenshot_pattern = r'!\[.*?\]\(.*?screenshot.*?\)'
        screenshots = len(re.findall(screenshot_pattern, self.content.lower()))
        self.max_score += 10
        
        if screenshots >= 5:
            self.score += 10
            self.successes.append(f"✅ {screenshots} screenshots referenced (+10)")
        elif screenshots > 0:
            partial = screenshots * 2
            self.score += partial
            self.warnings.append(f"⚠️ Only {screenshots} screenshots (need 5+) (+{partial}/10)")
        else:
            self.issues.append(f"❌ No screenshots (add visual proof) (missed 10 points)")
        
        # GitHub repository links
        github_pattern = r'github\.com/[^\s\)>]+'
        github_links = len(re.findall(github_pattern, self.content.lower()))
        self.max_score += 5
        
        if github_links >= 2:
            self.score += 5
            self.successes.append(f"✅ {github_links} GitHub links (+5)")
        else:
            self.issues.append(f"❌ Only {github_links} GitHub links (missed {5-github_links} points)")
    
    def check_readability(self) -> None:
        """Check readability metrics"""
        print(f"\n{Colors.BOLD}📖 READABILITY{Colors.END}")
        print("─" * 60)
        
        # Paragraph length (shouldn't be walls of text)
        paragraphs = self.content.split('\n\n')
        long_paragraphs = [p for p in paragraphs if len(p) > 500]
        
        self.max_score += 5
        if len(long_paragraphs) <= 2:
            self.score += 5
            self.successes.append(f"✅ Good paragraph length (scannable) (+5)")
        else:
            self.warnings.append(f"⚠️ {len(long_paragraphs)} long paragraphs (break them up)")
            self.score += 2
        
        # README length (not too short, not too long)
        word_count = len(self.content.split())
        self.max_score += 5
        
        if 1500 <= word_count <= 4000:
            self.score += 5
            self.successes.append(f"✅ Good length: {word_count} words (+5)")
        elif word_count < 1500:
            self.warnings.append(f"⚠️ Too short: {word_count} words (add more detail)")
            self.score += 2
        else:
            self.warnings.append(f"⚠️ Too long: {word_count} words (consider collapsible sections)")
            self.score += 3
    
    def check_contact_info(self) -> None:
        """Check for contact/hiring information"""
        print(f"\n{Colors.BOLD}📞 CONTACT & HIRING INFO{Colors.END}")
        print("─" * 60)
        
        content_lower = self.content.lower()
        
        # Contact elements
        contact_items = {
            'github': 3,
            'linkedin': 3,
            'email': 2,
            'location': 2,
        }
        
        for item, points in contact_items.items():
            self.max_score += points
            if item in content_lower:
                self.score += points
                self.successes.append(f"✅ {item.title()} mentioned (+{points})")
            else:
                self.issues.append(f"❌ No {item.title()} info (missed {points} points)")
        
        # Job-seeking indicators
        job_seeking_terms = ['seeking', 'looking for', 'open to', 'remote']
        self.max_score += 5
        
        found_terms = [term for term in job_seeking_terms if term in content_lower]
        if len(found_terms) >= 2:
            self.score += 5
            self.successes.append(f"✅ Job-seeking intent clear ({len(found_terms)} terms) (+5)")
        else:
            self.warnings.append(f"⚠️ Job intent unclear (add 'seeking roles' section)")
            self.score += 2
    
    def generate_report(self) -> None:
        """Generate final validation report"""
        print(f"\n{Colors.BOLD}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}{'VALIDATION REPORT':^60}{Colors.END}")
        print(f"{Colors.BOLD}{'='*60}{Colors.END}\n")
        
        # Calculate percentage
        percentage = (self.score / self.max_score * 100) if self.max_score > 0 else 0
        
        # Determine grade
        if percentage >= 90:
            grade = "A+"
            grade_color = Colors.GREEN
            status = "🏆 EXCELLENT - Ready to push!"
        elif percentage >= 80:
            grade = "A"
            grade_color = Colors.GREEN
            status = "✅ GOOD - Minor improvements suggested"
        elif percentage >= 70:
            grade = "B"
            grade_color = Colors.YELLOW
            status = "⚠️ FAIR - Fix issues before pushing"
        elif percentage >= 60:
            grade = "C"
            grade_color = Colors.YELLOW
            status = "⚠️ NEEDS WORK - Major improvements needed"
        else:
            grade = "F"
            grade_color = Colors.RED
            status = "❌ FAILING - Do not push yet"
        
        print(f"{Colors.BOLD}Score:{Colors.END} {grade_color}{self.score}/{self.max_score} ({percentage:.1f}%){Colors.END}")
        print(f"{Colors.BOLD}Grade:{Colors.END} {grade_color}{grade}{Colors.END}")
        print(f"{Colors.BOLD}Status:{Colors.END} {status}\n")
        
        # Summary counts
        print(f"{Colors.GREEN}✅ Successes:{Colors.END} {len(self.successes)}")
        print(f"{Colors.YELLOW}⚠️  Warnings:{Colors.END} {len(self.warnings)}")
        print(f"{Colors.RED}❌ Issues:{Colors.END} {len(self.issues)}\n")
        
        # Detailed feedback
        if self.issues:
            print(f"{Colors.RED}{Colors.BOLD}CRITICAL ISSUES (Fix These):{Colors.END}")
            for issue in self.issues[:10]:  # Show top 10
                print(f"  {issue}")
            if len(self.issues) > 10:
                print(f"  ... and {len(self.issues) - 10} more issues")
            print()
        
        if self.warnings:
            print(f"{Colors.YELLOW}{Colors.BOLD}WARNINGS (Improve These):{Colors.END}")
            for warning in self.warnings[:5]:  # Show top 5
                print(f"  {warning}")
            if len(self.warnings) > 5:
                print(f"  ... and {len(self.warnings) - 5} more warnings")
            print()
        
        # Recommendations
        print(f"{Colors.BOLD}💡 TOP RECOMMENDATIONS:{Colors.END}")
        if percentage < 70:
            print("  1. Add more AWS service keywords (EC2, S3, Lambda, VPC)")
            print("  2. Include quantifiable metrics (MTTR, incident count, costs)")
            print("  3. Add tables for skills and performance metrics")
            print("  4. Include screenshots/evidence of work")
            print("  5. Add contact information and job-seeking intent")
        elif percentage < 90:
            print("  1. Add a few more visual elements (emojis, bold text)")
            print("  2. Include more screenshots for portfolio proof")
            print("  3. Ensure all critical keywords appear 3+ times")
        else:
            print("  1. README looks excellent!")
            print("  2. Minor tweaks suggested above (if any)")
            print("  3. Ready to push to GitHub")
        
        print(f"\n{Colors.BOLD}{'='*60}{Colors.END}\n")
        
        # Return exit code
        return 0 if percentage >= 70 else 1
    
    def run_validation(self) -> int:
        """Run all validation checks"""
        print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.BLUE}{'README VALIDATOR FOR RECRUITERS':^60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")
        print(f"File: {self.readme_path}\n")
        
        if not self.load_readme():
            return 1
        
        # Run all checks
        self.check_6_second_scan()
        self.check_ats_keywords()
        self.check_quantifiable_metrics()
        self.check_structure()
        self.check_visual_elements()
        self.check_portfolio_proof()
        self.check_readability()
        self.check_contact_info()
        
        # Generate report
        return self.generate_report()


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Validate README for recruiter scannability and ATS optimization"
    )
    parser.add_argument(
        'readme_path',
        nargs='?',
        default='README.md',
        help='Path to README file (default: README.md)'
    )
    
    args = parser.parse_args()
    
    validator = READMEValidator(args.readme_path)
    exit_code = validator.run_validation()
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
