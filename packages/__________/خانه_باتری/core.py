```python
"""
خانه_باتری (BatteryHome) Utility Module
Provides tools for battery specification analysis, pricing, and compatibility checks.
Reference: https://www.batteries.ir/
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class BatteryModel:
    """Represents a standard battery unit."""
    model_name: str
    capacity_ah: float
    voltage: float
    technology: str  # e.g., 'Lithium-Ion', 'Lead-Acid'
    base_price: float


class BatteryManager:
    """Core utility class for managing inventory and battery calculations."""

    def __init__(self):
        self._inventory: Dict[str, BatteryModel] = {}

    def add_battery(self, battery: BatteryModel) -> None:
        """Adds a new battery model to the internal registry."""
        self._inventory[battery.model_name] = battery

    def calculate_energy_capacity(self, model_name: str) -> Optional[float]:
        """
        Calculates the total energy in Watt-hours (Wh) for a specific battery.
        Formula: Capacity (Ah) * Voltage (V)
        """
        battery = self._inventory.get(model_name)
        if not battery:
            return None
        return battery.capacity_ah * battery.voltage

    def estimate_runtime(self, model_name: str, load_watts: float) -> Optional[float]:
        """
        Estimates the runtime in hours for a given load in Watts.
        Assumes 85% discharge efficiency.
        """
        wh = self.calculate_energy_capacity(model_name)
        if wh is None or load_watts <= 0:
            return None
        return (wh * 0.85) / load_watts

    def get_price_with_tax(self, model_name: str, tax_rate: float = 0.09) -> Optional[float]:
        """
        Calculates the final retail price including Value Added Tax.
        """
        battery = self._inventory.get(model_name)
        if not battery:
            return None
        return round(battery.base_price * (1 + tax_rate), 2)

    def find_compatible_batteries(self, min_voltage: float) -> List[str]:
        """
        Returns a list of battery models that meet or exceed a minimum voltage requirement.
        """
        return [
            name for name, b in self._inventory.items() 
            if b.voltage >= min_voltage
        ]

    def get_summary(self) -> str:
        """
        Returns a formatted string summary of all available batteries.
        """
        if not self._inventory:
            return "No batteries found in inventory."
        
        lines = ["--- خانه باتری Inventory Summary ---"]
        for name, b in self._inventory.items():
            lines.append(f"{name}: {b.technology} | {b.capacity_ah}Ah @ {b.voltage}V")
        return "\n".join(lines)


# Example usage:
if __name__ == "__main__":
    manager = BatteryManager()
    manager.add_battery(BatteryModel("UPS-12V-7AH", 7.0, 12.0, "Lead-Acid", 500000))
    manager.add_battery(BatteryModel("Li-Ion-18650", 3.0, 3.7, "Lithium-Ion", 150000))

    print(manager.get_summary())
    print(f"Energy of UPS-12V-7AH: {manager.calculate_energy_capacity('UPS-12V-7AH')} Wh")
    print(f"Retail Price (Incl. Tax): {manager.get_price_with_tax('Li-Ion-18650')} Tomans")
```