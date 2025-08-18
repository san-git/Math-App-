from flask import Blueprint, render_template, request, jsonify
from models.concept import Concept
from models.practice import PracticeProblem
from app import db, csrf

guest_bp = Blueprint('guest', __name__)

@guest_bp.route('/')
def guest_home():
    """Guest home page with concept overview"""
    concepts = Concept.query.order_by(Concept.order_in_curriculum).all()
    return render_template('guest/home.html', concepts=concepts)

@guest_bp.route('/concepts')
def guest_concepts():
    """List all concepts for guests"""
    concepts = Concept.query.order_by(Concept.order_in_curriculum).all()
    return render_template('guest/concepts.html', concepts=concepts)

@guest_bp.route('/concept/<slug>')
def guest_concept_detail(slug):
    """Show concept lesson for guests"""
    concept = Concept.query.filter_by(slug=slug).first_or_404()
    
    # Get practice problems for this concept
    practice_problems = PracticeProblem.query.filter_by(concept_id=concept.id).limit(3).all()
    
    return render_template('guest/concept_detail.html',
                         concept=concept,
                         practice_problems=practice_problems)

@guest_bp.route('/practice/<int:concept_id>')
def guest_practice(concept_id):
    """Practice problems for guests"""
    concept = Concept.query.get_or_404(concept_id)
    problems = PracticeProblem.query.filter_by(concept_id=concept_id).limit(5).all()
    
    if not problems:
        return render_template('guest/no_practice.html', concept=concept)
    
    return render_template('guest/practice.html',
                         concept=concept,
                         problems=problems)

@guest_bp.route('/practice/submit/<int:problem_id>', methods=['POST'])
@csrf.exempt
def guest_submit_answer(problem_id):
    """Submit answer for guest practice (no scoring)"""
    problem = PracticeProblem.query.get_or_404(problem_id)
    
    data = request.get_json()
    user_answer = data.get('answer', '')
    
    # Check if answer is correct
    is_correct = problem.check_answer(user_answer)
    
    return jsonify({
        'success': True,
        'correct': is_correct,
        'explanation': problem.explanation if problem.explanation else None,
        'message': 'Great job! This is how guest mode works. Create an account to track your progress!'
    })

@guest_bp.route('/demo')
def guest_demo():
    """Demo page showing what the full app offers"""
    return render_template('guest/demo.html')
