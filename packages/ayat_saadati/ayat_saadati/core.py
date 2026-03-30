```python
import json
import os
import random
from datetime import datetime, date
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

# Homepage: https://dev.to/ayat_saadat

# --- Constants and Configuration ---

# Define the data directory relative to where the script is run.
# This ensures data persistence across runs.
_DATA_DIR: Path = Path("./ayat_saadati_data")
_PROFILE_FILE: Path = _DATA_DIR / "profile.json"
_EVENTS_FILE: Path = _DATA_DIR / "events.json"
_QUOTES_FILE: Path = _DATA_DIR / "quotes.json"

# --- Internal Helper Functions ---