# ⚡ Guía Rápida: Entender Docker en 30 Minutos

**Guía visual y compacta para entender tu proyecto dockerizado**

---

## 🎯 Visión General en 1 Minuto

### Tu Sistema

```
INTERNET (Usuario)
    ↓
┌───────────────────────────────────────────────────┐
│  🌐 NGINX (Puerto 80)                             │
│  • Recibe requests                                │
│  • Rate limiting (10 req/s)                       │
│  • SSL/HTTPS                                      │
└─────────────┬─────────────────────────────────────┘
              ↓
┌─────────────▼─────────────────────────────────────┐
│  🚀 FastAPI (Puerto 8000)                         │
│  • Análisis de sentimiento                        │
│  • Predicciones LSTM                              │
│  • Endpoints REST                                 │
└──────────┬────────────────────┬───────────────────┘
           ↓                    ↓
    ┌──────▼────────┐    ┌──────▼────────┐
    │ 🗄️ PostgreSQL │    │ 🔴 Redis      │
    │ (Puerto 5432) │    │ (Puerto 6379) │
    │ • Datos       │    │ • Cache       │
    │ • Predicciones│    │ • Sesiones    │
    └───────────────┘    └───────────────┘
           ↓
    ┌──────▼────────┐
    │ 📊 Prometheus │
    │ (Puerto 9090) │
    │ • Métricas    │
    └───────────────┘
```

---

## 📦 Los 5 Servicios

### Resumen de 1 línea cada uno:

| Servicio | ¿Qué hace? | Puerto | ¿Para qué? |
|----------|------------|--------|------------|
| **Nginx** | Puerta de entrada | 80 | Proxy, seguridad, SSL |
| **API** | Tu aplicación FastAPI | 8000 | Lógica de negocio, ML |
| **PostgreSQL** | Base de datos | 5432 | Guardar datos permanentes |
| **Redis** | Cache en memoria | 6379 | Velocidad, rate limiting |
| **Prometheus** | Monitoreo | 9090 | Ver métricas, alertas |

---

## 🔑 Conceptos Clave (5 minutos)

### 1. Contenedor vs Imagen

```
Imagen (Dockerfile)          Contenedor (docker-compose up)
      ↓                                ↓
   [Receta]                         [Comida]

• Es un template            • Es una instancia corriendo
• Inmutable                 • Tiene estado
• Se construye 1 vez        • Se puede arrancar/parar
```

**Analogía**: Imagen = programa instalado, Contenedor = programa ejecutándose

---

### 2. Volúmenes (Persistencia)

```
SIN VOLUMEN:
┌─────────────┐
│ Contenedor  │    docker-compose down
│ [datos]     │    →  💥 DATOS PERDIDOS
└─────────────┘

CON VOLUMEN:
┌─────────────┐
│ Contenedor  │    docker-compose down
│      ↓      │    →  ✅ Datos en disco
└──────┬──────┘
       ↓
  💾 Volumen
  (persiste)
```

**3 volúmenes en tu proyecto:**
- `postgres_data` → Base de datos (10,000 registros)
- `redis_data` → Cache (resultados de análisis)
- `api_cache` → Modelos ML (500MB, no re-descargar)

---

### 3. Redes (Comunicación)

```
TU PC                    DOCKER

localhost:80  →  [Nginx]
                    ↓
                 [API] ←→ [PostgreSQL]
                    ↓
                 [Redis]

MAGIA: "db" resuelve a IP de PostgreSQL
```

**¿Cómo funciona?**
```python
# En tu código:
DATABASE_URL = "postgresql://user:pass@db:5432/mydb"
                                      ↑↑
                      Docker DNS convierte "db" → 172.18.0.3
```

**Prueba:**
```bash
docker-compose exec api ping db
# ✅ Responde (db existe en la red Docker)
```

---

### 4. Puertos (Mapeo)

```
docker-compose.yml:
ports:
  - "8000:8000"
     ↑↑↑↑  ↑↑↑↑
     Host  Container

TU PC              DOCKER
Puerto 8000  →  Puerto 8000 (contenedor)
```

**Ejemplo práctico:**
```yaml
ports:
  - "80:8000"

# Significa:
localhost:80 → contenedor:8000
```

---

### 5. Healthcheck (¿Está vivo?)

```
Sin healthcheck:
docker ps  →  STATUS: Up 5 minutes
              (¿Pero funciona? 🤷)

Con healthcheck:
docker ps  →  STATUS: Up 5 minutes (healthy) ✅
              (¡Sí funciona!)
```

**Cómo funciona:**
```yaml
healthcheck:
  test: curl http://localhost:8000/health
  interval: 30s     # ← Cada 30 segundos
  retries: 3        # ← 3 fallos = unhealthy

Timeline:
0s:  ✅ Check 1 pasa
30s: ✅ Check 2 pasa
60s: ❌ Check 3 falla
90s: ❌ Check 4 falla
120s: ❌ Check 5 falla → UNHEALTHY
```

---

## 🏗️ Arquitectura Visual

### Flujo de un Request

```
1. Usuario → http://localhost/analyze/sentiment

2. Nginx recibe
   • Verifica rate limit (10 req/s)
   • Proxy pass → API

3. API recibe
   • Verifica en Redis cache
   • Si no existe:
     - Procesa con FinBERT
     - Guarda en Redis (1 hora)
     - Guarda en PostgreSQL

4. API responde
   • JSON con sentimiento
   • Headers de seguridad (Nginx)

5. Prometheus registra
   • Tiempo de respuesta
   • Status code
   • Endpoint usado
```

---

## 📁 Archivo docker-compose.yml Simplificado

### Estructura básica:

```yaml
version: '3.8'

services:           # ← Lista de contenedores

  api:              # ← Tu aplicación
    build: .        # ← Construir desde Dockerfile
    ports:          # ← Exponer puertos
      - "8000:8000"
    environment:    # ← Variables de config
      - DATABASE_URL=postgresql://...
    depends_on:     # ← Esperar a otros servicios
      - db
    volumes:        # ← Persistencia
      - ./logs:/app/logs
    restart: unless-stopped  # ← Reiniciar si crashea

  db:               # ← PostgreSQL
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:            # ← Declarar volúmenes
  postgres_data:

networks:           # ← Redes de comunicación
  backend:
```

---

## 🎬 Ciclo de Vida

### ¿Qué pasa cuando ejecutas comandos?

#### `docker-compose up -d`
```
Paso 1: Leer docker-compose.yml
Paso 2: Crear redes (frontend, backend)
Paso 3: Crear volúmenes (postgres_data, etc.)
Paso 4: Construir imágenes (si build: .)
Paso 5: Arrancar servicios en orden:
        db → redis → api → nginx → prometheus
Paso 6: Ejecutar healthchecks
Paso 7: Reportar estado

Tiempo: ~30 segundos (primera vez: ~2 min)
```

#### `docker-compose down`
```
Paso 1: Parar contenedores (gracefully)
Paso 2: Eliminar contenedores
Paso 3: Eliminar redes
Paso 4: ✅ MANTENER volúmenes (datos persisten)

Tiempo: ~5 segundos
```

#### `docker-compose down -v`
```
⚠️ TODO lo anterior +
Paso 5: 💥 ELIMINAR VOLÚMENES (datos perdidos)
```

---

## 🔧 Variables de Entorno Explicadas

### Las 5 más importantes:

```bash
# 1. DATABASE_URL
DATABASE_URL=postgresql://postgres:secretpassword@db:5432/financial_db
             └─────┬─────┘ └────┬────┘ └┬┘└──┬─┘ └─────┬──────┘
                  user      password   host port    database

# 2. REDIS_URL
REDIS_URL=redis://redis:6379/0
                  └─┬─┘ └─┬┘ └┬┘
                  host port db_number

# 3. SECRET_KEY (para JWT)
SECRET_KEY=8f7a2b9c3d4e5f6a7b8c9d0e1f2a3b4c
# Generar: openssl rand -hex 32

# 4. ENVIRONMENT
ENVIRONMENT=production    # o development

# 5. LOG_LEVEL
LOG_LEVEL=info           # debug, info, warning, error
```

---

## 🎯 Configuraciones Críticas Explicadas

### API Service

```yaml
api:
  # 🏗️ BUILD
  build: .              # Construir desde Dockerfile local

  # 🌐 NETWORKING
  ports:
    - "8000:8000"       # localhost:8000 → container:8000
  networks:
    - frontend          # Nginx puede acceder
    - backend           # Puede acceder a db/redis

  # 🔗 DEPENDENCIES
  depends_on:
    db:
      condition: service_healthy    # ⏳ Espera a que db esté OK

  # ⚙️ CONFIGURATION
  environment:
    - DATABASE_URL=...              # Dónde está la DB
    - REDIS_URL=...                 # Dónde está Redis

  # 💾 PERSISTENCE
  volumes:
    - ./logs:/app/logs              # Logs en tu PC
    - api_cache:/app/.cache         # Cache de modelos ML

  # 🔄 RESILIENCE
  restart: unless-stopped           # Auto-reiniciar si crashea

  # ❤️ HEALTH
  healthcheck:
    test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
    interval: 30s                   # Chequear cada 30s
    retries: 3                      # 3 fallos = unhealthy
```

### PostgreSQL Service

```yaml
db:
  # 📦 IMAGE
  image: postgres:15                # Pre-construida de Docker Hub

  # ⚙️ CONFIG
  environment:
    POSTGRES_DB: financial_db       # Crear esta DB
    POSTGRES_PASSWORD: secret       # ⚠️ Cambiar en producción

  # 💾 DATA
  volumes:
    - postgres_data:/var/lib/postgresql/data  # Persistencia

  # 🔐 SECURITY
  networks:
    - backend                       # Solo API puede acceder
```

### Redis Service

```yaml
redis:
  image: redis:7-alpine             # Versión ligera (29MB vs 116MB)

  command: redis-server --appendonly yes    # Persistencia AOF

  volumes:
    - redis_data:/data              # Guardar cache en disco
```

### Nginx Service

```yaml
nginx:
  image: nginx:alpine

  ports:
    - "80:80"                       # HTTP
    - "443:443"                     # HTTPS (cuando tengas SSL)

  volumes:
    - ./nginx.conf:/etc/nginx/nginx.conf:ro  # :ro = read-only

  depends_on:
    api:
      condition: service_healthy    # Esperar a que API funcione
```

---

## 🚨 Top 5 Errores y Soluciones

### 1. "Port already in use"
```
Error: Bind for 0.0.0.0:80 failed: port is already allocated

Causa: Otro servicio usa puerto 80 (Apache, IIS, otro Nginx)

Solución:
# Opción A: Cambiar puerto
ports:
  - "8080:80"  # Usar 8080 en lugar de 80

# Opción B: Parar el otro servicio
netstat -ano | findstr :80     # Ver quién usa el puerto
taskkill /PID <PID> /F         # Matar proceso
```

### 2. "unhealthy" status
```
docker ps
NAME    STATUS
api     Up 5 minutes (unhealthy)  ← ⚠️

Causa: Healthcheck falla (API no responde)

Debug:
# Ver logs:
docker-compose logs api

# Probar healthcheck manualmente:
docker-compose exec api curl http://localhost:8000/health

# Ver detalle de health:
docker inspect financial_ml_api | grep -A 10 Health

Soluciones:
1. Aumentar start_period (API tarda en arrancar)
2. Verificar que endpoint /health existe
3. Instalar curl en el contenedor
```

### 3. "Connection refused" a database
```
api_1 | sqlalchemy.exc.OperationalError:
could not connect to server: Connection refused

Causa: API arranca antes que PostgreSQL

Solución:
depends_on:
  db:
    condition: service_healthy  ← ⚠️ IMPORTANTE
```

### 4. "No space left on device"
```
Error: no space left on device

Causa: Docker usa mucho espacio (imágenes viejas, logs)

Solución:
# Limpiar TODO (⚠️ cuidado):
docker system prune -a --volumes

# Limpiar solo imágenes:
docker image prune -a

# Ver espacio usado:
docker system df
```

### 5. Datos perdidos después de down
```
Causa: Usaste docker-compose down -v

Regla de oro:
docker-compose down      # ✅ Mantiene volúmenes
docker-compose down -v   # ❌ BORRA volúmenes

Prevención:
# Backup antes de down -v:
docker-compose exec db pg_dump -U postgres financial_db > backup.sql
```

---

## 📊 Comparación: Con vs Sin Docker

### Sin Docker
```
Tu PC:
├─ Instalar Python 3.12
├─ Instalar PostgreSQL
├─ Instalar Redis
├─ Instalar Nginx
├─ Configurar cada uno
├─ Gestionar ports conflicts
├─ Actualizar manualmente
└─ "Works on my machine" 🤷

Nuevo developer:
• 2-3 horas de setup
• Problemas de versiones
• Conflictos de puertos
```

### Con Docker
```
Docker:
├─ docker-compose up -d
└─ ✅ Todo funcionando

Nuevo developer:
• 5 minutos de setup
• Versiones consistentes
• Sin conflictos
```

---

## 🎓 Comandos Esenciales (los 10 que más usarás)

```bash
# 1. Arrancar todo
docker-compose up -d

# 2. Ver logs
docker-compose logs -f api

# 3. Ver estado
docker-compose ps

# 4. Parar todo
docker-compose down

# 5. Reiniciar un servicio
docker-compose restart api

# 6. Entrar a un contenedor
docker-compose exec api bash

# 7. Ver variables de entorno
docker-compose exec api env

# 8. Limpiar imágenes viejas
docker image prune -a

# 9. Ver uso de recursos
docker stats

# 10. Backup de base de datos
docker-compose exec db pg_dump -U postgres financial_db > backup.sql
```

---

## 🔍 Debug en 3 Pasos

### Cuando algo no funciona:

```
Paso 1: Ver logs
docker-compose logs -f [servicio]

Paso 2: Ver estado
docker-compose ps
# Busca: (unhealthy), Restarting, Exit code

Paso 3: Entrar y probar
docker-compose exec [servicio] bash
# Ejecuta comandos dentro del contenedor
```

### Ejemplo práctico:

```bash
# API no responde

# 1. Ver logs:
docker-compose logs -f api
# Output: ImportError: No module named 'fastapi'

# 2. Verificar:
docker-compose ps
# Output: api Exit 1

# 3. Solución:
# Rebuild con dependencias:
docker-compose build api
docker-compose up -d api
```

---

## 🎯 Checklist Antes de Producción

```
Seguridad:
☐ SECRET_KEY cambiado (openssl rand -hex 32)
☐ Passwords cambiados (no usar "secretpassword")
☐ Archivo .env NO commiteado a git
☐ Puertos innecesarios NO expuestos
☐ SSL/HTTPS configurado en Nginx

Persistencia:
☐ Volúmenes definidos para datos críticos
☐ Backup strategy implementado
☐ Testear restore de backups

Monitoring:
☐ Prometheus scrapeando métricas
☐ Healthchecks implementados
☐ Alertas configuradas

Performance:
☐ Resource limits definidos
☐ Logs con rotation
☐ Cache (Redis) funcionando
```

---

## 🚀 Workflow de Desarrollo

### Día a día:

```bash
# Mañana (arrancar)
docker-compose up -d
docker-compose logs -f  # Ver que todo arranca OK

# Durante el día (modificar código)
# Editas ejercicio_5_1.py
docker-compose restart api  # Reiniciar solo API

# Si cambias Dockerfile o requirements.txt
docker-compose build api
docker-compose up -d api

# Tarde (parar)
docker-compose down  # Sin -v para mantener datos
```

---

## 💡 Analogías para Entender

### Docker Compose = Director de Orquesta

```
Director (docker-compose.yml):
  "Postgres, empieza primero"
  "Redis, tú después"
  "API, espera a que Postgres esté listo"
  "Nginx, tú al final"

Músicos (servicios):
  • Cada uno tiene su partitura (configuración)
  • Se comunican entre sí (redes)
  • Mantienen su estado (volúmenes)
```

### Volúmenes = USB

```
Contenedor = Computadora
Volumen = USB

Apagas la computadora (docker-compose down):
  • Todo en RAM se pierde
  • ✅ USB mantiene los datos

Prendes otra computadora (docker-compose up):
  • Conectas el mismo USB
  • ✅ Datos siguen ahí
```

### Healthcheck = Enfermera

```
Enfermera (healthcheck):
  Cada 30 segundos:
    "¿Cómo te sientes?" (curl /health)

Paciente (contenedor):
  • "Bien" ✅ → healthy
  • "Mal" ❌ (3 veces) → unhealthy
  • No responde → reiniciar
```

---

## 📚 Recursos Rápidos

### Cuando necesites más detalle:

| Tema | Archivo | Tiempo |
|------|---------|--------|
| **Setup inicial** | QUICK_START.md | 5 min |
| **Comandos** | DOCKER_CHEATSHEET.md | 10 min |
| **Todo en detalle** | GUIA_DOCKER_COMPOSE.md | 2-3 horas |
| **Navegación** | DOCKER_INDEX.md | 10 min |

---

## ✅ Test de Comprensión

### ¿Entendiste? Responde mentalmente:

1. ¿Qué hace `docker-compose up -d`?
2. ¿Cuál es la diferencia entre imagen y contenedor?
3. ¿Para qué sirven los volúmenes?
4. ¿Cómo se comunican los servicios entre sí?
5. ¿Qué hace un healthcheck?
6. ¿Cuándo se pierden los datos?
7. ¿Qué hace Nginx en la arquitectura?
8. ¿Por qué usar Redis además de PostgreSQL?

**Respuestas rápidas:**
1. Arranca todos los servicios en background
2. Imagen = receta, Contenedor = plato cocinado
3. Para que los datos persistan entre reinicios
4. Via nombres de servicios (Docker DNS)
5. Verifica que el servicio funciona realmente
6. Con `docker-compose down -v` (la flag -v)
7. Reverse proxy, seguridad, rate limiting
8. Redis es rápido (memoria), PostgreSQL es permanente (disco)

---

## 🎯 Próximos Pasos

```
☐ 1. Ejecutar: docker-compose up -d
☐ 2. Abrir: http://localhost/docs
☐ 3. Probar endpoints en Swagger UI
☐ 4. Ver métricas: http://localhost:9090
☐ 5. Ver logs: docker-compose logs -f
☐ 6. Leer DOCKER_CHEATSHEET.md para comandos
☐ 7. Cuando tengas dudas, consultar GUIA_DOCKER_COMPOSE.md
```

---

**Tiempo de lectura**: 20-30 minutos
**Nivel**: Principiante → Intermedio
**Prerequisitos**: Saber qué es Docker (concepto básico)

**¿Listo para arrancar?** → `docker-compose up -d` 🚀
