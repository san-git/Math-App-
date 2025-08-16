@echo off
echo 🚀 Starting Math Quest - 8th Grade Math Game
echo ==============================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📚 Installing dependencies...
pip install -r requirements.txt

REM Check if database exists, if not seed it
if not exist "math_game.db" (
    echo 🌱 Seeding database with initial data...
    python seed_data.py
)

REM Start the application
echo 🌟 Starting the application...
echo 🌐 Open your browser to: http://localhost:5001
echo ⏹️  Press Ctrl+C to stop the server
echo.

python run.py

pause
