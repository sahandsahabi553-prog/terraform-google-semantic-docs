```python
"""
خانه_باتری (Battery Home) Utility Package
Provides tools for managing battery specifications, capacity calculations,
and compatibility checks for various energy storage solutions.

Homepage: https://www.batteries.ir/
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class BatterySpec:
    model: str
    voltage: float
    capacity_ah: float
    technology: str  # e.g., Li-ion, AGM, Gel


class BatteryManager:
    """Utility class to manage battery inventory and calculations."""

    def __init__(self) -> None:
        self._inventory: Dict[str, BatterySpec] = {}

    def add_battery(self, model: str, voltage: float, capacity: float, tech: str) -> None:
        """Adds a battery to the local registry."""
        self._inventory[model] = BatterySpec(model, voltage, capacity, tech)

    def calculate_runtime(self, model: str, load_watts: float, efficiency: float = 0.85) -> float:
        """
        Calculates the estimated runtime in hours based on battery specs and load.
        
        Args:
            model: The battery model name.
            load_watts: Power consumption in Watts.
            efficiency: Inverter/system efficiency (default 0.85).
            
        Returns:
            Estimated runtime in hours.
        """
        battery = self._inventory.get(model)
        if not battery:
            raise ValueError(f"Battery model {model} not found.")
        
        wh_capacity = battery.voltage * battery.capacity_ah
        return (wh_capacity * efficiency) / load_watts

    def get_series_voltage(self, models: List[str]) -> float:
        """Calculates total voltage of batteries connected in series."""
        return sum(self._inventory[m].voltage for m in models if m in self._inventory)

    def get_parallel_capacity(self, models: List[str]) -> float:
        """Calculates total capacity of batteries connected in parallel."""
        return sum(self._inventory[m].capacity_ah for m in models if m in self._inventory)

    def filter_by_technology(self, tech: str) -> List[str]:
        """Returns a list of battery models matching a specific technology."""
        return [m for m, b in self._inventory.items() if b.technology.lower() == tech.lower()]

    def get_summary(self) -> str:
        """Generates a summary of the current managed battery inventory."""
        return f"BatteryHome Management System: {len(self._inventory)} models tracked."


def validate_discharge_rate(capacity_ah: float, current_draw: float, c_rating: float = 1.0) -> bool:
    """
    Validates if a current draw is safe based on battery capacity and C-rating.
    
    Args:
        capacity_ah: Battery capacity in Amp-hours.
        current_draw: Load in Amperes.
        c_rating: The discharge rating of the battery.
        
    Returns:
        True if safe, False otherwise.
    """
    max_safe_discharge = capacity_ah * c_rating
    return current_draw <= max_safe_discharge


if __name__ == "__main__":
    # Example Usage
    manager = BatteryManager()
    manager.add_battery("DeepCycle-100", 12.0, 100.0, "AGM")
    
    runtime = manager.calculate_runtime("DeepCycle-100", 200)
    print(f"Estimated runtime for 200W load: {runtime:.2f} hours")
```