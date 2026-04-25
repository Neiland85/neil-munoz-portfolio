# Production Hardening Checklist

## Branching

- [x] main is the default branch
- [x] local and remote branches cleaned
- [ ] branch protection enabled for main
- [ ] PR required before merge
- [ ] direct pushes to main blocked

## Application

- [x] FastAPI app boots correctly
- [x] API router is wired
- [x] database engine is restored
- [ ] production config policy finalized
- [ ] startup/bootstrap strategy documented
- [ ] error handling reviewed
- [ ] structured logging reviewed

## Database

- [x] local SQLite fallback works
- [x] production PostgreSQL compose base created
- [ ] production migrations flow defined
- [ ] DB healthcheck validated
- [ ] backup strategy defined

## Infrastructure

- [ ] reverse proxy added
- [ ] TLS strategy defined
- [ ] domain and DNS defined
- [ ] container restart policy validated
- [ ] secrets strategy defined
- [ ] production env variables documented

## Delivery

- [ ] CI checks required on PR
- [ ] deployment strategy selected
- [ ] smoke test checklist written
- [ ] rollback procedure documented
