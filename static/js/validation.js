// Client-side validation

function validateNumber(value, fieldName, min = null, max = null) {
    const num = parseFloat(value);
    if (isNaN(num)) {
        return { valid: false, message: `${fieldName} must be a valid number` };
    }
    if (min !== null && num < min) {
        return { valid: false, message: `${fieldName} must be at least ${min}` };
    }
    if (max !== null && num > max) {
        return { valid: false, message: `${fieldName} must be at most ${max}` };
    }
    return { valid: true };
}

// Real-time validation for BMI inputs
document.addEventListener('DOMContentLoaded', function() {
    const weightInput = document.getElementById('bmiWeight');
    const heightInput = document.getElementById('bmiHeight');
    
    if (weightInput) {
        weightInput.addEventListener('input', function() {
            const result = validateNumber(this.value, 'Weight', 1, 500);
            if (!result.valid) {
                this.style.borderColor = '#ff6b6b';
                this.title = result.message;
            } else {
                this.style.borderColor = '#6bcf7f';
                this.title = '';
            }
        });
    }
    
    if (heightInput) {
        heightInput.addEventListener('input', function() {
            const result = validateNumber(this.value, 'Height', 50, 300);
            if (!result.valid) {
                this.style.borderColor = '#ff6b6b';
                this.title = result.message;
            } else {
                this.style.borderColor = '#6bcf7f';
                this.title = '';
            }
        });
    }
});

// Form submission validation
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return true;
    
    const inputs = form.querySelectorAll('input[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            input.style.borderColor = '#ff6b6b';
            isValid = false;
        }
    });
    
    return isValid;
}