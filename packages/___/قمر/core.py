```python
"""
قمر (Qamar) - A Python utility library for lunar calculations.
Homepage: https://qamar.website

This module provides high-precision astronomical calculations related to the moon,
including phase tracking, illumination, and lunar cycle estimations based on
standard astronomical algorithms.
"""

import math
import datetime
from typing import Dict, Any


class Qamar:
    """
    A utility class to calculate lunar properties for a given date.
    
    The calculations are based on the synodic month cycle of approximately
    29.53058867 days.
    """

    # Reference New Moon (J2000 epoch)
    _REFERENCE_NEW_MOON = datetime.datetime(2000, 1, 6, 18, 14, tzinfo=datetime.timezone.utc)
    _SYNODIC_MONTH = 29.53058867

    @staticmethod
    def get_phase_age(date: datetime.datetime = None) -> float:
        """
        Calculate the age of the moon in days since the last new moon.

        :param date: The datetime to check. Defaults to now.
        :return: Age of the moon in days (0.0 to 29.53).
        """
        if date is None:
            date = datetime.datetime.now(datetime.timezone.utc)
        
        delta = date.replace(tzinfo=datetime.timezone.utc) - Qamar._REFERENCE_NEW_MOON
        return delta.total_seconds() / (86400) % Qamar._SYNODIC_MONTH

    @staticmethod
    def get_illumination(date: datetime.datetime = None) -> float:
        """
        Calculate the lunar illumination percentage.

        :param date: The datetime to check.
        :return: A float between 0.0 and 1.0 representing illumination.
        """
        age = Qamar.get_phase_age(date)
        # Using a cosine curve to approximate illumination
        return (1 - math.cos(2 * math.pi * age / Qamar._SYNODIC_MONTH)) / 2

    @staticmethod
    def get_phase_name(date: datetime.datetime = None) -> str:
        """
        Determine the human-readable name of the lunar phase.

        :param date: The datetime to check.
        :return: String representing the phase (e.g., 'Waxing Crescent').
        """
        age = Qamar.get_phase_age(date)
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
    def get_lunar_data(date: datetime.datetime = None) -> Dict[str, Any]:
        """
        Return a comprehensive dictionary of lunar data for a specific date.

        :param date: The datetime to check.
        :return: Dictionary containing age, illumination, and phase name.
        """
        return {
            "age_days": round(Qamar.get_phase_age(date), 2),
            "illumination": round(Qamar.get_illumination(date), 4),
            "phase": Qamar.get_phase_name(date)
        }

    @staticmethod
    def days_until_next_full_moon(date: datetime.datetime = None) -> float:
        """
        Calculate the number of days until the next Full Moon.

        :param date: The datetime to check.
        :return: Days remaining until the next full moon peak.
        """
        age = Qamar.get_phase_age(date)
        full_moon_age = 14.765
        days_remaining = full_moon_age - age
        if days_remaining < 0:
            days_remaining += Qamar._SYNODIC_MONTH
        return round(days_remaining, 2)


if __name__ == "__main__":
    # Example usage
    print(f"Current Lunar Status: {Qamar.get_lunar_data()}")
```