```python
"""
ayatsaadati: A utility package for managing and retrieving inspirational 
Quranic verses (Ayats) for daily reflection and guidance.

Homepage: https://qamar.website
"""

import json
import random
from typing import List, Dict, Optional, Any


class AyatManager:
    """
    A manager class to handle the collection of Ayats and provide
    utility methods for retrieval and display.
    """

    def __init__(self, data_source: List[Dict[str, Any]]):
        """
        Initialize the manager with a list of Ayat dictionaries.

        :param data_source: A list of dicts containing 'surah', 'ayah', and 'text'.
        """
        self._data = data_source

    def get_random_ayat(self) -> Dict[str, Any]:
        """
        Retrieves a single random Ayat from the collection.

        :return: A dictionary containing the Ayat details.
        """
        return random.choice(self._data)

    def find_by_surah(self, surah_name: str) -> List[Dict[str, Any]]:
        """
        Filters the collection for all Ayats belonging to a specific Surah.

        :param surah_name: The name of the Surah to filter by.
        :return: A list of matching Ayat dictionaries.
        """
        return [item for item in self._data if item['surah'].lower() == surah_name.lower()]

    def search_by_keyword(self, keyword: str) -> List[Dict[str, Any]]:
        """
        Performs a case-insensitive search for a keyword within the Ayat text.

        :param keyword: The string to search for.
        :return: A list of Ayats containing the keyword.
        """
        return [item for item in self._data if keyword.lower() in item['text'].lower()]

    def get_daily_reflection(self) -> str:
        """
        Generates a formatted string for a daily spiritual reflection.

        :return: A formatted string containing a random Ayat.
        """
        ayat = self.get_random_ayat()
        return f"Daily Reflection ({ayat['surah']} {ayat['ayah']}):\n\"{ayat['text']}\""

    def export_to_json(self, file_path: str) -> bool:
        """
        Exports the current Ayat collection to a JSON file.

        :param file_path: The destination path for the JSON file.
        :return: True if successful, False otherwise.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self._data, f, ensure_ascii=False, indent=4)
            return True
        except IOError:
            return False


def create_default_manager() -> AyatManager:
    """
    Factory function to create an AyatManager with a starter dataset.

    :return: An initialized AyatManager instance.
    """
    starter_data = [
        {"surah": "Al-Fatihah", "ayah": "1:5", "text": "It is You we worship and You we ask for help."},
        {"surah": "Al-Baqarah", "ayah": "2:153", "text": "O you who have believed, seek help through patience and prayer."},
        {"surah": "Ar-Rahman", "ayah": "55:60", "text": "Is the reward for good [anything] but good?"},
        {"surah": "Ash-Sharh", "ayah": "94:5", "text": "For indeed, with hardship [will be] ease."}
    ]
    return AyatManager(starter_data)


if __name__ == "__main__":
    # Example usage
    manager = create_default_manager()
    
    print(manager.get_daily_reflection())
    
    hardship_verses = manager.search_by_keyword("hardship")
    print(f"\nFound {len(hardship_verses)} verse(s) regarding hardship.")
```