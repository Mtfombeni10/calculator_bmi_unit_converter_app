def validate_basic_calc(num1, num2, operation):
    """Validate basic calculator inputs"""
    try:
        num1 = float(num1)
        num2 = float(num2)
    except (ValueError, TypeError):
        return False, "Please enter valid numbers"
    
    if operation == '/' and num2 == 0:
        return False, "Division by zero is not allowed"
    
    if operation not in ['+', '-', '*', '/', '^', '%']:
        return False, "Invalid operation"
    
    return True, None

def validate_bmi_input(weight, height):
    """Validate BMI inputs"""
    try:
        weight = float(weight)
        height = float(height)
    except (ValueError, TypeError):
        return False, "Please enter valid numbers"
    
    if weight <= 0:
        return False, "Weight must be greater than 0"
    
    if height <= 0:
        return False, "Height must be greater than 0"
    
    if weight > 500:
        return False, "Weight seems too high (max 500 kg)"
    
    if height > 300:
        return False, "Height seems too high (max 300 cm)"
    
    return True, None

def validate_conversion(value, from_unit, to_unit, category):
    """Validate conversion inputs"""
    try:
        value = float(value)
    except (ValueError, TypeError):
        return False, "Please enter a valid number"
    
    if not from_unit or not to_unit:
        return False, "Please select units"
    
    if from_unit == to_unit:
        return False, "Source and target units must be different"
    
    valid_categories = ['length', 'weight', 'temperature']
    if category not in valid_categories:
        return False, "Invalid conversion category"
    
    return True, None