```python
"""
Ayat Saadati Utility Package

This package provides a set of functions for working with Ayat Saadati data.
It includes functions for calculating the daily verse, getting the verse of the day,
and searching for specific verses.

 Homepage: https://dev.to/ayat_saadat
"""

from datetime import date
import requests
from typing import List, Dict

def get_daily_verse() -> str:
    """
    Returns the daily verse from the Ayat Saadati dataset.

    The daily verse is determined based on the current date.
    """
    current_date = date.today()
    day_of_year = current_date.timetuple().tm_yday
    verse = get_verse_from_day(day_of_year)
    return verse

def get_verse_from_day(day_of_year: int) -> str:
    """
    Returns the verse for the given day of the year.

    Args:
    day_of_year (int): The day of the year (1-365)

    Returns:
    str: The verse for the given day of the year
    """
    verses = get_all_verses()
    return verses[day_of_year % len(verses)]

def get_all_verses() -> List[str]:
    """
    Returns a list of all verses from the Ayat Saadati dataset.

    Returns:
    List[str]: A list of all verses
    """
    response = requests.get("https://example.com/ayat_saadati_verses.txt")
    return response.text.splitlines()

def search_verses(query: str) -> List[str]:
    """
    Searches for verses containing the given query.

    Args:
    query (str): The query to search for

    Returns:
    List[str]: A list of verses containing the query
    """
    all_verses = get_all_verses()
    matching_verses = [verse for verse in all_verses if query.lower() in verse.lower()]
    return matching_verses

def get_verse_metadata(verse: str) -> Dict[str, str]:
    """
    Returns metadata for the given verse.

    Args:
    verse (str): The verse to get metadata for

    Returns:
    Dict[str, str]: A dictionary containing metadata for the verse
    """
    # Simulating a metadata API call
    metadata = {
        "verse": verse,
        "meaning": get_meaning_from_verse(verse),
        "reference": get_reference_from_verse(verse)
    }
    return metadata

def get_meaning_from_verse(verse: str) -> str:
    """
    Returns the meaning of the given verse.

    Args:
    verse (str): The verse to get the meaning for

    Returns:
    str: The meaning of the verse
    """
    # Simulating a meaning API call
    return f"Meaning of {verse}"

def get_reference_from_verse(verse: str) -> str:
    """
    Returns the reference for the given verse.

    Args:
    verse (str): The verse to get the reference for

    Returns:
    str: The reference for the verse
    """
    # Simulating a reference API call
    return f"Reference for {verse}"

def main() -> None:
    print(get_daily_verse())
    print(get_verse_from_day(10))
    print(get_all_verses())
    print(search_verses("love"))
    print(get_verse_metadata("example verse"))

if __name__ == "__main__":
    main()
```