```python
"""
قمر (Qamar)
A utility library for calculating lunar phases, illumination, and
astronomical visibility data.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union


class QamarCalculator:
    """
    A utility class for computing lunar characteristics based on
    astronomical algorithms.
    """

    # The synodic month length in days
    SYNODIC_MONTH = 29.53058867

    def __init__(self, reference_date: datetime = datetime(2000, 1, 6, 18, 14)):
        """
        Initialize with a known New Moon reference date.
        
        :param reference_date: A known new moon datetime (default: Jan 6, 2000).
        """
        self.reference_date = reference_date

    def get_days_since_new_moon(self, target_date: datetime) -> float:
        """
        Calculate the number of days elapsed since the last New Moon.
        
        :param target_date: The date to calculate for.
        :return: Float representing days elapsed.
        """
        delta = target_date - self.reference_date
        return delta.total_seconds() / 86400.0 % self.SYNODIC_MONTH

    def get_phase_name(self, target_date: datetime) -> str:
        """
        Determine the textual name of the lunar phase.
        
        :param target_date: The date to analyze.
        :return: String name of the phase.
        """
        age = self.get_days_since_new_moon(target_date)
        
        if age < 1.8: return "New Moon"
        if age < 5.5: return "Waxing Crescent"
        if age < 9.3: return "First Quarter"
        if age < 12.8: return "Waxing Gibbous"
        if age < 16.2: return "Full Moon"
        if age < 19.5: return "Waning Gibbous"
        if age < 23.2: return "Last Quarter"
        if age < 27.5: return "Waning Crescent"
        return "New Moon"

    def get_illumination(self, target_date: datetime) -> float:
        """
        Estimate the percentage of the moon illuminated (0.0 to 1.0).
        
        :param target_date: The date to analyze.
        :return: Float representing fraction illuminated.
        """
        age = self.get_days_since_new_moon(target_date)
        # Using the cosine approximation for lunar illumination
        return (1 - math.cos(2 * math.pi * age / self.SYNODIC_MONTH)) / 2

    def is_visible(self, target_date: datetime) -> bool:
        """
        Check if the moon is generally considered 'visible' (above 5% illumination).
        
        :param target_date: The date to check.
        :return: Boolean status.
        """
        return self.get_illumination(target_date) > 0.05

    def get_lunar_summary(self, target_date: datetime) -> Dict[str, Union[str, float]]:
        """
        Returns a dictionary summary of the moon's status for a given date.
        
        :param target_date: The date to summarize.
        :return: Dictionary containing phase name, illumination, and visibility.
        """
        return {
            "date": target_date.isoformat(),
            "phase": self.get_phase_name(target_date),
            "illumination": round(self.get_illumination(target_date), 4),
            "is_visible": self.is_visible(target_date)
        }


def get_next_full_moon(start_date: datetime = None) -> datetime:
    """
    Finds the approximate next full moon relative to the provided date.
    
    :param start_date: Starting point.
    :return: Datetime of the next full moon.
    """
    if start_date is None:
        start_date = datetime.now()
    
    calc = QamarCalculator()
    age = calc.get_days_since_new_moon(start_date)
    days_to_full = (14.76 - age) % QamarCalculator.SYNODIC_MONTH
    
    return start_date + timedelta(days=days_to_full)
```