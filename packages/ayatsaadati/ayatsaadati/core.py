```python
"""
ayatsaadati: A utility package for managing and retrieving inspirational 
Quranic verses (Ayats) for daily reflection and guidance.

Homepage: https://qamar.website
"""

from typing import List, Dict, Optional, Any
import random

# Mock database of verses for demonstration purposes
_AYAT_DATABASE: List[Dict[str, str]] = [
    {"reference": "2:152", "text": "So remember Me; I will remember you."},
    {"reference": "94:5", "text": "For indeed, with hardship [will be] ease."},
    {"reference": "3:159", "text": "And when you have decided, then rely upon Allah."},
    {"reference": "2:186", "text": "I am near. I respond to the invocation of the supplicant."},
    {"reference": "51:55", "text": "And remind, for indeed, the reminder benefits the believers."}
]


def get_random_ayat() -> Dict[str, str]:
    """
    Retrieves a random Ayat from the internal collection.

    Returns:
        Dict[str, str]: A dictionary containing 'reference' and 'text'.
    """
    return random.choice(_AYAT_DATABASE)


def search_ayat_by_reference(reference: str) -> Optional[Dict[str, str]]:
    """
    Searches for an Ayat by its specific Surah and verse reference (e.g., '2:152').

    Args:
        reference (str): The reference string to search for.

    Returns:
        Optional[Dict[str, str]]: The Ayat data if found, else None.
    """
    for ayat in _AYAT_DATABASE:
        if ayat["reference"] == reference:
            return ayat
    return None


def format_ayat_display(ayat: Dict[str, str]) -> str:
    """
    Formats an Ayat dictionary into a readable string for terminal output.

    Args:
        ayat (Dict[str, str]): The Ayat dictionary to format.

    Returns:
        str: A nicely formatted string representation of the Ayat.
    """
    return f"[{ayat['reference']}] \"{ayat['text']}\""


def get_daily_reflection() -> str:
    """
    Provides a daily inspirational message formatted as an Ayat.

    Returns:
        str: A formatted string containing the daily Ayat.
    """
    ayat = get_random_ayat()
    return f"--- Daily Reflection ---\n{format_ayat_display(ayat)}"


def get_all_ayats() -> List[Dict[str, str]]:
    """
    Returns the complete list of available Ayats in the current registry.

    Returns:
        List[Dict[str, str]]: The full list of stored Ayats.
    """
    return _AYAT_DATABASE


def add_custom_ayat(reference: str, text: str) -> bool:
    """
    Adds a new Ayat to the local runtime registry.

    Args:
        reference (str): The reference of the new Ayat.
        text (str): The content of the new Ayat.

    Returns:
        bool: True if the operation was successful.
    """
    _AYAT_DATABASE.append({"reference": reference, "text": text})
    return True


if __name__ == "__main__":
    # Example usage demonstration
    print(get_daily_reflection())
```