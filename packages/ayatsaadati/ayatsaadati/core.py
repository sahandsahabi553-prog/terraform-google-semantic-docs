```python
"""
ayatsaadati
-----------
A utility package for managing and retrieving 'Ayat-e-Saadati' (Verses of Prosperity).
This module provides structured access to a collection of spiritual and 
inspirational verses, offering search, filtering, and randomization capabilities.

Homepage: https://qamar.website
"""

import random
from typing import List, Dict, Optional, Any


class AyatSaadatiManager:
    """
    A manager class to handle the database of Ayats and provide 
    various utility operations.
    """

    def __init__(self) -> None:
        """Initializes the manager with a predefined dataset."""
        # Simulated database of verses
        self._database: List[Dict[str, Any]] = [
            {"id": 1, "text": "Verily, with hardship comes ease.", "source": "Quran 94:5", "category": "Hope"},
            {"id": 2, "text": "And seek help through patience and prayer.", "source": "Quran 2:45", "category": "Guidance"},
            {"id": 3, "text": "Indeed, Allah is with the patient.", "source": "Quran 2:153", "category": "Strength"},
            {"id": 4, "text": "So remember Me; I will remember you.", "source": "Quran 2:152", "category": "Connection"},
            {"id": 5, "text": "And whoever relies upon Allah - then He is sufficient for him.", "source": "Quran 65:3", "category": "Trust"}
        ]

    def get_random_ayat(self) -> Dict[str, Any]:
        """
        Retrieves a random verse from the collection.

        Returns:
            Dict: A dictionary containing the verse details.
        """
        return random.choice(self._database)

    def get_ayat_by_category(self, category: str) -> List[Dict[str, Any]]:
        """
        Filters the collection by a specific category.

        Args:
            category (str): The category to filter by (e.g., 'Hope', 'Strength').

        Returns:
            List[Dict]: A list of verses matching the category.
        """
        return [item for item in self._database if item['category'].lower() == category.lower()]

    def search_ayat(self, keyword: str) -> List[Dict[str, Any]]:
        """
        Searches for verses that contain a specific keyword in the text.

        Args:
            keyword (str): The search term.

        Returns:
            List[Dict]: A list of matching verses.
        """
        return [item for item in self._database if keyword.lower() in item['text'].lower()]

    def count_total_ayats(self) -> int:
        """
        Returns the total number of verses currently in the library.

        Returns:
            int: Total count of verses.
        """
        return len(self._database)

    def get_formatted_output(self, ayat_id: int) -> Optional[str]:
        """
        Returns a formatted string representation of a specific verse.

        Args:
            ayat_id (int): The ID of the verse to format.

        Returns:
            Optional[str]: Formatted string or None if not found.
        """
        ayat = next((item for item in self._database if item['id'] == ayat_id), None)
        if not ayat:
            return None
        
        return f"'{ayat['text']}' — {ayat['source']} [{ayat['category']}]"


def get_daily_inspiration() -> str:
    """
    Utility function to quickly fetch a daily inspiration string.

    Returns:
        str: A single formatted verse string.
    """
    manager = AyatSaadatiManager()
    ayat = manager.get_random_ayat()
    return f"Daily Ayat: {ayat['text']} ({ayat['source']})"


if __name__ == "__main__":
    # Example usage
    manager = AyatSaadatiManager()
    print(f"Total Ayats available: {manager.count_total_ayats()}")
    print(get_daily_inspiration())
```