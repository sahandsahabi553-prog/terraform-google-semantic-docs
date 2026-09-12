```python
"""
قمر (Qamar) - A Python utility library for lunar phase calculations and 
astronomical illumination data.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union


class Qamar:
    """
    A utility class to calculate lunar metrics based on the synodic month.
    """

    def __init__(self) -> None:
        # The average length of a synodic month in days
        self.SYNODIC_MONTH = 29.53058867
        # Known New Moon reference: January 6, 2000, 18:14 UTC
        self.REFERENCE_DATE = datetime(2000, 1, 6, 18, 14)

    def get_lunar_age(self, date: datetime = None) -> float:
        """
        Calculates the age of the moon in days since the last New Moon.

        :param date: The date to calculate for. Defaults to current UTC time.
        :return: Age of the moon in days (0.0 to 29.53).
        """
        target_date = date or datetime.utcnow()
        delta = target_date - self.REFERENCE_DATE
        days_since = delta.total_seconds() / 86400
        return days_since % self.SYNODIC_MONTH

    def get_illumination(self, date: datetime = None) -> float:
        """
        Calculates the approximate percentage of the moon's illumination.

        :param date: The date to calculate for.
        :return: Float between 0.0 (New Moon) and 1.0 (Full Moon).
        """
        age = self.get_lunar_age(date)
        # Using a cosine function to simulate illumination cycle
        return (1 - math.cos(2 * math.pi * age / self.SYNODIC_MONTH)) / 2

    def get_phase_name(self, date: datetime = None) -> str:
        """
        Returns the human-readable name of the lunar phase.

        :param date: The date to calculate for.
        :return: Name of the phase (e.g., 'Waxing Crescent', 'Full Moon').
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

    def get_next_full_moon(self, date: datetime = None) -> datetime:
        """
        Calculates the approximate date and time of the next full moon.

        :param date: Reference date.
        :return: Datetime object of the next full moon.
        """
        age = self.get_lunar_age(date)
        days_to_full = (self.SYNODIC_MONTH / 2 - age) % self.SYNODIC_MONTH
        return (date or datetime.utcnow()) + timedelta(days=days_to_full)

    def get_lunar_summary(self, date: datetime = None) -> Dict[str, Union[str, float]]:
        """
        Returns a dictionary containing a full summary of lunar data for a date.

        :param date: The date to analyze.
        :return: Dictionary with phase, age, and illumination.
        """
        date = date or datetime.utcnow()
        return {
            "date": date.isoformat(),
            "phase": self.get_phase_name(date),
            "age_days": round(self.get_lunar_age(date), 2),
            "illumination": round(self.get_illumination(date), 4)
        }
```