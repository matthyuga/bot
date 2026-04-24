# Panorama general de los códigos: fundamentos de IA para iniciados

## ¿Qué nos pasó con estos códigos?
En los fragmentos compartidos aparecen **tres temas mezclados** que sí tienen relación entre sí:

1. **Base de datos (SQLite)** para guardar información.
2. **Modelo de aprendizaje** (perceptrón o red neuronal simple) para predecir salidas.
3. **Aplicación web (Flask)** para interactuar con el modelo desde un formulario.

La idea del proyecto es buena: construir una mini IA educativa. El reto principal fue que algunos scripts venían con errores de sintaxis y mezcla de enfoques.

---

## Mapa general (arquitectura mental)

```text
Usuario -> Formulario web (Flask) -> Modelo (Perceptrón/Red) -> Respuesta
                                \-> Base de datos (SQLite) para guardar/leer datos
```

- **Flask**: interfaz para capturar entradas (`x1`, `x2`).
- **Modelo**: calcula una salida (`0` o `1`, por ejemplo).
- **SQLite**: permite guardar historial y clientes para entrenar/mejorar después.

---

## Tema 1: Base de datos (SQLite)

### Qué hace
- Crea archivo `base_datos.db`.
- Crea tablas como `clientes` e `historial`.
- Permite guardar ejemplos para entrenamiento.

### Por qué importa en IA
Un modelo aprende de datos. Sin datos, no hay aprendizaje útil.

### Buenas prácticas sugeridas
- Validar conexión antes de cerrar (`conn` puede no existir si falla temprano).
- Guardar datos en tabla `historial` con estructura clara (`x1`, `x2`, `resultado`, `fecha`).
- Agregar más ejemplos reales antes de entrenar.

---

## Tema 2: Perceptrón (neurona única)

### Qué es
Un modelo básico que decide con una frontera lineal.

### Estructura típica
- Entradas: `x1`, `x2`
- Parámetros: `pesos`, `bias`
- Regla:
  - `z = dot(pesos, entrada) + bias`
  - salida = `1` si `z >= 0`, si no `0`

### Qué aprende bien
- Problemas lineales como **AND** y **OR**.

### Limitación
- No aprende **XOR** con una sola neurona.

---

## Tema 3: Red neuronal multicapa (MLP)

### Qué es
Una extensión del perceptrón: varias capas con activaciones (ej. sigmoide).

### Ventaja
- Puede modelar patrones no lineales.

### Problemas detectados en los códigos compartidos
- Variables mal escritas (`nentradas` vs `n_entradas`).
- Bucles incompletos (`for  in range(...)`).
- Indentación rota.
- Entrenamiento incompleto (solo actualizaba la última capa `W3`, faltaba retropropagación completa para `W1/W2`).

---

## Tema 4: Flask como interfaz educativa

### Qué aporta
- Permite probar entradas manuales y ver resultados rápido.
- Hace visible el valor interno `z`, pesos y bias.

### Recomendación
Separar en archivos:
- `app.py` (rutas web)
- `model.py` (entrenamiento/predicción)
- `db.py` (base de datos)
- `templates/index.html` (interfaz)

Esto evita mezclar código y reduce errores.

---

## ¿Cómo se relaciona todo para crear una IA asistente?

1. **Recolectar datos** (SQLite).
2. **Entrenar modelo** (perceptrón/MLP/otro).
3. **Exponer interacción** (Flask/API).
4. **Evaluar y mejorar** con nuevos datos.

Para un asistente real moderno, además se suma:
- NLP/LLM para lenguaje natural.
- Memoria y herramientas.
- Voz (STT/TTS) si quieren interacción hablada.

---

## Ruta de aprendizaje recomendada para su grupo

### Nivel 1 (fundamentos)
- Entender álgebra básica: vectores, matrices, producto punto.
- Implementar perceptrón para AND/OR.
- Medir precisión.

### Nivel 2 (redes simples)
- Implementar MLP de 1–2 capas con backprop completo.
- Probar XOR.
- Comparar resultados con perceptrón.

### Nivel 3 (aplicación)
- Integrar Flask + SQLite + modelo.
- Guardar historial de predicciones.
- Reentrenar periódicamente.

### Nivel 4 (asistente IA)
- Añadir pipeline de lenguaje (LLM + herramientas).
- Agregar voz si el proyecto lo requiere.

---

## Glosario breve
- **Feature (entrada)**: dato usado para predecir (`x1`, `x2`).
- **Label/target (salida esperada)**: resultado correcto (`y`).
- **Peso (`W`)**: importancia de cada entrada.
- **Bias (`b`)**: ajuste extra de la neurona.
- **Época**: una pasada completa por los datos de entrenamiento.
- **Learning rate (`lr`)**: tamaño de cada ajuste durante entrenamiento.
- **Backpropagation**: método para ajustar pesos en capas internas.

---

## Conclusión
Sus códigos sí tienen un hilo lógico: **datos + aprendizaje + interfaz**. Eso ya es una base real para aprender IA. La mejora clave es ordenar el proyecto y corregir errores de implementación para que el entrenamiento sea consistente y reproducible.
