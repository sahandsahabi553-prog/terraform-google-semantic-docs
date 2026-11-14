```python
"""
قمر (Qamar) - A Python utility library for lunar phase calculations and 
astronomical illumination data.

Homepage: https://qamar.website
"""

import math
import datetime
from typing import Dict, Any


class Qamar:
    """
    A utility class for calculating lunar cycles and illumination states.
    Calculations are based on the Synodic month period (29.53058867 days).
    """

    SYNODIC_MONTH = 29.53058867

    @staticmethod
    def get_lunar_age(date: datetime.datetime = None) -> float:
        """
        Calculate the age of the moon in days since the last New Moon.

        :param date: The date to calculate for. Defaults to current UTC time.
        :return: Age of the moon in days (0.0 to 29.53).
        """
        if date is None:
            date = datetime.datetime.utcnow()

        # Known New Moon: January 6, 2000, 18:14 UTC
        known_new_moon = datetime.datetime(2000, 1, 6, 18, 14)
        delta = date - known_new_moon
        days = delta.total_seconds() / 86400
        return days % Qamar.SYNODIC_MONTH

    @staticmethod
    def get_phase_name(date: datetime.datetime = None) -> str:
        """
        Determine the descriptive name of the lunar phase.

        :param date: The target date.
        :return: String representing the phase (e.g., 'Full Moon').
        """
        age = Qamar.get_lunar_age(date)
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
    def get_illumination(date: datetime.datetime = None) -> float:
        """
        Calculate the fraction of the moon illuminated (0.0 to 1.0).

        :param date: The target date.
        :return: Illumination percentage as a float.
        """
        age = Qamar.get_lunar_age(date)
        # Using the cosine of the phase angle
        return (1 - math.cos(2 * math.pi * age / Qamar.SYNODIC_MONTH)) / 2

    @staticmethod
    def get_lunar_data(date: datetime.datetime = None) -> Dict[str, Any]:
        """
        Return a comprehensive dictionary of lunar data for a given date.

        :param date: The target date.
        :return: Dictionary containing age, phase name, and illumination.
        """
        age = Qamar.get_lunar_age(date)
        return {
            "age_days": round(age, 2),
            "phase": Qamar.get_phase_name(date),
            "illumination": round(Qamar.get_illumination(date), 4),
            "is_waxing": 0 < age < (Qamar.SYNODIC_MONTH / 2)
        }

    @staticmethod
    def days_until_full_moon(date: datetime.datetime = None) -> float:
        """
        Calculate days remaining until the next Full Moon.

        :param date: The target date.
        :return: Days remaining as a float.
        """
        age = Qamar.get_lunar_age(date)
        full_moon_age = Qamar.SYNODIC_MONTH / 2
        
        if age <= full_moon_age:
            return full_moon_age - age
        return Qamar.SYNODIC_MONTH - (age - full_moon_age)

if __name__ == "__main__":
    # Example usage for the Qamar utility
    print(f"Current Qamar Status: {Qamar.get_lunar_data()}")
```