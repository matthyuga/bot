"""Orquestador Fase 4: intención -> tool -> respuesta + logging robusto."""

from __future__ import annotations

import json
import logging
import re
from typing import Any

from db import DB_PATH, execute, init_db
from intents import detect_intent
from tools import crear_cliente, listar_clientes, registrar_historial, ver_historial

logger = logging.getLogger(__name__)

HELP_TEXT = (
    "Comandos disponibles:\n"
    "- crear cliente <nombre>\n"
    "- listar clientes [limit]\n"
    "- registrar historial <x1> <x2> <resultado>\n"
    "- ver historial [limit]"
)


def _parse_int(text: str, default: int = 10) -> int:
    matches = re.findall(r"-?\d+", text)
    return int(matches[0]) if matches else default


def _parse_floats(text: str) -> list[float]:
    matches = re.findall(r"-?\d+(?:\.\d+)?", text)
    return [float(m) for m in matches]


def _parse_nombre(text: str) -> str:
    cleaned = text.strip()
    if "cliente" in cleaned.lower():
        parts = re.split(r"cliente", cleaned, flags=re.IGNORECASE, maxsplit=1)
        cleaned = parts[1].strip() if len(parts) > 1 else cleaned
    return cleaned


def _log_event(
    *,
    user_input: str,
    intent: str,
    tool_name: str | None,
    tool_args: dict[str, Any] | None,
    tool_result: dict[str, Any] | None,
    respuesta: str,
    ok: bool,
    db_path: str,
) -> None:
    init_db(db_path)
    execute(
        """
        INSERT INTO eventos_chat (user_input, intent, tool_name, tool_args, tool_result, respuesta, ok)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            user_input,
            intent,
            tool_name,
            json.dumps(tool_args or {}, ensure_ascii=False),
            json.dumps(tool_result or {}, ensure_ascii=False),
            respuesta,
            int(ok),
        ),
        db_path=db_path,
    )


def handle_turn(user_input: str, db_path: str = DB_PATH) -> dict:
    text = (user_input or "").strip()
    intent = detect_intent(text)
    tool_name = None
    tool_args: dict[str, Any] = {}
    tool_result: dict[str, Any] = {}
    respuesta = "No entendí tu solicitud. Escribe 'ayuda' para ver comandos."
    ok = True
    error_code: str | None = None

    try:
        if intent == "saludo":
            respuesta = "¡Hola! Ya estoy en Fase 4: más robusto y con métricas. Escribe 'ayuda'."

        elif intent == "ayuda":
            respuesta = HELP_TEXT

        elif intent == "crear_cliente":
            tool_name = "crear_cliente"
            nombre = _parse_nombre(text)
            tool_args = {"nombre": nombre}
            tool_result = crear_cliente(nombre, db_path=db_path)
            ok = bool(tool_result.get("ok"))
            if ok:
                cliente = tool_result["cliente"]
                respuesta = f"Cliente creado: #{cliente['id']} - {cliente['nombre']}"
            else:
                error_code = "VALIDATION_ERROR"
                respuesta = f"No pude crear cliente: {tool_result.get('error')}"

        elif intent == "listar_clientes":
            tool_name = "listar_clientes"
            limit = _parse_int(text, default=10)
            tool_args = {"limit": limit}
            tool_result = listar_clientes(limit=limit, db_path=db_path)
            ok = bool(tool_result.get("ok"))
            if ok:
                clientes = tool_result["clientes"]
                if not clientes:
                    respuesta = "No hay clientes registrados."
                else:
                    preview = ", ".join(f"#{c['id']} {c['nombre']}" for c in clientes[:5])
                    respuesta = f"Clientes ({tool_result['count']}): {preview}"
            else:
                error_code = "VALIDATION_ERROR"
                respuesta = f"Error al listar clientes: {tool_result.get('error')}"

        elif intent == "registrar_historial":
            tool_name = "registrar_historial"
            vals = _parse_floats(text)
            if len(vals) >= 3:
                x1, x2, resultado = vals[0], vals[1], vals[2]
                tool_args = {"x1": x1, "x2": x2, "resultado": resultado}
                tool_result = registrar_historial(x1, x2, resultado, db_path=db_path)
                ok = bool(tool_result.get("ok"))
                if ok:
                    reg = tool_result["registro"]
                    respuesta = (
                        f"Historial guardado: #{reg['id']} -> "
                        f"x1={reg['x1']}, x2={reg['x2']}, resultado={reg['resultado']}"
                    )
                else:
                    error_code = "VALIDATION_ERROR"
                    respuesta = f"Error al registrar historial: {tool_result.get('error')}"
            else:
                ok = False
                error_code = "BAD_ARGUMENTS"
                tool_args = {"raw": text}
                tool_result = {"ok": False, "error": "Debes enviar 3 números: x1 x2 resultado"}
                respuesta = tool_result["error"]

        elif intent == "ver_historial":
            tool_name = "ver_historial"
            limit = _parse_int(text, default=10)
            tool_args = {"limit": limit}
            tool_result = ver_historial(limit=limit, db_path=db_path)
            ok = bool(tool_result.get("ok"))
            if ok:
                historial = tool_result["historial"]
                if not historial:
                    respuesta = "No hay operaciones en historial."
                else:
                    preview = ", ".join(
                        f"#{h['id']}({h['x1']},{h['x2']}=>{h['resultado']})" for h in historial[:5]
                    )
                    respuesta = f"Historial ({tool_result['count']}): {preview}"
            else:
                error_code = "VALIDATION_ERROR"
                respuesta = f"Error al ver historial: {tool_result.get('error')}"

        else:
            ok = False
            error_code = "UNKNOWN_INTENT"

    except Exception as exc:  # hardening fase 4
        ok = False
        error_code = "INTERNAL_ERROR"
        tool_result = {"ok": False, "error": str(exc)}
        respuesta = "Ocurrió un error interno procesando tu solicitud."
        logger.exception("Error no controlado en handle_turn", extra={"user_input": text, "intent": intent})

    try:
        _log_event(
            user_input=text,
            intent=intent,
            tool_name=tool_name,
            tool_args=tool_args,
            tool_result=tool_result,
            respuesta=respuesta,
            ok=ok,
            db_path=db_path,
        )
    except Exception:
        logger.exception("No se pudo registrar evento en eventos_chat")

    return {
        "ok": ok,
        "intent": intent,
        "tool": tool_name,
        "tool_result": tool_result,
        "response": respuesta,
        "error_code": error_code,
    }
