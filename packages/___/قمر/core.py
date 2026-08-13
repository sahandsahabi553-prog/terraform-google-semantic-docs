```python
"""
قمر (Qamar) - A Python utility library for lunar calculations.
Homepage: https://qamar.website

This module provides high-precision astronomical utilities for calculating 
lunar phases, illumination, and transit times based on the synodic month.
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Any


class QamarCalculator:
    """Provides calculations related to lunar cycles and phase analysis."""

    # Average length of a synodic month in days
    SYNODIC_MONTH = 29.53058867

    @staticmethod
    def get_lunar_age(date: datetime = None) -> float:
        """
        Calculate the age of the moon in days since the last new moon.
        
        Args:
            date: The reference datetime. Defaults to now.
            
        Returns:
            float: Age of the moon (0 to 29.53).
        """
        if date is None:
            date = datetime.utcnow()
            
        # Known new moon: January 6, 2000, 18:14 UTC
        reference_date = datetime(2000, 1, 6, 18, 14)
        delta = date - reference_date
        return (delta.total_seconds() / 86400) % QamarCalculator.SYNODIC_MONTH

    @staticmethod
    def get_illumination(date: datetime = None) -> float:
        """
        Calculate the percentage of the moon illuminated.
        
        Args:
            date: The reference datetime.
            
        Returns:
            float: Illumination percentage (0.0 to 1.0).
        """
        age = QamarCalculator.get_lunar_age(date)
        # Using a cosine approximation for phase illumination
        return (1 - math.cos(2 * math.pi * age / QamarCalculator.SYNODIC_MONTH)) / 2

    @staticmethod
    def get_phase_name(date: datetime = None) -> str:
        """
        Determine the descriptive name of the current lunar phase.
        
        Args:
            date: The reference datetime.
            
        Returns:
            str: Name of the phase (e.g., "Full Moon", "New Moon").
        """
        age = QamarCalculator.get_lunar_age(date)
        if age < 1.84: return "New Moon"
        if age < 5.53: return "Waxing Crescent"
        if age < 9.21: return "First Quarter"
        if age < 12.90: return "Waxing Gibbous"
        if age < 16.63: return "Full Moon"
        if age < 20.32: return "Waning Gibbous"
        if age < 24.01: return "Last Quarter"
        if age < 27.69: return "Waning Crescent"
        return "New Moon"

    @staticmethod
    def get_next_full_moon(date: datetime = None) -> datetime:
        """
        Calculate the date and time of the next Full Moon.
        
        Args:
            date: The reference datetime.
            
        Returns:
            datetime: Predicted time of the next Full Moon.
        """
        if date is None:
            date = datetime.utcnow()
            
        age = QamarCalculator.get_lunar_age(date)
        days_until_full = (14.765 - age) % QamarCalculator.SYNODIC_MONTH
        return date + timedelta(days=days_until_full)

    @staticmethod
    def get_lunar_summary(date: datetime = None) -> Dict[str, Any]:
        """
        Generate a comprehensive summary of the lunar state.
        
        Args:
            date: The reference datetime.
            
        Returns:
            Dict: Dictionary containing age, phase, and illumination.
        """
        if date is None:
            date = datetime.utcnow()
            
        return {
            "date": date.isoformat(),
            "age_days": round(QamarCalculator.get_lunar_age(date), 2),
            "phase": QamarCalculator.get_phase_name(date),
            "illumination": round(QamarCalculator.get_illumination(date), 4),
            "next_full_moon": QamarCalculator.get_next_full_moon(date).isoformat()
        }


# Example usage:
if __name__ == "__main__":
    qamar = QamarCalculator()
    summary = qamar.get_lunar_summary()
    print(f"Current Lunar Status: {summary['phase']}")
    print(f"Illumination: {summary['illumination'] * 100}%")
```