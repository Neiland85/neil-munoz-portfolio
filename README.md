# Neil Muñoz Portfolio API

A FastAPI-based portfolio service designed as a demonstration artifact of architectural thinking, operational clarity, and secure-by-default engineering.

This repository is not intended to showcase feature volume.
It is intended to show how a system can remain understandable, testable, and evolvable under real operational constraints.

---

## Why this repository exists

This project exists to demonstrate practical architecture decisions in a compact system:

- clear boundaries between API, services, domain, models, and configuration
- explicit configuration contracts
- security-by-default middleware and delivery posture
- container-friendly execution
- operational documentation for hardening, smoke tests, and production runbooks
- a disciplined path for future evolution through ADRs

It is built to be reviewed quickly and discussed seriously.

---

## What this project demonstrates today

### Application structure
- FastAPI application with separated routes, services, schemas, models, and core modules
- SQLModel persistence layer
- migration-ready structure with Alembic
- HTML rendering for the public web surface
- API endpoints for health, system, and projects

### Configuration and execution model
- typed settings via `pydantic-settings`
- environment-driven configuration
- local SQLite workflow for speed
- PostgreSQL-ready production path
- Docker and Docker Compose execution

### Security and operational posture
- CORS configuration via environment
- security headers middleware
- cookie consent middleware
- production-oriented environment policy
- hardening and runbook documentation already present in `docs/`

### Reviewability
- small enough to inspect end-to-end
- opinionated enough to discuss trade-offs
- structured enough to evolve without immediate rewrites

---

## Architectural intent

The repository is designed around a simple idea:

> systems should be easy to reason about before they are made complex.

That means:

- boundaries should be visible
- contracts should be explicit
- configuration should be validated
- failure modes should be documented
- future evolution should be recorded through decisions, not memory

---

## Current repository layout

```text
src/app/
  api/        HTTP routes and web entry points
  core/       configuration, database, logging, middleware
  domain/     domain objects and conceptual core
  models/     persistence models
  schemas/    request and response contracts
  services/   application service layer

docs/
  configuration.md
  next-layer-architecture.md
  production-hardening-checklist.md
  production-runbook.md
  production-smoke-test.md
  adr/        architecture decision records
Key engineering decisions
1. Keep the system small, but structured

This is intentionally not a microservice system.
The goal is architectural signal, not distributed complexity.

2. Configuration is a contract

.env.example is part of the system contract.
The app validates required settings and rejects invalid production shapes early.

3. Security belongs in the default path

Security headers and basic request posture are part of the running application, not external commentary.

4. Local speed matters

SQLite is used locally to reduce setup friction.
The production path remains compatible with PostgreSQL and Alembic-based evolution.

5. Evolution must be documented

Future changes around idempotency, retries, queues, and edge resilience should be captured through ADRs.

Known constraints and next improvements
Current intentional constraints
no authentication layer yet
no background job system yet
no queue-based workflow yet
no explicit idempotency layer yet
no full observability stack yet
no edge or carrier-resilience implementation yet
Planned direction
strengthen architecture documentation with ADRs
formalize contracts and failure modes
define idempotency and retry policy before introducing asynchronous workflows
add edge resilience and carrier-readiness blueprint for enterprise discussion contexts
Local development
Requirements
Python 3.12
virtual environment
optional Docker / Docker Compose
Install
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
Run locally
cp .env.example .env.local
PYTHONPATH=src uvicorn app.main:app --app-dir src --reload
Run tests
PYTHONPATH=src pytest -q
Run with Docker Compose
docker-compose up --build
Documentation

The repository already includes operational documentation:

docs/configuration.md
docs/next-layer-architecture.md
docs/production-hardening-checklist.md
docs/production-runbook.md
docs/production-smoke-test.md

Architecture Decision Records are introduced under:

docs/adr/
Intended review lens

If you are evaluating this repository, focus on:

boundary clarity
contract definition
operational realism
trade-off quality
ease of future evolution

This repository is not about scale theatre.
It is about making the next correct change easier than the next accidental one.

Contact

For technical discussion, architecture review, or collaboration:

admin@claritystructures.com

License

This repository is released under the MIT License.
See LICENSE for details.
