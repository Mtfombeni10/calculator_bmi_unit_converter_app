def format_number(num, decimals=2):
    """Format a number with specified decimal places"""
    if isinstance(num, str):
        try:
            num = float(num)
        except ValueError:
            return num
    
    if num is None:
        return 'N/A'
    
    # Handle very large numbers
    if abs(num) > 1e15:
        return f"{num:.2e}"
    
    # Round to specified decimals
    rounded = round(num, decimals)
    
    # Remove trailing zeros if it's a whole number
    if rounded == int(rounded):
        return str(int(rounded))
    
    return f"{rounded:.{decimals}f}"

def format_timestamp(timestamp):
    """Format timestamp to readable date/time"""
    from datetime import datetime
    if timestamp:
        try:
            dt = datetime.fromtimestamp(float(timestamp))
            return dt.strftime('%Y-%m-%d %H:%M:%S')
        except:
            return 'Invalid date'
    return 'N/A'

def get_unit_symbol(unit):
    """Get symbol for common units"""
    symbols = {
        'mm': 'mm', 'cm': 'cm', 'm': 'm', 'km': 'km',
        'in': 'in', 'ft': 'ft', 'yd': 'yd', 'mi': 'mi',
        'mg': 'mg', 'g': 'g', 'kg': 'kg', 'oz': 'oz', 'lb': 'lb',
        'C': '°C', 'F': '°F', 'K': 'K'
    }
    return symbols.get(unit, unit)