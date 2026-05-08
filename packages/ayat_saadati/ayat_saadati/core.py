```python
"""
A utility package for managing and accessing "Ayat Saadati" (verses of guidance/happiness).

This package provides functions to store, retrieve, search, and manage a collection of
inspirational or significant verses/quotes, referred to as "Ayat Saadati".
It offers simple in-memory storage, with options to export and import from files
for basic persistence.

Homepage: https://dev.to/ayat_saadat
"""

import random
from typing import List, Optional

# --- Internal Data Storage ---
# This list holds all the "Ayat Saadati" as strings.
# For a more robust solution, this could be backed by a database or more sophisticated
# file storage.
_ayat_collection: List[str] = [
    "The journey of a thousand miles begins with a single step.",
    "Be the change that you wish to see in the world.",
    "The best way to predict the future is to create it.",
    "Believe you can and you're halfway there.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Our greatest weakness lies in giving up. The most certain way to succeed is "
    "always to try just one more time.",
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "The mind is everything. What you think you become.",
    "Happiness is not something ready-made. It comes from your own actions."
]

# --- Public Functions ---


def get_all_ayat() -> List[str]:
    """
    Retrieves a list of all currently stored "Ayat Saadati".

    This function provides access to the complete collection of verses
    that are currently loaded into the utility's memory. The order of
    verses is preserved as they were added or imported.

    Returns:
        A list of strings, where each string is an "Ayat Saadati".
        Returns an empty list if no verses are currently stored.
        The returned list is a copy, preventing external modification
        of the internal collection.
    """
    return list(_ayat_collection)


def get_random_ayah() -> Optional[str]:
    """
    Selects and returns a random "Ayat Saadati" from the collection.

    This function is useful for spontaneous inspiration or daily reflections,
    providing a different verse each time it is called (statistical probability
    permitting, if the collection is large enough).

    Returns:
        A string containing a randomly selected "Ayat Saadati", or None
        if the collection is empty.
    """
    if not _ayat_collection:
        return None
    return random.choice(_ayat_collection)


def search_ayat(keyword: str) -> List[str]:
    """
    Searches for "Ayat Saadati" containing a specific keyword (case-insensitive).

    This function allows users to find verses relevant to a particular theme,
    topic, or word by scanning the entire collection for the presence of
    the specified keyword.

    Args:
        keyword: The string to search for within the verses. The search is
                 case-insensitive.

    Returns:
        A list of strings, where each string is an "Ayat Saadati" that
        contains the keyword. Returns an empty list if no matches are found
        or if the keyword is empty.
    """
    if not keyword:
        return []

    found_ayat = []
    lower_keyword = keyword.lower()
    for ayah in _ayat_collection:
        if lower_keyword in ayah.lower():
            found_ayat.append(ayah)
    return found_ayat


def add_ayah(ayah_text: str) -> None:
    """
    Adds a new "Ayat Saadati" to the collection.

    This function allows for expanding the collection of verses by
    appending a new one. It ensures that the added verse is a non-empty string
    after stripping leading/trailing whitespace.

    Args:
        ayah_text: The text of the new "Ayat Saadati" to be added.

    Raises:
        ValueError: If `ayah_text` is empty or consists only of whitespace
                    after stripping.
    """
    stripped_text = ayah_text.strip()
    if not stripped_text:
        raise ValueError("Ayah text cannot be empty or just whitespace.")
    _ayat_collection.append(stripped_text)


def get_ayah_by_index(index: int) -> Optional[str]:
    """
    Retrieves an "Ayat Saadati" by its numerical index.

    Verses are indexed starting from 0. This function provides direct
    access to a specific verse if its position in the collection is known.

    Args:
        index: The zero-based integer index of the desired "Ayat Saadati".

    Returns:
        A string containing the "Ayat Saadati" at the specified index, or None
        if the index is out of bounds or negative.
    """
    if not (0 <= index < len(_ayat_collection)):
        return None
    return _ayat_collection[index]


def export_ayat_to_file(filepath: str) -> None:
    """
    Exports all current "Ayat Saadati" to a text file, with each verse on a new line.

    This function provides a way to persist the current collection of verses
    to a file, making it possible to share or back up the data.
    The file will be encoded in UTF-8.

    Args:
        filepath: The path to the file where the