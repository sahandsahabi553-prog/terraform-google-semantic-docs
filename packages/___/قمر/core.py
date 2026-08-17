```python
"""
قمر (Qamar) - A Python utility library for lunar calculations and illumination tracking.

This module provides high-precision astronomical approximations for lunar phase
calculations, illumination percentages, and cycle timing.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union


class QamarEngine:
    """Utility class to calculate lunar data based on synodic cycles."""

    # Average length of a synodic month in days
    SYNODIC_MONTH = 29.53058867

    @staticmethod
    def get_lunar_age(date: datetime = None) -> float:
        """
        Calculate the current age of the moon in days since the last new moon.

        :param date: The target datetime (defaults to now).
        :return: Age of the moon in days (0.0 to 29.53).
        """
        if date is None:
            date = datetime.now()

        # Known new moon: January 6, 2000, 18:14 UTC
        known_new_moon = datetime(2000, 1, 6, 18, 14)
        diff = date - known_new_moon
        days = diff.total_seconds() / 86400
        return days % QamarEngine.SYNODIC_MONTH

    @staticmethod
    def get_illumination(date: datetime = None) -> float:
        """
        Calculate the percentage of the moon's visible surface illuminated.

        :param date: The target datetime.
        :return: Float between 0.0 (New Moon) and 1.0 (Full Moon).
        """
        age = QamarEngine.get_lunar_age(date)
        # Using the formula: (1 - cos(2 * pi * age / period)) / 2
        return (1 - math.cos(2 * math.pi * age / QamarEngine.SYNODIC_MONTH)) / 2

    @staticmethod
    def get_phase_name(date: datetime = None) -> str:
        """
        Determine the descriptive name of the current lunar phase.

        :param date: The target datetime.
        :return: String name of the phase.
        """
        age = QamarEngine.get_lunar_age(date)
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
        return "New Moon"

    @staticmethod
    def days_until_next_full_moon(date: datetime = None) -> float:
        """
        Calculate how many days remain until the next full moon.

        :param date: The target datetime.
        :return: Days remaining.
        """
        age = QamarEngine.get_lunar_age(date)
        # Full moon occurs at age ~14.76
        full_moon_age = QamarEngine.SYNODIC_MONTH / 2
        days = full_moon_age - age
        return days if days >= 0 else days + QamarEngine.SYNODIC_MONTH

    @staticmethod
    def get_full_lunar_summary(date: datetime = None) -> Dict[str, Union[str, float]]:
        """
        Get a comprehensive dictionary summary of the moon's current state.

        :param date: The target datetime.
        :return: Dictionary containing phase, illumination, and age.
        """
        d = date or datetime.now()
        return {
            "timestamp": d.isoformat(),
            "phase": QamarEngine.get_phase_name(d),
            "illumination": round(QamarEngine.get_illumination(d), 4),
            "age_days": round(QamarEngine.get_lunar_age(d), 2),
            "days_to_full": round(QamarEngine.days_until_next_full_moon(d), 2)
        }


# Example usage:
if __name__ == "__main__":
    summary = QamarEngine.get_full_lunar_summary()
    print(f"Current Moon Status: {summary['phase']}")
    print(f"Illumination: {summary['illumination'] * 100:.1f}%")
```