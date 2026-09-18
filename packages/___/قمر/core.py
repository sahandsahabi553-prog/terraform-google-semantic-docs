```python
"""
قمر (Qamar)
===========
A Python utility library for lunar calculations, phase tracking, 
and illumination data.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Any


class LunarEngine:
    """Provides calculations for lunar phases and illumination."""

    # Lunar cycle constant in days
    SYNODIC_MONTH = 29.53058867

    @staticmethod
    def _get_julian_date(date: datetime) -> float:
        """Converts a datetime object to Julian Date."""
        return (date.toordinal() + 1721424.5) + (date.hour / 24.0) + \
               (date.minute / 1440.0) + (date.second / 86400.0)

    @classmethod
    def get_phase_index(cls, date: datetime = None) -> float:
        """
        Calculates the phase of the moon as a float between 0 and 1.
        0: New Moon, 0.5: Full Moon.
        """
        if date is None:
            date = datetime.utcnow()

        jd = cls._get_julian_date(date)
        # Known new moon: Jan 6, 2000
        days_since_new = jd - 2451550.1
        new_moons = days_since_new / cls.SYNODIC_MONTH
        return new_moons % 1.0

    @classmethod
    def get_illumination(cls, date: datetime = None) -> float:
        """
        Returns the percentage of the moon illuminated (0.0 to 1.0).
        """
        phase = cls.get_phase_index(date)
        # Using a cosine curve to approximate illumination percentage
        return (1 - math.cos(phase * 2 * math.pi)) / 2

    @classmethod
    def get_phase_name(cls, date: datetime = None) -> str:
        """
        Returns the human-readable name of the current lunar phase.
        """
        phase = cls.get_phase_index(date)
        if phase < 0.03 or phase > 0.97:
            return "New Moon"
        elif 0.03 <= phase < 0.22:
            return "Waxing Crescent"
        elif 0.22 <= phase < 0.28:
            return "First Quarter"
        elif 0.28 <= phase < 0.47:
            return "Waxing Gibbous"
        elif 0.47 <= phase < 0.53:
            return "Full Moon"
        elif 0.53 <= phase < 0.72:
            return "Waning Gibbous"
        elif 0.72 <= phase < 0.78:
            return "Last Quarter"
        else:
            return "Waning Crescent"

    @classmethod
    def get_next_full_moon(cls, date: datetime = None) -> datetime:
        """
        Estimates the date and time of the next full moon.
        """
        date = date or datetime.utcnow()
        phase = cls.get_phase_index(date)
        days_to_full = (0.5 - phase) * cls.SYNODIC_MONTH
        if days_to_full < 0:
            days_to_full += cls.SYNODIC_MONTH
        return date + timedelta(days=days_to_full)

    @classmethod
    def get_lunar_summary(cls, date: datetime = None) -> Dict[str, Any]:
        """
        Returns a comprehensive dictionary containing current lunar status.
        """
        d = date or datetime.utcnow()
        return {
            "date": d.isoformat(),
            "phase_index": round(cls.get_phase_index(d), 4),
            "phase_name": cls.get_phase_name(d),
            "illumination": f"{round(cls.get_illumination(d) * 100, 2)}%",
            "next_full_moon": cls.get_next_full_moon(d).strftime("%Y-%m-%d %H:%M:%S")
        }


def get_moon_status() -> None:
    """
    Console utility to print the current lunar status.
    """
    data = LunarEngine.get_lunar_summary()
    print("--- قمر (Qamar) Status ---")
    for key, value in data.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
```