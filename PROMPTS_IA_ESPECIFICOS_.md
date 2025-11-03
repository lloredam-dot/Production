# GUÍA DE IMPLEMENTACIÓN CON IA
## Prompts Específicos para Cada Ejercicio

---

## 🤖 PROMPTS PARA GEMINI

### MÓDULO 1: FUNDAMENTOS MODERNOS

#### Ejercicio 1.1: Configuración del Entorno con IA
```
PROMPT PARA GEMINI:
"Actúa como un experto en Python 3.12+ y ayúdame a implementar una clase AICodeReviewer que:

1. Se conecte a la API de Gemini para análisis de código
2. Tenga un método review_code() que analice código Python y sugiera mejoras
3. Incluya un método generate_docstring() para documentación automática
4. Maneje errores de API y rate limiting

Proporciona el código completo con manejo de errores robusto y explica cada parte."
```

#### Ejercicio 1.2: Python 3.12+ Features
```
PROMPT PARA GEMINI:
"Necesito implementar funciones modernas de Python 3.12+ para análisis financiero:

1. Una función con pattern matching que analice datos de acciones según diferentes criterios
2. Uso de TypedDict con NotRequired para datos opcionales
3. Función async que use TaskGroup para obtener datos de múltiples APIs en paralelo

Incluye ejemplos de uso y explica las ventajas de cada característica nueva."
```

### MÓDULO 2: APIs Y WEB SCRAPING

#### Ejercicio 2.1: Cliente API Moderno
```
PROMPT PARA GEMINI:
"Ayúdame a crear un cliente API financiero profesional basado en este patrón de findARestaurant.py:

[PEGAR CÓDIGO DE findARestaurant.py]

Necesito que el nuevo cliente:
1. Use async/await para requests paralelos
2. Implemente rate limiting inteligente
3. Tenga sistema de cache con TTL
4. Maneje errores de red y API de forma robusta
5. Use dataclasses para estructurar respuestas

Proporciona código completo con documentación."
```

#### Ejercicio 2.2: Web Scraping de Noticias
```
PROMPT PARA GEMINI:
"Necesito un scraper de noticias financieras que:

1. Use Selenium para contenido JavaScript
2. Extraiga títulos, fechas, contenido y URLs
3. Implemente análisis básico de sentimiento
4. Maneje diferentes estructuras de sitios web
5. Guarde resultados en formato estructurado

Incluye manejo de User-Agent, delays entre requests y detección de anti-bot."
```

---

## 🧠 PROMPTS PARA DEEPSEEK

### MÓDULO 3: PROCESAMIENTO DE TEXTO Y NLP

#### Ejercicio 3.1: Análisis de Sentimientos Financieros
```
PROMPT PARA DEEPSEEK:
"Implementa un sistema completo de análisis de sentimientos financieros basado en esta metodología de tesis:

[PEGAR SECCIÓN RELEVANTE DE 1752331352542.md]

El sistema debe:
1. Cargar múltiples modelos (FinBERT, Twitter-specific, general)
2. Preprocesar texto financiero (normalizar tickers, porcentajes)
3. Crear índice de sentimiento agregado como en la tesis
4. Manejar diferentes tipos de texto (tweets, noticias, opiniones)
5. Calcular métricas de confianza

Optimiza para performance y precisión."
```

#### Ejercicio 3.2: Procesamiento con spaCy
```
PROMPT PARA DEEPSEEK:
"Crea un procesador de texto financiero avanzado con spaCy que:

1. Extraiga entidades financieras específicas (tickers, cantidades, empresas)
2. Use Matcher patterns para patrones financieros complejos
3. Analice dependencias sintácticas para relaciones entre entidades
4. Genere grafo de conocimiento con NetworkX
5. Implemente resumen automático de documentos financieros

Incluye diccionarios especializados y reglas personalizadas."
```

### MÓDULO 4: MACHINE LEARNING FINANCIERO

#### Ejercicio 4.1: Red Neuronal LSTM
```
PROMPT PARA DEEPSEEK:
"Implementa una red LSTM para predicción de precios basada en esta arquitectura de tesis:

[PEGAR SECCIÓN DE METODOLOGÍA LSTM DE LA TESIS]

Requisitos:
1. Clase StockDataProcessor para preparar secuencias temporales
2. Modelo FinancialLSTM con múltiples capas y dropout
3. Función de entrenamiento con early stopping
4. Métricas de evaluación (MSE, MAE, precisión direccional)
5. Visualización de predicciones vs valores reales

Optimiza la arquitectura para datos financieros."
```

#### Ejercicio 4.2: Integración Sentimientos + LSTM
```
PROMPT PARA DEEPSEEK:
"Extiende el modelo LSTM para integrar variables de sentimiento como en la tesis:

Necesito:
1. SentimentEnhancedLSTM con ramas separadas para precio y sentimiento
2. Capa de fusión para combinar características
3. Comparación con modelo base (solo precios)
4. Análisis de contribución del sentimiento
5. Evaluación por regímenes de mercado (bull/bear)

Replica la mejora del 14% en MSE reportada en la tesis."
```

---

## 💻 PROMPTS PARA GITHUB COPILOT

### MÓDULO 5: INTEGRACIÓN Y DESPLIEGUE

#### Ejercicio 5.1: API con FastAPI
```
# Comentario para Copilot:
# Crear API REST completa para sistema de ML financiero
# Incluir endpoints para análisis de sentimientos y predicciones LSTM
# Implementar autenticación JWT, rate limiting y documentación automática
# Usar Pydantic para validación de datos y respuestas estructuradas

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
# Copilot completará automáticamente...
```

#### Ejercicio 5.2: Containerización
```
# Dockerfile para aplicación Python ML financiera
# Multi-stage build para optimizar tamaño
# Incluir dependencias de ML (PyTorch, Transformers)
# Usuario no-root para seguridad
# Health check endpoint

FROM python:3.12-slim as builder
# Copilot sugerirá la configuración completa...
```

---

## 🔧 PROMPTS PARA DEBUGGING

### Debugging con ChatGPT
```
PROMPT PARA DEBUGGING:
"Tengo este error en mi código de análisis de sentimientos:

[PEGAR ERROR Y CÓDIGO]

El error ocurre cuando intento procesar tweets con emojis. Analiza:
1. ¿Cuál es la causa raíz del problema?
2. ¿Cómo puedo solucionarlo manteniendo la funcionalidad?
3. ¿Qué mejores prácticas debería implementar para evitar errores similares?
4. ¿Puedes sugerir tests unitarios para este caso?

Proporciona solución completa con explicación."
```

### Code Review con Claude
```
PROMPT PARA CODE REVIEW:
"Revisa este código de mi modelo LSTM y sugiere mejoras:

[PEGAR CÓDIGO]

Evalúa:
1. Arquitectura del modelo - ¿es óptima para datos financieros?
2. Manejo de datos - ¿hay problemas de data leakage?
3. Performance - ¿cómo optimizar velocidad y memoria?
4. Mantenibilidad - ¿está bien estructurado?
5. Testing - ¿qué tests faltan?

Prioriza sugerencias por impacto."
```

---

## 🎯 PROMPTS PARA OPTIMIZACIÓN

### Performance con Perplexity
```
PROMPT PARA OPTIMIZACIÓN:
"Mi sistema de análisis financiero procesa 10,000 tweets por minuto pero necesito llegar a 50,000. Analiza estas opciones de optimización:

1. Batch processing vs streaming
2. Async/await vs multiprocessing
3. GPU acceleration para modelos
4. Caching strategies
5. Database optimization

¿Cuál es la mejor estrategia considerando costo-beneficio?"
```

### Arquitectura con Bard
```
PROMPT PARA ARQUITECTURA:
"Diseña la arquitectura de microservicios para mi sistema de ML financiero:

Componentes:
- API Gateway
- Servicio de análisis de sentimientos
- Servicio de predicción LSTM
- Base de datos de series temporales
- Cache distribuido
- Sistema de monitoreo

¿Cómo estructurarías la comunicación entre servicios y el manejo de fallos?"
```

---

## 📚 PROMPTS PARA DOCUMENTACIÓN

### Documentación Técnica
```
PROMPT PARA DOCUMENTACIÓN:
"Genera documentación técnica completa para mi clase FinancialLSTM:

[PEGAR CÓDIGO DE LA CLASE]

Incluye:
1. Descripción general y propósito
2. Parámetros del constructor con tipos y rangos
3. Métodos públicos con ejemplos de uso
4. Arquitectura interna explicada
5. Consideraciones de performance
6. Ejemplos de integración

Usa formato Sphinx/Google docstring."
```

### README del Proyecto
```
PROMPT PARA README:
"Crea un README profesional para mi proyecto de análisis financiero con ML:

Características del proyecto:
- Análisis de sentimientos con FinBERT
- Predicción de precios con LSTM
- API REST con FastAPI
- Dashboard con Streamlit
- Deployment con Docker

Incluye: instalación, uso, ejemplos, arquitectura, contribución y licencia."
```

---

## 🧪 PROMPTS PARA TESTING

### Tests Unitarios
```
PROMPT PARA TESTING:
"Genera suite completa de tests unitarios para mi clase SentimentAnalyzer:

[PEGAR CÓDIGO]

Necesito tests para:
1. Casos normales con diferentes tipos de texto
2. Edge cases (texto vacío, muy largo, caracteres especiales)
3. Manejo de errores de API
4. Performance con grandes volúmenes
5. Mocks para dependencias externas

Usa pytest con fixtures y parametrización."
```

### Tests de Integración
```
PROMPT PARA INTEGRATION TESTS:
"Diseña tests de integración para mi API de ML financiero:

Endpoints a probar:
- POST /analyze/sentiment
- POST /predict/stock
- GET /health

Incluye:
1. Tests de flujo completo end-to-end
2. Validación de respuestas y códigos de estado
3. Tests de carga y performance
4. Manejo de errores y timeouts
5. Autenticación y autorización

Usa httpx y pytest-asyncio."
```

---

## 🚀 PROMPTS PARA DEPLOYMENT

### Configuración de Producción
```
PROMPT PARA DEPLOYMENT:
"Ayúdame a configurar deployment de producción para mi API de ML financiero:

Requisitos:
- Alta disponibilidad (99.9% uptime)
- Escalabilidad horizontal
- Monitoreo y alertas
- Backup automático
- SSL/TLS
- Rate limiting

¿Cuál es la mejor estrategia usando Docker + Kubernetes o alternativas cloud?"
```

### Monitoreo y Observabilidad
```
PROMPT PARA MONITORING:
"Diseña sistema de monitoreo completo para mi aplicación de ML financiero:

Métricas necesarias:
- Performance de API (latencia, throughput)
- Precisión de modelos ML
- Uso de recursos (CPU, memoria, GPU)
- Errores y excepciones
- Métricas de negocio

Incluye dashboards, alertas y logs estructurados con Prometheus + Grafana."
```

---

## 💡 TIPS PARA USAR LAS IAS EFECTIVAMENTE

### 🎯 Mejores Prácticas

#### 1. **Sé Específico**
- ❌ "Ayúdame con ML"
- ✅ "Implementa LSTM para predicción de precios con estas características específicas..."

#### 2. **Proporciona Contexto**
- Incluye código existente
- Explica el dominio del problema
- Menciona restricciones técnicas

#### 3. **Itera y Refina**
- Haz preguntas de seguimiento
- Pide explicaciones detalladas
- Solicita optimizaciones específicas

#### 4. **Combina Herramientas**
- Gemini para conceptos y arquitectura
- DeepSeek para implementación
- Copilot para autocompletado
- ChatGPT para debugging

#### 5. **Valida Siempre**
- Ejecuta el código generado
- Verifica con tests
- Revisa mejores prácticas
- Compara con documentación oficial

### 🔄 Flujo de Trabajo Recomendado

1. **Planificación** → Gemini/Claude (arquitectura)
2. **Implementación** → DeepSeek/Copilot (código)
3. **Debugging** → ChatGPT (solución de errores)
4. **Optimización** → Perplexity (research)
5. **Documentación** → Bard (explicaciones)
6. **Testing** → Copilot (generación de tests)

### ⚡ Shortcuts de Productividad

```bash
# Alias útiles para el curso
alias gpt="echo 'Copiando al clipboard para ChatGPT...' && pbcopy"
alias gemini="echo 'Preparando prompt para Gemini...' && code prompt.md"
alias review="echo 'Iniciando code review con IA...' && git diff | pbcopy"
```

¡Con estos prompts y técnicas, maximizarás tu productividad y aprendizaje durante el curso! 🚀