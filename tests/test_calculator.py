import pytest
from application.services.calculator import (
    basic_calculate,
    calculate_bmi,
    get_bmi_category,
    convert_units
)

def test_basic_calculate():
    assert basic_calculate(2, 3, '+') == 5
    assert basic_calculate(10, 5, '-') == 5
    assert basic_calculate(4, 3, '*') == 12
    assert basic_calculate(15, 3, '/') == 5
    assert basic_calculate(2, 3, '^') == 8
    assert basic_calculate(10, 3, '%') == 1

def test_basic_calculate_division_by_zero():
    with pytest.raises(ValueError):
        basic_calculate(5, 0, '/')

def test_calculate_bmi():
    assert round(calculate_bmi(70, 175), 2) == 22.86
    assert round(calculate_bmi(50, 160), 2) == 19.53

def test_get_bmi_category():
    assert get_bmi_category(15.5) == 'Severe Underweight'
    assert get_bmi_category(17.0) == 'Underweight'
    assert get_bmi_category(22.0) == 'Normal Weight'
    assert get_bmi_category(27.0) == 'Overweight'
    assert get_bmi_category(32.0) == 'Obese Class I'
    assert get_bmi_category(37.0) == 'Obese Class II'
    assert get_bmi_category(42.0) == 'Obese Class III'

def test_convert_units():
    # Length
    assert convert_units(1, 'm', 'cm', 'length') == 100
    assert convert_units(1, 'km', 'm', 'length') == 1000
    assert convert_units(12, 'in', 'cm', 'length') == 30.48
    
    # Weight
    assert convert_units(1, 'kg', 'g', 'weight') == 1000
    assert convert_units(1, 'lb', 'oz', 'weight') == 16
    
    # Temperature
    assert convert_units(0, 'C', 'F', 'temperature') == 32
    assert convert_units(100, 'C', 'K', 'temperature') == 373.15
    assert convert_units(32, 'F', 'C', 'temperature') == 0