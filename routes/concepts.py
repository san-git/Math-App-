from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from models.concept import Concept
from models.progress import ProgressRecord
from models.practice import PracticeProblem
from app import db, csrf

concepts_bp = Blueprint('concepts', __name__)

@concepts_bp.route('/')
@login_required
def concept_list():
    """List all available concepts"""
    concepts = Concept.query.order_by(Concept.order_in_curriculum).all()
    
    # Get user's progress
    progress_records = ProgressRecord.query.filter_by(user_id=current_user.id).all()
    completed_concepts = {pr.concept_id for pr in progress_records if pr.completed}
    
    return render_template('concepts/list.html',
                         concepts=concepts,
                         completed_concepts=completed_concepts)

@concepts_bp.route('/<slug>')
@login_required
def concept_detail(slug):
    """Show concept lesson and details"""
    concept = Concept.query.filter_by(slug=slug).first_or_404()
    
    # Check if user can access this concept
    progress_records = ProgressRecord.query.filter_by(user_id=current_user.id).all()
    completed_concepts = {pr.concept_id for pr in progress_records if pr.completed}
    
    if not concept.is_available_for_user(completed_concepts):
        flash('You need to complete prerequisite concepts first!', 'warning')
        return redirect(url_for('concepts.concept_list'))
    
    # Get user's progress for this concept
    user_progress = ProgressRecord.query.filter_by(
        user_id=current_user.id,
        concept_id=concept.id
    ).first()
    
    # Get practice problems for this concept
    practice_problems = PracticeProblem.query.filter_by(concept_id=concept.id).limit(5).all()
    
    return render_template('concepts/detail.html',
                         concept=concept,
                         user_progress=user_progress,
                         practice_problems=practice_problems)

@concepts_bp.route('/<slug>/practice')
@login_required
def concept_practice(slug):
    """Practice problems for a specific concept"""
    concept = Concept.query.filter_by(slug=slug).first_or_404()
    
    # Get practice problems
    problems = PracticeProblem.query.filter_by(concept_id=concept.id).all()
    
    if not problems:
        flash('No practice problems available for this concept yet.', 'info')
        return redirect(url_for('concepts.concept_detail', slug=slug))
    
    return render_template('concepts/practice.html',
                         concept=concept,
                         problems=problems)

@concepts_bp.route('/<slug>/complete', methods=['POST'])
@login_required
@csrf.exempt
def mark_concept_complete(slug):
    """Mark a concept as completed"""
    concept = Concept.query.filter_by(slug=slug).first_or_404()
    
    # Get or create progress record
    progress = ProgressRecord.query.filter_by(
        user_id=current_user.id,
        concept_id=concept.id
    ).first()
    
    if not progress:
        progress = ProgressRecord(
            user_id=current_user.id,
            concept_id=concept.id,
            score=100,
            completed=True
        )
        db.session.add(progress)
    else:
        progress.score = 100
        progress.completed = True
    
    db.session.commit()
    
    flash(f'Congratulations! You completed "{concept.name}"!', 'success')
    return redirect(url_for('concepts.concept_detail', slug=slug))

@concepts_bp.route('/<slug>/progress', methods=['POST'])
@login_required
@csrf.exempt
def update_progress(slug):
    """Update user progress for a concept"""
    concept = Concept.query.filter_by(slug=slug).first_or_404()
    
    data = request.get_json()
    score = data.get('score', 0)
    time_spent = data.get('time_spent', 0)
    
    # Get or create progress record
    progress = ProgressRecord.query.filter_by(
        user_id=current_user.id,
        concept_id=concept.id
    ).first()
    
    if not progress:
        progress = ProgressRecord(
            user_id=current_user.id,
            concept_id=concept.id
        )
        db.session.add(progress)
    
    progress.update_progress(score, time_spent)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'new_score': progress.score,
        'completed': progress.completed
    })
