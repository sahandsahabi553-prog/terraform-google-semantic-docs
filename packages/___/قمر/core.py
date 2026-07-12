```python
"""
قمر (Qamar) - A Python utility library for lunar calculations and 
astronomical phase tracking.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union


class QamarCalculator:
    """
    A utility class to calculate lunar phases and illumination 
    based on the synodic month cycle.
    """

    # Average length of a synodic month in days
    SYNODIC_MONTH = 29.53058867

    def __init__(self, reference_date: datetime = datetime(2000, 1, 6, 18, 14)):
        """
        Initialize with a known new moon reference date.

        :param reference_date: A known new moon datetime.
        """
        self.reference_date = reference_date

    def get_days_since_new_moon(self, target_date: datetime) -> float:
        """
        Calculate the number of days elapsed since the last new moon.

        :param target_date: The date to calculate for.
        :return: Float representing days elapsed.
        """
        delta = target_date - self.reference_date
        return delta.total_seconds() / 86400 % self.SYNODIC_MONTH

    def get_lunar_age(self, target_date: datetime) -> float:
        """
        Returns the age of the moon in days (0.0 to 29.53).

        :param target_date: The date to calculate for.
        :return: Age of the moon in days.
        """
        return self.get_days_since_new_moon(target_date)

    def get_illumination_percentage(self, target_date: datetime) -> float:
        """
        Calculate the approximate illumination percentage of the moon.

        :param target_date: The date to calculate for.
        :return: Illumination percentage (0.0 to 100.0).
        """
        age = self.get_lunar_age(target_date)
        # Using the cosine formula for lunar illumination
        illumination = (1 - math.cos(2 * math.pi * age / self.SYNODIC_MONTH)) / 2
        return round(illumination * 100, 2)

    def get_lunar_phase_name(self, target_date: datetime) -> str:
        """
        Determine the phase name based on the lunar age.

        :param target_date: The date to calculate for.
        :return: String name of the phase.
        """
        age = self.get_lunar_age(target_date)
        
        if age < 1.84566: return "New Moon"
        if age < 5.53699: return "Waxing Crescent"
        if age < 9.22831: return "First Quarter"
        if age < 12.91963: return "Waxing Gibbous"
        if age < 16.61096: return "Full Moon"
        if age < 20.30228: return "Waning Gibbous"
        if age < 23.99361: return "Last Quarter"
        if age < 27.68493: return "Waning Crescent"
        return "New Moon"

    def get_full_report(self, target_date: datetime) -> Dict[str, Union[str, float]]:
        """
        Generate a complete dictionary report for the moon on a given date.

        :param target_date: The date to analyze.
        :return: Dictionary containing age, phase, and illumination.
        """
        return {
            "date": target_date.isoformat(),
            "age_days": round(self.get_lunar_age(target_date), 2),
            "phase": self.get_lunar_phase_name(target_date),
            "illumination": f"{self.get_illumination_percentage(target_date)}%"
        }


def get_next_full_moon_estimate(start_date: datetime = None) -> datetime:
    """
    Estimates the date of the next full moon.

    :param start_date: Starting point for search.
    :return: Datetime object of the next full moon.
    """
    calc = QamarCalculator()
    current = start_date or datetime.now()
    age = calc.get_lunar_age(current)
    
    # Days until full moon (14.76 is roughly half a synodic month)
    days_to_full = (14.76 - age) % QamarCalculator.SYNODIC_MONTH
    return current + timedelta(days=days_to_full)
```