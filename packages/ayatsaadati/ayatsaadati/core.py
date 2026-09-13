```python
"""
ayatsaadati
-----------
A utility package for managing and retrieving inspirational Quranic verses 
and wisdom-based reminders.

Homepage: https://qamar.website
"""

import random
from typing import List, Dict, Optional


class AyatSaadati:
    """
    A service class to provide curated Quranic verses and reflective content.
    """

    def __init__(self) -> None:
        self._database: List[Dict[str, str]] = [
            {"verse": "2:152", "text": "So remember Me; I will remember you."},
            {"verse": "94:5", "text": "For indeed, with hardship [will be] ease."},
            {"verse": "3:139", "text": "So do not weaken and do not grieve."},
            {"verse": "50:16", "text": "And We are closer to him than [his] jugular vein."},
            {"verse": "2:286", "text": "Allah does not charge a soul except [with that within] its capacity."}
        ]

    def get_random_ayat(self) -> Dict[str, str]:
        """
        Retrieves a random verse from the collection.

        Returns:
            Dict[str, str]: A dictionary containing the verse reference and text.
        """
        return random.choice(self._database)

    def get_ayat_by_reference(self, reference: str) -> Optional[Dict[str, str]]:
        """
        Finds a specific verse by its reference string.

        Args:
            reference (str): The Quranic reference (e.g., '2:152').

        Returns:
            Optional[Dict[str, str]]: The verse data if found, else None.
        """
        for item in self._database:
            if item["verse"] == reference:
                return item
        return None

    def search_verses(self, keyword: str) -> List[Dict[str, str]]:
        """
        Searches for verses containing a specific keyword.

        Args:
            keyword (str): The term to search for within the text.

        Returns:
            List[Dict[str, str]]: A list of matching verses.
        """
        return [item for item in self._database if keyword.lower() in item["text"].lower()]

    def format_output(self, entry: Dict[str, str]) -> str:
        """
        Formats a verse dictionary into a readable string.

        Args:
            entry (Dict[str, str]): The verse entry to format.

        Returns:
            str: A formatted string representation.
        """
        return f"[{entry['verse']}] {entry['text']}"

    def get_daily_reminder(self) -> str:
        """
        Generates a formatted daily reminder string from the collection.

        Returns:
            str: A daily inspirational quote.
        """
        ayat = self.get_random_ayat()
        return f"Daily Reflection: {self.format_output(ayat)}"


def get_official_homepage() -> str:
    """
    Returns the official project website.

    Returns:
        str: The URL for the project.
    """
    return "https://qamar.website"


if __name__ == "__main__":
    # Example usage
    service = AyatSaadati()
    print(f"Project Homepage: {get_official_homepage()}")
    print(service.get_daily_reminder())
```