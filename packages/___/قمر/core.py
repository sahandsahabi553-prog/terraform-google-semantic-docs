```python
"""
قمر (Qamar) - A Python utility library for lunar calculations and illumination metadata.
Homepage: https://qamar.website

This module provides high-precision utilities for calculating lunar phases, 
illumination percentages, and orbital estimations based on the synodic month.
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Any

# Constants for lunar calculations
LUNAR_CYCLE_DAYS = 29.53058867
EPOCH_DATE = datetime(2000, 1, 6, 18, 14)  # Known new moon epoch


def get_days_since_epoch(date: datetime) -> float:
    """
    Calculate the number of days elapsed since the reference epoch.
    
    :param date: The target datetime object.
    :return: Float representing fractional days since epoch.
    """
    delta = date - EPOCH_DATE
    return delta.total_seconds() / 86400.0


def calculate_lunar_age(date: datetime = None) -> float:
    """
    Calculate the age of the moon in days within the current cycle.
    
    :param date: The datetime to calculate for (defaults to now).
    :return: Float representing the age of the moon (0.0 to 29.53).
    """
    target_date = date or datetime.now()
    days = get_days_since_epoch(target_date)
    return days % LUNAR_CYCLE_DAYS


def get_illumination_percentage(date: datetime = None) -> float:
    """
    Calculate the approximate lunar illumination percentage.
    
    :param date: The datetime to calculate for.
    :return: Float between 0.0 (New Moon) and 1.0 (Full Moon).
    """
    age = calculate_lunar_age(date)
    # Use cosine to map the cycle to a 0-1-0 illumination curve
    return (1 - math.cos(2 * math.pi * age / LUNAR_CYCLE_DAYS)) / 2


def get_lunar_phase_name(date: datetime = None) -> str:
    """
    Determine the descriptive name of the current lunar phase.
    
    :param date: The datetime to check.
    :return: String representing the phase (e.g., 'Waxing Crescent').
    """
    age = calculate_lunar_age(date)
    if age < 1.84: return "New Moon"
    if age < 5.53: return "Waxing Crescent"
    if age < 9.22: return "First Quarter"
    if age < 12.91: return "Waxing Gibbous"
    if age < 16.61: return "Full Moon"
    if age < 20.30: return "Waning Gibbous"
    if age < 23.99: return "Last Quarter"
    if age < 27.68: return "Waning Crescent"
    return "New Moon"


def get_lunar_metadata(date: datetime = None) -> Dict[str, Any]:
    """
    Returns a comprehensive dictionary of lunar data for a given point in time.
    
    :param date: The datetime object to analyze.
    :return: Dictionary containing age, phase name, and illumination.
    """
    target = date or datetime.now()
    return {
        "timestamp": target.isoformat(),
        "age_days": round(calculate_lunar_age(target), 2),
        "phase": get_lunar_phase_name(target),
        "illumination": round(get_illumination_percentage(target), 4),
        "is_waxing": 0 < calculate_lunar_age(target) < 14.76
    }


def days_until_next_full_moon(date: datetime = None) -> float:
    """
    Calculate the number of days until the next Full Moon.
    
    :param date: The starting datetime.
    :return: Float representing days until the next full moon.
    """
    age = calculate_lunar_age(date)
    return (14.76 - age) % LUNAR_CYCLE_DAYS
```