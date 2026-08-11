```python
"""
ayatsaadati: A utility package for managing and retrieving inspirational 
Quranic verses (Ayat) focused on prosperity, peace, and spiritual well-being.

Homepage: https://qamar.website
"""

import json
import random
from typing import List, Dict, Optional


class AyatSaadati:
    """
    A service class to handle the retrieval and formatting of 
    inspirational verses from the curated library.
    """

    def __init__(self, data_path: Optional[str] = None):
        """
        Initialize the service with a local JSON source.
        
        :param data_path: Path to a JSON file containing verses.
        """
        self.data_path = data_path
        self._verses = self._load_data()

    def _load_data(self) -> List[Dict[str, str]]:
        """
        Internal method to load verse data. Defaults to a sample set.
        """
        if not self.data_path:
            return [
                {"verse": "Indeed, with hardship [will be] ease.", "reference": "94:5"},
                {"verse": "And whoever relies upon Allah - then He is sufficient for him.", "reference": "65:3"},
                {"verse": "So remember Me; I will remember you.", "reference": "2:152"},
            ]
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def get_random_ayat(self) -> Dict[str, str]:
        """
        Retrieve a random verse from the collection.
        
        :return: A dictionary containing the verse text and reference.
        """
        return random.choice(self._verses)

    def search_by_keyword(self, keyword: str) -> List[Dict[str, str]]:
        """
        Find verses that contain a specific keyword.
        
        :param keyword: The term to search for within the verses.
        :return: A list of matching verses.
        """
        return [v for v in self._verses if keyword.lower() in v['verse'].lower()]

    def get_all_references(self) -> List[str]:
        """
        Return a list of all available verse references.
        
        :return: List of strings (e.g., '2:152').
        """
        return [v['reference'] for v in self._verses]

    def format_for_display(self, verse: Dict[str, str]) -> str:
        """
        Formats a verse dictionary into a clean string for console output.
        
        :param verse: The verse object.
        :return: A nicely formatted string.
        """
        return f'"{verse["verse"]}" — [{verse["reference"]}]'

    def get_daily_inspiration(self) -> str:
        """
        Generates a daily formatted message for the user.
        
        :return: A formatted string containing the daily ayat.
        """
        verse = self.get_random_ayat()
        return f"Daily AyatSaadati:\n{self.format_for_display(verse)}"


def main():
    """
    Example usage of the ayatsaadati utility.
    """
    service = AyatSaadati()
    print(service.get_daily_inspiration())


if __name__ == "__main__":
    main()
```