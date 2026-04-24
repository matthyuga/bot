# Bitácora breve: IA conversacional con voz emocional + MMVCServerSIO

**Fecha:** 2026-04-23  
**Tema:** Viabilidad de una IA que hable con emociones y uso de MMVCServerSIO como modulador de voz.

## 1) Objetivo
Explorar si una IA puede hablar de forma más humana (entonación, ritmo, sorpresa y reacciones) y luego transformar su voz a la de un personaje con `w-okada/voice-changer`.

## 2) Hallazgos principales
- Sí es posible construir la solución.
- Cadena recomendada:
  1. **LLM** (genera contenido e intención),
  2. **TTS expresivo** (voz con emoción/prosodia),
  3. **Voice Changer (MMVC/RVC)** (cambia identidad tímbrica).
- La emoción percibida depende principalmente de la calidad del TTS de entrada.

## 3) Ventajas
- Permite voces de personaje con mayor naturalidad narrativa.
- Arquitectura modular (cada componente se puede reemplazar).
- Se puede orientar a uso en tiempo real con ajustes de latencia.

## 4) Retos técnicos
- Balancear naturalidad y latencia.
- Si el TTS base es plano, el resultado final también lo será en gran medida.
- Ajuste fino de buffer/chunks para evitar artefactos.

## 5) Consideraciones éticas y legales
- Obtener consentimiento para clonar/modular voces reales.
- Evitar suplantación o uso engañoso.
- Revisar licencias de modelos, datasets y voces.

## 6) Próximos pasos
1. Probar pipeline mínimo local con 3–4 emociones base.
2. Medir latencia total y calidad percibida.
3. Crear presets por estilo (neutral, alegre, sorpresa, serio).
4. Documentar configuración reproducible.

## 7) Conclusión
Sí, es viable usar MMVCServerSIO como capa de modulación de voz en una IA conversacional emocional. La clave está en combinar **TTS expresivo de calidad** + **voice changer bien calibrado**.
