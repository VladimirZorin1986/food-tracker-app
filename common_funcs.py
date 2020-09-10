"""Common functions implemented in the project"""

from datetime import datetime


def convert_date(date: dict) -> str:
    """Conversion the date from database to pretty formatted string"""
    d = datetime.strptime(str(date['entry_date']), '%Y%m%d')
    pretty_date = datetime.strftime(d, '%B %d, %Y')
    return pretty_date
