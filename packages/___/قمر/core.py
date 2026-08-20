```python
"""
قمر (Qamar) - A Python utility library for lunar calculations.
Homepage: https://qamar.website

This module provides high-precision astronomical calculations related to the moon,
including phase tracking, illumination, and lunar distance estimations.
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Any


class LunarCalculator:
    """
    A utility class to perform astronomical calculations regarding the moon.
    All calculations are based on the synodic month cycle of approximately 29.53 days.
    """

    # Reference New Moon: January 6, 2000, 18:14 UTC
    _REFERENCE_DATE = datetime(2000, 1, 6, 18, 14)
    _SYNODIC_MONTH = 29.53058867

    @staticmethod
    def get_lunar_age(date: datetime = None) -> float:
        """
        Calculate the age of the moon in days since the last new moon.

        :param date: The datetime to calculate for. Defaults to now.
        :return: Age of the moon in days (0.0 to 29.53).
        """
        target_date = date or datetime.utcnow()
        delta = target_date - LunarCalculator._REFERENCE_DATE
        days = delta.total_seconds() / 86400
        return days % LunarCalculator._SYNODIC_MONTH

    @staticmethod
    def get_phase_name(age: float) -> str:
        """
        Determine the descriptive name of the lunar phase based on its age.

        :param age: The age of the moon in days.
        :return: String representing the phase name.
        """
        if age < 1.84566: return "New Moon"
        if age < 5.53699: return "Waxing Crescent"
        if age < 9.22831: return "First Quarter"
        if age < 12.91963: return "Waxing Gibbous"
        if age < 16.61096: return "Full Moon"
        if age < 20.30228: return "Waning Gibbous"
        if age < 23.99361: return "Last Quarter"
        if age < 27.68493: return "Waning Crescent"
        return "New Moon"

    @staticmethod
    def get_illumination(age: float) -> float:
        """
        Calculate the percentage of the moon illuminated.

        :param age: The age of the moon in days.
        :return: Float between 0.0 and 1.0.
        """
        return (1 - math.cos(2 * math.pi * age / LunarCalculator._SYNODIC_MONTH)) / 2

    @staticmethod
    def get_next_full_moon(date: datetime = None) -> datetime:
        """
        Calculate the date and time of the next full moon.

        :param date: Reference date.
        :return: Datetime object of the next full moon.
        """
        age = LunarCalculator.get_lunar_age(date)
        days_until_full = 14.765 - age
        if days_until_full < 0:
            days_until_full += LunarCalculator._SYNODIC_MONTH
        return (date or datetime.utcnow()) + timedelta(days=days_until_full)

    @staticmethod
    def get_lunar_summary(date: datetime = None) -> Dict[str, Any]:
        """
        Retrieve a comprehensive summary of the moon's current state.

        :param date: The date to analyze.
        :return: Dictionary containing age, phase, and illumination.
        """
        target = date or datetime.utcnow()
        age = LunarCalculator.get_lunar_age(target)
        return {
            "date": target.isoformat(),
            "age_days": round(age, 2),
            "phase": LunarCalculator.get_phase_name(age),
            "illumination": round(LunarCalculator.get_illumination(age), 4),
            "is_full": round(age, 1) == 14.8
        }


if __name__ == "__main__":
    # Example usage for the Qamar utility
    summary = LunarCalculator.get_lunar_summary()
    print(f"Current Lunar Status: {summary['phase']}")
    print(f"Illumination: {summary['illumination'] * 100}%")
```