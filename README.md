# neil-munoz-portfolio

Portfolio técnico de Neil Muñoz construido sobre **FastAPI**.

El proyecto sirve una landing HTML desde el backend y expone una API mínima para healthcheck, configuración segura y gestión básica de proyectos.

## Estado real del proyecto

Este repositorio contiene actualmente:

- backend FastAPI
- landing HTML servida con Jinja2
- endpoints REST básicos
- middlewares de seguridad HTTP
- configuración tipada con `pydantic-settings`
- soporte de despliegue con Docker
- proxy de frontend en Vercel hacia backend en Railway

No contiene todavía:

- frontend desacoplado
- autenticación
- persistencia real integrada en las rutas de proyectos
- observabilidad completa
- pipeline CI formal
- endurecimiento completo de producción

## Arquitectura actual

### Runtime

- **Frontend público:** Vercel
- **Backend:** Railway
- **Aplicación:** FastAPI
- **Template engine:** Jinja2
- **Persistencia actual de `/api/v1/projects`:** memoria en proceso

### Estructura relevante

```text
src/app/main.py                 -> punto de entrada FastAPI
src/app/api/routes/web.py      -> landing HTML
src/app/api/routes/health.py   -> healthcheck API
src/app/api/routes/system.py   -> config segura
src/app/api/routes/projects.py -> CRUD básico en memoria
src/app/core/                  -> config, db, middleware, logging
src/app/templates/index.html   -> landing
tests/                         -> pruebas básicas
Dockerfile                     -> runtime Railway
vercel.json                    -> proxy Vercel -> Railway
Endpoints expuestos
HTML
GET /
GET /health
API
GET /api/v1/health
GET /api/v1/system/config
POST /api/v1/projects
GET /api/v1/projects
GET /api/v1/projects/{project_id}
PUT /api/v1/projects/{project_id}
DELETE /api/v1/projects/{project_id}
Requisitos
Python 3.12
pip
opcional: Docker
Instalación local
Entorno virtual
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .
pip install -r requirements-dev.txt
Variables de entorno

Crea .env.local si necesitas configuración local adicional.

El módulo de configuración admite, entre otras, estas variables:

APP_NAME
APP_ENV
APP_DEBUG
LOG_LEVEL
API_HOST
API_PORT
API_BASE_URL
CORS_ALLOW_ORIGINS
DATABASE_URL
SECRET_KEY
Arranque local
python -m uvicorn --app-dir src app.main:app --reload

Aplicación disponible en:

http://127.0.0.1:8000
Uso con Docker
Desarrollo
docker compose up --build

Aplicación disponible en:

http://127.0.0.1:8001
Pruebas y checks
Tests
PYTHONPATH=src pytest -q
Lint
ruff check src tests
Formato
ruff format src tests
Validación completa
make check
Despliegue actual
Backend en Railway

El Dockerfile ya está preparado para Railway y respeta la variable PORT.

Frontend en Vercel

Vercel no construye un frontend propio.
vercel.json hace rewrite de todas las rutas al backend publicado en Railway.

Limitaciones actuales
1. Persistencia de proyectos

La API de proyectos usa almacenamiento en memoria dentro del proceso.
Consecuencias:

no hay persistencia tras reinicio
no es adecuada para producción real
no garantiza consistencia entre múltiples réplicas
2. Configuración aún no integrada del todo

Existe módulo de configuración y de base de datos, pero la aplicación todavía no consume toda esa infraestructura de forma consistente.

3. README y estructura de producción en evolución

Hay archivos de soporte para PostgreSQL, Alembic, Nginx y Terraform, pero el flujo desplegado ahora mismo es deliberadamente más simple:

Vercel
Railway
FastAPI
landing servida por backend
Siguiente trabajo técnico prioritario

Orden correcto de mejora:

conectar rutas de proyectos a servicio real
sustituir almacenamiento en memoria por persistencia real
limpiar core/db.py
usar configuración centralizada para CORS y system/config
endurecer configuración de producción
ampliar test coverage
Licencia

MIT.

Contacto
Email: admin@claritystructures.com
GitHub: https://github.com/Neiland85
