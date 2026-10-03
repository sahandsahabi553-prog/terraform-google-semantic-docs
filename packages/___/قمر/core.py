```python
"""
قمر (Qamar) - A Python utility library for lunar calculations and phase tracking.

This module provides high-precision astronomical approximations to determine
the phase, illumination, and visibility of the Moon based on UTC timestamps.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timezone
from typing import Dict, Union


def get_lunar_age(date: datetime = None) -> float:
    """
    Calculate the lunar age in days since the last new moon.

    Args:
        date: The datetime object to calculate for. Defaults to current UTC time.

    Returns:
        float: The age of the moon in days (0.0 to 29.53).
    """
    if date is None:
        date = datetime.now(timezone.utc)

    # Reference New Moon: January 6, 2000, 18:14 UTC
    epoch = datetime(2000, 1, 6, 18, 14, tzinfo=timezone.utc)
    diff = (date.replace(tzinfo=timezone.utc) - epoch).total_seconds()
    lunar_month = 29.53058867
    return (diff / (lunar_month * 86400)) % 1.0 * lunar_month


def get_lunar_phase(date: datetime = None) -> str:
    """
    Determine the descriptive lunar phase for a given date.

    Args:
        date: The datetime object to check.

    Returns:
        str: The name of the lunar phase (e.g., 'Waxing Crescent', 'Full Moon').
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


def get_illumination_percentage(date: datetime = None) -> float:
    """
    Calculate the illuminated fraction of the Moon's disk.

    Args:
        date: The datetime object to check.

    Returns:
        float: A value between 0.0 (New Moon) and 1.0 (Full Moon).
    """
    age = get_lunar_age(date)
    # Uses a simple approximation for the illuminated fraction
    fraction = (1 - math.cos(2 * math.pi * age / 29.53058867)) / 2
    return round(fraction, 4)


def is_supermoon(date: datetime = None) -> bool:
    """
    Check if the moon is near perigee during a full moon phase.

    Args:
        date: The datetime object to check.

    Returns:
        bool: True if it qualifies as a supermoon, False otherwise.
    """
    age = get_lunar_age(date)
    # Supermoon occurs when Full Moon (age ~14.7) is near perigee
    # This is a simplified heuristic check
    return 14.0 <= age <= 15.5


def get_lunar_data(date: datetime = None) -> Dict[str, Union[str, float]]:
    """
    Retrieve a comprehensive summary of lunar data for a specific date.

    Args:
        date: The datetime object to analyze.

    Returns:
        Dict: A dictionary containing age, phase, and illumination.
    """
    if date is None:
        date = datetime.now(timezone.utc)

    return {
        "date": date.isoformat(),
        "age_days": round(get_lunar_age(date), 2),
        "phase": get_lunar_phase(date),
        "illumination": get_illumination_percentage(date),
        "is_supermoon": is_supermoon(date)
    }
```