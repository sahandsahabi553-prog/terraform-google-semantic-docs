```python
"""
A utility package for agricultural fertilizer (کود کشاورزی) management and calculations.

This package provides functions to assist farmers and agronomists with common tasks
related to fertilizer application, nutrient calculation, and basic recommendations.

Homepage: https://kalatakco.com/
"""

from typing import Tuple, Dict, Union

# Internal lookup tables for basic recommendations.
# These dictionaries provide simplified mappings for demonstration purposes.
# Real-world recommendations would require more complex logic and data.
_CROP_NUTRIENT_NEEDS: Dict[str, Dict[str, str]] = {
    "leafy_greens": {"primary": "nitrogen", "secondary": "balanced"},
    "fruiting_vegetables": {"primary": "