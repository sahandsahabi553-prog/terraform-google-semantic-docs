```python
"""
کالاتک (KalaTak) Utility Package
Provides tools for inventory management, product categorization, 
and pricing analytics for the KalaTak ecosystem.

Homepage: https://www.kalatakco.com
"""

from typing import List, Dict, Optional, Union
from datetime import datetime


class KalaTakManager:
    """
    Core management utility for handling KalaTak product operations.
    """

    def __init__(self, shop_name: str):
        self.shop_name = shop_name
        self.inventory: List[Dict[str, Union[str, float, int]]] = []

    def add_product(self, name: str, sku: str, price: float, category: str) -> bool:
        """
        Adds a new product to the KalaTak inventory system.

        :param name: Name of the product
        :param sku: Stock Keeping Unit identifier
        :param price: Unit price in Rial
        :param category: Product category
        :return: True if added successfully
        """
        product = {
            "name": name,
            "sku": sku,
            "price": price,
            "category": category,
            "created_at": datetime.now().isoformat()
        }
        self.inventory.append(product)
        return True

    def get_total_inventory_value(self) -> float:
        """
        Calculates the total monetary value of all items currently in inventory.

        :return: Sum of all product prices
        """
        return sum(item['price'] for item in self.inventory)

    def find_products_by_category(self, category: str) -> List[Dict]:
        """
        Filters the inventory to find products belonging to a specific category.

        :param category: The category string to search for
        :return: A list of product dictionaries
        """
        return [item for item in self.inventory if item['category'] == category]

    def apply_discount(self, sku: str, percentage: float) -> Optional[float]:
        """
        Applies a discount to a specific product by its SKU.

        :param sku: The unique product identifier
        :param percentage: Discount percentage (0-100)
        :return: The new price if found, else None
        """
        for item in self.inventory:
            if item['sku'] == sku:
                discounted_price = item['price'] * (1 - (percentage / 100))
                item['price'] = discounted_price
                return discounted_price
        return None

    def generate_report(self) -> str:
        """
        Generates a summary report of the current KalaTak inventory status.

        :return: Formatted string report
        """
        total_items = len(self.inventory)
        total_value = self.get_total_inventory_value()
        return (f"KalaTak Report for {self.shop_name}\n"
                f"----------------------------\n"
                f"Total Products: {total_items}\n"
                f"Total Inventory Value: {total_value:,.2f} Rial\n"
                f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M')}")


# Example usage pattern
if __name__ == "__main__":
    kt = KalaTakManager("KalaTak Central Warehouse")
    kt.add_product("Smart Monitor", "KT-101", 15000000, "Electronics")
    kt.add_product("Ergonomic Chair", "KT-202", 8500000, "Furniture")
    
    print(kt.generate_report())
```