import os
from pathlib import Path
from datetime import datetime

class AWSValidator:
    def __init__(self, repo_base):
        self.repo_base = Path(repo_base)
        self.results = []

    def log(self, message):
        print(message)

    # -----------------------------
    # Repository Structure Checks
    # -----------------------------
    def validate_structure(self):
        self.log("\n======================================================================")
        self.log("Repository Structure Validation")
        self.log("======================================================================")
        required_files = ["README.md", "LICENSE", ".gitignore", "CODE_OF_CONDUCT.md",
                          "CONTRIBUTING.md", "SECURITY.md", "main.tf"]
        required_dirs = ["incidents", "scripts", "docs", "templates"]

        passed = 0
        failed = 0

        for f in required_files:
            if (self.repo_base / f).exists():
                self.log(f"  ✓ Found {f}")
                passed += 1
            else:
                self.log(f"  ✗ Missing {f}")
                failed += 1

        for d in required_dirs:
            if (self.repo_base / d).exists():
                self.log(f"  ✓ Found {d}/ directory")
                passed += 1
            else:
                self.log(f"  ✗ Missing {d}/ directory")
                failed += 1

        # .gitignore checks
        gitignore_path = self.repo_base / ".gitignore"
        if gitignore_path.exists():
            gitignore_content = gitignore_path.read_text(encoding='utf-8')
            required_patterns = ["*.pem", "*.key", ".env", "*.tfstate", "__pycache__", "*.pyc"]
            for pattern in required_patterns:
                if pattern in gitignore_content:
                    self.log(f"  ✓ .gitignore includes {pattern}")
                else:
                    self.log(f"  ⚠ .gitignore missing {pattern}")
        else:
            self.log("  ⚠ .gitignore not found")

        self.results.append({"check": "Structure", "passed": passed, "failed": failed})

    # -----------------------------
    # Incident Scenarios Checks
    # -----------------------------
    def validate_incidents(self):
        self.log("\n======================================================================")
        self.log("Incident Scenarios Validation")
        self.log("======================================================================")

        incidents_path = self.repo_base / "incidents"
        if not incidents_path.exists():
            self.log("  ✗ incidents/ directory not found")
            self.results.append({"check": "Incidents", "passed": 0, "failed": 1})
            return

        incident_dirs = [d for d in incidents_path.iterdir() if d.is_dir()]
        if not incident_dirs:
            self.log("  ✗ No incident subdirectories found")
            self.results.append({"check": "Incidents", "passed": 0, "failed": 1})
            return

        passed = 0
        failed = 0
        for incident in sorted(incident_dirs):
            readme_file = incident / "README.md"
            problem_file = incident / "problem.py"
            solution_file = incident / "solution.py"
            if readme_file.exists() and problem_file.exists() and solution_file.exists():
                self.log(f"  ✓ {incident.name} contains all required files")
                passed += 1
            else:
                self.log(f"  ✗ {incident.name} is missing required files")
                failed += 1

        self.results.append({"check": "Incidents", "passed": passed, "failed": failed})

    # -----------------------------
    # Docstring Coverage
    # -----------------------------
    def validate_docstrings(self):
        self.log("\n======================================================================")
        self.log("Docstring Coverage Validation")
        self.log("======================================================================")
        py_files = list(self.repo_base.rglob("*.py"))
        total_files = len(py_files)
        if total_files == 0:
            self.log("  ⚠ No Python files found for docstring analysis")
            self.results.append({"check": "Docstrings", "coverage": 0})
            return

        with_docstring = 0
        for f in py_files:
            try:
                content = f.read_text(encoding='utf-8').strip()
            except Exception as e:
                self.log(f"  ⚠ Could not read {f}: {e}")
                continue
            if content.startswith('"""') or content.startswith("'''"):
                with_docstring += 1

        coverage = (with_docstring / total_files) * 100
        self.log(f"  ✓ Docstring coverage: {coverage:.1f}% ({with_docstring}/{total_files} files)")
        self.results.append({"check": "Docstrings", "coverage": coverage})

    # -----------------------------
    # README UTF-8 Check
    # -----------------------------
    def validate_readme(self):
        readme_path = self.repo_base / "README.md"
        if not readme_path.exists():
            self.log("  ✗ README.md not found")
            return
        try:
            content = readme_path.read_text(encoding='utf-8')
            self.log("  ✓ README.md read successfully with UTF-8 encoding")
        except UnicodeDecodeError:
            self.log("  ✗ README.md contains invalid UTF-8 characters")

    # -----------------------------
    # Run all validations
    # -----------------------------
    def run_all_validations(self):
        self.log(f"\nAWS ERROR-DRIVEN TROUBLESHOOTING LAB VALIDATOR")
        self.log(f"Timestamp: {datetime.now()}")
        self.validate_structure()
        self.validate_incidents()
        self.validate_docstrings()
        self.validate_readme()
        self.log("\n======================================================================")
        self.log("VALIDATION COMPLETE")
        self.log("======================================================================")
        return self.results


def main():
    repo_path = r"C:\Users\buche\docs\Desktop\REPOS\AWS_Error_Driven_Troubleshooting_Lab"
    validator = AWSValidator(repo_path)
    results = validator.run_all_validations()

if __name__ == "__main__":
    main()
