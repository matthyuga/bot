#!/usr/bin/env python3
"""Inicializa base de datos local para operación/demo."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from db import DB_PATH, init_db

if __name__ == "__main__":
    init_db(DB_PATH)
    print(f"DB inicializada en {DB_PATH}")
