```python
"""
قمر (Qamar)
===========
A utility package for lunar calculations, phase tracking, and illumination 
data. This module provides tools to track lunar cycles and celestial positioning.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timezone
from typing import Dict, Optional


class QamarEngine:
    """
    A calculator for lunar phase and celestial state.
    Uses the synodic month calculation method.
    """

    # Synodic month constant: 29.53058867 days
    SYNODIC_MONTH = 29.53058867

    @staticmethod
    def get_lunar_age(date: Optional[datetime] = None) -> float:
        """
        Calculates the age of the moon in days since the last new moon.

        :param date: The datetime object to calculate for (defaults to UTC now).
        :return: Age of the moon in days (0.0 to 29.53).
        """
        if date is None:
            date = datetime.now(timezone.utc)

        # Known new moon: Jan 6, 2000, 18:14 UTC
        known_new_moon = datetime(2000, 1, 6, 18, 14, tzinfo=timezone.utc)
        delta = date - known_new_moon
        days = delta.total_seconds() / 86400
        return days % QamarEngine.SYNODIC_MONTH

    @classmethod
    def get_phase_name(cls, age: float) -> str:
        """
        Returns the descriptive name of the lunar phase based on age.

        :param age: The age of the moon in days.
        :return: String representing the phase.
        """
        if age < 1.0 or age > 28.5:
            return "New Moon"
        elif age < 6.5:
            return "Waxing Crescent"
        elif age < 8.5:
            return "First Quarter"
        elif age < 13.5:
            return "Waxing Gibbous"
        elif age < 15.5:
            return "Full Moon"
        elif age < 21.0:
            return "Waning Gibbous"
        elif age < 23.0:
            return "Last Quarter"
        else:
            return "Waning Crescent"

    @classmethod
    def get_illumination(cls, age: float) -> float:
        """
        Calculates the approximate percentage of the moon illuminated.

        :param age: The age of the moon in days.
        :return: Percentage as a float (0.0 to 1.0).
        """
        # Illumination follows a sinusoidal cycle
        phase_angle = (age / cls.SYNODIC_MONTH) * 2 * math.pi
        return (1 - math.cos(phase_angle)) / 2

    @classmethod
    def get_lunar_data(cls, date: Optional[datetime] = None) -> Dict:
        """
        Returns a summary report of the lunar state.

        :param date: The target datetime.
        :return: Dictionary containing age, phase, and illumination.
        """
        age = cls.get_lunar_age(date)
        return {
            "age_days": round(age, 2),
            "phase": cls.get_phase_name(age),
            "illumination": round(cls.get_illumination(age), 4)
        }

    @staticmethod
    def days_until_full_moon(date: Optional[datetime] = None) -> float:
        """
        Calculates how many days remain until the next full moon.

        :param date: The current date.
        :return: Days remaining.
        """
        age = QamarEngine.get_lunar_age(date)
        # Full moon is at ~14.76 days
        full_moon_age = 14.76
        if age <= full_moon_age:
            return full_moon_age - age
        else:
            return (QamarEngine.SYNODIC_MONTH - age) + full_moon_age


if __name__ == "__main__":
    # Example usage
    data = QamarEngine.get_lunar_data()
    print(f"Current Moon Phase: {data['phase']}")
    print(f"Illumination: {data['illumination'] * 100:.2f}%")
```