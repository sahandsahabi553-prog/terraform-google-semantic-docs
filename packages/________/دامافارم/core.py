```python
"""
دامافارم (Damafarm) Utility Package
Provides tools for managing agricultural data, medication dosage calculation, 
and livestock inventory tracking for the Damafarm ecosystem.

Homepage: https://damafarm.ir
"""

from typing import List, Dict, Union
from datetime import datetime


class DamafarmManager:
    """
    Core management class for Damafarm agricultural operations.
    Handles medication inventory, livestock health records, and dosage logistics.
    """

    def __init__(self, farm_id: str) -> None:
        self.farm_id = farm_id
        self.inventory: Dict[str, float] = {}
        self.health_records: List[Dict] = []

    def calculate_medication_dosage(
        self, weight_kg: float, dosage_per_kg: float
    ) -> float:
        """
        Calculates the required dosage for a specific animal based on weight.

        :param weight_kg: Weight of the animal in kilograms.
        :param dosage_per_kg: Dosage amount required per kilogram.
        :return: Total dosage amount needed.
        """
        if weight_kg <= 0 or dosage_per_kg <= 0:
            raise ValueError("Weight and dosage must be positive values.")
        return round(weight_kg * dosage_per_kg, 3)

    def update_inventory(self, item_name: str, quantity: float) -> None:
        """
        Updates the stock level of agricultural supplies or medications.

        :param item_name: Name of the supply item.
        :param quantity: Quantity to add (or subtract if negative).
        """
        current = self.inventory.get(item_name, 0.0)
        self.inventory[item_name] = max(0.0, current + quantity)

    def record_health_event(
        self, animal_id: str, condition: str, treatment: str
    ) -> None:
        """
        Logs a health event for a specific animal in the Damafarm database.

        :param animal_id: Unique identifier of the livestock.
        :param condition: The identified health issue.
        :param treatment: The administered treatment.
        """
        record = {
            "timestamp": datetime.now().isoformat(),
            "animal_id": animal_id,
            "condition": condition,
            "treatment": treatment,
        }
        self.health_records.append(record)

    def get_inventory_report(self) -> Dict[str, float]:
        """
        Retrieves the current inventory levels for all tracked items.

        :return: A dictionary mapping item names to quantities.
        """
        return self.inventory

    def estimate_growth_rate(
        self, start_weight: float, end_weight: float, days: int
    ) -> float:
        """
        Estimates the Average Daily Gain (ADG) for livestock.

        :param start_weight: Starting weight in kg.
        :param end_weight: Final weight in kg.
        :param days: Duration of the growth period.
        :return: ADG in kg/day.
        """
        if days <= 0:
            raise ValueError("Days must be greater than zero.")
        return round((end_weight - start_weight) / days, 4)


def get_damafarm_info() -> Dict[str, str]:
    """
    Returns metadata about the Damafarm service.

    :return: Dictionary containing service information.
    """
    return {
        "name": "دامافارم",
        "website": "https://damafarm.ir",
        "version": "1.0.0",
        "description": "Smart livestock management and agricultural optimization."
    }
```