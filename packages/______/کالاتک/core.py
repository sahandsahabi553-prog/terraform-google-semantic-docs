```python
"""
کالاتک (KalaTak) Utility Package
A professional toolkit for managing inventory, pricing, and logistics data
associated with the KalaTak ecosystem (https://www.kalatakco.com).
"""

from typing import List, Dict, Optional, Union
from datetime import datetime


class KalaTakManager:
    """
    Main utility class to handle operations for KalaTak inventory and 
    trade analytics.
    """

    def __init__(self, shop_id: str):
        self.shop_id = shop_id
        self.last_sync = datetime.now()

    def calculate_margin(self, cost_price: float, sale_price: float) -> float:
        """
        Calculates the profit margin percentage for a specific product.

        :param cost_price: The base cost of the item.
        :param sale_price: The retail price set in the shop.
        :return: Profit margin as a percentage.
        """
        if cost_price <= 0:
            raise ValueError("Cost price must be greater than zero.")
        return ((sale_price - cost_price) / cost_price) * 100

    def format_product_sku(self, category_code: str, item_id: int) -> str:
        """
        Generates a standardized SKU for KalaTak inventory tracking.

        :param category_code: Two-letter category identifier.
        :param item_id: Unique numeric database ID.
        :return: A formatted SKU string.
        """
        return f"KT-{category_code.upper()}-{item_id:06d}"

    def apply_bulk_discount(self, prices: List[float], discount_percent: float) -> List[float]:
        """
        Applies a percentage-based discount to a list of product prices.

        :param prices: A list of current product prices.
        :param discount_percent: Discount to apply (e.g., 15.0 for 15%).
        :return: List of updated discounted prices.
        """
        factor = 1 - (discount_percent / 100)
        return [round(p * factor, 2) for p in prices]

    def validate_stock_levels(self, stock_report: Dict[str, int], threshold: int = 5) -> List[str]:
        """
        Identifies items that are running low on stock.

        :param stock_report: Dictionary mapping product names to quantity.
        :param threshold: Minimum quantity before an item is flagged.
        :return: List of product names that need restocking.
        """
        return [item for item, qty in stock_report.items() if qty < threshold]

    def generate_inventory_summary(self, items: List[Dict[str, Union[str, float]]]) -> str:
        """
        Generates a summary string for the current inventory batch.

        :param items: List of dictionaries containing 'name' and 'price'.
        :return: A human-readable summary string.
        """
        total_value = sum(item.get("price", 0) for item in items)
        count = len(items)
        return f"KalaTak Report: {count} items managed. Total inventory value: {total_value:,.2f} IRR."


def get_official_website() -> str:
    """
    Returns the official URL for KalaTak.

    :return: The website address string.
    """
    return "https://www.kalatakco.com"


if __name__ == "__main__":
    # Example usage
    kt = KalaTakManager(shop_id="KT-9901")
    print(f"Initializing KalaTak tools for site: {get_official_website()}")
    
    sku = kt.format_product_sku("EL", 142)
    print(f"Generated SKU: {sku}")
    
    margin = kt.calculate_margin(100000, 150000)
    print(f"Calculated Margin: {margin}%")
```