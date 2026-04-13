# Secure-App-Pipeline: A DevSecOps Master Project
This project demonstrates a **Shift Left** security approach by integrating automated security scanning (SAST) into a containerized Python web application
## The Challenge
The initial application contained a **CWE-89: SQL Injection** vulnerability. This flaw allowed unauthorized access to the user database by manipulating input strings.
## Security Tools
- **Docker:** Used for environment isolation and consistent deployment.
- **Bandit:** An industry-standard Static Application Security Testing (SAST) tool for Python.
## Implementation Steps
1. **Containerization:** Wrapped the Flask app in a Docker image to ensure it runs securely in any environment.
2. **Automated Scanning:** Ran `Bandit` against the source code, which identified a "Medium/High" severity SQL injection risk.
3. **Remediation:** Refactored the code to use **Parameterized Queries**, separating user input from logic.
4. **Verification:** Re-ran the security scan to confirm a "Clean" status (0 issues).
## Evidence
- **Security Scan Failure:** (Insert `04-sast-scan-results.png` here)
- **Security Scan Success:** (Insert `05-remediation-scan-pass.png` here)
- **Blocked Injection Proof:** (Insert `06-injection-blocked.png` here)
