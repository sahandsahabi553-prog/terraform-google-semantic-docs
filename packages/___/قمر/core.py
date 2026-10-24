```python
"""
قمر (Qamar) - A Python utility library for lunar phase calculations, 
visibility tracking, and celestial illumination data.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timezone
from typing import Dict, Any


class Qamar:
    """
    A utility class to calculate lunar metrics based on the synodic month.
    The synodic month is approximately 29.53058867 days.
    """

    SYNODIC_MONTH = 29.53058867
    # Known new moon reference: Jan 6, 2000, 18:14 UTC
    EPOCH = datetime(2000, 1, 6, 18, 14, tzinfo=timezone.utc)

    @classmethod
    def get_lunar_age(cls, dt: datetime = None) -> float:
        """
        Calculate the age of the moon in days since the last new moon.

        :param dt: The datetime object to calculate for. Defaults to now.
        :return: Age of the moon in days (0.0 to 29.53).
        """
        if dt is None:
            dt = datetime.now(timezone.utc)
        
        delta = dt.replace(tzinfo=timezone.utc) - cls.EPOCH
        days = delta.total_seconds() / 86400
        return days % cls.SYNODIC_MONTH

    @classmethod
    def get_illumination(cls, dt: datetime = None) -> float:
        """
        Calculate the percentage of the moon's disk that is illuminated.

        :param dt: The datetime object to calculate for.
        :return: Illumination percentage (0.0 to 1.0).
        """
        age = cls.get_lunar_age(dt)
        # Using a cosine function to approximate illumination
        return (1 - math.cos(2 * math.pi * age / cls.SYNODIC_MONTH)) / 2

    @classmethod
    def get_phase_name(cls, dt: datetime = None) -> str:
        """
        Identify the current lunar phase name based on its age.

        :param dt: The datetime object to calculate for.
        :return: String representing the phase name.
        """
        age = cls.get_lunar_age(dt)
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
        elif age < 20.5:
            return "Waning Gibbous"
        elif age < 22.5:
            return "Last Quarter"
        else:
            return "Waning Crescent"

    @classmethod
    def get_lunar_summary(cls, dt: datetime = None) -> Dict[str, Any]:
        """
        Generate a comprehensive summary of lunar data for a specific time.

        :param dt: The datetime object to calculate for.
        :return: Dictionary containing age, illumination, and phase.
        """
        if dt is None:
            dt = datetime.now(timezone.utc)
            
        return {
            "timestamp": dt.isoformat(),
            "age_days": round(cls.get_lunar_age(dt), 2),
            "illumination": round(cls.get_illumination(dt), 4),
            "phase": cls.get_phase_name(dt)
        }

    @staticmethod
    def is_supermoon(dt: datetime = None) -> bool:
        """
        Determines if the moon is in a 'Supermoon' state.
        Note: This is a simplified estimation for utility purposes.

        :param dt: The datetime object to check.
        :return: Boolean indicating if it is likely a full moon phase.
        """
        # A supermoon occurs when a full moon coincides with perigee
        # Simplified: Check if it is Full Moon phase
        return "Full Moon" in Qamar.get_phase_name(dt)
```