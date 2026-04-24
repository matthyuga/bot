#!/usr/bin/env python3
"""Evaluación simple de Fase 3: intención, éxito de tools y latencia."""

from __future__ import annotations

import json
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from db import fetch_all, init_db
from orchestrator import handle_turn

DATASET = Path("data/prompts_eval.jsonl")


def load_dataset(path: Path) -> list[dict]:
    rows: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def main() -> None:
    dataset = load_dataset(DATASET)
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = str(Path(tmpdir) / "eval.db")
        init_db(db_path)

        correct = 0
        tool_turns = 0
        tool_success = 0
        latencies = []

        for row in dataset:
            msg = row["message"]
            expected = row["expected_intent"]

            started = time.perf_counter()
            result = handle_turn(msg, db_path=db_path)
            latencies.append((time.perf_counter() - started) * 1000)

            if result["intent"] == expected:
                correct += 1

            if result.get("tool"):
                tool_turns += 1
                if result.get("ok"):
                    tool_success += 1

        total = len(dataset)
        accuracy = (correct / total) * 100 if total else 0
        avg_latency = sum(latencies) / len(latencies) if latencies else 0

        log_count = fetch_all("SELECT COUNT(*) AS c FROM eventos_chat", db_path=db_path)[0]["c"]
        unhandled = fetch_all("SELECT COUNT(*) AS c FROM eventos_chat WHERE ok = 0", db_path=db_path)[0]["c"]

        print("=== Evaluación Fase 3 ===")
        print(f"Prompts evaluados: {total}")
        print(f"Intent accuracy: {accuracy:.2f}% ({correct}/{total})")
        print(f"Tool success rate: {(tool_success / tool_turns * 100) if tool_turns else 0:.2f}% ({tool_success}/{tool_turns})")
        print(f"Latencia promedio: {avg_latency:.2f} ms")
        print(f"Eventos logueados: {log_count}")
        print(f"Turnos no exitosos (ok=0): {unhandled}")


if __name__ == "__main__":
    main()
