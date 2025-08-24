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
        """Check if concept is available based on user's completed concepts.

        Accepts a set of completed concept identifiers which may be either
        slugs (strings) or ids (integers). Prerequisites are defined as slugs,
        so if the provided set contains ids, we resolve prerequisite slugs to
        their corresponding ids before checking availability.
        """
        prereq_slugs = self.get_prerequisites_list()
        if not prereq_slugs:
            return True

        if not user_progress:
            return False

        # Detect whether user_progress contains ids (ints) or slugs (str)
        sample_item = next(iter(user_progress))
        if isinstance(sample_item, int):
            # user_progress is a set of ids; resolve prereq slugs to ids
            prereq_concepts = Concept.query.filter(Concept.slug.in_(prereq_slugs)).all()
            prereq_ids = {c.id for c in prereq_concepts}
            return prereq_ids.issubset(user_progress)
        else:
            # user_progress is expected to be a set of slugs
            return set(prereq_slugs).issubset(user_progress)
