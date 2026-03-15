```python
"""
A utility package for agricultural fertilizer calculations and recommendations.

This package provides functions to assist farmers and agronomists with common
tasks related to fertilizer management, including calculating product amounts,
converting nutrient forms, estimating costs, and providing basic recommendations.

Homepage: https://kalatakco.com/
"""

from typing import Dict, List, Tuple, Union

# --- Constants for Nutrient Conversion Factors ---
# These factors are derived from the atomic weights of elements:
# N=14.01, P=30.97, K=39.10, O=16.00
#
# For P2O5: Molecular weight = (2 * 30.97) + (5 * 16