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

---

## Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL (Docker) / SQLite (local)
- Docker & Docker Compose
- Pytest
- Ruff (linting & formatting)
- Pre-commit hooks

---

## Current Features

- Modular FastAPI architecture
- Health check endpoints
- Structured API routing
- Environment-based configuration
- Database migrations with Alembic
- Local + Dockerized development setup
- Pre-commit security and quality checks
- Pre-push automated test validation

---

## Engineering Trade-offs

This project intentionally balances simplicity with production-readiness.

Trade-offs made:

- SQLite for local development vs PostgreSQL in Docker for realism
- Minimal external dependencies to keep the system understandable
- Lightweight service layer instead of heavy abstraction
- Fast feedback hooks instead of heavy CI pipelines

These decisions prioritize clarity and iteration speed while still reflecting real-world constraints.

---

## What I would improve next

If this project evolved further, the next steps would be:

- Introduce authentication & authorization layer
- Add structured logging and observability (e.g. OpenTelemetry)
- Expand test coverage (integration + contract tests)
- Introduce CI/CD pipeline (GitHub Actions)
- Add API versioning strategy
- Improve error handling and monitoring

---
