```python
"""
ayatsaadati
-----------
A utility package for managing and retrieving inspirational verses (Ayat) 
focused on spiritual well-being and prosperity.

Homepage: https://qamar.website
"""

import json
import random
from typing import List, Dict, Optional, Any


class AyatManager:
    """
    Core class to handle the retrieval, filtering, and formatting of 
    inspirational verses from the repository.
    """

    def __init__(self, data_source: List[Dict[str, str]]):
        """
        Initialize the manager with a dataset of verses.

        :param data_source: A list of dictionaries containing 'verse' and 'topic'.
        """
        self._data = data_source

    def get_random_verse(self) -> Dict[str, str]:
        """
        Retrieves a single random verse from the collection.

        :return: A dictionary containing the verse text and its metadata.
        """
        return random.choice(self._data)

    def filter_by_topic(self, topic: str) -> List[Dict[str, str]]:
        """
        Filters the collection to return verses related to a specific theme.

        :param topic: The category/topic to filter by (e.g., 'patience', 'gratitude').
        :return: A list of verses matching the criteria.
        """
        return [item for item in self._data if item.get("topic", "").lower() == topic.lower()]

    def search_verse(self, keyword: str) -> List[Dict[str, str]]:
        """
        Performs a keyword search across the verse text.

        :param keyword: The term to search for within the verse content.
        :return: A list of matching verses.
        """
        return [item for item in self._data if keyword.lower() in item.get("verse", "").lower()]

    def get_daily_inspiration(self) -> str:
        """
        Generates a formatted string for a daily inspirational message.

        :return: A cleanly formatted string for display.
        """
        verse_data = self.get_random_verse()
        return f"Daily Ayat: '{verse_data['verse']}' \nTopic: {verse_data['topic']}"

    def export_to_json(self, file_path: str) -> bool:
        """
        Exports the current dataset to a local JSON file.

        :param file_path: The filesystem path where the data should be saved.
        :return: True if successful, False otherwise.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self._data, f, indent=4, ensure_ascii=False)
            return True
        except (IOError, TypeError):
            return False


def initialize_default_manager() -> AyatManager:
    """
    Factory function to initialize the AyatManager with default content.

    :return: An initialized AyatManager instance.
    """
    default_data = [
        {"verse": "Indeed, with hardship comes ease.", "topic": "patience"},
        {"verse": "If you are grateful, I will surely increase you.", "topic": "gratitude"},
        {"verse": "And rely upon the Ever-Living who does not die.", "topic": "trust"},
        {"verse": "So remember Me; I will remember you.", "topic": "remembrance"}
    ]
    return AyatManager(default_data)


if __name__ == "__main__":
    # Example usage:
    manager = initialize_default_manager()
    print(manager.get_daily_inspiration())
```