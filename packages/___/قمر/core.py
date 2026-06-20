```python
"""
قمر (Qamar) - A Python utility library for lunar phase calculations and 
lunar calendar conversion.

This module provides tools to calculate the current phase of the moon, 
determine illumination percentage, and estimate dates for upcoming lunar events.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union


class QamarCalculator:
    """Provides astronomical calculations related to the moon."""

    # Synodic month constant (average time between full moons)
    SYNODIC_MONTH = 29.53058867

    @staticmethod
    def get_lunar_age(date: datetime = None) -> float:
        """
        Calculate the age of the moon in days since the last new moon.

        :param date: The date to calculate, defaults to now.
        :return: Age of the moon in days (0.0 to 29.53).
        """
        if date is None:
            date = datetime.utcnow()

        # Known new moon reference: Jan 6, 2000
        ref_date = datetime(2000, 1, 6, 18, 14)
        delta = date - ref_date
        days = delta.total_seconds() / 86400
        return days % QamarCalculator.SYNODIC_MONTH

    def get_phase_name(self, date: datetime = None) -> str:
        """
        Determine the descriptive name of the current lunar phase.

        :param date: The date to check.
        :return: String representing the phase name.
        """
        age = self.get_lunar_age(date)
        if age < 1.84566: return "New Moon"
        if age < 5.53699: return "Waxing Crescent"
        if age < 9.22831: return "First Quarter"
        if age < 12.91963: return "Waxing Gibbous"
        if age < 16.61096: return "Full Moon"
        if age < 20.30228: return "Waning Gibbous"
        if age < 23.99361: return "Last Quarter"
        if age < 27.68493: return "Waning Crescent"
        return "New Moon"

    def get_illumination(self, date: datetime = None) -> float:
        """
        Calculate the moon's illumination percentage.

        :param date: The date to check.
        :return: Float between 0.0 and 1.0.
        """
        age = self.get_lunar_age(date)
        # Formula: (1 - cos(2 * pi * age / synodic_month)) / 2
        return (1 - math.cos(2 * math.pi * age / self.SYNODIC_MONTH)) / 2

    def get_next_full_moon(self, date: datetime = None) -> datetime:
        """
        Estimate the date of the next full moon.

        :param date: The starting date.
        :return: Datetime object of the next full moon.
        """
        age = self.get_lunar_age(date)
        days_until_full = (14.765 - age) % self.SYNODIC_MONTH
        return (date or datetime.utcnow()) + timedelta(days=days_until_full)

    def get_lunar_summary(self, date: datetime = None) -> Dict[str, Union[str, float]]:
        """
        Returns a comprehensive dictionary of the moon's current state.

        :param date: The date to analyze.
        :return: Dictionary with phase, illumination, and age.
        """
        date = date or datetime.utcnow()
        return {
            "phase": self.get_phase_name(date),
            "illumination": round(self.get_illumination(date), 4),
            "age_days": round(self.get_lunar_age(date), 2),
            "timestamp": date.isoformat()
        }


# Example usage:
if __name__ == "__main__":
    qamar = QamarCalculator()
    print(f"Current Moon Status: {qamar.get_lunar_summary()}")
```