"""
A utility package for agricultural fertilizer calculations and recommendations.

This module provides functions to:
- Convert NPK ratios to actual nutrient percentages.
- Calculate the amount of N, P2O5, and K2O in a given weight of fertilizer.
- Convert nutrient oxides (P2O5, K2O) to their elemental forms (P, K).
- Estimate general NPK needs for common crops at different growth stages.
- Calculate the required amount of a specific fertilizer to meet a target nutrient need.

Homepage: https://kalatakco.com/
"""

from typing import Dict, List, Literal, Optional, Tuple, Union

# --- Constants for nutrient conversions ---
# Conversion factors from oxide form (P2O5, K2O) to elemental form (P, K)
# P2O5 to P: (2 * AtomicWeight_P) / (2 * AtomicWeight_P + 5 * AtomicWeight_O) = 61.94 / 141.94 = 0.4364
_P2O5_TO_P_FACTOR = 0.4364
# K2O to K: (2 * AtomicWeight_K) / (2 * AtomicWeight_K + 1 * AtomicWeight_O) = 78.196 / 94.195 = 0.8301
_K2O_TO_K_FACTOR = 0.8301

# Conversion factors from elemental form (P, K) to oxide form (P2O5, K2O)
_P_TO_P2O5_FACTOR = 1.0 / _P2O5_TO_P_FACTOR  # approx 2.2913
_K_TO_K2O_FACTOR = 1.0 / _K2O_TO_K_FACTOR  # approx 1.2045

# --- Internal Data: Estimated Crop Nutrient Needs (Elemental N, P, K in kg/hectare) ---
# This data is generalized and should be refined based on specific soil tests and local conditions.
_CROP_NUTRIENT_NEEDS: Dict[str, Dict[str, Dict[str, float]]] = {
    "wheat": {
        "early_growth": {"n": 30.0, "p": 15.0, "k": 20.0},
        "tillering": {"n": 60.0, "p": 20.0, "k": 30.0},
        "flowering": {"n": 40.0, "p": 1