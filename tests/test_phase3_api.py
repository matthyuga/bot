import pytest

pytest.importorskip("flask")

from app import app


def test_metrics_endpoint_shape():
    client = app.test_client()

    client.post("/chat", json={"message": "ayuda"})

    response = client.get("/metrics")
    assert response.status_code == 200
    payload = response.get_json()

    assert payload["ok"] is True
    assert "total_turnos" in payload
    assert "tasa_exito" in payload
    assert isinstance(payload["por_intent"], list)


def test_chat_unknown_intent_returns_400():
    client = app.test_client()
    response = client.post("/chat", json={"message": "bla bla sin comando"})

    assert response.status_code == 400
    payload = response.get_json()
    assert payload["ok"] is False
    assert payload["error_code"] == "UNKNOWN_INTENT"
