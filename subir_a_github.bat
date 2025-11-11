@echo off
echo ========================================
echo   SUBIR PROYECTO A GITHUB
echo ========================================
echo.

REM Solicitar usuario de GitHub
set /p GITHUB_USER="Ingresa tu usuario de GitHub: "

echo.
echo ========================================
echo   PASOS A SEGUIR:
echo ========================================
echo.
echo 1. Abre tu navegador en: https://github.com/new
echo.
echo 2. Configura el repositorio asi:
echo    Repository name: nlp-produccion
echo    Description: Sistema completo de NLP en Produccion con Docker
echo    [X] Public
echo    [ ] NO marques "Add a README"
echo    [ ] NO marques "Add .gitignore"
echo.
echo 3. Click en "Create repository"
echo.
echo 4. Vuelve aqui y presiona ENTER
pause

echo.
echo ========================================
echo   CONECTANDO Y SUBIENDO...
echo ========================================
echo.

REM Agregar remote
git remote remove origin 2>nul
git remote add origin https://github.com/%GITHUB_USER%/nlp-produccion.git

echo.
echo Intentando hacer push...
echo (Te pedira tus credenciales de GitHub)
echo.

REM Hacer push
git push -u origin master

echo.
echo ========================================
echo   VERIFICANDO...
echo ========================================
echo.

git remote -v

echo.
echo ========================================
echo   LISTO!
echo ========================================
echo.
echo Tu proyecto esta en:
echo https://github.com/%GITHUB_USER%/nlp-produccion
echo.
echo Comparte ese link con tus alumnos!
echo.
echo Ellos lo clonaran con:
echo git clone https://github.com/%GITHUB_USER%/nlp-produccion.git
echo.
pause
