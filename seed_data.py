#!/usr/bin/env python3
"""
Data seeding script for 8th Grade Math Game
Populates the database with concepts and practice problems
"""

import json
from app import create_app, db
from models.user import User
from models.concept import Concept
from models.practice import PracticeProblem

def seed_concepts():
    """Seed the database with 8th-grade math concepts"""
    
    concepts_data = [
        {
            "name": "Number Systems",
            "slug": "number_systems",
            "description": "Understanding rational and irrational numbers, real numbers, and their properties",
            "difficulty_level": 1,
            "order_in_curriculum": 1,
            "category": "Numbers and Operations",
            "lesson_content": """
            <h2>Number Systems</h2>
            <p>In 8th grade, we explore different types of numbers and how they relate to each other.</p>
            
            <h3>Rational Numbers</h3>
            <p>Rational numbers can be expressed as fractions where both numerator and denominator are integers.</p>
            <ul>
                <li>Examples: 1/2, -3/4, 5/1, 0.75</li>
                <li>All integers are rational numbers</li>
                <li>Terminating and repeating decimals are rational</li>
            </ul>
            
            <h3>Irrational Numbers</h3>
            <p>Irrational numbers cannot be expressed as simple fractions.</p>
            <ul>
                <li>Examples: √2, π, e</li>
                <li>Non-terminating, non-repeating decimals</li>
                <li>Cannot be written as a/b where a and b are integers</li>
            </ul>
            
            <h3>Real Numbers</h3>
            <p>The set of all rational and irrational numbers together form the real numbers.</p>
            <p>Every point on the number line represents a real number.</p>
            """,
            "examples": json.dumps([
                {"question": "Is 0.333... rational or irrational?", "answer": "Rational (it's 1/3)"},
                {"question": "What type of number is √9?", "answer": "Rational (it equals 3)"},
                {"question": "Is π rational?", "answer": "Irrational"}
            ]),
            "prerequisites": ""
        },
        {
            "name": "Exponents and Powers",
            "slug": "exponents_powers",
            "description": "Working with exponents, scientific notation, and power rules",
            "difficulty_level": 2,
            "order_in_curriculum": 2,
            "category": "Numbers and Operations",
            "lesson_content": """
            <h2>Exponents and Powers</h2>
            <p>Exponents are a way to represent repeated multiplication.</p>
            
            <h3>Basic Exponent Rules</h3>
            <ul>
                <li><strong>Product Rule:</strong> a^m × a^n = a^(m+n)</li>
                <li><strong>Quotient Rule:</strong> a^m ÷ a^n = a^(m-n)</li>
                <li><strong>Power Rule:</strong> (a^m)^n = a^(m×n)</li>
                <li><strong>Zero Exponent:</strong> a^0 = 1 (where a ≠ 0)</li>
                <li><strong>Negative Exponent:</strong> a^(-n) = 1/a^n</li>
            </ul>
            
            <h3>Scientific Notation</h3>
            <p>Scientific notation expresses numbers as a × 10^n where 1 ≤ a < 10.</p>
            <ul>
                <li>Examples: 3.2 × 10^5 = 320,000</li>
                <li>2.1 × 10^(-3) = 0.0021</li>
            </ul>
            """,
            "examples": json.dumps([
                {"question": "Simplify: 2^3 × 2^4", "answer": "2^7 = 128"},
                {"question": "What is 5^0?", "answer": "1"},
                {"question": "Convert 0.00045 to scientific notation", "answer": "4.5 × 10^(-4)"}
            ]),
            "prerequisites": "number_systems"
        },
        {
            "name": "Linear Equations",
            "slug": "linear_equations",
            "description": "Solving one-variable linear equations and inequalities",
            "difficulty_level": 2,
            "order_in_curriculum": 3,
            "category": "Algebra",
            "lesson_content": """
            <h2>Linear Equations</h2>
            <p>Linear equations are equations where the variable is raised only to the first power.</p>
            
            <h3>Solving Linear Equations</h3>
            <p>Steps to solve:</p>
            <ol>
                <li>Simplify both sides</li>
                <li>Collect variable terms on one side</li>
                <li>Collect constant terms on the other side</li>
                <li>Divide by the coefficient of the variable</li>
            </ol>
            
            <h3>Example</h3>
            <p>Solve: 3x + 5 = 2x + 8</p>
            <p>Step 1: Subtract 2x from both sides</p>
            <p>3x - 2x + 5 = 8</p>
            <p>Step 2: Subtract 5 from both sides</p>
            <p>x = 3</p>
            
            <h3>Linear Inequalities</h3>
            <p>Solve inequalities the same way as equations, but remember to reverse the inequality sign when multiplying or dividing by a negative number.</p>
            """,
            "examples": json.dumps([
                {"question": "Solve: 2x + 3 = 11", "answer": "x = 4"},
                {"question": "Solve: 3x - 7 > 8", "answer": "x > 5"},
                {"question": "Solve: 4(x + 2) = 20", "answer": "x = 3"}
            ]),
            "prerequisites": "exponents_powers"
        },
        {
            "name": "Functions",
            "slug": "functions",
            "description": "Understanding functions, domain, range, and function notation",
            "difficulty_level": 3,
            "order_in_curriculum": 4,
            "category": "Algebra",
            "lesson_content": """
            <h2>Functions</h2>
            <p>A function is a special relationship where each input has exactly one output.</p>
            
            <h3>Function Notation</h3>
            <p>f(x) = 2x + 3 means:</p>
            <ul>
                <li>f is the function name</li>
                <li>x is the input variable</li>
                <li>2x + 3 is the rule</li>
                <li>f(2) = 2(2) + 3 = 7</li>
            </ul>
            
            <h3>Domain and Range</h3>
            <ul>
                <li><strong>Domain:</strong> All possible input values (x-values)</li>
                <li><strong>Range:</strong> All possible output values (y-values)</li>
            </ul>
            
            <h3>Linear Functions</h3>
            <p>f(x) = mx + b where:</p>
            <ul>
                <li>m is the slope</li>
                <li>b is the y-intercept</li>
            </ul>
            """,
            "examples": json.dumps([
                {"question": "If f(x) = 3x - 2, find f(4)", "answer": "10"},
                {"question": "What is the domain of f(x) = √x?", "answer": "x ≥ 0"},
                {"question": "Find the slope of f(x) = -2x + 5", "answer": "-2"}
            ]),
            "prerequisites": "linear_equations"
        },
        {
            "name": "Geometry Basics",
            "slug": "geometry_basics",
            "description": "Angles, triangles, quadrilaterals, and basic geometric properties",
            "difficulty_level": 2,
            "order_in_curriculum": 5,
            "category": "Geometry",
            "lesson_content": """
            <h2>Geometry Basics</h2>
            <p>Geometry is the study of shapes, sizes, and properties of figures.</p>
            
            <h3>Angles</h3>
            <ul>
                <li><strong>Acute:</strong> Less than 90°</li>
                <li><strong>Right:</strong> Exactly 90°</li>
                <li><strong>Obtuse:</strong> Between 90° and 180°</li>
                <li><strong>Straight:</strong> Exactly 180°</li>
            </ul>
            
            <h3>Triangles</h3>
            <ul>
                <li><strong>Sum of angles:</strong> Always 180°</li>
                <li><strong>Types by sides:</strong> Equilateral, isosceles, scalene</li>
                <li><strong>Types by angles:</strong> Acute, right, obtuse</li>
            </ul>
            
            <h3>Quadrilaterals</h3>
            <ul>
                <li><strong>Parallelogram:</strong> Opposite sides parallel and equal</li>
                <li><strong>Rectangle:</strong> All angles 90°</li>
                <li><strong>Square:</strong> All sides equal, all angles 90°</li>
                <li><strong>Trapezoid:</strong> One pair of parallel sides</li>
            </ul>
            """,
            "examples": json.dumps([
                {"question": "What is the sum of angles in a triangle?", "answer": "180°"},
                {"question": "If two angles of a triangle are 45° and 60°, what is the third?", "answer": "75°"},
                {"question": "What type of triangle has all sides equal?", "answer": "Equilateral"}
            ]),
            "prerequisites": ""
        },
        {
            "name": "Pythagorean Theorem",
            "slug": "pythagorean_theorem",
            "description": "Understanding and applying the Pythagorean theorem",
            "difficulty_level": 3,
            "order_in_curriculum": 6,
            "category": "Geometry",
            "lesson_content": """
            <h2>Pythagorean Theorem</h2>
            <p>In a right triangle, the square of the hypotenuse equals the sum of squares of the other two sides.</p>
            
            <h3>Formula</h3>
            <p>a² + b² = c²</p>
            <p>Where c is the hypotenuse (longest side, opposite the right angle)</p>
            
            <h3>When to Use</h3>
            <ul>
                <li>Only works for right triangles</li>
                <li>Use to find missing side lengths</li>
                <li>Use to check if a triangle is right</li>
            </ul>
            
            <h3>Example</h3>
            <p>Find the hypotenuse of a right triangle with legs 3 and 4:</p>
            <p>3² + 4² = c²</p>
            <p>9 + 16 = c²</p>
            <p>25 = c²</p>
            <p>c = 5</p>
            """,
            "examples": json.dumps([
                {"question": "In a right triangle, if a=6 and b=8, find c", "answer": "10"},
                {"question": "Is a triangle with sides 5, 12, 13 a right triangle?", "answer": "Yes (5²+12²=13²)"},
                {"question": "Find the missing leg if hypotenuse=10 and one leg=6", "answer": "8"}
            ]),
            "prerequisites": "geometry_basics"
        },
        {
            "name": "Data Analysis",
            "slug": "data_analysis",
            "description": "Measures of central tendency, variability, and data interpretation",
            "difficulty_level": 2,
            "order_in_curriculum": 7,
            "category": "Statistics and Probability",
            "lesson_content": """
            <h2>Data Analysis</h2>
            <p>Data analysis helps us understand and interpret information.</p>
            
            <h3>Measures of Central Tendency</h3>
            <ul>
                <li><strong>Mean:</strong> Average (sum of all values ÷ number of values)</li>
                <li><strong>Median:</strong> Middle value when data is ordered</li>
                <li><strong>Mode:</strong> Most frequent value</li>
            </ul>
            
            <h3>Measures of Variability</h3>
            <ul>
                <li><strong>Range:</strong> Difference between highest and lowest values</li>
                <li><strong>Interquartile Range (IQR):</strong> Q3 - Q1</li>
            </ul>
            
            <h3>Box Plots</h3>
            <p>Show the distribution of data using:</p>
            <ul>
                <li>Minimum and maximum values</li>
                <li>First and third quartiles</li>
                <li>Median</li>
            </ul>
            """,
            "examples": json.dumps([
                {"question": "Find the mean of: 2, 4, 6, 8, 10", "answer": "6"},
                {"question": "Find the median of: 1, 3, 5, 7, 9", "answer": "5"},
                {"question": "What is the range of: 5, 8, 12, 15, 20?", "answer": "15"}
            ]),
            "prerequisites": ""
        },
        {
            "name": "Probability",
            "slug": "probability",
            "description": "Basic probability concepts, experimental vs theoretical probability",
            "difficulty_level": 3,
            "order_in_curriculum": 8,
            "category": "Statistics and Probability",
            "lesson_content": """
            <h2>Probability</h2>
            <p>Probability measures how likely an event is to occur.</p>
            
            <h3>Basic Probability</h3>
            <p>P(event) = Number of favorable outcomes / Total number of possible outcomes</p>
            <p>Probability is always between 0 and 1 (or 0% and 100%)</p>
            
            <h3>Types of Probability</h3>
            <ul>
                <li><strong>Theoretical:</strong> Based on mathematical calculations</li>
                <li><strong>Experimental:</strong> Based on actual experiments or data</li>
            </ul>
            
            <h3>Example</h3>
            <p>What's the probability of rolling a 3 on a fair die?</p>
            <p>Favorable outcomes: 1 (rolling a 3)</p>
            <p>Total outcomes: 6 (1, 2, 3, 4, 5, 6)</p>
            <p>P(3) = 1/6 ≈ 0.167 or 16.7%</p>
            """,
            "examples": json.dumps([
                {"question": "What's the probability of flipping heads on a coin?", "answer": "1/2 or 0.5"},
                {"question": "What's the probability of rolling an even number on a die?", "answer": "1/2 or 0.5"},
                {"question": "If P(A) = 0.3, what's P(not A)?", "answer": "0.7"}
            ]),
            "prerequisites": "data_analysis"
        }
    ]
    
    for concept_data in concepts_data:
        concept = Concept(**concept_data)
        db.session.add(concept)
    
    db.session.commit()
    print(f"Seeded {len(concepts_data)} concepts")

def seed_practice_problems():
    """Seed practice problems for each concept"""
    
    problems_data = [
        # Number Systems
        {
            "concept_id": 1,
            "question": "Which of the following is a rational number?",
            "problem_type": "multiple_choice",
            "correct_answer": "0.75",
            "options": json.dumps(["√2", "π", "0.75", "e"]),
            "explanation": "0.75 can be written as 3/4, making it a rational number.",
            "difficulty": 1,
            "points": 10
        },
        {
            "concept_id": 1,
            "question": "Is √16 rational or irrational?",
            "problem_type": "multiple_choice",
            "correct_answer": "Rational",
            "options": json.dumps(["Rational", "Irrational", "Neither", "Both"]),
            "explanation": "√16 = 4, which is a whole number and therefore rational.",
            "difficulty": 1,
            "points": 10
        },
        
        # Exponents and Powers
        {
            "concept_id": 2,
            "question": "Simplify: 2³ × 2⁴",
            "problem_type": "multiple_choice",
            "correct_answer": "2⁷",
            "options": json.dumps(["2⁷", "2¹²", "4⁷", "8⁷"]),
            "explanation": "Use the product rule: a^m × a^n = a^(m+n). So 2³ × 2⁴ = 2^(3+4) = 2⁷.",
            "difficulty": 2,
            "points": 15
        },
        {
            "concept_id": 2,
            "question": "What is 5⁰?",
            "problem_type": "fill_blank",
            "correct_answer": "1",
            "explanation": "Any non-zero number raised to the power of 0 equals 1.",
            "difficulty": 1,
            "points": 10
        },
        
        # Linear Equations
        {
            "concept_id": 3,
            "question": "Solve for x: 3x + 5 = 20",
            "problem_type": "fill_blank",
            "correct_answer": "5",
            "explanation": "Subtract 5 from both sides: 3x = 15. Then divide by 3: x = 5.",
            "difficulty": 2,
            "points": 15
        },
        {
            "concept_id": 3,
            "question": "Solve the inequality: 2x - 3 > 7",
            "problem_type": "multiple_choice",
            "correct_answer": "x > 5",
            "options": json.dumps(["x > 5", "x < 5", "x > 2", "x < 2"]),
            "explanation": "Add 3 to both sides: 2x > 10. Then divide by 2: x > 5.",
            "difficulty": 2,
            "points": 15
        },
        
        # Functions
        {
            "concept_id": 4,
            "question": "If f(x) = 2x + 3, find f(4)",
            "problem_type": "fill_blank",
            "correct_answer": "11",
            "explanation": "Substitute x = 4: f(4) = 2(4) + 3 = 8 + 3 = 11.",
            "difficulty": 2,
            "points": 15
        },
        {
            "concept_id": 4,
            "question": "What is the slope of the function f(x) = -3x + 7?",
            "problem_type": "fill_blank",
            "correct_answer": "-3",
            "explanation": "In the form f(x) = mx + b, m is the slope. So the slope is -3.",
            "difficulty": 2,
            "points": 15
        },
        
        # Geometry Basics
        {
            "concept_id": 5,
            "question": "What is the sum of the angles in a triangle?",
            "problem_type": "fill_blank",
            "correct_answer": "180",
            "explanation": "The sum of the interior angles of any triangle is always 180°.",
            "difficulty": 1,
            "points": 10
        },
        {
            "concept_id": 5,
            "question": "If two angles of a triangle are 45° and 60°, what is the third angle?",
            "problem_type": "fill_blank",
            "correct_answer": "75",
            "explanation": "180° - 45° - 60° = 75°.",
            "difficulty": 2,
            "points": 15
        },
        
        # Pythagorean Theorem
        {
            "concept_id": 6,
            "question": "In a right triangle, if the legs are 6 and 8, what is the hypotenuse?",
            "problem_type": "fill_blank",
            "correct_answer": "10",
            "explanation": "Use a² + b² = c²: 6² + 8² = 36 + 64 = 100. So c = √100 = 10.",
            "difficulty": 3,
            "points": 20
        },
        {
            "concept_id": 6,
            "question": "Is a triangle with sides 5, 12, 13 a right triangle?",
            "problem_type": "multiple_choice",
            "correct_answer": "Yes",
            "options": json.dumps(["Yes", "No", "Cannot determine", "Sometimes"]),
            "explanation": "Check: 5² + 12² = 25 + 144 = 169 = 13². So yes, it's a right triangle.",
            "difficulty": 2,
            "points": 15
        },
        
        # Data Analysis
        {
            "concept_id": 7,
            "question": "Find the mean of: 2, 4, 6, 8, 10",
            "problem_type": "fill_blank",
            "correct_answer": "6",
            "explanation": "Mean = (2 + 4 + 6 + 8 + 10) ÷ 5 = 30 ÷ 5 = 6.",
            "difficulty": 1,
            "points": 10
        },
        {
            "concept_id": 7,
            "question": "What is the median of: 1, 3, 5, 7, 9, 11?",
            "problem_type": "fill_blank",
            "correct_answer": "6",
            "explanation": "With 6 numbers, the median is the average of the 3rd and 4th: (5 + 7) ÷ 2 = 6.",
            "difficulty": 2,
            "points": 15
        },
        
        # Probability
        {
            "concept_id": 8,
            "question": "What is the probability of flipping heads on a fair coin?",
            "problem_type": "multiple_choice",
            "correct_answer": "1/2",
            "options": json.dumps(["1/2", "1/4", "1", "0"]),
            "explanation": "There are 2 equally likely outcomes (heads or tails), so P(heads) = 1/2.",
            "difficulty": 1,
            "points": 10
        },
        {
            "concept_id": 8,
            "question": "What is the probability of rolling an even number on a standard die?",
            "problem_type": "fill_blank",
            "correct_answer": "1/2",
            "explanation": "Even numbers on a die: 2, 4, 6. So 3 favorable outcomes out of 6 total = 3/6 = 1/2.",
            "difficulty": 2,
            "points": 15
        }
    ]
    
    for problem_data in problems_data:
        problem = PracticeProblem(**problem_data)
        db.session.add(problem)
    
    db.session.commit()
    print(f"Seeded {len(problems_data)} practice problems")

def seed_transformations():
    """Seed 8th-grade geometry transformations (translations, reflections, rotations, dilations)."""
    from models.concept import Concept
    from models.practice import PracticeProblem

    existing = Concept.query.filter_by(slug="transformations").first()
    if not existing:
        concept = Concept(
            name="Transformations",
            slug="transformations",
            description="Translations, reflections, rotations, and dilations on the coordinate plane",
            difficulty_level=3,
            order_in_curriculum=9,
            category="Geometry",
            lesson_content="""
            <h2>Transformations on the Coordinate Plane</h2>
            <p>A transformation moves or changes a figure to produce a new figure called the image.</p>
            <h3>Translations</h3>
            <p>Slide a figure without rotating or reflecting it. (x, y) → (x + a, y + b)</p>
            <h3>Reflections</h3>
            <p>Flip a figure over a line (axis of reflection). Examples: Over x-axis: (x, y) → (x, −y); Over y-axis: (x, y) → (−x, y)</p>
            <h3>Rotations</h3>
            <p>Turn a figure about the origin by 90°, 180°, or 270°.</p>
            <ul>
                <li>90° CCW: (x, y) → (−y, x)</li>
                <li>180°: (x, y) → (−x, −y)</li>
                <li>270° CCW: (x, y) → (y, −x)</li>
            </ul>
            <h3>Dilations</h3>
            <p>Resize a figure from the origin by a scale factor k: (x, y) → (kx, ky). If k > 1, enlargement; if 0 < k < 1, reduction.</p>
            """,
            examples=json.dumps([
                {"question": "Translate (−3, 4) by (5, −2).", "answer": "(2, 2)"},
                {"question": "Reflect (2, −7) over the y-axis.", "answer": "(−2, −7)"},
                {"question": "Rotate (1, 5) 90° CCW about the origin.", "answer": "(−5, 1)"}
            ]),
            prerequisites="geometry_basics"
        )
        db.session.add(concept)
        db.session.commit()
        existing = concept

    # Seed practice problems tied to the transformations concept
    problems = [
        {
            "question": "Translate the point (−3, 4) by the vector (5, −2). Give the image as (x, y).",
            "problem_type": "fill_blank",
            "correct_answer": "(2, 2)",
            "explanation": "Add component-wise: (−3+5, 4+(−2)) = (2, 2)",
            "difficulty": 2,
            "points": 10
        },
        {
            "question": "Reflect the point (2, −7) across the y-axis. Give the image as (x, y).",
            "problem_type": "fill_blank",
            "correct_answer": "(−2, −7)",
            "explanation": "Reflection across y-axis negates x: (x, y) → (−x, y)",
            "difficulty": 2,
            "points": 10
        },
        {
            "question": "Rotate the point (1, 5) 90° counterclockwise about the origin.",
            "problem_type": "fill_blank",
            "correct_answer": "(−5, 1)",
            "explanation": "90° CCW rotation: (x, y) → (−y, x)",
            "difficulty": 3,
            "points": 15
        },
        {
            "question": "Dilate the point (−4, 3) by a scale factor of k = 1.5 about the origin.",
            "problem_type": "fill_blank",
            "correct_answer": "(−6.0, 4.5)",
            "explanation": "Multiply coordinates by k: (−4×1.5, 3×1.5) = (−6.0, 4.5)",
            "difficulty": 2,
            "points": 10
        },
        {
            "question": "Which rule represents reflection across the x-axis?",
            "problem_type": "multiple_choice",
            "correct_answer": "(x, y) → (x, −y)",
            "options": json.dumps(["(x, y) → (−x, y)", "(x, y) → (x, −y)", "(x, y) → (−y, x)", "(x, y) → (kx, ky)"]),
            "explanation": "Reflection across x-axis negates y.",
            "difficulty": 1,
            "points": 10
        }
    ]

    # Avoid duplicate seeding: only add if there are no practice problems yet for this concept
    existing_problems_count = PracticeProblem.query.filter_by(concept_id=existing.id).count()
    if existing_problems_count == 0:
        for p in problems:
            db.session.add(PracticeProblem(concept_id=existing.id, **p))
        db.session.commit()
        print("Seeded Transformations concept and practice problems")
    else:
        print("Transformations practice problems already exist; skipping")

def seed_additional_8th_grade_concepts():
    """Seed additional 8th-grade concepts if they don't exist yet."""
    from models.concept import Concept
    from models.practice import PracticeProblem

    concepts = [
        {
            "slug": "rigid_transformations",
            "name": "Rigid Transformations",
            "description": "Translations, reflections, and rotations that preserve distance and angle measure",
            "category": "Geometry",
            "order_in_curriculum": 10,
            "difficulty_level": 3,
            "lesson_content": """
            <h2>Rigid Transformations</h2>
            <p>Rigid transformations (isometries) preserve shape and size: translations, reflections, and rotations.</p>
            <ul>
              <li>Translations: (x, y) → (x+a, y+b)</li>
              <li>Reflections: over x-axis (x, y) → (x, −y); over y-axis (x, y) → (−x, y)</li>
              <li>Rotations about origin: 90° CCW (x, y) → (−y, x); 180° (x, y) → (−x, −y)</li>
            </ul>
            <p>Rigid transformations preserve distance, angle measure, and orientation (except reflections change orientation).</p>
            """,
            "examples": json.dumps([
                {"question": "A translation is rigid: True or False?", "answer": "True"},
                {"question": "Rotation preserves distances: True or False?", "answer": "True"}
            ]),
            "prerequisites": "geometry_basics"
        },
        {
            "slug": "congruence",
            "name": "Congruence",
            "description": "Figures are congruent if there is a sequence of rigid motions mapping one to the other",
            "category": "Geometry",
            "order_in_curriculum": 11,
            "difficulty_level": 3,
            "lesson_content": """
            <h2>Congruence</h2>
            <p>Two figures are congruent if one can be mapped to the other using a sequence of rigid transformations.</p>
            <p>Corresponding sides and angles are equal in congruent figures.</p>
            """,
            "examples": json.dumps([
                {"question": "Which transformations show congruence?", "answer": "Rigid transformations"}
            ]),
            "prerequisites": "rigid_transformations"
        },
        {
            "slug": "dilations_similarity",
            "name": "Dilations and Similarity",
            "description": "Dilations scale figures; similarity uses dilations and rigid motions",
            "category": "Geometry",
            "order_in_curriculum": 12,
            "difficulty_level": 3,
            "lesson_content": """
            <h2>Dilations and Similarity</h2>
            <p>Dilation with scale factor k sends (x, y) to (kx, ky). Similar figures have equal corresponding angles and proportional side lengths.</p>
            """,
            "examples": json.dumps([
                {"question": "Dilate (2, −3) by k=2", "answer": "(4, −6)"}
            ]),
            "prerequisites": "transformations"
        },
        {
            "slug": "tessellations",
            "name": "Tessellations",
            "description": "Covering the plane with repeated shapes without gaps or overlaps",
            "category": "Geometry",
            "order_in_curriculum": 13,
            "difficulty_level": 2,
            "lesson_content": """
            <h2>Tessellations</h2>
            <p>Regular tessellations use a single regular polygon (equilateral triangles, squares, or regular hexagons).</p>
            <p>At each vertex, the angles around the point sum to 360°.</p>
            """,
            "examples": json.dumps([
                {"question": "Do regular pentagons tessellate the plane?", "answer": "No"}
            ]),
            "prerequisites": "rigid_transformations"
        },
        {
            "slug": "slope_and_linear_relationships",
            "name": "Slope and Linear Relationships",
            "description": "Slope as rate of change, proportional relationships, and linear equations",
            "category": "Algebra",
            "order_in_curriculum": 14,
            "difficulty_level": 3,
            "lesson_content": """
            <h2>Slope and Linear Relationships</h2>
            <p>Slope m = (change in y)/(change in x). Linear equations: y = mx + b. Proportional when b=0.</p>
            """,
            "examples": json.dumps([
                {"question": "Slope between (1,2) and (3,6)", "answer": "2"},
                {"question": "Is y=3x proportional?", "answer": "Yes"}
            ]),
            "prerequisites": "linear_equations"
        }
    ]

    for c in concepts:
        if not Concept.query.filter_by(slug=c["slug"]).first():
            db.session.add(Concept(**c))
    db.session.commit()

    # Minimal practice problems for each
    mapping = {
        "rigid_transformations": [
            {"question": "Reflect (−4, 2) across x-axis", "answer": "(−4, −2)", "difficulty": 2, "points": 10},
            {"question": "Rotate (0, 3) 180°", "answer": "(0, −3)", "difficulty": 2, "points": 10}
        ],
        "congruence": [
            {"question": "Rigid motion preserves side lengths (True/False)", "answer": "True", "difficulty": 1, "points": 10}
        ],
        "dilations_similarity": [
            {"question": "Dilate (−2, 5) by k=0.5", "answer": "(−1.0, 2.5)", "difficulty": 2, "points": 10}
        ],
        "tessellations": [
            {"question": "Squares tessellate the plane (True/False)", "answer": "True", "difficulty": 1, "points": 10}
        ],
        "slope_and_linear_relationships": [
            {"question": "Slope between (2,1) and (5,7)", "answer": "2", "difficulty": 2, "points": 10},
            {"question": "Is y=2x+3 proportional? (Yes/No)", "answer": "No", "difficulty": 1, "points": 10}
        ]
    }

    for slug, plist in mapping.items():
        concept = Concept.query.filter_by(slug=slug).first()
        if not concept:
            continue
        from models.practice import PracticeProblem
        if PracticeProblem.query.filter_by(concept_id=concept.id).count() > 0:
            continue
        for p in plist:
            db.session.add(PracticeProblem(
                concept_id=concept.id,
                question=p["question"],
                problem_type="fill_blank",
                correct_answer=p["answer"],
                explanation=None,
                difficulty=p["difficulty"],
                points=p["points"]
            ))
    db.session.commit()

def main():
    """Main seeding function"""
    app = create_app()
    
    with app.app_context():
        print("Starting database seeding...")
        
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Seed data
        seed_concepts()
        seed_practice_problems()
        seed_transformations()
        seed_additional_8th_grade_concepts()
        
        print("Database seeding completed successfully!")

if __name__ == "__main__":
    main()
