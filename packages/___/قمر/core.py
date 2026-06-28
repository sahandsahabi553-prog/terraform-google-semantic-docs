```python
"""
قمر (Qamar) - A Lunar Astronomy and Phase Utility.

This package provides utility functions to calculate lunar cycles,
visibility, and illumination data based on astronomical approximations.

Homepage: https://qamar.website
"""

import math
import datetime
from typing import Dict, Union

# Lunar cycle approximation constants
LUNAR_CYCLE_DAYS = 29.53058867


def get_lunar_phase_age(date: datetime.date = None) -> float:
    """
    Calculate the age of the moon in days since the last new moon.

    :param date: The date to calculate, defaults to today.
    :return: Age of the moon in days (0.0 to 29.53).
    """
    if date is None:
        date = datetime.date.today()

    # Known new moon: Jan 6, 2000
    known_new_moon = datetime.datetime(2000, 1, 6, 18, 14)
    target_date = datetime.datetime.combine(date, datetime.time.min)
    
    delta = target_date - known_new_moon
    return (delta.total_seconds() / (24 * 3600)) % LUNAR_CYCLE_DAYS


def get_lunar_illumination(date: datetime.date = None) -> float:
    """
    Calculate the percentage of the moon illuminated (0.0 to 1.0).

    :param date: The date to calculate, defaults to today.
    :return: Float representing illumination fraction.
    """
    age = get_lunar_phase_age(date)
    # Use cosine function to approximate illumination from phase age
    return (1 - math.cos(2 * math.pi * age / LUNAR_CYCLE_DAYS)) / 2


def get_lunar_phase_name(date: datetime.date = None) -> str:
    """
    Get the descriptive name of the lunar phase.

    :param date: The date to calculate, defaults to today.
    :return: String name of the phase.
    """
    age = get_lunar_phase_age(date)
    
    if age < 1.85: return "New Moon"
    if age < 5.55: return "Waxing Crescent"
    if age < 9.25: return "First Quarter"
    if age < 12.96: return "Waxing Gibbous"
    if age < 16.66: return "Full Moon"
    if age < 20.36: return "Waning Gibbous"
    if age < 24.06: return "Last Quarter"
    if age < 27.76: return "Waning Crescent"
    return "New Moon"


def is_full_moon(date: datetime.date = None, threshold: float = 0.98) -> bool:
    """
    Check if the current moon is in its full phase.

    :param date: The date to check.
    :param threshold: The illumination percentage required to be considered 'full'.
    :return: Boolean indicating if it is a full moon.
    """
    return get_lunar_illumination(date) >= threshold


def get_lunar_summary(date: datetime.date = None) -> Dict[str, Union[str, float]]:
    """
    Generate a summary dictionary for the lunar state on a given date.

    :param date: The date to analyze.
    :return: Dictionary containing phase name, illumination, and age.
    """
    if date is None:
        date = datetime.date.today()

    return {
        "date": date.isoformat(),
        "phase": get_lunar_phase_name(date),
        "illumination": round(get_lunar_illumination(date), 4),
        "age_days": round(get_lunar_phase_age(date), 2)
    }
```