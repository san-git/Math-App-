from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Import db from app
from app import db

class ProgressRecord(db.Model):
    """Model tracking user progress through concepts"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    concept_id = db.Column(db.Integer, db.ForeignKey('concept.id'), nullable=False)
    
    # Progress data
    score = db.Column(db.Integer, default=0)  # 0-100
    attempts = db.Column(db.Integer, default=0)
    time_spent = db.Column(db.Integer, default=0)  # in seconds
    completed = db.Column(db.Boolean, default=False)
    
    # Timestamps
    first_attempt = db.Column(db.DateTime, default=datetime.utcnow)
    last_attempt = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    
    def __repr__(self):
        return f'<ProgressRecord {self.user_id}:{self.concept_id}>'
    
    def update_progress(self, new_score, time_spent_seconds):
        """Update progress with new attempt"""
        self.attempts += 1
        self.score = max(self.score, new_score)  # Keep best score
        self.time_spent += time_spent_seconds
        self.last_attempt = datetime.utcnow()
        
        if new_score >= 80 and not self.completed:
            self.completed = True
            self.completed_at = datetime.utcnow()
    
    def get_progress_percentage(self):
        """Get progress as percentage"""
        return min(100, self.score)
