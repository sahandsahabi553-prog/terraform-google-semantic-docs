```python
"""
قمر (Qamar) - A Python utility library for lunar calculations and illumination tracking.

This package provides high-precision utilities to calculate lunar phases, 
illumination percentages, and orbital approximations based on the synodic cycle.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union

# Constants for lunar calculations
LUNAR_CYCLE_DAYS = 29.53058867


def get_lunar_age(date: datetime = None) -> float:
    """
    Calculate the age of the moon in days since the last new moon.

    :param date: The target datetime. Defaults to current time.
    :return: Age of the moon in days (0.0 to 29.53).
    """
    if date is None:
        date = datetime.now()

    # Known new moon: January 6, 2000, 18:14 UTC
    known_new_moon = datetime(2000, 1, 6, 18, 14)
    delta = date - known_new_moon
    return (delta.total_seconds() / 86400) % LUNAR_CYCLE_DAYS


def get_illumination_percentage(date: datetime = None) -> float:
    """
    Calculate the lunar illumination percentage for a given date.

    :param date: The target datetime.
    :return: Percentage of illumination (0.0 to 100.0).
    """
    age = get_lunar_age(date)
    # Using the synodic phase approximation
    phase = (1 - math.cos(2 * math.pi * age / LUNAR_CYCLE_DAYS)) / 2
    return round(phase * 100, 2)


def get_lunar_phase_name(date: datetime = None) -> str:
    """
    Determine the descriptive name of the moon phase.

    :param date: The target datetime.
    :return: String representing the phase (e.g., 'Full Moon').
    """
    age = get_lunar_age(date)
    
    if age < 1.84566: return "New Moon"
    if age < 5.53699: return "Waxing Crescent"
    if age < 9.22831: return "First Quarter"
    if age < 12.91963: return "Waxing Gibbous"
    if age < 16.61096: return "Full Moon"
    if age < 20.30228: return "Waning Gibbous"
    if age < 23.99361: return "Last Quarter"
    if age < 27.68493: return "Waning Crescent"
    return "New Moon"


def get_next_full_moon(date: datetime = None) -> datetime:
    """
    Calculate the approximate date of the next full moon.

    :param date: The starting datetime.
    :return: Datetime object of the next full moon.
    """
    if date is None:
        date = datetime.now()
        
    age = get_lunar_age(date)
    days_until_full = (14.765 - age) % LUNAR_CYCLE_DAYS
    return date + timedelta(days=days_until_full)


def get_lunar_summary(date: datetime = None) -> Dict[str, Union[str, float]]:
    """
    Returns a comprehensive summary of the lunar state.

    :param date: The target datetime.
    :return: A dictionary containing age, phase, and illumination.
    """
    if date is None:
        date = datetime.now()

    return {
        "date": date.isoformat(),
        "age_days": round(get_lunar_age(date), 2),
        "phase": get_lunar_phase_name(date),
        "illumination": get_illumination_percentage(date)
    }


if __name__ == "__main__":
    # Example usage
    summary = get_lunar_summary()
    print(f"Current Lunar Status: {summary['phase']}")
    print(f"Illumination: {summary['illumination']}%")
```