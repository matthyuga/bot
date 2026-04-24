"""Clasificador de intención por reglas para Fase 2."""

from __future__ import annotations


INTENTS = {
    "saludo": ("hola", "buenas", "hey", "saludos"),
    "crear_cliente": ("crear cliente", "registrar cliente", "nuevo cliente"),
    "listar_clientes": ("listar clientes", "ver clientes", "mostrar clientes"),
    "registrar_historial": ("registrar historial", "guardar operacion", "guardar operación"),
    "ver_historial": ("ver historial", "mostrar historial", "listar historial"),
    "ayuda": ("ayuda", "comandos", "que puedes hacer", "qué puedes hacer"),
}


def detect_intent(user_input: str) -> str:
    text = (user_input or "").strip().lower()
    if not text:
        return "fallback"

    for intent, keywords in INTENTS.items():
        if any(keyword in text for keyword in keywords):
            return intent

    return "fallback"
