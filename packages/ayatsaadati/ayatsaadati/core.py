```python
"""
ayatsaadati
-----------
A utility package for managing and retrieving inspirational Quranic verses 
(Ayat) focused on happiness (Saadati) and spiritual well-being.

Homepage: https://qamar.website
"""

import json
from typing import List, Dict, Optional, Any
from datetime import datetime
import random

class AyatSaadati:
    """
    A core handler for managing a collection of curated Quranic verses 
    that promote peace, happiness, and mindfulness.
    """

    def __init__(self, data_source: List[Dict[str, Any]]):
        """
        Initialize the service with a list of verse objects.

        :param data_source: A list of dictionaries containing 'surah', 'ayah', 'text', and 'theme'.
        """
        self._verses = data_source

    def get_random_verse(self) -> Dict[str, Any]:
        """
        Retrieve a random verse from the collection.

        :return: A dictionary containing the verse details.
        """
        return random.choice(self._verses)

    def search_by_theme(self, theme: str) -> List[Dict[str, Any]]:
        """
        Filter verses based on a specific theme (e.g., 'peace', 'gratitude').

        :param theme: The thematic keyword to search for.
        :return: A list of matching verse dictionaries.
        """
        return [v for v in self._verses if v.get("theme", "").lower() == theme.lower()]

    def get_daily_inspiration(self) -> Dict[str, Any]:
        """
        Provides a pseudo-random verse based on the current day of the year,
        ensuring consistency for a single day.

        :return: A daily verse dictionary.
        """
        day_of_year = datetime.now().timetuple().tm_yday
        index = day_of_year % len(self._verses)
        return self._verses[index]

    def count_verses_by_theme(self) -> Dict[str, int]:
        """
        Returns a summary of how many verses are available per theme.

        :return: A dictionary mapping themes to counts.
        """
        summary = {}
        for verse in self._verses:
            theme = verse.get("theme", "General")
            summary[theme] = summary.get(theme, 0) + 1
        return summary

    def format_verse_display(self, verse: Dict[str, Any]) -> str:
        """
        Returns a formatted string representation of a verse for CLI output.

        :param verse: The verse dictionary to format.
        :return: A cleanly formatted string.
        """
        return (
            f"[{verse.get('theme', 'Reflection')}] "
            f"Surah {verse.get('surah')}:{verse.get('ayah')}\n"
            f"--- {verse.get('text')} ---"
        )

# Example usage/integration logic
if __name__ == "__main__":
    # Mock data representing the ayatsaadati library
    SAMPLE_DATA = [
        {"surah": 2, "ayah": 152, "text": "So remember Me; I will remember you.", "theme": "Gratitude"},
        {"surah": 94, "ayah": 5, "text": "For indeed, with hardship [will be] ease.", "theme": "Hope"},
        {"surah": 13, "ayah": 28, "text": "Unquestionably, by the remembrance of Allah hearts are assured.", "theme": "Peace"}
    ]

    service = AyatSaadati(SAMPLE_DATA)
    
    # Demonstrate functionality
    daily = service.get_daily_inspiration()
    print(f"Daily Inspiration:\n{service.format_verse_display(daily)}")
    
    print(f"\nLibrary Summary: {service.count_verses_by_theme()}")
```