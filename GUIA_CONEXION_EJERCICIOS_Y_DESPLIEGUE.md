# Guía de Conexión: De los Ejercicios al Despliegue

## ¿Estás Confundido? ¡Es Normal!

Este documento te explica cómo se conectan **los ejercicios del proyecto**, **el manual de despliegue** y **la presentación PowerPoint**. Si sientes que hay muchos pasos o que no entiendes por qué tantos ejercicios, **estás en el lugar correcto**.

---

## La Gran Imagen: Dos Caminos Complementarios

Tu proyecto tiene **DOS caminos de aprendizaje** que se complementan:

### 📚 **Camino 1: Los Fundamentos (analisis_sentimientos_basico/)**

**Propósito:** Entender NLP desde cero

Los 5 ejercicios básicos (01-05) te enseñan la teoría fundamental:
- ¿Qué es tokenización?
- ¿Cómo funciona el análisis de sentimientos?
- ¿Qué son los vectores TF-IDF?

**Estado:** ✅ **ESTOS ESTÁN COMPLETOS Y FUNCIONAN**

**Relación con el manual:** Ninguna directa. Son la base teórica.

---

### 🏗️ **Camino 2: Del Script al Servicio (ejercicios 1.1 - 5.3)**

**Propósito:** Construir un sistema de análisis financiero completo y desplegarlo en producción

Este es el camino que documenta el **MANUAL_DESARROLLO_Y_DESPLIEGUE.md** y la presentación PowerPoint.

**Estado:** 🚧 **ESTOS SON PLANTILLAS (TODOs) - TÚ LOS COMPLETAS**

---

## ¿Cómo se Conecta Todo? El Viaje Completo

Imagina que estás construyendo un servicio web de análisis financiero. Este es el viaje:

```
FASE 1: RECOLECCIÓN        FASE 2: ANÁLISIS         FASE 3: SERVICIO
    DE DATOS                 INTELIGENTE              WEB

┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│  Ejercicio 2.1  │──────│  Ejercicio 3.1  │──────│  Ejercicio 5.1  │
│  Cliente API    │      │  Sentiment con  │      │  API REST con   │
│  (Alpha Vantage)│      │  Transformers   │      │  FastAPI        │
└─────────────────┘      └─────────────────┘      └─────────────────┘
        │                        │                        │
        ▼                        ▼                        ▼
  Obtener datos          Analizar texto             Exponer el
  financieros            con modelos IA             sistema como
  en tiempo real                                    servicio web

                                                          │
                                                          ▼
                                               ┌─────────────────────┐
                                               │   Ejercicio 5.2     │
                                               │   Dockerización     │
                                               │   (Despliegue)      │
                                               └─────────────────────┘
```

---

## Desglose Detallado: ¿Qué Hace Cada Ejercicio?

### 🟦 **MÓDULO 1: Python Avanzado (Fundamentos Técnicos)**

**¿De qué va?** Aprender técnicas modernas de Python que usarás en TODO el proyecto.

#### Ejercicio 1.1: `ejercicio_1_1.py` - Configuración con IA
**Objetivo:** Usar APIs de IA (Gemini) para automatizar tareas
**Relación con el viaje:** Aprenderás a llamar APIs externas, algo que harás en el Módulo 2

#### Ejercicio 1.2: `ejercicio_1_2.py` - Async/Await
**Objetivo:** Programación asíncrona para hacer múltiples peticiones en paralelo
**Relación con el viaje:** La API del Módulo 5 será asíncrona (FastAPI lo requiere)

#### Ejercicio 1.3: `ejercicio_1_3.py` - Context Managers
**Objetivo:** Gestionar recursos (archivos, conexiones) de forma profesional
**Relación con el viaje:** Útil para manejar conexiones a APIs y bases de datos

---

### 🟩 **MÓDULO 2: APIs y Web Scraping (Recolección de Datos)**

**¿De qué va?** Obtener datos del mundo real (precios de acciones, noticias).

#### Ejercicio 2.1: `ejercicio_2_1.py` - Cliente API Financiera
**Objetivo:** Conectarse a Alpha Vantage API para obtener precios de acciones
**Qué construyes:** Clase `FinancialAPIClient` con:
- Cache (para no repetir peticiones)
- Rate limiting (para no ser bloqueado)
- Manejo de errores

**Relación con el viaje:** Este módulo provee los **datos de entrada** para el análisis

#### Ejercicio 2.2: `ejercicio_2_2.py` - Web Scraping de Noticias
**Objetivo:** Extraer noticias financieras de sitios como Yahoo Finance
**Qué construyes:** Scraper con BeautifulSoup o Selenium

**Relación con el viaje:** Las noticias serán analizadas por el módulo de sentimientos

#### Ejercicio 2.3: `ejercicio_2_3.py` - OAuth 2.0
**Objetivo:** Implementar autenticación segura con OAuth
**Relación con el viaje:** Aprenderás autenticación que luego aplicarás en tu API

---

### 🟨 **MÓDULO 3: Transformers y NLP (El Cerebro del Sistema)**

**¿De qué va?** Usar modelos de IA para analizar texto financiero.

#### Ejercicio 3.1: `ejercicio_3_1.py` - Análisis de Sentimientos con FinBERT
**Objetivo:** Crear analizador de sentimientos especializado en finanzas
**Qué construyes:** Clase `AdvancedFinancialSentimentAnalyzer` que:
- Carga modelos pre-entrenados (FinBERT, Twitter-BERT)
- Analiza si una noticia es positiva, negativa o neutral
- Genera índices de sentimiento agregados

**Relación con el viaje:** Este es el **núcleo inteligente** que la API expondrá

#### Ejercicio 3.2: `ejercicio_3_2.py` - Procesamiento de Texto
**Objetivo:** Limpieza y preprocesamiento de datos
**Relación con el viaje:** Preparar los datos antes de pasarlos al modelo

#### Ejercicio 3.3: `ejercicio_3_3.py` - Generación de Texto
**Objetivo:** Generar resúmenes automáticos de análisis
**Relación con el viaje:** Funcionalidad adicional para la API

---

### 🟧 **MÓDULO 4: Machine Learning Aplicado (Predicción)**

**¿De qué va?** Usar los sentimientos + datos históricos para predecir precios.

#### Ejercicio 4.1-4.3: Predicción con LSTM
**Objetivo:** Crear modelo que prediga tendencias de acciones
**Qué construyes:** Modelo que combina:
- Datos históricos de precios
- Sentimientos de noticias
- Predicciones a futuro

**Relación con el viaje:** La predicción es otro servicio que la API ofrecerá

---

### 🟥 **MÓDULO 5: Despliegue (De Script a Servicio) ⭐ AQUÍ ENTRA EL MANUAL**

**¿De qué va?** Convertir todo lo anterior en un servicio web profesional.

#### Ejercicio 5.1: `ejercicio_5_1.py` - API REST con FastAPI
**Objetivo:** Exponer todos los módulos anteriores como endpoints HTTP
**Qué construyes:**
```python
# Tu API tendrá endpoints como:
POST /analyze/sentiment     # Usa el Módulo 3
POST /predict/price         # Usa el Módulo 4
GET  /stock/{symbol}        # Usa el Módulo 2
```

**⚠️ ESTE ES EL EJERCICIO QUE DOCUMENTA EL MANUAL**

El manual cuenta la historia de:
1. **Capítulos 1-3:** Arreglar imports y dependencias del `ejercicio_5_1.py`
2. **Capítulos 4-5:** Convertirlo en un servidor web con FastAPI
3. **Capítulos 6-9:** Meterlo en Docker para que funcione en cualquier lugar
4. **Capítulo 10:** Monitorear y mantener el servicio

#### Ejercicio 5.2: `ejercicio_5_2_docker_setup.py` - Dockerización
**Objetivo:** Empaquetar la API en un contenedor Docker
**Qué construyes:**
- `Dockerfile` (receta para crear la imagen)
- `.dockerignore` (optimización)
- Scripts de deployment

**Relación con el manual:** Capítulos 6-9 del manual

#### Ejercicio 5.3: `ejercicio_5_3_monitoring.py` - Monitoreo
**Objetivo:** Agregar logging, métricas y alertas
**Qué construyes:**
- Sistema de logs
- Métricas con Prometheus
- Health checks

**Relación con el manual:** Capítulo 10 del manual

---

## ¿Por Qué Tantos Ejercicios? La Respuesta

**No te has equivocado.** Construir un servicio web profesional requiere TODAS estas piezas:

```
1. 📥 Módulo 2: ¿Cómo obtengo los datos?
2. 🧠 Módulo 3: ¿Cómo los analizo con IA?
3. 📊 Módulo 4: ¿Cómo hago predicciones?
4. 🌐 Módulo 5.1: ¿Cómo expongo esto como servicio web?
5. 📦 Módulo 5.2: ¿Cómo lo despliego en cualquier servidor?
6. 📈 Módulo 5.3: ¿Cómo monitoreo si funciona bien?
```

**Cada ejercicio es una pieza del rompecabezas final.**

---

## El Flujo Real: ¿Qué Pasa Cuando un Usuario Llama a Tu API?

Supongamos que alguien hace esta petición a tu API desplegada:

```http
POST http://tu-servidor.com:8000/analyze/sentiment
{
  "text": "Apple supera expectativas en ventas del iPhone 15"
}
```

**Este es el viaje interno:**

```
1. FastAPI recibe la petición        (Ejercicio 5.1)
   ↓
2. Valida los datos con Pydantic      (Ejercicio 5.1)
   ↓
3. Llama a FinancialAPIClient         (Ejercicio 2.1)
   para obtener datos de contexto
   ↓
4. Pasa el texto al                   (Ejercicio 3.1)
   AdvancedFinancialSentimentAnalyzer
   ↓
5. El analizador usa FinBERT          (Ejercicio 3.1)
   y devuelve: "Positivo (95%)"
   ↓
6. La API responde al usuario         (Ejercicio 5.1)
   ↓
7. Prometheus registra la métrica     (Ejercicio 5.3)
   "petición exitosa, 120ms"
```

**Todo está ejecutándose dentro de un contenedor Docker** (Ejercicio 5.2) que puede estar en AWS, Azure o tu propio servidor.

---

## Sobre la Presentación PowerPoint

Tu presentación **"Del Script al Servicio: Transformando Código en Producción"** es una versión resumida del **MANUAL_DESARROLLO_Y_DESPLIEGUE.md**.

**Contenido probable de la presentación:**
- Diapositivas 1-5: ¿Por qué desplegar en producción?
- Diapositivas 6-10: FastAPI y creación de la API
- Diapositivas 11-15: Docker y contenerización
- Diapositivas 16-20: Buenas prácticas y monitoreo

**¿A qué ejercicios se refiere?** Principalmente al **Módulo 5** (ejercicios 5.1, 5.2, 5.3).

---

## Cronología del Proyecto: ¿Qué Hiciste y en Qué Orden?

Basándome en los archivos, esto es lo que probablemente pasó:

1. **Semana 1:** Creaste los ejercicios básicos (01-05) y funcionaron ✅
2. **Semana 2-3:** Empezaste los ejercicios avanzados (1.1 - 5.3) como TODOs
3. **Semana 4:** Trabajaste específicamente en el ejercicio 5.1 (FastAPI)
4. **Sesión interactiva:** Tuviste problemas con imports, Docker, etc.
5. **Post-sesión:** Alguien (¿tú o un colaborador?) documentó toda esa sesión en el MANUAL_DESARROLLO_Y_DESPLIEGUE.md
6. **Después:** Creaste la presentación PowerPoint basándote en el manual
7. **Hoy:** Te das cuenta de que no ves la conexión clara entre todo

---

## Hoja de Ruta Sugerida: ¿Qué Hacer Ahora?

### Opción A: Ruta Completa (Recomendada para Aprendizaje)

```
Paso 1: Completa los ejercicios en orden
├── Módulo 1 (1.1, 1.2, 1.3)
├── Módulo 2 (2.1, 2.2, 2.3)
├── Módulo 3 (3.1, 3.2, 3.3)
├── Módulo 4 (4.1, 4.2, 4.3)
└── Módulo 5 (5.1, 5.2, 5.3)

Paso 2: Una vez funcione el ejercicio 5.1 (la API)
└── Sigue el manual para dockerizarlo

Paso 3: Usa la presentación para explicar el proyecto
```

### Opción B: Ruta Rápida (Si Ya Sabes los Fundamentos)

```
Paso 1: Ve directo al ejercicio 5.1
└── Usa versiones simplificadas de los módulos 2-4

Paso 2: Hazlo funcionar como API local
└── Prueba los endpoints en http://localhost:8000/docs

Paso 3: Sigue el manual para dockerizar
└── Capítulos 6-9 del MANUAL_DESARROLLO_Y_DESPLIEGUE.md

Paso 4: Agrega monitoreo
└── Ejercicio 5.3
```

---

## Preguntas y Respuestas

### ❓ "¿Los ejercicios 1.1 - 5.3 están completos o son plantillas?"

**Respuesta:** Son **plantillas con TODOs**. Tú debes completarlos.

El manual documenta la experiencia de **completar y desplegar el ejercicio 5.1**, pero en el proceso se encontraron errores que se fueron solucionando.

---

### ❓ "¿El manual es sobre TODOS los ejercicios o solo el 5.1?"

**Respuesta:** El manual se centra en **el ejercicio 5.1 (la API) y su despliegue**.

Los demás ejercicios (2.1, 3.1, etc.) son módulos que **importa** el ejercicio 5.1.

Ejemplo del código:
```python
# En ejercicio_5_1.py líneas 22-24:
# from ejercicio_3_1 import AdvancedFinancialSentimentAnalyzer
# from ejercicio_4_2 import SentimentEnhancedLSTM
```

El manual menciona (Capítulo 2.1) un error de `NameError: name 'dataclass' is not defined` que probablemente vino de uno de estos imports.

---

### ❓ "¿Por qué el manual habla de ejercicio_2_2.py y ejercicio_2_3.py si se supone que es solo sobre el 5.1?"

**Respuesta:** Porque el ejercicio 5.1 **depende de ellos**.

El manual documenta la solución de errores en esos archivos **porque se descubrieron al intentar ejecutar la API**.

---

### ❓ "¿La presentación PowerPoint es igual al manual?"

**Respuesta:** Probablemente es un **resumen visual** del manual.

El manual tiene 454 líneas con mucho detalle. La presentación es para **explicar** el concepto sin tanto texto.

---

### ❓ "¿Tengo que hacer todos los ejercicios para seguir el manual?"

**Respuesta:** Depende:

- **Para ejecutar el manual:** Solo necesitas los ejercicios que el 5.1 importa (2.x, 3.x, 4.x)
- **Para entender el manual:** Deberías al menos entender qué hacen esos módulos
- **Para aprender todo:** Sí, completa todos los ejercicios

---

## Documento de Arquitectura Visual

Para visualizar cómo se conecta todo, mira el **Apéndice A** del manual (líneas 306-384).

Ahí hay diagramas que muestran:
1. **Diagrama de Sistema:** Usuario → API → Fuentes de Datos
2. **Diagrama de Contenedores:** Cómo la API, la DB y Redis hablan entre sí en Docker

---

## Checklist de Entendimiento

Usa este checklist para verificar que entiendes la conexión:

- [ ] Entiendo que hay ejercicios básicos (01-05) y avanzados (1.1-5.3)
- [ ] Sé que el ejercicio 5.1 es una API que importa código de otros ejercicios
- [ ] Comprendo que el manual documenta el viaje del 5.1 a producción con Docker
- [ ] Veo la relación entre el Módulo 2 (datos) → Módulo 3 (análisis) → Módulo 5.1 (API)
- [ ] Entiendo que la presentación es para explicar este proceso visualmente
- [ ] Sé que los TODOs en los ejercicios son para que yo los complete
- [ ] Puedo explicar qué pasa cuando un usuario llama a la API

---

## Recursos Adicionales

### Si Quieres Entender el Código del Ejercicio 5.1

Lee estos capítulos del manual:
- **Capítulo 4:** Explica el modelo cliente-servidor
- **Capítulo 5:** Explica qué es un middleware en FastAPI
- **Capítulo 7:** Explica el Dockerfile línea por línea

### Si Quieres Dockerizar Tu Proyecto Ahora

Sigue estos capítulos en orden:
1. **Capítulo 3:** Crea el `requirements.txt`
2. **Capítulo 7.3:** Crea el `.dockerignore`
3. **Capítulo 7.1:** Crea el `Dockerfile`
4. **Capítulo 8:** Ejecuta `docker build` y `docker run`

### Si Eres Instructor y Quieres Enseñar Esto

Lee el **Apéndice B** del manual (líneas 387-454). Tiene una guía pedagógica completa.

---

## Resumen en Una Frase

**El manual documenta cómo el ejercicio 5.1 (que usa código de los ejercicios 2-4) se convirtió en un servicio web con Docker; todos los demás ejercicios son las piezas que construyen ese sistema final.**

---

## Próximos Pasos Recomendados

1. **Lee este documento completamente** (¡acabas de hacerlo! ✅)
2. **Revisa el Apéndice A del manual** para ver los diagramas
3. **Decide tu ruta:** ¿Opción A (completa) u Opción B (rápida)?
4. **Empieza por el ejercicio 2.1** o ve directo al 5.1 si tienes prisa
5. **Cuando tengas el 5.1 funcionando, sigue el manual** para dockerizarlo
6. **Usa la presentación PowerPoint para explicar tu proyecto** a otros

---

## ¿Aún Tienes Dudas?

Crea un archivo llamado `DUDAS.md` y escribe tus preguntas específicas. Algunas plantillas útiles:

**Duda sobre conexión de ejercicios:**
```
¿Cómo se conecta el ejercicio X con el ejercicio Y?
¿Qué datos pasa uno al otro?
```

**Duda sobre el manual:**
```
En el Capítulo Z del manual, no entiendo [concepto].
¿Podrías explicarlo con un ejemplo?
```

**Duda sobre ejecución:**
```
Al ejecutar [comando], obtengo [error].
¿Qué parte del manual cubre esto?
```

---

**Creado:** 2025-11-10
**Versión:** 1.0
**Propósito:** Conectar los ejercicios del proyecto con el manual de despliegue y la presentación

---

# Diagrama Final: El Puzzle Completo

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   🎓 TU PROYECTO: Sistema de Análisis Financiero               │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   Módulo 1   │  │   Módulo 2   │  │   Módulo 3   │         │
│  │   Python     │→ │  Recolectar  │→ │   Analizar   │         │
│  │   Avanzado   │  │    Datos     │  │   con IA     │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│         │                 │                   │                 │
│         └─────────────────┴───────────────────┘                 │
│                           │                                     │
│                           ▼                                     │
│                  ┌──────────────────┐                          │
│                  │   Módulo 5.1     │                          │
│                  │  API con FastAPI │◄─────────┐               │
│                  └──────────────────┘          │               │
│                           │                    │               │
│                           ▼                    │               │
│                  ┌──────────────────┐          │               │
│                  │   Módulo 5.2     │          │               │
│                  │  Dockerización   │          │               │
│                  └──────────────────┘          │               │
│                           │                    │               │
│                           ▼                    │               │
│                  ┌──────────────────┐          │               │
│                  │   Módulo 5.3     │          │               │
│                  │   Monitoreo      │          │               │
│                  └──────────────────┘          │               │
│                           │                    │               │
│  ╔════════════════════════╧═════════╗          │               │
│  ║  MANUAL_DESARROLLO_Y_DESPLIEGUE  ║──────────┘               │
│  ║  Documenta este proceso         ║                          │
│  ╚═════════════════════════════════╝                          │
│                           │                                     │
│                           ▼                                     │
│              ┌──────────────────────────┐                      │
│              │  Presentación PowerPoint │                      │
│              │  (Versión Resumida)      │                      │
│              └──────────────────────────┘                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**¡Ahora sí debería tener sentido todo!** 🎉
