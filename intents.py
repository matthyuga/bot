"""Detección básica de intención (placeholder de Fase 2)."""


def detect_intent(user_input: str) -> str:
    text = (user_input or "").strip().lower()
    if not text:
        return "fallback"
    if any(k in text for k in ("hola", "buenas", "hey")):
        return "saludo"
    return "fallback"
