#!/usr/bin/env bash
set -euo pipefail

echo "[1/5] health"
curl -s http://localhost:5000/health
printf '\n\n'

echo "[2/5] ayuda"
curl -s -X POST http://localhost:5000/chat -H 'Content-Type: application/json' -d '{"message":"ayuda"}'
printf '\n\n'

echo "[3/5] crear cliente"
curl -s -X POST http://localhost:5000/chat -H 'Content-Type: application/json' -d '{"message":"crear cliente Ana"}'
printf '\n\n'

echo "[4/5] listar clientes"
curl -s -X POST http://localhost:5000/chat -H 'Content-Type: application/json' -d '{"message":"listar clientes 5"}'
printf '\n\n'

echo "[5/5] metrics"
curl -s http://localhost:5000/metrics
printf '\n'
