from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from models.progress import ProgressRecord
from models.concept import Concept
from models.practice import PracticeAttempt
from app import db
from datetime import datetime, timedelta
import json

progress_bp = Blueprint('progress', __name__)

@progress_bp.route('/')
@login_required
def progress_overview():
    """Show overall progress overview"""
    # Get all concepts
    concepts = Concept.query.order_by(Concept.order_in_curriculum).all()
    
    # Get user's progress
    progress_records = ProgressRecord.query.filter_by(user_id=current_user.id).all()
    progress_dict = {pr.concept_id: pr for pr in progress_records}
    
    # Calculate statistics
    total_concepts = len(concepts)
    completed_concepts = sum(1 for pr in progress_records if pr.completed)
    in_progress = sum(1 for pr in progress_records if not pr.completed and pr.attempts > 0)
    not_started = total_concepts - completed_concepts - in_progress
    
    # Calculate average score
    total_score = sum(pr.score for pr in progress_records)
    average_score = total_score / len(progress_records) if progress_records else 0
    
    # Get recent activity
    recent_attempts = PracticeAttempt.query.filter_by(user_id=current_user.id)\
        .order_by(PracticeAttempt.completed_at.desc()).limit(10).all()
    
    return render_template('progress/overview.html',
                         concepts=concepts,
                         progress_dict=progress_dict,
                         total_concepts=total_concepts,
                         completed_concepts=completed_concepts,
                         in_progress=in_progress,
                         not_started=not_started,
                         average_score=average_score,
                         recent_attempts=recent_attempts)

@progress_bp.route('/concept/<int:concept_id>')
@login_required
def concept_progress(concept_id):
    """Show detailed progress for a specific concept"""
    concept = Concept.query.get_or_404(concept_id)
    progress = ProgressRecord.query.filter_by(
        user_id=current_user.id,
        concept_id=concept_id
    ).first()
    
    # Get practice attempts for this concept
    attempts = PracticeAttempt.query.join(PracticeProblem)\
        .filter(PracticeProblem.concept_id == concept_id,
                PracticeAttempt.user_id == current_user.id)\
        .order_by(PracticeAttempt.completed_at.desc()).all()
    
    return render_template('progress/concept.html',
                         concept=concept,
                         progress=progress,
                         attempts=attempts)

@progress_bp.route('/stats')
@login_required
def progress_stats():
    """Show detailed statistics and analytics"""
    # Get all progress records
    progress_records = ProgressRecord.query.filter_by(user_id=current_user.id).all()
    
    # Calculate various statistics
    total_score = sum(pr.score for pr in progress_records)
    total_time = sum(pr.time_spent for pr in progress_records)
    total_attempts = sum(pr.attempts for pr in progress_records)
    
    # Get practice statistics
    practice_attempts = PracticeAttempt.query.filter_by(user_id=current_user.id).all()
    correct_answers = sum(1 for pa in practice_attempts if pa.is_correct)
    total_practice = len(practice_attempts)
    accuracy = (correct_answers / total_practice * 100) if total_practice > 0 else 0
    
    # Weekly progress (last 4 weeks)
    four_weeks_ago = datetime.utcnow() - timedelta(weeks=4)
    recent_progress = ProgressRecord.query.filter(
        ProgressRecord.user_id == current_user.id,
        ProgressRecord.last_attempt >= four_weeks_ago
    ).all()
    
    weekly_data = []
    for i in range(4):
        week_start = datetime.utcnow() - timedelta(weeks=i+1)
        week_end = datetime.utcnow() - timedelta(weeks=i)
        week_progress = [pr for pr in recent_progress 
                        if week_start <= pr.last_attempt < week_end]
        weekly_data.append({
            'week': f'Week {4-i}',
            'concepts_attempted': len(week_progress),
            'average_score': sum(pr.score for pr in week_progress) / len(week_progress) if week_progress else 0
        })
    
    return render_template('progress/stats.html',
                         total_score=total_score,
                         total_time=total_time,
                         total_attempts=total_attempts,
                         accuracy=accuracy,
                         correct_answers=correct_answers,
                         total_practice=total_practice,
                         weekly_data=weekly_data)

@progress_bp.route('/achievements')
@login_required
def achievements():
    """Show user achievements and badges"""
    # Get user's progress
    progress_records = ProgressRecord.query.filter_by(user_id=current_user.id).all()
    completed_concepts = [pr for pr in progress_records if pr.completed]
    
    # Define achievements
    achievements = []
    
    # Concept completion achievements
    if len(completed_concepts) >= 1:
        achievements.append({
            'name': 'First Steps',
            'description': 'Complete your first concept',
            'icon': '🎯',
            'earned': True,
            'date': min(pr.completed_at for pr in completed_concepts)
        })
    
    if len(completed_concepts) >= 5:
        achievements.append({
            'name': 'Math Explorer',
            'description': 'Complete 5 concepts',
            'icon': '🌟',
            'earned': True,
            'date': sorted([pr.completed_at for pr in completed_concepts])[4]
        })
    
    if len(completed_concepts) >= 10:
        achievements.append({
            'name': 'Math Master',
            'description': 'Complete 10 concepts',
            'icon': '👑',
            'earned': True,
            'date': sorted([pr.completed_at for pr in completed_concepts])[9]
        })
    
    # Score achievements
    total_score = sum(pr.score for pr in progress_records)
    if total_score >= 100:
        achievements.append({
            'name': 'Century Club',
            'description': 'Earn 100 total points',
            'icon': '💯',
            'earned': True,
            'date': datetime.utcnow()
        })
    
    if total_score >= 500:
        achievements.append({
            'name': 'High Achiever',
            'description': 'Earn 500 total points',
            'icon': '🏆',
            'earned': True,
            'date': datetime.utcnow()
        })
    
    # Add unearned achievements for motivation
    if len(completed_concepts) < 15:
        achievements.append({
            'name': 'Math Champion',
            'description': 'Complete 15 concepts',
            'icon': '🏅',
            'earned': False,
            'date': None
        })
    
    if total_score < 1000:
        achievements.append({
            'name': 'Ultimate Math',
            'description': 'Earn 1000 total points',
            'icon': '💎',
            'earned': False,
            'date': None
        })
    
    return render_template('progress/achievements.html', achievements=achievements)

@progress_bp.route('/api/chart-data')
@login_required
def chart_data():
    """API endpoint for chart data"""
    # Get progress over time
    progress_records = ProgressRecord.query.filter_by(user_id=current_user.id)\
        .order_by(ProgressRecord.last_attempt).all()
    
    chart_data = []
    cumulative_score = 0
    
    for pr in progress_records:
        cumulative_score += pr.score
        chart_data.append({
            'date': pr.last_attempt.strftime('%Y-%m-%d'),
            'score': cumulative_score,
            'concept': pr.concept.name
        })
    
    return jsonify(chart_data)
