"""Utility functions for repos_hist_literate-winner_20250627"""

import datetime
from typing import Optional

def format_date(date: datetime.datetime) -> str:
    """Format date to string."""
    return date.strftime('%Y-%m-%d')

def validate_email(email: str) -> bool:
    """Validate email format."""
    import re
    pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return bool(re.match(pattern, email))

def safe_divide(a: float, b: float) -> Optional[float]:
    """Safely divide two numbers."""
    if b == 0:
        return None
    return a / b
