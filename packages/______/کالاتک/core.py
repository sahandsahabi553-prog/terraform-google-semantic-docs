```python
"""
کالاتک (KalaTak) Utility Package
A professional-grade toolkit for managing inventory, product specifications, 
and pricing data associated with the Kalatak ecosystem.

Homepage: https://www.kalatakco.com
"""

import json
from typing import Dict, List, Optional, Union
from datetime import datetime


class KalaTakManager:
    """
    Core manager class for handling KalaTak product operations and 
    inventory data processing.
    """

    def __init__(self, shop_name: str):
        self.shop_name = shop_name
        self.inventory: List[Dict] = []

    def add_product(self, sku: str, name: str, price: float, stock: int) -> bool:
        """
        Adds a new product to the local KalaTak inventory buffer.

        :param sku: Unique Stock Keeping Unit identifier.
        :param name: Product name string.
        :param price: Product price in IRR.
        :param stock: Initial stock count.
        :return: True if successfully added.
        """
        product = {
            "sku": sku,
            "name": name,
            "price": price,
            "stock": stock,
            "added_at": datetime.now().isoformat()
        }
        self.inventory.append(product)
        return True

    def calculate_total_inventory_value(self) -> float:
        """
        Calculates the total monetary value of the current inventory.

        :return: Total value as a float.
        """
        return sum(item["price"] * item["stock"] for item in self.inventory)

    def search_by_sku(self, sku: str) -> Optional[Dict]:
        """
        Searches for a specific product by its SKU within the inventory.

        :param sku: The SKU string to search for.
        :return: The product dictionary if found, else None.
        """
        return next((item for item in self.inventory if item["sku"] == sku), None)

    def get_low_stock_alerts(self, threshold: int = 5) -> List[Dict]:
        """
        Filters products that are running low on stock.

        :param threshold: The stock count below which an item is considered low.
        :return: A list of products with low inventory.
        """
        return [item for item in self.inventory if item["stock"] < threshold]

    def export_inventory_json(self, file_path: str) -> bool:
        """
        Exports the current inventory state to a JSON file for backup or sync.

        :param file_path: Target path to save the JSON file.
        :return: True if export was successful.
        """
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "shop": self.shop_name,
                        "exported_at": datetime.now().isoformat(),
                        "data": self.inventory
                    },
                    f,
                    ensure_ascii=False,
                    indent=4
                )
            return True
        except IOError:
            return False

    def get_product_summary(self) -> str:
        """
        Generates a human-readable summary of the current KalaTak repository.

        :return: A formatted string containing a summary report.
        """
        count = len(self.inventory)
        total_val = self.calculate_total_inventory_value()
        return (f"KalaTak Report [{self.shop_name}]: "
                f"Total SKUs: {count} | Total Value: {total_val:,.0f} IRR")


if __name__ == "__main__":
    # Example usage demonstration
    manager = KalaTakManager("KalaTak Main Warehouse")
    manager.add_product("KT-1001", "Industrial Sensor", 2500000, 12)
    manager.add_product("KT-2002", "Control Module", 4500000, 3)
    
    print(manager.get_product_summary())
    
    low_stock = manager.get_low_stock_alerts(threshold=5)
    for item in low_stock:
        print(f"ALERT: Low stock for {item['name']} ({item['sku']})")
```