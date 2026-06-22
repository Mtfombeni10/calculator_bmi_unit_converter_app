// Frontend calculator logic

// Basic Calculator
document.addEventListener('DOMContentLoaded', function() {
    const basicForm = document.getElementById('basicForm');
    if (basicForm) {
        basicForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const num1 = document.getElementById('basicNum1').value;
            const num2 = document.getElementById('basicNum2').value;
            const operation = document.getElementById('basicOperation').value;
            
            try {
                const response = await fetch('/api/basic', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ num1, num2, operation })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    document.getElementById('basicResult').textContent = result.result;
                    document.getElementById('basicExpression').textContent = result.expression + ' =';
                    document.getElementById('basicResultBox').classList.add('visible');
                    
                    // Update history
                    updateHistory();
                } else {
                    alert(result.error);
                }
            } catch (error) {
                alert('Error: ' + error.message);
            }
        });
    }
});

// BMI Calculator
document.addEventListener('DOMContentLoaded', function() {
    const bmiForm = document.getElementById('bmiForm');
    if (bmiForm) {
        bmiForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const weight = document.getElementById('bmiWeight').value;
            const height = document.getElementById('bmiHeight').value;
            
            try {
                const response = await fetch('/api/bmi', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ weight, height })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    document.getElementById('bmiValue').textContent = result.bmi;
                    const categoryEl = document.getElementById('bmiCategory');
                    categoryEl.textContent = result.category;
                    
                    // Set category class
                    const categoryClass = result.category.toLowerCase().replace(/ /g, '-');
                    categoryEl.className = 'result-category category-' + 
                        (categoryClass.includes('normal') ? 'normal' :
                         categoryClass.includes('underweight') ? 'underweight' :
                         categoryClass.includes('overweight') ? 'overweight' : 'obese');
                    
                    document.getElementById('bmiResultBox').classList.add('visible');
                    
                    // Update history
                    updateHistory();
                } else {
                    alert(result.error);
                }
            } catch (error) {
                alert('Error: ' + error.message);
            }
        });
    }
});

// Unit Converter
document.addEventListener('DOMContentLoaded', function() {
    const converterForm = document.getElementById('converterForm');
    if (converterForm) {
        converterForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const value = document.getElementById('convertValue').value;
            const category = document.getElementById('convertCategory').value;
            const fromUnit = document.getElementById('convertFrom').value;
            const toUnit = document.getElementById('convertTo').value;
            
            try {
                const response = await fetch('/api/convert', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ value, category, from_unit: fromUnit, to_unit: toUnit })
                });
                
                const result = await response.json();
                
                if (result.success) {
                    document.getElementById('convertResult').textContent = result.result;
                    document.getElementById('convertFromLabel').textContent = result.from_value + ' ' + result.from_unit;
                    document.getElementById('convertToLabel').textContent = result.to_unit;
                    document.getElementById('convertResultBox').classList.add('visible');
                    
                    // Update history
                    updateHistory();
                } else {
                    alert(result.error);
                }
            } catch (error) {
                alert('Error: ' + error.message);
            }
        });
    }
    
    // Update unit options when category changes
    const categorySelect = document.getElementById('convertCategory');
    if (categorySelect) {
        categorySelect.addEventListener('change', function() {
            updateUnitOptions(this.value);
        });
    }
});

function updateUnitOptions(category) {
    const units = {
        length: ['mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi'],
        weight: ['mg', 'g', 'kg', 'oz', 'lb'],
        temperature: ['C', 'F', 'K']
    };
    
    const unitOptions = units[category] || [];
    const fromSelect = document.getElementById('convertFrom');
    const toSelect = document.getElementById('convertTo');
    
    [fromSelect, toSelect].forEach(select => {
        select.innerHTML = '';
        unitOptions.forEach(unit => {
            const option = document.createElement('option');
            option.value = unit;
            option.textContent = unit;
            select.appendChild(option);
        });
    });
}

// Update history display
async function updateHistory() {
    try {
        const response = await fetch('/history');
        const html = await response.text();
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const historyList = doc.querySelector('#historyList');
        
        const currentHistory = document.querySelector('#historyList');
        if (currentHistory && historyList) {
            currentHistory.innerHTML = historyList.innerHTML;
        }
    } catch (error) {
        console.error('Error updating history:', error);
    }
}