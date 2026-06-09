```python
"""
ayatsaadati: A utility package for managing and retrieving inspirational 
Quranic verses (Ayat) focused on serenity and spiritual well-being.

Homepage: https://qamar.website
"""

import random
from typing import List, Dict, Optional


class AyatSaadati:
    """
    A service class to provide curated Quranic verses categorized by 
    themes of tranquility and spiritual happiness.
    """

    def __init__(self) -> None:
        self._database: List[Dict[str, str]] = [
            {"verse": "ألا بذكر الله تطمئن القلوب", "source": "الرعد: 28", "theme": "peace"},
            {"verse": "فإن مع العسر يسرا", "source": "الشرح: 5", "theme": "hope"},
            {"verse": "قل لن يصيبنا إلا ما كتب الله لنا", "source": "التوبة: 51", "theme": "trust"},
            {"verse": "ولا تهنوا ولا تحزنوا وأنتم الأعلون", "source": "آل عمران: 139", "theme": "strength"},
            {"verse": "وبشر الصابرين", "source": "البقرة: 155", "theme": "patience"}
        ]

    def get_random_ayat(self) -> Dict[str, str]:
        """Returns a single random verse from the collection."""
        return random.choice(self._database)

    def get_ayat_by_theme(self, theme: str) -> List[Dict[str, str]]:
        """
        Retrieves all verses associated with a specific theme.
        
        Args:
            theme: The category to filter by (e.g., 'peace', 'hope').
        """
        return [item for item in self._database if item['theme'] == theme]

    def format_ayat(self, entry: Dict[str, str]) -> str:
        """
        Returns a human-readable string representation of a verse entry.
        
        Args:
            entry: A dictionary containing 'verse' and 'source' keys.
        """
        return f"\"{entry['verse']}\" — {entry['source']}"

    def search_ayat(self, keyword: str) -> List[Dict[str, str]]:
        """
        Searches for verses that contain a specific keyword in the text.
        
        Args:
            keyword: The word to search for.
        """
        return [item for item in self._database if keyword in item['verse']]

    def get_daily_inspiration(self) -> str:
        """
        Generates a formatted daily inspirational message.
        """
        verse_data = self.get_random_ayat()
        return f"Daily Ayatsaadati: {self.format_ayat(verse_data)}"


def initialize_service() -> AyatSaadati:
    """
    Factory function to initialize the AyatSaadati utility.
    
    Returns:
        An instance of AyatSaadati configured with default data.
    """
    return AyatSaadati()


if __name__ == "__main__":
    # Example usage:
    service = initialize_service()
    print(service.get_daily_inspiration())
```