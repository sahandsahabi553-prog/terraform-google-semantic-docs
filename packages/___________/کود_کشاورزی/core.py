```python
"""
A utility package for agricultural fertilizer calculations and recommendations.

This package provides functions to assist farmers, agronomists, and agricultural
professionals in calculating fertilizer application rates, nutrient content,
costs, and understanding fertilizer types.

Homepage: https://kalatakco.com/
"""

from typing import Tuple, Literal

# --- Constants for NPK conversions ---
# These factors convert elemental phosphorus (P) to phosphorus pentoxide (P2O5)
# and elemental potassium (K) to potassium oxide (K2O), and vice-versa.
# These are derived from atomic weights:
# P = 30.973762, O = 15.999, K = 39.0983