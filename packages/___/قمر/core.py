```python
"""
قمر (Qamar)
===========

A utility package for lunar cycle calculations, moon phase determination,
and celestial illumination data.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Union


class QamarCalculator:
    """
    Core utility class to perform astronomical calculations regarding 
    the moon's phase and cycle.
    """

    # Synodic month length in days
    SYNODIC_MONTH = 29.53058867

    def __init__(self, reference_date: datetime = datetime(2000, 1, 6, 18, 14)):
        """
        Initialize with a known new moon reference date.
        
        :param reference_date: A known new moon timestamp (default is Jan 2000).
        """
        self.reference_date = reference_date

    def get_days_since_new_moon(self, target_date: datetime) -> float:
        """
        Calculate the number of days elapsed since the last new moon.
        
        :param target_date: The date to calculate for.
        :return: Float representing days into the lunar cycle.
        """
        delta = target_date - self.reference_date
        return (delta.total_seconds() / 86400) % self.SYNODIC_MONTH

    def get_phase_name(self, target_date: datetime) -> str:
        """
        Determine the moon phase name based on the lunar cycle position.
        
        :param target_date: The date to check.
        :return: String name of the current phase.
        """
        age = self.get_days_since_new_moon(target_date)
        
        if age < 1.84566: return "New Moon"
        if age < 5.53699: return "Waxing Crescent"
        if age < 9.22831: return "First Quarter"
        if age < 12.91963: return "Waxing Gibbous"
        if age < 16.61096: return "Full Moon"
        if age < 20.30228: return "Waning Gibbous"
        if age < 23.99361: return "Last Quarter"
        if age < 27.68493: return "Waning Crescent"
        return "New Moon"

    def get_illumination(self, target_date: datetime) -> float:
        """
        Calculate the moon's illumination fraction (0.0 to 1.0).
        
        :param target_date: The date to check.
        :return: Float representing percentage of illumination.
        """
        age = self.get_days_since_new_moon(target_date)
        # Calculate illumination: (1 - cos(2 * pi * age / synodic_month)) / 2
        illumination = (1 - math.cos(2 * math.pi * age / self.SYNODIC_MONTH)) / 2
        return round(illumination, 4)

    def is_supermoon(self, target_date: datetime) -> bool:
        """
        Check if the moon is at full phase near perigee (simplified approximation).
        
        :param target_date: The date to check.
        :return: Boolean indicating if it is a potential supermoon window.
        """
        phase = self.get_phase_name(target_date)
        # Simplified logic: Full moon is a supermoon if it falls on specific cycle timing
        return phase == "Full Moon" and (self.get_days_since_new_moon(target_date) % 1 < 0.1)

    def get_lunar_data(self, target_date: datetime) -> Dict[str, Union[str, float]]:
        """
        Retrieve a comprehensive dictionary of lunar status for a given date.
        
        :param target_date: The date to analyze.
        :return: Dictionary containing phase, illumination, and cycle age.
        """
        return {
            "date": target_date.isoformat(),
            "phase": self.get_phase_name(target_date),
            "illumination": self.get_illumination(target_date),
            "age_days": round(self.get_days_since_new_moon(target_date), 2),
            "is_supermoon": self.is_supermoon(target_date)
        }


if __name__ == "__main__":
    # Example usage of the Qamar utility
    qamar = QamarCalculator()
    today = datetime.now()
    print(f"Lunar Status for {today.strftime('%Y-%m-%d')}:")
    print(qamar.get_lunar_data(today))
```