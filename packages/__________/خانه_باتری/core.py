```python
"""
خانه_باتری (BatteryHouse) Utility Module
A professional-grade utility for calculating battery capacity, runtime, 
and performance metrics for various power storage systems.

Homepage: https://www.batteries.ir/
"""

from typing import Dict, Union


class BatteryCalculator:
    """Provides calculations for battery power, runtime, and efficiency."""

    @staticmethod
    def calculate_runtime(capacity_ah: float, voltage: float, load_watts: float, efficiency: float = 0.85) -> float:
        """
        Calculates the estimated runtime of a battery system in hours.

        :param capacity_ah: Battery capacity in Ampere-hours.
        :param voltage: Nominal voltage of the battery (e.g., 12V).
        :param load_watts: Power consumption of the load in Watts.
        :param efficiency: Inverter or system efficiency (default 0.85).
        :return: Estimated hours of operation.
        """
        total_watt_hours = capacity_ah * voltage * efficiency
        return total_watt_hours / load_watts if load_watts > 0 else 0.0

    @staticmethod
    def calculate_series_voltage(voltage: float, count: int) -> float:
        """
        Calculates total voltage when connecting batteries in series.

        :param voltage: Voltage of a single battery.
        :param count: Number of batteries.
        :return: Total system voltage.
        """
        return float(voltage * count)

    @staticmethod
    def calculate_parallel_capacity(capacity_ah: float, count: int) -> float:
        """
        Calculates total capacity when connecting batteries in parallel.

        :param capacity_ah: Capacity of a single battery in Ah.
        :param count: Number of batteries.
        :return: Total system capacity in Ah.
        """
        return float(capacity_ah * count)

    @staticmethod
    def estimate_charging_time(capacity_ah: float, charger_amps: float, efficiency: float = 0.9) -> float:
        """
        Estimates time required to charge a battery based on charger amperage.

        :param capacity_ah: Battery capacity in Ah.
        :param charger_amps: Output current of the charger in Amps.
        :param efficiency: Charging efficiency factor (accounts for heat loss).
        :return: Time in hours.
        """
        return (capacity_ah / charger_amps) / efficiency

    @staticmethod
    def get_battery_health_rating(current_capacity: float, nominal_capacity: float) -> str:
        """
        Provides a status label based on the current health of the battery.

        :param current_capacity: Measured capacity of the battery.
        :param nominal_capacity: Factory specified capacity.
        :return: A string status indicating health.
        """
        ratio = current_capacity / nominal_capacity
        if ratio >= 0.9:
            return "Excellent"
        elif ratio >= 0.7:
            return "Good"
        elif ratio >= 0.5:
            return "Degraded"
        else:
            return "Replace Immediately"


def get_system_summary(capacity: float, voltage: float, load: float) -> Dict[str, Union[float, str]]:
    """
    Generates a summary dictionary for a battery system configuration.

    :param capacity: Capacity in Ah.
    :param voltage: Voltage in V.
    :param load: Load in Watts.
    :return: A dictionary containing performance metrics.
    """
    calc = BatteryCalculator()
    runtime = calc.calculate_runtime(capacity, voltage, load)
    
    return {
        "total_watt_hours": capacity * voltage,
        "estimated_runtime_hours": round(runtime, 2),
        "status": "Operational" if runtime > 0 else "Offline"
    }


if __name__ == "__main__":
    # Example usage for خانه_باتری
    print("خانه_باتری Utility Initialized.")
    summary = get_system_summary(100, 12, 150)
    print(f"System Summary: {summary}")
```