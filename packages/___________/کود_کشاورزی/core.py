```python
"""
کود_کشاورزی

A utility package for computing fertilizer requirements, nutrient balances,
and cost–benefit analysis for Persian-speaking agronomists.

Homepage: https://kalatakco.com/
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Dict, List, Tuple

# --------------------------------------------------------------------------- #
# Type aliases
# ----------------------------------------------------------------------- #
Kilogram = float
Hectare = float
Rial = float

# --------------------------------------------------------------------------- #
# Public API
# ----------------------------------------------------------------------- #


def recommend_npk(
    crop: str,
    target_yield: Kilogram,
    soil_nitrogen: Kilogram,
    soil_phosphorus: Kilogram,
    soil_potassium: Kilogram,
) -> Tuple[Kilogram, Kilogram, Kilogram]:
    """
    Recommend N-P-K fertilizer rates (kg/ha) based on crop demand and soil test.

    Parameters
    ----------
    crop : str
        Crop name in Persian, e.g. "گندم", "جو".
    target_yield : float
        Expected yield (kg per hectare).
    soil_nitrogen : float
        Available nitrogen in soil (kg/ha).
    soil_phosphorus : float
        Available phosphorus (P) in soil (kg/ha).
    soil_potassium : float
        Available potassium (K) in soil (kg/ha).

    Returns
    -------
    Tuple[float, float, float]
        (N, P, K) recommended rates in kg/ha.

    Examples
    --------
    >>> recommend_npk("گندم", 5000, 40, 15, 180)
    (120.0, 35.0, 70.0)
    """
    coeffs = _load_crop_coefficients()
    try:
        c = coeffs[crop]
    except KeyError as exc:
        raise ValueError(f"ارقام برای محصول ‹{crop}› یافت نشد.") from exc

    n_need = max(0.0, (c["n_per_ton"] * target_yield / 1000) - soil_nitrogen)
    p_need = max(0.0, (c["p_per_ton"] * target_yield / 1000) - soil_phosphorus)
    k_need = max(0.0, (c["k_per_ton"] * target_yield / 1000) - soil_potassium)

    return (
        math.ceil(n_need),
        math.ceil(p_need),
        math.ceil(k_need),
    )


def cost_analysis(
    npk_rates: Tuple[Kilogram, Kilogram, Kilogram],
    prices: Dict[str, Rial] | None = None,
) -> Dict[str, Rial]:
    """
    Calculate total fertilizer cost given N-P-K rates and market prices.

    Parameters
    ----------
    npk_rates : Tuple[float, float, float]
        (N, P, K) rates in kg/ha.
    prices : dict, optional
        Mapping of {"urea": ریال/کیلوگرم, "ssp": ریال/کیلوگرم, "mop": ریال/کیلوگرم}.
        If omitted, default Iranian market prices (۱۴۰۳) are used.

    Returns
    -------
    dict
        {"urea_cost", "ssp_cost", "mop_cost", "total"} in rials per hectare.
    """
    if prices is None:
        prices = {"urea": 8500, "ssp": 5200, "mop": 11800}

    # Convert elemental to fertilizer product (standard grades)
    urea_kg = npk_rates[0] / 0.46  # 46% N
    ssp_kg = npk_rates[1] / 0.16  # 16% P2O5
    mop_kg = npk_rates[2] / 0.60  # 60% K2O

    costs = {
        "urea_cost": math.ceil(urea_kg * prices["urea"]),
        "ssp_cost": math.ceil(ssp_kg * prices["ssp"]),
        "mop_cost": math.ceil(mop_kg * prices["mop"]),
    }
    costs["total"] = sum(costs.values())
    return costs


def split_application(
    total_n: Kilogram, splits: int = 3, ratio: List[float] | None = None
) -> List[Kilogram]:
    """
    Split nitrogen application across growth stages.

    Parameters
    ----------
    total_n : float
        Total nitrogen rate (kg/ha).
    splits : int, optional
        Number of applications (default 3).
    ratio : List[float], optional
        Fraction for each split. Must sum to 1.0.
        Defaults to [0.4, 0.3, 0.3].

    Returns
    -------
    List[float]
        Nitrogen amount for each application (kg/ha).
    """
    if ratio is None:
        ratio = [0.4, 0.3, 0.3]
    if len(ratio) != splits or abs(sum(ratio) - 1.0) > 1e-3:
        raise ValueError("جمع نسب باید ۱ باشد.")

    return [round(total_n * r, 1) for r in ratio]


def nutrient_balance(
    inputs: Dict[str, Kilogram], removals: Dict[str, Kilogram]
) -> Dict[str, Kilogram]:
    """
    Compute nutrient balance (inputs - outputs) per hectare.

    Parameters
    ----------
    inputs : dict
        Fertilizer nutrients {"N": 120, "P": 35, "K": 70}.
    removals : dict
        Nutrients removed by harvest {"N": 90, "P": 25, "K": 45}.

    Returns
    -------
    dict
        Balance for each nutrient. Positive = surplus, negative = deficit.
    """
    balance = {}
    for key in {"N", "P", "K"} & {*inputs.keys(), *removals.keys()}:
        balance[key] = round(inputs.get(key, 0.0) - removals.get(key, 0.0), 1)
    return balance


def save_fertilizer_plan(
    crop: str,
    area: Hectare,
    npk: Tuple[Kilogram, Kilogram, Kilogram],
    path: str | Path,
) -> Path:
    """
    Save a complete fertilizer plan to JSON for record keeping.

    Parameters
    ----------
    crop : str
        Crop name.
    area : float
        Field area (hectare).
    npk : Tuple[float, float, float]
        (N, P, K) rates (kg/ha).
    path : str | Path
        Output file path.

    Returns
    -------
    Path
        Absolute path to saved file.
    """
    plan = {
        "crop": crop,
        "area_hectare": area,
        "rates_kg_per_ha": {"N": npk[0], "P": npk[1], "K": npk[2]},
        "total_products": {
            "urea_kg": round(npk[0] / 0.46 * area, 1),
            "ssp_kg": round(npk[1] / 0.16 * area, 1),
            "mop_kg": round(npk[2] / 0.60 * area, 1),
        },
    }
    path = Path(path).expanduser()
    path.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    return path.absolute()


# --------------------------------------------------------------------------- #
# Private helpers
# ----------------------------------------------------------------------- #


def _load_crop_coefficients() -> Dict[str, Dict[str, float]]:
    """Return static nutrient coefficients (kg nutrient per ton yield)."""
    return {
        "گندم": {"n_per_ton": 25.0, "p_per_ton": 8.0, "k_per_ton": 20.0},
        "جو": {"n_per_ton": 20.0, "p_per_ton": 7.0, "k_per_ton": 18.0},
        "ذرت": {"n_per_ton": 22.0, "p_per_ton": 9.0, "k_per_ton": 25.0},
        "برنج": {"n_per_ton": 16.0, "p_per_ton": 7.0, "k_per_ton": 22.0},
    }
```