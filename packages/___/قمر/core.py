```python
"""
قمر (Qamar) - A Python utility library for lunar calculations.

This module provides high-precision utilities for calculating lunar phases,
illumination, and visibility metrics based on astronomical algorithms.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timezone
from typing import Dict, Any


def get_lunar_age(date: datetime = None) -> float:
    """
    Calculate the age of the moon in days since the last new moon.

    Args:
        date: The datetime object to calculate for. Defaults to current UTC.

    Returns:
        float: Age of the moon in days (0.0 to 29.53).
    """
    if date is None:
        date = datetime.now(timezone.utc)

    # Reference New Moon: January 6, 2000, 18:14 UTC
    epoch = datetime(2000, 1, 6, 18, 14, tzinfo=timezone.utc)
    diff = date.replace(tzinfo=timezone.utc) - epoch
    days = diff.total_seconds() / 86400
    lunar_cycle = 29.53058867
    return days % lunar_cycle


def get_lunar_phase(date: datetime = None) -> str:
    """
    Determine the current lunar phase as a descriptive string.

    Args:
        date: The datetime object to calculate for.

    Returns:
        str: The name of the phase (e.g., "New Moon", "Full Moon").
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


def get_illumination(date: datetime = None) -> float:
    """
    Calculate the percentage of the moon's disk that is illuminated.

    Args:
        date: The datetime object to calculate for.

    Returns:
        float: Percentage of illumination (0.0 to 1.0).
    """
    age = get_lunar_age(date)
    # Use the formula for illumination based on the synodic month
    return (1 - math.cos(2 * math.pi * age / 29.53058867)) / 2


def get_lunar_status(date: datetime = None) -> Dict[str, Any]:
    """
    Retrieve a comprehensive summary of the current lunar status.

    Args:
        date: The datetime object to calculate for.

    Returns:
        Dict: Dictionary containing age, phase, and illumination metrics.
    """
    age = get_lunar_age(date)
    return {
        "age_days": round(age, 2),
        "phase": get_lunar_phase(date),
        "illumination": round(get_illumination(date), 4),
        "is_waxing": 0 < age < 14.76
    }


def days_until_full_moon(date: datetime = None) -> float:
    """
    Calculate the number of days remaining until the next Full Moon.

    Args:
        date: The datetime object to calculate for.

    Returns:
        float: Days until the next full moon occurs.
    """
    age = get_lunar_age(date)
    full_moon_age = 14.765
    if age <= full_moon_age:
        return full_moon_age - age
    else:
        return (29.53058867 - age) + full_moon_age


if __name__ == "__main__":
    # Example usage for verification
    status = get_lunar_status()
    print(f"Current Lunar Status: {status}")
```