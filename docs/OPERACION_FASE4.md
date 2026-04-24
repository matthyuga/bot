# Operación Fase 4 (hardening + demo)

## Objetivo
Dejar el MVP en estado demostrable con mejor manejo de errores, trazabilidad y guía operativa.

## Mejoras aplicadas
- `orchestrator.py` con:
  - `error_code` en respuestas,
  - `try/except` para evitar caídas por errores inesperados,
  - logging de excepciones,
  - intento de logging de evento incluso si hubo fallo en ejecución.
- `app.py` con:
  - manejo de errores en `/chat` y `/metrics`,
  - códigos HTTP coherentes (`200/400/500`),
  - `elapsed_ms` por turno,
  - configuración de logging con timestamp y nivel.
- scripts operativos:
  - `scripts/init_db.py` para inicializar DB,
  - `scripts/demo_fase4.sh` para demo guiada por endpoint.

## Runbook rápido
1. Inicializar DB:
   ```bash
   python3 scripts/init_db.py
   ```
2. Levantar servidor:
   ```bash
   ./run.sh
   ```
3. Ejecutar demo (en otra terminal):
   ```bash
   ./scripts/demo_fase4.sh
   ```

## Escenarios demo sugeridos
1. `ayuda`
2. `crear cliente Ana`
3. `listar clientes 5`
4. `registrar historial 1 2 3`
5. `ver historial 5`
6. `mensaje no reconocido`
7. consultar `/metrics`

## Señales de calidad esperadas
- No hay crash del servicio ante entradas inválidas.
- Siempre hay `response` y `error_code` cuando `ok=false`.
- `eventos_chat` crece por cada turno procesado.
- `/metrics` responde agregados incluso con bajo volumen.
