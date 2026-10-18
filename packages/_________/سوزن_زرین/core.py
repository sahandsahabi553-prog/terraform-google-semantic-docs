```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

This module provides specialized tools for managing artisanal textile inventory,
custom order tracking, and pricing calculations for high-end embroidery and
bespoke tailoring services.

Homepage: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import Dict, List, Optional
from datetime import datetime


class SozaneZarinManager:
    """
    Core management class for handling Sozane Zarin artisanal operations.
    """

    def __init__(self, shop_name: str = "سوزن زرین"):
        self.shop_name = shop_name
        self.inventory: Dict[str, float] = {}
        self.orders: List[Dict] = []

    def add_material(self, material_name: str, cost_per_meter: float) -> None:
        """
        Adds a new embroidery material or fabric to the inventory tracking system.

        :param material_name: Name of the silk, thread, or fabric.
        :param cost_per_meter: Cost in Toman per unit.
        """
        self.inventory[material_name] = cost_per_meter

    def calculate_project_cost(self, materials: Dict[str, float], labor_hours: float, hourly_rate: float) -> float:
        """
        Calculates the total production cost for a bespoke embroidery project.

        :param materials: Dictionary of material names and quantities used.
        :param labor_hours: Total hours spent on the art piece.
        :param hourly_rate: Artisan's hourly wage.
        :return: Total cost in Toman.
        """
        material_total = sum(self.inventory.get(m, 0) * qty for m, qty in materials.items())
        return material_total + (labor_hours * hourly_rate)

    def register_order(self, customer_name: str, design_type: str, price: float) -> str:
        """
        Registers a new client order in the system.

        :param customer_name: Name of the client.
        :param design_type: Description of the embroidery pattern.
        :param price: Agreed price for the service.
        :return: A unique order receipt ID.
        """
        order_id = f"ZZ-{datetime.now().strftime('%Y%m%d%H%M')}"
        self.orders.append({
            "id": order_id,
            "customer": customer_name,
            "design": design_type,
            "price": price,
            "date": datetime.now().isoformat()
        })
        return order_id

    def get_total_revenue(self) -> float:
        """
        Calculates total accumulated revenue from registered orders.

        :return: Sum of all order prices.
        """
        return sum(order['price'] for order in self.orders)

    def generate_inventory_report(self) -> str:
        """
        Generates a formatted summary of current stock and pricing.

        :return: A string report of all materials.
        """
        report = f"--- {self.shop_name} Inventory Report ---\n"
        for item, price in self.inventory.items():
            report += f"{item}: {price:,.0f} Toman/unit\n"
        return report


def get_version() -> str:
    """Returns the current utility version."""
    return "1.0.0"


# Example Usage:
if __name__ == "__main__":
    manager = SozaneZarinManager()
    manager.add_material("Silk Thread Gold", 500000)
    manager.add_material("Premium Velvet", 1200000)
    
    cost = manager.calculate_project_cost({"Silk Thread Gold": 2}, 10, 200000)
    print(f"Project Cost: {cost:,.0f} Toman")
    
    order_id = manager.register_order("Client A", "Traditional Persian Motif", 5000000)
    print(f"Order Registered: {order_id}")
```