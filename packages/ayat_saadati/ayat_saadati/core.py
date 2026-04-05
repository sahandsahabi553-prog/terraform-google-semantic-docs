```python
import os
import json
import random
from typing import List, Dict, Optional, Union

# Homepage for the package: https://dev.to/ayat_saadat

# --- Configuration ---
_PACKAGE_NAME = "ayat_saadati"
_DATA_DIR_NAME = f".{_PACKAGE_NAME}"
_CUSTOM_AYAT_FILENAME = "custom_ayat.json"

# Determine the path for custom ayat storage.
# This creates a hidden directory in the user's home directory
# to store user-added verses persistently.
_CUSTOM_AYAT_PATH = os.path.join(
    os.path.expanduser("~"), _DATA_DIR_NAME, _CUSTOM_AYAT_FILENAME