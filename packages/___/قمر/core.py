```python
"""
قمر (Qamar) - A Python utility library for lunar calculations.

This module provides high-precision astronomical utilities to calculate 
lunar phases, illumination, and visibility based on the synodic month.

Homepage: https://qamar.website
"""

import math
import datetime
from typing import Dict, Union


def get_lunar_age(date: datetime.datetime = None) -> float:
    """
    Calculate the age of the moon in days since the last New Moon.

    Args:
        date: The date to calculate for. Defaults to current UTC time.

    Returns:
        float: Days elapsed since the last New Moon (0.0 to 29.53).
    """
    if date is None:
        date = datetime.datetime.utcnow()
    
    # Reference New Moon: January 6, 2000
    reference_date = datetime.datetime(2000, 1, 6, 18, 14)
    delta = date - reference_date
    days = delta.total_seconds() / 86400
    synodic_month = 29.53058867
    
    return days % synodic_month


def get_lunar_phase(date: datetime.datetime = None) -> str:
    """
    Determine the current lunar phase as a string description.

    Args:
        date: The date to calculate for.

    Returns:
        str: The name of the phase (e.g., 'New Moon', 'Full Moon').
    """
    age = get_lunar_age(date)
    
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


def get_illumination(date: datetime.datetime = None) -> float:
    """
    Calculate the percentage of the moon illuminated.

    Args:
        date: The date to calculate for.

    Returns:
        float: Illumination percentage between 0.0 and 1.0.
    """
    age = get_lunar_age(date)
    # Using a simplified sine-based approximation for illumination
    return (1 - math.cos(2 * math.pi * age / 29.53058867)) / 2


def is_full_moon(date: datetime.datetime = None, threshold: float = 0.05) -> bool:
    """
    Check if the current phase is within the 'Full Moon' window.

    Args:
        date: The date to calculate for.
        threshold: Variance allowed to be considered full.

    Returns:
        bool: True if it is a Full Moon.
    """
    return get_illumination(date) >= (1.0 - threshold)


def get_lunar_data(date: datetime.datetime = None) -> Dict[str, Union[str, float]]:
    """
    Retrieve a comprehensive dictionary of lunar data.

    Args:
        date: The date to calculate for.

    Returns:
        Dict: A collection of lunar metrics.
    """
    return {
        "age_days": round(get_lunar_age(date), 2),
        "phase": get_lunar_phase(date),
        "illumination": round(get_illumination(date), 4),
        "is_full": is_full_moon(date)
    }
```