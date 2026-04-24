"""Contratos iniciales de herramientas del asistente."""


def crear_cliente(nombre: str) -> dict:
    return {"ok": False, "error": "Not implemented", "tool": "crear_cliente"}


def listar_clientes(limit: int = 10) -> dict:
    return {"ok": False, "error": "Not implemented", "tool": "listar_clientes", "limit": limit}


def registrar_historial(x1: float, x2: float, resultado: float) -> dict:
    return {
        "ok": False,
        "error": "Not implemented",
        "tool": "registrar_historial",
        "x1": x1,
        "x2": x2,
        "resultado": resultado,
    }


def ver_historial(limit: int = 10) -> dict:
    return {"ok": False, "error": "Not implemented", "tool": "ver_historial", "limit": limit}
