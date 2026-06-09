# Environment Loading and Secrets Policy

## Status

This repository does not auto-load local environment files from application runtime code.

Runtime configuration is read from process environment variables.

## Local development

Local `.env.local` files may be used by developers, but they must be loaded explicitly by the developer shell or local tooling.

Example:

    set -a
    source .env.local
    set +a

Then run the application normally.

## Production

Production secrets must be injected by the runtime platform, container orchestrator or deployment environment.

The application must not depend on implicit local env-file loading in production mode.

## Repository policy

Real secret files must never be committed.

The following files are local/runtime material only:

- `.env`
- `.env.local`
- `.env.production`
- `.env.*.local`

Examples may exist only as placeholder templates.

## Redaction

Application configuration summaries must not expose secret values.

Boolean indicators such as `secret_key_configured` are acceptable.

Raw values such as passwords, tokens, DSNs or database URLs must not be printed in logs or summaries.
