# Production Smoke Test

## Local Docker validation

### Build image
docker build -t neil-munoz-portfolio:local .

### Run container
docker run --rm \
  -p 8001:8000 \
  -e APP_ENV=local \
  -e APP_NAME=nm-portfolio-api \
  -e APP_DEBUG=false \
  -e LOG_LEVEL=INFO \
  -e API_BASE_URL=http://127.0.0.1:8001 \
  -e CORS_ALLOW_ORIGINS=http://localhost:3000,http://127.0.0.1:3000,http://localhost:8001,http://127.0.0.1:8001 \
  -e DATABASE_URL=sqlite:///./data/local.db \
  -e SECRET_KEY=local-development-secret-key-12345 \
  -v $(pwd)/data:/app/data \
  neil-munoz-portfolio:local

### Verify
curl http://127.0.0.1:8001/health
curl http://127.0.0.1:8001/api/v1/health
curl http://127.0.0.1:8001/api/v1/system/config
curl http://127.0.0.1:8001/api/v1/projects

## Compose validation

### Start
docker compose up --build -d

### Verify
docker compose ps
curl http://127.0.0.1:8001/health
curl http://127.0.0.1:8001/api/v1/health
curl http://127.0.0.1:8001/api/v1/system/config
curl http://127.0.0.1:8001/api/v1/projects

### Stop
docker compose down

## Production-like validation

### Required
A local `.env.production` file with real runtime values.

### Start
docker compose -f docker-compose.prod.yml up --build -d

### Verify
docker compose -f docker-compose.prod.yml ps
curl http://127.0.0.1:8001/health
curl http://127.0.0.1:8001/api/v1/health
curl http://127.0.0.1:8001/api/v1/system/config
curl http://127.0.0.1:8001/api/v1/projects

### Stop
docker compose -f docker-compose.prod.yml down
