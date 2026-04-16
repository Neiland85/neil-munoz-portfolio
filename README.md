## 🧠 Why this project exists

This is not just a backend portfolio.

This repository is designed as a **demonstration artifact of architectural thinking**, aligned with real-world system design challenges.

It reflects how I approach:

- system boundaries
- security by default
- developer workflow as part of architecture
- verifiability over assumptions

---

## 🎯 Context & Intent

This project was built while preparing for senior/staff-level architecture roles, particularly in environments nearly to ciber-security and where systems are:
This project was built while preparing for senior/staff-level architecture roles, particularly in environments like **Minsait (Indra)**, where systems are:

- distributed
- long-lived
- integration-heavy
- subject to evolving constraints

Instead of showcasing complexity for its own sake, the goal is to demonstrate:

> how to build systems that remain understandable, testable, and trustworthy over time.

---

## 🧩 Architectural Philosophy

This repository embodies a simplified version of a broader concept:

> **Sentinel Mesh Gateway mindset**

Where:

- systems are not just built → they are **guarded**
- workflows are not optional → they are **enforced**
- trust is not assumed → it is **verified continuously**

---

## 🔍 What this project demonstrates

- Clear separation of concerns (API / domain / infra)
- Security integrated into the development lifecycle (not externalized)
- Fast feedback loops via local automation (pre-commit / pre-push)
- Predictable structure for maintainability
- Container-ready deployment model

---

## ⚖️ Engineering Trade-offs

This is intentionally **not over-engineered**.

Decisions made:

- SQLite locally vs PostgreSQL in Docker → balance between speed and realism
- Minimal abstraction layers → prioritize clarity over theoretical purity
- Git hooks over heavy CI → faster developer feedback
- Limited scope → focus on architectural signal, not feature volume

---

## 🚫 What is intentionally NOT included

- Authentication layer → not relevant to the core architectural goal
- Distributed tracing → acknowledged, but out of scope
- Microservices → would reduce clarity for this demonstration

---

## ⚠️ Known limitations

- Git hooks can be bypassed → this is a workflow guard, not a guarantee
- Limited test coverage → focuses on fast validation, not completeness
- No observability stack yet → identified as next step

---

## 🧪 Verifiability (for reviewers)

This repository is designed so that claims can be validated quickly:

```bash
# Run tests
PYTHONPATH=src pytest -q

# Trigger hooks manually
pre-commit run --all-files

# Build & run
docker-compose up --build

---

## 📬 Contact

For technical discussions, architecture reviews, or collaboration opportunities:

📧 admin@claritystructures.com

This repository is part of a broader body of work focused on **system design, security, and architectural clarity**.

---

## 🧾 License & Usage

© 2026 Neil Muñoz Lago — Clarity Structures Digital S.L

This project is released under the MIT License.

You are free to:

- use
- study
- adapt

However:

- this repository is intended as a **demonstration of architectural approach**
- not all design decisions are meant to be reused without context
- attribution is appreciated when referencing ideas or structure

---

## 🧠 Final Note

This repository is not just about code.

It is about:

- making systems understandable
- making behavior predictable
- making trust explicit

If you are evaluating this project:

> focus on the decisions, not just the implementation
