# Asistente IA MVP (Fase 2)

El proyecto ahora incluye la **Fase 2**: detección de intención + orquestación + ejecución de tools + logging en base de datos.

## Qué incluye actualmente
- Base web mínima:
  - `app.py` (`/`, `/health`, `/chat`)
  - `templates/index.html`
- Persistencia:
  - `db.py` (conexión, init y helpers)
  - `db/schema.sql` (tablas `clientes`, `historial`, `eventos_chat`)
- Herramientas funcionales:
  - `crear_cliente`
  - `listar_clientes`
  - `registrar_historial`
  - `ver_historial`
- IA (reglas):
  - `intents.py` (clasificador de intención por keywords)
  - `orchestrator.py` (router intención->tool + respuesta)
- Tests:
  - `tests/test_tools.py`
  - `tests/test_orchestrator.py`
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

## Probar endpoints
```bash
curl -s http://localhost:5000/health
curl -s -X POST http://localhost:5000/chat \
  -H 'Content-Type: application/json' \
  -d '{"message":"ayuda"}'
```

## Ejecutar pruebas
```bash
pytest -q
```

## Próximo paso
Fase 3: mejorar UX del chat, métricas y evaluación con dataset de prompts.
