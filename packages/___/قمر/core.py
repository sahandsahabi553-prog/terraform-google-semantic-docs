```python
"""
قمر (Qamar) - A Python utility library for lunar cycle calculations.

This module provides tools for tracking lunar phases, illumination percentages,
and celestial timing based on astronomical algorithms.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timezone
from typing import Dict, Union


def get_lunar_age(date: datetime = None) -> float:
    """
    Calculate the age of the moon in days since the last new moon.

    Args:
        date: The datetime object to calculate for. Defaults to current UTC.

    Returns:
        float: The age of the moon in days (0.0 to 29.53).
    """
    if date is None:
        date = datetime.now(timezone.utc)

    # Reference New Moon: January 6, 2000, 18:14 UTC
    epoch = datetime(2000, 1, 6, 18, 14, tzinfo=timezone.utc)
    diff = date.replace(tzinfo=timezone.utc) - epoch
    days = diff.total_seconds() / 86400
    return days % 29.53058867


def get_illumination_percentage(date: datetime = None) -> float:
    """
    Calculate the approximate lunar illumination percentage.

    Args:
        date: The datetime object to calculate for.

    Returns:
        float: Illumination percentage (0.0 to 100.0).
    """
    age = get_lunar_age(date)
    # Use a cosine wave to approximate illumination based on age
    return 50 * (1 - math.cos(2 * math.pi * age / 29.53058867))


def get_lunar_phase_name(date: datetime = None) -> str:
    """
    Determine the current lunar phase name.

    Args:
        date: The datetime object to calculate for.

    Returns:
        str: Name of the phase (e.g., 'New Moon', 'Full Moon').
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


def get_lunar_data(date: datetime = None) -> Dict[str, Union[str, float]]:
    """
    Get a comprehensive dictionary of lunar data for a specific date.

    Args:
        date: The datetime object to calculate for.

    Returns:
        Dict: Contains age, illumination, and phase name.
    """
    if date is None:
        date = datetime.now(timezone.utc)

    return {
        "date": date.isoformat(),
        "age_days": round(get_lunar_age(date), 2),
        "illumination": round(get_illumination_percentage(date), 2),
        "phase": get_lunar_phase_name(date)
    }


def is_full_moon(date: datetime = None, tolerance: float = 0.5) -> bool:
    """
    Check if the moon is in the Full Moon phase within a given tolerance.

    Args:
        date: The datetime object to check.
        tolerance: Days of tolerance around the peak.

    Returns:
        bool: True if it is a full moon, False otherwise.
    """
    age = get_lunar_age(date)
    # Full moon occurs at ~14.76 days
    return abs(age - 14.76) <= tolerance
```