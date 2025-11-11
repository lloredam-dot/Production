# 📖 Guía de Despliegue Paso a Paso

**De cero a producción: Tutorial completo para principiantes**

Esta guía te llevará desde la instalación inicial hasta tener un sistema completo de NLP corriendo en Docker, paso a paso, sin asumir conocimientos previos.

---

## 📋 Tabla de Contenidos

1. [Antes de Empezar](#antes-de-empezar)
2. [Fase 1: Configuración del Entorno](#fase-1-configuración-del-entorno)
3. [Fase 2: Ejecutando los Ejercicios (Módulos 1-4)](#fase-2-ejecutando-los-ejercicios-módulos-1-4)
4. [Fase 3: Creando tu API con FastAPI](#fase-3-creando-tu-api-con-fastapi)
5. [Fase 4: Dockerización](#fase-4-dockerización)
6. [Fase 5: Monitoreo y Observabilidad](#fase-5-monitoreo-y-observabilidad)
7. [Fase 6: Despliegue Completo con Docker Compose](#fase-6-despliegue-completo-con-docker-compose)
8. [Solución de Problemas Comunes](#solución-de-problemas-comunes)
9. [Verificación y Testing](#verificación-y-testing)
10. [Próximos Pasos](#próximos-pasos)

---

## 🎯 Antes de Empezar

### ¿Qué vamos a lograr?

Al final de esta guía, tendrás:
- ✅ Un entorno Python configurado correctamente
- ✅ 15 ejercicios ejecutados y entendidos
- ✅ Una API REST funcionando con FastAPI
- ✅ Tu aplicación corriendo en Docker
- ✅ Monitoreo con Prometheus
- ✅ Un sistema completo listo para producción

### ¿Qué necesitas tener instalado?

| Software | Versión Mínima | ¿Dónde descargarlo? |
|----------|---------------|---------------------|
| **Python** | 3.8+ (recomendado 3.12) | https://www.python.org/downloads/ |
| **Docker Desktop** | 24.0+ | https://www.docker.com/products/docker-desktop/ |
| **Git** | 2.30+ | https://git-scm.com/downloads |
| **Editor de código** | Cualquiera | VS Code recomendado: https://code.visualstudio.com/ |

### ¿Cuánto tiempo tomará?

- **Configuración inicial**: 30 minutos
- **Módulos 1-4**: 30-40 horas (distribuidas)
- **Módulo 5 (Despliegue)**: 6-9 horas
- **Total**: Puedes completarlo en 1-2 semanas trabajando 3-4 horas diarias

---

## 🛠️ Fase 1: Configuración del Entorno

### Paso 1.1: Verifica que Python esté instalado

**Windows:**
```cmd
python --version
```

**Linux/Mac:**
```bash
python3 --version
```

**¿Qué esperar?**
```
Python 3.12.0  # O cualquier versión 3.8+
```

**Si no funciona:**
- Descarga Python desde https://www.python.org/downloads/
- En Windows: Marca la opción "Add Python to PATH" durante instalación
- Reinicia tu terminal después de instalar

---

### Paso 1.2: Navega al directorio del proyecto

**Windows:**
```cmd
cd C:\Users\jhonnconnor367\PycharmProjects\dokerizacion
```

**Linux/Mac:**
```bash
cd /ruta/donde/clonaste/dokerizacion
```

**Verifica que estás en el lugar correcto:**
```bash
dir  # Windows
ls   # Linux/Mac
```

**Deberías ver:**
```
ejercicio_1_1.py
ejercicio_1_2.py
...
Dockerfile
requirements.txt
README.md
```

---

### Paso 1.3: Crea un entorno virtual

**¿Por qué?**
Un entorno virtual aísla las dependencias de este proyecto de tu instalación global de Python. Es como tener un Python "privado" solo para este proyecto.

**Windows:**
```cmd
python -m venv .venv
```

**Linux/Mac:**
```bash
python3 -m venv .venv
```

**¿Qué acabas de hacer?**
Creaste una carpeta `.venv` que contiene una copia limpia de Python y pip.

---

### Paso 1.4: Activa el entorno virtual

**Windows (CMD):**
```cmd
.venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Si PowerShell te da error de permisos:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Luego intenta activar de nuevo.

**Linux/Mac:**
```bash
source .venv/bin/activate
```

**¿Cómo saber si funcionó?**
Tu terminal debería mostrar `(.venv)` al inicio de la línea:
```
(.venv) C:\Users\jhonnconnor367\PycharmProjects\dokerizacion>
```

---

### Paso 1.5: Actualiza pip

**Todos los sistemas:**
```bash
python -m pip install --upgrade pip
```

**¿Por qué?**
Asegura que tienes la última versión del instalador de paquetes.

---

### Paso 1.6: Instala las dependencias del proyecto

```bash
pip install -r requirements.txt
```

**Esto instalará:**
- FastAPI (para crear APIs)
- Transformers (para usar modelos de NLP)
- PyTorch (framework de deep learning)
- Pandas (para manipular datos)
- Y 15+ librerías más...

**Tiempo estimado:** 5-10 minutos (dependiendo de tu conexión)

**¿Cómo saber que funcionó?**
```bash
pip list
```

Deberías ver una lista larga de paquetes instalados incluyendo:
- fastapi
- transformers
- torch
- pandas
- etc.

---

### Paso 1.7: Descarga el modelo de spaCy

Algunos ejercicios usan spaCy para análisis de texto. Necesitas descargar su modelo:

```bash
python -m spacy download en_core_web_sm
```

**¿Qué hace esto?**
Descarga un modelo pre-entrenado (50MB) para procesamiento de lenguaje natural en inglés.

---

### ✅ Verificación de la Fase 1

Ejecuta estos comandos para verificar que todo está bien:

```bash
python -c "import fastapi; print('FastAPI OK')"
python -c "import transformers; print('Transformers OK')"
python -c "import torch; print('PyTorch OK')"
python -c "import spacy; print('spaCy OK')"
```

**Si todos imprimen "OK", ¡estás listo para continuar!**

---

## 🎓 Fase 2: Ejecutando los Ejercicios (Módulos 1-4)

### ¿Cómo están organizados los ejercicios?

```
Módulo 1 (Fundamentos Python):
  - ejercicio_1_1.py  # Configuración de asistentes IA
  - ejercicio_1_2.py  # Programación asíncrona
  - ejercicio_1_3.py  # Context managers

Módulo 2 (Recolección de Datos):
  - ejercicio_2_1.py  # APIs financieras
  - ejercicio_2_2.py  # Web scraping
  - ejercicio_2_3.py  # Limpieza y OAuth

Módulo 3 (NLP Moderno):
  - ejercicio_3_1.py  # FinBERT sentiment
  - ejercicio_3_2.py  # NER y POS tagging
  - ejercicio_3_3.py  # Text generation

Módulo 4 (NLP Financiero):
  - ejercicio_4_1.py  # Extracción de datos
  - ejercicio_4_2.py  # Análisis de sentimiento
  - ejercicio_4_3.py  # Predicción con LSTM

Módulo 5 (Producción):
  - ejercicio_5_1.py  # API con FastAPI
  - ejercicio_5_2_docker_setup.py  # Docker
  - ejercicio_5_3_monitoring.py  # Prometheus
```

---

### Paso 2.1: Ejecuta tu primer ejercicio

```bash
python ejercicio_1_1.py
```

**¿Qué hace este ejercicio?**
Configura un asistente de IA (Gemini o DeepSeek) para revisar código.

**Si necesitas API keys:**
- Gemini: https://makersuite.google.com/app/apikey
- DeepSeek: https://platform.deepseek.com/

**¿Qué deberías ver?**
```
=== Configuración de Asistente IA ===
✅ API configurada correctamente
...
```

---

### Paso 2.2: Lee el código antes de ejecutar

**IMPORTANTE:** Antes de ejecutar cada ejercicio, ábrelo en tu editor y lee:
1. Los comentarios al inicio (explican qué hace)
2. Los docstrings de las funciones
3. Los comentarios inline

**Ejemplo:**
```python
# ejercicio_1_2.py
"""
OBJETIVO: Aprender programación asíncrona con async/await
...
"""
```

---

### Paso 2.3: Ejecuta los ejercicios en orden

**Módulo 1:**
```bash
python ejercicio_1_1.py
python ejercicio_1_2.py
python ejercicio_1_3.py
```

**Entre cada ejercicio:**
1. Lee la salida en la terminal
2. Abre el archivo .py y entiende el código
3. Modifica algo pequeño y vuelve a ejecutar
4. Busca los conceptos que no entiendas

**Módulo 2:**
```bash
python ejercicio_2_1.py
python ejercicio_2_2.py
python ejercicio_2_3.py
```

**Nota sobre ejercicio_2_2.py:**
- Usa web scraping, puede tomar tiempo
- Necesitarás ChromeDriver si usas Selenium
- Puedes comentar esa parte si solo quieres probar BeautifulSoup

**Módulo 3:**
```bash
python ejercicio_3_1.py  # Primera vez descargará FinBERT (~500MB)
python ejercicio_3_2.py
python ejercicio_3_3.py  # Puede tomar tiempo, usa GPU si tienes
```

**⚠️ IMPORTANTE sobre Módulo 3:**
- La primera ejecución de 3.1 descargará modelos grandes
- Si no tienes GPU, los modelos correrán en CPU (más lento pero funciona)
- Ten paciencia, es normal que tarde

**Módulo 4:**
```bash
python ejercicio_4_1.py
python ejercicio_4_2.py
python ejercicio_4_3.py  # LSTM training, puede tomar 10-30 min
```

**⚠️ IMPORTANTE sobre ejercicio_4_3.py:**
- Entrena una red LSTM desde cero
- Puede tomar 10-30 minutos dependiendo de tu CPU/GPU
- Verás una barra de progreso por cada época de entrenamiento

---

### Paso 2.4: Toma notas mientras avanzas

Crea un archivo `mis_notas.md` y escribe:
- ¿Qué aprendiste en cada ejercicio?
- ¿Qué conceptos te costaron más?
- ¿Qué modificaciones hiciste?

**Ejemplo:**
```markdown
## Ejercicio 1.2 - Async/await

Aprendí:
- async/await permite ejecutar tareas concurrentemente
- asyncio.gather() corre varias coroutines en paralelo
- Es útil para llamadas a APIs que tardan

Dudas:
- ¿Cuándo usar async vs threading?
- ¿Cómo manejo errores en async?
```

---

### ✅ Verificación de la Fase 2

Has completado esta fase si:
- ✅ Ejecutaste todos los ejercicios de Módulos 1-4
- ✅ Cada uno corrió sin errores fatales
- ✅ Entiendes (al menos básicamente) qué hace cada uno
- ✅ Tienes los modelos descargados (FinBERT, spaCy, etc.)

**No te preocupes si no entiendes TODO a la perfección.** La comprensión profunda viene con la práctica.

---

## 🚀 Fase 3: Creando tu API con FastAPI

### Paso 3.1: Entiende qué es una API REST

**API REST** = Una forma de que programas se comuniquen por internet usando HTTP.

**Analogía:**
Es como un mesero en un restaurante:
- Tú (cliente) haces un pedido (request)
- El mesero lo lleva a la cocina (servidor)
- La cocina prepara tu orden (procesamiento)
- El mesero te trae la comida (response)

**FastAPI** = Una librería de Python que hace súper fácil crear estos "meseros".

---

### Paso 3.2: Ejecuta el servidor FastAPI

```bash
python ejercicio_5_1.py
```

**¿Qué verás?**
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

**¡Tu servidor está vivo! 🎉**

---

### Paso 3.3: Prueba tu API

**Opción 1: Navegador Web**

Abre tu navegador y ve a:
```
http://localhost:8000/docs
```

**¿Qué verás?**
La documentación interactiva de tu API (Swagger UI). Puedes:
- Ver todos los endpoints disponibles
- Probar cada uno haciendo clic en "Try it out"
- Ver las respuestas en tiempo real

**Opción 2: Terminal (curl)**

Abre OTRA terminal (deja la del servidor corriendo) y ejecuta:

```bash
curl http://localhost:8000/health
```

**Respuesta esperada:**
```json
{"status": "healthy", "timestamp": "2025-01-11T10:30:00"}
```

**Opción 3: Postman**

Si tienes Postman:
1. Crea una nueva request GET
2. URL: `http://localhost:8000/health`
3. Click en "Send"

---

### Paso 3.4: Prueba el endpoint de análisis de sentimiento

**En Swagger UI (http://localhost:8000/docs):**

1. Busca el endpoint `POST /analyze/sentiment`
2. Click en "Try it out"
3. En el body JSON, escribe:
```json
{
  "text": "Apple stock is performing great today!"
}
```
4. Click en "Execute"

**Respuesta esperada:**
```json
{
  "sentiment": "positive",
  "score": 0.9234,
  "label": "POSITIVE"
}
```

**¿Qué acaba de pasar?**
1. Enviaste texto a tu API
2. Tu API usó el modelo FinBERT
3. El modelo analizó el sentimiento
4. Te devolvió el resultado en JSON

**¡Acabas de hacer tu primera llamada de NLP en producción!** 🎊

---

### Paso 3.5: Explora todos los endpoints

Tu API tiene varios endpoints. Pruébalos todos en `/docs`:

| Endpoint | Método | ¿Qué hace? |
|----------|--------|------------|
| `/health` | GET | Verifica que el servidor esté vivo |
| `/analyze/sentiment` | POST | Analiza sentimiento de texto |
| `/extract/entities` | POST | Extrae entidades (nombres, empresas) |
| `/predict/price` | POST | Predice tendencia de precio |

---

### Paso 3.6: Detén el servidor

Cuando termines de probar, ve a la terminal donde corre el servidor y presiona:
```
Ctrl + C
```

**Verás:**
```
INFO:     Shutting down
INFO:     Finished server shutdown.
```

---

### ✅ Verificación de la Fase 3

Has completado esta fase si:
- ✅ Lograste iniciar el servidor FastAPI
- ✅ Accediste a http://localhost:8000/docs
- ✅ Probaste al menos 2 endpoints diferentes
- ✅ Recibiste respuestas JSON válidas
- ✅ Entiendes el flujo básico: request → procesamiento → response

---

## 🐳 Fase 4: Dockerización

### ¿Por qué Docker?

**El Problema:**
```
Desarrollador: "En mi máquina funciona 🤷"
Servidor: "Aquí no funciona 💥"
```

**La Solución: Docker**
- Empaqueta tu app + todas sus dependencias
- Funciona igual en tu laptop, servidor, nube
- Es el estándar de la industria para despliegue

---

### Paso 4.1: Verifica que Docker esté instalado

```bash
docker --version
```

**Debes ver algo como:**
```
Docker version 24.0.7, build 24.0.7
```

**Si no está instalado:**
- Windows/Mac: Descarga Docker Desktop de https://www.docker.com/products/docker-desktop/
- Linux: `sudo apt-get install docker.io` (Ubuntu/Debian)

**Verifica que Docker esté corriendo:**
```bash
docker ps
```

Si ves una tabla (aunque esté vacía), Docker está funcionando.

---

### Paso 4.2: Entiende el Dockerfile

Abre el archivo `Dockerfile` en tu editor. Vamos a entenderlo línea por línea:

```dockerfile
# Usa Python 3.12 slim (versión liviana)
FROM python:3.12-slim

# Define el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Descarga el modelo de spaCy
RUN python -m spacy download en_core_web_sm

# Copia todo el código de tu app
COPY . .

# Expone el puerto 8000
EXPOSE 8000

# Comando para iniciar el servidor
CMD ["uvicorn", "ejercicio_5_1:app", "--host", "0.0.0.0", "--port", "8000"]
```

**¿Qué hace cada parte?**
- `FROM`: Imagen base (Python ya instalado)
- `WORKDIR`: Dónde viven tus archivos dentro del contenedor
- `COPY`: Traer archivos de tu máquina al contenedor
- `RUN`: Ejecutar comandos durante la construcción
- `EXPOSE`: Decirle a Docker qué puerto usa tu app
- `CMD`: Comando que corre cuando inicias el contenedor

---

### Paso 4.3: Construye la imagen Docker

```bash
docker build -t nlp-api:latest .
```

**¿Qué hace este comando?**
- `docker build`: Construye una imagen
- `-t nlp-api:latest`: Le pone nombre y etiqueta
- `.`: Usa el Dockerfile del directorio actual

**Tiempo estimado:** 5-10 minutos

**Verás:**
```
[+] Building 240.5s (12/12) FINISHED
Step 1/8 : FROM python:3.12-slim
Step 2/8 : WORKDIR /app
...
Successfully built abc123def456
Successfully tagged nlp-api:latest
```

**Verifica que la imagen se creó:**
```bash
docker images
```

**Deberías ver:**
```
REPOSITORY   TAG      IMAGE ID       CREATED         SIZE
nlp-api      latest   abc123def456   2 minutes ago   2.1GB
```

---

### Paso 4.4: Ejecuta tu contenedor

```bash
docker run -d -p 8000:8000 --name nlp-container nlp-api:latest
```

**Desglosando el comando:**
- `docker run`: Inicia un contenedor
- `-d`: Modo detached (corre en background)
- `-p 8000:8000`: Mapea puerto 8000 del contenedor → 8000 de tu máquina
- `--name nlp-container`: Nombre del contenedor
- `nlp-api:latest`: Imagen a usar

**Verifica que esté corriendo:**
```bash
docker ps
```

**Deberías ver:**
```
CONTAINER ID   IMAGE              STATUS         PORTS                    NAMES
abc123456789   nlp-api:latest     Up 5 seconds   0.0.0.0:8000->8000/tcp   nlp-container
```

---

### Paso 4.5: Prueba tu API Dockerizada

**Abre tu navegador:**
```
http://localhost:8000/docs
```

**Deberías ver la misma UI de Swagger que antes, pero ahora tu app corre dentro de Docker!** 🐳

**Prueba un endpoint:**
```bash
curl http://localhost:8000/health
```

---

### Paso 4.6: Ve los logs del contenedor

```bash
docker logs nlp-container
```

**Verás los mismos logs de Uvicorn:**
```
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Para ver logs en tiempo real:**
```bash
docker logs -f nlp-container
```
(Presiona Ctrl+C para salir)

---

### Paso 4.7: Entra al contenedor (opcional pero educativo)

```bash
docker exec -it nlp-container bash
```

**Ahora estás "dentro" del contenedor.** Es como SSH a otra máquina.

**Prueba algunos comandos:**
```bash
pwd                    # Verás /app
ls                     # Verás tus archivos Python
python --version       # Verás Python 3.12
pip list               # Verás las dependencias instaladas
exit                   # Para salir
```

---

### Paso 4.8: Detén y elimina el contenedor

```bash
# Detener el contenedor
docker stop nlp-container

# Eliminar el contenedor
docker rm nlp-container
```

**Si quieres hacer ambas cosas a la vez:**
```bash
docker rm -f nlp-container
```

---

### ✅ Verificación de la Fase 4

Has completado esta fase si:
- ✅ Construiste la imagen Docker sin errores
- ✅ Iniciaste un contenedor correctamente
- ✅ Accediste a http://localhost:8000/docs desde el contenedor
- ✅ Probaste al menos un endpoint
- ✅ Viste los logs del contenedor
- ✅ Entiendes la diferencia entre imagen y contenedor

**Imagen = Plantilla (como un .exe)**
**Contenedor = Instancia corriendo (como un programa abierto)**

---

## 📊 Fase 5: Monitoreo y Observabilidad

### ¿Por qué monitorear?

**En producción necesitas saber:**
- ¿Está mi servicio vivo?
- ¿Qué tan rápido responde?
- ¿Cuántas requests está manejando?
- ¿Se está quedando sin memoria?

**Prometheus** es la herramienta estándar para esto.

---

### Paso 5.1: Ejecuta el ejercicio de monitoreo

```bash
python ejercicio_5_3_monitoring.py
```

**¿Qué hace este script?**
- Configura métricas de Prometheus
- Expone un endpoint `/metrics`
- Simula tráfico y captura estadísticas

**Deberías ver:**
```
=== Sistema de Monitoreo con Prometheus ===
✅ Servidor iniciado en http://localhost:8000
✅ Métricas disponibles en http://localhost:8000/metrics
...
```

---

### Paso 5.2: Ve las métricas crudas

Abre tu navegador:
```
http://localhost:8000/metrics
```

**Verás algo como:**
```
# HELP nlp_requests_total Total number of NLP requests
# TYPE nlp_requests_total counter
nlp_requests_total{endpoint="/analyze"} 42.0

# HELP nlp_request_duration_seconds Request duration
# TYPE nlp_request_duration_seconds histogram
nlp_request_duration_seconds_bucket{le="0.1"} 35.0
nlp_request_duration_seconds_bucket{le="0.5"} 42.0
...
```

**Estos son los datos que Prometheus consumiría.**

---

### Paso 5.3: Entiende las métricas principales

**Contador (Counter):**
```python
nlp_requests_total{endpoint="/analyze"} 42.0
```
→ Se ha llamado 42 veces al endpoint `/analyze`

**Histograma (Histogram):**
```python
nlp_request_duration_seconds_bucket{le="0.5"} 42.0
```
→ 42 requests tomaron ≤ 0.5 segundos

**Gauge (Medidor):**
```python
nlp_active_requests 5.0
```
→ Hay 5 requests procesándose ahora mismo

---

### Paso 5.4: Integra monitoreo en tu API

El archivo `ejercicio_5_1.py` ya tiene monitoreo integrado. Búscalo:

```python
from prometheus_client import Counter, Histogram, generate_latest

# Definir métricas
REQUEST_COUNT = Counter('api_requests_total', 'Total API requests')
REQUEST_DURATION = Histogram('api_request_duration_seconds', 'Request duration')

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
```

**¡Tu API ya está instrumentada para Prometheus!**

---

### ✅ Verificación de la Fase 5

Has completado esta fase si:
- ✅ Ejecutaste el script de monitoreo
- ✅ Accediste a `/metrics` y viste datos
- ✅ Entiendes qué es un Counter, Histogram y Gauge
- ✅ Sabes que estos datos los consumiría Prometheus

**Nota:** No vamos a instalar Prometheus completo (es complejo), pero tu API ya está preparada para cuando lo necesites.

---

## 🎼 Fase 6: Despliegue Completo con Docker Compose

### ¿Qué es Docker Compose?

**Docker Compose** = Orquestar múltiples contenedores como una sola aplicación.

**Ejemplo:**
- Contenedor 1: Tu API FastAPI
- Contenedor 2: Base de datos PostgreSQL
- Contenedor 3: Redis (caché)
- Contenedor 4: Prometheus (monitoreo)
- Contenedor 5: Nginx (reverse proxy)

**Todos funcionando juntos.**

---

### Paso 6.1: Entiende el archivo docker-compose.yml

Abre `docker-compose.yml`:

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/nlpdb
    depends_on:
      - db
      - redis

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=nlpdb

  redis:
    image: redis:7-alpine

  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
```

**¿Qué define cada sección?**
- `api`: Tu aplicación FastAPI
- `db`: Base de datos PostgreSQL
- `redis`: Caché en memoria
- `prometheus`: Sistema de monitoreo
- `nginx`: Proxy inverso (punto de entrada)

---

### Paso 6.2: Completa las configuraciones (TODO)

El archivo tiene TODOs marcados. Vamos a completarlos:

**TODO 1: Variables de entorno para la API**

Crea un archivo `.env` en el directorio raíz:

```bash
# .env
DATABASE_URL=postgresql://nlpuser:nlppassword@db:5432/nlpdb
REDIS_URL=redis://redis:6379/0
API_SECRET_KEY=tu-clave-secreta-super-segura-cambiame
```

**TODO 2: Configuración de Prometheus**

Crea `prometheus.yml`:

```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'nlp-api'
    static_configs:
      - targets: ['api:8000']
    metrics_path: '/metrics'
```

**TODO 3: Configuración de Nginx**

Crea `nginx.conf`:

```nginx
# nginx.conf
events {
    worker_connections 1024;
}

http {
    upstream api {
        server api:8000;
    }

    server {
        listen 80;

        location / {
            proxy_pass http://api;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
}
```

---

### Paso 6.3: Actualiza docker-compose.yml para usar las configs

Edita `docker-compose.yml` y reemplaza las secciones:

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db
      - redis
    restart: unless-stopped

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: nlpuser
      POSTGRES_PASSWORD: nlppassword
      POSTGRES_DB: nlpdb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    restart: unless-stopped

  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - api
    restart: unless-stopped

volumes:
  postgres_data:
  prometheus_data:
```

---

### Paso 6.4: Levanta todo el stack

```bash
docker-compose up -d
```

**¿Qué hace este comando?**
- Construye las imágenes necesarias
- Inicia todos los contenedores
- Los conecta en una red privada
- `-d`: Corre en background

**Tiempo estimado:** 3-5 minutos (primera vez)

**Verás:**
```
Creating network "dokerizacion_default"
Creating volume "dokerizacion_postgres_data"
Creating dokerizacion_db_1         ... done
Creating dokerizacion_redis_1      ... done
Creating dokerizacion_api_1        ... done
Creating dokerizacion_prometheus_1 ... done
Creating dokerizacion_nginx_1      ... done
```

---

### Paso 6.5: Verifica que todo esté corriendo

```bash
docker-compose ps
```

**Deberías ver algo como:**
```
NAME                    IMAGE              STATUS    PORTS
dokerizacion_api_1      nlp-api:latest     Up        0.0.0.0:8000->8000/tcp
dokerizacion_db_1       postgres:15        Up        5432/tcp
dokerizacion_redis_1    redis:7-alpine     Up        6379/tcp
dokerizacion_prometheus_1 prom/prometheus  Up        0.0.0.0:9090->9090/tcp
dokerizacion_nginx_1    nginx:alpine       Up        0.0.0.0:80->80/tcp
```

**Todos deben tener STATUS = "Up"**

---

### Paso 6.6: Prueba el sistema completo

**1. API a través de Nginx (puerto 80):**
```
http://localhost/docs
```

**2. API directa (puerto 8000):**
```
http://localhost:8000/docs
```

**3. Prometheus (puerto 9090):**
```
http://localhost:9090
```

En Prometheus:
- Ve a "Status" → "Targets"
- Deberías ver `nlp-api` con estado "UP"
- Ve a "Graph" y escribe: `api_requests_total`
- Click "Execute" para ver la métrica

**4. Haz algunas requests para generar datos:**

```bash
curl -X POST http://localhost/analyze/sentiment \
  -H "Content-Type: application/json" \
  -d '{"text": "The market is looking great!"}'
```

Repite varias veces y luego refresca Prometheus.

---

### Paso 6.7: Ve los logs de todos los servicios

```bash
# Logs de todos los servicios
docker-compose logs

# Logs solo de la API
docker-compose logs api

# Logs en tiempo real
docker-compose logs -f api
```

---

### Paso 6.8: Detén todo el stack

```bash
docker-compose down
```

**Para eliminar también los volúmenes (base de datos):**
```bash
docker-compose down -v
```

---

### ✅ Verificación de la Fase 6

Has completado esta fase si:
- ✅ Levantaste todo el stack con `docker-compose up`
- ✅ Todos los contenedores están "Up"
- ✅ Accediste a la API vía Nginx (puerto 80)
- ✅ Viste métricas en Prometheus (puerto 9090)
- ✅ Hiciste requests y las métricas se actualizaron
- ✅ Detuviste todo con `docker-compose down`

**¡Felicitaciones! Acabas de desplegar un sistema completo de microservicios. 🎉**

---

## 🔧 Solución de Problemas Comunes

### Problema 1: "ModuleNotFoundError: No module named 'fastapi'"

**Causa:** No activaste el entorno virtual o no instalaste dependencias.

**Solución:**
```bash
# Activa el entorno virtual
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Instala dependencias
pip install -r requirements.txt
```

---

### Problema 2: "Port 8000 is already in use"

**Causa:** Ya hay algo corriendo en el puerto 8000.

**Solución Windows:**
```cmd
# Encuentra qué proceso usa el puerto
netstat -ano | findstr :8000

# Mata el proceso (reemplaza PID con el número que viste)
taskkill /PID <PID> /F
```

**Solución Linux/Mac:**
```bash
# Encuentra el proceso
lsof -i :8000

# Mata el proceso
kill -9 <PID>
```

**O simplemente usa otro puerto:**
```bash
uvicorn ejercicio_5_1:app --port 8001
```

---

### Problema 3: Docker build falla con "No space left on device"

**Causa:** Docker se quedó sin espacio.

**Solución:**
```bash
# Limpia contenedores e imágenes no usados
docker system prune -a

# Limpia volúmenes
docker volume prune
```

---

### Problema 4: Transformers descarga modelos muy lento

**Causa:** Conexión lenta o servidor de Hugging Face saturado.

**Solución:**
```python
# Usa cache local si ya descargaste antes
from transformers import pipeline
classifier = pipeline('sentiment-analysis',
                     model='ProsusAI/finbert',
                     local_files_only=True)  # Solo usar cache local
```

---

### Problema 5: "RuntimeError: CUDA out of memory"

**Causa:** Estás intentando usar GPU pero no hay memoria suficiente.

**Solución:**
```python
# Fuerza uso de CPU
import torch
device = torch.device("cpu")

# Al cargar modelos
model = AutoModel.from_pretrained("ProsusAI/finbert").to(device)
```

---

### Problema 6: Docker Compose no encuentra archivo .env

**Causa:** El archivo .env no está en el directorio correcto.

**Solución:**
```bash
# El .env debe estar en el mismo directorio que docker-compose.yml
cd C:\Users\jhonnconnor367\PycharmProjects\dokerizacion

# Verifica que existe
dir .env  # Windows
ls -la .env  # Linux/Mac

# Si no existe, créalo
echo DATABASE_URL=postgresql://nlpuser:nlppassword@db:5432/nlpdb > .env
```

---

### Problema 7: PostgreSQL no acepta conexiones

**Causa:** El contenedor de la DB no terminó de inicializarse.

**Solución:**
```bash
# Ve los logs
docker-compose logs db

# Espera a ver este mensaje:
# "database system is ready to accept connections"

# Si tarda mucho, reinicia
docker-compose restart db
```

---

### Problema 8: Prometheus no scrapes las métricas

**Causa:** Configuración incorrecta de prometheus.yml o la API no expone /metrics.

**Solución:**

1. Verifica que la API exponga métricas:
```bash
curl http://localhost:8000/metrics
```

2. Verifica prometheus.yml:
```yaml
scrape_configs:
  - job_name: 'nlp-api'
    static_configs:
      - targets: ['api:8000']  # ← Debe ser 'api', no 'localhost'
```

3. Reinicia Prometheus:
```bash
docker-compose restart prometheus
```

---

## ✅ Verificación y Testing

### Checklist Final

Antes de dar por terminado el proyecto, verifica:

**Entorno Local:**
- [ ] Entorno virtual activo
- [ ] Todas las dependencias instaladas
- [ ] Modelos de NLP descargados (FinBERT, spaCy)

**Ejercicios:**
- [ ] Módulo 1 (1.1, 1.2, 1.3) completados
- [ ] Módulo 2 (2.1, 2.2, 2.3) completados
- [ ] Módulo 3 (3.1, 3.2, 3.3) completados
- [ ] Módulo 4 (4.1, 4.2, 4.3) completados

**API Local:**
- [ ] Servidor FastAPI inicia sin errores
- [ ] `/docs` accesible y funcional
- [ ] Al menos 3 endpoints probados exitosamente
- [ ] `/metrics` expone datos de Prometheus

**Docker:**
- [ ] Imagen construida exitosamente
- [ ] Contenedor corre sin errores
- [ ] API accesible desde contenedor
- [ ] Logs visibles con `docker logs`

**Docker Compose:**
- [ ] Todos los servicios (api, db, redis, prometheus, nginx) corren
- [ ] API accesible vía Nginx (puerto 80)
- [ ] Prometheus scrapes métricas (puerto 9090)
- [ ] Base de datos acepta conexiones

**Documentación:**
- [ ] README.md leído completamente
- [ ] DIAPOSITIVAS.md revisado
- [ ] Esta guía seguida paso a paso

---

### Script de Testing Automatizado

Crea un archivo `test_deployment.py`:

```python
"""
Script para verificar que todo el despliegue funciona correctamente.
"""
import requests
import time

def test_api_health():
    """Verifica que la API esté viva"""
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        assert response.status_code == 200
        print("✅ API health check: OK")
        return True
    except Exception as e:
        print(f"❌ API health check: FAILED - {e}")
        return False

def test_sentiment_analysis():
    """Verifica análisis de sentimiento"""
    try:
        payload = {"text": "The stock market is doing great!"}
        response = requests.post("http://localhost:8000/analyze/sentiment",
                                json=payload, timeout=10)
        assert response.status_code == 200
        data = response.json()
        assert "sentiment" in data
        print(f"✅ Sentiment analysis: OK (sentiment={data['sentiment']})")
        return True
    except Exception as e:
        print(f"❌ Sentiment analysis: FAILED - {e}")
        return False

def test_metrics():
    """Verifica que las métricas estén disponibles"""
    try:
        response = requests.get("http://localhost:8000/metrics", timeout=5)
        assert response.status_code == 200
        assert "api_requests_total" in response.text
        print("✅ Prometheus metrics: OK")
        return True
    except Exception as e:
        print(f"❌ Prometheus metrics: FAILED - {e}")
        return False

def test_prometheus():
    """Verifica que Prometheus esté corriendo"""
    try:
        response = requests.get("http://localhost:9090/-/healthy", timeout=5)
        assert response.status_code == 200
        print("✅ Prometheus server: OK")
        return True
    except Exception as e:
        print(f"❌ Prometheus server: FAILED - {e}")
        return False

def main():
    print("=== Testing Deployment ===\n")

    tests = [
        test_api_health,
        test_sentiment_analysis,
        test_metrics,
        test_prometheus
    ]

    results = [test() for test in tests]

    print(f"\n=== Results: {sum(results)}/{len(results)} tests passed ===")

    if all(results):
        print("🎉 ¡Todo funciona correctamente!")
        return 0
    else:
        print("⚠️  Algunos tests fallaron. Revisa los errores arriba.")
        return 1

if __name__ == "__main__":
    exit(main())
```

**Ejecuta el test:**
```bash
# Primero levanta el stack
docker-compose up -d

# Espera 30 segundos para que todo inicie
sleep 30

# Ejecuta los tests
python test_deployment.py
```

---

## 🚀 Próximos Pasos

### Has completado el proyecto base. ¿Qué sigue?

#### Nivel 1: Mejoras Rápidas (1-2 horas cada una)

1. **Agregar autenticación JWT**
   - Protege tus endpoints con tokens
   - Ejercicio 5.1 tiene ejemplos comentados

2. **Implementar rate limiting**
   - Prevenir abuso de la API
   - Usa `slowapi` o Redis

3. **Agregar logging estructurado**
   - Reemplaza prints con `logging`
   - Usa formato JSON para logs

4. **Crear tests unitarios**
   - Usa `pytest`
   - Cubre al menos los endpoints principales

#### Nivel 2: Mejoras Intermedias (4-8 horas cada una)

5. **Base de datos real**
   - Implementa SQLAlchemy o SQLModel
   - Guarda resultados de análisis en PostgreSQL
   - Crea endpoints para consultar histórico

6. **Cache con Redis**
   - Cachea resultados de modelos pesados
   - Reduce tiempo de respuesta en 50-80%

7. **Async task queue**
   - Usa Celery + Redis
   - Procesa análisis largos en background

8. **CI/CD con GitHub Actions**
   - Automatiza tests
   - Construye y publica imagen Docker automáticamente

#### Nivel 3: Proyectos Avanzados (1-2 semanas)

9. **Dashboard interactivo con Streamlit**
   - Visualiza tendencias de sentimiento
   - Gráficos en tiempo real

10. **Despliegue en la nube**
    - AWS ECS o Google Cloud Run
    - Configura dominio y HTTPS
    - Implementa auto-scaling

11. **Agregador de múltiples fuentes**
    - Twitter API para tweets en tiempo real
    - NewsAPI para artículos de noticias
    - Yahoo Finance para datos de mercado

12. **Sistema de alertas**
    - Notificaciones cuando sentimiento cambia drásticamente
    - Integración con Slack, Email, Telegram

---

### Recursos para Continuar Aprendiendo

**Documentación:**
- FastAPI: https://fastapi.tiangolo.com/tutorial/
- Transformers: https://huggingface.co/course
- Docker: https://docs.docker.com/get-started/

**Cursos (gratis):**
- FastAPI Full Tutorial: YouTube (freeCodeCamp)
- Hugging Face NLP Course: https://huggingface.co/learn/nlp-course
- Docker for Beginners: Docker.com

**Libros:**
- "FastAPI - Modern Python Web Development" (Bill Lubanovic)
- "Natural Language Processing with Transformers" (Lewis Tunstall)
- "Docker Deep Dive" (Nigel Poulton)

**Comunidades:**
- r/FastAPI (Reddit)
- Hugging Face Discord
- Docker Community Forums

---

## 🎓 Certificación de Completitud

**Si llegaste hasta aquí y completaste todas las fases, ¡felicitaciones!**

Has demostrado que puedes:
- ✅ Configurar entornos Python profesionales
- ✅ Implementar modelos de NLP state-of-the-art
- ✅ Crear APIs REST con FastAPI
- ✅ Dockerizar aplicaciones
- ✅ Orquestar múltiples servicios con Docker Compose
- ✅ Implementar monitoreo y observabilidad
- ✅ Seguir guías técnicas y resolver problemas

**Estas habilidades son valiosas en:**
- Ingeniero de Machine Learning
- Backend Developer
- MLOps Engineer
- Data Engineer
- DevOps Engineer

---

## 📝 Feedback y Contribuciones

**¿Encontraste un error en esta guía?**
- Abre un issue en el repo

**¿Tienes sugerencias de mejora?**
- Envía un pull request

**¿Completaste el proyecto?**
- Comparte tu experiencia: ¿qué aprendiste? ¿qué fue difícil?

---

## 🙏 Agradecimientos

Esta guía fue creada para ayudar a desarrolladores a dar el salto de "código que funciona localmente" a "servicios en producción".

Si esta guía te ayudó, considera:
- ⭐ Darle estrella al repositorio
- 📢 Compartirla con otros desarrolladores
- 💬 Dejar feedback para mejorarla

---

**¡Éxito en tu viaje de aprendizaje! 🚀**

---

**Última actualización:** Enero 2025
**Versión:** 1.0
**Proyecto:** Del Código al Despliegue - NLP en Producción
