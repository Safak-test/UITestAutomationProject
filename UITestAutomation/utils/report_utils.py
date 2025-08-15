import os
import datetime
from pathlib import Path

def get_timestamp():
    """Get current timestamp in a readable format"""
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def get_date_folder():
    """Get date folder name in YYYY-MM-DD format"""
    return datetime.datetime.now().strftime("%Y-%m-%d")

def create_dated_report_path(base_path="reports"):
    """Create a dated report path"""
    date_folder = get_date_folder()
    timestamp = get_timestamp()
    
    # Create path like: reports/2024-08-14/134523/
    report_path = os.path.join(base_path, date_folder, timestamp)
    
    # Create directories if they don't exist
    os.makedirs(report_path, exist_ok=True)
    
    return report_path

def get_report_metadata():
    """Get metadata for reports"""
    return {
        "timestamp": get_timestamp(),
        "date": get_date_folder(),
        "datetime": datetime.datetime.now().isoformat(),
        "environment": os.getenv("TEST_ENV", "local"),
        "browser": os.getenv("BROWSER", "chrome")
    } 