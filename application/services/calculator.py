import math

def basic_calculate(num1, num2, operation):
    """Perform basic arithmetic operations"""
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else float('inf'),
        '^': num1 ** num2,
        '%': num1 % num2
    }
    
    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}")
    
    result = operations[operation]
    if result == float('inf'):
        raise ValueError("Division by zero")
    
    return result

def calculate_bmi(weight, height):
    """Calculate BMI from weight (kg) and height (cm)"""
    height_m = height / 100  # Convert cm to meters
    if height_m <= 0:
        raise ValueError("Height must be greater than 0")
    return weight / (height_m * height_m)

def get_bmi_category(bmi):
    """Return BMI category based on WHO standards"""
    if bmi < 16.0:
        return 'Severe Underweight'
    elif bmi < 18.5:
        return 'Underweight'
    elif bmi < 25.0:
        return 'Normal Weight'
    elif bmi < 30.0:
        return 'Overweight'
    elif bmi < 35.0:
        return 'Obese Class I'
    elif bmi < 40.0:
        return 'Obese Class II'
    else:
        return 'Obese Class III'

def convert_units(value, from_unit, to_unit, category):
    """Convert between units"""
    # Length conversions (base: meters)
    length_units = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.34
    }
    
    # Weight conversions (base: grams)
    weight_units = {
        'mg': 0.001,
        'g': 1.0,
        'kg': 1000.0,
        'oz': 28.3495,
        'lb': 453.592
    }
    
    # Temperature conversions (special case)
    if category == 'temperature':
        return convert_temperature(value, from_unit, to_unit)
    
    # Select conversion map
    unit_map = length_units if category == 'length' else weight_units
    
    if from_unit not in unit_map or to_unit not in unit_map:
        raise ValueError(f"Unsupported units: {from_unit} to {to_unit}")
    
    # Convert to base unit, then to target
    base_value = value * unit_map[from_unit]
    result = base_value / unit_map[to_unit]
    
    return result

def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Celsius, Fahrenheit, Kelvin"""
    # Convert to Celsius first
    if from_unit == 'C':
        celsius = value
    elif from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    else:
        raise ValueError(f"Unsupported temperature unit: {from_unit}")
    
    # Convert from Celsius to target
    if to_unit == 'C':
        return celsius
    elif to_unit == 'F':
        return celsius * 9/5 + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:
        raise ValueError(f"Unsupported temperature unit: {to_unit}")