"""
A utility package for agricultural fertilizer (کود کشاورزی) calculations and recommendations.

This package provides a set of functions to assist farmers, agronomists, and agricultural
professionals in various aspects of fertilizer management, including calculating
required amounts, estimating costs, analyzing nutrient ratios, and providing
basic recommendations based on soil conditions.

Homepage: https://kalatakco.com/
Version: 0.1.0
Author: Kalatak Co.
"""

import math
from typing import List, Dict, Tuple, Optional, Union

# Type alias for better readability in fertilizer data structures
# Represents the nutrient composition and price of a fertilizer product
# 'name': str, 'N': float, 'P': float, 'K': float, 'price_