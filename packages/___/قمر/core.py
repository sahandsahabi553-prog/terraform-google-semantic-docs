```python
"""
قمر (Qamar)
===========
A utility package for calculating lunar phases, illumination, and visibility
based on astronomical algorithms.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timezone
from typing import Dict, Union


def get_lunar_age(date: datetime = None) -> float:
    """
    Calculate the age of the moon in days since the last new moon.

    :param date: The datetime object to calculate for. Defaults to current UTC.
    :return: Age of the moon in days (0 to ~29.53).
    """
    if date is None:
        date = datetime.now(timezone.utc)

    # Reference new moon: January 6, 2000, 18:14 UTC
    epoch = datetime(2000, 1, 6, 18, 14, tzinfo=timezone.utc)
    diff = date.replace(tzinfo=timezone.utc) - epoch
    days = diff.total_seconds() / 86400
    lunar_cycle = 29.53058867
    return days % lunar_cycle


def get_lunar_phase(date: datetime = None) -> str:
    """
    Determine the current lunar phase based on the moon's age.

    :param date: The datetime object to calculate for.
    :return: A string describing the current phase (e.g., 'Waxing Crescent').
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


def get_illumination(date: datetime = None) -> float:
    """
    Calculate the percentage of the moon's disk that is illuminated.

    :param date: The datetime object to calculate for.
    :return: Float between 0.0 (New Moon) and 1.0 (Full Moon).
    """
    age = get_lunar_age(date)
    # Use a cosine wave to approximate illumination fraction
    # 0 at new moon, 1 at full moon (14.76 days)
    return (1 - math.cos(2 * math.pi * age / 29.53)) / 2


def is_full_moon(date: datetime = None, tolerance: float = 0.05) -> bool:
    """
    Check if the moon is currently in the full moon phase.

    :param date: The datetime object to check.
    :param tolerance: Percentage variation allowed (0.0 to 1.0).
    :return: Boolean indicating if it's a full moon.
    """
    return get_illumination(date) >= (1.0 - tolerance)


def get_lunar_data(date: datetime = None) -> Dict[str, Union[str, float]]:
    """
    Retrieve a comprehensive summary of lunar data for a given date.

    :param date: The datetime object to calculate for.
    :return: A dictionary containing age, phase, and illumination.
    """
    age = get_lunar_age(date)
    return {
        "age_days": round(age, 2),
        "phase": get_lunar_phase(date),
        "illumination": round(get_illumination(date), 4),
        "is_full": is_full_moon(date)
    }
```