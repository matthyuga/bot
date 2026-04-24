"""Módulo base de conexión a SQLite para el MVP."""

import sqlite3
from contextlib import contextmanager

DB_PATH = "base_datos.db"


@contextmanager
def get_connection(db_path: str = DB_PATH):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()
