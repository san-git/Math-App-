from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    """Application factory pattern for creating Flask app"""
    app = Flask(__name__)
    
    # Configuration
    from config import get_config
    app.config.from_object(get_config())
    
    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    csrf.init_app(app)

    # Jinja filters
    @app.template_filter('from_json')
    def from_json_filter(value):
        try:
            if value is None or value == '':
                return []
            return json.loads(value)
        except Exception:
            return []
    
    # Register blueprints
    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.concepts import concepts_bp
    from routes.practice import practice_bp
    from routes.progress import progress_bp
    from routes.guest import guest_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(concepts_bp, url_prefix='/concepts')
    app.register_blueprint(practice_bp, url_prefix='/practice')
    app.register_blueprint(progress_bp, url_prefix='/progress')
    app.register_blueprint(guest_bp, url_prefix='/guest')
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
