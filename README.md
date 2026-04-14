# neil-munoz-portfolio

Professional portfolio project built with **FastAPI**, with support for:

- backend API structure
- local SQLite development
- Dockerized PostgreSQL development
- Alembic migrations
- environment-based configuration
- Jinja2 template rendering
- static asset serving
- portfolio landing page integration

---

## Overview

This repository contains the foundation of a professional FastAPI application and the first integrated version of the portfolio website.

The project is designed to support both:

- **backend architecture work**, including API routes, services, schemas, and migrations
- **frontend portfolio delivery**, rendered through FastAPI using Jinja2 templates and static assets

The current implementation includes a portfolio landing page served at the root route.

---

## Current Features

- FastAPI application bootstrap
- health endpoint
- project API endpoint
- Alembic migration setup
- SQLite local development flow
- PostgreSQL Docker flow
- environment file policy for safe local configuration
- Jinja2 template support
- static files mounting
- portfolio landing page rendered from `/`

---

## Tech Stack

- **Python 3.12**
- **FastAPI**
- **SQLAlchemy**
- **Alembic**
- **Jinja2**
- **SQLite** for local development
- **PostgreSQL** for Dockerized development
- **Docker Compose**
- **Ruff**
- **Pytest**

---

## Project Structure

```text
src/
  app/
    api/
    core/
    domain/
    models/
    schemas/
    services/
    static/
    templates/
    main.py

alembic/
tests/
docs/
scripts/
data/
