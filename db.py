"""Módulo de persistencia SQLite para Fase 1."""

from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterable

DB_PATH = "base_datos.db"
SCHEMA_PATH = Path("db/schema.sql")


@contextmanager
def get_connection(db_path: str = DB_PATH):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


def _read_schema(schema_path: Path = SCHEMA_PATH) -> str:
    return schema_path.read_text(encoding="utf-8")


def init_db(db_path: str = DB_PATH, schema_path: Path = SCHEMA_PATH) -> None:
    schema_sql = _read_schema(schema_path)
    with get_connection(db_path) as conn:
        conn.executescript(schema_sql)
        conn.commit()


def fetch_all(query: str, params: Iterable | tuple = (), db_path: str = DB_PATH) -> list[sqlite3.Row]:
    with get_connection(db_path) as conn:
        cur = conn.execute(query, tuple(params))
        return cur.fetchall()


def execute(query: str, params: Iterable | tuple = (), db_path: str = DB_PATH) -> int:
    with get_connection(db_path) as conn:
        cur = conn.execute(query, tuple(params))
        conn.commit()
        return int(cur.lastrowid or 0)
