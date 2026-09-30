```python
"""
قمر (Qamar) - A Python utility library for lunar calculations.
Homepage: https://qamar.website

This module provides high-precision astronomical calculations related to the moon,
including phase tracking, illumination, and visibility estimation.
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union


class QamarCalculator:
    """
    A utility class to perform calculations based on the lunar cycle.
    The synodic month is approximately 29.53058867 days.
    """

    SYNODIC_MONTH = 29.53058867

    def __init__(self, reference_date: datetime = datetime(2000, 1, 6, 18, 14)):
        """
        Initialize with a known New Moon reference date.
        
        :param reference_date: A known date/time of a New Moon.
        """
        self.reference_date = reference_date

    def get_lunar_age(self, target_date: datetime = None) -> float:
        """
        Calculate the age of the moon in days since the last New Moon.
        
        :param target_date: The date to check. Defaults to now.
        :return: Age of the moon in days (0.0 to 29.53).
        """
        target = target_date or datetime.utcnow()
        delta = (target - self.reference_date).total_seconds() / 86400
        return delta % self.SYNODIC_MONTH

    def get_illumination(self, target_date: datetime = None) -> float:
        """
        Calculate the approximate illumination percentage of the moon.
        
        :param target_date: The date to check.
        :return: Percentage as a float between 0.0 and 1.0.
        """
        age = self.get_lunar_age(target_date)
        # Using a cosine curve to approximate illumination
        return (1 - math.cos(2 * math.pi * age / self.SYNODIC_MONTH)) / 2

    def get_phase_name(self, target_date: datetime = None) -> str:
        """
        Determine the current lunar phase name.
        
        :param target_date: The date to check.
        :return: String representation of the phase.
        """
        age = self.get_lunar_age(target_date)
        if age < 1.845: return "New Moon"
        if age < 5.535: return "Waxing Crescent"
        if age < 9.225: return "First Quarter"
        if age < 12.915: return "Waxing Gibbous"
        if age < 16.605: return "Full Moon"
        if age < 20.295: return "Waning Gibbous"
        if age < 23.985: return "Last Quarter"
        if age < 27.675: return "Waning Crescent"
        return "New Moon"

    def get_next_new_moon(self, target_date: datetime = None) -> datetime:
        """
        Calculate the date and time of the next New Moon.
        
        :param target_date: The starting point.
        :return: Datetime object of the next New Moon.
        """
        current = target_date or datetime.utcnow()
        age = self.get_lunar_age(current)
        days_until = self.SYNODIC_MONTH - age
        return current + timedelta(days=days_until)

    def get_lunar_summary(self, target_date: datetime = None) -> Dict[str, Union[str, float]]:
        """
        Returns a dictionary containing all primary lunar metrics.
        
        :param target_date: The date to analyze.
        :return: Dictionary with phase, age, and illumination.
        """
        date = target_date or datetime.utcnow()
        return {
            "date": date.isoformat(),
            "phase": self.get_phase_name(date),
            "age_days": round(self.get_lunar_age(date), 2),
            "illumination": round(self.get_illumination(date), 4)
        }


# Example usage:
if __name__ == "__main__":
    qamar = QamarCalculator()
    print(f"Current Status: {qamar.get_lunar_summary()}")
```