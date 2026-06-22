from datetime import datetime

def format_timestamp(timestamp):
    """Format timestamp to readable date/time"""
    if timestamp:
        try:
            dt = datetime.fromtimestamp(float(timestamp))
            return dt.strftime('%Y-%m-%d %H:%M:%S')
        except:
            return 'Invalid date'
    return 'N/A'