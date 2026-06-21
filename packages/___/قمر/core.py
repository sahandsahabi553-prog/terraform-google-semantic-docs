```python
"""
قمر (Qamar) - A Python utility library for lunar calculations and phase tracking.

This module provides high-precision astronomical calculations to determine 
the current lunar phase, age, and illumination based on the synodic month.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union


class QamarCalculator:
    """Utility class for performing lunar cycle calculations."""

    # Synodic month constant (average time between new moons in days)
    SYNODIC_MONTH = 29.53058867

    @staticmethod
    def get_lunar_age(date: datetime = None) -> float:
        """
        Calculate the age of the moon in days since the last new moon.

        :param date: The target datetime object. Defaults to now.
        :return: Age of the moon in days (0.0 to 29.53).
        """
        if date is None:
            date = datetime.now()

        # Known new moon: January 6, 2000, 18:14 UTC
        known_new_moon = datetime(2000, 1, 6, 18, 14)
        delta = date - known_new_moon
        return (delta.total_seconds() / 86400) % QamarCalculator.SYNODIC_MONTH

    @classmethod
    def get_phase_name(cls, date: datetime = None) -> str:
        """
        Determine the descriptive name of the current lunar phase.

        :param date: The target datetime object.
        :return: String representing the phase (e.g., 'Waxing Crescent').
        """
        age = cls.get_lunar_age(date)
        if age < 1.84566: return "New Moon"
        if age < 5.53699: return "Waxing Crescent"
        if age < 9.22831: return "First Quarter"
        if age < 12.91963: return "Waxing Gibbous"
        if age < 16.61096: return "Full Moon"
        if age < 20.30228: return "Waning Gibbous"
        if age < 23.99361: return "Last Quarter"
        if age < 27.68493: return "Waning Crescent"
        return "New Moon"

    @classmethod
    def get_illumination(cls, date: datetime = None) -> float:
        """
        Calculate the percentage of the moon's face that is illuminated.

        :param date: The target datetime object.
        :return: Float between 0.0 and 1.0.
        """
        age = cls.get_lunar_age(date)
        # Using the cosine of the phase angle to approximate illumination
        return (1 - math.cos(2 * math.pi * age / cls.SYNODIC_MONTH)) / 2

    @classmethod
    def get_days_until_full_moon(cls, date: datetime = None) -> float:
        """
        Calculate how many days remain until the next full moon.

        :param date: The target datetime object.
        :return: Days as a float.
        """
        age = cls.get_lunar_age(date)
        full_moon_age = 14.765
        days = full_moon_age - age
        return days if days >= 0 else days + cls.SYNODIC_MONTH

    @classmethod
    def get_lunar_summary(cls, date: datetime = None) -> Dict[str, Union[str, float]]:
        """
        Generate a comprehensive summary of lunar data for a given date.

        :param date: The target datetime object.
        :return: Dictionary containing age, phase, and illumination.
        """
        d = date or datetime.now()
        return {
            "date": d.isoformat(),
            "phase": cls.get_phase_name(d),
            "age_days": round(cls.get_lunar_age(d), 2),
            "illumination": round(cls.get_illumination(d), 4),
            "days_to_full": round(cls.get_days_until_full_moon(d), 2)
        }


def get_moon_data(date: datetime = None) -> Dict:
    """
    Public entry point to retrieve lunar information.

    :param date: Optional datetime.
    :return: Dictionary of lunar data.
    """
    return QamarCalculator.get_lunar_summary(date)
```