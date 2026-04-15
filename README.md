# 🧠 Backend Systems Portfolio — Arquitectura Operable, Auditable y Segura

> No se trata de que un sistema funcione.
> Se trata de que pueda **operarse, entenderse y evolucionar sin romperse**.

---

## 📌 Visión

Este proyecto no es una simple API ni una landing.
Es una demostración de cómo diseñar sistemas backend con foco en:

- **Operabilidad**
- **Auditabilidad**
- **Seguridad por defecto**
- **Separación clara de responsabilidades**

Inspirado en entornos donde:
- los sistemas viven años
- múltiples equipos interactúan
- los errores cuestan dinero

---

## 🧱 Arquitectura (Blueprint)

👉 [Ver sección arquitectura en la web](/#arquitectura)

El sistema se estructura en bloques independientes:

### 🔹 Context
- Request, identidad, permisos, intención
- Todo explícito, nada implícito

### 🔹 Policy
- Reglas de negocio y decisiones justificadas
- Separación entre lógica y ejecución

### 🔹 Execution
- Orquestación de acciones
- Idempotencia, transacciones, control de efectos

### 🔹 Data
- Persistencia coherente
- No accidental, siempre intencional

### 🔹 Audit
- Logs, trazas y eventos
- El sistema deja rastro útil

### 🔹 Ops
- Observabilidad
- Runbooks implícitos en el diseño

---

## 🔐 Seguridad (Security by Design)

Este proyecto implementa seguridad desde la base:

### ✅ CORS Controlado
- No se expone el backend indiscriminadamente
- Configuración explícita por entorno

### ✅ Security Headers Middleware
- `X-Content-Type-Options`
- `X-Frame-Options`
- `Content-Security-Policy`
- `Referrer-Policy`

👉 Protege contra:
- Clickjacking
- MIME sniffing
- XSS básicos

---

### 🍪 Cookie Consent (GDPR-ready)
- Middleware que inyecta `cookie_consent`
- Sin consentimiento → sin tracking implícito

---

### 🔒 Endpoint Hygiene

Ejemplo:

```http
GET /api/v1/system/config

✔ Expone configuración segura
❌ No filtra secretos

🌐 Endpoints clave
GET /api/v1/health
GET /api/v1/system/config
GET /api/v1/projects
POST /api/v1/projects
Healthcheck
{
  "status": "ok",
  "service": "portfolio-api"
}
System Config
{
  "service": "portfolio-api",
  "environment": "production"
}
🧪 Testing

El sistema incluye tests de:

Healthcheck
Seguridad (cookies, headers)
CRUD de proyectos
PYTHONPATH=src pytest -q
🐳 Docker (Production-ready)
Build
docker build -f Dockerfile.prod -t portfolio-api:prod .
Run
docker run -p 8000:8000 --env-file .env.production portfolio-api:prod
⚙️ Infraestructura
NGINX
Reverse proxy
Separación frontend/backend
Preparado para TLS
Docker Compose
API
DB (Postgres)
NGINX
📂 Estructura del proyecto
src/app/
  api/
  core/
  domain/
  services/
  templates/

Separación clara:

domain → lógica pura
services → casos de uso
api → entrada HTTP
🧠 Principios aplicados
Explicit > Implicit
Systems > Scripts
Operable > Funcional
Observable > Opaco
Evolvable > Rígido
🚀 Despliegue

Preparado para:

VPS (Hetzner)
Docker
NGINX reverse proxy
DNS externo (GoDaddy / Cloudflare)
📖 Filosofía

La diferencia entre un backend y un sistema es que
el segundo puede sobrevivir en producción.

👤 Autor

Neil Muñoz
Arquitectura backend enfocada a sistemas reales
