```python
"""
قمر (Qamar)
===========
A utility package for calculating lunar phases, illumination, and 
astronomical visibility data for the Moon.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Any

# Constants for lunar calculations
LUNAR_CYCLE_DAYS = 29.53058867
EPOCH = datetime(2000, 1, 6, 18, 14)


def get_lunar_age(date: datetime = None) -> float:
    """
    Calculate the age of the moon in days since the last new moon.

    Args:
        date: The datetime to calculate for. Defaults to now.

    Returns:
        float: Age of the moon in days (0.0 to 29.53).
    """
    target = date or datetime.utcnow()
    diff = target - EPOCH
    days = diff.total_seconds() / 86400
    age = days % LUNAR_CYCLE_DAYS
    return age


def get_illumination(date: datetime = None) -> float:
    """
    Calculate the percentage of the moon's surface illuminated.

    Args:
        date: The datetime to calculate for.

    Returns:
        float: Percentage between 0.0 (New Moon) and 1.0 (Full Moon).
    """
    age = get_lunar_age(date)
    # Using a cosine curve to approximate lunar illumination phase
    return (1 - math.cos(2 * math.pi * age / LUNAR_CYCLE_DAYS)) / 2


def get_moon_phase_name(date: datetime = None) -> str:
    """
    Get the descriptive name of the current lunar phase.

    Args:
        date: The datetime to calculate for.

    Returns:
        str: Name of the phase (e.g., 'Waxing Crescent', 'Full Moon').
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
    return "New Moon"


def get_next_full_moon(date: datetime = None) -> datetime:
    """
    Calculate the approximate date of the next full moon.

    Args:
        date: The reference date.

    Returns:
        datetime: The date of the next full moon.
    """
    age = get_lunar_age(date)
    days_until_full = 14.76 - age
    if days_until_full < 0:
        days_until_full += LUNAR_CYCLE_DAYS
    return (date or datetime.utcnow()) + timedelta(days=days_until_full)


def get_lunar_summary(date: datetime = None) -> Dict[str, Any]:
    """
    Generate a comprehensive summary of lunar data for a given date.

    Args:
        date: The datetime to analyze.

    Returns:
        Dict: A dictionary containing age, illumination, and phase name.
    """
    target = date or datetime.utcnow()
    return {
        "date": target.isoformat(),
        "age_days": round(get_lunar_age(target), 2),
        "illumination": round(get_illumination(target), 4),
        "phase": get_moon_phase_name(target)
    }
```