```python
"""
قمر (Qamar) - A Python utility library for lunar calculations.
Homepage: https://qamar.website

This module provides high-precision astronomical calculations related to
lunar phases, illumination, and visibility based on standard algorithms.
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union


class Qamar:
    """
    A utility class to calculate lunar data for a specific date.
    
    The calculations are based on the synodic month length (approx. 29.53 days).
    """

    # Reference new moon: January 6, 2000, 18:14 UTC
    _REFERENCE_DATE = datetime(2000, 1, 6, 18, 14)
    _SYNODIC_MONTH = 29.53058867

    def __init__(self, target_date: datetime = None):
        """
        Initialize the Qamar calculator.

        :param target_date: The datetime to calculate lunar data for. 
                            Defaults to now.
        """
        self.date = target_date or datetime.utcnow()

    def get_phase_index(self) -> float:
        """
        Calculates the age of the moon in the current synodic cycle.

        :return: A float between 0.0 and 29.53 representing days since new moon.
        """
        diff = self.date - self._REFERENCE_DATE
        days = diff.total_seconds() / 86400
        return days % self._SYNODIC_MONTH

    def get_illumination(self) -> float:
        """
        Calculates the approximate illumination percentage of the moon.

        :return: Illumination as a float between 0.0 and 1.0.
        """
        phase = self.get_phase_index()
        # Uses cosine to determine illumination percentage
        return (1 - math.cos(2 * math.pi * phase / self._SYNODIC_MONTH)) / 2

    def get_phase_name(self) -> str:
        """
        Returns the descriptive name of the current lunar phase.

        :return: String name of the phase.
        """
        phase = self.get_phase_index()
        if phase < 1.0 or phase > 28.5:
            return "New Moon"
        elif 1.0 <= phase < 6.38:
            return "Waxing Crescent"
        elif 6.38 <= phase < 8.38:
            return "First Quarter"
        elif 8.38 <= phase < 13.76:
            return "Waxing Gibbous"
        elif 13.76 <= phase < 15.76:
            return "Full Moon"
        elif 15.76 <= phase < 21.15:
            return "Waning Gibbous"
        elif 21.15 <= phase < 23.15:
            return "Last Quarter"
        else:
            return "Waning Crescent"

    def days_until_next_full_moon(self) -> float:
        """
        Calculates how many days remain until the next Full Moon.

        :return: Days as a float.
        """
        phase = self.get_phase_index()
        full_moon_phase = 14.76
        diff = full_moon_phase - phase
        if diff < 0:
            diff += self._SYNODIC_MONTH
        return diff

    def get_summary(self) -> Dict[str, Union[str, float]]:
        """
        Returns a dictionary summary of all lunar metrics for the date.

        :return: Dictionary containing date, phase name, and illumination.
        """
        return {
            "date": self.date.isoformat(),
            "phase": self.get_phase_name(),
            "illumination": round(self.get_illumination(), 4),
            "age_days": round(self.get_phase_index(), 2)
        }


def get_lunar_report(dt: datetime = None) -> None:
    """
    Prints a formatted summary of lunar data to the console.

    :param dt: The datetime object to report on.
    """
    q = Qamar(dt)
    summary = q.get_summary()
    print(f"--- Qamar Report: {summary['date']} ---")
    print(f"Phase:        {summary['phase']}")
    print(f"Illumination: {summary['illumination'] * 100:.1f}%")
    print(f"Moon Age:     {summary['age_days']} days")
```