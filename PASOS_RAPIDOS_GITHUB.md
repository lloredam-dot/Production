# 🚀 GUÍA ULTRA-RÁPIDA: Subir a GitHub en 5 Minutos

## ⚡ Opción 1: Script Automático (MÁS FÁCIL)

### Windows:
```cmd
subir_a_github.bat
```

### Linux/Mac:
```bash
chmod +x subir_a_github.sh
./subir_a_github.sh
```

**El script hará TODO por ti, solo necesitas:**
1. Tu usuario de GitHub
2. Crear el repo en el navegador (te dice cómo)
3. Tus credenciales cuando te las pida

---

## 📝 Opción 2: Manual (3 Pasos)

### PASO 1: Crear Repositorio en GitHub

1. **Abre:** https://github.com/new

2. **Llena el formulario:**
   ```
   Repository name: nlp-produccion
   Description: Sistema completo de NLP en Producción con Docker
   ✅ Public
   ❌ NO marques "Add a README"
   ❌ NO marques "Add .gitignore"
   ❌ NO marques "Choose a license"
   ```

3. **Click:** "Create repository"

---

### PASO 2: Conectar y Subir

**Copia y pega esto (reemplaza `TU-USUARIO` con tu usuario real de GitHub):**

```bash
git remote remove origin
git remote add origin https://github.com/TU-USUARIO/nlp-produccion.git
git push -u origin master
```

**Ejemplo real:**
```bash
# Si tu usuario es "juan123"
git remote remove origin
git remote add origin https://github.com/juan123/nlp-produccion.git
git push -u origin master
```

**Te pedirá:**
- Usuario de GitHub
- Contraseña (o Personal Access Token si tienes 2FA)

---

### PASO 3: Verificar y Compartir

1. **Recarga:** https://github.com/TU-USUARIO/nlp-produccion
2. **Verifica que aparecen:**
   - ✅ README.md
   - ✅ Ejercicios (ejercicio_*.py)
   - ✅ Documentación
   - ✅ Dockerfile

3. **Comparte el link con tus alumnos:**
   ```
   https://github.com/TU-USUARIO/nlp-produccion
   ```

---

## 🔐 Si GitHub te Pide Token (2FA Activado)

### Crear Personal Access Token:

1. **Ve a:** https://github.com/settings/tokens
2. **Click:** "Generate new token (classic)"
3. **Configura:**
   - Note: `Token para subir repos`
   - Expiration: `90 days`
   - ✅ Marca solo: `repo` (todos los sub-items)
4. **Click:** "Generate token"
5. **COPIA EL TOKEN** (solo lo verás una vez)

### Usar el Token:

Cuando hagas `git push`, en lugar de tu contraseña, pega el token.

**Guardar credenciales (para no escribirlas cada vez):**
```bash
git config --global credential.helper store
```

---

## ✅ Checklist

- [ ] Repositorio creado en GitHub
- [ ] Git remote configurado
- [ ] Push exitoso (sin errores)
- [ ] Verificado en el navegador
- [ ] Link compartido con alumnos

---

## 🆘 Problemas Comunes

### "fatal: remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/TU-USUARIO/nlp-produccion.git
```

### "Permission denied"
- Verifica usuario y contraseña
- Si tienes 2FA, usa Personal Access Token

### "Updates were rejected"
```bash
git pull origin master --rebase
git push
```

---

## 📱 Compartir con Alumnos

**Envíales este mensaje:**

```
¡Hola! Les comparto el proyecto de NLP en Producción:

🔗 Repositorio:
https://github.com/TU-USUARIO/nlp-produccion

📥 Para clonarlo:
git clone https://github.com/TU-USUARIO/nlp-produccion.git
cd nlp-produccion

🐍 Instalar:
python -m venv .venv
.venv\Scripts\activate  (Windows)
source .venv/bin/activate  (Linux/Mac)
pip install -r requirements.txt

📖 Leer:
- README.md: Introducción
- DIAPOSITIVAS.md: Presentación del proyecto
- GUIA_DESPLIEGUE_PASO_A_PASO.md: Tutorial completo

¡Éxito!
```

---

## 🎯 ¿Qué se Subió?

✅ **16 archivos Python** (ejercicios 1_1 → 5_3 + proyecto_final)
✅ **6 documentos** (README, guías, diapositivas)
✅ **3 archivos Docker** (Dockerfile, docker-compose.yml, .dockerignore)
✅ **1 requirements.txt**
✅ **1 .gitignore** (ignora archivos pesados)

❌ **NO se subió:**
- .venv/ (500+ MB)
- __pycache__/
- Configuraciones del IDE
- Modelos pre-entrenados

**Total:** ~5,000 líneas de código en ~100 KB

---

## 🎓 Para tus Alumnos

Diles que después de clonar:

1. **Lean README.md primero**
2. **Vean DIAPOSITIVAS.md** para contexto
3. **Sigan GUIA_DESPLIEGUE_PASO_A_PASO.md**
4. **Ejecuten ejercicios en orden** (1_1 → 5_3)

---

## 🔄 Actualizar el Repo Después

Si haces cambios:

```bash
git add .
git commit -m "Descripción del cambio"
git push
```

Tus alumnos actualizan con:
```bash
git pull
```

---

**¿Dudas? Lee INSTRUCCIONES_GITHUB.md para más detalles.**
