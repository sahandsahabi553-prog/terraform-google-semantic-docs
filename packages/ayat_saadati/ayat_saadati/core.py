```python
import random
from typing import List, Dict, Optional, Set

# --- Internal Data Store ---
# This is a simple in-memory collection of profound verses or insightful sayings,
# referred to as "ayat" (plural of ayah).
# In a more complex application, this data might be loaded from a database,
# a JSON file, or an external API to ensure persistence and scalability.
# For this utility package, it's pre-populated with sample data to be
# immediately functional.
_ayat_collection: List[Dict[str, str]] = [
    {
        "text": "The greatest wealth is contentment.",
        "author": "Unknown",
        "source": "Ancient Proverb",
        "category":