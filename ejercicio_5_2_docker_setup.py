# Archivo: ejercicio_5_2_docker_setup.py

"""
EJERCICIO: Containerizar la aplicación con Docker
1. Crear Dockerfile optimizado
2. Docker Compose para servicios múltiples
3. Configuración de producción
"""

# Dockerfile
dockerfile_content = """
# TODO: Completar Dockerfile
FROM python:3.12-slim

# Configurar variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \\
    PYTHONUNBUFFERED=1 \\
    PYTHONPATH=/app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \\
    # TODO: Agregar dependencias necesarias
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# TODO: Copiar y instalar requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# TODO: Copiar código de aplicación
COPY . .

# TODO: Crear usuario no-root para seguridad

# TODO: Configurar health check

# TODO: Exponer puerto

# TODO: Comando de inicio
"""

# docker-compose.yml
docker_compose_content = """
# TODO: Completar docker-compose.yml
version: '3.8'

services:
  # Servicio principal de la API
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      # TODO: Variables de entorno
    depends_on:
      # TODO: Dependencias
    volumes:
      # TODO: Volúmenes para logs y modelos
    restart: unless-stopped
    healthcheck:
      # TODO: Health check

  # Base de datos PostgreSQL
  db:
    image: postgres:15
    environment:
      # TODO: Configuración de PostgreSQL
    volumes:
      # TODO: Persistencia de datos
    ports:
      - "5432:5432"

  # Redis para cache
  redis:
    image: redis:7-alpine
    # TODO: Configuración de Redis

  # Nginx como reverse proxy
  nginx:
    image: nginx:alpine
    # TODO: Configuración de Nginx

  # Prometheus para métricas
  prometheus:
    image: prom/prometheus
    # TODO: Configuración de monitoreo

volumes:
  # TODO: Definir volúmenes

networks:
  # TODO: Definir redes
"""

# nginx.conf
nginx_config = """
# TODO: Configuración de Nginx
events {
    worker_connections 1024;
}

http {
    upstream api {
        # TODO: Configurar upstream
    }
    
    server {
        listen 80;
        
        # TODO: Configurar proxy pass
        # TODO: Configurar SSL
        # TODO: Configurar rate limiting
    }
}
"""

def create_docker_files():
    """
    TODO: Crear archivos de Docker
    1. Escribir Dockerfile
    2. Escribir docker-compose.yml
    3. Crear configuraciones adicionales
    """
    pass

def build_and_test_container():
    """
    TODO: Construir y probar contenedor
    1. docker build
    2. docker run con tests
    3. Verificar health checks
    """
    pass

# Comandos útiles de Docker
docker_commands = """
# TODO: Documentar comandos útiles

# Construir imagen
docker build -t financial-ml-api .

# Ejecutar contenedor
docker run -p 8000:8000 financial-ml-api

# Ejecutar con docker-compose
docker-compose up -d

# Ver logs
docker-compose logs -f api

# Escalar servicios
docker-compose up -d --scale api=3

# Actualizar servicios
docker-compose pull && docker-compose up -d

# Backup de base de datos
docker-compose exec db pg_dump -U user financial_db > backup.sql
"""
