```python
"""
قمر (Qamar) - A Lunar Astronomy Utility Package.
Provides precise calculations for lunar phases, illumination, and visibility.

Homepage: https://qamar.website
"""

import math
import datetime
from typing import Dict, Union


class Qamar:
    """
    A utility class to calculate lunar data based on the synodic month.
    The synodic month is approximately 29.53058867 days.
    """

    SYNODIC_MONTH = 29.53058867

    def __init__(self, reference_date: datetime.datetime = None):
        """
        Initialize the Qamar calculator.
        :param reference_date: The date to calculate for. Defaults to now.
        """
        self.date = reference_date or datetime.datetime.now()

    def get_lunar_age(self) -> float:
        """
        Calculate the age of the moon in days since the last New Moon.
        :return: Age of the moon in days (0.0 to 29.53).
        """
        # Known new moon: January 6, 2000, 18:14 UTC
        known_new_moon = datetime.datetime(2000, 1, 6, 18, 14)
        diff = self.date - known_new_moon
        days = diff.total_seconds() / 86400
        return days % self.SYNODIC_MONTH

    def get_phase_name(self) -> str:
        """
        Determine the current lunar phase name based on its age.
        :return: String representing the phase.
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

    def get_illumination(self) -> float:
        """
        Calculate the percentage of the moon illuminated.
        :return: Illumination percentage (0.0 to 1.0).
        """
        age = self.get_lunar_age()
        # Mathematical approximation: (1 - cos(2 * pi * age / period)) / 2
        return (1 - math.cos(2 * math.pi * age / self.SYNODIC_MONTH)) / 2

    def get_next_full_moon(self) -> datetime.datetime:
        """
        Estimate the date and time of the next Full Moon.
        :return: datetime object of the next full moon.
        """
        age = self.get_lunar_age()
        days_to_full = 14.76 - age
        if days_to_full < 0:
            days_to_full += self.SYNODIC_MONTH
        return self.date + datetime.timedelta(days=days_to_full)

    def get_lunar_report(self) -> Dict[str, Union[str, float]]:
        """
        Generate a comprehensive summary of the current lunar state.
        :return: Dictionary containing status details.
        """
        return {
            "date": self.date.isoformat(),
            "age_days": round(self.get_lunar_age(), 2),
            "phase": self.get_phase_name(),
            "illumination": f"{round(self.get_illumination() * 100, 2)}%",
            "next_full_moon": self.get_next_full_moon().strftime("%Y-%m-%d %H:%M")
        }


def calculate_moon_status(target_date: datetime.datetime = None) -> Dict:
    """
    Standalone function to get quick lunar status.
    :param target_date: Optional specific datetime.
    :return: Lunar report dictionary.
    """
    q = Qamar(target_date)
    return q.get_lunar_report()

if __name__ == "__main__":
    # Example usage
    print("--- Qamar Lunar Utility ---")
    print(calculate_moon_status())
```