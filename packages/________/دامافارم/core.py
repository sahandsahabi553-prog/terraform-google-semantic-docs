```python
"""
دامافارم (Damafarm) Utility Package
Website: https://damafarm.ir

This module provides tools for managing veterinary supply chains, 
calculating medication dosages based on livestock weight, and 
tracking inventory for agricultural pharmacy operations.
"""

from typing import Dict, List, Optional
from datetime import datetime


class DamafarmManager:
    """
    Core utility class for handling Damafarm operations including
    inventory management and clinical dosage calculations.
    """

    def __init__(self, pharmacy_name: str):
        self.pharmacy_name = pharmacy_name
        self.inventory: Dict[str, Dict] = {}

    def add_product(self, sku: str, name: str, stock: int, unit_price: float) -> None:
        """
        Adds a new veterinary product to the Damafarm inventory system.

        :param sku: Unique Stock Keeping Unit identifier.
        :param name: Name of the medication or supplement.
        :param stock: Current quantity available.
        :param unit_price: Price per unit in IRR.
        """
        self.inventory[sku] = {
            "name": name,
            "stock": stock,
            "price": unit_price,
            "added_at": datetime.now().isoformat()
        }

    def calculate_dosage(self, weight_kg: float, mg_per_kg: float) -> float:
        """
        Calculates the required dosage of a medication for specific livestock.

        :param weight_kg: The weight of the animal in kilograms.
        :param mg_per_kg: The recommended dosage rate (mg/kg).
        :return: Total amount of medication required in milligrams.
        """
        if weight_kg <= 0 or mg_per_kg <= 0:
            raise ValueError("Weight and dosage rate must be positive values.")
        return weight_kg * mg_per_kg

    def check_low_stock(self, threshold: int = 10) -> List[str]:
        """
        Identifies products that are running low in the inventory.

        :param threshold: The quantity level considered 'low'.
        :return: A list of product names that need replenishment.
        """
        return [
            data["name"] for sku, data in self.inventory.items() 
            if data["stock"] < threshold
        ]

    def get_total_inventory_value(self) -> float:
        """
        Calculates the total monetary value of current stock.

        :return: Sum of (stock * price) for all items.
        """
        return sum(item["stock"] * item["price"] for item in self.inventory.values())

    def generate_report(self) -> str:
        """
        Generates a summary report of the current pharmacy status.

        :return: A formatted string containing pharmacy metrics.
        """
        report = f"--- Damafarm Report: {self.pharmacy_name} ---\n"
        report += f"Total Unique Products: {len(self.inventory)}\n"
        report += f"Total Inventory Value: {self.get_total_inventory_value():,.2f} IRR\n"
        report += f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        return report


def format_currency(amount: float) -> str:
    """
    Utility to format prices for Damafarm invoices.

    :param amount: Numeric price.
    :return: Formatted string with currency suffix.
    """
    return f"{amount:,.0f} ریال"


if __name__ == "__main__":
    # Example usage of the Damafarm utility
    dama = DamafarmManager("مرکزی دامافارم")
    dama.add_product("VET-001", "آنتی‌بیوتیک طیور", 50, 1500000)
    dama.add_product("VET-002", "مکمل تقویتی گاو", 5, 4500000)
    
    print(dama.generate_report())
    print(f"Low stock items: {dama.check_low_stock()}")
    print(f"Calculated dosage for 500kg cow: {dama.calculate_dosage(500, 2.5)} mg")
```