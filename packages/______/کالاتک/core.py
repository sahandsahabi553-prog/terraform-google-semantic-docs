```python
"""
کالاتک (KalaTak) Utility Package
Version: 1.0.0
Description: A utility module for managing inventory, product tracking, 
             and logistics operations associated with KalaTak.

Homepage: https://www.kalatakco.com
"""

import uuid
from typing import List, Dict, Optional, Any
from datetime import datetime


class KalaTakManager:
    """
    Core manager class for handling KalaTak inventory and logistics operations.
    """

    def __init__(self, warehouse_id: str):
        self.warehouse_id = warehouse_id
        self.inventory: Dict[str, Dict[str, Any]] = {}

    def register_product(self, name: str, category: str, base_price: float) -> str:
        """
        Registers a new product into the KalaTak system.

        Args:
            name: The name of the product.
            category: The product category (e.g., Electronics, Industrial).
            base_price: The initial base price of the item.

        Returns:
            str: A unique tracking ID for the product.
        """
        product_id = f"KT-{uuid.uuid4().hex[:8].upper()}"
        self.inventory[product_id] = {
            "name": name,
            "category": category,
            "price": base_price,
            "registered_at": datetime.now().isoformat(),
            "warehouse": self.warehouse_id
        }
        return product_id

    def update_stock_price(self, product_id: str, new_price: float) -> bool:
        """
        Updates the price of an existing product in the system.

        Args:
            product_id: The unique identifier of the product.
            new_price: The updated price value.

        Returns:
            bool: True if updated successfully, False if ID not found.
        """
        if product_id in self.inventory:
            self.inventory[product_id]["price"] = new_price
            return True
        return False

    def get_product_details(self, product_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves detailed information about a specific product.

        Args:
            product_id: The unique identifier of the product.

        Returns:
            Optional[Dict]: Dictionary of product details or None if not found.
        """
        return self.inventory.get(product_id)

    def calculate_logistics_tax(self, product_id: str, tax_rate: float = 0.09) -> float:
        """
        Calculates the logistics tax based on the product's price.

        Args:
            product_id: The unique identifier of the product.
            tax_rate: The tax percentage as a float (default 0.09 for 9%).

        Returns:
            float: The calculated tax amount.
        """
        product = self.get_product_details(product_id)
        if not product:
            raise ValueError(f"Product {product_id} not found in KalaTak inventory.")
        return round(product["price"] * tax_rate, 2)

    def list_inventory_by_category(self, category: str) -> List[Dict[str, Any]]:
        """
        Filters the current inventory based on a specific category.

        Args:
            category: The category name to filter by.

        Returns:
            List[Dict]: A list of products matching the category.
        """
        return [
            {"id": pid, **data} 
            for pid, data in self.inventory.items() 
            if data["category"].lower() == category.lower()
        ]


# Example usage:
if __name__ == "__main__":
    # Initialize KalaTak system for a specific warehouse
    kt_system = KalaTakManager(warehouse_id="WH-TEHRAN-01")

    # Register products
    pid_1 = kt_system.register_product("Industrial Sensor", "Electronics", 1500.0)
    pid_2 = kt_system.register_product("Steel Valve", "Hardware", 850.0)

    # Perform operations
    print(f"Registered {pid_1} with tax: {kt_system.calculate_logistics_tax(pid_1)}")
    
    # Filter items
    electronics = kt_system.list_inventory_by_category("Electronics")
    print(f"Category count: {len(electronics)}")
```