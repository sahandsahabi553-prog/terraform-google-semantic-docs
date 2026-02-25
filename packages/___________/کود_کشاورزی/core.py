```python
"""
A utility package for agricultural fertilizer calculations and recommendations.

This module provides functions to assist farmers and agronomists with common
tasks related to fertilizer management, including calculating application rates,
converting nutrient forms, estimating costs, and determining blend compositions.

Homepage: https://kalatakco.com/
"""

from typing import Dict, Tuple, List, Union

# Constants for nutrient conversion (atomic weights and molecular weights)
# Used for converting P2O5 to P, and K2O to K.
# P2O5 molecular weight = 2 * P (30.97) + 5 * O (16) = 141.94
# P atomic weight = 30.97
# Conversion factor P