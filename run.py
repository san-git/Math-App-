#!/usr/bin/env python3
"""
Simple run script for Math Quest
"""

from app import create_app

if __name__ == '__main__':
    app = create_app()
    print("🚀 Starting Math Quest...")
    print("📚 8th Grade Math Learning Platform")
    print("🌐 Open your browser to: http://localhost:5001")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5001)
    except KeyboardInterrupt:
        print("\n👋 Shutting down Math Quest...")
        print("Thanks for learning with us! 🎓")
