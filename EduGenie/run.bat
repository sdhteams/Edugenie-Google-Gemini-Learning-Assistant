@echo off
title EduGenie - AI Learning Assistant
color 0B

echo ===================================================
echo        Starting EduGenie Learning Assistant        
echo ===================================================
echo.

cd /d "%~dp0"

:: 1. Check for Python installation
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed or not added to PATH.
    echo Please install Python 3.10+ from https://www.python.org/
    pause
    exit /b 1
)

:: 2. Check / Create Virtual Environment
if not exist "venv\Scripts\activate.bat" (
    echo [INFO] Virtual environment not found. Creating 'venv'...
    python -m venv venv
    if %ERRORLEVEL% NEQ 0 (
        echo [ERROR] Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo [OK] Virtual environment created.
)

:: 3. Activate Virtual Environment
echo [INFO] Activating virtual environment...
call venv\Scripts\activate.bat

:: 4. Verify / Install Dependencies
echo [INFO] Checking and installing dependencies from requirements.txt...
python -m pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Package installation failed. Please verify requirements.txt.
    pause
    exit /b 1
)

:: 5. Check for .env file
if not exist ".env" (
    echo [WARNING] No .env file found in root directory!
    echo Creating sample .env file. Please add your GEMINI_API_KEY.
    (
        echo GEMINI_API_KEY=your_actual_gemini_api_key_here
        echo GEMINI_MODEL=gemini-2.5-flash
    ) > .env
    echo [ACTION REQUIRED] Open .env, add your API key, then re-run this script.
    pause
    exit /b 1
)

:: 6. Launch FastAPI Server
echo.
echo ===================================================
echo EduGenie is running at: http://127.0.0.1:8000
echo Swagger API docs at:   http://127.0.0.1:8000/docs
echo Press CTRL+C in this terminal to stop the server.
echo ===================================================
echo.

python -m uvicorn app.main:app --reload

pause