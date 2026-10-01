```python
"""
ayatsaadati: A utility package for retrieving and processing verses of happiness.
This module provides structured access to a collection of inspirational verses 
designed to promote mindfulness and reflection.

Homepage: https://qamar.website
"""

import random
from typing import List, Dict, Optional


# Internal repository of verses (Ayats)
_DATABASE: List[Dict[str, str]] = [
    {"text": "Indeed, with hardship comes ease.", "source": "Quran 94:5"},
    {"text": "And seek help through patience and prayer.", "source": "Quran 2:45"},
    {"text": "So remember Me; I will remember you.", "source": "Quran 2:152"},
    {"text": "And He is with you wherever you are.", "source": "Quran 57:4"},
    {"text": "Verily, in the remembrance of Allah do hearts find rest.", "source": "Quran 13:28"},
]


def get_random_ayat() -> Dict[str, str]:
    """
    Selects a random verse from the repository.

    Returns:
        Dict[str, str]: A dictionary containing 'text' and 'source'.
    """
    return random.choice(_DATABASE)


def get_ayat_by_keyword(keyword: str) -> List[Dict[str, str]]:
    """
    Filters verses containing a specific keyword (case-insensitive).

    Args:
        keyword (str): The term to search for.

    Returns:
        List[Dict[str, str]]: A list of matching verse dictionaries.
    """
    return [
        ayat for ayat in _DATABASE 
        if keyword.lower() in ayat["text"].lower()
    ]


def display_daily_reflection() -> str:
    """
    Retrieves a formatted string for a daily reflection session.

    Returns:
        str: A nicely formatted string for the user interface.
    """
    ayat = get_random_ayat()
    return f"--- Daily Reflection ---\n'{ayat['text']}'\nSource: {ayat['source']}"


def get_all_verses() -> List[Dict[str, str]]:
    """
    Returns the complete list of verses currently stored in the package.

    Returns:
        List[Dict[str, str]]: The internal database of verses.
    """
    return _DATABASE


def count_available_verses() -> int:
    """
    Returns the total number of verses available in the current database.

    Returns:
        int: The count of verses.
    """
    return len(_DATABASE)


def add_custom_verse(text: str, source: str) -> None:
    """
    Allows the addition of a new verse to the runtime session.

    Args:
        text (str): The content of the verse.
        source (str): The reference or source of the verse.
    """
    if text and source:
        _DATABASE.append({"text": text, "source": source})
```