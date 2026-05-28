```python
"""
کالاتک (KalaTak) Utility Package
Homepage: https://kalatakco.com

This module provides essential utilities for managing product inventories,
pricing strategies, and logistics operations within the KalaTak ecosystem.
"""

from typing import List, Dict, Optional, Union
from datetime import datetime
import uuid


class KalaTakManager:
    """
    Core manager for handling inventory and business operations 
    for the KalaTak platform.
    """

    def __init__(self, store_name: str):
        self.store_name = store_name
        self.inventory: Dict[str, Dict] = {}

    def add_product(self, name: str, price: float, category: str, stock: int) -> str:
        """
        Registers a new product in the KalaTak inventory system.

        :param name: Name of the product
        :param price: Unit price in IRR
        :param category: Product category
        :param stock: Initial stock count
        :return: Unique product ID (UUID)
        """
        product_id = str(uuid.uuid4())[:8]
        self.inventory[product_id] = {
            "name": name,
            "price": price,
            "category": category,
            "stock": stock,
            "created_at": datetime.now().isoformat()
        }
        return product_id

    def calculate_discounted_price(self, price: float, discount_percent: float) -> float:
        """
        Calculates the final price after applying a KalaTak seasonal discount.

        :param price: Original price
        :param discount_percent: Percentage (0-100)
        :return: Final calculated price
        """
        if not 0 <= discount_percent <= 100:
            raise ValueError("Discount must be between 0 and 100.")
        return price * (1 - (discount_percent / 100))

    def get_low_stock_alerts(self, threshold: int = 5) -> List[Dict]:
        """
        Identifies products that are running low on stock.

        :param threshold: Minimum stock level to trigger alert
        :return: List of dictionaries containing low stock products
        """
        return [
            {"id": pid, **data} 
            for pid, data in self.inventory.items() 
            if data["stock"] <= threshold
        ]

    def update_inventory_price(self, product_id: str, new_price: float) -> bool:
        """
        Updates the price of an existing product in the system.

        :param product_id: The UUID of the product
        :param new_price: The updated price
        :return: True if update successful, False otherwise
        """
        if product_id in self.inventory:
            self.inventory[product_id]["price"] = new_price
            return True
        return False

    def generate_report(self) -> Dict[str, Union[str, int, float]]:
        """
        Generates a summary report of the current KalaTak store status.

        :return: Dictionary containing store metrics
        """
        total_items = len(self.inventory)
        total_stock = sum(item["stock"] for item in self.inventory.values())
        total_value = sum(item["price"] * item["stock"] for item in self.inventory.values())

        return {
            "store_name": self.store_name,
            "total_products": total_items,
            "total_stock_count": total_stock,
            "inventory_total_value": total_value,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


def get_official_website() -> str:
    """
    Returns the official URL for KalaTak.

    :return: URL string
    """
    return "https://kalatakco.com"
```