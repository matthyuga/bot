"""Pipeline de voz Fase 5 (STT/TTS + hook opcional de modulación)."""

from __future__ import annotations

import time
from dataclasses import dataclass
from pathlib import Path


@dataclass
class VoiceConfig:
    tts_style: str = "neutral"
    voice_character: str = "default"
    enable_modulation: bool = False


class MockSTT:
    """STT mock para MVP: en Fase 5 aceptamos texto directo o bytes y devolvemos texto marcador."""

    def transcribe(self, audio_bytes: bytes) -> str:
        if not audio_bytes:
            return ""
        return "[transcripcion_mock]"


class MockTTS:
    """TTS mock: guarda un archivo de texto como artefacto de salida."""

    def synthesize(self, text: str, style: str, out_dir: Path = Path("outputs")) -> Path:
        out_dir.mkdir(parents=True, exist_ok=True)
        ts = int(time.time() * 1000)
        file_path = out_dir / f"tts_{ts}.txt"
        file_path.write_text(f"style={style}\ntext={text}\n", encoding="utf-8")
        return file_path


class MockVoiceModulator:
    """Hook de modulación opcional (MMVC/RVC futuro).

    Hoy no transforma audio real; devuelve metadatos de una etapa futura.
    """

    def modulate(self, input_path: Path, character: str) -> dict:
        return {
            "enabled": True,
            "character": character,
            "input_artifact": str(input_path),
            "output_artifact": str(input_path),
            "note": "Mock mode: integrar MMVC/RVC en Fase 5.1",
        }


class VoicePipeline:
    def __init__(self):
        self.stt = MockSTT()
        self.tts = MockTTS()
        self.modulator = MockVoiceModulator()

    def run_text(self, assistant_response: str, cfg: VoiceConfig) -> dict:
        tts_artifact = self.tts.synthesize(assistant_response, style=cfg.tts_style)
        modulation = None

        if cfg.enable_modulation:
            modulation = self.modulator.modulate(tts_artifact, cfg.voice_character)

        return {
            "ok": True,
            "tts_artifact": str(tts_artifact),
            "tts_style": cfg.tts_style,
            "modulation": modulation,
        }
