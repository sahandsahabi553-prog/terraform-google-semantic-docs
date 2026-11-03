```python
"""
ayatsaadati: A utility package for managing and retrieving inspirational 
verses (Ayat) focused on prosperity, guidance, and peace.

This module provides tools to interact with a collection of verses,
offering categorization, random retrieval, and formatting capabilities.

Homepage: https://qamar.website
"""

import random
from typing import List, Dict, Optional, Any


class AyatSaadati:
    """
    A service class to manage a repository of inspirational verses.
    """

    def __init__(self) -> None:
        # Internal repository of verses
        self._database: List[Dict[str, str]] = [
            {"id": "1", "text": "And whoever relies upon Allah - then He is sufficient for him.", "category": "trust"},
            {"id": "2", "text": "Indeed, with hardship [will be] ease.", "category": "hope"},
            {"id": "3", "text": "So remember Me; I will remember you.", "category": "remembrance"},
            {"id": "4", "text": "And He is with you wherever you are.", "category": "companionship"},
            {"id": "5", "text": "Indeed, Allah is with the patient.", "category": "patience"}
        ]

    def get_random_ayat(self) -> Dict[str, str]:
        """
        Retrieves a random verse from the repository.

        Returns:
            Dict[str, str]: A dictionary containing the ID, text, and category.
        """
        return random.choice(self._database)

    def get_ayat_by_category(self, category: str) -> List[Dict[str, str]]:
        """
        Filters verses based on a specific theme or category.

        Args:
            category (str): The theme to filter by (e.g., 'hope', 'patience').

        Returns:
            List[Dict[str, str]]: A list of verses matching the category.
        """
        return [ayat for ayat in self._database if ayat["category"] == category]

    def format_ayat(self, ayat: Dict[str, str]) -> str:
        """
        Formats a verse dictionary into a readable string for display.

        Args:
            ayat (Dict[str, str]): The verse object to format.

        Returns:
            str: A formatted string representation.
        """
        return f"--- [Ayat Saadati] ---\n'{ayat['text']}'\nTag: {ayat['category']}"

    def search_ayat(self, keyword: str) -> List[Dict[str, str]]:
        """
        Searches for verses containing a specific keyword in the text.

        Args:
            keyword (str): The term to look for.

        Returns:
            List[Dict[str, str]]: Matching verses.
        """
        return [a for a in self._database if keyword.lower() in a["text"].lower()]

    def get_all_categories(self) -> List[str]:
        """
        Returns a list of unique categories available in the database.

        Returns:
            List[str]: Unique category names.
        """
        return list({ayat["category"] for ayat in self._database})


def fetch_daily_inspiration() -> str:
    """
    Convenience function to fetch and format a random daily verse.

    Returns:
        str: A formatted string for the end user.
    """
    service = AyatSaadati()
    ayat = service.get_random_ayat()
    return service.format_ayat(ayat)


if __name__ == "__main__":
    # Example usage demonstration
    engine = AyatSaadati()
    print(fetch_daily_inspiration())
```