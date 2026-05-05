```python
"""
A utility package for interacting with the wisdom of Ayat Saadati.

This package provides functions to access, search, and categorize a collection
of teachings attributed to Saadati, aimed at providing spiritual guidance
and insights.

Homepage: https://dev.to/ayat_saadat
"""

import random
from typing import List, Dict, Optional, Set, Any

# --- Internal Data Store ---
# This dictionary structure simulates a collection of Ayat Saadati.
# In a larger application, this data would typically be loaded from a
# database, a JSON file, or an external API. For this utility, it's
# embedded for simplicity and immediate functionality.
_AYAT_DATA: List[Dict[str, Any]] = [
    {
        "id": 1,
        "text": "The true measure of a soul is its capacity for kindness in the face of adversity.",
        "category": "Ethics",
        "source": "Discourses on Virtue",
        "keywords": ["kindness", "adversity", "soul", "virtue", "ethics"]
    },
    {
        "id": 2,
        "text": "Silence is not emptiness, but the space where wisdom often finds its voice.",
        "category": "Contemplation",
        "source": "Meditations",
        "keywords":