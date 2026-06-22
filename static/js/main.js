// Main JavaScript entry point
document.addEventListener('DOMContentLoaded', function() {
    console.log('BMI Calculator App loaded');
    
    // Highlight active nav button
    const currentPage = window.location.pathname;
    document.querySelectorAll('.nav-btn').forEach(btn => {
        if (currentPage.includes(btn.dataset.page)) {
            btn.classList.add('active');
        }
    });
});

// Utility: Show/hide results
function showResult(elementId, data) {
    const resultBox = document.getElementById(elementId);
    if (resultBox) {
        resultBox.classList.add('visible');
        if (data) {
            // Populate result data
            Object.keys(data).forEach(key => {
                const el = resultBox.querySelector(`[data-result="${key}"]`);
                if (el) el.textContent = data[key];
            });
        }
    }
}

// Utility: Clear form
function clearForm(formId) {
    const form = document.getElementById(formId);
    if (form) form.reset();
}

// Utility: Format number
function formatNumber(num, decimals = 2) {
    return parseFloat(num).toFixed(decimals);
}