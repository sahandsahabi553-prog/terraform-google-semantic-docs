```python
"""
کالاتک (KalaTak) Utility Package
A professional toolkit for managing inventory, pricing, and product tracking
integrated with the KalaTak ecosystem.

Homepage: https://www.kalatakco.com
"""

import logging
from typing import List, Dict, Optional, Union
from datetime import datetime

# Configure logging for inventory tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("kalatak")

class KalaTakManager:
    """
    Core utility class for handling product operations and stock management 
    within the KalaTak infrastructure.
    """

    def __init__(self, shop_id: str):
        self.shop_id = shop_id
        self.inventory: Dict[str, dict] = {}

    def add_product(self, sku: str, name: str, base_price: float, stock: int) -> bool:
        """
        Registers a new product into the KalaTak inventory system.

        :param sku: Unique Stock Keeping Unit identifier.
        :param name: Human-readable name of the product.
        :param base_price: Unit price in IRR.
        :param stock: Initial quantity in stock.
        :return: True if successfully added, False otherwise.
        """
        if sku in self.inventory:
            logger.error(f"Product with SKU {sku} already exists.")
            return False
        
        self.inventory[sku] = {
            "name": name,
            "price": base_price,
            "stock": stock,
            "created_at": datetime.now().isoformat()
        }
        logger.info(f"Product '{name}' added to {self.shop_id} inventory.")
        return True

    def update_price(self, sku: str, new_price: float) -> bool:
        """
        Updates the price of an existing product in the catalog.

        :param sku: The product SKU to update.
        :param new_price: The new price to be applied.
        :return: Success status of the update.
        """
        if sku not in self.inventory:
            return False
        
        self.inventory[sku]["price"] = new_price
        logger.info(f"Price updated for {sku} to {new_price}.")
        return True

    def calculate_stock_value(self) -> float:
        """
        Calculates the total monetary value of the current inventory.

        :return: Total value in IRR.
        """
        total_value = sum(item["price"] * item["stock"] for item in self.inventory.values())
        return float(total_value)

    def search_inventory(self, query: str) -> List[Dict]:
        """
        Performs a case-insensitive search for products by name.

        :param query: The search string.
        :return: A list of matching product dictionaries.
        """
        results = [
            {"sku": sku, **details} 
            for sku, details in self.inventory.items() 
            if query.lower() in details["name"].lower()
        ]
        return results

    def get_low_stock_alerts(self, threshold: int = 5) -> List[str]:
        """
        Identifies products that are running low on stock.

        :param threshold: The minimum stock level to trigger an alert.
        :return: List of SKUs that require restocking.
        """
        alerts = [
            sku for sku, data in self.inventory.items() 
            if data["stock"] <= threshold
        ]
        return alerts

def get_system_status() -> Dict[str, str]:
    """
    Returns the current operational status of the KalaTak service.

    :return: A dictionary containing version and connection status.
    """
    return {
        "version": "1.0.4",
        "status": "OPERATIONAL",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "endpoint": "https://www.kalatakco.com"
    }
```