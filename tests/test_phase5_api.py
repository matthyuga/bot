import pytest

pytest.importorskip("flask")

from app import app


def test_voice_chat_endpoint_returns_voice_payload():
    client = app.test_client()
    response = client.post(
        "/voice/chat",
        json={
            "message": "ayuda",
            "tts_style": "calm",
            "enable_modulation": True,
            "voice_character": "hero",
        },
    )

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["ok"] is True
    assert payload["voice"]["ok"] is True
    assert payload["voice"]["modulation"]["character"] == "hero"
