#!/bin/bash

echo "🚀 Starting Math Quest - 8th Grade Math Game"
echo "=============================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Check if database exists, if not seed it
if [ ! -f "math_game.db" ]; then
    echo "🌱 Seeding database with initial data..."
    python seed_data.py
fi

# Start the application
echo "🌟 Starting the application..."
echo "🌐 Open your browser to: http://localhost:5001"
echo "⏹️  Press Ctrl+C to stop the server"
echo ""

python run.py
