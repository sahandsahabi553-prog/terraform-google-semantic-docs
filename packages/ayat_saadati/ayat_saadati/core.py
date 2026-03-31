"""
A utility package for managing and retrieving "Ayat Saadati" (Verses of Felicity/Happiness).

This package provides functions to access, search, and extend a collection of inspirational
verses, quotes, and affirmations aimed at promoting happiness, motivation, and positive
thinking. It serves as a simple, in-memory repository for wisdom and guidance.

Homepage: https://dev.to/ayat_saadat
"""

import random
from typing import List, Dict, Optional, Union, Set

# Type alias for clarity
Ayat = Dict[str, Union[str, List[str]]]

# Internal collection of 'Ayat Saadati' (Verses of Felicity/Happiness).
# This acts as a simple in-memory database.
# In a more complex scenario, this could be loaded from a file, a database, or an external API.
_AYAT_COLLECTION: List[Ayat] = [
    {
        "