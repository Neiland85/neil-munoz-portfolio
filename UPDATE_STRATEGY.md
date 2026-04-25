# Update Strategy

This project is maintained as a versioned deployment-ready software package.

## Branches

- main: active development
- deploy/production: stable deploy branch
- releases/vX.Y.Z: packaged client releases

## Update model

Clients receive updates through tagged releases.

Recommended update flow:

1. Backup current environment variables.
2. Pull latest release.
3. Rebuild containers.
4. Run tests.
5. Deploy.

## Commands

git fetch --tags
git checkout vX.Y.Z
docker compose build
docker compose up -d

## Safety

Never commit .env files.
Never overwrite client-specific configuration.
