from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Import db from app
from app import db

class Concept(db.Model):
    """Model representing a math concept in the curriculum"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    difficulty_level = db.Column(db.Integer, default=1)  # 1-5 scale
    order_in_curriculum = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    
    # Content
    lesson_content = db.Column(db.Text, nullable=False)
    examples = db.Column(db.Text)  # JSON string of examples
    prerequisites = db.Column(db.String(200))  # Comma-separated concept slugs
    
    # Metadata
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    progress_records = db.relationship('ProgressRecord', backref='concept', lazy=True)
    practice_problems = db.relationship('PracticeProblem', backref='concept', lazy=True)
    
    def __repr__(self):
        return f'<Concept {self.name}>'
    
    def get_prerequisites_list(self):
        """Get list of prerequisite concept slugs"""
        if self.prerequisites:
            return [p.strip() for p in self.prerequisites.split(',')]
        return []
    
    def is_available_for_user(self, user_progress):
        """Check if concept is available based on user's completed concepts"""
        prereqs = self.get_prerequisites_list()
        if not prereqs:
            return True
        return all(prereq in user_progress for prereq in prereqs)
