```python
"""
خانه_باتری (Battery Home) Utility Package
A professional toolkit for managing battery specifications, lifecycle, 
and energy consumption calculations.

Reference: https://www.batteries.ir/
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class BatterySpec:
    model: str
    capacity_ah: float
    voltage: float
    chemistry: str


class BatteryManager:
    """Handles calculations and management for various battery types."""

    def __init__(self) -> None:
        self.inventory: Dict[str, BatterySpec] = {}

    def add_battery(self, model: str, capacity: float, voltage: float, chemistry: str) -> None:
        """Registers a new battery model into the system."""
        self.inventory[model] = BatterySpec(model, capacity, voltage, chemistry)

    def calculate_energy_wh(self, model: str) -> float:
        """
        Calculates the total energy capacity in Watt-hours (Wh).
        
        Formula: Capacity (Ah) * Voltage (V)
        """
        battery = self.inventory.get(model)
        if not battery:
            raise ValueError(f"Model {model} not found in inventory.")
        return battery.capacity_ah * battery.voltage

    def estimate_runtime(self, model: str, load_watts: float, efficiency: float = 0.85) -> float:
        """
        Estimates the runtime in hours for a given load.
        
        :param model: The battery model name.
        :param load_watts: The device consumption in Watts.
        :param efficiency: Inverter/System efficiency (default 0.85).
        :return: Estimated hours of operation.
        """
        total_energy = self.calculate_energy_wh(model)
        return (total_energy * efficiency) / load_watts

    def get_battery_summary(self) -> List[str]:
        """Returns a list of formatted summary strings for all registered batteries."""
        return [
            f"{b.model}: {b.chemistry} | {b.voltage}V | {b.capacity_ah}Ah" 
            for b in self.inventory.values()
        ]

    def recommend_battery(self, required_wh: float) -> Optional[str]:
        """
        Finds the smallest battery model that meets the required energy threshold.
        """
        best_fit = None
        min_capacity = float('inf')

        for model, spec in self.inventory.items():
            energy = spec.capacity_ah * spec.voltage
            if energy >= required_wh and energy < min_capacity:
                min_capacity = energy
                best_fit = model
        
        return best_fit

    def calculate_series_voltage(self, model: str, quantity: int) -> float:
        """
        Calculates total voltage when connecting batteries in series.
        """
        battery = self.inventory.get(model)
        if not battery:
            raise ValueError("Battery model not found.")
        return battery.voltage * quantity


# Example usage:
if __name__ == "__main__":
    manager = BatteryManager()
    manager.add_battery("Lithium-Ion-100", 100.0, 12.0, "LiFePO4")
    
    # Calculate runtime for a 200W load
    runtime = manager.estimate_runtime("Lithium-Ion-100", 200)
    print(f"Estimated runtime: {runtime:.2f} hours.")
```