#!/bin/bash

set -e

echo "==== Installing Portfolio System ===="

if ! command -v docker &> /dev/null
then
    echo "Docker is required but not installed."
    exit 1
fi

if ! command -v docker compose &> /dev/null
then
    echo "Docker Compose is required but not installed."
    exit 1
fi

if [ ! -f .env ]; then
    echo "Creating .env from template..."
    cp .env.example .env
    echo "Please edit .env before continuing."
    exit 0
fi

echo "Building containers..."
docker compose build

echo "Starting services..."
docker compose up -d

echo "==== Installation completed ===="
