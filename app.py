from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect, generate_csrf
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

    # Normalize DATABASE_URL for SQLAlchemy (prefer psycopg3 driver)
    database_url = os.environ.get('DATABASE_URL') or app.config.get('SQLALCHEMY_DATABASE_URI')
    if database_url:
        if database_url.startswith('postgres://'):
            database_url = database_url.replace('postgres://', 'postgresql+psycopg://', 1)
        elif database_url.startswith('postgresql://') and '+psycopg' not in database_url:
            database_url = database_url.replace('postgresql://', 'postgresql+psycopg://', 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    
    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    csrf.init_app(app)

    # Make csrf_token() available in templates
    @app.context_processor
    def inject_csrf_token():
        return dict(csrf_token=generate_csrf)

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
        # Auto-seed if database is empty (first deploys)
        try:
            from models.concept import Concept
            if Concept.query.count() == 0:
                # Import here to avoid circular imports at module import time
                import seed_data as seeder
                seeder.seed_concepts()
                seeder.seed_practice_problems()
                seeder.seed_transformations()
            else:
                # Ensure transformations exist even if base seed ran earlier
                import seed_data as seeder
                seeder.seed_transformations()
        except Exception:
            # Fail silently to avoid blocking app startup in production
            pass
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
