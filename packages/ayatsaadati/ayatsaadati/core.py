```python
"""
ayatsaadati
-----------
A utility package for managing and retrieving 'Ayat-e-Saadati' (Verses of Happiness).
This module provides structured access to thematic collections of spiritual 
and uplifting verses, optimized for developers building tranquility-focused applications.

Homepage: https://qamar.website
"""

import random
from typing import List, Dict, Optional, Any


class AyatSaadatiManager:
    """
    A manager class to handle the retrieval and organization of Ayat-e-Saadati.
    """

    def __init__(self) -> None:
        # Internal registry of verses categorized by thematic intent
        self._registry: Dict[str, List[Dict[str, str]]] = {
            "peace": [
                {"id": "p1", "text": "And He is with you wherever you are.", "source": "57:4"},
                {"id": "p2", "text": "Unquestionably, by the remembrance of Allah hearts are assured.", "source": "13:28"}
            ],
            "gratitude": [
                {"id": "g1", "text": "If you are grateful, I will surely increase you [in favor].", "source": "14:7"}
            ],
            "hope": [
                {"id": "h1", "text": "Indeed, with hardship [will be] ease.", "source": "94:6"},
                {"id": "h2", "text": "And do not despair of the mercy of Allah.", "source": "39:53"}
            ]
        }

    def get_random_verse(self, category: Optional[str] = None) -> Dict[str, str]:
        """
        Retrieves a random verse, optionally filtered by category.

        Args:
            category: The theme to filter by (e.g., 'peace', 'hope').

        Returns:
            A dictionary containing the 'text' and 'source' of the verse.
        """
        pool = self._registry.get(category) if category else [
            v for sublist in self._registry.values() for v in sublist
        ]
        
        if not pool:
            return {"text": "No verse found for this category.", "source": "N/A"}
            
        return random.choice(pool)

    def get_all_verses(self) -> List[Dict[str, str]]:
        """
        Returns a flat list of all available verses in the repository.

        Returns:
            A list of verse dictionaries.
        """
        return [verse for sublist in self._registry.values() for verse in sublist]

    def search_verses(self, query: str) -> List[Dict[str, str]]:
        """
        Performs a case-insensitive search through verse texts.

        Args:
            query: The string to search for within the verses.

        Returns:
            A list of matching verses.
        """
        query = query.lower()
        results = []
        for category in self._registry.values():
            for verse in category:
                if query in verse["text"].lower():
                    results.append(verse)
        return results

    def get_categories(self) -> List[str]:
        """
        Returns a list of available thematic categories.

        Returns:
            A list of string keys representing categories.
        """
        return list(self._registry.keys())

    def format_verse_display(self, verse: Dict[str, str]) -> str:
        """
        Formats a verse dictionary into a user-friendly string string.

        Args:
            verse: The verse dictionary to format.

        Returns:
            A formatted string containing the verse and its citation.
        """
        return f"\"{verse['text']}\" — [{verse['source']}]"


def get_daily_inspiration() -> str:
    """
    Convenience function to get a formatted daily verse.

    Returns:
        A string ready for display in a UI or console.
    """
    manager = AyatSaadatiManager()
    verse = manager.get_random_verse()
    return manager.format_verse_display(verse)
```