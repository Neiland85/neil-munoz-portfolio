# Next Layer Architecture

## Current runtime

- Public entrypoint: Vercel
- Backend runtime: Railway
- Application: FastAPI
- HTML rendering: Jinja2
- Current project API: CRUD over project resource
- Current data strategy: SQLModel-compatible application with Alembic already present in the repository

## Scalable technologies compatible with the current architecture

### 1. Managed PostgreSQL

Natural next step for durable persistence.

Why it fits:

- already aligned with SQLAlchemy / SQLModel
- already anticipated in repository docs and examples
- supported natively by Railway
- avoids process-memory state loss

### 2. SQLModel + SQLAlchemy session pattern

Natural persistence layer without redesign.

Why it fits:

- dependencies already present
- current domain/service split can evolve into repository/service split later
- low migration cost from current code

### 3. Alembic

Schema migration control.

Why it fits:

- already present in repository
- avoids manual schema drift
- required once PostgreSQL becomes canonical

### 4. Redis

Optional next layer after DB persistence.

Use cases:

- idempotency keys
- lightweight caching
- request throttling
- small ephemeral control state

Not required for the current production cut.

### 5. Structured logging

First observability layer.

Minimum useful shape:

- request path
- method
- status code
- duration
- environment
- request id

### 6. OpenTelemetry

Next serious observability layer.

Use when:

- external integrations grow
- multiple services appear
- request tracing becomes necessary

### 7. Request ID / Correlation ID

Cheap and high-value runtime control.

Use for:

- incident tracing
- log correlation
- debugging across proxy/runtime boundaries

## Recommended production path

### Phase 1

- real production environment variables
- clean runtime config
- durable database connection

### Phase 2

- move project persistence to SQLModel-backed storage
- stop using process-local memory as state

### Phase 3

- formalize migrations with Alembic
- introduce structured logging

### Phase 4

- add Redis only if idempotency/caching becomes necessary
- add OpenTelemetry only if real tracing pressure exists

## Technologies intentionally postponed

- Kubernetes
- microservices
- queues
- API gateway
- service mesh
- Terraform-heavy rollout
- extra proxies beyond current need

## Decision

Keep the current architecture.

Scale by deepening the existing stack:

- FastAPI
- Railway
- Vercel
- SQLModel
- PostgreSQL
- Alembic
- later: Redis and observability
