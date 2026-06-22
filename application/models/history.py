import time

# In-memory history storage
_history = []
MAX_HISTORY = 50

def add_history_entry(entry):
    """Add a new entry to history"""
    entry['timestamp'] = time.time()  # FIX: Add timestamp
    entry['id'] = len(_history) + 1
    _history.insert(0, entry)
    
    # Keep only last MAX_HISTORY entries
    if len(_history) > MAX_HISTORY:
        _history.pop()
    
    return entry

def get_history(limit=None):
    """Get history entries, optionally limited"""
    if limit:
        return _history[:limit]
    return _history

def clear_history():
    """Clear all history"""
    _history.clear()

def get_history_by_type(calc_type):
    """Get history entries filtered by type"""
    return [h for h in _history if h.get('type') == calc_type]