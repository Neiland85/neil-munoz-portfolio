# Production Runbook

## Goal
Deploy the portfolio API in a production-like setup with:
- FastAPI app
- PostgreSQL
- reverse proxy
- controlled environment variables
- repeatable deployment steps

## Required decisions
1. Hosting target
   - VPS
   - managed container platform
   - Kubernetes
2. Domain and TLS
3. Secret storage strategy
4. Database migration workflow
5. Backup and restore workflow

## Minimum production architecture
- reverse proxy (Nginx or Caddy)
- API container
- PostgreSQL container or managed database
- persistent volume for database
- environment file not committed with real secrets

## Deployment checks
- API health endpoint responds
- root route responds
- database connection works
- migrations applied
- logs visible
- restart survives reboot
- backup path verified

## Rollback
- keep previous image tag available
- keep previous env file backup
- restore previous compose version
- verify health endpoint
