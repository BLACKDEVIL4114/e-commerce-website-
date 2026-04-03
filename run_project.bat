@echo off
setlocal

set "ROOT=%~dp0"
cd /d "%ROOT%"

echo Creating virtual environment...
if not exist ".venv\Scripts\python.exe" (
  py -3 -m venv .venv
)

set "PYTHON=.venv\Scripts\python.exe"
if not exist "%PYTHON%" (
  echo ERROR: Could not create virtual environment.
  exit /b 1
)

echo Installing dependencies...
"%PYTHON%" -m pip install --upgrade pip
"%PYTHON%" -m pip install -r "ecommerce-master\requirement.txt"
if errorlevel 1 exit /b 1

echo.
echo Running Django migrations...
cd /d "%ROOT%ecommerce-master"
"%PYTHON%" manage.py migrate --noinput
if errorlevel 1 exit /b 1

echo.
echo Starting Django development server...
echo Server running at http://127.0.0.1:8000
"%PYTHON%" run_server.py
