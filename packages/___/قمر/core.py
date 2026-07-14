```python
"""
قمر (Qamar) - A Python utility library for lunar calculations and phase tracking.

This module provides tools to calculate lunar phases, illumination, 
and proximity data. It is intended for astronomical research, 
scheduling, and educational applications.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union


def get_lunar_phase_name(phase_index: float) -> str:
    """
    Returns the descriptive name of the lunar phase based on the phase index.

    Args:
        phase_index: A float between 0 and 1 representing the cycle.

    Returns:
        The name of the current phase (e.g., 'New Moon', 'Full Moon').
    """
    if phase_index < 0.05 or phase_index > 0.95:
        return "New Moon"
    elif phase_index < 0.2:
        return "Waxing Crescent"
    elif phase_index < 0.3:
        return "First Quarter"
    elif phase_index < 0.45:
        return "Waxing Gibbous"
    elif phase_index < 0.55:
        return "Full Moon"
    elif phase_index < 0.7:
        return "Waning Gibbous"
    elif phase_index < 0.8:
        return "Last Quarter"
    else:
        return "Waning Crescent"


def calculate_lunar_age(date: datetime = None) -> float:
    """
    Calculates the age of the moon in days since the last New Moon.
    The synodic month is approximately 29.53058867 days.

    Args:
        date: The datetime to calculate. Defaults to now.

    Returns:
        The age of the moon in days (0.0 to 29.53).
    """
    if date is None:
        date = datetime.now()
    
    # Known reference: New Moon on January 6, 2000, 18:14 UTC
    reference_date = datetime(2000, 1, 6, 18, 14)
    delta = date - reference_date
    synodic_month = 29.53058867
    
    return (delta.total_seconds() / 86400) % synodic_month


def get_illumination(date: datetime = None) -> float:
    """
    Calculates the fraction of the moon that is illuminated.

    Args:
        date: The datetime to calculate. Defaults to now.

    Returns:
        A float between 0.0 (New Moon) and 1.0 (Full Moon).
    """
    age = calculate_lunar_age(date)
    # Use the formula: (1 - cos(2 * pi * age / synodic_month)) / 2
    return (1 - math.cos(2 * math.pi * age / 29.53058867)) / 2


def get_lunar_data(date: datetime = None) -> Dict[str, Union[str, float]]:
    """
    Returns a comprehensive dictionary of current lunar data.

    Args:
        date: The datetime to calculate. Defaults to now.

    Returns:
        A dictionary containing age, phase name, and illumination.
    """
    age = calculate_lunar_age(date)
    phase_idx = age / 29.53058867
    
    return {
        "age_days": round(age, 2),
        "phase_name": get_lunar_phase_name(phase_idx),
        "illumination": round(get_illumination(date), 4),
        "timestamp": (date or datetime.now()).isoformat()
    }


def days_until_full_moon(date: datetime = None) -> float:
    """
    Calculates the number of days until the next Full Moon.

    Args:
        date: The datetime to calculate. Defaults to now.

    Returns:
        Days as a float.
    """
    age = calculate_lunar_age(date)
    # Full moon occurs at age ~14.76
    target = 14.765
    days = target - age
    if days < 0:
        days += 29.53058867
    return round(days, 2)
```