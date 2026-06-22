// History management

document.addEventListener('DOMContentLoaded', function() {
    const clearBtn = document.getElementById('clearHistory');
    if (clearBtn) {
        clearBtn.addEventListener('click', async function() {
            if (confirm('Are you sure you want to clear all history?')) {
                try {
                    const response = await fetch('/api/history/clear', {
                        method: 'POST'
                    });
                    
                    const result = await response.json();
                    if (result.success) {
                        const historyList = document.getElementById('historyList');
                        if (historyList) {
                            historyList.innerHTML = '<p class="history-empty">No calculations yet</p>';
                        }
                    }
                } catch (error) {
                    alert('Error clearing history: ' + error.message);
                }
            }
        });
    }
});

// Filter history by type
function filterHistory(type) {
    const items = document.querySelectorAll('.history-item');
    items.forEach(item => {
        if (type === 'all' || item.dataset.type === type) {
            item.style.display = 'flex';
        } else {
            item.style.display = 'none';
        }
    });
}

// Export history as CSV
function exportHistoryCSV() {
    const items = document.querySelectorAll('.history-item');
    if (items.length === 0) {
        alert('No history to export');
        return;
    }
    
    let csv = 'Type,Details,Result,Category,Time\n';
    items.forEach(item => {
        const details = item.querySelector('.history-details')?.textContent || '';
        const result = item.querySelector('.history-result')?.textContent || '';
        const category = item.querySelector('.history-category')?.textContent || '';
        const type = item.dataset.type || '';
        const time = item.querySelector('.history-time')?.textContent || '';
        csv += `${type},"${details}","${result}","${category}","${time}"\n`;
    });
    
    // Download CSV
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'calculator_history.csv';
    a.click();
    window.URL.revokeObjectURL(url);
}