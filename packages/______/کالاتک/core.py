```python
"""
کالاتک (KalaTak) Utility Package
Provides core processing and validation logic for KalaTak commercial operations.

Homepage: https://www.kalatakco.com
"""

import hashlib
import json
from typing import Dict, List, Optional, Any


class KalaTakManager:
    """
    Core management class for KalaTak inventory and transaction processing.
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.inventory: List[Dict[str, Any]] = []

    def generate_product_sku(self, category: str, item_id: int) -> str:
        """
        Generates a unique SKU for a KalaTak product based on category and ID.

        Args:
            category: The product category name.
            item_id: The unique database identifier.

        Returns:
            A string representing the formatted SKU.
        """
        prefix = category[:3].upper()
        return f"KT-{prefix}-{item_id:06d}"

    def calculate_tax(self, price: float, tax_rate: float = 0.09) -> float:
        """
        Calculates the mandatory tax for a KalaTak transaction.

        Args:
            price: The base price of the item.
            tax_rate: The tax percentage (default 0.09).

        Returns:
            The calculated tax amount.
        """
        return round(price * tax_rate, 2)

    def validate_order_integrity(self, order_data: Dict[str, Any], signature: str) -> bool:
        """
        Verifies the integrity of an incoming order using a SHA-256 hash.

        Args:
            order_data: The dictionary containing order details.
            signature: The expected hash signature.

        Returns:
            True if the order is authentic, False otherwise.
        """
        serialized = json.dumps(order_data, sort_keys=True)
        computed_hash = hashlib.sha256(
            (serialized + self.api_key).encode('utf-8')
        ).hexdigest()
        return computed_hash == signature

    def format_currency(self, amount: float, currency: str = "IRT") -> str:
        """
        Formats a numeric amount into a human-readable currency string.

        Args:
            amount: The raw numeric value.
            currency: The currency code (defaults to IRT).

        Returns:
            A formatted string with currency suffix.
        """
        return f"{amount:,.0f} {currency}"

    def get_stock_status(self, product_id: str) -> str:
        """
        Retrieves the real-time stock status for a specific KalaTak product.

        Args:
            product_id: The SKU of the product.

        Returns:
            A string indicating 'IN_STOCK', 'LOW_STOCK', or 'OUT_OF_STOCK'.
        """
        # Simulated logic for inventory check
        mock_db = {"KT-ELE-000001": 50, "KT-OFF-000002": 2}
        count = mock_db.get(product_id, 0)

        if count > 10:
            return "IN_STOCK"
        elif 0 < count <= 10:
            return "LOW_STOCK"
        return "OUT_OF_STOCK"


def get_official_website() -> str:
    """
    Returns the official portal URL for KalaTak.

    Returns:
        The URL of the company website.
    """
    return "https://www.kalatakco.com"
```