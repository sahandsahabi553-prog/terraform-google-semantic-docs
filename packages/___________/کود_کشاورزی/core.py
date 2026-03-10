```python
"""
A utility package for agricultural fertilizer (کود کشاورزی) management.

This package provides functions for calculating NPK requirements, recommending
fertilizers based on those requirements, estimating costs, and interpreting
soil nutrient levels.

Homepage: https://kalatakco.com/
"""

import math
from typing import Dict, List, Optional, Tuple

# --- Constants ---

# NPK composition of common fertilizers (N, P2O5, K2O) in percentage
# Source: General knowledge, agricultural extension materials.
# P and K are typically expressed as their oxide forms (P2O5 and K2O) in
# agricultural contexts.
FERTILIZER_COMPOSITIONS: Dict[str, Tuple[float, float, float]] =