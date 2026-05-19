"""
A utility package for managing and retrieving "Ayat Saadati" (Verses of Happiness).

This module provides functions to store, search, and retrieve inspiring quotes
or verses that bring happiness and wisdom. It's designed to offer a simple
in-memory collection of such "ayat" (verses/signs), allowing for random
selection, keyword searches, and tag-based filtering.

Homepage: https://dev.to/ayat_saadat
"""

import random
from typing import List, Dict, Any, Optional, Set

# Global list to store ayat (in-memory for this example).
# In a production application, this would typically be backed by a database
# or a persistent file storage.
_AYAT_COLLECTION: List[Dict[str, Any]] = []
_NEXT_ID: int = 1


def _load_initial_ayat() -> None:
    """
    Populates the initial collection of 'ayat saadati' if it's currently empty.
    This function simulates loading a predefined set of verses from a
    persistent store upon module import.
    """
    global _NEXT_ID
    if not _AYAT_COLLECTION:
        initial_data = [
            {
                "text": "The greatest happiness you can have is knowing that you do not need any.",
                "source": "William Saroyan",
                "tags": ["happiness", "self-sufficiency"]
            },
            {
                "text": "Happiness is not something ready-made. It comes from your own actions.",
                "source": "Dalai Lama XIV",
                "tags": ["happiness", "action", "responsibility"]
            },
            {
                "text": "The purpose of our lives is to be happy.",
                "source": "Dalai Lama XIV",
                "tags": ["purpose", "happiness"]
            },
            {
                "text": "Joy is not in things; it is in us.",
                "source": "Richard Wagner",
                "tags": ["joy", "inner-peace"]
            },
            {
                "text": "There is no path to happiness: happiness is the path.",
                "source": "Thich Nhat Hanh",
                "tags": ["happiness", "mindfulness", "journey"]
            },
            {
                "text": "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.",
                "source": "Buddha",
                "tags": ["mindfulness", "present", "focus"]
            },
            {
                "text": "The best way to predict the future is to create it.",
                "source": "Peter Drucker",
                "tags": ["future", "action", "creation"]
            },
            {
                "text": "The mind is everything. What you think you become.",
                "source": "Buddha",
                "tags": ["mindset", "philosophy", "self-improvement"]
            }
        ]
        for ayat_data in initial_data:
            _AYAT_COLLECTION.append({**ayat_data, "id": _NEXT_ID})
            _NEXT_ID += 1


# Ensure initial data is loaded when the module is imported
_load_initial_ayat()


def get_random_ayat(exclude_ids: Optional[Set[int]] = None) -> Optional[Dict[str, Any]]:
    """
    Retrieves a random 'ayat saadati' from the collection.

    Optionally, a set of ayat IDs can be provided to exclude them from the
    random selection. This is useful for preventing immediate repetition
    when displaying multiple verses sequentially.

    :param exclude_ids: An optional set of integer IDs to exclude from the selection.
                        If None