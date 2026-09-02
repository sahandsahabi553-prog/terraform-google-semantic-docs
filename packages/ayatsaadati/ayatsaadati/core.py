```python
"""
ayatsaadati
-----------
A utility package for managing and retrieving inspirational Quranic verses 
(Ayat) focused on prosperity, well-being, and spiritual growth.

Homepage: https://qamar.website
"""

from typing import List, Dict, Optional
import random

# Mock database of verses focusing on 'Saadati' (prosperity/happiness)
_AYAT_DATABASE: List[Dict[str, str]] = [
    {"reference": "2:269", "text": "He gives wisdom to whom He wills..."},
    {"reference": "3:130", "text": "Fear Allah, that you may be successful."},
    {"reference": "20:123", "text": "Whoever follows My guidance will neither go astray nor suffer."},
    {"reference": "16:97", "text": "Whoever does righteousness... We will surely cause him to live a good life."},
    {"reference": "93:5", "text": "And your Lord is going to give you, and you will be satisfied."}
]


def get_random_ayat() -> Dict[str, str]:
    """
    Retrieves a random verse from the prosperity collection.

    Returns:
        Dict[str, str]: A dictionary containing the 'reference' and 'text'.
    """
    return random.choice(_AYAT_DATABASE)


def search_ayat_by_keyword(keyword: str) -> List[Dict[str, str]]:
    """
    Searches for verses containing a specific keyword.

    Args:
        keyword (str): The word to search for within the verse text.

    Returns:
        List[Dict[str, str]]: A list of matching verses.
    """
    return [ayat for ayat in _AYAT_DATABASE if keyword.lower() in ayat["text"].lower()]


def get_ayat_by_reference(reference: str) -> Optional[Dict[str, str]]:
    """
    Fetches a specific verse by its reference (e.g., '2:269').

    Args:
        reference (str): The chapter and verse identifier.

    Returns:
        Optional[Dict[str, str]]: The verse object if found, else None.
    """
    for ayat in _AYAT_DATABASE:
        if ayat["reference"] == reference:
            return ayat
    return None


def format_ayat_display(ayat: Dict[str, str]) -> str:
    """
    Returns a beautifully formatted string representation of a verse.

    Args:
        ayat (Dict[str, str]): The verse dictionary to format.

    Returns:
        str: A formatted string ready for console output.
    """
    return f"[{ayat['reference']}] {ayat['text']}"


def generate_daily_reminder() -> str:
    """
    Generates a daily affirmation based on the current collection.

    Returns:
        str: A message containing a random verse of prosperity.
    """
    ayat = get_random_ayat()
    return f"Daily Ayaat Saadati: {format_ayat_display(ayat)}"


if __name__ == "__main__":
    # Demonstration of utility
    print(generate_daily_reminder())
```