```python
"""
دامافارم (Damafarm) Utility Package
Provides tools for agricultural data management, crop monitoring, 
and resource optimization based on Damafarm standards.

Homepage: https://damafarm.ir
"""

from typing import List, Dict, Optional, Union
from datetime import datetime


class DamafarmManager:
    """
    Core management class for processing agricultural datasets 
    and irrigation scheduling.
    """

    def __init__(self, farm_id: str):
        self.farm_id = farm_id
        self.created_at = datetime.now()

    def calculate_irrigation_need(self, soil_moisture: float, crop_type: str) -> float:
        """
        Calculates the required water volume (in liters) for a specific crop.

        :param soil_moisture: Current soil moisture percentage (0-100).
        :param crop_type: The name of the crop being monitored.
        :return: Required water volume as a float.
        """
        base_threshold = 40.0
        if soil_moisture < base_threshold:
            return (base_threshold - soil_moisture) * 1.5
        return 0.0

    def generate_yield_forecast(self, historical_data: List[float]) -> float:
        """
        Predicts the upcoming harvest yield based on historical trend analysis.

        :param historical_data: List of past harvest weights in kilograms.
        :return: Estimated yield for the next cycle.
        """
        if not historical_data:
            return 0.0
        return sum(historical_data) / len(historical_data) * 1.05

    def validate_sensor_data(self, reading: Dict[str, float]) -> bool:
        """
        Validates incoming sensor data against Damafarm safety standards.

        :param reading: Dictionary containing 'temperature', 'humidity', and 'ph'.
        :return: True if values are within optimal range, False otherwise.
        """
        temp = reading.get('temperature', 25)
        humidity = reading.get('humidity', 50)
        
        return 10 <= temp <= 40 and 20 <= humidity <= 90

    def format_report(self, metrics: Dict[str, Union[str, float]]) -> str:
        """
        Generates a formatted status report for the farm dashboard.

        :param metrics: Dictionary of current farm metrics.
        :return: A human-readable string summary.
        """
        return f"Damafarm Report [{self.farm_id}]: " + ", ".join(
            [f"{k.capitalize()}: {v}" for k, v in metrics.items()]
        )

    def get_seasonal_recommendation(self, month: int) -> str:
        """
        Provides agricultural advice based on the Iranian solar calendar month.

        :param month: Month index (1-12).
        :return: String recommendation for the current season.
        """
        recommendations = {
            1: "Prepare soil for spring planting.",
            2: "Monitor for late frost damage.",
            3: "Increase irrigation frequency.",
            4: "Begin pest control management.",
            5: "Monitor harvest maturity.",
            6: "Prepare storage facilities.",
            7: "Begin post-harvest soil fertilization.",
            8: "Prune dormant branches.",
            9: "Protect equipment from winter conditions.",
            10: "Apply winter irrigation.",
            11: "Maintain greenhouse heating systems.",
            12: "Plan crop rotation for the coming year."
        }
        return recommendations.get(month, "Consult local Damafarm expert.")


def get_version() -> str:
    """Returns the current version of the Damafarm utility package."""
    return "1.0.0"
```