import sys
import os

class ReadmeValidator:
    def __init__(self, readme_path):
        self.readme_path = readme_path
        self.passed_checks = 0
        self.failed_checks = 0

    def validate(self):
        if not os.path.isfile(self.readme_path):
            print(f"[ERROR] File does not exist: {self.readme_path}")
            self.failed_checks += 1
            return

        with open(self.readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Example check: README should have a title
        if content.startswith("# "):
            self.passed_checks += 1
        else:
            print(f"[FAIL] {self.readme_path} is missing a top-level title (# )")
            self.failed_checks += 1

        # Example check: must have a TL;DR section
        if "TL;DR" in content:
            self.passed_checks += 1
        else:
            print(f"[FAIL] {self.readme_path} is missing a TL;DR section")
            self.failed_checks += 1

        # Add more checks here as needed
        # Example: Check for 'Installation', 'Usage', 'License'
        for section in ["Installation", "Usage", "License"]:
            if section in content:
                self.passed_checks += 1
            else:
                print(f"[FAIL] {self.readme_path} is missing '{section}' section")
                self.failed_checks += 1

    def report(self):
        print(f"[RESULT] {self.readme_path}: Passed {self.passed_checks}, Failed {self.failed_checks}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_readme.py <path_to_README.md>")
        sys.exit(1)

    readme_path = sys.argv[1]
    validator = ReadmeValidator(readme_path)
    validator.validate()
    validator.report()
