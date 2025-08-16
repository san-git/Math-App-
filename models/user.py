from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Import db from app
from app import db

class User(UserMixin, db.Model):
    """User model for authentication and progress tracking"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    # Progress tracking
    current_concept = db.Column(db.String(100), default='number_systems')
    total_score = db.Column(db.Integer, default=0)
    concepts_completed = db.Column(db.Integer, default=0)
    
    # Relationships
    progress_records = db.relationship('ProgressRecord', backref='user', lazy=True)
    practice_attempts = db.relationship('PracticeAttempt', backref='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def update_progress(self, concept, score):
        """Update user progress for a specific concept"""
        self.current_concept = concept
        self.total_score += score
        if score >= 80:  # 80% threshold for concept completion
            self.concepts_completed += 1
    
    def __repr__(self):
        return f'<User {self.username}>'
