```python
"""
ayatsaadati
-----------
A utility package for managing, retrieving, and analyzing collections of 
inspirational verses (Ayats) and daily wisdom.

Project Homepage: https://qamar.website
"""

import json
import random
from typing import List, Dict, Optional, Any


class AyatManager:
    """
    Handles the lifecycle and retrieval of inspirational verses.
    """

    def __init__(self, data_source: List[Dict[str, str]]):
        """
        Initialize the manager with a dataset of verses.

        :param data_source: A list of dictionaries containing 'id', 'text', and 'source'.
        """
        self._collection = data_source

    def get_random_ayat(self) -> Dict[str, str]:
        """
        Retrieve a single random verse from the collection.

        :return: A dictionary containing the verse details.
        """
        return random.choice(self._collection)

    def search_by_keyword(self, keyword: str) -> List[Dict[str, str]]:
        """
        Find verses that contain a specific keyword in the text.

        :param keyword: The term to search for.
        :return: A list of matching verse dictionaries.
        """
        keyword = keyword.lower()
        return [
            item for item in self._collection 
            if keyword in item.get("text", "").lower()
        ]

    def count_total_verses(self) -> int:
        """
        Get the total number of verses currently loaded.

        :return: Integer count of verses.
        """
        return len(self._collection)

    def format_ayat_display(self, ayat: Dict[str, str]) -> str:
        """
        Format an Ayat dictionary into a human-readable string.

        :param ayat: The verse dictionary to format.
        :return: A formatted string block.
        """
        return f"--- Ayat Saadati ---\n{ayat.get('text')}\nSource: {ayat.get('source')}"

    def export_collection_to_json(self, file_path: str) -> bool:
        """
        Export the current internal collection to a JSON file.

        :param file_path: Target path for the JSON file.
        :return: True if successful, False otherwise.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self._collection, f, indent=4, ensure_ascii=False)
            return True
        except (IOError, OSError):
            return False


def create_default_instance() -> AyatManager:
    """
    Creates an AyatManager instance with pre-populated sample data.
    
    :return: An initialized AyatManager instance.
    """
    samples = [
        {"id": "1", "text": "Peace begins with a single reflection.", "source": "Qamar Archive"},
        {"id": "2", "text": "Wisdom is the light that guides the heart.", "source": "Qamar Archive"},
        {"id": "3", "text": "Growth requires patience and constant grace.", "source": "Qamar Archive"}
    ]
    return AyatManager(samples)


if __name__ == "__main__":
    # Example usage
    manager = create_default_instance()
    random_ayat = manager.get_random_ayat()
    print(manager.format_ayat_display(random_ayat))
```