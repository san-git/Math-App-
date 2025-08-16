from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from models.user import User
from models.concept import Concept
from models.progress import ProgressRecord
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Home page for non-authenticated users"""
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    """User dashboard showing progress and available concepts"""
    # Get user's progress
    progress_records = ProgressRecord.query.filter_by(user_id=current_user.id).all()
    completed_concepts = {pr.concept_id for pr in progress_records if pr.completed}
    
    # Get all concepts ordered by curriculum
    concepts = Concept.query.order_by(Concept.order_in_curriculum).all()
    
    # Calculate overall progress
    total_concepts = len(concepts)
    completed_count = len(completed_concepts)
    progress_percentage = (completed_count / total_concepts * 100) if total_concepts > 0 else 0
    
    # Get next available concept
    next_concept = None
    for concept in concepts:
        if concept.id not in completed_concepts and concept.is_available_for_user(completed_concepts):
            next_concept = concept
            break
    
    return render_template('dashboard.html',
                         concepts=concepts,
                         progress_records=progress_records,
                         completed_concepts=completed_concepts,
                         progress_percentage=progress_percentage,
                         next_concept=next_concept)

@main_bp.route('/about')
def about():
    """About page explaining the math game"""
    return render_template('about.html')

@main_bp.route('/curriculum')
def curriculum():
    """Curriculum overview page"""
    concepts = Concept.query.order_by(Concept.order_in_curriculum).all()
    return render_template('curriculum.html', concepts=concepts)
