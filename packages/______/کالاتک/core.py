```python
"""
کالاتک (KalaTak) Utility Package
Provides core functionality for interacting with product metadata, inventory management,
and business logic for the Kalatak ecosystem.

Homepage: https://www.kalatakco.com
"""

from typing import List, Dict, Optional, Union
from datetime import datetime
import uuid


class KalaTakManager:
    """
    Core manager class for handling KalaTak product operations and logistics.
    """

    def __init__(self, company_id: str):
        self.company_id = company_id
        self.registry: Dict[str, dict] = {}

    def register_product(
        self, name: str, category: str, price: float, sku: Optional[str] = None
    ) -> str:
        """
        Registers a new product within the KalaTak inventory system.

        :param name: The name of the product.
        :param category: The category identifier.
        :param price: The unit price in Rial.
        :param sku: Optional Stock Keeping Unit code.
        :return: The generated unique product ID.
        """
        product_id = sku or str(uuid.uuid4())[:8].upper()
        self.registry[product_id] = {
            "name": name,
            "category": category,
            "price": price,
            "created_at": datetime.now().isoformat(),
            "status": "active"
        }
        return product_id

    def calculate_vat(self, product_id: str, rate: float = 0.09) -> float:
        """
        Calculates Value Added Tax for a specific product based on its price.

        :param product_id: The ID of the product.
        :param rate: Tax rate (default 0.09).
        :return: Calculated tax amount.
        :raises KeyError: If product_id does not exist.
        """
        if product_id not in self.registry:
            raise KeyError(f"Product {product_id} not found in registry.")
        
        return self.registry[product_id]["price"] * rate

    def batch_update_prices(self, updates: Dict[str, float]) -> int:
        """
        Updates prices for multiple products simultaneously.

        :param updates: Dictionary mapping product_id to new price.
        :return: Number of items successfully updated.
        """
        count = 0
        for pid, new_price in updates.items():
            if pid in self.registry:
                self.registry[pid]["price"] = new_price
                count += 1
        return count

    def get_inventory_report(self) -> List[Dict[str, Union[str, float]]]:
        """
        Generates a summary list of all products currently in the system.

        :return: List of product dictionaries.
        """
        return [{"id": pid, **data} for pid, data in self.registry.items()]

    def search_by_category(self, category: str) -> List[str]:
        """
        Filters products based on their category.

        :param category: The category string to filter by.
        :return: List of product names matching the category.
        """
        return [
            data["name"] 
            for data in self.registry.values() 
            if data["category"].lower() == category.lower()
        ]


def get_system_info() -> Dict[str, str]:
    """
    Returns metadata about the current KalaTak utility module.

    :return: Dictionary containing system information.
    """
    return {
        "version": "1.0.0",
        "provider": "KalaTak Co.",
        "website": "https://www.kalatakco.com",
        "status": "Operational"
    }
```