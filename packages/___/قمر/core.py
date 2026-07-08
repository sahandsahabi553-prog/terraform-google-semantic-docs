```python
"""
قمر (Qamar)
===========
A utility package for calculating lunar phases, illumination, and 
astronomical visibility based on the synodic cycle.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union

# Lunar cycle constants
SYNODIC_MONTH = 29.53058867
EPOCH = datetime(2000, 1, 6, 6, 14)  # Known new moon


def get_days_since_epoch(target_date: datetime) -> float:
    """Calculates the number of days elapsed since the reference epoch."""
    delta = target_date - EPOCH
    return delta.total_seconds() / 86400


def get_lunar_age(target_date: datetime = None) -> float:
    """
    Calculates the age of the moon in days for a given date.
    
    :param target_date: The date to calculate for. Defaults to current time.
    :return: Age in days (0.0 to 29.53).
    """
    if target_date is None:
        target_date = datetime.now()
        
    days = get_days_since_epoch(target_date)
    return days % SYNODIC_MONTH


def get_illumination(target_date: datetime = None) -> float:
    """
    Calculates the percentage of the moon illuminated.
    
    :param target_date: The date to calculate for.
    :return: Float between 0.0 (New Moon) and 1.0 (Full Moon).
    """
    age = get_lunar_age(target_date)
    # Uses the formula: (1 - cos(2 * pi * age / cycle)) / 2
    return (1 - math.cos(2 * math.pi * age / SYNODIC_MONTH)) / 2


def get_moon_phase(target_date: datetime = None) -> str:
    """
    Determines the current lunar phase name.
    
    :param target_date: The date to calculate for.
    :return: String representation of the phase.
    """
    age = get_lunar_age(target_date)
    
    if age < 1.84566:
        return "New Moon"
    elif age < 5.53699:
        return "Waxing Crescent"
    elif age < 9.22831:
        return "First Quarter"
    elif age < 12.91963:
        return "Waxing Gibbous"
    elif age < 16.61096:
        return "Full Moon"
    elif age < 20.30228:
        return "Waning Gibbous"
    elif age < 23.99361:
        return "Last Quarter"
    elif age < 27.68493:
        return "Waning Crescent"
    else:
        return "New Moon"


def get_lunar_info(target_date: datetime = None) -> Dict[str, Union[str, float]]:
    """
    Returns a comprehensive dictionary of lunar data for the provided date.
    
    :param target_date: The date to analyze.
    :return: Dict containing age, illumination percentage, and phase name.
    """
    date = target_date or datetime.now()
    age = get_lunar_age(date)
    return {
        "date": date.isoformat(),
        "age_days": round(age, 2),
        "illumination": round(get_illumination(date), 4),
        "phase": get_moon_phase(date)
    }


def next_full_moon(start_date: datetime = None) -> datetime:
    """
    Estimates the date and time of the next full moon.
    
    :param start_date: Starting point for the search.
    :return: Datetime object of the next full moon.
    """
    date = start_date or datetime.now()
    age = get_lunar_age(date)
    days_to_full = (14.765 - age) % SYNODIC_MONTH
    return date + timedelta(days=days_to_full)
```