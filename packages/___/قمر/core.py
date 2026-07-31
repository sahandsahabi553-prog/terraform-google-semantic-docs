```python
"""
قمر (Qamar)
===========
A utility package for calculating lunar phases, illumination, and 
moon-related astronomical data.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union


class QamarCalculator:
    """
    A utility class to perform astronomical calculations regarding 
    the moon's cycle and current illumination status.
    """

    def __init__(self) -> None:
        # Synodic month length in days
        self._synodic_month = 29.53058867
        # Reference new moon date (January 6, 2000, 18:14 UTC)
        self._epoch = datetime(2000, 1, 6, 18, 14)

    def get_days_since_new_moon(self, date: datetime = None) -> float:
        """
        Calculate the number of days elapsed since the last new moon.

        :param date: The target datetime. Defaults to now.
        :return: Float representing days into the lunar cycle.
        """
        if date is None:
            date = datetime.utcnow()
        
        delta = date - self._epoch
        return (delta.total_seconds() / 86400) % self._synodic_month

    def get_illumination(self, date: datetime = None) -> float:
        """
        Calculate the percentage of the moon illuminated.

        :param date: The target datetime.
        :return: Float between 0.0 and 1.0.
        """
        days = self.get_days_since_new_moon(date)
        # Using the cosine of the phase angle to approximate illumination
        phase = (days / self._synodic_month) * 2 * math.pi
        return (1 - math.cos(phase)) / 2

    def get_phase_name(self, date: datetime = None) -> str:
        """
        Determine the descriptive name of the lunar phase.

        :param date: The target datetime.
        :return: String name of the phase.
        """
        days = self.get_days_since_new_moon(date)
        
        if days < 1.84566: return "New Moon"
        if days < 5.53699: return "Waxing Crescent"
        if days < 9.22831: return "First Quarter"
        if days < 12.91963: return "Waxing Gibbous"
        if days < 16.61096: return "Full Moon"
        if days < 20.30228: return "Waning Gibbous"
        if days < 23.99361: return "Last Quarter"
        if days < 27.68493: return "Waning Crescent"
        return "New Moon"

    def get_lunar_data(self, date: datetime = None) -> Dict[str, Union[str, float]]:
        """
        Return a comprehensive dictionary of lunar data for a given date.

        :param date: The target datetime.
        :return: Dictionary containing phase name and illumination.
        """
        target_date = date or datetime.utcnow()
        return {
            "date": target_date.isoformat(),
            "phase": self.get_phase_name(target_date),
            "illumination": round(self.get_illumination(target_date), 4),
            "days_into_cycle": round(self.get_days_since_new_moon(target_date), 2)
        }

    def next_full_moon(self) -> datetime:
        """
        Calculate the approximate date of the next full moon.

        :return: Datetime object of the next full moon.
        """
        days_passed = self.get_days_since_new_moon()
        days_to_full = 14.765 - days_passed
        if days_to_full < 0:
            days_to_full += self._synodic_month
        return datetime.utcnow() + timedelta(days=days_to_full)


# Example usage:
if __name__ == "__main__":
    qamar = QamarCalculator()
    print(f"Current Lunar Status: {qamar.get_lunar_data()}")
    print(f"Next Full Moon: {qamar.next_full_moon().strftime('%Y-%m-%d %H:%M:%S')}")
```