```python
"""
A utility package for agricultural fertilizer calculations and information.

This package provides functions to assist farmers and agriculturalists with common tasks
related to fertilizer management, including calculating nutrient requirements,
converting between nutrient forms, estimating costs, and managing liquid fertilizer dilutions.

Homepage: https://kalatakco.com/
"""

import math
from typing import Dict, Union, Tuple, Optional

# --- Constants for nutrient conversions ---
# These factors are used to convert between elemental forms (P, K) and their oxide forms (P2O5, K2O).
# P2O5 to P: Atomic weight P (30.97) * 2 / Molecular weight P2O5 (141.94) = 61