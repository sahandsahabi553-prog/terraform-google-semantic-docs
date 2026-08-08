```python
"""
سوزن_زرین (Sozane Zarin) Utility Package.

This module provides specialized utilities for managing artisanal embroidery 
inventory, tracking custom orders, and calculating pricing for handcrafted 
textile projects.

Homepage: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Optional
from datetime import datetime


class SozaneZarinManager:
    """Handles core business logic for the Sozane Zarin embroidery brand."""

    def __init__(self, shop_name: str = "سوزن زرین"):
        self.shop_name = shop_name
        self.inventory: Dict[str, float] = {}
        self.orders: List[Dict] = []

    def register_material(self, item_name: str, cost_per_unit: float) -> None:
        """
        Registers a new embroidery material into the inventory system.

        Args:
            item_name: The name of the thread, fabric, or accessory.
            cost_per_unit: The purchase price per unit.
        """
        self.inventory[item_name] = cost_per_unit

    def calculate_project_cost(self, materials: List[str], labor_hours: float, hourly_rate: float) -> float:
        """
        Calculates the total production cost of an embroidery project.

        Args:
            materials: A list of material names used in the project.
            labor_hours: Total hours spent on the piece.
            hourly_rate: The rate charged for artistic labor.

        Returns:
            The total cost as a float.
        """
        material_cost = sum(self.inventory.get(m, 0.0) for m in materials)
        return material_cost + (labor_hours * hourly_rate)

    def create_order(self, customer_name: str, item_description: str, price: float) -> Dict:
        """
        Logs a new customer order into the system.

        Args:
            customer_name: Name of the client.
            item_description: Details of the embroidery piece.
            price: Final sale price.

        Returns:
            A dictionary representing the order record.
        """
        order = {
            "customer": customer_name,
            "item": item_description,
            "price": price,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "status": "Pending"
        }
        self.orders.append(order)
        return order

    def get_total_revenue(self) -> float:
        """
        Calculates the total revenue from all logged orders.

        Returns:
            Sum of all order prices.
        """
        return sum(order["price"] for order in self.orders)

    def generate_inventory_report(self) -> str:
        """
        Generates a summary report of current material costs.

        Returns:
            A formatted string report of the inventory.
        """
        report = f"--- {self.shop_name} Inventory Report ---\n"
        for item, price in self.inventory.items():
            report += f"{item}: {price} Toman\n"
        return report


def get_brand_info() -> Dict[str, str]:
    """
    Returns metadata about the Sozane Zarin brand.

    Returns:
        Dictionary containing contact and social media information.
    """
    return {
        "brand": "سوزن زرین",
        "instagram": "https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==",
        "specialization": "Artisanal Embroidery"
    }
```