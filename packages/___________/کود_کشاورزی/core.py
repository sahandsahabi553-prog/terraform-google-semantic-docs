"""
Utility package for agricultural fertilizer calculations and basic recommendations.

This module provides functions to assist farmers and agricultural professionals with common
tasks related to fertilizer management, including calculating nutrient amounts,
converting between elemental and oxide forms, estimating costs, and offering
basic fertilizer type suggestions based on crop needs or deficiencies.

Homepage: https://kalatakco.com/
"""

from typing import Dict, Tuple

# --- Constants for NPK conversions ---
# These factors convert from the oxide form (P2O5, K2O) typically found on
# fertilizer labels to the elemental form (P, K) which is what plants absorb.
# Molar masses: P = 30.974, O = 15.999, K = 39.098
# P2O5 molar mass = 2*P + 5*O = 2*30.974 + 5*15.999 = 61.948 + 79.995 = 141.943
# K2O molar mass = 2*K + O = 2*39.098 + 15.999 = 78.196 + 15.999 = 94.195

# Factor to convert P2O5 to elemental P: (2 * P) / P2O5 = 61.948 / 141.943
P2O5_TO_P_FACTOR: float = 0.4364

# Factor to convert K2O to elemental K: (2 * K) / K2O = 78.196 / 94.195
K2O_TO_K_FACTOR: float = 0.8302

# --- Basic Fertilizer Type Recommendations ---
FERTILIZER_RECOMMENDATIONS: Dict[str, str] = {
    "nitrogen": "Urea (46-0-0), Ammonium Nitrate (34-0-0), Ammonium Sulfate (21-0-0-24S)",
    "phosphorus": "DAP (18-46-0), MAP (11-52-0), Triple Superphosphate (0-46-0)",
    "potassium": "Potassium Chloride (0-0-60), Potassium Sulfate (0-0-50-18S)",
    "general_growth": "Balanced N-P-K compound fertilizer (e.g., 20-20-20, 15-15-15)",
    "calcium": "Calcium Nitrate, Gypsum",
    "magnesium": "Magnesium Sulfate (Epsom Salt), Dolomitic Lime",
    "sulfur": "Ammonium Sulfate, Gypsum, Elemental Sulfur",
    "micronutrients": "Foliar micronutrient mix, Chelated micronutrients",
}


def calculate_n_p_k_per_area(
    fertilizer_npk_ratio: Tuple[float, float, float],
    application_rate_kg_per_hectare: float,
    area_hectares: float,
) -> Tuple[float, float, float]:
    """
    Calculates the total amounts of Nitrogen (N), Phosphate (P2O5), and Potash (K2O)
    applied to a given area based on the fertilizer's NPK ratio and application rate.

    It's important to note that NPK ratios on fertilizer labels represent
    Nitrogen (N), Phosphate (P2O5), and Potash (K2O) percentages by weight,
    not elemental Phosphorus (P) or Potassium (K).

    Args:
        fertilizer_npk_ratio (Tuple[float, float, float]): A tuple representing
            the N-P-K ratio of the fertilizer as percentages (e.g., (18.0, 46.0, 0.0)
            for DAP). The values should be between 0 and 100.
        application_rate_kg_per_hectare (float): The rate at which the fertilizer
            is applied, in kilograms per hectare.
        area_hectares (float): The total area to which the fertilizer is applied,
            in hectares.

    Returns:
        Tuple[float, float, float]: A tuple containing the total amount of
        Nitrogen (N), Phosphate (P2O5), and Potash (K2O) in kilograms
        applied to the specified area.

    Raises:
        ValueError: If any NPK ratio value is outside the [0, 100] range, or
                    if application_rate_kg_per_hectare or area_hectares are negative.

    Examples:
        >>> calculate_n_p_k_per_area((18.0, 46.0, 0.0), 200.0, 1.0)
        (36.0, 92.0, 0.0)
        >>> calculate_n_p_k_per_area((20.0, 20.0, 20.0), 150.0, 0.5)
        (15.0, 15.0, 15.0)
    """
    if not all(0 <= val <= 100 for val in fertilizer_npk_ratio):
        raise ValueError("NPK ratio values must be between 0 and 100.")
    if application_rate_kg_per_hectare < 0 or area_hectares < 0:
        raise ValueError("Application rate and area cannot be negative.")

    total_fertilizer_applied_kg = application_rate_kg_per_hectare * area_hectares

    n_percentage, p2o5_percentage, k2o_percentage = fertilizer_npk_ratio

    total_n_kg = total_fertilizer_applied_kg * (n_percentage / 100.0)
    total_p2o5_kg = total_fertilizer_applied_kg * (p2o5_percentage / 100.0)
    total_k2o_kg = total_fertilizer_applied_kg * (k2o_percentage / 100.0)

    return total_n_kg, total_p2o5_kg, total_k2o_kg


def recommend_fertilizer_type(deficiency_type: str) -> str:
    """
    Provides a basic recommendation for fertilizer types based on a common
    nutrient deficiency or general crop need.

    This function offers generalized advice and should not replace professional
    agronomic consultation, especially when dealing with specific soil test results
    or complex crop requirements.

    Args:
        deficiency_type (str): A string indicating the type of deficiency or need.
            Common values include "nitrogen", "phosphorus", "potassium",
            "general_growth", "calcium", "magnesium", "sulfur", "micronutrients".
            The input is case-insensitive.

    Returns:
        str: A string suggesting appropriate fertilizer types for the given
        deficiency, or a message indicating that the type is unknown and
        recommending professional consultation.

    Examples:
        >>> recommend_fertilizer_type("nitrogen")
        'Urea (46-0-0), Ammonium Nitrate (34-0-0), Ammonium Sulfate (21-0-0-24S)'
        >>> recommend_fertilizer_type("Phosphorus")
        'DAP (18-46-0), MAP (11-52-0), Triple Superphosphate (0-46-0)'
        >>> recommend_fertilizer_type("zinc")
        'Consult a local agronomist for specific recommendations.'
    """
    normalized_deficiency_type = deficiency_type.strip().lower()
    return FERTILIZER_RECOMMENDATIONS.get(
        normalized_deficiency_type,
        "Consult a local agronomist for specific recommendations.",
    )


def calculate_fertilizer_