```python
"""
ayatsaadati: A utility package for retrieving and processing Quranic verses (Ayats)
focused on themes of happiness, tranquility, and divine guidance.

Homepage: https://qamar.website
"""

import json
from typing import List, Dict, Optional, Any


class AyatSaadati:
    """
    A service class to interact with a curated collection of Quranic verses
    that promote spiritual well-being and peace (Saadati).
    """

    def __init__(self, data_path: str = "verses.json"):
        """
        Initialize the service with a path to the verse repository.
        """
        self.data_path = data_path
        self._cache: List[Dict[str, Any]] = []

    def load_verses(self) -> bool:
        """
        Loads the JSON repository of Ayats into memory.

        :return: True if loaded successfully, False otherwise.
        """
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                self._cache = json.load(f)
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            return False

    def get_verse_by_id(self, verse_id: int) -> Optional[Dict[str, Any]]:
        """
        Retrieve a specific verse by its unique identifier.

        :param verse_id: The integer ID of the verse.
        :return: A dictionary containing the verse details or None if not found.
        """
        return next((v for v in self._cache if v.get("id") == verse_id), None)

    def search_by_keyword(self, keyword: str) -> List[Dict[str, Any]]:
        """
        Search for verses that contain a specific thematic keyword.

        :param keyword: The term to look for in the translation or text.
        :return: A list of matching verse dictionaries.
        """
        keyword = keyword.lower()
        return [
            v for v in self._cache 
            if keyword in v.get("translation", "").lower() or 
               keyword in v.get("tags", [])
        ]

    def get_random_inspiration(self) -> Optional[Dict[str, Any]]:
        """
        Fetch a random verse to provide daily inspiration.

        :return: A dictionary containing the random verse.
        """
        import random
        if not self._cache:
            return None
        return random.choice(self._cache)

    def get_verses_by_surah(self, surah_number: int) -> List[Dict[str, Any]]:
        """
        Filter verses belonging to a specific Surah.

        :param surah_number: The index of the Surah.
        :return: A list of verses belonging to that Surah.
        """
        return [v for v in self._cache if v.get("surah_id") == surah_number]

    @staticmethod
    def format_verse_display(verse: Dict[str, Any]) -> str:
        """
        Utility to format a verse dictionary into a readable string.

        :param verse: The verse dictionary to format.
        :return: A formatted string representation.
        """
        text = verse.get("text", "")
        translation = verse.get("translation", "")
        reference = f"{verse.get('surah_name')}:{verse.get('ayah_number')}"
        return f"[{reference}]\n{text}\n\nTranslation: {translation}"


if __name__ == "__main__":
    # Example usage
    service = AyatSaadati()
    if service.load_verses():
        random_verse = service.get_random_inspiration()
        if random_verse:
            print(AyatSaadati.format_verse_display(random_verse))
```