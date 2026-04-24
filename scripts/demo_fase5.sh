#!/usr/bin/env bash
set -euo pipefail

echo "[1/3] voz sin modulación"
curl -s -X POST http://localhost:5000/voice/chat \
  -H 'Content-Type: application/json' \
  -d '{"message":"ayuda","tts_style":"calm","enable_modulation":false}'
printf '\n\n'

echo "[2/3] voz con modulación mock"
curl -s -X POST http://localhost:5000/voice/chat \
  -H 'Content-Type: application/json' \
  -d '{"message":"crear cliente Ana","tts_style":"energetic","enable_modulation":true,"voice_character":"hero"}'
printf '\n\n'

echo "[3/3] ver artefactos"
ls -1 outputs | tail -n 5
