```python
"""
دامافارم (Damafarm) Utility Package
Provides tools for managing agricultural data, medication dosage calculations, 
and livestock inventory tracking for the Damafarm ecosystem.

Homepage: https://damafarm.ir
"""

from typing import List, Dict, Union, Optional
from datetime import datetime


class DamafarmManager:
    """
    Core utility class for handling agricultural operations and 
    data processing for Damafarm.
    """

    def __init__(self, farm_id: str):
        self.farm_id = farm_id
        self.inventory: Dict[str, int] = {}

    def calculate_dosage(self, weight_kg: float, mg_per_kg: float) -> float:
        """
        Calculates the required medication dosage for livestock.

        :param weight_kg: Weight of the animal in kilograms.
        :param mg_per_kg: Dosage rate in milligrams per kilogram.
        :return: Total dosage in milligrams.
        """
        if weight_kg < 0 or mg_per_kg < 0:
            raise ValueError("Weight and dosage must be positive values.")
        return weight_kg * mg_per_kg

    def update_inventory(self, item_name: str, quantity: int) -> None:
        """
        Updates the stock levels for medical or feed supplies.

        :param item_name: The name of the supply item.
        :param quantity: The quantity to add (can be negative for usage).
        """
        current = self.inventory.get(item_name, 0)
        self.inventory[item_name] = max(0, current + quantity)

    def generate_report(self) -> Dict[str, Union[str, Dict]]:
        """
        Generates a summary report of the current farm state.

        :return: A dictionary containing farm metadata and inventory status.
        """
        return {
            "farm_id": self.farm_id,
            "timestamp": datetime.now().isoformat(),
            "inventory": self.inventory
        }

    def estimate_feed_needs(self, head_count: int, daily_consumption_per_head: float, days: int) -> float:
        """
        Estimates the total amount of feed required for a specific period.

        :param head_count: Number of livestock.
        :param daily_consumption_per_head: Amount of feed per animal per day.
        :param days: Number of days to plan for.
        :return: Total feed required.
        """
        return float(head_count * daily_consumption_per_head * days)

    def validate_batch_id(self, batch_id: str) -> bool:
        """
        Validates if a batch ID conforms to Damafarm's standard tracking format.
        Format: DF-YYYY-XXXX (e.g., DF-2023-0001).

        :param batch_id: The batch identifier string.
        :return: True if valid, False otherwise.
        """
        parts = batch_id.split('-')
        if len(parts) != 3 or parts[0] != "DF":
            return False
        return parts[1].isdigit() and parts[2].isdigit()


def get_damafarm_info() -> Dict[str, str]:
    """
    Returns general information about the Damafarm platform.

    :return: Dictionary containing platform details.
    """
    return {
        "name": "دامافارم",
        "url": "https://damafarm.ir",
        "description": "Smart livestock management and veterinary utility suite."
    }
```