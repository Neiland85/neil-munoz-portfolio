# Production Hardening Checklist

## Branching

- [x] main is the default branch
- [x] local and remote branches cleaned
- [x] branch protection enabled for main
- [x] PR required before merge
- [x] direct pushes to main blocked

## Application

- [x] FastAPI app boots correctly
- [x] API router is wired
- [x] database engine is restored
- [x] production config policy finalized
- [x] startup/bootstrap strategy documented
- [ ] error handling reviewed
- [ ] structured logging reviewed
- [x] error handling reviewed
- [x] structured logging reviewed

## Database

- [x] local SQLite fallback works
- [x] production PostgreSQL compose base created
- [x] production migrations flow defined
- [x] DB healthcheck validated
- [ ] backup strategy defined

## Infrastructure

- [ ] reverse proxy added
- [ ] TLS strategy defined
- [ ] domain and DNS defined
- [ ] container restart policy validated
- [x] reverse proxy added
- [ ] TLS strategy defined
- [ ] domain and DNS defined
- [x] container restart policy validated
- [x] secrets strategy defined
- [x] production env variables documented

## Delivery

- [x] CI checks required on PR
- [x] deployment strategy selected
- [x] smoke test checklist written
- [x] rollback procedure documented
