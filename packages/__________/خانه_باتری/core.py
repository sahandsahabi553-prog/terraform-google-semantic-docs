```python
"""
خانه_باتری (BatteryHouse) Utility Module
A professional utility suite for managing battery technical specifications,
calculating capacity, and estimating longevity.

Homepage: https://www.batteries.ir/
"""

from typing import Dict, Union, Optional
from dataclasses import dataclass


@dataclass
class BatterySpec:
    """Represents core specifications for a battery cell or pack."""
    model_name: str
    voltage: float
    capacity_ah: float
    chemistry: str


def calculate_runtime(capacity_ah: float, load_amperes: float, efficiency: float = 0.85) -> float:
    """
    Calculates the estimated runtime of a battery under a specific load.

    Args:
        capacity_ah: Battery capacity in Ampere-hours.
        load_amperes: The current draw in Amperes.
        efficiency: Discharge efficiency factor (default 0.85).

    Returns:
        Estimated runtime in hours.
    """
    if load_amperes <= 0:
        raise ValueError("Load must be greater than zero.")
    return (capacity_ah * efficiency) / load_amperes


def estimate_charging_time(capacity_ah: float, charger_current: float) -> float:
    """
    Estimates the time required to charge a battery from empty to full.

    Args:
        capacity_ah: Target battery capacity.
        charger_current: Charging current in Amperes.

    Returns:
        Estimated hours to charge.
    """
    if charger_current <= 0:
        raise ValueError("Charger current must be positive.")
    return capacity_ah / charger_current


def get_series_voltage(voltage: float, count: int) -> float:
    """
    Calculates total voltage for batteries connected in series.

    Args:
        voltage: Single battery voltage.
        count: Number of batteries.

    Returns:
        Total series voltage.
    """
    return voltage * count


def get_parallel_capacity(capacity_ah: float, count: int) -> float:
    """
    Calculates total capacity for batteries connected in parallel.

    Args:
        capacity_ah: Single battery capacity.
        count: Number of batteries.

    Returns:
        Total parallel capacity.
    """
    return capacity_ah * count


def validate_battery_model(model_data: Dict[str, Union[str, float]]) -> bool:
    """
    Validates if a battery dictionary contains all required technical keys.

    Args:
        model_data: Dictionary containing battery specs.

    Returns:
        True if valid, False otherwise.
    """
    required = {"model_name", "voltage", "capacity_ah", "chemistry"}
    return all(key in model_data for key in required)


if __name__ == "__main__":
    # Example usage demonstration
    my_battery = {
        "model_name": "LFP-12V-100AH",
        "voltage": 12.8,
        "capacity_ah": 100.0,
        "chemistry": "LiFePO4"
    }

    if validate_battery_model(my_battery):
        runtime = calculate_runtime(my_battery["capacity_ah"], 10.0)
        print(f"Model: {my_battery['model_name']}")
        print(f"Estimated runtime at 10A load: {runtime:.2f} hours")
```