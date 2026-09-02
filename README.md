# DevSecOps Automated Vulnerability Scanner

A lightweight DevSecOps pipeline project featuring a containerized Flask web application with an automated security scanning mechanism using Trivy and GitHub Actions.

## 🚀 Features
- **Web UI Dashboard:** Simple interface allowing users to access the application and upload code archives for analysis.
- **Containerization:** Fully packaged using Docker for environment consistency.
- **Automated Security Scanning:** Integrated **Trivy** via GitHub Actions to scan Docker images for vulnerabilities on every push.
- **Security Guardrail:** Automatically fails the CI pipeline when critical or high vulnerabilities are detected, preventing insecure deployments.

## 🛠️ Tech Stack
- **Python (Flask)** - Web framework
- **Docker** - Containerization
- **Trivy** - Vulnerability scanner
- **GitHub Actions** - CI/CD pipeline automation

## ⚙️ Local Setup & Execution
1. Clone the repository:
   ```bash
   git clone [https://github.com/Anjali-0910/devsecops-scanner.git](https://github.com/Anjali-0910/devsecops-scanner.git)
   cd devsecops-scanner