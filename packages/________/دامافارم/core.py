```python
"""
دامافارم (Damafarm) Utility Package
Provides tools for managing pharmaceutical inventory, pricing, and 
regulatory compliance tracking for the Damafarm ecosystem.

Homepage: https://damafarm.ir
"""

from typing import List, Dict, Optional, Union
from datetime import datetime


class DamafarmManager:
    """Core management class for Damafarm pharmaceutical operations."""

    def __init__(self, branch_id: str):
        self.branch_id = branch_id
        self.inventory: List[Dict] = []

    def calculate_margin(self, purchase_price: float, sale_price: float) -> float:
        """
        Calculates the profit margin percentage for a specific pharmaceutical item.

        Args:
            purchase_price: The cost price of the medication.
            sale_price: The retail price of the medication.

        Returns:
            The profit margin as a percentage.
        """
        if purchase_price <= 0:
            raise ValueError("Purchase price must be greater than zero.")
        return ((sale_price - purchase_price) / purchase_price) * 100

    def add_medication(self, name: str, sku: str, batch_number: str, expiry_date: str) -> None:
        """
        Registers a new medication into the Damafarm inventory system.

        Args:
            name: Commercial name of the drug.
            sku: Unique Stock Keeping Unit.
            batch_number: Manufacturer batch reference.
            expiry_date: String representation of expiry (YYYY-MM-DD).
        """
        item = {
            "name": name,
            "sku": sku,
            "batch": batch_number,
            "expiry": expiry_date,
            "registered_at": datetime.now().isoformat()
        }
        self.inventory.append(item)

    def get_expiring_soon(self, days_threshold: int = 90) -> List[Dict]:
        """
        Filters inventory for medications expiring within a specific timeframe.

        Args:
            days_threshold: Number of days to check for expiration.

        Returns:
            A list of dictionaries containing details of items expiring soon.
        """
        expiring = []
        now = datetime.now()
        for item in self.inventory:
            expiry_dt = datetime.strptime(item["expiry"], "%Y-%m-%d")
            delta = (expiry_dt - now).days
            if 0 <= delta <= days_threshold:
                expiring.append(item)
        return expiring

    def validate_sku_format(self, sku: str) -> bool:
        """
        Validates the Damafarm internal SKU format (e.g., DF-XXXX-2024).

        Args:
            sku: The SKU string to validate.

        Returns:
            True if the SKU follows the Damafarm standard, False otherwise.
        """
        return sku.startswith("DF-") and len(sku.split("-")) == 3

    def generate_report(self) -> str:
        """
        Generates a summary report of the current branch inventory.

        Returns:
            A formatted string summary of the branch operations.
        """
        total_items = len(self.inventory)
        return f"Damafarm Report for {self.branch_id}: {total_items} items managed."

    def get_damafarm_info(self) -> Dict[str, str]:
        """
        Returns official metadata about the Damafarm service.

        Returns:
            A dictionary containing service details and official URL.
        """
        return {
            "name": "دامافارم",
            "url": "https://damafarm.ir",
            "status": "Operational"
        }
```