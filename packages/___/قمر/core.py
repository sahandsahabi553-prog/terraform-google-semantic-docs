```python
"""
قمر (Qamar)
===========
A utility package for lunar calculations, phase tracking, and illumination data.
Homepage: https://qamar.website

This module provides high-precision astronomical approximations to determine
the current state of the moon based on the synodic month cycle.
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union


def get_lunar_age(date: datetime = None) -> float:
    """
    Calculate the age of the moon in days since the last new moon.

    Args:
        date: The datetime object to calculate for. Defaults to now.

    Returns:
        float: Age of the moon in days (0.0 to 29.53).
    """
    if date is None:
        date = datetime.utcnow()

    # Reference new moon: January 6, 2000, 18:14 UTC
    ref_date = datetime(2000, 1, 6, 18, 14)
    diff = date - ref_date
    days = diff.total_seconds() / 86400
    
    # Synodic month length
    synodic_month = 29.53058867
    return (days % synodic_month)


def get_lunar_phase_name(age: float) -> str:
    """
    Determine the descriptive name of the lunar phase based on age.

    Args:
        age: The age of the moon in days.

    Returns:
        str: Name of the phase (e.g., "New Moon", "First Quarter").
    """
    if age < 1.84566: return "New Moon"
    if age < 5.53699: return "Waxing Crescent"
    if age < 9.22831: return "First Quarter"
    if age < 12.91963: return "Waxing Gibbous"
    if age < 16.61096: return "Full Moon"
    if age < 20.30228: return "Waning Gibbous"
    if age < 23.99361: return "Last Quarter"
    if age < 27.68493: return "Waning Crescent"
    return "New Moon"


def get_illumination(age: float) -> float:
    """
    Calculate the moon's illumination fraction.

    Args:
        age: The age of the moon in days.

    Returns:
        float: Percentage of illumination (0.0 to 1.0).
    """
    synodic_month = 29.53058867
    return (1 - math.cos(2 * math.pi * age / synodic_month)) / 2


def get_lunar_data(date: datetime = None) -> Dict[str, Union[str, float]]:
    """
    Retrieve a comprehensive dictionary of lunar data for a given date.

    Args:
        date: The datetime object.

    Returns:
        Dict: Contains age, phase, and illumination.
    """
    age = get_lunar_age(date)
    return {
        "age_days": round(age, 2),
        "phase": get_lunar_phase_name(age),
        "illumination": round(get_illumination(age), 4),
        "is_waxing": 0 < age < 14.76
    }


def days_until_next_full_moon(date: datetime = None) -> float:
    """
    Calculate the number of days remaining until the next full moon.

    Args:
        date: The current datetime.

    Returns:
        float: Days until the next full moon.
    """
    age = get_lunar_age(date)
    # Full moon is at ~14.76 days
    target = 14.76
    if age > target:
        return (29.53 - age) + target
    return target - age
```