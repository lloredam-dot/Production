# 🚀 Instrucciones para Subir a GitHub

## ✅ YA ESTÁ LISTO

Ya preparé todo el repositorio Git con:
- ✅ .gitignore configurado (ignora .venv, __pycache__, etc.)
- ✅ Commit inicial hecho
- ✅ Solo archivos necesarios incluidos

---

## 📝 Pasos para Crear el Repo en GitHub y Subir

### 1️⃣ Crear Repositorio en GitHub

1. Ve a https://github.com
2. Click en el botón **"+"** (arriba derecha) → **"New repository"**
3. Llena los datos:
   ```
   Repository name: nlp-produccion
   Description: Sistema completo de NLP en Producción con Docker
   Public ✅ (para que tus alumnos puedan clonarlo)
   ❌ NO marques "Add a README" (ya tenemos uno)
   ❌ NO agregues .gitignore (ya tenemos uno)
   ❌ NO agregues licencia (por ahora)
   ```
4. Click en **"Create repository"**

---

### 2️⃣ Conectar tu Repo Local con GitHub

**GitHub te mostrará instrucciones. Usa estas (reemplaza TU-USUARIO con tu usuario real):**

```bash
git remote add origin https://github.com/TU-USUARIO/nlp-produccion.git
git branch -M master
git push -u origin master
```

**Ejemplo con tu usuario real:**
```bash
# Reemplaza "tu-usuario" con tu usuario de GitHub
git remote add origin https://github.com/tu-usuario/nlp-produccion.git
git branch -M master
git push -u origin master
```

**Te pedirá autenticación:**
- Puede pedir usuario y contraseña
- O usar Personal Access Token (si tienes 2FA activado)

---

### 3️⃣ Verificar que Subió Correctamente

1. Recarga la página de tu repositorio en GitHub
2. Deberías ver:
   ```
   ✅ README.md (se muestra en la página principal)
   ✅ Carpetas con los ejercicios
   ✅ Dockerfile y docker-compose.yml
   ✅ Documentación completa
   ```

---

### 4️⃣ Compartir con tus Alumnos

**Opción A: Link directo al repo**
```
https://github.com/TU-USUARIO/nlp-produccion
```

**Opción B: Comando para clonar**
```bash
git clone https://github.com/TU-USUARIO/nlp-produccion.git
cd nlp-produccion
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

---

## 📊 ¿Qué Archivos se Subieron?

✅ **Código (16 archivos Python):**
- ejercicio_1_1.py → ejercicio_1_3.py (Módulo 1)
- ejercicio_2_1.py → ejercicio_2_3.py (Módulo 2)
- ejercicio_3_1.py → ejercicio_3_3.py (Módulo 3)
- ejercicio_4_1.py → ejercicio_4_3.py (Módulo 4)
- ejercicio_5_1.py → ejercicio_5_3.py (Módulo 5)
- proyecto_final.py

✅ **Documentación (6 archivos):**
- README.md (visión general)
- DIAPOSITIVAS.md (presentación)
- GUIA_DESPLIEGUE_PASO_A_PASO.md (tutorial completo)
- GUIA_CONEXION_EJERCICIOS_Y_DESPLIEGUE.md
- CONTEXTO_DEL_PROYECTO.md
- TODOS_LOS_EJERCICIOS.txt (código de referencia)

✅ **Configuración (4 archivos):**
- requirements.txt (dependencias)
- Dockerfile (contenedor)
- docker-compose.yml (orquestación)
- .dockerignore (optimización)

✅ **Git:**
- .gitignore (ignora archivos innecesarios)

---

## ❌ ¿Qué NO se Subió?

❌ `.venv/` (entorno virtual - 500MB+)
❌ `__pycache__/` (archivos temporales)
❌ `.idea/`, `.vscode/` (configuración del IDE)
❌ `.claude/settings.local.json` (configuración local)
❌ Modelos pre-entrenados (muy pesados)
❌ Scripts de preparación (preparar_para_alumnos.*)

**Los alumnos crearán su propio .venv después de clonar**

---

## 🔄 ¿Cómo Actualizar el Repo Después?

Si haces cambios en el proyecto:

```bash
# 1. Ver qué cambió
git status

# 2. Agregar cambios
git add .

# 3. Hacer commit
git commit -m "Descripción de los cambios"

# 4. Subir a GitHub
git push
```

**Tus alumnos actualizan con:**
```bash
git pull
```

---

## 🎯 Ejemplo de README que se Verá en GitHub

Tu README.md ya está perfecto. GitHub lo mostrará automáticamente en la página principal con:
- Título grande
- Descripción del proyecto
- Tabla de módulos
- Instrucciones de instalación
- Enlaces a las guías

---

## 💡 Tips para tus Alumnos

**Diles que:**

1. **Clonar el repo:**
   ```bash
   git clone https://github.com/TU-USUARIO/nlp-produccion.git
   ```

2. **Seguir el README:**
   - Crear entorno virtual
   - Instalar dependencias
   - Leer DIAPOSITIVAS.md primero
   - Seguir GUIA_DESPLIEGUE_PASO_A_PASO.md

3. **Ejecutar ejercicios en orden:**
   ```bash
   python ejercicio_1_1.py
   python ejercicio_1_2.py
   # ... etc
   ```

4. **Si se pierden:**
   - Consultar TODOS_LOS_EJERCICIOS.txt
   - Leer las guías

---

## 🔒 Repositorio Privado vs Público

**Si quieres hacerlo privado:**
1. Ve a Settings del repo
2. Scroll down a "Danger Zone"
3. "Change repository visibility" → Private
4. Invita a tus alumnos: Settings → Collaborators → Add people

**Recomendación:** Déjalo público para que sea más fácil de compartir.

---

## 📱 Compartir el Link

**Opción 1: Link directo**
```
https://github.com/tu-usuario/nlp-produccion
```

**Opción 2: QR Code**
GitHub tiene un botón para generar QR del repo (útil para presentaciones)

**Opción 3: README Badge**
Puedes agregar badges bonitos al README:
```markdown
![Python](https://img.shields.io/badge/python-3.12-blue)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-green)
```

---

## ✅ Checklist Final

Antes de compartir con tus alumnos, verifica:

- [ ] Repo creado en GitHub
- [ ] Todo subido correctamente (ve los archivos en GitHub)
- [ ] README.md se ve bien en la página principal
- [ ] Los links en el README funcionan
- [ ] Pusiste instrucciones claras de instalación
- [ ] Probaste clonar el repo en otra carpeta (para verificar)

---

## 🆘 Problemas Comunes

### "Permission denied (publickey)"
**Solución:** Usa HTTPS en lugar de SSH:
```bash
git remote set-url origin https://github.com/TU-USUARIO/nlp-produccion.git
```

### "Updates were rejected"
**Solución:** Haz pull primero:
```bash
git pull origin master --rebase
git push
```

### "Large files detected"
**Solución:** El .gitignore ya los ignora. Si hay archivos grandes:
```bash
git rm --cached archivo_grande
echo "archivo_grande" >> .gitignore
git commit -m "Ignorar archivos grandes"
```

---

## 🎉 ¡Listo!

Ahora solo:
1. Ejecuta los comandos del paso 2️⃣
2. Comparte el link con tus alumnos
3. Disfruta viendo cómo aprenden

**Link que compartirás:**
```
https://github.com/TU-USUARIO/nlp-produccion
```

---

**¿Dudas? Revisa la documentación de GitHub: https://docs.github.com**
