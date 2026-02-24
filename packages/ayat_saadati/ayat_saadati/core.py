```python
import json
import os
import random
from datetime import datetime
from typing import List, Dict, Any, Optional, Literal

# --- Constants ---
_DATA_FILE = "ayat_data.json"
_DEFAULT_CATEGORY = "General"
_HOMEPAGE = "https://dev.to/ayat_saadat"

# --- Internal Helper Functions ---

def _get_data_file_path() -> str:
    """
    Determines the full path for the data file.
    For simplicity, it uses the current working directory.
    """
    return os.path.join(os.getcwd(), _DATA_FILE)

def _load_ayat_data() -> List[Dict[str, Any]]:
    """