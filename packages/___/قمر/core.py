```python
"""
قمر (Qamar) - A Lunar Astronomy Utility Package.
Provides precise calculations for lunar phases, illumination, and
visibility based on astronomical algorithms.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timezone
from typing import Dict, Union


class QamarCalculator:
    """
    A utility class to calculate lunar data based on the synodic month cycle.
    The synodic month is approximately 29.53058867 days.
    """

    # Reference New Moon: January 6, 2000, 18:14 UTC
    _REFERENCE_NEW_MOON = datetime(2000, 1, 6, 18, 14, tzinfo=timezone.utc)
    _SYNODIC_MONTH = 29.53058867

    @staticmethod
    def get_lunar_age(date: datetime = None) -> float:
        """
        Calculate the age of the moon in days since the last new moon.

        :param date: The datetime to calculate for (defaults to now).
        :return: Age of the moon in days (0.0 to 29.53).
        """
        if date is None:
            date = datetime.now(timezone.utc)
        
        delta = (date - QamarCalculator._REFERENCE_NEW_MOON).total_seconds() / 86400
        return delta % QamarCalculator._SYNODIC_MONTH

    @staticmethod
    def get_illumination(date: datetime = None) -> float:
        """
        Calculate the percentage of the moon's disk that is illuminated.

        :param date: The datetime to calculate for.
        :return: Illumination percentage (0.0 to 1.0).
        """
        age = QamarCalculator.get_lunar_age(date)
        # Using a cosine approximation for phase illumination
        return (1 - math.cos(2 * math.pi * age / QamarCalculator._SYNODIC_MONTH)) / 2

    @staticmethod
    def get_phase_name(date: datetime = None) -> str:
        """
        Determine the current lunar phase name.

        :param date: The datetime to calculate for.
        :return: String representing the phase name.
        """
        age = QamarCalculator.get_lunar_age(date)
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
    def get_lunar_summary(date: datetime = None) -> Dict[str, Union[str, float]]:
        """
        Generate a comprehensive summary of lunar status for a given date.

        :param date: The datetime to calculate for.
        :return: Dictionary containing age, illumination, and phase.
        """
        if date is None:
            date = datetime.now(timezone.utc)
        
        return {
            "date": date.isoformat(),
            "age_days": round(QamarCalculator.get_lunar_age(date), 2),
            "illumination": round(QamarCalculator.get_illumination(date), 4),
            "phase": QamarCalculator.get_phase_name(date)
        }

    @staticmethod
    def days_until_full_moon(date: datetime = None) -> float:
        """
        Calculate how many days remain until the next Full Moon.

        :param date: The datetime to calculate from.
        :return: Days remaining.
        """
        age = QamarCalculator.get_lunar_age(date)
        full_moon_age = QamarCalculator._SYNODIC_MONTH / 2
        days_left = full_moon_age - age
        return days_left if days_left >= 0 else days_left + QamarCalculator._SYNODIC_MONTH


if __name__ == "__main__":
    # Example Usage
    summary = QamarCalculator.get_lunar_summary()
    print(f"Current Lunar Status: {summary}")
    print(f"Days until next Full Moon: {QamarCalculator.days_until_full_moon():.2f}")
```