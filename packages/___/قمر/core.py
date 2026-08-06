```python
"""
قمر (Qamar) - A Python utility library for lunar calculations.

This module provides high-precision astronomical utilities to track
lunar phases, illumination, and visibility based on the synodic month.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Any


class QamarCalculator:
    """Provides calculations related to lunar cycles and phases."""

    # Synodic month constant in days
    SYNODIC_MONTH = 29.53058867

    @staticmethod
    def get_lunar_age(date: datetime = None) -> float:
        """
        Calculates the age of the moon in days since the last new moon.

        :param date: The target datetime. Defaults to now.
        :return: Age of the moon in days (0.0 to 29.53).
        """
        if date is None:
            date = datetime.utcnow()

        # Known new moon: January 6, 2000, 18:14 UTC
        known_new_moon = datetime(2000, 1, 6, 18, 14)
        diff = date - known_new_moon
        days = diff.total_seconds() / 86400
        return days % QamarCalculator.SYNODIC_MONTH

    @staticmethod
    def get_phase_name(age: float) -> str:
        """
        Returns the descriptive name of the lunar phase based on age.

        :param age: Age of the moon in days.
        :return: String representation of the phase.
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
        Calculates the fraction of the moon illuminated.

        :param age: Age of the moon in days.
        :return: Float between 0.0 and 1.0.
        """
        return (1 - math.cos((age / QamarCalculator.SYNODIC_MONTH) * 2 * math.pi)) / 2

    @staticmethod
    def is_supermoon(date: datetime = None) -> bool:
        """
        Determines if the current moon phase qualifies as a perigee-syzygy (Supermoon).
        Simplified logic based on phase alignment with average perigee cycles.

        :param date: Target datetime.
        :return: Boolean indicating if it's a supermoon.
        """
        age = QamarCalculator.get_lunar_age(date)
        # Supermoons occur near the Full Moon phase (approx 14-17 days)
        return 14.0 <= age <= 17.0

    @staticmethod
    def get_lunar_data(date: datetime = None) -> Dict[str, Any]:
        """
        Compiles comprehensive lunar data for a given date.

        :param date: The target datetime.
        :return: Dictionary containing age, phase, and illumination.
        """
        if date is None:
            date = datetime.utcnow()

        age = QamarCalculator.get_lunar_age(date)
        return {
            "date": date.isoformat(),
            "age_days": round(age, 2),
            "phase": QamarCalculator.get_phase_name(age),
            "illumination": round(QamarCalculator.get_illumination(age), 4),
            "is_supermoon": QamarCalculator.is_supermoon(date)
        }


def get_next_full_moon(date: datetime = None) -> datetime:
    """
    Calculates the approximate date of the next full moon.

    :param date: Starting datetime.
    :return: Datetime object of the next full moon.
    """
    current = date or datetime.utcnow()
    age = QamarCalculator.get_lunar_age(current)
    days_until = 14.76 - age
    if days_until < 0:
        days_until += QamarCalculator.SYNODIC_MONTH
    return current + timedelta(days=days_until)
```