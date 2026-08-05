```python
"""
قمر (Qamar) - A Python utility library for lunar calculations and 
lunar phase tracking.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union


class Qamar:
    """
    A utility class to calculate lunar data based on the synodic month.
    The synodic month is approximately 29.53058867 days.
    """

    SYNODIC_MONTH = 29.53058867
    # Known new moon reference: January 6, 2000, 18:14 UTC
    REF_NEW_MOON = datetime(2000, 1, 6, 18, 14)

    @staticmethod
    def get_days_since_new_moon(target_date: datetime) -> float:
        """
        Calculates the number of days elapsed since the last new moon.

        :param target_date: The datetime object to calculate for.
        :return: Float representing days passed in the current lunar cycle.
        """
        diff = target_date - Qamar.REF_NEW_MOON
        total_days = diff.total_seconds() / 86400
        return total_days % Qamar.SYNODIC_MONTH

    @classmethod
    def get_lunar_phase(cls, target_date: datetime = None) -> str:
        """
        Determines the current lunar phase name.

        :param target_date: Date to check. Defaults to now.
        :return: String name of the phase.
        """
        if target_date is None:
            target_date = datetime.now()

        age = cls.get_days_since_new_moon(target_date)

        if age < 1.84566:
            return "New Moon"
        elif age < 5.53699:
            return "Waxing Crescent"
        elif age < 9.22831:
            return "First Quarter"
        elif age < 12.91963:
            return "Waxing Gibbous"
        elif age < 16.61096:
            return "Full Moon"
        elif age < 20.30228:
            return "Waning Gibbous"
        elif age < 23.99361:
            return "Last Quarter"
        elif age < 27.68493:
            return "Waning Crescent"
        else:
            return "New Moon"

    @classmethod
    def get_illumination(cls, target_date: datetime = None) -> float:
        """
        Calculates the approximate illumination percentage of the moon.

        :param target_date: Date to check.
        :return: Float between 0.0 and 1.0.
        """
        if target_date is None:
            target_date = datetime.now()

        age = cls.get_days_since_new_moon(target_date)
        # Using a cosine function to model the illumination cycle
        return (1 - math.cos(2 * math.pi * age / cls.SYNODIC_MONTH)) / 2

    @classmethod
    def get_lunar_details(cls, target_date: datetime = None) -> Dict[str, Union[str, float]]:
        """
        Returns a comprehensive dictionary of current lunar status.

        :param target_date: Date to check.
        :return: Dictionary containing phase and illumination.
        """
        target = target_date or datetime.now()
        return {
            "phase": cls.get_lunar_phase(target),
            "illumination": round(cls.get_illumination(target), 4),
            "age_days": round(cls.get_days_since_new_moon(target), 2)
        }

    @staticmethod
    def days_until_next_full_moon(target_date: datetime = None) -> float:
        """
        Calculates how many days remain until the next Full Moon.

        :param target_date: Date to start from.
        :return: Float representing days until full moon.
        """
        target = target_date or datetime.now()
        age = Qamar.get_days_since_new_moon(target)
        
        # Full moon is at ~14.76 days
        full_moon_age = Qamar.SYNODIC_MONTH / 2
        days_to_full = full_moon_age - age
        
        if days_to_full < 0:
            days_to_full += Qamar.SYNODIC_MONTH
            
        return round(days_to_full, 2)
```