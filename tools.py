"""Herramientas de Fase 1 con validación y persistencia."""

from __future__ import annotations

from db import DB_PATH, execute, fetch_all, init_db


def _validar_limite(limit: int) -> int:
    if not isinstance(limit, int):
        raise ValueError("'limit' debe ser entero")
    if limit < 1 or limit > 100:
        raise ValueError("'limit' debe estar entre 1 y 100")
    return limit


def crear_cliente(nombre: str, db_path: str = DB_PATH) -> dict:
    init_db(db_path)

    if not isinstance(nombre, str) or not nombre.strip():
        return {"ok": False, "error": "Nombre inválido", "tool": "crear_cliente"}

    nombre_limpio = nombre.strip()
    nuevo_id = execute(
        "INSERT INTO clientes (nombre) VALUES (?)",
        (nombre_limpio,),
        db_path=db_path,
    )

    return {
        "ok": True,
        "tool": "crear_cliente",
        "cliente": {"id": nuevo_id, "nombre": nombre_limpio},
    }


def listar_clientes(limit: int = 10, db_path: str = DB_PATH) -> dict:
    init_db(db_path)

    try:
        limite = _validar_limite(limit)
    except ValueError as exc:
        return {"ok": False, "error": str(exc), "tool": "listar_clientes"}

    rows = fetch_all(
        "SELECT id, nombre, fecha_registro FROM clientes ORDER BY id DESC LIMIT ?",
        (limite,),
        db_path=db_path,
    )
    clientes = [dict(r) for r in rows]

    return {"ok": True, "tool": "listar_clientes", "clientes": clientes, "count": len(clientes)}


def registrar_historial(x1: float, x2: float, resultado: float, db_path: str = DB_PATH) -> dict:
    init_db(db_path)

    try:
        x1_f = float(x1)
        x2_f = float(x2)
        res_f = float(resultado)
    except (TypeError, ValueError):
        return {"ok": False, "error": "x1, x2 y resultado deben ser numéricos", "tool": "registrar_historial"}

    nuevo_id = execute(
        "INSERT INTO historial (x1, x2, resultado) VALUES (?, ?, ?)",
        (x1_f, x2_f, res_f),
        db_path=db_path,
    )

    return {
        "ok": True,
        "tool": "registrar_historial",
        "registro": {"id": nuevo_id, "x1": x1_f, "x2": x2_f, "resultado": res_f},
    }


def ver_historial(limit: int = 10, db_path: str = DB_PATH) -> dict:
    init_db(db_path)

    try:
        limite = _validar_limite(limit)
    except ValueError as exc:
        return {"ok": False, "error": str(exc), "tool": "ver_historial"}

    rows = fetch_all(
        "SELECT id, x1, x2, resultado, fecha FROM historial ORDER BY id DESC LIMIT ?",
        (limite,),
        db_path=db_path,
    )
    historial = [dict(r) for r in rows]

    return {"ok": True, "tool": "ver_historial", "historial": historial, "count": len(historial)}
