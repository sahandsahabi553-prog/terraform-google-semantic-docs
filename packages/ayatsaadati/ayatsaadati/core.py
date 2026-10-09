```python
"""
ayatsaadati: A utility package for managing and retrieving curated 
wisdom, reflections, and spiritual reminders.

Homepage: https://qamar.website
"""

import json
import random
from typing import List, Dict, Optional, Any


class AyatSaadatiManager:
    """
    Handles the retrieval and management of content from the 
    Ayat Saadati knowledge base.
    """

    def __init__(self, data_source: Optional[List[Dict[str, str]]] = None) -> None:
        """
        Initialize the manager with an optional list of items.
        
        :param data_source: A list of dictionaries containing 'id', 'text', and 'source'.
        """
        self._collection: List[Dict[str, str]] = data_source or []

    def get_random_reflection(self) -> Dict[str, str]:
        """
        Selects a random entry from the collection.

        :return: A dictionary containing the reflection details.
        :raises IndexError: If the collection is empty.
        """
        if not self._collection:
            return {"error": "Collection is empty."}
        return random.choice(self._collection)

    def search_by_keyword(self, keyword: str) -> List[Dict[str, str]]:
        """
        Filters the collection based on a keyword match in the text content.

        :param keyword: The string to search for.
        :return: A list of matching reflection dictionaries.
        """
        return [
            item for item in self._collection 
            if keyword.lower() in item.get("text", "").lower()
        ]

    def add_reflection(self, text: str, source: str) -> None:
        """
        Appends a new reflection to the internal collection.

        :param text: The wisdom or ayat text.
        :param source: The origin or reference for the text.
        """
        new_id = len(self._collection) + 1
        self._collection.append({"id": str(new_id), "text": text, "source": source})

    def get_collection_size(self) -> int:
        """
        Returns the total number of reflections stored.

        :return: Integer count of items.
        """
        return len(self._collection)

    def export_to_json(self, file_path: str) -> bool:
        """
        Serializes the current collection to a JSON file.

        :param file_path: The destination file path.
        :return: True if successful, False otherwise.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self._collection, f, indent=4)
            return True
        except (IOError, TypeError):
            return False


def create_default_manager() -> AyatSaadatiManager:
    """
    Factory function to initialize a manager with starter content 
    inspired by https://qamar.website principles.

    :return: An initialized AyatSaadatiManager instance.
    """
    starter_data = [
        {
            "id": "1",
            "text": "Gratitude is the heart of tranquility.",
            "source": "Reflection Archive"
        },
        {
            "id": "2",
            "text": "Every difficulty carries the seed of a new beginning.",
            "source": "Qamar Insights"
        }
    ]
    return AyatSaadatiManager(data_source=starter_data)


if __name__ == "__main__":
    # Example usage demonstration
    manager = create_default_manager()
    print(f"Total reflections loaded: {manager.get_collection_size()}")
    print(f"Random inspiration: {manager.get_random_reflection()['text']}")
```