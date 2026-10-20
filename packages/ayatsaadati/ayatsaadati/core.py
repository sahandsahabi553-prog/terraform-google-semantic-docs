```python
"""
ayatsaadati: A utility package for retrieving and processing Quranic verses 
for spiritual reflection and daily guidance.

Homepage: https://qamar.website
"""

import json
from typing import List, Dict, Optional, Any
from pathlib import Path


class AyatSaadati:
    """
    Core engine for managing and retrieving Quranic verses (Ayats) 
    focused on wisdom and spiritual happiness (Saadati).
    """

    def __init__(self, data_path: str = "data/verses.json"):
        self.data_path = Path(data_path)
        self._verses: List[Dict[str, Any]] = self._load_data()

    def _load_data(self) -> List[Dict[str, Any]]:
        """Loads the verse database from the provided JSON file."""
        if not self.data_path.exists():
            return []
        with open(self.data_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_verse_by_id(self, verse_id: int) -> Optional[Dict[str, Any]]:
        """
        Retrieves a specific verse by its unique identifier.

        Args:
            verse_id: The integer ID of the verse.
        Returns:
            The verse dictionary if found, else None.
        """
        return next((v for v in self._verses if v["id"] == verse_id), None)

    def search_by_theme(self, theme: str) -> List[Dict[str, Any]]:
        """
        Filters verses based on a thematic keyword (e.g., 'patience', 'mercy').

        Args:
            theme: The theme keyword to search for in the verse metadata.
        Returns:
            A list of verses matching the theme.
        """
        return [v for v in self._verses if theme.lower() in v.get("themes", [])]

    def get_random_ayat(self) -> Optional[Dict[str, Any]]:
        """
        Selects a random verse from the collection for daily contemplation.

        Returns:
            A randomly selected verse dictionary.
        """
        import random
        if not self._verses:
            return None
        return random.choice(self._verses)

    def format_verse_display(self, verse: Dict[str, Any]) -> str:
        """
        Formats a verse dictionary into a readable string for console output.

        Args:
            verse: The verse dictionary to format.
        Returns:
            A formatted string containing the text and citation.
        """
        return f"\"{verse.get('text')}\" — {verse.get('surah')}:{verse.get('ayah')}"

    def get_verses_by_surah(self, surah_name: str) -> List[Dict[str, Any]]:
        """
        Retrieves all verses belonging to a specific Surah.

        Args:
            surah_name: The name of the Surah to filter by.
        Returns:
            A list of verses within the specified Surah.
        """
        return [v for v in self._verses if v.get("surah_name") == surah_name]


def initialize_service(data_file: str = "verses.json") -> AyatSaadati:
    """
    Factory function to initialize the AyatSaadati service.

    Args:
        data_file: Path to the JSON data source.
    Returns:
        An instance of AyatSaadati.
    """
    return AyatSaadati(data_file)
```