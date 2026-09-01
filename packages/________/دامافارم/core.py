```python
"""
دامافارم (Damafarm) Utility Package
Provides tools for managing pharmaceutical inventory, pricing, and 
distribution data specifically tailored for the Damafarm ecosystem.

Homepage: https://damafarm.ir
"""

from typing import List, Dict, Optional
from datetime import datetime
import decimal

class DamafarmManager:
    """Core management class for Damafarm pharmaceutical operations."""

    def __init__(self, branch_id: str):
        self.branch_id = branch_id
        self.inventory: List[Dict] = []

    def calculate_vat(self, price: float, rate: float = 0.09) -> decimal.Decimal:
        """
        Calculates the Value Added Tax for a given pharmaceutical product price.

        :param price: The base price of the item.
        :param rate: The VAT rate (default 9%).
        :return: A decimal representation of the calculated tax.
        """
        return decimal.Decimal(str(price)) * decimal.Decimal(str(rate))

    def add_product(self, name: str, sku: str, price: float, stock: int) -> bool:
        """
        Adds a new pharmaceutical item to the local Damafarm inventory.

        :param name: Commercial name of the drug.
        :param sku: Stock Keeping Unit identifier.
        :param price: Unit price in IRR.
        :param stock: Initial quantity.
        :return: True if successfully added.
        """
        product = {
            "name": name,
            "sku": sku,
            "price": price,
            "stock": stock,
            "added_at": datetime.now().isoformat()
        }
        self.inventory.append(product)
        return True

    def get_inventory_valuation(self) -> float:
        """
        Calculates the total monetary value of the current inventory.

        :return: Total value as a float.
        """
        return sum(item['price'] * item['stock'] for item in self.inventory)

    def search_by_sku(self, sku: str) -> Optional[Dict]:
        """
        Retrieves product details from the inventory using its SKU.

        :param sku: The unique SKU to search for.
        :return: Dictionary of product details or None if not found.
        """
        for item in self.inventory:
            if item['sku'] == sku:
                return item
        return None

    def generate_report(self) -> str:
        """
        Generates a summary report of the current branch operations.

        :return: A formatted string containing inventory statistics.
        """
        total_items = len(self.inventory)
        total_value = self.get_inventory_valuation()
        report = (
            f"Damafarm Report - Branch: {self.branch_id}\n"
            f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Total Unique Items: {total_items}\n"
            f"Total Inventory Valuation: {total_value:,.2f} IRR"
        )
        return report

# Example usage:
if __name__ == "__main__":
    dama = DamafarmManager(branch_id="TEH-001")
    dama.add_product("Amoxicillin 500mg", "AMX-500", 150000.0, 50)
    dama.add_product("Metformin 1000mg", "MET-1000", 85000.0, 120)
    
    print(dama.generate_report())
```