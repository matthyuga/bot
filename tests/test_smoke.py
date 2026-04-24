import pytest

pytest.importorskip("flask")

from app import app


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["ok"] is True


def test_chat_endpoint_works():
    client = app.test_client()
    response = client.post("/chat", json={"message": "ayuda"})

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["intent"] == "ayuda"
    assert "Comandos disponibles" in payload["response"]
