# Asistente IA MVP (Fase 1)

Este repositorio contiene la base del asistente IA y ahora incluye la **Fase 1 completa**: persistencia SQLite + tools funcionales con validación.

## Qué incluye actualmente
- Base web mínima:
  - `app.py` (`/` y `/health`)
  - `templates/index.html`
- Persistencia:
  - `db.py` (conexión, inicialización y helpers)
  - `db/schema.sql` (tablas `clientes`, `historial`, `eventos_chat`)
- Herramientas de dominio:
  - `crear_cliente`
  - `listar_clientes`
  - `registrar_historial`
  - `ver_historial`
- Módulos de IA inicial:
  - `intents.py`
  - `orchestrator.py`
- Tests:
  - `tests/test_tools.py`
  - `tests/test_smoke.py` (se omite si Flask no está disponible)

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

Abrir en navegador:
- `http://localhost:5000/`
- `http://localhost:5000/health`

## Ejecutar pruebas
```bash
pytest -q
```

## Próximo paso
Fase 2: intención + orquestador conectados a tools para endpoint de chat (`/chat`).
