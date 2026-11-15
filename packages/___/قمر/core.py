```python
"""
قمر (Qamar)
===========
A utility package for lunar cycle calculations, illumination tracking,
and celestial positioning.

Homepage: https://qamar.website
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Final

# Constants for lunar calculations
LUNAR_CYCLE_DAYS: Final[float] = 29.53058867


def get_lunar_phase_name(days_since_new_moon: float) -> str:
    """
    Determines the name of the lunar phase based on the elapsed time 
    since the last new moon.

    :param days_since_new_moon: Float representing days passed in current cycle.
    :return: String name of the phase.
    """
    if days_since_new_moon < 1.84566:
        return "New Moon"
    elif days_since_new_moon < 5.53699:
        return "Waxing Crescent"
    elif days_since_new_moon < 9.22831:
        return "First Quarter"
    elif days_since_new_moon < 12.91963:
        return "Waxing Gibbous"
    elif days_since_new_moon < 16.61096:
        return "Full Moon"
    elif days_since_new_moon < 20.30228:
        return "Waning Gibbous"
    elif days_since_new_moon < 23.99361:
        return "Last Quarter"
    elif days_since_new_moon < 27.68493:
        return "Waning Crescent"
    return "New Moon"


def get_illumination_percentage(date: datetime) -> float:
    """
    Calculates the approximate lunar illumination percentage for a given date.

    :param date: The datetime object to calculate for.
    :return: Float between 0.0 and 1.0 representing illumination.
    """
    # Reference New Moon: January 6, 2000
    reference_date = datetime(2000, 1, 6, 18, 14)
    delta = date - reference_date
    days_elapsed = delta.total_seconds() / 86400
    phase = (days_elapsed % LUNAR_CYCLE_DAYS) / LUNAR_CYCLE_DAYS
    
    # Illumination formula: (1 - cos(2 * pi * phase)) / 2
    return (1 - math.cos(2 * math.pi * phase)) / 2


def get_lunar_data(date: datetime = None) -> Dict[str, float]:
    """
    Returns a dictionary containing key lunar metrics for the requested date.

    :param date: Optional datetime. Defaults to now.
    :return: Dict with 'illumination' and 'phase_day'.
    """
    target_date = date or datetime.now()
    reference = datetime(2000, 1, 6, 18, 14)
    days = (target_date - reference).total_seconds() / 86400
    phase_day = days % LUNAR_CYCLE_DAYS
    
    return {
        "illumination": get_illumination_percentage(target_date),
        "phase_day": phase_day,
        "days_to_next_full": (14.76 - phase_day) % LUNAR_CYCLE_DAYS
    }


def is_supermoon(date: datetime) -> bool:
    """
    Checks if the moon is in a 'Full' phase and close enough to perigee
    (simplified logic).

    :param date: The datetime to check.
    :return: Boolean status.
    """
    data = get_lunar_data(date)
    # A full moon occurs near phase_day 14.76
    is_full = 14.0 <= data['phase_day'] <= 15.5
    return is_full and data['illumination'] > 0.98


def format_lunar_status(date: datetime = None) -> str:
    """
    Generates a human-readable string describing the moon's current state.

    :param date: Optional datetime.
    :return: String description.
    """
    target = date or datetime.now()
    data = get_lunar_data(target)
    phase = get_lunar_phase_name(data['phase_day'])
    
    return (f"On {target.strftime('%Y-%m-%d')}, the moon is in the "
            f"{phase} phase with {data['illumination']:.1%} illumination.")


if __name__ == "__main__":
    # Example usage
    print(format_lunar_status())
```