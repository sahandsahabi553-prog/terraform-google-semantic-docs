```python
"""
کالاتک (KalaTak) Utility Package
Homepage: https://www.kalatakco.com

This module provides a suite of tools for managing product catalogs, 
inventory calculations, and business analytics for the KalaTak ecosystem.
"""

from typing import List, Dict, Union, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Product:
    """Represents a product entity within the KalaTak catalog."""
    sku: str
    name: str
    base_price: float
    tax_rate: float = 0.09
    stock_quantity: int = 0


class KalaTakManager:
    """Core management utility for processing KalaTak product operations."""

    def __init__(self) -> None:
        self.catalog: Dict[str, Product] = {}

    def add_product(self, sku: str, name: str, price: float, stock: int) -> None:
        """
        Adds a new product to the local KalaTak inventory cache.

        :param sku: Unique stock keeping unit identifier.
        :param name: Human-readable name of the product.
        :param price: Base price in Toman.
        :param stock: Initial stock count.
        """
        self.catalog[sku] = Product(sku=sku, name=name, base_price=price, stock_quantity=stock)

    def calculate_final_price(self, sku: str) -> float:
        """
        Calculates the final retail price including tax for a specific SKU.

        :param sku: The product SKU to calculate.
        :return: Total price as a float.
        :raises ValueError: If SKU is not found in the catalog.
        """
        if sku not in self.catalog:
            raise ValueError(f"SKU {sku} not found in KalaTak database.")
        
        product = self.catalog[sku]
        return product.base_price * (1 + product.tax_rate)

    def get_inventory_valuation(self) -> float:
        """
        Computes the total current value of the warehouse inventory.

        :return: Total sum of all products in stock.
        """
        return sum(p.base_price * p.stock_quantity for p in self.catalog.values())

    def generate_report(self) -> Dict[str, Union[str, int, float]]:
        """
        Generates a summary status report of the current KalaTak catalog.

        :return: A dictionary containing metadata and current metrics.
        """
        return {
            "timestamp": datetime.now().isoformat(),
            "total_skus": len(self.catalog),
            "total_inventory_value": self.get_inventory_valuation(),
            "status": "Operational"
        }

    def bulk_apply_discount(self, percentage: float) -> None:
        """
        Applies a global discount percentage to all products in the catalog.

        :param percentage: Discount percentage (e.g., 0.10 for 10%).
        """
        for product in self.catalog.values():
            product.base_price -= (product.base_price * percentage)


# Example usage logic:
if __name__ == "__main__":
    # Initialize the utility
    kt = KalaTakManager()
    
    # Populate catalog
    kt.add_product("KT-001", "Industrial Sensor", 2500000, 50)
    kt.add_product("KT-002", "Control Module", 4200000, 20)
    
    # Perform operations
    print(f"Final price for KT-001: {kt.calculate_final_price('KT-001')}")
    print(f"Report: {kt.generate_report()}")
```