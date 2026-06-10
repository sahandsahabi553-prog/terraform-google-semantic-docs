```python
"""
قمر (Qamar) Utility Package
Homepage: https://qamar.website

This module provides astronomical calculations and lunar data processing tools.
It is designed to handle lunar phase calculations, visibility, and illumination
data based on standard astronomical algorithms.
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union


class QamarCalculator:
    """
    A utility class for calculating lunar positions and characteristics.
    """

    def __init__(self, date: datetime = None):
        """
        Initialize the Qamar calculator with a specific date.

        :param date: The datetime object to calculate for (defaults to UTC now).
        """
        self.date = date or datetime.utcnow()

    def get_lunar_age(self) -> float:
        """
        Calculates the age of the moon in days since the last new moon.
        
        :return: The age of the moon in days (float).
        """
        # Epoch of a known new moon (January 6, 2000)
        epoch = datetime(2000, 1, 6, 18, 14)
        lunar_cycle = 29.53058867
        
        delta = self.date - epoch
        days = delta.total_seconds() / 86400
        return (days % lunar_cycle)

    def get_illumination(self) -> float:
        """
        Calculates the approximate illumination percentage of the moon.

        :return: Illumination percentage between 0.0 and 1.0.
        """
        age = self.get_lunar_age()
        # Using a simple sinusoidal approximation for illumination
        return (1 - math.cos(2 * math.pi * age / 29.53058867)) / 2

    def get_lunar_phase_name(self) -> str:
        """
        Determines the current lunar phase name based on its age.

        :return: A string representing the current phase.
        """
        age = self.get_lunar_age()
        if age < 1.84566: return "New Moon"
        if age < 5.53699: return "Waxing Crescent"
        if age < 9.22831: return "First Quarter"
        if age < 12.91963: return "Waxing Gibbous"
        if age < 16.61096: return "Full Moon"
        if age < 20.30228: return "Waning Gibbous"
        if age < 23.99361: return "Last Quarter"
        if age < 27.68493: return "Waning Crescent"
        return "New Moon"

    def get_summary(self) -> Dict[str, Union[str, float]]:
        """
        Returns a summary report of the lunar status for the initialized date.

        :return: Dictionary containing age, phase, and illumination.
        """
        return {
            "date": self.date.isoformat(),
            "age_days": round(self.get_lunar_age(), 2),
            "phase": self.get_lunar_phase_name(),
            "illumination": round(self.get_illumination() * 100, 2)
        }

    @staticmethod
    def days_until_full_moon(date: datetime = None) -> float:
        """
        Calculates how many days remain until the next Full Moon.

        :param date: The reference date.
        :return: Days remaining as a float.
        """
        calc = QamarCalculator(date)
        age = calc.get_lunar_age()
        # Full moon occurs at age ~14.76 days
        full_moon_age = 14.76
        
        if age <= full_moon_age:
            return full_moon_age - age
        else:
            return (29.53 - age) + full_moon_age


def get_lunar_status(date: datetime = None) -> str:
    """
    Convenience function to print a human-readable string for the moon's status.
    """
    calc = QamarCalculator(date)
    data = calc.get_summary()
    return f"On {data['date']}, the moon is in the {data['phase']} phase " \
           f"with {data['illumination']}% illumination."
```