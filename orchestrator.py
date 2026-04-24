"""Orquestador mínimo para enrutar intención (placeholder de Fase 2)."""

from intents import detect_intent


def handle_turn(user_input: str) -> dict:
    intent = detect_intent(user_input)
    if intent == "saludo":
        return {"ok": True, "intent": intent, "response": "¡Hola! Estoy en fase de inicialización."}
    return {"ok": True, "intent": "fallback", "response": "Aún no tengo tools activas. Seguimos en Fase 0."}
