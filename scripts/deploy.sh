#!/bin/bash
set -e

echo "==> Pulling target environment baseline..."
git pull origin main

echo "==> Building docker containers..."
docker-compose build --no-cache

echo "==> Running databank and schema migrations..."
docker-compose run --rm prov3rbs-api python scripts/populate_bank.py
docker-compose run --rm prov3rbs-api python scripts/init_db.py

echo "==> Tearing down stale services..."
docker-compose down --remove-orphans

echo "==> Spawning application stack..."
docker-compose up -d

echo "==> System deployment successfully completed."
