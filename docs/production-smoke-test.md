# Production Smoke Test

## Start
docker compose --env-file .env.production -f docker-compose.prod.yml up --build -d

## Verify containers
docker compose --env-file .env.production -f docker-compose.prod.yml ps

## Verify API through Nginx
curl http://127.0.0.1:8080/
curl http://127.0.0.1:8080/api/v1/health
curl http://127.0.0.1:8080/api/v1/projects

## Verify logs
docker compose --env-file .env.production -f docker-compose.prod.yml logs --tail=100 api
docker compose --env-file .env.production -f docker-compose.prod.yml logs --tail=100 nginx
docker compose --env-file .env.production -f docker-compose.prod.yml logs --tail=100 db

## Stop
docker compose --env-file .env.production -f docker-compose.prod.yml down
