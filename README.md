# Proyecto de Procesamiento de Lenguaje Natural (NLP) en Python

Este repositorio contiene un conjunto completo de ejercicios y proyectos prácticos para aprender Procesamiento de Lenguaje Natural (NLP) desde los fundamentos básicos hasta aplicaciones avanzadas con Machine Learning.

## Índice
- [Descripción General](#descripción-general)
- [Análisis de Sentimientos Básico](#análisis-de-sentimientos-básico)
- [Ejercicios Avanzados](#ejercicios-avanzados)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Cómo Ejecutar](#cómo-ejecutar)
- [Estructura del Proyecto](#estructura-del-proyecto)

---

## Descripción General

Este proyecto está diseñado con un enfoque pedagógico progresivo:

1. **Primero**: Dominar los fundamentos de NLP con ejercicios simples y autocontenidos
2. **Segundo**: Aplicar técnicas avanzadas con APIs, Docker y modelos de Machine Learning
3. **Objetivo**: Construir una base sólida antes de enfrentar proyectos complejos

---

## Análisis de Sentimientos Básico

La carpeta `analisis_sentimientos_basico/` contiene **5 ejercicios fundamentales** que todo practicante de NLP debe dominar. Estos ejercicios son completamente autocontenidos y no requieren bases de datos ni APIs externas.

### ¿Por qué empezar aquí?

Estos ejercicios te enseñan la **mecánica interna** del procesamiento de texto, desde la tokenización hasta el clustering. Son la base necesaria para entender los ejercicios avanzados.

### Los 5 Ejercicios Fundamentales

#### 1. `01_conteo_palabras.py` - Tokenización y Frecuencias
**Qué aprenderás:**
- Normalizar texto (minúsculas)
- Tokenizar con expresiones regulares
- Contar frecuencias de palabras con `Counter`
- Visualizar resultados con gráficos de barras

**Ejecución:**
```bash
python analisis_sentimientos_basico/01_conteo_palabras.py
```

#### 2. `02_limpieza_texto.py` - Eliminación de Stopwords
**Qué aprenderás:**
- Crear y usar sets de stopwords
- Filtrar palabras sin significado
- Comparar texto antes y después de la limpieza

**Ejecución:**
```bash
python analisis_sentimientos_basico/02_limpieza_texto.py
```

#### 3. `03_sentimiento_por_lexicon.py` - Clasificador de Sentimientos
**Qué aprenderás:**
- Crear léxicos de palabras positivas y negativas
- Calcular puntajes de sentimiento
- Clasificar texto como Positivo/Negativo/Neutro
- Visualizar distribución con gráficos de tarta

**Ejecución:**
```bash
python analisis_sentimientos_basico/03_sentimiento_por_lexicon.py
```

#### 4. `04_similitud_jaccard.py` - Similitud entre Textos
**Qué aprenderás:**
- Calcular similitud de Jaccard
- Construir matrices de similitud
- Crear mapas de calor con `seaborn`

**Ejecución:**
```bash
python analisis_sentimientos_basico/04_similitud_jaccard.py
```

#### 5. `05_vectorizacion_y_clustering.py` - Machine Learning No Supervisado
**Qué aprenderás:**
- Vectorización TF-IDF con `scikit-learn`
- Clustering con K-Means
- Reducción de dimensionalidad con PCA
- Visualizar clusters en 2D

**Ejecución:**
```bash
python analisis_sentimientos_basico/05_vectorizacion_y_clustering.py
```

### Documentación Completa

Dentro de `analisis_sentimientos_basico/` encontrarás un `README.md` detallado con explicaciones teóricas de cada técnica.

---

## Ejercicios Avanzados

Una vez dominados los fundamentos, puedes avanzar a los ejercicios complejos en la raíz del proyecto:

### Módulo 1: Python Avanzado y Estructura de Datos
- `ejercicio_1_1.py` - Decoradores y manejo de memoria
- `ejercicio_1_2.py` - Async/Await y programación concurrente
- `ejercicio_1_3.py` - Context managers y gestión de recursos

### Módulo 2: Web Scraping
- `ejercicio_2_1.py` - Scraping básico con BeautifulSoup
- `ejercicio_2_2.py` - Scraping dinámico con Selenium
- `ejercicio_2_3.py` - Análisis y limpieza de datos

### Módulo 3: Transformers y Modelos de Lenguaje
- `ejercicio_3_1.py` - Fine-tuning de modelos BERT
- `ejercicio_3_2.py` - Análisis de sentimientos con transformers
- `ejercicio_3_3.py` - Generación de texto

### Módulo 4: NLP Aplicado a Finanzas
- `ejercicio_4_1.py` - Extracción de datos financieros
- `ejercicio_4_2.py` - Análisis de sentimientos financiero
- `ejercicio_4_3.py` - Predicción de tendencias

### Módulo 5: Despliegue y Producción
- `ejercicio_5_1.py` - API REST con FastAPI
- `ejercicio_5_2_docker_setup.py` - Contenerización
- `ejercicio_5_3_monitoring.py` - Monitoreo con Prometheus

### Proyecto Final
- `proyecto_final.py` - Sistema completo de análisis financiero

---

## Requisitos Previos

### Conocimientos Necesarios

**Para Análisis de Sentimientos Básico:**
- ✅ Python básico (variables, listas, diccionarios, loops)
- ✅ No se requiere experiencia previa en NLP

**Para Ejercicios Avanzados:**
- ✅ Dominio de los 5 ejercicios básicos
- ✅ Comprensión de vectorización y clustering
- ✅ Familiaridad con conceptos de ML
- ✅ (Opcional) Experiencia con APIs REST
- ✅ (Opcional) Conocimientos de Docker

### Software Necesario

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- (Opcional) Docker Desktop - solo para ejercicios del Módulo 5

---

## Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/NacheTyson/npl_intro.git
cd npl_intro
```

### 2. Crear un Entorno Virtual (Recomendado)

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar Dependencias

**Para ejercicios básicos (mínimo necesario):**
```bash
pip install matplotlib scikit-learn seaborn
```

**Para todos los ejercicios:**
```bash
pip install -r requirements.txt
```

> **Nota**: La instalación completa incluye PyTorch (~2GB) y puede tardar varios minutos.

---

## Cómo Ejecutar

### Ruta de Aprendizaje Recomendada

#### Fase 1: Fundamentos (COMENZAR AQUÍ)

Ejecuta los ejercicios en orden:

```bash
# 1. Conteo de palabras
python analisis_sentimientos_basico/01_conteo_palabras.py

# 2. Limpieza de texto
python analisis_sentimientos_basico/02_limpieza_texto.py

# 3. Análisis de sentimientos
python analisis_sentimientos_basico/03_sentimiento_por_lexicon.py

# 4. Similitud de textos
python analisis_sentimientos_basico/04_similitud_jaccard.py

# 5. Clustering con ML
python analisis_sentimientos_basico/05_vectorizacion_y_clustering.py
```

Cada script generará gráficos que se mostrarán automáticamente. **Lee el README dentro de la carpeta `analisis_sentimientos_basico/` para entender la teoría**.

#### Fase 2: Ejercicios Avanzados

Una vez completada la Fase 1, puedes ejecutar los ejercicios avanzados:

```bash
# Ejemplo: Ejecutar el módulo de web scraping
python ejercicio_2_1.py
```

#### Fase 3: API y Despliegue

Para el servidor API:

```bash
# Ejecutar servidor FastAPI
python ejercicio_5_1.py

# Acceder a la documentación interactiva
# Abre tu navegador en: http://localhost:8000/docs
```

Para Docker:

```bash
# Construir la imagen
docker build -t npl-app .

# Ejecutar el contenedor
docker run -p 8000:8000 npl-app
```

---

## Estructura del Proyecto

```
npl_intro/
│
├── analisis_sentimientos_basico/    # ⭐ COMENZAR AQUÍ
│   ├── 01_conteo_palabras.py
│   ├── 02_limpieza_texto.py
│   ├── 03_sentimiento_por_lexicon.py
│   ├── 04_similitud_jaccard.py
│   ├── 05_vectorizacion_y_clustering.py
│   └── README.md                    # Documentación teórica
│
├── ejercicio_1_1.py                 # Módulo 1: Python Avanzado
├── ejercicio_1_2.py
├── ejercicio_1_3.py
│
├── ejercicio_2_1.py                 # Módulo 2: Web Scraping
├── ejercicio_2_2.py
├── ejercicio_2_3.py
│
├── ejercicio_3_1.py                 # Módulo 3: Transformers
├── ejercicio_3_2.py
├── ejercicio_3_3.py
│
├── ejercicio_4_1.py                 # Módulo 4: NLP Financiero
├── ejercicio_4_2.py
├── ejercicio_4_3.py
│
├── ejercicio_5_1.py                 # Módulo 5: Producción
├── ejercicio_5_2_docker_setup.py
├── ejercicio_5_3_monitoring.py
│
├── proyecto_final.py                # Proyecto integrador
│
├── requirements.txt                 # Dependencias del proyecto
├── Dockerfile                       # Configuración de Docker
├── docker-compose.yml
│
├── MANUAL_PYTHON_AVANZADO_2024.md   # Manuales de referencia
├── MANUAL_DESARROLLO_Y_DESPLIEGUE.md
├── CONTEXTO_DEL_PROYECTO.md
└── README.md                        # Este archivo
```

---

## Recursos Adicionales

### Documentación Incluida

- **MANUAL_PYTHON_AVANZADO_2024.md**: Referencia completa de conceptos avanzados
- **MANUAL_DESARROLLO_Y_DESPLIEGUE.md**: Guía de infraestructura y DevOps
- **CONTEXTO_DEL_PROYECTO.md**: Historia y evolución del proyecto

### Próximos Pasos Sugeridos

Después de completar los ejercicios básicos:

1. Experimenta modificando el corpus de frases
2. Añade nuevas palabras a los léxicos
3. Implementa mejoras (ej. manejo de negaciones)
4. Prueba con datasets más grandes (reviews de productos, tweets)

---

## Contribuciones

¿Encontraste un error o tienes una mejora? ¡Las contribuciones son bienvenidas!

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/mejora`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abre un Pull Request

---

## Licencia

Este proyecto tiene fines educativos. Siéntete libre de usar y modificar el código para tu aprendizaje.

---

## Contacto

¿Preguntas o sugerencias? Abre un issue en este repositorio.

---

**¡Comienza tu viaje en NLP con los ejercicios básicos y construye una base sólida! 🚀**
