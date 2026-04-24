# Asistente IA MVP (Fase 5)

El proyecto ahora incluye la **Fase 5**: integración de voz básica (mock) sobre el flujo del asistente, con endpoint dedicado y contrato para modulación futura MMVC/RVC.

## Qué incluye actualmente
- Base web:
  - `app.py` (`/`, `/health`, `/chat`, `/voice/chat`, `/metrics`)
  - `templates/index.html`
- Persistencia:
  - `db.py`
  - `db/schema.sql`
- Herramientas funcionales:
  - `crear_cliente`, `listar_clientes`, `registrar_historial`, `ver_historial`
- IA (reglas):
  - `intents.py`
  - `orchestrator.py`
- Voz Fase 5:
  - `voice_pipeline.py` (MockSTT/MockTTS/MockVoiceModulator)
  - `scripts/demo_fase5.sh`
  - `docs/OPERACION_FASE5.md`
- Evaluación y operación previa:
  - `data/prompts_eval.jsonl`
  - `scripts/evaluar_fase3.py`
  - `scripts/init_db.py`
  - `docs/OPERACION_FASE4.md`
- Tests:
  - `tests/test_tools.py`
  - `tests/test_orchestrator.py`
  - `tests/test_phase3_api.py`
  - `tests/test_phase5_api.py`
  - `tests/test_voice_pipeline.py`
  - `tests/test_smoke.py`

## Requisitos
- Python 3.10+

## Instalación rápida
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Runbook rápido (fase 5)
```bash
python3 scripts/init_db.py
./run.sh
# en otra terminal:
./scripts/demo_fase5.sh
```

## Probar endpoint de voz
```bash
curl -s -X POST http://localhost:5000/voice/chat \
  -H 'Content-Type: application/json' \
  -d '{"message":"crear cliente Ana","tts_style":"energetic","enable_modulation":true,"voice_character":"hero"}'
```

## Ejecutar pruebas
```bash
pytest -q
```

## Próximo paso
Fase 5.1: reemplazar mocks de TTS/modulación por integración real con proveedor TTS y MMVC/RVC.
