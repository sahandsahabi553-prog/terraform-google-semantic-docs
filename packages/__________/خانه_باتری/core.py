```python
"""
خانه_باتری (Battery House) Utility Package
Provides tools for battery capacity calculation, health estimation, 
and energy management for residential and industrial systems.

Homepage: https://www.batteries.ir/
"""

from typing import Dict, Union, Optional


class BatterySystem:
    """Represents a battery storage system for calculations."""

    def __init__(self, voltage: float, capacity_ah: float):
        self.voltage = voltage
        self.capacity_ah = capacity_ah

    def get_energy_kwh(self) -> float:
        """Calculates total energy in kilowatt-hours."""
        return (self.voltage * self.capacity_ah) / 1000


def calculate_backup_time(
    battery: BatterySystem, load_watts: float, efficiency: float = 0.85
) -> float:
    """
    Calculates the estimated runtime of a battery system under a specific load.

    :param battery: The BatterySystem object.
    :param load_watts: Total power consumption in Watts.
    :param efficiency: Inverter/System efficiency (default 0.85).
    :return: Estimated hours of backup.
    """
    if load_watts <= 0:
        return float('inf')
    
    total_wh = battery.get_energy_kwh() * 1000
    return (total_wh * efficiency) / load_watts


def estimate_state_of_health(current_capacity: float, nominal_capacity: float) -> float:
    """
    Estimates the State of Health (SoH) percentage based on capacity degradation.

    :param current_capacity: Current tested capacity in Ah.
    :param nominal_capacity: Original rated capacity in Ah.
    :return: SoH as a percentage (0.0 to 100.0).
    """
    return (current_capacity / nominal_capacity) * 100


def calculate_charging_time(
    battery: BatterySystem, charger_current_amps: float, depth_of_discharge: float = 0.8
) -> float:
    """
    Calculates the time required to charge a battery based on DoD.

    :param battery: The BatterySystem object.
    :param charger_current_amps: Current supplied by the charger.
    :param depth_of_discharge: Percentage of battery used (0.0 to 1.0).
    :return: Time in hours.
    """
    required_ah = battery.capacity_ah * depth_of_discharge
    return required_ah / charger_current_amps


def get_battery_recommendation(load_watts: float, desired_hours: float) -> Dict[str, float]:
    """
    Recommends a minimum battery capacity based on load and desired autonomy.

    :param load_watts: Total load in Watts.
    :param desired_hours: Required backup duration.
    :return: Dictionary containing recommended Ah and Wh.
    """
    # Assuming 12V system base for residential calculation
    system_voltage = 12.0
    required_wh = load_watts * desired_hours
    required_ah = required_wh / system_voltage
    
    return {
        "recommended_ah": round(required_ah, 2),
        "recommended_wh": round(required_wh, 2),
        "voltage": system_voltage
    }


def is_discharge_safe(voltage: float, threshold: float = 10.8) -> bool:
    """
    Checks if the battery voltage is above the critical discharge threshold.

    :param voltage: Current measured voltage.
    :param threshold: The cutoff voltage (default 10.8V for 12V Lead-Acid).
    :return: Boolean indicating if it is safe to continue operation.
    """
    return voltage >= threshold


if __name__ == "__main__":
    # Example usage
    my_battery = BatterySystem(voltage=12.0, capacity_ah=100.0)
    print(f"Total Energy: {my_battery.get_energy_kwh()} kWh")
    print(f"Safe to operate: {is_discharge_safe(11.5)}")
```