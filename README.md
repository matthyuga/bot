# Asistente IA MVP (Fase 3)

El proyecto ahora incluye la **Fase 3**: UX básica de chat + métricas operativas + evaluación con dataset de prompts.

## Qué incluye actualmente
- Base web:
  - `app.py` (`/`, `/health`, `/chat`, `/metrics`)
  - `templates/index.html` (UI de chat para probar intención/tool/latencia)
- Persistencia:
  - `db.py`
  - `db/schema.sql`
- Herramientas funcionales:
  - `crear_cliente`, `listar_clientes`, `registrar_historial`, `ver_historial`
- IA (reglas):
  - `intents.py` (clasificador por keywords)
  - `orchestrator.py` (router intención->tool + logging)
- Evaluación Fase 3:
  - `data/prompts_eval.jsonl` (dataset de prompts con intención esperada)
  - `scripts/evaluar_fase3.py` (accuracy intención, éxito de tools, latencia)
- Tests:
  - `tests/test_tools.py`
  - `tests/test_orchestrator.py`
  - `tests/test_smoke.py`
  - `tests/test_phase3_api.py`

## Requisitos
- Python 3.10+

## Instalación rápida
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar app
```bash
./run.sh
```

## Probar endpoints
```bash
curl -s http://localhost:5000/health
curl -s -X POST http://localhost:5000/chat \
  -H 'Content-Type: application/json' \
  -d '{"message":"crear cliente Ana"}'
curl -s http://localhost:5000/metrics
```

## Evaluar Fase 3
```bash
python3 scripts/evaluar_fase3.py
```

## Ejecutar pruebas
```bash
pytest -q
```

## Próximo paso
Fase 4: endurecimiento (errores, observabilidad, documentación de operación y demo estable).
