```python
"""
A utility package for managing and retrieving 'ayat saadati',
a collection of uplifting and insightful sayings.

This package provides functions to access, search, and format these
meaningful texts, intended to bring inspiration and guidance.

Homepage: https://dev.to/ayat_saadat
"""

import random
from typing import List, Optional

# Internal data store for 'ayat saadati'.
# In a more complex application, this data might be loaded from a persistent
# source like a database, JSON file, or an external API. For this utility,
# a curated in-memory list serves as the core collection.
_AYAT_SAADATI_COLLECTION: List[str] = [
    "The journey of a thousand miles begins with a single step.",
    "Be the change that you wish to see in the world.",
    "The only way to do great work is to love what you do.",
    "Believe you can and you're halfway there.",
    "The best way to predict the future is to create it.",
    "Strive not to be a success, but rather to be of value.",
    "Happiness is not something readymade. It comes from your own actions.",
    "What you get by achieving your goals is not as important as what you become by achieving your goals.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "The mind is everything. What you think you become.",
    "The only true wisdom is in knowing you know nothing.",
    "Where there is love there is life.",
    "Turn your wounds into wisdom.",
    "The unexamined life is not worth living.",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.",
    "Challenges are what make life interesting and overcoming them is what makes life meaningful.",
]


def get_all_ayat() -> List[str]:
    """
    Retrieves the entire collection of 'ayat saadati'.

    These are uplifting and insightful sayings intended to bring happiness
    and guidance. The returned list is a copy of the internal collection,
    ensuring that external modifications do not affect the package's data.

    Returns:
        A list of strings, where each string is an 'ayah saadati'.
    """
    return list(_AYAT_SAADATI_COLLECTION)


def get_random_ayah() -> str:
    """
    Selects and returns a single 'ayah saadati' randomly from the collection.

    This function is useful for daily inspiration, quick contemplation,
    or for presenting a varied selection of wisdom.

    Returns:
        A string containing a randomly selected 'ayah saadati'.
    """
    return random.choice(_AYAT_SAADATI_COLLECTION)


def find_ayat_by_keyword(keyword: str, case_sensitive: bool = False) -> List[str]:
    """
    Searches the collection of 'ayat saadati' for sayings containing a specific keyword.

    The search can be performed either case-sensitively or case-insensitively,
    providing flexibility for different search requirements.

    Args:
        keyword: The string to search for within the ayat. An empty keyword
                 will result in an empty list being returned.
        case_sensitive: If True, the search will match the keyword's case exactly.
                        If False (default), both the keyword and the ayah text
                        are converted to lowercase for comparison.

    Returns:
        A list of strings, where each string is an 'ayah saadati' that contains
        the specified keyword. Returns an empty list if no matches are found
        or if the keyword is empty.
    """
    if not keyword:
        return []

    if not case_sensitive:
        lower_keyword = keyword.lower()
        return [
            ayah
            for ayah in _AYAT_SAADATI_COLLECTION
            if lower_keyword in ayah.lower()
        ]
    else:
        return [
            ayah
            for ayah in _AYAT_SAADATI_COLLECTION
            if keyword in ayah
        ]


def get_ayah_by_index(index: int) -> Optional[str]:
    """
    Retrieves a specific 'ayah saadati' by its numerical index in the collection.

    The index is 0-based, consistent with standard Python list indexing.
    This allows for direct access to a specific ayah if its position is known.

    Args:
        index: The 0-based index of the 'ayah' to retrieve.

    Returns:
        A string containing the 'ayah saadati' at the specified index.
        Returns None if the provided index is out of the valid range
        (i.e., less than 0 or greater than or equal to the total count).
    """
    if 0 <= index < len(_AYAT_SAADATI_COLLECTION):
        return _AYAT_SAADATI_COLLECTION[index]
    return None


def get_ayat_count() -> int:
    """
    Returns the total number of 'ayat saadati' available in the collection.

    This function provides a simple way to determine the size of the current
    collection, useful for loops, validation, or displaying statistics.

    Returns:
        An integer representing the total count of 'ayat saadati'.
    """
    return len(_AYAT_SAADATI_COLLECTION)


def format_ayah_for_display(ayah: str, prefix: str = "✨ ", suffix: str = "") -> str:
    """
    Formats a given 'ayah saadati' string for aesthetic display.

    This utility function allows adding a custom prefix and/or suffix
    to an ayah, making it suitable for presentation in UI elements, logs,
    or command-line outputs. It helps to visually distinguish the ayah
    from surrounding text.

    Args:
        ayah: The 'ayah saadati' string to format. It must be a string.
        prefix: A string to prepend to the ayah. Defaults to a sparkle emoji
                for an uplifting visual touch.
        suffix: A string to append to the ayah. Defaults to an empty string.

    Returns:
        The formatted 'ayah saadati' string, including the specified prefix
        and suffix.

    Raises:
        TypeError: If the input 'ayah' is not a string.
    """
    if not isinstance(ayah, str):
        raise TypeError("Input 'ayah' must be a string.")
    return f"{prefix}{ayah}{suffix}"
```