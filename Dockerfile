# Usamos una imagen ligera de Python como base
FROM python:3.12-slim

# --- BUENAS PRÁCTICAS DE ENTORNO ---
# Evita que Python escriba archivos .pyc y asegura que los logs se muestren al instante
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Actualiza el sistema e instala dependencias que podríamos necesitar (ej. para compilar librerías)
# Limpiamos la caché de apt para mantener la imagen ligera
RUN apt-get update && apt-get install -y build-essential \
    && rm -rf /var/lib/apt/lists/*

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# --- MANEJO DE DEPENDENCIAS ---
# Copiamos solo el archivo de requerimientos primero.
# Docker cacheará este paso. Si no cambiamos requirements.txt, no volverá a instalar todo.
COPY requirements.txt .

# Instalamos las dependencias. --no-cache-dir ahorra espacio.
RUN pip install --no-cache-dir -r requirements.txt

# --- COPIAR CÓDIGO DE LA APLICACIÓN ---
# Ahora copiamos el resto del código. Gracias al .dockerignore, no copiaremos archivos innecesarios.
COPY . .

# --- CONFIGURACIÓN DE RED ---
# Le decimos a Docker que el contenedor escuchará en el puerto 8000
EXPOSE 8000

# --- COMANDO DE INICIO (PRODUCCIÓN) ---
# Este es el comando que se ejecutará cuando el contenedor inicie.
# Usamos uvicorn directamente, sin el auto-reloader, que es más eficiente para producción.
# host 0.0.0.0 es crucial para que sea accesible desde fuera del contenedor.
CMD ["uvicorn", "ejercicio_5_1:app", "--host", "0.0.0.0", "--port", "8000"]
