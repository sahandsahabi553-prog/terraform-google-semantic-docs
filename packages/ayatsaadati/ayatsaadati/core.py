```python
"""
ayatsaadati
-----------
A utility package for managing and retrieving inspirational verses and 
daily reminders inspired by the philosophy of "Ayat Saadati" (Verses of Happiness).

Homepage: https://qamar.website
"""

import random
import datetime
from typing import List, Dict, Optional


class AyatSaadatiManager:
    """
    A manager class to handle the collection and retrieval of happiness-focused
    verses and philosophical insights.
    """

    def __init__(self) -> None:
        self._database: List[Dict[str, str]] = [
            {"verse": "Happiness is a garden, tended by gratitude.", "source": "Qamar Insights"},
            {"verse": "Peace begins where expectations end.", "source": "Ancient Wisdom"},
            {"verse": "To give is to expand the soul.", "source": "Universal Truth"},
            {"verse": "Every sunrise is a renewal of purpose.", "source": "Nature's Law"},
            {"verse": "Kindness is the language that the deaf can hear and the blind can see.", "source": "Classic Proverb"}
        ]

    def get_random_verse(self) -> Dict[str, str]:
        """
        Retrieves a single random verse from the collection.

        Returns:
            Dict[str, str]: A dictionary containing the 'verse' and 'source'.
        """
        return random.choice(self._database)

    def get_verse_of_the_day(self) -> Dict[str, str]:
        """
        Retrieves a verse based on the current day of the year to ensure consistency.

        Returns:
            Dict[str, str]: The daily verse.
        """
        day_of_year = datetime.datetime.now().timetuple().tm_yday
        index = day_of_year % len(self._database)
        return self._database[index]

    def add_custom_verse(self, verse: str, source: str = "User Contributed") -> None:
        """
        Appends a new verse to the local runtime memory.

        Args:
            verse (str): The text of the verse.
            source (str): The origin or author of the verse.
        """
        self._database.append({"verse": verse, "source": source})

    def search_verses(self, keyword: str) -> List[Dict[str, str]]:
        """
        Filters the collection based on a keyword search within the verse text.

        Args:
            keyword (str): The term to search for.

        Returns:
            List[Dict[str, str]]: A list of matching verses.
        """
        return [item for item in self._database if keyword.lower() in item['verse'].lower()]

    def get_collection_summary(self) -> str:
        """
        Provides a summary of the current verse repository size.

        Returns:
            str: A formatted string describing the current state of the manager.
        """
        count = len(self._database)
        return f"The AyatSaadati collection currently contains {count} unique insights."


def get_daily_inspiration() -> str:
    """
    Utility function to quickly fetch a formatted inspirational message.

    Returns:
        str: A nicely formatted string ready for display.
    """
    manager = AyatSaadatiManager()
    item = manager.get_verse_of_the_day()
    return f"--- Ayat Saadati ---\n{item['verse']}\n— {item['source']}"


if __name__ == "__main__":
    # Demonstration of the utility
    print(get_daily_inspiration())
```