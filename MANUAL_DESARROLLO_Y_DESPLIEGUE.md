# Guía Avanzada de Despliegue para Científicos de Datos: De Python a Docker

## Prólogo: El Salto del Laboratorio a Producción

Este documento no es un simple resumen; es la crónica de un viaje. Un viaje que todo profesional de datos debe emprender: el que va desde el entorno controlado y familiar de un script de análisis o un Jupyter Notebook, hacia el mundo dinámico y exigente de las aplicaciones de software en producción.

Como científico de datos, tu dominio reside en la extracción de valor a partir de los datos: la estadística, el modelado predictivo, la comprensión del negocio. Este manual se ha diseñado para servir como un puente robusto hacia las disciplinas de la Ingeniería de Software y DevOps, habilidades que transforman un modelo brillante en un producto útil y escalable.

Nuestra sesión interactiva fue una simulación acelerada de este viaje. Encontramos obstáculos, nos enfrentamos a errores crípticos, cuestionamos comportamientos inesperados y, en cada paso, descubrimos los principios fundamentales que rigen el software moderno. Este manual cristaliza ese proceso, con la intención de ser un recurso teórico y práctico al que puedas volver una y otra vez.

---

## Índice

**Parte I: Fundamentos y Configuración del Entorno de Desarrollo**
1.  [El Punto de Partida: Scripts y Dependencias](#capítulo-1-el-punto-de-partida-scripts-y-dependencias)
2.  [Diagnóstico de Errores Comunes de Python](#capítulo-2-diagnóstico-de-errores-comunes-de-python)
    *   2.1. El `NameError`: Una Lección sobre Namespaces e Importaciones
    *   2.2. El Aviso de `transformers`: Comprendiendo los Motores de Backend
3.  [Gestión Profesional de Dependencias: `requirements.txt`](#capítulo-3-gestión-profesional-de-dependencias-requirements.txt)

**Parte II: Creación de un Servicio Web con FastAPI**
4.  [El Cambio de Paradigma: De Script a Servidor](#capítulo-4-el-cambio-de-paradigma-de-script-a-servidor)
    *   4.1. Teoría: El Modelo Cliente-Servidor, Puertos y APIs
    *   4.2. Descubrimiento: "El Servidor Arranca Pero No Hace Nada"
5.  [Depurando la Capa Web: El Middleware](#capítulo-5-depurando-la-capa-web-el-middleware)
    *   5.1. Teoría: ¿Qué es un Middleware y el Ciclo Request-Response?
    *   5.2. El Error `TypeError: 'NoneType' object is not callable`: Análisis y Solución

**Parte III: Contenerización Profesional con Docker**
6.  [El Problema Fundamental: "En mi máquina funciona"](#capítulo-6-el-problema-fundamental-en-mi-máquina-funciona)
    *   6.1. Teoría: Virtualización vs. Contenerización. Imágenes vs. Contenedores
7.  [Construyendo Nuestra Primera Imagen Docker (`docker build`)](#capítulo-7-construyendo-nuestra-primera-imagen-docker-docker-build)
    *   7.1. El `Dockerfile`: Anatomía de un Plano de Construcción
    *   7.2. Diagnóstico: "¡Docker está consumiendo todos mis recursos!"
    *   7.3. Solución Profesional: Optimizando el Contexto con `.dockerignore`
8.  [Ejecución y Gestión de Contenedores (`docker run`)](#capítulo-8-ejecución-y-gestión-de-contenedores-docker-run)
    *   8.1. Teoría: Mapeo de Puertos y el Aislamiento del Contenedor
    *   8.2. Diagnóstico: "La CPU está al 70% en reposo"
    *   8.3. Solución Profesional: Separando Entornos de Desarrollo y Producción con `CMD`
9.  [Inspección y Depuración de Contenedores](#capítulo-9-inspección-y-depuración-de-contenedores)
    *   9.1. `docker stats`: La Verdad sobre el Consumo de Recursos
    *   9.2. La Interfaz de Docker Desktop: El Puente de Mando

**Parte IV: Mantenimiento y Buenas Prácticas**
10. [Gestión de Recursos del Sistema](#capítulo-10-gestión-de-recursos-del-sistema)
    *   10.1. Forzando la Limpieza de la Caché de Memoria en Windows (RamMap)
    *   10.2. Mantenimiento del Entorno Docker (`docker system prune`)

**Conclusión: Integrando la Ingeniería de Software en la Ciencia de Datos**

**Apéndices**
*   [Apéndice A: Arquitectura Visual del Sistema](#apéndice-a-arquitectura-visual-del-sistema)
*   [Apéndice B: Guía Pedagógica para Instructores](#apéndice-b-guía-pedagógica-para-instructores)

---

## Parte I: Fundamentos y Configuración del Entorno de Desarrollo

### Capítulo 1: El Punto de Partida: Scripts y Dependencias

Iniciamos con una estructura de proyecto compuesta por múltiples ficheros `.py` y `.md`. Cada fichero `.py` representaba un módulo de un sistema de análisis financiero. Esta estructura modular es una excelente práctica de ingeniería de software, ya que divide un problema complejo en partes más pequeñas y manejables.

### Capítulo 2: Diagnóstico de Errores Comunes de Python

Nuestra primera tarea fue validar los scripts. Inmediatamente, nos encontramos con errores que son ritos de iniciación para cualquier desarrollador.

#### 2.1. El `NameError`: Una Lección sobre Namespaces e Importaciones

> **El Incidente:** Al ejecutar `ejercicio_2_2.py` y `ejercicio_2_3.py`, nos topamos con `NameError: name 'dataclass' is not defined` y `NameError: name 'List' is not defined`.
>
> **Teoría Profunda:** Python opera sobre un concepto llamado **namespace** (espacio de nombres). Imagina que es una libreta donde Python anota todos los nombres de variables y funciones que conoce en un momento dado. Cuando el intérprete de Python se encuentra con un nombre (ej. `dataclass`), lo busca en su libreta. Si no lo encuentra, lanza un `NameError`.
> Por defecto, la "libreta" de Python solo contiene un conjunto de funciones y tipos básicos (como `print`, `len`, `str`, `list`). Herramientas más avanzadas, aunque formen parte de la biblioteca estándar de Python, viven en módulos separados para mantener el sistema base ligero y organizado.
> *   `dataclass` vive en el módulo `dataclasses`.
> *   `List`, `Dict`, `Optional`, `Tuple` son herramientas para el "Type Hinting" (pistas de tipo, una práctica moderna para escribir código más legible y robusto) y viven en el módulo `typing`.
>
> **La Solución Profesional:** La directiva `import` es la que le dice a Python: "Ve a este módulo, coge esta herramienta y anótala en tu libreta para que pueda usarla".
>
> ```python
> # Solución para ejercicio_2_2.py
> from dataclasses import dataclass # Anota 'dataclass' en el namespace
> from typing import Optional, List, Dict # Anota estos tres nombres
>
> # Solución para ejercicio_3_2.py
> from datetime import datetime # Anota 'datetime'
> ```
> **Consejo Top:** Un `NameError` es uno de los errores más informativos. Casi siempre significa una de dos cosas: o escribiste mal el nombre de una variable, o te olvidaste de importarla.

#### 2.2. El Aviso de `transformers`: Comprendiendo los Motores de Backend

> **El Incidente:** Al ejecutar `ejercicio_3_1.py`, no obtuvimos un error, sino un aviso: `None of PyTorch, TensorFlow >= 2.0, or Flax have been found`.
>
> **Teoría Profunda:** Este incidente revela la arquitectura en capas del software moderno. La librería `transformers` de Hugging Face es una **abstracción de alto nivel**. Su trabajo es proporcionar una interfaz sencilla y unificada para trabajar con modelos de lenguaje complejos. Sin embargo, no reinventa la rueda del cálculo numérico y la diferenciación automática necesarios para el deep learning. En su lugar, **delega** ese trabajo a un **motor de backend** o "framework" de bajo nivel.
> Es como un coche (la librería `transformers`) que puede venir con diferentes motores (PyTorch, TensorFlow, Flax). El coche te ofrece el volante y los pedales, pero necesita uno de esos motores para moverse. El aviso nos decía: "He instalado el chasis del coche, pero no encuentro ningún motor en el garaje".
>
> **La Solución Profesional:** Identificar y proveer el motor necesario. En el ecosistema de `transformers`, PyTorch (`torch`) es a menudo la opción más común y mejor soportada. La solución no era modificar el código, sino enriquecer nuestro entorno de desarrollo.

### Capítulo 3: Gestión Profesional de Dependencias: `requirements.txt`

Este capítulo conecta directamente con el anterior. ¿Cómo proveemos el "motor" y todas las demás librerías que nuestro proyecto necesita de una forma estructurada?

> **El Problema:** Podríamos ejecutar `pip install torch`, `pip install pandas`, etc., uno por uno. Pero esto es manual, propenso a errores y no es repetible. Si compartes tu proyecto, la otra persona no sabría qué instalar.
>
> **Teoría Profunda:** Un pilar de la ingeniería de software es la **reproducibilidad**. Un entorno de desarrollo debe poder ser recreado de forma idéntica en cualquier máquina. El fichero `requirements.txt` es el estándar de facto en el ecosistema Python para lograr esto.
> Es un simple fichero de texto que actúa como un manifiesto, listando cada dependencia externa del proyecto con su versión (opcional pero recomendado para una reproducibilidad estricta).
>
> **La Solución Profesional:** Creamos un fichero `requirements.txt` y lo poblamos con todas las librerías necesarias. Luego, usamos un único comando para instalar todo.
>
> ```bash
> # En la terminal, con el entorno virtual activado:
> pip install -r requirements.txt
> ```
> La bandera `-r` (de "requirement") le indica a `pip` que lea el fichero y lo use como una lista de tareas de instalación. Al hacer esto, instalamos `torch` y todas las demás dependencias, solucionando el aviso de `transformers` de forma permanente y profesional.

---

## Parte II: Creación de un Servicio Web con FastAPI

### Capítulo 4: El Cambio de Paradigma: De Script a Servidor

Aquí tuvo lugar nuestra primera gran transición conceptual.

#### 4.1. Teoría: El Modelo Cliente-Servidor, Puertos y APIs

*   **Script:** Un programa que se ejecuta, realiza una tarea y termina. Tiene un principio y un fin definidos.
*   **Servidor:** Un programa diseñado para ejecutarse **indefinidamente**, en un bucle constante donde "escucha" peticiones entrantes. No termina hasta que se le detiene explícitamente.
*   **Puerto:** Imagina que la dirección IP de tu ordenador (`localhost` o `127.0.0.1`) es la dirección de un gran edificio. Un puerto es el número de un apartamento específico dentro de ese edificio. Cuando una petición llega a tu ordenador, el número de puerto le dice al sistema operativo a qué aplicación entregarle el mensaje. El puerto 8000 que elegimos es un puerto de uso general, perfecto para desarrollo.
*   **API (Application Programming Interface):** Es un contrato, un conjunto de reglas y definiciones que especifican cómo un programa (el cliente, como tu navegador) puede comunicarse con otro (nuestro servidor FastAPI). No está diseñada para ser bonita, sino para ser funcional y predecible.
*   **JSON (JavaScript Object Notation):** Es el lenguaje franco de las APIs modernas. Un formato de texto ligero y legible para humanos que estructura los datos en pares de clave-valor, similar a un diccionario de Python.

#### 4.2. Descubrimiento: "El Servidor Arranca Pero No Hace Nada"

> **La Duda:** Ejecutamos `ejercicio_5_1.py` y la terminal mostró `Uvicorn running on http://0.0.0.0:8000`. Al visitar la página, solo vimos un texto simple. Parecía que no funcionaba.
>
> **La Revelación:** ¡Este era el comportamiento correcto! El mensaje indicaba que el servidor estaba activo y escuchando en el puerto 8000. El texto que vimos en el navegador era la respuesta **JSON** de nuestra API. El verdadero "panel de control" para un desarrollador de FastAPI está en la URL `/docs`, que genera una interfaz interactiva para explorar y probar la API.

### Capítulo 5: Depurando la Capa Web: El Middleware

#### 5.1. Teoría: ¿Qué es un Middleware y el Ciclo Request-Response?

Imagina el viaje de una petición en FastAPI como una cadena de montaje. La petición entra por un lado, pasa por varias estaciones y la respuesta sale por el otro. Un **middleware** es una de esas estaciones. Es una función que se ejecuta para **cada petición** que entra a la API, antes de que llegue al endpoint específico.

Es increíblemente útil para tareas transversales como:
*   Logging (registrar cada petición).
*   Autenticación (verificar si el usuario tiene permiso).
*   Medición de tiempos.
*   Compresión de respuestas.

La regla de oro de un middleware es que, después de hacer su trabajo, **debe pasar la petición a la siguiente estación** en la cadena. 

#### 5.2. El Error `TypeError: 'NoneType' object is not callable`: Análisis y Solución

> **El Incidente:** Al intentar acceder a `/docs`, la aplicación se rompió con un error masivo y críptico. La línea clave era `TypeError: 'NoneType' object is not callable`.
>
> **Análisis Profundo:** El error significa que Python intentó ejecutar algo como si fuera una función, pero ese "algo" era `None` (nulo). Rastreando el flujo, descubrimos que el culpable era nuestro middleware `log_requests`:
>
> ```python
> # El código erróneo
> @app.middleware("http")
> async def log_requests(request, call_next):
>     pass # No hace nada, y por tanto, devuelve None
> ```
> El servidor le pasaba la petición a nuestro middleware. Éste no hacía nada y devolvía `None`. El servidor recibía `None` en lugar de una respuesta válida y no sabía cómo proceder, causando el colapso.
>
> **La Solución Profesional:** Implementamos el patrón correcto de middleware, asegurando que la petición continúe su viaje y que una respuesta sea devuelta.
>
> ```python
> # El código correcto
> @app.middleware("http")
> async def log_requests(request: Request, call_next):
>     start_time = time.time()
>     # Pasa la petición a la siguiente estación y espera la respuesta
>     response = await call_next(request)
>     processing_time = time.time() - start_time
>     print(f"Request processed in {processing_time:.4f}s")
>     # Devuelve la respuesta al servidor
>     return response
> ```
> **Consejo Top:** Cuando trabajes con frameworks web, entiende el ciclo de vida de una petición. Un error en una capa temprana como un middleware afectará a toda la aplicación.

---

## Parte III: Contenerización Profesional con Docker

### Capítulo 6: El Problema Fundamental: "En mi máquina funciona"

Este es el problema que Docker vino a resolver. Un software no es solo código; es código + sistema operativo + dependencias + configuraciones. Docker nos permite empaquetar todo esto en una unidad coherente y portátil.

#### 6.1. Teoría: Virtualización vs. Contenerización. Imágenes vs. Contenedores

*   **Máquina Virtual (VM):** Emula un ordenador completo, incluyendo un sistema operativo huésped completo. Es pesado y lento de arrancar.
*   **Contenedor:** Es mucho más ligero. No emula un hardware, sino que comparte el kernel del sistema operativo anfitrión. Solo empaqueta la aplicación y sus dependencias. Es rápido, eficiente y portátil.
*   **Imagen Docker:** Es una **plantilla inmutable**, un plano o un molde. Contiene todas las instrucciones para crear un entorno. Se construye con `docker build`.
*   **Contenedor Docker:** Es una **instancia en ejecución** de una imagen. Es la "caja mágica" viva y funcionando. Se crea con `docker run`.

### Capítulo 7: Construyendo Nuestra Primera Imagen Docker (`docker build`)

#### 7.1. El `Dockerfile`: Anatomía de un Plano de Construcción

Es un fichero de texto con instrucciones secuenciales. Cada instrucción crea una "capa" en la imagen, que Docker puede cachear para acelerar futuras construcciones.

```dockerfile
# 1. Punto de partida
FROM python:3.12-slim

# 2. Directorio de trabajo
WORKDIR /app

# 3. Copiar y instalar dependencias (paso clave para el cacheo)
COPY requirements.txt .
RUN pip install -r requirements.txt

# 4. Copiar el resto del código
COPY . .

# 5. Exponer el puerto
EXPOSE 8000

# 6. Comando de inicio por defecto
CMD ["uvicorn", "ejercicio_5_1:app", "--host", "0.0.0.0"]
```

#### 7.2. Diagnóstico: "¡Docker está consumiendo todos mis recursos!"

> **El Incidente:** El primer `docker build` fue lento (11 minutos) y el Administrador de Tareas mostró un uso de RAM de `55 GB`.
>
> **Análisis Profundo:** Esto se debió a dos factores:
> 1.  **Contexto de Construcción (Build Context):** Antes de construir, Docker empaqueta todo el directorio del proyecto y se lo envía a su motor. Vimos que estaba enviando `1.72 GB` de datos, lo cual era excesivo.
> 2.  **Compilación de Dependencias:** El paso `RUN pip install` tuvo que compilar extensiones C/C++ de librerías científicas, un proceso muy intensivo en CPU y RAM.
> 3.  **Caché del Sistema Operativo:** Windows utilizó la RAM libre como caché de disco ("Standby List") para acelerar el proceso. Esta memoria no estaba realmente "en uso" por Docker, sino reservada inteligentemente por el SO.

#### 7.3. Solución Profesional: Optimizando el Contexto con `.dockerignore`

> **La Solución:** Creamos un fichero `.dockerignore` para excluir directorios innecesarios del contexto de construcción, como `.venv`, `.idea`, y `__pycache__`. 
>
> **El Resultado:** El contexto de construcción se redujo de `1.72 GB` a unos pocos megabytes. La construcción se volvió drásticamente más rápida y el pico de consumo de recursos, mucho menor. **Nunca construyas una imagen sin un fichero `.dockerignore` bien configurado.**

### Capítulo 8: Ejecución y Gestión de Contenedores (`docker run`)

#### 8.1. Teoría: Mapeo de Puertos y el Aislamiento del Contenedor

Un contenedor está aislado por defecto. Para comunicarnos con él, debemos "publicar" sus puertos al exterior. El flag `-p 8000:8000` crea un túnel: las peticiones que llegan al puerto 8000 de tu PC son redirigidas al puerto 8000 dentro del contenedor.

#### 8.2. Diagnóstico: "La CPU está al 70% en reposo"

> **El Incidente:** Al ejecutar el contenedor, `docker stats` mostró un uso de CPU muy alto y constante.
>
> **Análisis Profundo:** El culpable fue el **auto-reloader** de Uvicorn, que habíamos iniciado con `python ejercicio_5_1.py`. Este modo de desarrollo vigila constantemente los cambios en los ficheros, una actividad que consume mucha CPU.

#### 8.3. Solución Profesional: Separando Entornos de Desarrollo y Producción con `CMD`

> **La Solución:** Aprovechamos la instrucción `CMD` en el `Dockerfile` para definir un comando de inicio de **producción** por defecto, que no incluye el reloader.
>
> Esto nos dio un sistema dual:
> ```bash
> # Modo Producción: Eficiente y ligero. Usa el CMD del Dockerfile.
> docker run -p 8000:8000 financial-ml-api
>
> # Modo Desarrollo: Cómodo para programar. Sobrescribe el CMD.
> docker run -p 8000:8000 financial-ml-api python ejercicio_5_1.py
> ```
> **Consejo Top:** Tu imagen de Docker debe estar siempre lista para producción. El modo de desarrollo debe ser una modificación que aplicas al ejecutar, no el comportamiento por defecto.

### Capítulo 9: Inspección y Depuración de Contenedores

#### 9.1. `docker stats`: La Verdad sobre el Consumo de Recursos

Este comando fue nuestra herramienta de diagnóstico clave. Nos demostró que el consumo de memoria real del contenedor era mínimo (`~125MB`), desmitificando los alarmantes números del Administrador de Tareas.

#### 9.2. La Interfaz de Docker Desktop: El Puente de Mando

Descubrimos que Docker Desktop no es solo un panel vacío, sino una potente interfaz para contenedores **en ejecución**. Las pestañas `Logs`, `Inspect` y, sobre todo, `Exec` (o `Terminal`), nos permitieron "entrar" en nuestro contenedor, explorar su sistema de archivos (`ls -l`) y verificar su estado interno, conectando la teoría con la práctica.

---

## Parte IV: Mantenimiento y Buenas Prácticas

### Capítulo 10: Gestión de Recursos del Sistema

#### 10.1. Forzando la Limpieza de la Caché de Memoria en Windows (RamMap)

Para liberar la memoria que Windows mantiene en la "Standby List" tras una operación pesada, utilizamos la herramienta oficial **RamMap** de Microsoft Sysinternals. La acción `Empty -> Empty Standby List` nos permite devolver el sistema a un estado de memoria base.

#### 10.2. Mantenimiento del Entorno Docker (`docker system prune`)

Docker puede acumular muchos artefactos (imágenes intermedias, cachés de construcción, redes sin usar) que ocupan espacio en disco. El comando `docker system prune -a` es la herramienta de limpieza esencial para cualquier desarrollador que trabaje con Docker regularmente.

---

## Conclusión: Integrando la Ingeniería de Software en la Ciencia de Datos

Este viaje nos ha enseñado que un producto de datos es mucho más que un modelo. Es un sistema de software. Hemos aprendido a:

*   **Gestionar dependencias** de forma profesional.
*   **Servir un modelo** a través de una API robusta.
*   **Depurar errores** no solo en el código, sino en la interacción entre componentes del sistema.
*   **Empaquetar una aplicación** de forma aislada y reproducible con Docker.
*   **Optimizar el proceso de construcción** para ser más rápido y ligero.
*   **Gestionar la ejecución** para diferentes entornos (desarrollo vs. producción).
*   **Monitorear y diagnosticar** el comportamiento de nuestra aplicación en tiempo real.

Estas no son habilidades secundarias; son el conjunto de herramientas que te permite llevar tus análisis y modelos al siguiente nivel, creando soluciones escalables, mantenibles y de alto impacto. Has sentado las bases para convertirte en un profesional de datos verdaderamente integral.

---

## Apéndice A: Arquitectura Visual del Sistema

Para comprender cómo interactúan todos los componentes, podemos visualizar la arquitectura en dos niveles: el sistema completo en producción y la orquestación de servicios con Docker Compose.

### Diagrama de Arquitectura de Alto Nivel (Estilo C4 - System Context)

Este diagrama muestra el sistema como una caja negra e ilustra cómo interactúa con los usuarios y otros sistemas.

```
+---------------------------------------------------------------------------------+
|                                                                                 |
|   +------------------+         +-------------------------------------------+   |
|   |                  |         |                                           |   |
|   |  Usuario Final   | ------->|  Sistema de Análisis Financiero (Docker)  |   |
|   | (Científico de   |         |                                           |   |
|   |  Datos, App...)  | <-------+                                           |   |
|   +------------------+         |                                           |   |
|                                +-------------------------------------------+   |
|                                                  |           ^                |
|                                                  |           |                |
|                                                  v           |                |
|   +--------------------------+   +---------------------------+   +------------------------+
|   |                          |   |                           |   |                        |
|   | API de Datos de Mercado  |   |   Sitios de Noticias      |   |   API de Modelos IA    |
|   |   (ej. Alpha Vantage)    |   |   (ej. Yahoo Finance)     |   |     (ej. Gemini)       |
|   |                          |   |                           |   |                        |
|   +--------------------------+   +---------------------------+   +------------------------+
|                                                                                 |
+---------------------------------------------------------------------------------+
```

**Descripción:**
*   El **Usuario Final** interactúa con nuestro sistema a través de peticiones HTTP (por ejemplo, desde un navegador, un script de Python o una aplicación).
*   Nuestro **Sistema de Análisis Financiero** vive dentro de un entorno Docker. Este sistema es el único que se comunica con el exterior.
*   Para funcionar, el sistema consume datos de tres fuentes externas:
    1.  **APIs de Mercado:** Para obtener datos de precios de acciones.
    2.  **Sitios de Noticias:** Para realizar web scraping y obtener texto para el análisis de sentimientos.
    3.  **APIs de Modelos IA:** Para tareas como la revisión de código o la generación de texto.

### Diagrama de Contenedores con Docker Compose (Estilo C4 - Containers)

Este diagrama hace "zoom" dentro de nuestro sistema y muestra los diferentes contenedores que lo componen, tal como se define en `docker-compose.yml`.

```
+------------------------------------------------------------------+
|                                                                  |
|                  Entorno Docker (Tu Máquina o Servidor)          |
|                                                                  |
| +----------------+      Petición HTTP (Puerto 8000)      +-------+
| |                | <------------------------------------ |       |
| | Usuario Final  |                                       |  API  |
| |                | ------------------------------------->| (FastAPI) |
| +----------------+      Respuesta JSON (Puerto 8000)     |       |
|                                                          +--+----+
|                                                             |
|                                                             | (Red interna de Docker)
|                                                             |
|      +-----------------------+----------------+-------------+
|      |                       |                |
|      v                       v                v
| +----+----+             +----+----+      +----+----+
| |         |             |         |      |         |
| |   DB    |             |  Redis  |      |  Otros  |
| |(PostgreSQL)|           | (Caché) |      | (Monitor) |
| |         |             |         |      |         |
| +---------+             +---------+      +---------+
|                                                                  |
+------------------------------------------------------------------+
```

**Descripción:**
*   El **Usuario Final** solo habla con el contenedor de la **API (FastAPI)** a través del puerto 8000 que hemos expuesto.
*   Dentro del entorno Docker, todos los contenedores están conectados a través de una **red virtual privada**. Esto significa que la API puede hablar con la base de datos usando un nombre de host (ej. `db`) en lugar de una IP.
*   El contenedor de la **API** es el cerebro. Contiene nuestro código Python y los modelos de ML. Cuando necesita guardar datos persistentes, se comunica con el contenedor de la **Base de Datos (DB)**.
*   Si necesita una operación de caché rápida, se comunica con el contenedor de **Redis**.
*   Otros servicios, como un sistema de **Monitoreo (Prometheus)**, también vivirían como contenedores separados, recogiendo métricas de la API.

Este diseño se conoce como **arquitectura de microservicios**: cada componente principal del sistema es un servicio independiente y autocontenido, lo que facilita su desarrollo, escalado y mantenimiento.

---

## Apéndice B: Guía Pedagógica para Instructores

Esta sección está diseñada para un instructor que desee utilizar este proyecto como material didáctico para alumnos con perfil de informática, ingeniería de software o similar.

### Objetivo General del Curso

Capacitar al alumno para que pueda tomar un conjunto de scripts de análisis de datos y desplegarlos como un servicio web robusto, escalable y mantenible, utilizando para ello herramientas y prácticas modernas de desarrollo de software y DevOps.

### Desglose por Ejercicio

#### **Módulo 1: Fundamentos Modernos**

*   **Ejercicio 1.1: Configuración del Entorno con IA**
    *   **Objetivo de Aprendizaje:** Comprender el concepto de "Infraestructura como Código" aplicado al propio entorno de desarrollo. Introducir la idea de usar APIs (en este caso, de IA) para automatizar tareas de programación.
    *   **Instrucción Clave:** "Implementa la clase `AICodeReviewer`. Deberás inicializar el cliente de la API de Gemini en el constructor y usarlo en el método `review_code` para enviar el código de muestra y procesar la respuesta."
    *   **Puntos de Discusión:** ¿Cuáles son las ventajas de automatizar la revisión de código? ¿Qué limitaciones podría tener una IA para esta tarea? Discutir la importancia de las claves de API y cómo gestionarlas de forma segura (variables de entorno).

*   **Ejercicio 1.2: Python 3.12+ Features**
    *   **Objetivo de Aprendizaje:** Familiarizarse con características modernas de Python que mejoran la claridad y seguridad del código (`TypedDict`, `NotRequired`) y la eficiencia (`asyncio`, `TaskGroup`).
    *   **Instrucción Clave:** "Completa la `TypedDict` `StockData` usando `NotRequired`. Implementa el `pattern matching` en `analyze_stock_data` para manejar los diferentes casos. Finalmente, refactoriza el bucle de `fetch_multiple_stocks` para usar `asyncio.TaskGroup` y ejecutar las llamadas en paralelo."
    *   **Puntos de Discusión:** Comparar `TypedDict` con una clase normal o un diccionario simple. ¿Cuándo es útil cada uno? Explicar la diferencia entre concurrencia (`asyncio`) y paralelismo (multiprocessing). ¿Por qué `asyncio` es ideal para operaciones de red (I/O-bound)?

*   **Ejercicio 1.3: Integración con IA para Debugging**
    *   **Objetivo de Aprendizaje:** Aplicar el análisis de texto y la generación de código para crear herramientas de desarrollo avanzadas. Introducir el módulo `ast` para el análisis estático de código.
    *   **Instrucción Clave:** "En `analyze_error`, usa el módulo `traceback` para extraer información del error. Envía esta información junto con el código a una IA para que sugiera una causa. En `generate_tests`, pide a la IA que cree tests unitarios para una función dada, basándose en su firma y contenido."
    *   **Puntos de Discusión:** Análisis estático vs. dinámico. ¿Qué tipo de errores puede detectar `ast` sin ejecutar el código? ¿Cómo se podría construir un prompt efectivo para que la IA genere tests útiles?

#### **Módulo 2: APIs y Web Scraping**

*   **Ejercicio 2.1: Cliente API Moderno**
    *   **Objetivo de Aprendizaje:** Diseñar un cliente de API robusto, implementando patrones de resiliencia como reintentos, caché y manejo de límites de tasa.
    *   **Instrucción Clave:** "Implementa la lógica de caché en `get_stock_price`, comprobando primero si la respuesta está en `self.cache` y si no ha expirado. Implementa `_check_rate_limit` para que introduzca una pausa si se hacen demasiadas llamadas seguidas. Usa `asyncio.gather` o `TaskGroup` en `get_multiple_stocks`."
    *   **Puntos de Discusión:** ¿Por qué es crucial el `rate limiting` al interactuar con APIs de terceros? Discutir diferentes estrategias de caché (en memoria, en disco, Redis).

*   **Ejercicio 2.2: Web Scraping de Noticias Financieras**
    *   **Objetivo de Aprendizaje:** Diferenciar entre scraping de contenido estático (con `requests` y `BeautifulSoup`) y dinámico (con `Selenium`). Entender los desafíos del web scraping (bloqueos, cambios de layout).
    *   **Instrucción Clave:** "Usa `Selenium` para cargar la página de noticias de Yahoo Finance, esperando explícitamente a que los elementos de las noticias aparezcan. Extrae los datos usando selectores CSS o XPath. Compara este enfoque con el uso de `requests` en una página más simple como MarketWatch."
    *   **Puntos de Discusión:** Ética del web scraping y cómo respetar los ficheros `robots.txt`. Estrategias para evitar ser bloqueado (User-Agents, proxies, delays).

*   **Ejercicio 2.3: Autenticación OAuth 2.0**
    *   **Objetivo de Aprendizaje:** Comprender el flujo de autenticación OAuth 2.0, uno de los estándares más importantes para la autorización delegada en la web.
    *   **Instrucción Clave:** "Implementa `generate_auth_url` para construir la URL de autorización con los parámetros correctos, incluyendo el `code_challenge` para PKCE. Luego, implementa `exchange_code_for_token` para realizar la petición POST al `token_url` y manejar la respuesta que contiene los tokens."
    *   **Puntos de Discusión:** Diferencia entre autenticación y autorización. ¿Por qué OAuth 2.0 es más seguro que simplemente pasar un usuario y contraseña? Explicar el rol de cada actor: cliente, servidor de recursos, servidor de autorización, usuario.

#### **Módulo 3-4: NLP y Machine Learning**

*   **Ejercicios 3.1 a 4.3:**
    *   **Objetivo de Aprendizaje:** Estos módulos son el núcleo de la ciencia de datos. El enfoque aquí es la **integración** de estos modelos en la estructura de software que estamos construyendo.
    *   **Instrucción Clave:** "El objetivo no es solo construir el modelo, sino hacerlo de una manera modular. Encapsula la lógica de preprocesamiento, entrenamiento y predicción en clases bien definidas (`AdvancedFinancialSentimentAnalyzer`, `StockPredictor`). Asegúrate de que los métodos de estas clases puedan ser llamados fácilmente desde nuestra API."
    *   **Puntos de Discusión:** La importancia de versionar modelos y datos. ¿Cómo se integra un modelo entrenado en un entorno de producción? (Serialización de modelos con `joblib` o `torch.save`). Discutir el desafío de mantener la consistencia entre las features de entrenamiento y las de inferencia.

#### **Módulo 5: Integración y Despliegue**

*   **Ejercicio 5.1: API con FastAPI**
    *   **Objetivo de Aprendizaje:** Exponer la lógica de negocio y los modelos de ML a través de una API RESTful.
    *   **Instrucción Clave:** "Importa las clases de los módulos anteriores. En los endpoints de la API (ej. `/analyze/sentiment`), crea una instancia de tu analizador y úsala para procesar los datos de la petición. Devuelve el resultado en el formato definido por el modelo Pydantic de respuesta."
    *   **Puntos de Discusión:** Diseño de APIs RESTful (uso de verbos HTTP, estructura de URLs). Ventajas de la validación de datos con Pydantic.

*   **Ejercicio 5.2: Containerización con Docker**
    *   **Objetivo de Aprendizaje:** Lograr la reproducibilidad total del entorno de la aplicación y entender los fundamentos de la contenerización.
    *   **Instrucción Clave:** "Primero, crea un fichero `.dockerignore` para excluir la carpeta `.venv`. Luego, completa el `Dockerfile`: copia `requirements.txt`, ejecuta `pip install`, copia el resto del código y define un `CMD` de producción. Finalmente, ejecuta `docker build` y `docker run`."
    *   **Puntos de Discusión:** El orden de las instrucciones en un `Dockerfile` es crucial para el cacheo. ¿Por qué copiamos `requirements.txt` antes que el resto del código? Discutir la diferencia entre `CMD` y `ENTRYPOINT`.

*   **Ejercicio 5.3: Monitoreo y Logging**
    *   **Objetivo de Aprendizaje:** Entender la importancia de la observabilidad en un sistema en producción.
    *   **Instrucción Clave:** "Importa las clases de `ejercicio_5_3` en `ejercicio_5_1`. En el middleware de FastAPI, después de procesar una petición, llama a los métodos del `MetricsCollector` para registrar la duración y el resultado. Expón las métricas en un nuevo endpoint `/metrics`."
    *   **Puntos de Discusión:** Los tres pilares de la observabilidad: Logs, Métricas y Trazas. ¿Qué métricas son clave para un servicio de ML? (Latencia de predicción, accuracy del modelo en producción, etc.).
