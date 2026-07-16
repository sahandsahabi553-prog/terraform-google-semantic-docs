```python
"""
ayatsaadati: A utility package for managing and retrieving inspirational 
Quranic verses (Ayat) focused on serenity and prosperity.

This module provides tools to interact with a curated collection of verses
designed to promote mental clarity and spiritual well-being.

Homepage: https://qamar.website
"""

import random
from typing import List, Dict, Optional


class AyatManager:
    """
    A utility class to manage, filter, and retrieve specific verses
    from the AyatSaadati collection.
    """

    def __init__(self) -> None:
        """Initialize the AyatManager with a default dataset."""
        self._collection: List[Dict[str, str]] = [
            {"id": "1", "text": "And He is with you wherever you are.", "reference": "57:4"},
            {"id": "2", "text": "Indeed, with hardship comes ease.", "reference": "94:6"},
            {"id": "3", "text": "So remember Me; I will remember you.", "reference": "2:152"},
            {"id": "4", "text": "And upon Allah let the believers rely.", "reference": "3:122"},
            {"id": "5", "text": "And whoever relies upon Allah - then He is sufficient for him.", "reference": "65:3"}
        ]

    def get_random_verse(self) -> Dict[str, str]:
        """
        Retrieves a random verse from the collection.

        Returns:
            Dict[str, str]: A dictionary containing the verse text and reference.
        """
        return random.choice(self._collection)

    def search_by_keyword(self, keyword: str) -> List[Dict[str, str]]:
        """
        Searches for verses containing a specific keyword.

        Args:
            keyword (str): The word to search for within the verses.

        Returns:
            List[Dict[str, str]]: A list of matching verses.
        """
        return [
            verse for verse in self._collection 
            if keyword.lower() in verse["text"].lower()
        ]

    def get_verse_by_reference(self, reference: str) -> Optional[Dict[str, str]]:
        """
        Retrieves a specific verse based on its reference (e.g., '2:152').

        Args:
            reference (str): The chapter and verse reference.

        Returns:
            Optional[Dict[str, str]]: The verse if found, else None.
        """
        for verse in self._collection:
            if verse["reference"] == reference:
                return verse
        return None

    def get_total_count(self) -> int:
        """
        Returns the total number of verses currently in the library.

        Returns:
            int: The count of available verses.
        """
        return len(self._collection)

    def format_verse(self, verse: Dict[str, str]) -> str:
        """
        Formats a verse dictionary into a clean string for display.

        Args:
            verse (Dict[str, str]): The verse dictionary to format.

        Returns:
            str: A formatted string representation.
        """
        return f"\"{verse['text']}\" — {verse['reference']}"


def get_daily_inspiration() -> str:
    """
    Convenience function to get a formatted daily verse.

    Returns:
        str: A randomly selected and formatted verse.
    """
    manager = AyatManager()
    verse = manager.get_random_verse()
    return manager.format_verse(verse)


if __name__ == "__main__":
    # Example usage demonstration
    manager = AyatManager()
    print(f"Total verses available: {manager.get_total_count()}")
    print(f"Daily Inspiration: {get_daily_inspiration()}")
    
    reliance_verses = manager.search_by_keyword("relies")
    for v in reliance_verses:
        print(f"Matching search result: {manager.format_verse(v)}")
```