from flask import Blueprint, render_template
from application.models.history import get_history

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Homepage with all calculators"""
    return render_template('index.html')

@main_bp.route('/calculator/basic')
def basic_calculator():
    """Basic arithmetic calculator"""
    return render_template('calculator/basic.html')

@main_bp.route('/calculator/bmi')
def bmi_calculator():
    """BMI calculator with history"""
    history = get_history()
    return render_template('calculator/bmi.html', history=history)

@main_bp.route('/calculator/converter')
def unit_converter():
    """Unit converter"""
    return render_template('calculator/converter.html')

@main_bp.route('/history')
def history_page():
    """Full history page"""
    history = get_history()
    return render_template('history.html', history=history)

@main_bp.route('/about')
def about():
    """About page"""
    return render_template('about.html')