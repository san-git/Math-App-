# Math Quest - 8th Grade Math Game

A comprehensive, interactive math learning platform designed specifically for 8th-grade students. Built with Python Flask, this web application provides a gamified learning experience covering the entire 8th-grade mathematics curriculum.

## 🎯 Features

- **Complete Curriculum Coverage**: All 8th-grade math concepts from number systems to probability
- **Interactive Lessons**: Step-by-step explanations with examples and visual aids
- **Practice Problems**: Multiple choice and fill-in-the-blank questions with instant feedback
- **Progress Tracking**: Monitor learning progress with detailed analytics and achievements
- **Gamified Learning**: Earn points, unlock achievements, and track completion
- **Responsive Design**: Modern, mobile-friendly interface
- **Scalable Architecture**: Modular design for easy expansion and maintenance

## 📚 Curriculum Topics

1. **Number Systems** - Rational and irrational numbers, real numbers
2. **Exponents and Powers** - Exponent rules, scientific notation
3. **Linear Equations** - One-variable equations and inequalities
4. **Functions** - Function notation, domain, range, linear functions
5. **Geometry Basics** - Angles, triangles, quadrilaterals
6. **Pythagorean Theorem** - Right triangles and applications
7. **Data Analysis** - Measures of central tendency, variability
8. **Probability** - Basic probability concepts and calculations

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd math
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Initialize the database**
   ```bash
   python seed_data.py
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open your browser**
   Navigate to `http://localhost:5000`

## 🏗️ Architecture

### Project Structure
```
math/
├── app.py                 # Main application entry point
├── requirements.txt       # Python dependencies
├── seed_data.py          # Database seeding script
├── models/               # Database models
│   ├── __init__.py
│   ├── user.py          # User authentication and progress
│   ├── concept.py       # Math concepts and lessons
│   ├── progress.py      # User progress tracking
│   └── practice.py      # Practice problems and attempts
├── routes/               # Application routes
│   ├── __init__.py
│   ├── main.py          # Main pages (home, dashboard)
│   ├── auth.py          # Authentication (login/register)
│   ├── concepts.py      # Concept lessons and content
│   ├── practice.py      # Practice problems and quizzes
│   └── progress.py      # Progress tracking and analytics
└── templates/            # HTML templates
    ├── base.html         # Base template with navigation
    ├── index.html        # Home page
    ├── dashboard.html    # User dashboard
    └── auth/            # Authentication templates
        ├── login.html
        └── register.html
```

### Key Components

- **Flask Application**: Web framework with blueprint architecture
- **SQLAlchemy**: Database ORM for data management
- **Flask-Login**: User authentication and session management
- **Bootstrap 5**: Modern, responsive UI framework
- **Modular Design**: Blueprint-based routing for scalability

## 🎮 Usage

### For Students

1. **Create an Account**: Register with username, email, and password
2. **Start Learning**: Begin with the first concept (Number Systems)
3. **Follow the Path**: Complete concepts in order to unlock new ones
4. **Practice Regularly**: Use practice problems to reinforce learning
5. **Track Progress**: Monitor your advancement and earn achievements

### For Teachers/Parents

- Monitor student progress through the dashboard
- Review completed concepts and practice scores
- Identify areas needing additional focus
- Encourage regular practice and concept completion

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///math_game.db
FLASK_ENV=development
```

### Database

The application uses SQLite by default for development. For production, consider using PostgreSQL or MySQL by updating the `DATABASE_URL`.

## 📊 Database Schema

### Core Tables

- **users**: User accounts and authentication
- **concepts**: Math concepts and lesson content
- **progress_records**: User progress through concepts
- **practice_problems**: Practice questions and answers
- **practice_attempts**: User attempts at practice problems

### Relationships

- Users have many progress records and practice attempts
- Concepts have many practice problems
- Progress records link users to concepts
- Practice attempts link users to practice problems

## 🚀 Deployment

### Production Setup

1. **Use a production WSGI server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 app:create_app()
   ```

2. **Set production environment variables**
   ```env
   FLASK_ENV=production
   SECRET_KEY=strong-production-secret-key
   DATABASE_URL=postgresql://user:pass@localhost/mathgame
   ```

3. **Configure reverse proxy (nginx)**
4. **Set up SSL certificates**
5. **Configure database backups**

### Docker Deployment

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:create_app()"]
```

## 🔒 Security Features

- Password hashing with Werkzeug
- CSRF protection with Flask-WTF
- Secure session management
- Input validation and sanitization
- SQL injection prevention through ORM

## 📱 Responsive Design

- Mobile-first approach
- Bootstrap 5 grid system
- Touch-friendly interface
- Optimized for all screen sizes

## 🧪 Testing

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-flask

# Run tests
pytest

# Run with coverage
pytest --cov=app
```

### Test Structure

- Unit tests for models and utilities
- Integration tests for routes
- End-to-end tests for user workflows

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include type hints where appropriate
- Write comprehensive tests
- Update documentation as needed

## 📈 Future Enhancements

- **Advanced Analytics**: Detailed learning analytics and insights
- **Adaptive Learning**: AI-powered problem difficulty adjustment
- **Multi-language Support**: Internationalization for global users
- **Mobile App**: Native mobile applications
- **Social Features**: Student collaboration and competitions
- **Teacher Dashboard**: Advanced classroom management tools
- **Content Management**: Easy lesson and problem creation
- **Integration**: LMS and educational platform integration

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Flask community for the excellent web framework
- Bootstrap team for the responsive UI components
- Educational researchers for learning methodology insights
- 8th-grade math teachers for curriculum guidance

## 📞 Support

For questions, issues, or contributions:

- Create an issue on GitHub
- Contact the development team
- Check the documentation wiki

---

**Happy Learning! 🎓✨**
