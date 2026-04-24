# Operación Fase 5 (voz básica + hook de modulación)

## Objetivo
Agregar un pipeline de voz mínimo para el asistente:
1. generar respuesta textual,
2. sintetizar artefacto TTS,
3. activar modulación opcional (mock) para futura integración MMVC/RVC.

## Qué se agregó
- `voice_pipeline.py`:
  - `VoiceConfig`
  - `MockSTT`
  - `MockTTS`
  - `MockVoiceModulator`
  - `VoicePipeline`
- endpoint `POST /voice/chat` en `app.py`.
- script `scripts/demo_fase5.sh` para demo rápida.

## Nota importante
La modulación actual está en **modo mock**; no transforma audio real todavía. El objetivo es dejar listo el contrato para integrar MMVC/RVC en fase siguiente.

## Runbook
1. Levantar servidor:
   ```bash
   ./run.sh
   ```
2. Ejecutar demo:
   ```bash
   ./scripts/demo_fase5.sh
   ```
3. Revisar artefactos generados:
   ```bash
   ls outputs/
   ```

## Contrato de `/voice/chat`
Entrada JSON:
```json
{
  "message": "crear cliente Ana",
  "tts_style": "energetic",
  "enable_modulation": true,
  "voice_character": "hero"
}
```

Salida (ejemplo):
```json
{
  "ok": true,
  "intent": "crear_cliente",
  "response": "Cliente creado: #1 - Ana",
  "error_code": null,
  "voice": {
    "ok": true,
    "tts_artifact": "outputs/tts_...txt",
    "tts_style": "energetic",
    "modulation": {
      "enabled": true,
      "character": "hero",
      "note": "Mock mode: integrar MMVC/RVC en Fase 5.1"
    }
  },
  "elapsed_ms": 12.3
}
```
