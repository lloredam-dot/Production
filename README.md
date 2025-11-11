# 🚀 Del Código al Despliegue: NLP en Producción

**Aprende a construir, dockerizar y desplegar sistemas de NLP profesionales**

---

## 🎯 ¿Por qué este proyecto?

**El problema que existe en la industria:**

Muchos cursos te enseñan a programar modelos de NLP que funcionan en Jupyter notebooks, pero cuando llega el momento de llevarlos a producción... **no tienes idea de cómo hacerlo**.

Este proyecto llena ese vacío. No es solo teoría ni solo código de juguete. Es el **camino completo** desde Python básico hasta un sistema real corriendo en Docker con monitoreo, listo para producción.

---

## 💡 ¿Qué aprenderás?

### Habilidades Técnicas

Al completar este proyecto, dominarás:

| Área | Tecnologías | Aplicación Real |
|------|-------------|-----------------|
| **Backend Moderno** | FastAPI, Uvicorn, Pydantic | Crear APIs REST profesionales |
| **NLP State-of-the-Art** | Transformers, BERT, spaCy | Análisis de sentimiento, NER, generación de texto |
| **Deep Learning** | PyTorch, LSTM | Predicción de series temporales |
| **DevOps** | Docker, Docker Compose | Contenerización y orquestación |
| **Observabilidad** | Prometheus | Monitoreo de servicios en producción |
| **Python Avanzado** | Async/await, decoradores, context managers | Código eficiente y escalable |
| **Data Engineering** | Web scraping, APIs, OAuth 2.0 | Recolección de datos del mundo real |

### Habilidades Prácticas

- ✅ Consumir APIs REST de terceros (financieras, noticias)
- ✅ Construir tus propias APIs documentadas con Swagger
- ✅ Entrenar y usar modelos pre-entrenados (FinBERT, GPT-2)
- ✅ Dockerizar cualquier aplicación Python
- ✅ Monitorear servicios con métricas (Prometheus)
- ✅ Trabajar con datos financieros reales
- ✅ Implementar autenticación JWT
- ✅ Manejar tareas asíncronas y concurrencia

---

## 🎓 ¿Para quién es este proyecto?

### ✅ Perfil Ideal:

- Sabes Python básico (funciones, clases, manejo de archivos)
- Has usado pandas o numpy alguna vez
- Quieres aprender NLP/ML de forma práctica, no solo teórica
- Necesitas llevar tus modelos a producción (o saber cómo hacerlo)
- Quieres entender DevOps sin perderte en documentación infinita

### ❌ NO necesitas:

- Ser experto en Docker (lo aprenderás aquí)
- Conocer FastAPI (lo enseñamos desde cero)
- Tener experiencia en NLP (empezamos desde fundamentos)
- Un servidor en la nube (todo corre localmente con Docker)

---

## 📚 Estructura del Curso

El proyecto está organizado en **5 módulos progresivos** con 15 ejercicios:

### 🟢 Módulo 1: Fundamentos de Python Avanzado
**Duración estimada: 6-9 horas**

- **ejercicio_1_1.py** - Configuración de asistentes IA (Gemini/DeepSeek)
- **ejercicio_1_2.py** - Programación asíncrona con async/await
- **ejercicio_1_3.py** - Context managers y gestión de recursos

**¿Qué aprenderás?**
Patrones avanzados de Python que hacen tu código más profesional, eficiente y mantenible.

---

### 🟡 Módulo 2: Recolección de Datos
**Duración estimada: 6-9 horas**

- **ejercicio_2_1.py** - Cliente de APIs financieras (rate limiting, autenticación)
- **ejercicio_2_2.py** - Web scraping con BeautifulSoup y Selenium
- **ejercicio_2_3.py** - Limpieza de datos y OAuth 2.0

**¿Qué aprenderás?**
Cómo obtener datos del mundo real: APIs, web scraping, autenticación, y limpieza de datos.

---

### 🟠 Módulo 3: Transformers y NLP Moderno
**Duración estimada: 9-12 horas**

- **ejercicio_3_1.py** - Análisis de sentimientos con FinBERT
- **ejercicio_3_2.py** - Named Entity Recognition y POS tagging con spaCy
- **ejercicio_3_3.py** - Generación de texto con modelos GPT

**¿Qué aprenderás?**
Los modelos de lenguaje más modernos: cómo usarlos, afinarlos, y entender qué está pasando por dentro.

---

### 🔴 Módulo 4: NLP Aplicado a Finanzas
**Duración estimada: 9-12 horas**

- **ejercicio_4_1.py** - Extracción de indicadores financieros
- **ejercicio_4_2.py** - Análisis de sentimiento en earnings calls
- **ejercicio_4_3.py** - Predicción de precios con LSTM (PyTorch)

**¿Qué aprenderás?**
Aplicar NLP a un dominio específico (finanzas), entrenar redes LSTM, y hacer predicciones con datos reales.

---

### 🔵 Módulo 5: Despliegue y Producción
**Duración estimada: 6-9 horas**

- **ejercicio_5_1.py** - API REST con FastAPI (Swagger, JWT, CORS)
- **ejercicio_5_2_docker_setup.py** - Dockerización y optimización
- **ejercicio_5_3_monitoring.py** - Monitoreo con Prometheus

**¿Qué aprenderás?**
Llevar tu código a producción: APIs profesionales, contenedores Docker, y monitoreo.

---

### 🎯 Proyecto Final
**Duración estimada: 2-4 horas**

- **proyecto_final.py** - Sistema integrado que combina todo lo anterior

**¿Qué construirás?**
Un sistema completo de análisis financiero con NLP que corre en Docker, tiene API REST, y está monitoreado.

---

## ⏱️ Tiempo Total Estimado

| Ritmo | Duración | Horas por día |
|-------|----------|---------------|
| **Intensivo** | 1-2 semanas | 3-4 horas |
| **Regular** | 4-6 semanas | 1-2 horas |
| **Relajado** | 8-10 semanas | 30-60 minutos |

**Total: 40-55 horas** (incluyendo lectura de documentación)

---

## 🚀 Inicio Rápido (Quick Start)

### Paso 1: Requisitos previos

Instala esto antes de empezar:

- **Python 3.8+** (recomendado 3.12): https://www.python.org/downloads/
- **Docker Desktop**: https://www.docker.com/products/docker-desktop/
- **Git**: https://git-scm.com/downloads
- **Editor de código**: VS Code recomendado

---

### Paso 2: Clonar e instalar

```bash
# Clonar el repositorio
git clone <tu-repo-url>
cd dokerizacion

# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Descargar modelo de spaCy
python -m spacy download en_core_web_sm
```

---

### Paso 3: Ejecutar tu primer ejercicio

```bash
python ejercicio_1_1.py
```

**¡Si ves output sin errores, estás listo! 🎉**

---

### Paso 4: Sigue la guía paso a paso

Abre y lee:
```
GUIA_DESPLIEGUE_PASO_A_PASO.md
```

Esta guía te lleva de la mano desde cero hasta tener todo funcionando en Docker.

---

## 📖 Documentación Incluida

Este proyecto incluye documentación completa y didáctica:

| Archivo | Descripción | Cuándo leerlo |
|---------|-------------|---------------|
| **README.md** | Este archivo - Visión general | **Lee primero** |
| **[DIAPOSITIVAS.md](./DIAPOSITIVAS.md)** | Presentación visual del proyecto | Antes de empezar |
| **[GUIA_DESPLIEGUE_PASO_A_PASO.md](./GUIA_DESPLIEGUE_PASO_A_PASO.md)** | Tutorial detallado paso a paso | Durante todo el proceso |
| **[CONTEXTO_DEL_PROYECTO.md](./CONTEXTO_DEL_PROYECTO.md)** | Historia y decisiones técnicas | Cuando quieras contexto |
| **[GUIA_CONEXION_EJERCICIOS_Y_DESPLIEGUE.md](./GUIA_CONEXION_EJERCICIOS_Y_DESPLIEGUE.md)** | Cómo se conectan todos los ejercicios | Para entender el flujo completo |

---

## 🏗️ Arquitectura del Sistema Final

Al terminar el proyecto, habrás construido esto:

```
                     INTERNET
                        │
                        ▼
                ┌──────────────┐
                │    NGINX     │ ← Reverse Proxy
                │   (Puerto 80) │
                └──────┬───────┘
                       │
                       ▼
           ┌───────────────────────┐
           │   FastAPI Application │ ← Tu código
           │     (Puerto 8000)     │
           │  • NLP con FinBERT    │
           │  • REST endpoints     │
           │  • JWT auth           │
           └─────┬────────────┬────┘
                 │            │
          ┌──────▼─┐      ┌───▼────────┐
          │PostgreSQL│      │ Prometheus │ ← Monitoreo
          │(Database)│      │(Metrics)   │
          └──────────┘      └────────────┘
                 │
          ┌──────▼─┐
          │ Redis  │ ← Caché
          └────────┘
```

**Todo orquestado con Docker Compose.**

---

## 📂 Estructura de Archivos

```
dokerizacion/
│
├── 📄 README.md                        ← Estás aquí
├── 📊 DIAPOSITIVAS.md                  ← Presentación del proyecto
├── 📖 GUIA_DESPLIEGUE_PASO_A_PASO.md   ← Tutorial completo
├── 📝 CONTEXTO_DEL_PROYECTO.md
├── 📝 GUIA_CONEXION_EJERCICIOS_Y_DESPLIEGUE.md
│
├── 🐍 Módulo 1: Python Avanzado
│   ├── ejercicio_1_1.py
│   ├── ejercicio_1_2.py
│   └── ejercicio_1_3.py
│
├── 🌐 Módulo 2: Recolección de Datos
│   ├── ejercicio_2_1.py
│   ├── ejercicio_2_2.py
│   └── ejercicio_2_3.py
│
├── 🤖 Módulo 3: NLP Moderno
│   ├── ejercicio_3_1.py
│   ├── ejercicio_3_2.py
│   └── ejercicio_3_3.py
│
├── 💰 Módulo 4: NLP Financiero
│   ├── ejercicio_4_1.py
│   ├── ejercicio_4_2.py
│   └── ejercicio_4_3.py
│
├── 🚀 Módulo 5: Producción
│   ├── ejercicio_5_1.py
│   ├── ejercicio_5_2_docker_setup.py
│   └── ejercicio_5_3_monitoring.py
│
├── 🎯 proyecto_final.py
│
├── 🐳 Docker
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── .dockerignore
│
└── 📦 requirements.txt
```

---

## 🎯 ¿Qué construirás exactamente?

### Sistema de Análisis Financiero con NLP

**INPUT:**
- Noticias financieras (scraping de webs)
- Tweets sobre acciones (API de Twitter)
- Reportes de earnings calls (APIs financieras)

**PROCESAMIENTO:**
- Limpieza y normalización de texto
- Análisis de sentimiento con FinBERT
- Extracción de entidades (empresas, fechas, montos)
- Predicción de tendencias con LSTM

**OUTPUT:**
- API REST documentada (Swagger UI)
- Métricas en tiempo real (Prometheus)
- Respuestas JSON estructuradas
- Contenedor Docker listo para desplegar

**Casos de uso reales:**
- Detectar sentimiento de mercado antes de eventos importantes
- Alertar cuando el sentimiento cambia drásticamente
- Agregar sentimiento de múltiples fuentes
- Predecir movimientos de precios basados en noticias

---

## 🛤️ Camino de Aprendizaje Recomendado

### Fase 1: Configuración (Día 1)
```bash
1. Lee README.md (este archivo) ✓
2. Lee DIAPOSITIVAS.md
3. Configura tu entorno (Python, Docker)
4. Instala dependencias
5. Ejecuta ejercicio_1_1.py
```

### Fase 2: Fundamentos (Semana 1-2)
```bash
Módulo 1: Python Avanzado
Módulo 2: Recolección de Datos

Consejo: Lee el código ANTES de ejecutar.
         Entiende qué hace cada ejercicio.
         Modifica y experimenta.
```

### Fase 3: NLP (Semana 3-4)
```bash
Módulo 3: Transformers
Módulo 4: NLP Financiero

Consejo: La primera ejecución descargará modelos grandes (~500MB).
         Ten paciencia, es normal que tarde.
         Si no tienes GPU, usa CPU (más lento pero funciona).
```

### Fase 4: Producción (Semana 5-6)
```bash
Módulo 5: Despliegue

Consejo: Sigue GUIA_DESPLIEGUE_PASO_A_PASO.md al pie de la letra.
         Prueba cada endpoint en Swagger UI.
         Ve las métricas en Prometheus.
```

### Fase 5: Integración (Semana 7-8)
```bash
Proyecto Final

Consejo: Este proyecto combina TODO lo anterior.
         Es tu oportunidad de demostrar lo que aprendiste.
         Modifícalo para tu caso de uso específico.
```

---

## 💪 Consejos para el Éxito

### ✅ DO (Haz esto)

1. **Sigue el orden** - Los ejercicios están diseñados para construir sobre el anterior
2. **Lee el código** - Cada archivo tiene comentarios extensos explicando el "por qué"
3. **Experimenta** - Modifica parámetros, rompe cosas, arregla cosas
4. **Toma notas** - Escribe lo que aprendiste después de cada ejercicio
5. **Usa la documentación** - Consulta GUIA_DESPLIEGUE_PASO_A_PASO.md cuando te atores

### ❌ DON'T (Evita esto)

1. **No te saltes ejercicios** - Cada uno enseña algo importante
2. **No copies y pegues** - Escribe el código tú mismo para aprender
3. **No te frustres** - Es normal atascarse. Usa la guía y Google
4. **No corras** - Mejor entender 1 ejercicio bien que hacer 5 mal
5. **No ignores los errores** - Los errores enseñan. Entiéndelos antes de continuar

---

## 🔧 Solución de Problemas Rápidos

### Problema: "ModuleNotFoundError"
```bash
# Solución: Activa el entorno virtual
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Instala dependencias
pip install -r requirements.txt
```

### Problema: "Port 8000 is already in use"
```bash
# Solución: Usa otro puerto
uvicorn ejercicio_5_1:app --port 8001

# O encuentra y mata el proceso
# Windows: netstat -ano | findstr :8000
# Linux/Mac: lsof -i :8000
```

### Problema: Docker build muy lento
```bash
# Solución: Limpia el cache
docker system prune -a
```

**Para más problemas, consulta la sección "Solución de Problemas Comunes" en GUIA_DESPLIEGUE_PASO_A_PASO.md**

---

## 📊 ¿Qué te llevarás de este proyecto?

### Habilidades Técnicas Verificables

Al completar este proyecto, tendrás:

- ✅ **Portfolio piece**: Un proyecto real para mostrar a empleadores
- ✅ **Conocimiento práctico**: No solo teoría, sino código que funciona
- ✅ **Experiencia con herramientas modernas**: FastAPI, Docker, Transformers
- ✅ **Comprensión del ciclo completo**: Desde código hasta despliegue

### Estas habilidades son demandadas para:

- 💼 Ingeniero de Machine Learning
- 💼 Backend Developer (Python)
- 💼 MLOps Engineer
- 💼 Data Engineer
- 💼 NLP Engineer

---

## 🚀 Después de Completar Este Proyecto

### Próximos Pasos Sugeridos:

**Nivel 1: Mejoras rápidas**
- Agregar testing automatizado (pytest)
- Implementar autenticación JWT completa
- Agregar rate limiting con Redis

**Nivel 2: Proyectos intermedios**
- Desplegar en la nube (AWS, GCP, Azure)
- Agregar CI/CD con GitHub Actions
- Crear dashboard con Streamlit

**Nivel 3: Proyectos avanzados**
- Implementar caché distribuido con Redis
- Agregar Kubernetes para orquestación
- Crear sistema de alertas con Grafana

---

## 🤝 Contribuciones

¿Encontraste un error? ¿Tienes una mejora? ¡Las contribuciones son bienvenidas!

1. Fork el repositorio
2. Crea una rama: `git checkout -b feature/mejora`
3. Commit: `git commit -m 'Descripción de la mejora'`
4. Push: `git push origin feature/mejora`
5. Abre un Pull Request

---

## 📜 Licencia

Este proyecto tiene fines educativos. Siéntete libre de usar y modificar el código para tu aprendizaje.

---

## 📞 Soporte

**¿Tienes preguntas?**
- Abre un issue en el repositorio
- Consulta la sección de troubleshooting en GUIA_DESPLIEGUE_PASO_A_PASO.md
- Revisa los comentarios en el código

---

## 🙏 Agradecimientos

Este proyecto fue creado para ayudar a desarrolladores a dar el salto de "código que funciona localmente" a "servicios en producción".

Si este proyecto te ayudó:
- ⭐ Dale estrella al repositorio
- 📢 Compártelo con otros desarrolladores
- 💬 Deja feedback para mejorarlo

---

## 🎯 TL;DR (Resumen Ultra-Rápido)

```bash
# 1. Clona e instala
git clone <repo-url>
cd dokerizacion
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# 2. Lee las guías
# - DIAPOSITIVAS.md (visión general)
# - GUIA_DESPLIEGUE_PASO_A_PASO.md (tutorial completo)

# 3. Ejecuta ejercicios en orden
python ejercicio_1_1.py
# ... continúa hasta ejercicio_5_3.py

# 4. Construye y despliega con Docker
docker build -t nlp-api .
docker run -p 8000:8000 nlp-api

# 5. O usa Docker Compose para el stack completo
docker-compose up -d
```

**¡Eso es todo! Ahora empieza a aprender. 🚀**

---

**Última actualización:** Enero 2025
**Versión:** 2.0 (Simplificada y enfocada en producción)
**Mantenedor:** Tu nombre aquí

---

**¿Listo para empezar? Abre [GUIA_DESPLIEGUE_PASO_A_PASO.md](./GUIA_DESPLIEGUE_PASO_A_PASO.md) y comienza tu viaje. 🎓**
