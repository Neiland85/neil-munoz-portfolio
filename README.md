# neil-munoz-portfolio

Professional portfolio project built with **FastAPI**, with a strong focus on:

- backend architecture
- security by design
- developer workflow automation
- production-ready practices

---

## ⚙️ Development Workflow & Security

This project follows a **security-first and automation-driven development workflow**.

### 🔒 Pre-commit Hooks

Before every commit:

- Code formatting (`ruff-format`)
- Linting (`ruff`)
- Trailing whitespace & EOF fixes
- Merge conflict detection
- Sensitive file protection

---

### 🚫 Sensitive Data Protection

The repository blocks:

- `.env`, `.env.*`
- `*.pem`, `*.key`
- credentials or secrets

---

### 🧪 Pre-push Validation

Before pushing:

- Test suite runs automatically

```bash
PYTHONPATH=src pytest -q
🧠 Philosophy
Signal over noise
Fast developer feedback
Security by design
🚀 Why This Matters
Prevents production issues early
Reduces debugging time
Ensures consistent quality
Protects against credential leaks
