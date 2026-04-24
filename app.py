import logging
import time

from flask import Flask, jsonify, render_template, request

from db import DB_PATH, fetch_all, init_db
from orchestrator import handle_turn

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/health")
def health():
    return {"ok": True, "service": "assistant-mvp"}


@app.post("/chat")
def chat():
    payload = request.get_json(silent=True) or {}
    user_input = str(payload.get("message", "")).strip()

    started = time.perf_counter()
    try:
        result = handle_turn(user_input)
        status = 200 if result.get("ok", False) else 400
    except Exception:
        logger.exception("Fallo crítico en endpoint /chat")
        result = {
            "ok": False,
            "intent": "fallback",
            "tool": None,
            "tool_result": {},
            "response": "Error crítico del servicio.",
            "error_code": "CHAT_ENDPOINT_ERROR",
        }
        status = 500

    elapsed_ms = round((time.perf_counter() - started) * 1000, 2)
    return jsonify({**result, "elapsed_ms": elapsed_ms}), status


@app.get("/metrics")
def metrics():
    try:
        init_db(DB_PATH)

        total_rows = fetch_all("SELECT COUNT(*) AS total FROM eventos_chat", db_path=DB_PATH)[0]["total"]
        ok_rows = fetch_all("SELECT COUNT(*) AS ok_count FROM eventos_chat WHERE ok = 1", db_path=DB_PATH)[0][
            "ok_count"
        ]
        by_intent = [
            dict(row)
            for row in fetch_all(
                "SELECT intent, COUNT(*) AS count FROM eventos_chat GROUP BY intent ORDER BY count DESC",
                db_path=DB_PATH,
            )
        ]

        return {
            "ok": True,
            "total_turnos": total_rows,
            "turnos_exitosos": ok_rows,
            "tasa_exito": round((ok_rows / total_rows) * 100, 2) if total_rows else 0.0,
            "por_intent": by_intent,
        }
    except Exception:
        logger.exception("Error generando métricas")
        return {
            "ok": False,
            "error": "No se pudieron generar métricas",
            "error_code": "METRICS_ERROR",
        }, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
