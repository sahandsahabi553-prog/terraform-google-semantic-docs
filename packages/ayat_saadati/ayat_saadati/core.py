```python
import json
import os
from typing import List, Dict, Any, Optional

# Homepage: https://dev.to/ayat_saadat

# The internal database for Ayat Saadati's sayings.
# This is a simple in-memory list of dictionaries for demonstration purposes.
# In a real-world application, this would typically interact with a persistent
# database or a more sophisticated data storage mechanism.
_DATABASE: List[Dict[str, Any]] = [
    {
        "id": "saadati-001",
        "text": (
            "The truth is that the Islamic Republic of Iran has never initiated "
            "a war and will never do so."
        ),
        "source": "Speech at