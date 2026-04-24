from pathlib import Path

from db import init_db
from tools import crear_cliente, listar_clientes, registrar_historial, ver_historial


def test_crear_y_listar_clientes(tmp_path: Path):
    db_path = str(tmp_path / "fase1.db")
    init_db(db_path)

    r1 = crear_cliente("Ana", db_path=db_path)
    assert r1["ok"] is True

    r2 = listar_clientes(limit=10, db_path=db_path)
    assert r2["ok"] is True
    assert r2["count"] == 1
    assert r2["clientes"][0]["nombre"] == "Ana"


def test_registrar_y_ver_historial(tmp_path: Path):
    db_path = str(tmp_path / "fase1.db")
    init_db(db_path)

    r1 = registrar_historial(1, 2, 3, db_path=db_path)
    assert r1["ok"] is True

    r2 = ver_historial(limit=5, db_path=db_path)
    assert r2["ok"] is True
    assert r2["count"] == 1
    assert r2["historial"][0]["resultado"] == 3.0


def test_validaciones_de_tools(tmp_path: Path):
    db_path = str(tmp_path / "fase1.db")
    init_db(db_path)

    bad_name = crear_cliente("   ", db_path=db_path)
    assert bad_name["ok"] is False

    bad_limit = listar_clientes(limit=0, db_path=db_path)
    assert bad_limit["ok"] is False

    bad_hist = registrar_historial("a", 1, 2, db_path=db_path)
    assert bad_hist["ok"] is False
