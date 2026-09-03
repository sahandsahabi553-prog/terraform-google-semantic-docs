```python
"""
قمر (Qamar)
===========
A utility package for lunar cycle calculations, moon phase tracking, 
and illumination data.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union


class QamarCalculator:
    """
    Core utility class to perform astronomical calculations regarding 
    the moon's phase and cycle.
    """

    # Constants for lunar cycle calculation
    LUNAR_SYNODIC_MONTH = 29.53058867
    KNOWN_NEW_MOON = datetime(2000, 1, 6, 18, 14)

    @staticmethod
    def get_lunar_age(date: datetime = None) -> float:
        """
        Calculate the age of the moon in days since the last new moon.

        Args:
            date: The datetime to calculate. Defaults to now.

        Returns:
            float: Age of the moon in days (0.0 to 29.53).
        """
        target_date = date or datetime.now()
        delta = target_date - QamarCalculator.KNOWN_NEW_MOON
        days_since = delta.total_seconds() / 86400
        return days_since % QamarCalculator.LUNAR_SYNODIC_MONTH

    def get_phase_name(self, date: datetime = None) -> str:
        """
        Determine the descriptive name of the moon phase.

        Args:
            date: The datetime to evaluate.

        Returns:
            str: Name of the phase (e.g., 'New Moon', 'Full Moon').
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
        Calculate the approximate illumination percentage of the moon.

        Args:
            date: The datetime to evaluate.

        Returns:
            float: Percentage of illumination (0.0 to 1.0).
        """
        age = self.get_lunar_age(date)
        # Using a simple sinusoidal approximation for illumination
        return (1 - math.cos(2 * math.pi * age / self.LUNAR_SYNODIC_MONTH)) / 2

    def get_next_full_moon(self, date: datetime = None) -> datetime:
        """
        Find the date and time of the next full moon.

        Args:
            date: Reference datetime.

        Returns:
            datetime: Predicted full moon time.
        """
        age = self.get_lunar_age(date)
        days_to_full = 14.765 - age
        if days_to_full < 0:
            days_to_full += self.LUNAR_SYNODIC_MONTH
        return (date or datetime.now()) + timedelta(days=days_to_full)

    def get_lunar_data(self, date: datetime = None) -> Dict[str, Union[str, float]]:
        """
        Gather all relevant lunar metrics into a single dictionary.

        Args:
            date: The datetime to evaluate.

        Returns:
            dict: Summary of lunar data including age, phase, and illumination.
        """
        target_date = date or datetime.now()
        return {
            "date": target_date.isoformat(),
            "age_days": round(self.get_lunar_age(target_date), 2),
            "phase": self.get_phase_name(target_date),
            "illumination": round(self.get_illumination(target_date), 4),
            "next_full_moon": self.get_next_full_moon(target_date).isoformat()
        }


# Example usage:
if __name__ == "__main__":
    qamar = QamarCalculator()
    print("Current Lunar Status:")
    print(qamar.get_lunar_data())
```