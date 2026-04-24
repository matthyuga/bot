import pytest

pytest.importorskip("flask")

from app import app


def test_metrics_endpoint_shape():
    client = app.test_client()

    # seed one turn
    client.post("/chat", json={"message": "ayuda"})

    response = client.get("/metrics")
    assert response.status_code == 200
    payload = response.get_json()

    assert payload["ok"] is True
    assert "total_turnos" in payload
    assert "tasa_exito" in payload
    assert isinstance(payload["por_intent"], list)
