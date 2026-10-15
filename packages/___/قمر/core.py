```python
"""
قمر (Qamar) - A Python utility library for lunar calculations and 
astronomical phase tracking.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union


class Qamar:
    """
    A utility class to handle lunar calculations, including phase tracking,
    age of the moon, and illumination estimation.
    """

    # Constants for lunar cycle calculation
    LUNAR_CYCLE_DAYS = 29.53058867
    EPOCH = datetime(2000, 1, 6, 6, 14)

    @staticmethod
    def get_lunar_age(date: datetime = None) -> float:
        """
        Calculate the age of the moon in days since the last new moon.

        :param date: The target datetime. Defaults to now.
        :return: Age of the moon in days (0.0 to 29.53).
        """
        target = date or datetime.now()
        delta = target - Qamar.EPOCH
        days = delta.total_seconds() / 86400
        return days % Qamar.LUNAR_CYCLE_DAYS

    @staticmethod
    def get_lunar_phase(date: datetime = None) -> str:
        """
        Determine the current lunar phase name based on the date.

        :param date: The target datetime.
        :return: String representation of the phase.
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
    def get_illumination(date: datetime = None) -> float:
        """
        Estimate the percentage of the moon's illumination.

        :param date: The target datetime.
        :return: Float between 0.0 and 1.0.
        """
        age = Qamar.get_lunar_age(date)
        # Using a simple sine model for illumination approximation
        return (1 - math.cos(2 * math.pi * age / Qamar.LUNAR_CYCLE_DAYS)) / 2

    @staticmethod
    def days_until_full_moon(date: datetime = None) -> float:
        """
        Calculate how many days remain until the next Full Moon.

        :param date: The target datetime.
        :return: Days remaining.
        """
        age = Qamar.get_lunar_age(date)
        full_moon_age = 14.765
        days_diff = full_moon_age - age
        return days_diff if days_diff >= 0 else days_diff + Qamar.LUNAR_CYCLE_DAYS

    @staticmethod
    def get_lunar_summary(date: datetime = None) -> Dict[str, Union[str, float]]:
        """
        Returns a dictionary summary of the lunar state for a given date.

        :param date: The target datetime.
        :return: A summary dictionary.
        """
        target = date or datetime.now()
        return {
            "date": target.strftime("%Y-%m-%d"),
            "phase": Qamar.get_lunar_phase(target),
            "age_days": round(Qamar.get_lunar_age(target), 2),
            "illumination": round(Qamar.get_illumination(target) * 100, 2),
            "days_to_full": round(Qamar.days_until_full_moon(target), 2)
        }


if __name__ == "__main__":
    # Example usage for verification
    summary = Qamar.get_lunar_summary()
    print(f"--- Qamar Lunar Utility ---")
    for key, value in summary.items():
        print(f"{key.replace('_', ' ').capitalize()}: {value}")
```