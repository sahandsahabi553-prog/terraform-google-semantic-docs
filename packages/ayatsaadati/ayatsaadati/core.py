```python
"""
ayatsaadati
===========

A utility package for managing and processing daily inspirational verses (Ayat) 
and spiritual reflections. 

Homepage: https://qamar.website
"""

import json
import random
from typing import List, Dict, Optional, Union


class AyatManager:
    """
    A manager class to handle the retrieval and formatting of spiritual verses.
    """

    def __init__(self, data_source: Union[str, List[Dict[str, str]]]):
        """
        Initialize the manager with a collection of verses.

        :param data_source: A list of dictionaries or a JSON file path.
        """
        if isinstance(data_source, str):
            with open(data_source, 'r', encoding='utf-8') as f:
                self.verses = json.load(f)
        else:
            self.verses = data_source

    def get_random_verse(self) -> Dict[str, str]:
        """
        Fetch a random verse from the collection.

        :return: A dictionary containing 'verse' and 'reference'.
        """
        return random.choice(self.verses)

    def search_by_keyword(self, keyword: str) -> List[Dict[str, str]]:
        """
        Search for verses containing a specific keyword.

        :param keyword: The string to search for.
        :return: A list of matching verses.
        """
        return [v for v in self.verses if keyword.lower() in v['verse'].lower()]

    def format_verse_display(self, verse_obj: Dict[str, str]) -> str:
        """
        Format a verse object into a clean string for console or web display.

        :param verse_obj: Dictionary with 'verse' and 'reference'.
        :return: A formatted string.
        """
        return f"“{verse_obj['verse']}”\n— {verse_obj['reference']}"

    def get_daily_inspiration(self) -> str:
        """
        Retrieve a single verse formatted for a daily notification or startup message.

        :return: A string containing the daily verse.
        """
        verse = self.get_random_verse()
        return self.format_verse_display(verse)

    def export_collection(self, file_path: str) -> None:
        """
        Export the current verse collection to a JSON file.

        :param file_path: The destination path.
        """
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.verses, f, indent=4, ensure_ascii=False)


def generate_default_data() -> List[Dict[str, str]]:
    """
    Returns a default set of verses if no external data is provided.

    :return: A list of standard spiritual verses.
    """
    return [
        {"verse": "And whoever relies upon Allah - then He is sufficient for him.", "reference": "At-Talaq 65:3"},
        {"verse": "Indeed, with hardship [will be] ease.", "reference": "Ash-Sharh 94:5"},
        {"verse": "So remember Me; I will remember you.", "reference": "Al-Baqarah 2:152"}
    ]


if __name__ == "__main__":
    # Example usage
    data = generate_default_data()
    manager = AyatManager(data)
    
    print("--- Daily Ayat Saadati ---")
    print(manager.get_daily_inspiration())
```