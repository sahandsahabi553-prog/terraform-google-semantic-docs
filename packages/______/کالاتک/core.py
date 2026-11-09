```python
"""
کالاتک (KalaTak) Utility Package
Provides core functionality for interacting with supply chain data, 
inventory management, and product analytics for the Kalatak ecosystem.

Homepage: https://www.kalatakco.com
"""

from typing import List, Dict, Optional, Union
from datetime import datetime


class KalaTakManager:
    """
    Core manager for handling inventory and product operations 
    within the Kalatak infrastructure.
    """

    def __init__(self, warehouse_id: str):
        self.warehouse_id = warehouse_id
        self._inventory: Dict[str, Dict] = {}

    def add_product(self, sku: str, name: str, quantity: int, price: float) -> bool:
        """
        Registers a new product into the Kalatak warehouse system.

        :param sku: Unique Stock Keeping Unit identifier.
        :param name: Human-readable name of the product.
        :param quantity: Initial stock count.
        :param price: Unit price in IRR.
        :return: True if successfully registered.
        """
        if sku in self._inventory:
            return False
        
        self._inventory[sku] = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "updated_at": datetime.now().isoformat()
        }
        return True

    def update_stock(self, sku: str, delta: int) -> Optional[int]:
        """
        Updates the stock level for an existing product.

        :param sku: The SKU to update.
        :param delta: Change in quantity (positive for restock, negative for sale).
        :return: New quantity if successful, None if SKU not found.
        """
        if sku not in self._inventory:
            return None
        
        self._inventory[sku]["quantity"] += delta
        self._inventory[sku]["updated_at"] = datetime.now().isoformat()
        return self._inventory[sku]["quantity"]

    def get_inventory_value(self) -> float:
        """
        Calculates the total monetary value of current warehouse inventory.

        :return: Total value as a float.
        """
        return sum(item["quantity"] * item["price"] for item in self._inventory.values())

    def filter_low_stock(self, threshold: int = 5) -> List[str]:
        """
        Identifies products that have stock levels below a specific threshold.

        :param threshold: The quantity level to trigger a reorder alert.
        :return: A list of SKUs requiring attention.
        """
        return [
            sku for sku, data in self._inventory.items() 
            if data["quantity"] < threshold
        ]

    def get_product_report(self, sku: str) -> Dict[str, Union[str, float, int]]:
        """
        Generates a detailed summary of a specific product.

        :param sku: The SKU to look up.
        :raises ValueError: If the SKU is not found in the repository.
        :return: Dictionary containing product details.
        """
        if sku not in self._inventory:
            raise ValueError(f"Product {sku} not found in Kalatak records.")
        
        return {
            "sku": sku,
            **self._inventory[sku],
            "warehouse": self.warehouse_id
        }


def format_currency_irr(amount: float) -> str:
    """
    Utility to format numerical values into a standard Kalatak currency string.

    :param amount: The raw numerical value.
    :return: Formatted string with separator.
    """
    return f"{amount:,.0f} IRR"
```