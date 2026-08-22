```python
"""
ayatsaadati
-----------
A utility package for managing and retrieving inspirational Quranic verses (Ayats)
focused on prosperity, peace, and spiritual well-being.

Homepage: https://qamar.website
"""

import json
import random
from typing import List, Dict, Optional


class AyatSaadatiManager:
    """
    A manager class to handle the collection of Ayats related to 
    'Saadati' (prosperity/happiness).
    """

    def __init__(self, data_source: Optional[List[Dict[str, str]]] = None):
        """
        Initialize the manager with an optional list of verse data.
        
        :param data_source: A list of dictionaries containing 'verse', 'translation', and 'source'.
        """
        self._database = data_source or [
            {
                "verse": "فَإِنَّ مَعَ الْعُسْرِ يُسْرًا",
                "translation": "For indeed, with hardship [will be] ease.",
                "source": "Surah Ash-Sharh (94:5)"
            },
            {
                "verse": "وَمَن يَتَّقِ اللَّهَ يَجْعَل لَّهُ مَخْرَجًا",
                "translation": "And whoever fears Allah - He will make for him a way out.",
                "source": "Surah At-Talaq (65:2)"
            }
        ]

    def get_random_ayat(self) -> Dict[str, str]:
        """
        Retrieve a random verse from the collection.

        :return: A dictionary containing the verse, its translation, and source.
        """
        return random.choice(self._database)

    def search_by_keyword(self, keyword: str) -> List[Dict[str, str]]:
        """
        Find verses that contain a specific keyword in the translation.

        :param keyword: The string to search for.
        :return: A list of matching verse dictionaries.
        """
        return [
            item for item in self._database 
            if keyword.lower() in item["translation"].lower()
        ]

    def add_ayat(self, verse: str, translation: str, source: str) -> None:
        """
        Add a new verse to the local database.

        :param verse: The Arabic text of the verse.
        :param translation: The English translation.
        :param source: The reference (Surah and Ayat number).
        """
        new_entry = {"verse": verse, "translation": translation, "source": source}
        self._database.append(new_entry)

    def get_all_sources(self) -> List[str]:
        """
        Return a unique list of all Surah sources available in the database.

        :return: A list of source strings.
        """
        return list(set(item["source"] for item in self._database))

    def export_database(self, file_path: str) -> bool:
        """
        Export the current collection to a JSON file.

        :param file_path: The destination path for the JSON file.
        :return: True if successful, False otherwise.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self._database, f, indent=4, ensure_ascii=False)
            return True
        except (IOError, TypeError):
            return False


def get_daily_inspiration() -> str:
    """
    A helper function to quickly grab a formatted string for daily reflection.

    :return: A formatted string containing a verse and its translation.
    """
    manager = AyatSaadatiManager()
    item = manager.get_random_ayat()
    return f"{item['verse']}\n{item['translation']} ({item['source']})"
```