# Configuration and secrets policy

## Scope

This project treats environment variables as a runtime input mechanism, not as a secret management system.

## Rules

1. Real secrets are never committed to the repository.
2. `.env.example` is the configuration contract.
3. Local development uses `.env.local`, which is ignored by Git.
4. Staging and production must receive secrets from runtime or platform-managed secret storage.
5. The application must fail fast if required variables are missing or invalid.
6. Secrets must never be printed in logs, stack traces, build output, or health endpoints.

## Environment model

### Local
- Uses `.env.local`
- Lowest possible privileges
- Sandbox/test credentials whenever possible

### Dev
- Separate credentials from local
- Prefer platform/runtime injection over shared files

### Staging
- Mirrors production structure
- Never reuses production secrets

### Production
- No `.env.production` committed to repo
- Secrets injected at runtime
- Rotation and access control required

## Frontend rule

Any variable reachable by browser code must be treated as public by design.

## Backend rule

Settings must be validated on startup and secrets must be redacted from logs.
