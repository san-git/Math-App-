from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from models.practice import PracticeProblem, PracticeAttempt
from models.concept import Concept
from app import db
from datetime import datetime
import json

practice_bp = Blueprint('practice', __name__)

@practice_bp.route('/')
@login_required
def practice_home():
    """Practice home page with concept selection"""
    concepts = Concept.query.order_by(Concept.order_in_curriculum).all()
    return render_template('practice/home.html', concepts=concepts)

@practice_bp.route('/concept/<int:concept_id>')
@login_required
def practice_concept(concept_id):
    """Practice problems for a specific concept"""
    concept = Concept.query.get_or_404(concept_id)
    problems = PracticeProblem.query.filter_by(concept_id=concept_id).all()
    
    if not problems:
        flash('No practice problems available for this concept.', 'info')
        return redirect(url_for('concepts.concept_detail', slug=concept.slug))
    
    return render_template('practice/concept.html',
                         concept=concept,
                         problems=problems)

@practice_bp.route('/problem/<int:problem_id>')
@login_required
def practice_problem(problem_id):
    """Individual practice problem"""
    problem = PracticeProblem.query.get_or_404(problem_id)
    concept = Concept.query.get(problem.concept_id)
    
    return render_template('practice/problem.html',
                         problem=problem,
                         concept=concept)

@practice_bp.route('/submit/<int:problem_id>', methods=['POST'])
@login_required
def submit_answer(problem_id):
    """Submit answer for a practice problem"""
    problem = PracticeProblem.query.get_or_404(problem_id)
    
    data = request.get_json()
    user_answer = data.get('answer', '')
    time_taken = data.get('time_taken', 0)
    
    # Check if answer is correct
    is_correct = problem.check_answer(user_answer)
    
    # Create attempt record
    attempt = PracticeAttempt(
        user_id=current_user.id,
        problem_id=problem_id,
        user_answer=user_answer,
        is_correct=is_correct,
        time_taken=time_taken
    )
    
    # Calculate score
    score = attempt.calculate_score()
    
    db.session.add(attempt)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'correct': is_correct,
        'score': score,
        'explanation': problem.explanation if problem.explanation else None
    })

@practice_bp.route('/quiz/<int:concept_id>')
@login_required
def concept_quiz(concept_id):
    """Quiz mode for a concept with multiple problems"""
    concept = Concept.query.get_or_404(concept_id)
    problems = PracticeProblem.query.filter_by(concept_id=concept_id).limit(10).all()
    
    if not problems:
        flash('No problems available for quiz mode.', 'info')
        return redirect(url_for('concepts.concept_detail', slug=concept.slug))
    
    return render_template('practice/quiz.html',
                         concept=concept,
                         problems=problems)

@practice_bp.route('/quiz/submit', methods=['POST'])
@login_required
def submit_quiz():
    """Submit quiz answers and calculate final score"""
    data = request.get_json()
    concept_id = data.get('concept_id')
    answers = data.get('answers', {})
    total_time = data.get('total_time', 0)
    
    concept = Concept.query.get_or_404(concept_id)
    problems = PracticeProblem.query.filter_by(concept_id=concept_id).all()
    
    total_score = 0
    correct_answers = 0
    
    for problem in problems:
        if str(problem.id) in answers:
            user_answer = answers[str(problem.id)]
            is_correct = problem.check_answer(user_answer)
            
            if is_correct:
                correct_answers += 1
                total_score += problem.points
            
            # Record attempt
            attempt = PracticeAttempt(
                user_id=current_user.id,
                problem_id=problem.id,
                user_answer=user_answer,
                is_correct=is_correct,
                time_taken=total_time // len(problems)  # Approximate time per problem
            )
            attempt.calculate_score()
            db.session.add(attempt)
    
    # Calculate percentage score
    percentage_score = (correct_answers / len(problems)) * 100 if problems else 0
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'total_score': total_score,
        'correct_answers': correct_answers,
        'total_problems': len(problems),
        'percentage': percentage_score
    })

@practice_bp.route('/history')
@login_required
def practice_history():
    """Show user's practice history"""
    attempts = PracticeAttempt.query.filter_by(user_id=current_user.id)\
        .order_by(PracticeAttempt.completed_at.desc()).limit(50).all()
    
    return render_template('practice/history.html', attempts=attempts)
