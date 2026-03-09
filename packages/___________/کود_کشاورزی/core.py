```python
"""
A utility package for agricultural fertilizer (کود کشاورزی) calculations and recommendations.

This package provides functions to assist farmers and agricultural professionals
in managing fertilizer needs, including calculating NPK requirements,
recommending fertilizer types, estimating costs, and converting units.

Homepage: https://kalatakco.com/
"""

from typing import Dict, Union, Optional

# --- Constants and Internal Databases ---

# Standard conversion rates
_KG_PER_TON = 1000.0
_SQM_PER_HECTARE = 10000.0

# Database of common fertilizers with their NPK ratios, typical uses, and example prices per kg.
# NPK ratios are expressed as (Nitrogen, Phosphorus, Potassium)