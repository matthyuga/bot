from pathlib import Path

from voice_pipeline import VoiceConfig, VoicePipeline


def test_voice_pipeline_tts_artifact_creation(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    pipeline = VoicePipeline()

    result = pipeline.run_text("hola", VoiceConfig(tts_style="calm", enable_modulation=False))

    assert result["ok"] is True
    artifact = Path(result["tts_artifact"])
    assert artifact.exists()
    assert "style=calm" in artifact.read_text(encoding="utf-8")


def test_voice_pipeline_with_modulation(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    pipeline = VoicePipeline()

    result = pipeline.run_text(
        "hola",
        VoiceConfig(tts_style="energetic", enable_modulation=True, voice_character="hero"),
    )

    assert result["ok"] is True
    assert result["modulation"] is not None
    assert result["modulation"]["character"] == "hero"
