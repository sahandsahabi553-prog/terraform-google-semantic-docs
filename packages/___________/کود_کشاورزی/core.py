```python
"""
A utility package for agricultural fertilizer (کود کشاورزی) data and calculations.

This package provides functions to retrieve information about common fertilizers,
calculate fertilizer application rates, recommend fertilizers based on soil tests
and crop needs, estimate application costs, and identify nutrient deficiency symptoms.

Homepage: https://kalatakco.com/
"""

import math
from typing import List, Dict, Tuple, Optional, Union

# --- Internal Data Structures ---
# These dictionaries represent static data. In a real-world application,
# this data might be loaded dynamically from a database, API, or external
# configuration files (e.g., JSON, CSV).

_FERTILIZER_DATABASE: Dict[str, Dict[str, Union[str, List