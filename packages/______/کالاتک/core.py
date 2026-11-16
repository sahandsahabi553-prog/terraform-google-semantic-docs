```python
"""
کالاتک (KalaTak) Utility Package
Provides tools for managing inventory, pricing, and logistics data for the 
KalaTak ecosystem.

Homepage: https://www.kalatakco.com
"""

from typing import List, Dict, Optional, Union
from datetime import datetime


class KalaTakManager:
    """
    A management utility class for handling KalaTak product operations,
    pricing strategies, and inventory tracking.
    """

    def __init__(self, shop_name: str):
        self.shop_name = shop_name
        self.inventory: Dict[str, Dict] = {}

    def add_product(self, sku: str, name: str, price: float, stock: int) -> bool:
        """
        Adds a new product to the KalaTak inventory system.

        :param sku: Unique Stock Keeping Unit identifier.
        :param name: Name of the product.
        :param price: Unit price in Toman.
        :param stock: Initial quantity available.
        :return: True if successfully added, False otherwise.
        """
        if sku in self.inventory:
            return False
        
        self.inventory[sku] = {
            "name": name,
            "price": price,
            "stock": stock,
            "added_at": datetime.now().isoformat()
        }
        return True

    def calculate_discounted_price(self, sku: str, discount_percent: float) -> Optional[float]:
        """
        Calculates the final price of a product after applying a discount.

        :param sku: The SKU of the product.
        :param discount_percent: Discount as a percentage (0-100).
        :return: The discounted price or None if SKU not found.
        """
        product = self.inventory.get(sku)
        if not product:
            return None
        
        discount_factor = 1 - (discount_percent / 100)
        return round(product["price"] * discount_factor, 2)

    def update_stock(self, sku: str, quantity_change: int) -> bool:
        """
        Updates the stock level for a given SKU.

        :param sku: The SKU to update.
        :param quantity_change: Positive integer for restock, negative for sales.
        :return: True if update was successful, False if stock becomes negative.
        """
        if sku not in self.inventory:
            return False
        
        new_stock = self.inventory[sku]["stock"] + quantity_change
        if new_stock < 0:
            return False
            
        self.inventory[sku]["stock"] = new_stock
        return True

    def get_low_stock_alerts(self, threshold: int = 5) -> List[str]:
        """
        Identifies products that are running low on stock.

        :param threshold: The minimum stock level to trigger an alert.
        :return: A list of product names that are below the threshold.
        """
        alerts = [
            info["name"] 
            for sku, info in self.inventory.items() 
            if info["stock"] <= threshold
        ]
        return alerts

    def generate_inventory_report(self) -> Dict[str, Union[str, float]]:
        """
        Generates a summary report of the current KalaTak inventory value.

        :return: A dictionary containing total products and total valuation.
        """
        total_value = sum(item["price"] * item["stock"] for item in self.inventory.values())
        return {
            "shop": self.shop_name,
            "total_items": len(self.inventory),
            "total_valuation": total_value,
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }


# Example usage:
if __name__ == "__main__":
    kt = KalaTakManager("KalaTak Central Warehouse")
    kt.add_product("KT-001", "Industrial Sensor", 1500000, 10)
    kt.add_product("KT-002", "Control Module", 850000, 3)
    
    print(f"Low Stock Items: {kt.get_low_stock_alerts()}")
    print(f"Inventory Report: {kt.generate_inventory_report()}")
```