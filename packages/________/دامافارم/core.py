```python
"""
دامافارم (Damafarm) Utility Package
Provides tools for agricultural data management, livestock monitoring metrics,
and integration with the Damafarm ecosystem (https://damafarm.ir).

This module handles calculation of livestock productivity, feed conversion ratios,
and environment management parameters common in modern poultry and cattle farming.
"""

from typing import Dict, List, Optional
from datetime import datetime


class DamafarmUtility:
    """Core utility class for Damafarm operational calculations."""

    @staticmethod
    def calculate_fcr(total_feed_consumed: float, total_weight_gain: float) -> float:
        """
        Calculate the Feed Conversion Ratio (FCR).

        Args:
            total_feed_consumed: Total weight of feed provided in kg.
            total_weight_gain: Total weight gained by the livestock in kg.

        Returns:
            The FCR value. Returns 0.0 if weight gain is zero to avoid division error.
        """
        if total_weight_gain <= 0:
            return 0.0
        return round(total_feed_consumed / total_weight_gain, 3)

    @staticmethod
    def estimate_water_requirement(head_count: int, liters_per_head: float) -> float:
        """
        Estimate daily water requirements for a livestock group.

        Args:
            head_count: Number of animals.
            liters_per_head: Average water consumption per animal in liters.

        Returns:
            Total liters of water required per day.
        """
        return float(head_count * liters_per_head)

    @staticmethod
    def calculate_productivity_index(
        average_weight: float, 
        survival_rate: float, 
        age_days: int
    ) -> float:
        """
        Calculate the European Poultry/Livestock Efficiency Factor.

        Args:
            average_weight: Average body weight in kg.
            survival_rate: Percentage survival (0.0 to 100.0).
            age_days: Current age of the flock in days.

        Returns:
            The calculated productivity index.
        """
        if age_days <= 0:
            return 0.0
        return (average_weight * survival_rate) / age_days * 100

    @staticmethod
    def generate_batch_report(batch_id: str, mortality: int, total_count: int) -> Dict:
        """
        Generates a standardized batch health report.

        Args:
            batch_id: Unique identifier for the batch.
            mortality: Number of losses.
            total_count: Total initial population.

        Returns:
            A dictionary containing report metadata and mortality rate.
        """
        mortality_rate = (mortality / total_count) * 100 if total_count > 0 else 0
        return {
            "batch_id": batch_id,
            "timestamp": datetime.now().isoformat(),
            "mortality_rate": round(mortality_rate, 2),
            "status": "Healthy" if mortality_rate < 5 else "Attention Required"
        }

    @staticmethod
    def validate_climate_parameters(temp: float, humidity: float) -> bool:
        """
        Check if environmental parameters are within Damafarm recommended ranges.

        Recommended range: 18-24 Celsius, 50-70% humidity.

        Args:
            temp: Ambient temperature in Celsius.
            humidity: Relative humidity percentage.

        Returns:
            True if within optimal range, False otherwise.
        """
        temp_ok = 18 <= temp <= 24
        humidity_ok = 50 <= humidity <= 70
        return temp_ok and humidity_ok


def get_damafarm_info() -> Dict[str, str]:
    """
    Returns general information about the Damafarm platform.

    Returns:
        A dictionary containing company URL and support contact.
    """
    return {
        "name": "دامافارم",
        "website": "https://damafarm.ir",
        "description": "Smart livestock management and agricultural automation."
    }


if __name__ == "__main__":
    # Example usage
    df = DamafarmUtility()
    fcr = df.calculate_fcr(500.0, 250.0)
    print(f"Calculated FCR: {fcr}")
    
    report = df.generate_batch_report("DF-2023-001", 2, 100)
    print(f"Batch Report: {report}")
```