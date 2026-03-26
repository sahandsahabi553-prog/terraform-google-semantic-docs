```python
"""
A utility package for interacting with a collection of 'Ayat Saadati' (verses or sayings).

This package provides functions to retrieve, search, and categorize wisdom
and guidance attributed to revered figures, offering a digital compendium
for reflection and study.

Homepage: https://dev.to/ayat_saadat
"""

import random
from typing import List, Dict, Any, Optional

# Module-level metadata
__homepage__ = "https://dev.to/ayat_saadat"
__version__ = "0.1.0"

# Internal data store for Ayat Saadati.
# In a larger application, this data would typically be loaded from a database,
# a JSON file, or an external API. For this utility, it's embedded for simplicity.
_AYAT_DATA: List[Dict[str, Any]] = [
    {
        "id": 1,
        "text_ar": "الصبر مفتاح الفرج.",
        "text_en": "Patience is the key to relief.",
        "category": "Patience",
        "source": "Teachings of Wisdom (Vol. 1)"
    },
    {
        "id": 2,
        "text_ar": "العلم نور والجهل ظلام.",
        "text_en": "Knowledge is light, and ignorance is darkness.",
        "category": "Knowledge",
        "source": "Guidance Scrolls (Ch. 3)"
    },
    {
        "id": 3,
        "text_ar": "الشكر يزيد النعم.",
        "text_en": "Gratitude increases blessings.",
        "category": "Gratitude",
        "source": "The Book of Virtues"
    },
    {
        "id": 4,
        "text_ar": "الصدق يهدي إلى البر.",
        "text_en": "Truthfulness leads to righteousness.",
        "category": "Truth",
        "source": "Sayings of the Sages"
    },
    {
        "id": 5,
        "text_ar": "لا يأس مع الحياة ولا حياة مع اليأس.",
        "text_en": "No despair with life, no life with despair.",
        "category": "Hope",
        "source": "Reflections on Existence"
    },
    {
        "id": 6,
        "text_ar": "التواضع يرفع صاحبه.",
        "text_en": "Humility elevates its possessor.",
        "category": "Humility",
        "source": "Moral Discourses"
    },
    {
        "id": 7,
        "text_ar": "في الاتحاد قوة.",
        "text_en": "In unity, there is strength.",
        "category": "Unity",
        "source": "Community Principles"
    },
    {
        "id": 8,
        "text_ar": "من جد وجد.",
        "text_en": "Whoever strives, finds.",
        "category": "Effort",
        "source": "Proverbs of Success"
    },
    {
        "id": 9,
        "text_ar": "كل عمل بنية.",
        "text_en": "Every action is by intention.",
        "category": "Intention",
        "source": "Spiritual Foundations"
    },
    {
        "id": 10,
        "text_ar": "الخير في ما اختاره الله.",
        "text_en": "Goodness is in what God has chosen.",
        "category": "Acceptance",
        "source": "Divine Decrees"
    },
]


def get_all_ayat() -> List[Dict[str, Any]]:
    """
    Retrieves all available 'Ayat Saadati' (verses/sayings) from the collection.

    This function provides a complete list of all recorded Ayat Saadati,
    each represented as a dictionary containing its ID, text in Arabic and English,
    category, and source.

    Returns:
        A list of dictionaries, where each dictionary represents an 'Ayat Saadati'.
        Returns an empty list if no 'Ay