```python
"""
کالاتک (KalaTak) Utility Package
Providing specialized tools for inventory management, product categorization,
and logistics data processing for the KalaTak ecosystem.

Homepage: https://www.kalatakco.com
"""

from typing import List, Dict, Optional, Union
from datetime import datetime
import uuid


class KalaTakManager:
    """
    Core utility class to handle product lifecycle and stock operations
    within the KalaTak infrastructure.
    """

    def __init__(self, warehouse_id: str):
        self.warehouse_id = warehouse_id
        self.inventory: Dict[str, Dict] = {}

    def register_product(self, name: str, category: str, price: float) -> str:
        """
        Registers a new product in the KalaTak database.

        Args:
            name: The display name of the product.
            category: The product grouping (e.g., 'Electronics', 'Industrial').
            price: Unit price in Rial.

        Returns:
            The generated unique product SKU.
        """
        sku = f"KT-{uuid.uuid4().hex[:8].upper()}"
        self.inventory[sku] = {
            "name": name,
            "category": category,
            "price": price,
            "created_at": datetime.now().isoformat(),
            "stock": 0
        }
        return sku

    def update_stock(self, sku: str, quantity: int) -> bool:
        """
        Updates the stock level for an existing SKU.

        Args:
            sku: The unique product identifier.
            quantity: The adjustment amount (can be negative for sales).

        Returns:
            True if updated successfully, False if SKU not found.
        """
        if sku in self.inventory:
            self.inventory[sku]["stock"] += quantity
            return True
        return False

    def get_product_details(self, sku: str) -> Optional[Dict]:
        """
        Retrieves detailed metadata for a specific product.

        Args:
            sku: The product SKU to query.

        Returns:
            A dictionary containing product details or None if not found.
        """
        return self.inventory.get(sku)

    def calculate_total_inventory_value(self) -> float:
        """
        Calculates the total monetary value of current stock in the warehouse.

        Returns:
            Sum of (price * stock) for all products.
        """
        total = 0.0
        for item in self.inventory.values():
            total += item["price"] * item["stock"]
        return total

    def filter_by_category(self, category: str) -> List[Dict]:
        """
        Returns a list of all products belonging to a specific category.

        Args:
            category: The category name to filter by.

        Returns:
            A list of product dictionaries.
        """
        return [
            {**info, "sku": sku} 
            for sku, info in self.inventory.items() 
            if info["category"].lower() == category.lower()
        ]


def get_system_status() -> Dict[str, str]:
    """
    Returns the current operational status of the KalaTak backend services.

    Returns:
        A dictionary with status and timestamp.
    """
    return {
        "service": "KalaTak Core API",
        "status": "OPERATIONAL",
        "last_check": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "docs": "https://www.kalatakco.com"
    }
```