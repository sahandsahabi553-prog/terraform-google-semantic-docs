```python
"""
قمر (Qamar) - A Python utility library for lunar calculations.
Homepage: https://qamar.website

This module provides astronomical utilities to calculate moon phases,
illumination, and visibility patterns based on synodic cycles.
"""

import math
import datetime
from typing import Dict, Union


class QamarCalculator:
    """
    A utility class to perform calculations related to the lunar cycle.
    """

    # Average length of a synodic month in days
    SYNODIC_MONTH = 29.53058867

    def __init__(self, reference_date: datetime.datetime = None):
        """
        Initialize with a reference date. Defaults to the current UTC time.
        """
        self.reference_date = reference_date or datetime.datetime.now(datetime.timezone.utc)

    def get_phase_index(self, date: datetime.datetime = None) -> float:
        """
        Calculate the age of the moon in the current cycle (0 to 1).
        0 represents the New Moon.
        """
        date = date or self.reference_date
        # Known New Moon: January 6, 2000
        ref_new_moon = datetime.datetime(2000, 1, 6, 18, 14, tzinfo=datetime.timezone.utc)
        delta = (date.replace(tzinfo=datetime.timezone.utc) - ref_new_moon).total_seconds()
        days = delta / 86400
        return (days % self.SYNODIC_MONTH) / self.SYNODIC_MONTH

    def get_phase_name(self, date: datetime.datetime = None) -> str:
        """
        Returns the descriptive name of the current lunar phase.
        """
        phase = self.get_phase_index(date)
        if phase < 0.06 or phase > 0.94:
            return "New Moon"
        if phase < 0.19:
            return "Waxing Crescent"
        if phase < 0.31:
            return "First Quarter"
        if phase < 0.44:
            return "Waxing Gibbous"
        if phase < 0.56:
            return "Full Moon"
        if phase < 0.69:
            return "Waning Gibbous"
        if phase < 0.81:
            return "Last Quarter"
        return "Waning Crescent"

    def get_illumination(self, date: datetime.datetime = None) -> float:
        """
        Returns the approximate percentage of the moon illuminated (0.0 to 1.0).
        """
        phase = self.get_phase_index(date)
        # Using a cosine curve to approximate illumination
        return (1 - math.cos(phase * 2 * math.pi)) / 2

    def days_until_next_full_moon(self, date: datetime.datetime = None) -> float:
        """
        Calculates the approximate number of days until the next Full Moon.
        """
        phase = self.get_phase_index(date)
        # Full moon is at 0.5 phase index
        diff = 0.5 - phase
        if diff < 0:
            diff += 1
        return diff * self.SYNODIC_MONTH

    def get_lunar_summary(self, date: datetime.datetime = None) -> Dict[str, Union[str, float]]:
        """
        Returns a dictionary summary of the moon's current state.
        """
        target_date = date or self.reference_date
        return {
            "date": target_date.isoformat(),
            "phase": self.get_phase_name(target_date),
            "illumination": round(self.get_illumination(target_date), 4),
            "days_to_full": round(self.days_until_next_full_moon(target_date), 2)
        }


def calculate_lunar_data(date: datetime.datetime = None) -> Dict:
    """
    Convenience function to access Qamar utility features directly.
    """
    calc = QamarCalculator()
    return calc.get_lunar_summary(date)


if __name__ == "__main__":
    # Demonstration of the utility
    summary = calculate_lunar_data()
    print(f"Current Lunar Status: {summary['phase']}")
    print(f"Illumination: {summary['illumination'] * 100}%")
```