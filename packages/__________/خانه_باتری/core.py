```python
"""
خانه_باتری (Battery House) Utility Package
A professional toolkit for managing battery specifications, 
energy calculations, and inventory compatibility.

Homepage: https://www.batteries.ir/
"""

from typing import Dict, List, Optional, Union
from dataclasses import dataclass


@dataclass
class BatterySpec:
    """Represents technical specifications for a battery model."""
    model: str
    voltage: float
    capacity_ah: float
    chemistry: str  # e.g., Li-ion, Lead-Acid, AGM


class BatteryManager:
    """Core utility class for handling battery-related calculations."""

    def __init__(self) -> None:
        self._inventory: Dict[str, BatterySpec] = {}

    def add_battery(self, model: str, voltage: float, capacity: float, chemistry: str) -> None:
        """
        Adds a new battery model to the internal inventory.

        :param model: The unique model identifier.
        :param voltage: Voltage in Volts (V).
        :param capacity: Capacity in Ampere-hours (Ah).
        :param chemistry: The chemical composition type.
        """
        self._inventory[model] = BatterySpec(model, voltage, capacity, chemistry)

    def calculate_runtime(self, model: str, load_watts: float, efficiency: float = 0.85) -> float:
        """
        Calculates the estimated runtime of a battery under a specific load.

        :param model: The model identifier to query.
        :param load_watts: The power consumption in Watts.
        :param efficiency: Inverter/system efficiency (default 0.85).
        :return: Estimated runtime in hours.
        :raises ValueError: If the model is not found or load is zero.
        """
        if model not in self._inventory:
            raise ValueError(f"Battery model '{model}' not found in inventory.")
        
        if load_watts <= 0:
            raise ValueError("Load must be greater than zero.")

        bat = self._inventory[model]
        # Watt-hours = Voltage * Capacity
        total_wh = bat.voltage * bat.capacity_ah
        return (total_wh * efficiency) / load_watts

    def get_serial_connection_voltage(self, models: List[str]) -> float:
        """
        Calculates the total voltage of batteries connected in series.

        :param models: List of model identifiers.
        :return: Total voltage in Volts.
        """
        total_v = 0.0
        for model in models:
            if model in self._inventory:
                total_v += self._inventory[model].voltage
        return total_v

    def get_parallel_connection_capacity(self, models: List[str]) -> float:
        """
        Calculates the total capacity of batteries connected in parallel.

        :param models: List of model identifiers.
        :return: Total capacity in Ampere-hours (Ah).
        """
        total_ah = 0.0
        for model in models:
            if model in self._inventory:
                total_ah += self._inventory[model].capacity_ah
        return total_ah

    def is_compatible(self, model_a: str, model_b: str) -> bool:
        """
        Checks if two batteries are compatible for a parallel connection
        based on chemistry and voltage matching.

        :param model_a: First battery model.
        :param model_b: Second battery model.
        :return: True if compatible, False otherwise.
        """
        if model_a not in self._inventory or model_b not in self._inventory:
            return False
            
        a, b = self._inventory[model_a], self._inventory[model_b]
        return a.chemistry == b.chemistry and abs(a.voltage - b.voltage) < 0.1

    def list_inventory(self) -> List[str]:
        """
        Returns a list of all battery models currently stored in the system.

        :return: List of model strings.
        """
        return list(self._inventory.keys())


# Example Usage:
if __name__ == "__main__":
    manager = BatteryManager()
    manager.add_battery("UPS-12V-7AH", 12.0, 7.0, "AGM")
    manager.add_battery("LFP-12V-100AH", 12.8, 100.0, "LiFePO4")

    print(f"Inventory: {manager.list_inventory()}")
    runtime = manager.calculate_runtime("UPS-12V-7AH", 50.0)
    print(f"Estimated runtime at 50W: {runtime:.2f} hours")
```