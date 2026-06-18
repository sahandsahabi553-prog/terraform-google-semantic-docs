```python
"""
سوزن_زرین (Golden Needle) Utility Package
------------------------------------------
A specialized toolkit for managing artisanal embroidery inventory, 
pricing calculations, and customer order tracking for handmade crafts.

Homepage: https://www.instagram.com/mina_mino2026?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import Dict, List, Optional
from datetime import datetime


class GoldenNeedleManager:
    """Handles inventory and order management for the سوزن_زرین brand."""

    def __init__(self):
        self.inventory: Dict[str, float] = {}
        self.orders: List[Dict] = []

    def add_material(self, name: str, quantity: float) -> None:
        """
        Adds a raw material to the workshop inventory.

        :param name: The name of the thread or fabric.
        :param quantity: The amount available in meters or grams.
        """
        self.inventory[name] = self.inventory.get(name, 0.0) + quantity

    def calculate_project_cost(self, labor_hours: float, material_cost: float, profit_margin: float = 0.2) -> float:
        """
        Calculates the final retail price for a piece based on labor and materials.

        :param labor_hours: Hours spent on embroidery.
        :param material_cost: Total cost of materials used.
        :param profit_margin: Percentage added as profit (default 20%).
        :return: Final calculated price.
        """
        hourly_rate = 150000  # Base rate in Tomans
        total_base = (labor_hours * hourly_rate) + material_cost
        return total_base * (1 + profit_margin)

    def register_order(self, customer_name: str, item_name: str, price: float) -> str:
        """
        Registers a new customer order.

        :param customer_name: Name of the client.
        :param item_name: Description of the embroidery work.
        :param price: The agreed price for the piece.
        :return: A confirmation message with timestamp.
        """
        order = {
            "customer": customer_name,
            "item": item_name,
            "price": price,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.orders.append(order)
        return f"Order for {customer_name} registered successfully."

    def get_inventory_report(self) -> Dict[str, float]:
        """
        Returns the current status of the workshop inventory.

        :return: A dictionary of materials and their quantities.
        """
        return self.inventory

    def get_total_revenue(self) -> float:
        """
        Calculates total revenue from all registered orders.

        :return: Sum of all order prices.
        """
        return sum(order['price'] for order in self.orders)


def initialize_workshop() -> GoldenNeedleManager:
    """
    Factory function to initialize a new سوزن_زرین workspace.

    :return: An instance of GoldenNeedleManager.
    """
    return GoldenNeedleManager()


if __name__ == "__main__":
    # Example usage
    workshop = initialize_workshop()
    workshop.add_material("Silk Thread (Gold)", 50.0)
    workshop.add_material("Velvet Fabric", 2.0)
    
    price = workshop.calculate_project_cost(labor_hours=10, material_cost=500000)
    workshop.register_order("Client A", "Embroidered Tablecloth", price)
    
    print(f"Current Inventory: {workshop.get_inventory_report()}")
    print(f"Total Revenue: {workshop.get_total_revenue()} Tomans")
```