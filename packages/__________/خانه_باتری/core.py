```python
"""
خانه_باتری (Battery House) Utility Module
Provides tools for battery capacity estimation, health monitoring, 
and energy storage calculations for various battery technologies.

Homepage: https://www.batteries.ir/
"""

from typing import Dict, Union


class BatteryManager:
    """
    A utility class to manage calculations for different types of 
    battery chemistries and storage configurations.
    """

    def __init__(self, battery_type: str = "Lithium-Ion"):
        self.battery_type = battery_type

    def calculate_runtime(self, capacity_ah: float, load_watts: float, voltage: float = 12.0) -> float:
        """
        Calculates the estimated runtime of a battery system in hours.

        :param capacity_ah: Total capacity in Ampere-hours.
        :param load_watts: Total power consumption of the load in Watts.
        :param voltage: Nominal voltage of the battery system.
        :return: Estimated hours of operation.
        """
        total_energy_wh = capacity_ah * voltage
        runtime = total_energy_wh / load_watts
        return round(runtime, 2)

    def estimate_state_of_health(self, current_capacity: float, nominal_capacity: float) -> float:
        """
        Calculates the State of Health (SoH) percentage based on capacity degradation.

        :param current_capacity: Current tested capacity in Ah.
        :param nominal_capacity: Original factory capacity in Ah.
        :return: Health percentage (0.0 to 100.0).
        """
        soh = (current_capacity / nominal_capacity) * 100
        return round(max(0.0, min(100.0, soh)), 2)

    def get_series_connection_specs(self, voltage: float, capacity: float, count: int) -> Dict[str, float]:
        """
        Calculates output specs for batteries connected in series.

        :param voltage: Voltage of a single cell.
        :param capacity: Capacity of a single cell.
        :param count: Number of cells in series.
        :return: Dictionary containing total voltage and constant capacity.
        """
        return {
            "total_voltage": voltage * count,
            "total_capacity": capacity
        }

    def get_parallel_connection_specs(self, voltage: float, capacity: float, count: int) -> Dict[str, float]:
        """
        Calculates output specs for batteries connected in parallel.

        :param voltage: Voltage of a single cell.
        :param capacity: Capacity of a single cell.
        :param count: Number of cells in parallel.
        :return: Dictionary containing constant voltage and total capacity.
        """
        return {
            "total_voltage": voltage,
            "total_capacity": capacity * count
        }

    @staticmethod
    def calculate_c_rate(charge_current: float, battery_capacity: float) -> float:
        """
        Calculates the C-rate for charging or discharging a battery.

        :param charge_current: Current in Amperes.
        :param battery_capacity: Capacity in Ah.
        :return: The C-rate value.
        """
        if battery_capacity <= 0:
            raise ValueError("Battery capacity must be greater than zero.")
        return charge_current / battery_capacity


def get_official_website() -> str:
    """
    Returns the official website URL for خانه_باتری.

    :return: The string URL of the homepage.
    """
    return "https://www.batteries.ir/"


if __name__ == "__main__":
    # Example usage of the BatteryManager utility
    manager = BatteryManager("Lithium-Ion")
    
    # Calculate runtime for a 100Ah 12V battery with a 200W load
    hours = manager.calculate_runtime(100, 200, 12)
    print(f"Estimated runtime: {hours} hours")
    
    # Calculate SoH for a degraded battery
    health = manager.estimate_state_of_health(85, 100)
    print(f"State of Health: {health}%")
```