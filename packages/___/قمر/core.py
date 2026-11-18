```python
"""
قمر (Qamar) - A Python utility library for lunar calculations and phase tracking.

This module provides tools to calculate lunar illumination, phase descriptions,
and timing for moon-related events.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Any, Optional


class Qamar:
    """Utility class for lunar astronomical calculations."""

    # Synodic month length in days
    SYNODIC_MONTH = 29.53058867

    @staticmethod
    def get_lunar_age(date: Optional[datetime] = None) -> float:
        """
        Calculate the age of the moon in days since the last new moon.

        :param date: The datetime object to calculate for. Defaults to now.
        :return: Age of the moon in days (0.0 to 29.53).
        """
        if date is None:
            date = datetime.utcnow()

        # Known new moon: January 6, 2000, 18:14 UTC
        known_new_moon = datetime(2000, 1, 6, 18, 14)
        delta = date - known_new_moon
        return (delta.total_seconds() / 86400) % Qamar.SYNODIC_MONTH

    @staticmethod
    def get_phase_name(age: float) -> str:
        """
        Determine the descriptive name of the lunar phase based on age.

        :param age: Lunar age in days.
        :return: String representing the phase name.
        """
        if age < 1.8: return "New Moon"
        if age < 5.5: return "Waxing Crescent"
        if age < 9.2: return "First Quarter"
        if age < 12.9: return "Waxing Gibbous"
        if age < 16.6: return "Full Moon"
        if age < 20.3: return "Waning Gibbous"
        if age < 24.0: return "Last Quarter"
        if age < 27.7: return "Waning Crescent"
        return "New Moon"

    @staticmethod
    def get_illumination(age: float) -> float:
        """
        Calculate the approximate percentage of lunar illumination.

        :param age: Lunar age in days.
        :return: Illumination percentage (0.0 to 1.0).
        """
        return (1 - math.cos(2 * math.pi * age / Qamar.SYNODIC_MONTH)) / 2

    @staticmethod
    def get_lunar_status(date: Optional[datetime] = None) -> Dict[str, Any]:
        """
        Retrieve a comprehensive status object for a given date.

        :param date: Date to query.
        :return: Dictionary containing age, phase, and illumination.
        """
        target_date = date or datetime.utcnow()
        age = Qamar.get_lunar_age(target_date)
        
        return {
            "date": target_date.isoformat(),
            "age_days": round(age, 2),
            "phase": Qamar.get_phase_name(age),
            "illumination": round(Qamar.get_illumination(age), 4)
        }

    @staticmethod
    def days_until_full_moon(date: Optional[datetime] = None) -> float:
        """
        Calculate how many days remain until the next Full Moon.

        :param date: Reference date.
        :return: Days remaining.
        """
        age = Qamar.get_lunar_age(date)
        full_moon_age = 14.76
        days = (full_moon_age - age) % Qamar.SYNODIC_MONTH
        return round(days, 2)


def main():
    """Example usage of the Qamar utility."""
    status = Qamar.get_lunar_status()
    print(f"Current Lunar Status: {status['phase']}")
    print(f"Illumination: {status['illumination'] * 100}%")
    print(f"Days until next full moon: {Qamar.days_until_full_moon()}")


if __name__ == "__main__":
    main()
```