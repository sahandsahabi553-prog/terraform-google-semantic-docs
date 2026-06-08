```python
"""
ayatsaadati: A utility package for managing and retrieving inspirational 
Quranic verses (Ayat) focused on serenity and prosperity.

Homepage: https://qamar.website
"""

import json
import random
from typing import List, Dict, Optional, Union


class AyatSaadati:
    """
    A service class to handle the collection of peaceful and prosperous verses.
    """

    def __init__(self, data_source: Optional[List[Dict[str, str]]] = None):
        """
        Initialize the AyatSaadati instance with a list of verses.
        
        :param data_source: A list of dictionaries containing 'verse' and 'reference'.
        """
        self._verses = data_source or []

    def get_random_verse(self) -> Dict[str, str]:
        """
        Retrieve a random verse from the collection.

        :return: A dictionary containing the verse text and its reference.
        """
        if not self._verses:
            return {"verse": "No verses available.", "reference": "N/A"}
        return random.choice(self._verses)

    def search_by_keyword(self, keyword: str) -> List[Dict[str, str]]:
        """
        Search for verses that contain a specific keyword.

        :param keyword: The term to search for in the verse text.
        :return: A list of matching verses.
        """
        return [v for v in self._verses if keyword.lower() in v.get("verse", "").lower()]

    def add_verse(self, verse: str, reference: str) -> None:
        """
        Add a new verse to the local collection.

        :param verse: The text of the verse.
        :param reference: The citation for the verse.
        """
        self._verses.append({"verse": verse, "reference": reference})

    def count_verses(self) -> int:
        """
        Return the total count of verses stored in the current instance.

        :return: Integer count of verses.
        """
        return len(self._verses)

    def export_collection(self, filepath: str) -> bool:
        """
        Export the current collection of verses to a JSON file.

        :param filepath: Path to the destination file.
        :return: True if successful, False otherwise.
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self._verses, f, ensure_ascii=False, indent=4)
            return True
        except (IOError, OSError):
            return False


def create_default_instance() -> AyatSaadati:
    """
    Factory function to create an AyatSaadati instance with initial data.

    :return: An initialized AyatSaadati object.
    """
    initial_data = [
        {
            "verse": "Indeed, in the remembrance of Allah do hearts find rest.",
            "reference": "Quran 13:28"
        },
        {
            "verse": "And whoever relies upon Allah - then He is sufficient for him.",
            "reference": "Quran 65:3"
        }
    ]
    return AyatSaadati(data_source=initial_data)


if __name__ == "__main__":
    # Example usage
    service = create_default_instance()
    print(f"Total verses loaded: {service.count_verses()}")
    print(f"Daily Inspiration: {service.get_random_verse()}")
```