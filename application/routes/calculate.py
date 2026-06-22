from flask import Blueprint, request, jsonify
from application.services.calculator import (
    basic_calculate,
    calculate_bmi,
    get_bmi_category,
    convert_units
)
from application.services.validation import (
    validate_basic_calc,
    validate_bmi_input,
    validate_conversion
)
from application.models.history import add_history_entry
from application.utils.formatters import format_number

calculate_bp = Blueprint('calculate', __name__)

@calculate_bp.route('/basic', methods=['POST'])
def basic_math():
    """Handle basic arithmetic operations"""
    try:
        data = request.get_json()
        num1 = data.get('num1')
        num2 = data.get('num2')
        operation = data.get('operation')
        
        # Validate input
        is_valid, error = validate_basic_calc(num1, num2, operation)
        if not is_valid:
            return jsonify({'success': False, 'error': error}), 400
        
        # Calculate
        result = basic_calculate(float(num1), float(num2), operation)
        
        # Add to history
        entry = {
            'type': 'basic',
            'expression': f"{num1} {operation} {num2}",
            'result': format_number(result)
        }
        add_history_entry(entry)
        
        return jsonify({
            'success': True,
            'result': format_number(result),
            'expression': entry['expression']
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@calculate_bp.route('/bmi', methods=['POST'])
def bmi():
    """Calculate BMI"""
    try:
        data = request.get_json()
        weight = data.get('weight')
        height = data.get('height')
        
        # Validate
        is_valid, error = validate_bmi_input(weight, height)
        if not is_valid:
            return jsonify({'success': False, 'error': error}), 400
        
        # Calculate
        bmi = calculate_bmi(float(weight), float(height))
        category = get_bmi_category(bmi)
        
        # Add to history
        entry = {
            'type': 'bmi',
            'weight': float(weight),
            'height': float(height),
            'bmi': format_number(bmi),
            'category': category
        }
        add_history_entry(entry)
        
        return jsonify({
            'success': True,
            'bmi': format_number(bmi),
            'category': category
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@calculate_bp.route('/convert', methods=['POST'])
def convert():
    """Handle unit conversion"""
    try:
        data = request.get_json()
        value = data.get('value')
        from_unit = data.get('from_unit')
        to_unit = data.get('to_unit')
        category = data.get('category')
        
        # Validate
        is_valid, error = validate_conversion(value, from_unit, to_unit, category)
        if not is_valid:
            return jsonify({'success': False, 'error': error}), 400
        
        # Convert
        result = convert_units(float(value), from_unit, to_unit, category)
        
        # Add to history
        entry = {
            'type': 'conversion',
            'category': category,
            'from_value': float(value),
            'from_unit': from_unit,
            'to_unit': to_unit,
            'result': format_number(result)
        }
        add_history_entry(entry)
        
        return jsonify({
            'success': True,
            'result': format_number(result),
            'from_value': float(value),
            'from_unit': from_unit,
            'to_unit': to_unit
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@calculate_bp.route('/history/clear', methods=['POST'])
def clear_history():
    """Clear all history"""
    from application.models.history import clear_history
    clear_history()
    return jsonify({'success': True})