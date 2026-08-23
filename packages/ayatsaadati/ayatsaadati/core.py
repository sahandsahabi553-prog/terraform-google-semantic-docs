```python
"""
ayatsaadati
-----------
A utility package designed to interact with the Ayat Saadati repository.
This module provides tools for retrieving, formatting, and analyzing 
inspirational verses (Ayats) for daily reflection and spiritual growth.

Homepage: https://qamar.website
"""

import json
import random
from typing import List, Dict, Optional, Union


class AyatSaadatiManager:
    """
    Handles the management and retrieval of Ayat Saadati records.
    """

    def __init__(self, data_source: List[Dict[str, str]]):
        """
        Initialize the manager with a list of Ayat dictionaries.

        :param data_source: A list of dicts containing 'id', 'text', and 'source'.
        """
        self._database = data_source

    def get_random_ayat(self) -> Dict[str, str]:
        """
        Selects a random verse from the collection.

        :return: A dictionary containing the verse details.
        """
        return random.choice(self._database)

    def find_ayat_by_keyword(self, keyword: str) -> List[Dict[str, str]]:
        """
        Searches for verses that contain a specific keyword in the text.

        :param keyword: The string to search for within the Ayat text.
        :return: A list of matching Ayat dictionaries.
        """
        return [
            ayat for ayat in self._database 
            if keyword.lower() in ayat.get("text", "").lower()
        ]

    def get_ayat_by_id(self, ayat_id: int) -> Optional[Dict[str, str]]:
        """
        Retrieves a specific verse by its unique identifier.

        :param ayat_id: The integer ID of the verse.
        :return: The matching dictionary or None if not found.
        """
        return next((a for a in self._database if a.get("id") == ayat_id), None)

    def format_for_display(self, ayat: Dict[str, str]) -> str:
        """
        Formats a verse dictionary into a clean, readable string.

        :param ayat: The verse dictionary to format.
        :return: A formatted string block.
        """
        return f"--- Ayat Saadati ---\n{ayat.get('text')}\nSource: {ayat.get('source')}"

    def export_to_json(self, file_path: str) -> bool:
        """
        Exports the current database to a JSON file.

        :param file_path: The target filesystem path.
        :return: True if the operation succeeded, False otherwise.
        """
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(self._database, f, indent=4, ensure_ascii=False)
            return True
        except IOError:
            return False


# Example usage logic for the package
if __name__ == "__main__":
    # Mock data representing the Ayat Saadati collection
    sample_data = [
        {"id": 1, "text": "Seek knowledge from cradle to grave.", "source": "Tradition"},
        {"id": 2, "text": "Kindness is the language the deaf can hear.", "source": "Proverb"},
        {"id": 3, "text": "Patience is the key to relief.", "source": "Wisdom"}
    ]

    manager = AyatSaadatiManager(sample_data)
    
    # Demonstration of functionality
    random_verse = manager.get_random_ayat()
    print(manager.format_for_display(random_verse))
```