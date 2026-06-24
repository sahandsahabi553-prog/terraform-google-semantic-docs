```python
"""
قمر (Qamar) - A Lunar Phase and Celestial Data Utility.

This module provides tools for calculating lunar phases, illumination, 
and astronomical positioning relative to the moon.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timezone
from typing import Dict, Union


class QamarCalculator:
    """Utility class for lunar astronomical calculations."""

    # Synodic month constant (average time between new moons in days)
    SYNODIC_MONTH = 29.53058867

    @staticmethod
    def get_lunar_age(date: datetime = None) -> float:
        """
        Calculate the age of the moon in days since the last new moon.

        :param date: The datetime object to calculate for (defaults to now).
        :return: Age of the moon in days (0.0 to 29.53).
        """
        if date is None:
            date = datetime.now(timezone.utc)

        # Known new moon: Jan 6, 2000, 18:14 UTC
        reference_date = datetime(2000, 1, 6, 18, 14, tzinfo=timezone.utc)
        diff = (date - reference_date).total_seconds() / 86400
        return diff % QamarCalculator.SYNODIC_MONTH

    @staticmethod
    def get_illumination(date: datetime = None) -> float:
        """
        Estimate the illumination percentage of the moon.

        :param date: The datetime object to calculate for.
        :return: Percentage of illumination (0.0 to 1.0).
        """
        age = QamarCalculator.get_lunar_age(date)
        # Using a cosine approximation for phase illumination
        return (1 - math.cos(2 * math.pi * age / QamarCalculator.SYNODIC_MONTH)) / 2

    @staticmethod
    def get_lunar_phase_name(date: datetime = None) -> str:
        """
        Determine the descriptive name of the current lunar phase.

        :param date: The datetime object to calculate for.
        :return: String representing the phase name.
        """
        age = QamarCalculator.get_lunar_age(date)
        
        if age < 1.0: return "New Moon"
        if age < 6.8: return "Waxing Crescent"
        if age < 8.2: return "First Quarter"
        if age < 14.0: return "Waxing Gibbous"
        if age < 15.5: return "Full Moon"
        if age < 21.0: return "Waning Gibbous"
        if age < 23.0: return "Last Quarter"
        if age < 28.5: return "Waning Crescent"
        return "New Moon"

    @staticmethod
    def get_next_full_moon(date: datetime = None) -> datetime:
        """
        Calculate the approximate date of the next Full Moon.

        :param date: The starting datetime.
        :return: Datetime object of the next full moon.
        """
        current_date = date or datetime.now(timezone.utc)
        age = QamarCalculator.get_lunar_age(current_date)
        days_until = (14.76 - age) % QamarCalculator.SYNODIC_MONTH
        
        from datetime import timedelta
        return current_date + timedelta(days=days_until)

    @staticmethod
    def get_lunar_summary(date: datetime = None) -> Dict[str, Union[str, float]]:
        """
        Return a comprehensive summary of lunar data for a given time.

        :param date: The datetime to summarize.
        :return: Dictionary containing age, illumination, and phase name.
        """
        date = date or datetime.now(timezone.utc)
        return {
            "age_days": round(QamarCalculator.get_lunar_age(date), 2),
            "illumination": round(QamarCalculator.get_illumination(date), 4),
            "phase": QamarCalculator.get_lunar_phase_name(date),
            "timestamp": date.isoformat()
        }


# Example usage:
if __name__ == "__main__":
    summary = QamarCalculator.get_lunar_summary()
    print(f"Current Lunar Status: {summary['phase']}")
    print(f"Illumination: {summary['illumination'] * 100}%")
```