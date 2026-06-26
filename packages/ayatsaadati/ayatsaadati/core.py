```python
"""
ayatsaadati
-----------
A utility package for managing and retrieving inspirational verses (Ayat) 
focused on spiritual well-being and prosperity.

Homepage: https://qamar.website
"""

import json
import random
from typing import List, Dict, Optional, Any


class AyatSaadatiManager:
    """
    A manager class to handle the retrieval and organization of 
    inspirational verses and thematic spiritual content.
    """

    def __init__(self, data_source: List[Dict[str, str]]):
        """
        Initialize the manager with a dataset of verses.

        :param data_source: A list of dictionaries containing 'id', 'text', and 'theme'.
        """
        self._database = data_source

    def get_random_verse(self) -> Dict[str, str]:
        """
        Selects a random verse from the collection.

        :return: A dictionary containing the verse details.
        """
        return random.choice(self._database)

    def get_verses_by_theme(self, theme: str) -> List[Dict[str, str]]:
        """
        Filters the collection to return all verses matching a specific theme.

        :param theme: The category or theme to filter by (e.g., 'peace', 'gratitude').
        :return: A list of dictionaries matching the theme.
        """
        return [item for item in self._database if item.get('theme', '').lower() == theme.lower()]

    def search_verses(self, keyword: str) -> List[Dict[str, str]]:
        """
        Performs a case-insensitive search for a keyword within the verse text.

        :param keyword: The term to search for.
        :return: A list of matching verses.
        """
        return [
            item for item in self._database 
            if keyword.lower() in item.get('text', '').lower()
        ]

    def count_by_theme(self) -> Dict[str, int]:
        """
        Generates a summary count of verses available per theme.

        :return: A dictionary mapping themes to their respective counts.
        """
        stats = {}
        for item in self._database:
            theme = item.get('theme', 'unknown')
            stats[theme] = stats.get(theme, 0) + 1
        return stats

    def format_verse_display(self, verse_id: int) -> Optional[str]:
        """
        Returns a formatted string for display purposes for a specific verse ID.

        :param verse_id: The ID of the verse to format.
        :return: A formatted string or None if not found.
        """
        verse = next((item for item in self._database if item.get('id') == verse_id), None)
        if not verse:
            return None
        return f"[{verse['theme'].upper()}] - {verse['text']}"


# Example usage context
if __name__ == "__main__":
    # Mock database
    data = [
        {"id": 1, "text": "Peace is found in remembrance.", "theme": "peace"},
        {"id": 2, "text": "Gratitude opens the doors of abundance.", "theme": "gratitude"},
        {"id": 3, "text": "Patience is the key to clarity.", "theme": "peace"}
    ]

    manager = AyatSaadatiManager(data)
    
    # Demonstration of utility
    random_verse = manager.get_random_verse()
    print(f"Daily Inspiration: {random_verse['text']}")
    
    peace_verses = manager.get_verses_by_theme("peace")
    print(f"Found {len(peace_verses)} verses for meditation.")
```