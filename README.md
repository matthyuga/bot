# Asistente IA MVP (Fase 4)

El proyecto ahora incluye la **Fase 4**: hardening operativo, manejo robusto de errores, logging y runbook/demo reproducible.

## Qué incluye actualmente
- Base web:
  - `app.py` (`/`, `/health`, `/chat`, `/metrics`) con manejo de errores HTTP.
  - `templates/index.html` para pruebas manuales.
- Persistencia:
  - `db.py`
  - `db/schema.sql`
- Herramientas funcionales:
  - `crear_cliente`, `listar_clientes`, `registrar_historial`, `ver_historial`
- IA (reglas):
  - `intents.py`
  - `orchestrator.py` (routing + `error_code` + logging de excepciones)
- Evaluación:
  - `data/prompts_eval.jsonl`
  - `scripts/evaluar_fase3.py`
- Operación Fase 4:
  - `scripts/init_db.py`
  - `scripts/demo_fase4.sh`
  - `docs/OPERACION_FASE4.md`
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

## Runbook rápido
```bash
python3 scripts/init_db.py
./run.sh
# en otra terminal:
./scripts/demo_fase4.sh
```

## Evaluación automática
```bash
python3 scripts/evaluar_fase3.py
```

## Ejecutar pruebas
```bash
pytest -q
```

## Próximo paso
Fase 5: integración de voz (STT/TTS) y opcional modulación MMVC/RVC.
