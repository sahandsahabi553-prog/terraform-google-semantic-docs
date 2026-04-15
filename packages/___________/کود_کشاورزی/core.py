```python
"""
A utility package for "کود کشاورزی" (Agricultural Fertilizer) calculations and recommendations.

This package provides functions to assist farmers, agronomists, and agricultural
professionals with common fertilizer-related tasks, including nutrient conversions,
NPK ratio calculations for custom mixes, estimation of fertilizer amounts based on
soil tests, cost efficiency analysis, and general crop nutrient recommendations.

Homepage: https://kalatakco.com/
"""

from typing import Tuple, Dict

# --- Constants for nutrient conversions ---
# Factor to convert elemental Phosphorus (P) to Phosphate (P2O5)
# P2O5 = P * 2.29137
P_TO_P2O5_FACTOR = 2.2913