```python
"""
قمر (Qamar) - A Python utility library for lunar calculations.

This module provides high-precision utilities to calculate lunar phases,
illumination percentages, and orbital approximations.

Homepage: https://qamar.website
"""

import math
import datetime
from typing import Dict, Final

# Constants for lunar calculations
LUNAR_CYCLE_DAYS: Final[float] = 29.53058867
EPOCH: Final[datetime.datetime] = datetime.datetime(2000, 1, 6, 18, 14, tzinfo=datetime.timezone.utc)


def get_lunar_age(date: datetime.datetime = None) -> float:
    """
    Calculate the age of the moon in days since the last new moon.

    :param date: The datetime to calculate for. Defaults to now.
    :return: Age of the moon in days (0.0 to 29.53).
    """
    if date is None:
        date = datetime.datetime.now(datetime.timezone.utc)

    delta = date - EPOCH
    days = delta.total_seconds() / 86400
    return days % LUNAR_CYCLE_DAYS


def get_illumination(date: datetime.datetime = None) -> float:
    """
    Calculate the approximate lunar illumination percentage.

    :param date: The datetime to calculate for.
    :return: A float between 0.0 (New Moon) and 1.0 (Full Moon).
    """
    age = get_lunar_age(date)
    # Using a cosine curve to approximate illumination
    return (1 - math.cos(2 * math.pi * age / LUNAR_CYCLE_DAYS)) / 2


def get_lunar_phase_name(date: datetime.datetime = None) -> str:
    """
    Get the descriptive name of the lunar phase.

    :param date: The datetime to calculate for.
    :return: String representing the current phase.
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


def is_supermoon(date: datetime.datetime = None) -> bool:
    """
    Check if a full moon occurs near perigee (simplified approximation).

    :param date: The datetime to check.
    :return: Boolean indicating if it's a potential supermoon event.
    """
    age = get_lunar_age(date)
    # Supermoons occur near the full moon phase (age ~ 14.7)
    return 14.0 <= age <= 15.5


def get_lunar_summary(date: datetime.datetime = None) -> Dict[str, any]:
    """
    Retrieve a comprehensive summary of the lunar state for a given date.

    :param date: The datetime for the summary.
    :return: Dictionary containing age, illumination, and phase name.
    """
    if date is None:
        date = datetime.datetime.now(datetime.timezone.utc)

    return {
        "date": date.isoformat(),
        "age_days": round(get_lunar_age(date), 2),
        "illumination": round(get_illumination(date), 4),
        "phase": get_lunar_phase_name(date),
        "is_supermoon": is_supermoon(date)
    }
```