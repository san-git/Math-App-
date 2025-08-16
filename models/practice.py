from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

# Import db from app
from app import db

class PracticeProblem(db.Model):
    """Model representing practice problems for concepts"""
    id = db.Column(db.Integer, primary_key=True)
    concept_id = db.Column(db.Integer, db.ForeignKey('concept.id'), nullable=False)
    
    # Problem data
    question = db.Column(db.Text, nullable=False)
    problem_type = db.Column(db.String(50), nullable=False)  # multiple_choice, fill_blank, etc.
    difficulty = db.Column(db.Integer, default=1)  # 1-5 scale
    
    # Answer data (stored as JSON for flexibility)
    correct_answer = db.Column(db.Text, nullable=False)
    options = db.Column(db.Text)  # JSON string for multiple choice
    explanation = db.Column(db.Text)
    
    # Metadata
    points = db.Column(db.Integer, default=10)
    time_limit = db.Column(db.Integer, default=120)  # seconds
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    attempts = db.relationship('PracticeAttempt', backref='problem', lazy=True)
    
    def __repr__(self):
        return f'<PracticeProblem {self.id}:{self.problem_type}>'
    
    def get_options_list(self):
        """Get options as list for multiple choice problems"""
        if self.options:
            return json.loads(self.options)
        return []
    
    def check_answer(self, user_answer):
        """Check if user answer is correct"""
        return str(user_answer).strip().lower() == str(self.correct_answer).strip().lower()

class PracticeAttempt(db.Model):
    """Model tracking user attempts at practice problems"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    problem_id = db.Column(db.Integer, db.ForeignKey('practice_problem.id'), nullable=False)
    
    # Attempt data
    user_answer = db.Column(db.Text, nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    time_taken = db.Column(db.Integer, default=0)  # seconds
    score = db.Column(db.Integer, default=0)
    
    # Timestamps
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<PracticeAttempt {self.user_id}:{self.problem_id}>'
    
    def calculate_score(self):
        """Calculate score based on correctness and time"""
        if self.is_correct:
            base_score = self.problem.points
            # Bonus for speed (if completed in less than 60 seconds)
            if self.time_taken < 60:
                time_bonus = int((60 - self.time_taken) / 10)
                self.score = min(100, base_score + time_bonus)
            else:
                self.score = base_score
        else:
            self.score = 0
        return self.score
