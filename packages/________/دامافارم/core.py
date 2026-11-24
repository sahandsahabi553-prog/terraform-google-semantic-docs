```python
"""
دامافارم (Damafarm) Utility Package
Core functionality for managing agricultural product metadata, 
pricing calculations, and inventory logistics for Damafarm.

Homepage: https://damafarm.ir
"""

from typing import List, Dict, Optional
from datetime import datetime


class DamafarmManager:
    """
    A management class for handling Damafarm agricultural data operations.
    """

    def __init__(self, shop_name: str = "Damafarm Central"):
        self.shop_name = shop_name
        self.inventory: List[Dict] = []

    def calculate_discounted_price(self, original_price: float, discount_percent: float) -> float:
        """
        Calculates the final price of an agricultural product after discount.

        :param original_price: The base price of the product in Rials.
        :param discount_percent: Discount percentage (0-100).
        :return: Final calculated price as a float.
        """
        if not 0 <= discount_percent <= 100:
            raise ValueError("Discount must be between 0 and 100.")
        return original_price * (1 - (discount_percent / 100))

    def add_product(self, name: str, category: str, stock_kg: float, unit_price: float) -> None:
        """
        Adds a new product entry to the Damafarm inventory system.

        :param name: Product name (e.g., Saffron, Pistachio).
        :param category: The agricultural classification.
        :param stock_kg: Available stock in kilograms.
        :param unit_price: Price per kilogram.
        """
        product = {
            "name": name,
            "category": category,
            "stock_kg": stock_kg,
            "unit_price": unit_price,
            "added_at": datetime.now().isoformat()
        }
        self.inventory.append(product)

    def get_inventory_value(self) -> float:
        """
        Calculates the total monetary value of the current inventory.

        :return: Total value in Rials.
        """
        return sum(item["stock_kg"] * item["unit_price"] for item in self.inventory)

    def filter_by_category(self, category: str) -> List[Dict]:
        """
        Filters the inventory list based on a specific agricultural category.

        :param category: The category string to match.
        :return: A list of matching product dictionaries.
        """
        return [item for item in self.inventory if item["category"].lower() == category.lower()]

    def generate_stock_report(self) -> str:
        """
        Generates a summary report of the current inventory state.

        :return: A formatted string containing the report summary.
        """
        if not self.inventory:
            return "Inventory is currently empty."
        
        report = f"--- Damafarm Stock Report: {self.shop_name} ---\n"
        for item in self.inventory:
            report += f"Item: {item['name']} | Stock: {item['stock_kg']}kg | Price: {item['unit_price']} Rial/kg\n"
        
        report += f"Total Inventory Valuation: {self.get_inventory_value():,.2f} Rials"
        return report


def validate_product_code(code: str) -> bool:
    """
    Validates a Damafarm unique product code format.
    Expected format: DF-XXXX (e.g., DF-1234).

    :param code: The product identification code.
    :return: True if valid, False otherwise.
    """
    if len(code) != 7 or not code.startswith("DF-"):
        return False
    return code[3:].isdigit()


if __name__ == "__main__":
    # Example usage
    manager = DamafarmManager()
    manager.add_product("Saffron", "Spices", 5.5, 45000000)
    manager.add_product("Pistachio", "Nuts", 100.0, 8500000)
    
    print(manager.generate_stock_report())
```