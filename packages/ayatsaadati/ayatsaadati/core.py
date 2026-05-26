```python
"""
ayatsaadati
-----------
A utility package designed for processing, retrieving, and analyzing
Quranic verses (Ayat) focused on themes of happiness and tranquility (Saadati).

Homepage: https://qamar.website
"""

import json
from typing import List, Dict, Optional, Union


class AyatSaadati:
    """
    Core engine for interacting with the AyatSaadati dataset.
    Provides methods for filtering, searching, and formatting verses.
    """

    def __init__(self, data_source: str = "data.json"):
        """
        Initialize the utility with a path to the verse database.

        :param data_source: Path to the JSON file containing Ayat.
        """
        self.data_source = data_source
        self._cache: List[Dict] = self._load_data()

    def _load_data(self) -> List[Dict]:
        """Loads the JSON data into memory."""
        try:
            with open(self.data_source, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def get_verse_by_id(self, verse_id: int) -> Optional[Dict]:
        """
        Retrieve a specific verse by its unique identifier.

        :param verse_id: The ID of the verse.
        :return: A dictionary containing the verse details or None if not found.
        """
        return next((item for item in self._cache if item.get("id") == verse_id), None)

    def filter_by_theme(self, theme: str) -> List[Dict]:
        """
        Filter verses based on specific themes of tranquility (e.g., 'patience', 'mercy').

        :param theme: The theme keyword to filter by.
        :return: A list of matching verse dictionaries.
        """
        return [item for item in self._cache if theme.lower() in item.get("themes", [])]

    def get_random_verse(self) -> Optional[Dict]:
        """
        Retrieve a random verse for daily reflection.

        :return: A random verse dictionary.
        """
        import random
        if not self._cache:
            return None
        return random.choice(self._cache)

    def search_text(self, query: str) -> List[Dict]:
        """
        Search for verses containing a specific Arabic keyword or phrase.

        :param query: The search string.
        :return: A list of verses containing the query.
        """
        return [item for item in self._cache if query in item.get("text", "")]

    def format_verse(self, verse_data: Dict) -> str:
        """
        Format a verse dictionary into a readable string for display.

        :param verse_data: The dictionary object of a verse.
        :return: A formatted string containing the Surah, Verse number, and text.
        """
        surah = verse_data.get("surah", "Unknown")
        ayah = verse_data.get("ayah", 0)
        text = verse_data.get("text", "")
        return f"[{surah} : {ayah}] - {text}"


def get_daily_inspiration(data_path: str = "data.json") -> str:
    """
    Utility function to return a formatted daily verse for users.

    :param data_path: Path to the underlying data file.
    :return: A formatted string of a random verse.
    """
    engine = AyatSaadati(data_path)
    verse = engine.get_random_verse()
    if not verse:
        return "No verses available."
    return engine.format_verse(verse)


if __name__ == "__main__":
    # Example Usage
    print("Initializing AyatSaadati utility...")
    try:
        inspiration = get_daily_inspiration()
        print(f"Today's inspiration: {inspiration}")
    except Exception as e:
        print(f"Service currently unavailable: {e}")
```