# Plan técnico MVP: Asistente IA con herramientas y contexto

## 1) Objetivo del MVP (4 semanas)
Construir un asistente que:
- entienda mensajes de usuario,
- detecte intención,
- use herramientas internas (SQLite),
- responda con contexto,
- y deje trazabilidad para mejorar iterativamente.

> Alcance MVP: texto primero. Voz opcional en fase posterior.

---

## 2) Casos de uso iniciales (solo 3)
Para mantener foco y medir avance:
1. **Registrar cliente** (`nombre`).
2. **Consultar historial** reciente.
3. **Registrar operación** (`x1`, `x2`, `resultado`) y devolver confirmación.

Criterio: cada caso debe poder ejecutarse desde chat y quedar guardado en DB.

---

## 3) Arquitectura propuesta

```text
[Frontend Flask]
   -> [API /chat]
      -> [Orquestador]
          -> [Clasificador de intención]
          -> [Router de herramientas]
              -> [Tool: DB clientes]
              -> [Tool: DB historial]
          -> [Generador de respuesta]
      -> [Logs / trazas]
```

### Componentes
- **Frontend Flask**: formulario o chat básico.
- **Orquestador**: decide flujo de ejecución por turno.
- **Clasificador de intención**: regla inicial + expansión futura.
- **Tools**: funciones explícitas con input/output tipado.
- **DB SQLite**: persistencia.
- **Logger**: auditoría de entradas, acciones y resultados.

---

## 4) Estructura de proyecto recomendada

```text
project/
  app.py
  requirements.txt
  db/
    schema.sql
    db.py
  ai/
    intents.py
    orchestrator.py
    response.py
    tools.py
  templates/
    index.html
  tests/
    test_tools.py
    test_intents.py
  docs/
    PLAN_TECNICO_MVP_ASISTENTE_IA.md
```

---

## 5) Esquema SQL mínimo

```sql
CREATE TABLE IF NOT EXISTS clientes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS historial (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  x1 REAL,
  x2 REAL,
  resultado REAL,
  fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS eventos_chat (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_input TEXT,
  intent TEXT,
  tool_name TEXT,
  tool_args TEXT,
  tool_result TEXT,
  respuesta TEXT,
  ok INTEGER,
  fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 6) Contratos de herramientas (tool calling local)

Definir cada herramienta como función pura con contrato estricto.

### `crear_cliente(nombre: str) -> dict`
- valida nombre,
- inserta en DB,
- retorna `{ok, cliente_id, nombre}`.

### `listar_clientes(limit: int) -> dict`
- retorna lista acotada.

### `registrar_historial(x1: float, x2: float, resultado: float) -> dict`
- inserta operación,
- retorna confirmación.

### `ver_historial(limit: int) -> dict`
- retorna operaciones recientes.

Regla: **si falla validación, no toca DB** y responde error estructurado.

---

## 7) Pipeline de un turno de chat

1. Recibir `user_input`.
2. Detectar intención (primero con reglas).
3. Si requiere herramienta:
   - parsear argumentos,
   - validar,
   - ejecutar tool,
   - registrar traza.
4. Generar respuesta final en lenguaje natural.
5. Guardar evento en `eventos_chat`.

---

## 8) Clasificación de intención (versión MVP)

Intenciones iniciales:
- `saludo`
- `crear_cliente`
- `listar_clientes`
- `registrar_historial`
- `ver_historial`
- `ayuda`
- `fallback`

Implementación inicial:
- reglas por palabras clave + regex,
- fallback seguro si no hay confianza.

Evolución:
- reemplazar por clasificador ML/LLM cuando tengan dataset real.

---

## 9) Seguridad y control operativo

- Validar tipos/rangos en todas las tools.
- Limitar tamaño de texto de entrada.
- Sanitizar salidas para UI.
- Añadir `timeout` y manejo de errores controlado.
- Registrar `ok/error` por evento para observabilidad.

---

## 10) Métricas de aceptación del MVP

- **Intent accuracy (manual)**: >= 80% en set pequeño de pruebas.
- **Tool success rate**: >= 95% en casos válidos.
- **Errores no controlados**: 0 en pruebas básicas.
- **Latencia media**: < 1s por turno en local (sin LLM remoto).

---

## 11) Plan de trabajo por semanas

## Semana 1 — Base estable
- crear estructura de carpetas,
- schema + módulo DB,
- tools CRUD básicas,
- tests unitarios de tools.

**Entregable:** DB + tools funcionando por terminal.

## Semana 2 — Orquestador
- clasificador por reglas,
- router de intención->tool,
- endpoint `/chat` en Flask,
- logging en `eventos_chat`.

**Entregable:** chat textual con acciones en DB.

## Semana 3 — Calidad
- validaciones robustas,
- respuestas más claras,
- tests de flujos completos,
- dataset de 100 prompts para evaluación manual.

**Entregable:** MVP usable por el equipo.

## Semana 4 — Hardening + demo
- métricas y correcciones,
- documentación de operación,
- script de inicialización,
- demo con casos reales.

**Entregable:** versión `v0.1` demostrable.

---

## 12) Backlog post-MVP

1. Sustituir clasificador por modelo ML/LLM.
2. Memoria de largo plazo por usuario.
3. Motor de planificación multi-paso.
4. Integración de voz (STT/TTS).
5. Voz expresiva + modulador (MMVC/RVC) como capa final.

---

## 13) Checklist técnico de arranque (hoy)

- [ ] Crear estructura de carpetas propuesta.
- [ ] Migrar SQL a `db/schema.sql`.
- [ ] Implementar `db.py` con conexión segura.
- [ ] Crear `tools.py` con contratos definidos.
- [ ] Crear `intents.py` por reglas.
- [ ] Implementar `orchestrator.py`.
- [ ] Exponer endpoint Flask `/chat`.
- [ ] Registrar todos los eventos en `eventos_chat`.
- [ ] Agregar pruebas mínimas (`pytest`).
- [ ] Preparar guía de ejecución local.

---

## 14) Definición de éxito

El MVP se considera exitoso si cualquier miembro del equipo puede:
1. levantar el proyecto en local,
2. enviar mensajes al chat,
3. ejecutar al menos 3 tareas con herramientas,
4. y auditar cada paso en la base de datos.
