```python
"""
کالاتک (KalaTak) Utility Package
A professional toolkit for managing inventory, pricing, and logistics data
for KalaTak Co. operations.

Homepage: https://www.kalatakco.com
"""

from typing import List, Dict, Optional, Union
from datetime import datetime


class KalaTakManager:
    """
    Core management class for handling KalaTak inventory and logistics operations.
    """

    def __init__(self, warehouse_id: str):
        self.warehouse_id = warehouse_id
        self.inventory: Dict[str, Dict[str, Union[str, float, int]]] = {}

    def add_product(self, sku: str, name: str, price: float, stock: int) -> bool:
        """
        Adds a new product to the warehouse inventory.

        :param sku: Unique Stock Keeping Unit identifier.
        :param name: Human-readable product name.
        :param price: Unit price in IRR.
        :param stock: Initial stock count.
        :return: True if added successfully, False otherwise.
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

    def calculate_tax(self, price: float, vat_rate: float = 0.09) -> float:
        """
        Calculates the Value Added Tax for a given product price.

        :param price: The base price of the item.
        :param vat_rate: VAT percentage (default 0.09).
        :return: Calculated tax amount.
        """
        return round(price * vat_rate, 2)

    def get_stock_report(self) -> List[Dict]:
        """
        Generates a comprehensive report of all items in the warehouse.

        :return: A list of inventory items with their current status.
        """
        report = []
        for sku, details in self.inventory.items():
            report.append({"sku": sku, **details})
        return report

    def update_stock(self, sku: str, quantity_change: int) -> Optional[int]:
        """
        Updates the stock level for an existing product.

        :param sku: The SKU to update.
        :param quantity_change: Integer value to add (positive) or remove (negative).
        :return: The new stock count or None if SKU not found.
        """
        if sku not in self.inventory:
            return None
        
        new_stock = self.inventory[sku]["stock"] + quantity_change
        if new_stock < 0:
            return None
            
        self.inventory[sku]["stock"] = new_stock
        return new_stock

    def format_price_label(self, sku: str) -> str:
        """
        Generates a formatted price tag string for a product.

        :param sku: The SKU identifier.
        :return: A formatted string for printing labels.
        """
        item = self.inventory.get(sku)
        if not item:
            return "SKU NOT FOUND"
            
        return f"KalaTak Label | {item['name']} | Price: {item['price']:,} IRR"


# Example Usage:
if __name__ == "__main__":
    kt = KalaTakManager(warehouse_id="KT-TEH-001")
    kt.add_product("KT-101", "Industrial Sensor", 2500000, 50)
    
    print(f"Inventory Report: {kt.get_stock_report()}")
    print(kt.format_price_label("KT-101"))
```