# Guía por fases: implementación de un asistente IA (para equipo principiante)

## Objetivo
Entregar una ruta práctica para que el equipo implemente un asistente IA por etapas, con entregables claros y tareas que puedan realizar por su cuenta.

---

## Fase 0 — Preparación (1-2 días)

### Meta
Dejar entorno y base del proyecto listos.

### Tareas
- [ ] Crear repositorio y estructura inicial:
  - `app.py`, `db.py`, `tools.py`, `orchestrator.py`, `intents.py`, `templates/index.html`, `tests/`.
- [ ] Crear `requirements.txt` con dependencias mínimas (`flask`, `pytest`).
- [ ] Definir normas del equipo:
  - convención de nombres,
  - formato de commits,
  - definición de “hecho”.
- [ ] Crear script de arranque local (`run.sh` o instrucciones README).

### Entregable
Proyecto levanta en local sin errores, aunque todavía sin lógica completa.

---

## Fase 1 — Datos y herramientas base (Semana 1)

### Meta
Tener persistencia estable y herramientas funcionales.

### Tareas
- [ ] Crear esquema SQL:
  - `clientes`,
  - `historial`,
  - `eventos_chat`.
- [ ] Implementar módulo `db.py`:
  - conexión,
  - ejecución segura,
  - manejo de errores.
- [ ] Implementar tools con contratos claros:
  - `crear_cliente(nombre)`
  - `listar_clientes(limit)`
  - `registrar_historial(x1, x2, resultado)`
  - `ver_historial(limit)`
- [ ] Validar entradas (tipos/rangos) antes de tocar DB.
- [ ] Añadir tests de tools (casos exitosos + errores).

### Entregable
Tools funcionan desde terminal y los tests básicos pasan.

---

## Fase 2 — Cerebro de decisión (Semana 2)

### Meta
Que el sistema entienda intención y elija herramienta.

### Tareas
- [ ] Implementar `intents.py` por reglas:
  - saludo,
  - crear_cliente,
  - listar_clientes,
  - registrar_historial,
  - ver_historial,
  - ayuda,
  - fallback.
- [ ] Implementar `orchestrator.py`:
  - recibe texto,
  - detecta intención,
  - parsea argumentos,
  - llama tool,
  - genera respuesta textual.
- [ ] Guardar trazas en `eventos_chat` por cada turno.
- [ ] Manejar errores sin romper flujo (siempre responder algo útil).

### Entregable
Un flujo completo de chat textual con ejecución de tools y registro de eventos.

---

## Fase 3 — Interfaz usable y evaluación (Semana 3)

### Meta
Convertir el sistema en MVP utilizable por el equipo.

### Tareas
- [ ] Crear interfaz Flask sencilla para chat.
- [ ] Mostrar respuesta, intención detectada y estado de ejecución.
- [ ] Armar dataset manual de 100 prompts.
- [ ] Medir:
  - precisión de intención,
  - éxito de tools,
  - errores no controlados,
  - latencia promedio.
- [ ] Corregir los 10 errores más frecuentes.

### Entregable
MVP usable por personas no técnicas del equipo.

---

## Fase 4 — Endurecimiento y demo (Semana 4)

### Meta
Dejar una versión presentable y reproducible.

### Tareas
- [ ] Mejorar mensajes de error y confirmación.
- [ ] Añadir logs más claros para depuración.
- [ ] Documentar instalación/ejecución paso a paso.
- [ ] Crear guion de demo con 5 escenarios reales.
- [ ] Congelar versión `v0.1`.

### Entregable
Demo estable + documentación para que cualquiera del equipo la ejecute.

---

## Fase 5 (Opcional) — Voz y expresividad

### Meta
Agregar entrada/salida de voz y modular identidad vocal.

### Tareas
- [ ] Integrar STT (voz a texto).
- [ ] Integrar TTS (texto a voz).
- [ ] Medir latencia total de pipeline.
- [ ] Opcional: modular voz con MMVC/RVC.
- [ ] Definir límites éticos y de consentimiento para voces.

### Entregable
Asistente con voz funcional y criterios de uso responsables.

---

## Reparto recomendado del equipo

- **Rol A (Backend/DB):** `db.py`, SQL, tools.
- **Rol B (IA lógica):** intents + orchestrator.
- **Rol C (Frontend):** Flask + interfaz.
- **Rol D (QA):** pruebas, métricas, bugs.
- **Rol E (PM/Docs):** coordinación, roadmap, decisiones.

> Si son menos personas, combinen roles A+B o C+D.

---

## Métricas mínimas para decidir “seguimos o no”

- Precisión de intención >= 80%.
- Éxito de tools >= 95% en casos válidos.
- Errores no controlados = 0.
- Latencia promedio por turno < 1s (sin llamadas externas).

Si no se cumple una métrica, no pasar de fase hasta resolver.

---

## Qué pueden hacer ustedes por su lado (paralelo)

Mientras se implementa el núcleo, pueden avanzar en paralelo con:
- [ ] Recolectar prompts reales de uso.
- [ ] Definir tono/persona del asistente.
- [ ] Diseñar reglas de seguridad y casos prohibidos.
- [ ] Preparar dataset para futura mejora del clasificador.
- [ ] Escribir ejemplos de conversación “ideal”.

---

## Checklist de inicio inmediato (hoy)

- [ ] Crear issues por fase.
- [ ] Asignar responsables y fecha por issue.
- [ ] Completar Fase 0 en 48 horas.
- [ ] Revisión técnica grupal al cierre de cada semana.
- [ ] Demo corta interna cada viernes.

---

## Definición de éxito del plan

El plan funciona si en 4 semanas su equipo logra:
1. un asistente textual estable,
2. que use herramientas reales,
3. con trazabilidad en base de datos,
4. y con mejoras guiadas por métricas.
