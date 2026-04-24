# Asistente IA MVP (Fase 0)

Este repositorio quedó preparado con la **estructura base de arranque** para el proyecto del asistente IA.

## Qué incluye Fase 0
- Estructura inicial de módulos:
  - `app.py`
  - `db.py`
  - `tools.py`
  - `intents.py`
  - `orchestrator.py`
  - `templates/index.html`
  - `tests/test_smoke.py`
- Dependencias mínimas en `requirements.txt`.
- Script de arranque `run.sh`.
- Normas de trabajo en `NORMAS_EQUIPO.md`.

## Requisitos
- Python 3.10+

## Instalación rápida
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar
```bash
./run.sh
```

Abrir en navegador:
- `http://localhost:5000/`
- `http://localhost:5000/health`

## Ejecutar pruebas
```bash
pytest -q
```

## Próximo paso
Implementar Fase 1: esquema SQL + tools reales con validación y persistencia.
