#!/usr/bin/env bash
set -eu

echo "Checking for forbidden env files tracked by git..."

tracked_env_files="$(git ls-files | grep -E '(^|/)\.env($|[.])' || true)"

if [ -n "$tracked_env_files" ]; then
  echo "ERROR: tracked env-like files found:"
  echo "$tracked_env_files"
  echo
  echo "Only .env.example should be committed."
  exit 1
fi

echo "OK: no tracked secret env files detected."
