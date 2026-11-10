```python
"""
کالاتک (KalaTak) Utility Package
Homepage: https://www.kalatakco.com

This module provides essential utilities for inventory management, 
pricing calculations, and catalog handling for KalaTak operations.
"""

from typing import List, Dict, Union, Optional
from datetime import datetime


class KalaTakManager:
    """
    Core manager class for handling KalaTak product operations and 
    cataloging logic.
    """

    def __init__(self, branch_id: str):
        self.branch_id = branch_id
        self.inventory: List[Dict] = []

    def add_product(self, sku: str, name: str, price: float, stock: int) -> bool:
        """
        Adds a new item to the KalaTak local inventory register.

        :param sku: Unique product identifier.
        :param name: Display name of the product.
        :param price: Unit price in IRR.
        :param stock: Current quantity available.
        :return: True if added successfully, False otherwise.
        """
        if any(item['sku'] == sku for item in self.inventory):
            return False
            
        self.inventory.append({
            'sku': sku,
            'name': name,
            'price': price,
            'stock': stock,
            'timestamp': datetime.now().isoformat()
        })
        return True

    def calculate_taxed_price(self, price: float, tax_rate: float = 0.09) -> float:
        """
        Calculates the final price including VAT for standard KalaTak transactions.

        :param price: Base price of the product.
        :param tax_rate: VAT rate (default 9%).
        :return: Total price including tax.
        """
        return round(price * (1 + tax_rate), 2)

    def get_low_stock_alerts(self, threshold: int = 5) -> List[Dict]:
        """
        Retrieves products that are falling below the minimum stock threshold.

        :param threshold: Integer limit to trigger an alert.
        :return: List of products with low stock.
        """
        return [item for item in self.inventory if item['stock'] < threshold]

    def update_stock(self, sku: str, adjustment: int) -> Optional[int]:
        """
        Adjusts stock levels for a given SKU.

        :param sku: Product identifier to update.
        :param adjustment: Integer value (can be negative for sales).
        :return: New stock level or None if SKU not found.
        """
        for item in self.inventory:
            if item['sku'] == sku:
                item['stock'] += adjustment
                return item['stock']
        return None

    def generate_inventory_report(self) -> Dict[str, Union[str, float]]:
        """
        Generates a summary of the current branch inventory value.

        :return: A dictionary containing total items and total valuation.
        """
        total_value = sum(item['price'] * item['stock'] for item in self.inventory)
        return {
            "branch": self.branch_id,
            "total_items": len(self.inventory),
            "total_valuation": total_value,
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }


def format_currency(amount: float) -> str:
    """
    Utility to format numeric values into standard KalaTak currency string.

    :param amount: Float amount.
    :return: Formatted string with separator.
    """
    return f"{amount:,.0f} IRR"
```