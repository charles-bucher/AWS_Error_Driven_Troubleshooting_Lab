#!/usr/bin/env python3
"""
README Validator for AWS Error-Driven Troubleshooting Lab
Checks for broken links, missing screenshots, formatting issues, and completeness.
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict

class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

class ReadmeValidator:
    def __init__(self, readme_path: str, repo_root: str = None):
        self.readme_path = Path(readme_path)
        self.repo_root = Path(repo_root) if repo_root else self.readme_path.parent
        self.errors = []
        self.warnings = []
        self.info = []
        
        # Read README content
        with open(self.readme_path, 'r', encoding='utf-8') as f:
            self.content = f.read()
    
    def validate_all(self) -> bool:
        """Run all validation checks"""
        print(f"{Colors.BOLD}{Colors.BLUE}🔍 Validating README.md...{Colors.END}\n")
        
        self.check_required_sections()
        self.check_image_links()
        self.check_badges()
        self.check_code_blocks()
        self.check_incident_table()
        self.check_file_structure()
        self.check_broken_links()
        self.check_formatting()
        
        return self.print_results()
    
    def check_required_sections(self):
        """Check for required README sections"""
        required_sections = [
            'TL;DR',
            'Quick Start',
            'Incident Scenarios',
            'Installation',
            'Skills',
            'License',
            'Contact'
        ]
        
        for section in required_sections:
            if section.lower() not in self.content.lower():
                self.warnings.append(f"Missing recommended section: '{section}'")
            else:
                self.info.append(f"✓ Found section: '{section}'")
    
    def check_image_links(self):
        """Validate all image links and check if files exist"""
        # Pattern to match markdown images: ![alt](path)
        image_pattern = r'!\[([^\]]*)\]\(([^\)]+)\)'
        images = re.findall(image_pattern, self.content)
        
        if not images:
            self.warnings.append("No images found in README")
            return
        
        self.info.append(f"Found {len(images)} image references")
        
        for alt_text, img_path in images:
            # Skip external URLs
            if img_path.startswith(('http://', 'https://')):
                continue
            
            # Check if file exists
            full_path = self.repo_root / img_path
            if not full_path.exists():
                self.errors.append(f"Image not found: {img_path}")
            else:
                self.info.append(f"✓ Image exists: {img_path}")
            
            # Check if alt text is present
            if not alt_text or alt_text.strip() == '':
                self.warnings.append(f"Missing alt text for image: {img_path}")
    
    def check_badges(self):
        """Check for badges in README"""
        badge_pattern = r'\[!\[([^\]]+)\]\(([^\)]+)\)\]\(([^\)]+)\)'
        badges = re.findall(badge_pattern, self.content)
        
        if badges:
            self.info.append(f"✓ Found {len(badges)} badges")
        else:
            self.warnings.append("No badges found - consider adding status badges")
    
    def check_code_blocks(self):
        """Validate code blocks are properly formatted"""
        # Check for code blocks
        code_block_pattern = r'```[\s\S]*?```'
        code_blocks = re.findall(code_block_pattern, self.content)
        
        if code_blocks:
            self.info.append(f"✓ Found {len(code_blocks)} code blocks")
            
            # Check for language specification
            for block in code_blocks:
                first_line = block.split('\n')[0]
                if first_line == '```':
                    self.warnings.append("Code block without language specification")
        
        # Check for inline code
        inline_code_pattern = r'`[^`]+`'
        inline_codes = re.findall(inline_code_pattern, self.content)
        if inline_codes:
            self.info.append(f"✓ Found {len(inline_codes)} inline code snippets")
    
    def check_incident_table(self):
        """Check incident scenarios table"""
        # Look for table with incident information
        table_pattern = r'\|\s*ID\s*\|.*?\n\|[-:\s|]+\n((?:\|.*?\n)+)'
        tables = re.findall(table_pattern, self.content, re.MULTILINE)
        
        if not tables:
            self.errors.append("Incident scenarios table not found")
            return
        
        self.info.append("✓ Found incident scenarios table")
        
        # Count rows in table
        rows = tables[0].strip().split('\n')
        incident_count = len(rows)
        self.info.append(f"✓ Table contains {incident_count} incidents")
        
        # Check for required columns
        required_columns = ['ID', 'Incident', 'Services', 'Difficulty', 'Status']
        header_line = self.content.split('Incident Scenarios')[1].split('\n')[1]
        
        for column in required_columns:
            if column.lower() not in header_line.lower():
                self.warnings.append(f"Missing column in incident table: '{column}'")
    
    def check_file_structure(self):
        """Check if mentioned file structure exists"""
        # Look for incidents directory
        incidents_dir = self.repo_root / 'incidents'
        
        if not incidents_dir.exists():
            self.warnings.append("'incidents' directory not found in repo root")
            return
        
        self.info.append("✓ Found 'incidents' directory")
        
        # Check for incident folders
        incident_folders = [d for d in incidents_dir.iterdir() if d.is_dir()]
        self.info.append(f"✓ Found {len(incident_folders)} incident folders")
        
        # Check each incident folder for screenshots
        for folder in incident_folders:
            screenshot_dirs = [d for d in folder.iterdir() if 'screenshot' in d.name.lower()]
            if not screenshot_dirs:
                self.warnings.append(f"No screenshot directory in {folder.name}")
    
    def check_broken_links(self):
        """Check for broken internal links"""
        # Pattern to match markdown links: [text](url)
        link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
        links = re.findall(link_pattern, self.content)
        
        internal_links = [link for _, link in links if not link.startswith(('http://', 'https://', '#', 'mailto:'))]
        
        for link in internal_links:
            full_path = self.repo_root / link
            if not full_path.exists():
                self.errors.append(f"Broken link: {link}")
    
    def check_formatting(self):
        """Check for common formatting issues"""
        lines = self.content.split('\n')
        
        # Check for excessive blank lines
        blank_count = 0
        for i, line in enumerate(lines):
            if line.strip() == '':
                blank_count += 1
                if blank_count > 3:
                    self.warnings.append(f"Excessive blank lines around line {i+1}")
                    blank_count = 0  # Reset to avoid duplicate warnings
            else:
                blank_count = 0
        
        # Check for proper heading hierarchy
        headings = re.findall(r'^(#{1,6})\s+(.+)$', self.content, re.MULTILINE)
        if headings:
            self.info.append(f"✓ Found {len(headings)} headings")
        
        # Check for trailing whitespace
        trailing_whitespace_lines = [i+1 for i, line in enumerate(lines) if line.endswith(' ') or line.endswith('\t')]
        if trailing_whitespace_lines:
            self.warnings.append(f"Trailing whitespace on {len(trailing_whitespace_lines)} lines")
        
        # Check for contact information
        if 'github.com' not in self.content.lower():
            self.warnings.append("No GitHub profile link found")
    
    def print_results(self) -> bool:
        """Print validation results and return success status"""
        print("\n" + "="*60)
        
        # Print errors
        if self.errors:
            print(f"\n{Colors.RED}{Colors.BOLD}❌ ERRORS ({len(self.errors)}):{Colors.END}")
            for error in self.errors:
                print(f"{Colors.RED}  • {error}{Colors.END}")
        
        # Print warnings
        if self.warnings:
            print(f"\n{Colors.YELLOW}{Colors.BOLD}⚠️  WARNINGS ({len(self.warnings)}):{Colors.END}")
            for warning in self.warnings:
                print(f"{Colors.YELLOW}  • {warning}{Colors.END}")
        
        # Print info
        if self.info and not self.errors:
            print(f"\n{Colors.GREEN}{Colors.BOLD}✅ INFO ({len(self.info)}):{Colors.END}")
            for info_msg in self.info[:10]:  # Limit to first 10 to avoid clutter
                print(f"{Colors.GREEN}  • {info_msg}{Colors.END}")
            if len(self.info) > 10:
                print(f"{Colors.GREEN}  ... and {len(self.info) - 10} more checks passed{Colors.END}")
        
        print("\n" + "="*60)
        
        # Final summary
        if not self.errors and not self.warnings:
            print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 README validation passed with no issues!{Colors.END}\n")
            return True
        elif not self.errors:
            print(f"\n{Colors.YELLOW}{Colors.BOLD}✓ README validation passed with warnings{Colors.END}\n")
            return True
        else:
            print(f"\n{Colors.RED}{Colors.BOLD}✗ README validation failed{Colors.END}\n")
            return False

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <path_to_README.md> [repo_root]")
        print(f"Example: python {sys.argv[0]} README.md")
        print(f"Example: python {sys.argv[0]} README.md /path/to/repo")
        sys.exit(1)
    
    readme_path = sys.argv[1]
    repo_root = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not os.path.exists(readme_path):
        print(f"{Colors.RED}Error: README file not found: {readme_path}{Colors.END}")
        sys.exit(1)
    
    validator = ReadmeValidator(readme_path, repo_root)
    success = validator.validate_all()
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()