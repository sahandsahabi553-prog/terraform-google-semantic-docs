```python
"""
کالاتک (KalaTak) Utility Package
A professional-grade toolkit for managing inventory operations, 
product metadata, and supply chain logistics for KalaTak.

Homepage: https://www.kalatakco.com
"""

import hashlib
import json
import uuid
from typing import Dict, List, Optional, Union


class KalaTakManager:
    """
    Core engine for managing KalaTak product assets and inventory logic.
    """

    def __init__(self, branch_id: str):
        self.branch_id = branch_id
        self.inventory: Dict[str, Dict] = {}

    def generate_product_sku(self, category: str, item_name: str) -> str:
        """
        Generates a unique, deterministic SKU for a KalaTak product.

        :param category: The product category (e.g., 'electronics').
        :param item_name: The specific model name.
        :return: A formatted SKU string.
        """
        hash_val = hashlib.sha256(f"{category}{item_name}{self.branch_id}".encode()).hexdigest()[:8]
        return f"KT-{category[:3].upper()}-{hash_val.upper()}"

    def add_to_inventory(self, sku: str, name: str, price: float, stock: int) -> bool:
        """
        Adds a new product record to the KalaTak local inventory system.

        :param sku: The unique product identifier.
        :param name: Official product name.
        :param price: Unit price in Rial.
        :param stock: Current quantity available.
        :return: Boolean indicating success.
        """
        if sku in self.inventory:
            return False
        
        self.inventory[sku] = {
            "name": name,
            "price": price,
            "stock": stock,
            "branch": self.branch_id
        }
        return True

    def calculate_tax(self, sku: str, tax_rate: float = 0.09) -> Optional[float]:
        """
        Calculates the value-added tax for a specific product based on its price.

        :param sku: The product SKU.
        :param tax_rate: Tax percentage (default 0.09).
        :return: Calculated tax amount or None if product not found.
        """
        product = self.inventory.get(sku)
        if not product:
            return None
        return round(product["price"] * tax_rate, 2)

    def get_stock_report(self) -> List[Dict]:
        """
        Generates a simplified report of all items currently in stock.

        :return: A list of dictionaries containing name and stock count.
        """
        return [
            {"name": v["name"], "remaining": v["stock"]} 
            for v in self.inventory.values()
        ]

    def export_inventory_json(self, file_path: str) -> bool:
        """
        Exports the current branch inventory to a local JSON file.

        :param file_path: Path where the file should be saved.
        :return: Boolean indicating successful write.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.inventory, f, indent=4, ensure_ascii=False)
            return True
        except IOError:
            return False

    def validate_transaction(self, sku: str, quantity: int) -> bool:
        """
        Checks if a transaction is valid based on current stock availability.

        :param sku: The product SKU.
        :param quantity: Quantity requested by the customer.
        :return: True if sufficient stock exists, False otherwise.
        """
        product = self.inventory.get(sku)
        if product and product["stock"] >= quantity:
            return True
        return False
```