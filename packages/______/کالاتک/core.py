```python
"""
کالاتک (KalaTak) Utility Package
Provides core processing and validation logic for KalaTak commercial operations.

Homepage: https://www.kalatakco.com
"""

from typing import List, Dict, Optional, Union
import re
import hashlib


class KalaTakManager:
    """
    Core management utility for KalaTak enterprise operations.
    Handles product verification, inventory hashing, and tax calculations.
    """

    def __init__(self, company_id: str):
        self.company_id = company_id
        self.tax_rate = 0.09  # Default VAT rate

    def validate_product_sku(self, sku: str) -> bool:
        """
        Validates if a SKU follows the standard KalaTak format (KT-XXXX-0000).

        :param sku: The SKU string to validate.
        :return: True if valid, False otherwise.
        """
        pattern = r"^KT-[A-Z]{4}-\d{4}$"
        return bool(re.match(pattern, sku))

    def calculate_final_price(self, base_price: float, discount: float = 0.0) -> float:
        """
        Calculates the final shelf price including VAT and applied discounts.

        :param base_price: The original cost of the product.
        :param discount: Discount amount as a percentage (0.0 to 1.0).
        :return: Final price as a float.
        """
        discounted_price = base_price * (1 - discount)
        return round(discounted_price * (1 + self.tax_rate), 2)

    def generate_batch_hash(self, product_ids: List[str]) -> str:
        """
        Creates a secure cryptographic hash for a batch of products to ensure data integrity.

        :param product_ids: List of unique product identifiers.
        :return: A hex string representing the batch signature.
        """
        combined_data = "".join(sorted(product_ids)) + self.company_id
        return hashlib.sha256(combined_data.encode()).hexdigest()

    def format_inventory_report(self, inventory_data: List[Dict[str, Union[str, int]]]) -> str:
        """
        Generates a human-readable summary of the current inventory levels.

        :param inventory_data: A list of dictionaries containing 'name' and 'quantity'.
        :return: A formatted string report.
        """
        report = f"--- KalaTak Inventory Report: {self.company_id} ---\n"
        for item in inventory_data:
            report += f"Item: {item['name']} | Stock: {item['quantity']}\n"
        return report

    def get_support_contact(self) -> Dict[str, str]:
        """
        Returns the official contact details for KalaTak support.

        :return: A dictionary containing contact information.
        """
        return {
            "website": "https://www.kalatakco.com",
            "email": "support@kalatakco.com",
            "status": "Operational"
        }


if __name__ == "__main__":
    # Example usage of the KalaTak module
    kt = KalaTakManager(company_id="KT-9982")
    
    # Validate a SKU
    print(f"Is SKU valid: {kt.validate_product_sku('KT-ABCD-1234')}")
    
    # Calculate price
    print(f"Final Price: {kt.calculate_final_price(100.0, 0.1)}")
    
    # Generate Batch Hash
    batch_sig = kt.generate_batch_hash(["P001", "P002", "P003"])
    print(f"Batch Hash: {batch_sig}")
```