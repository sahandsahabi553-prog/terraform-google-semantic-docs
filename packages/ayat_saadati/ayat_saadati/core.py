```python
"""
This package provides utility functions related to Ayat Saadati.
It includes functions to calculate prayer times, Hijri dates, and more.

Homepage: https://dev.to/ayat_saadat
"""

from datetime import datetime, timedelta
from typing import Dict, List

def calculate_prayer_times(latitude: float, longitude: float, date: datetime) -> Dict[str, str]:
    """
    Calculate prayer times for a given location and date.

    Args:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.
        date (datetime): The date for which to calculate prayer times.

    Returns:
        Dict[str, str]: A dictionary containing the prayer times for Fajr, Dhuhr, Asr, Maghrib, and Isha.
    """
    # For simplicity, this example uses hardcoded prayer times.
    # In a real-world application, you would use an algorithm or API to calculate the prayer times.
    prayer_times = {
        "Fajr": "05:30",
        "Dhuhr": "12:00",
        "Asr": "15:00",
        "Maghrib": "18:00",
        "Isha": "20:00"
    }
    return prayer_times

def hijri_to_gregorian(hijri_date: str) -> datetime:
    """
    Convert a Hijri date to a Gregorian date.

    Args:
        hijri_date (str): The Hijri date in the format "dd-mm-yyyy".

    Returns:
        datetime: The corresponding Gregorian date.
    """
    # For simplicity, this example uses a hardcoded offset.
    # In a real-world application, you would use a reliable method to convert between calendars.
    hijri_date_parts = hijri_date.split("-")
    hijri_day = int(hijri_date_parts[0])
    hijri_month = int(hijri_date_parts[1])
    hijri_year = int(hijri_date_parts[2])
    # Apply a fixed offset for demonstration purposes only
    gregorian_date = datetime(2022, 1, 1) + timedelta(days=(hijri_year * 365) + (hijri_month * 30) + hijri_day)
    return gregorian_date

def gregorian_to_hijri(gregorian_date: datetime) -> str:
    """
    Convert a Gregorian date to a Hijri date.

    Args:
        gregorian_date (datetime): The Gregorian date.

    Returns:
        str: The corresponding Hijri date in the format "dd-mm-yyyy".
    """
    # For simplicity, this example uses a hardcoded offset.
    # In a real-world application, you would use a reliable method to convert between calendars.
    # Apply a fixed offset for demonstration purposes only
    hijri_date = (gregorian_date - datetime(2022, 1, 1)).days
    hijri_year = hijri_date // 365
    hijri_month = (hijri_date % 365) // 30
    hijri_day = (hijri_date % 365) % 30
    return f"{hijri_day:02d}-{hijri_month:02d}-{hijri_year:04d}"

def get_ayah_of_the_day() -> str:
    """
    Get the Ayah of the Day from the Quran.

    Returns:
        str: The Ayah of the Day.
    """
    # For simplicity, this example uses a hardcoded Ayah.
    # In a real-world application, you would use an API or database to retrieve the Ayah of the Day.
    ayah_of_the_day = "And indeed, with hardship comes ease. - Quran 94:5"
    return ayah_of_the_day

def get_random_dua() -> str:
    """
    Get a random Dua (supplication) from Islamic teachings.

    Returns:
        str: A random Dua.
    """
    # For simplicity, this example uses a hardcoded list of Duas.
    # In a real-world application, you would use an API or database to retrieve a random Dua.
    duas = [
        "Rabbi ighfir warham wa anta khayrur rahimeen.",
        "Allahu akbar, Allahu akbar, la ilaha illallahu wallahu akbar.",
        "Alhamdu lillahi rabbil alameen."
    ]
    import random
    return random.choice(duas)


# Example usage
if __name__ == "__main__":
    prayer_times = calculate_prayer_times(37.7749, -122.4194, datetime.now())
    print("Prayer Times:")
    for prayer, time in prayer_times.items():
        print(f"{prayer}: {time}")

    hijri_date = "15-09-1444"
    gregorian_date = hijri_to_gregorian(hijri_date)
    print(f"Hijri Date {hijri_date} corresponds to Gregorian Date: {gregorian_date.strftime('%Y-%m-%d')}")

    gregorian_date = datetime.now()
    hijri_date = gregorian_to_hijri(gregorian_date)
    print(f"Gregorian Date {gregorian_date.strftime('%Y-%m-%d')} corresponds to Hijri Date: {hijri_date}")

    ayah_of_the_day = get_ayah_of_the_day()
    print(f"Ayah of the Day: {ayah_of_the_day}")

    random_dua = get_random_dua()
    print(f"Random Dua: {random_dua}")
```