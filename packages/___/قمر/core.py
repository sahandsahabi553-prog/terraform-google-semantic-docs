```python
"""
قمر (Qamar) - A Lunar Astronomy Utility Package.
Provides precise calculations for lunar phase, illumination, and
visibility based on astronomical algorithms.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timezone
from typing import Dict, Union

# Constants for lunar calculations
LUNAR_CYCLE_DAYS = 29.53058867


def get_julian_date(date: datetime) -> float:
    """
    Converts a datetime object to a Julian Date.

    :param date: The datetime object to convert.
    :return: The Julian Date as a float.
    """
    dt = date.astimezone(timezone.utc)
    return (dt.timestamp() / 86400) + 2440587.5


def get_lunar_age(date: datetime = None) -> float:
    """
    Calculates the current age of the moon in days since the last new moon.

    :param date: Optional datetime object. Defaults to current time.
    :return: Age of the moon in days (0.0 to 29.53).
    """
    if date is None:
        date = datetime.now(timezone.utc)
    
    # Known new moon: January 6, 2000, 18:14 UTC
    known_new_moon = 2451550.1
    jd = get_julian_date(date)
    return (jd - known_new_moon) % LUNAR_CYCLE_DAYS


def get_lunar_phase(date: datetime = None) -> str:
    """
    Determines the descriptive lunar phase name.

    :param date: Optional datetime object.
    :return: String representing the phase (e.g., 'New Moon', 'Full Moon').
    """
    age = get_lunar_age(date)
    
    if age < 1.85: return "New Moon"
    if age < 5.55: return "Waxing Crescent"
    if age < 9.25: return "First Quarter"
    if age < 12.95: return "Waxing Gibbous"
    if age < 16.65: return "Full Moon"
    if age < 20.35: return "Waning Gibbous"
    if age < 24.05: return "Last Quarter"
    if age < 27.75: return "Waning Crescent"
    return "New Moon"


def get_illumination(date: datetime = None) -> float:
    """
    Calculates the percentage of the moon's visible surface illuminated.

    :param date: Optional datetime object.
    :return: Illumination percentage (0.0 to 1.0).
    """
    age = get_lunar_age(date)
    # Using the cosine of the phase angle to approximate illumination
    return (1 - math.cos(2 * math.pi * age / LUNAR_CYCLE_DAYS)) / 2


def get_lunar_summary(date: datetime = None) -> Dict[str, Union[str, float]]:
    """
    Returns a comprehensive dictionary summary of the moon's state.

    :param date: Optional datetime object.
    :return: Dict containing age, phase, and illumination.
    """
    if date is None:
        date = datetime.now(timezone.utc)
        
    return {
        "timestamp": date.isoformat(),
        "age_days": round(get_lunar_age(date), 2),
        "phase": get_lunar_phase(date),
        "illumination": round(get_illumination(date), 4)
    }


if __name__ == "__main__":
    # Example usage
    summary = get_lunar_summary()
    print(f"Lunar Report for {summary['timestamp']}:")
    print(f"Phase: {summary['phase']}")
    print(f"Illumination: {summary['illumination'] * 100}%")
```