from pathlib import Path

from db import fetch_all, init_db
from orchestrator import handle_turn


def test_handle_turn_crear_cliente(tmp_path: Path):
    db_path = str(tmp_path / "fase2.db")
    init_db(db_path)

    result = handle_turn("crear cliente Ana", db_path=db_path)

    assert result["ok"] is True
    assert result["intent"] == "crear_cliente"
    assert "Cliente creado" in result["response"]

    rows = fetch_all("SELECT nombre FROM clientes", db_path=db_path)
    assert len(rows) == 1
    assert rows[0]["nombre"] == "Ana"


def test_handle_turn_historial_y_logging(tmp_path: Path):
    db_path = str(tmp_path / "fase2.db")
    init_db(db_path)

    r1 = handle_turn("registrar historial 1 2 3", db_path=db_path)
    assert r1["ok"] is True

    r2 = handle_turn("ver historial 5", db_path=db_path)
    assert r2["ok"] is True
    assert r2["intent"] == "ver_historial"

    logs = fetch_all("SELECT intent, ok FROM eventos_chat ORDER BY id", db_path=db_path)
    assert len(logs) == 2
    assert logs[0]["intent"] == "registrar_historial"
    assert logs[1]["intent"] == "ver_historial"
