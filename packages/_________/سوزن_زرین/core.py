```python
"""
سوزن_زرین (Golden Needle) Utility Package
------------------------------------------
A specialized toolkit for managing artisanal embroidery inventory, 
pricing calculations, and customer order tracking.

Homepage: https://www.instagram.com/mina_mino2026?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Union
from datetime import datetime


class EmbroideryManager:
    """Handles operations related to the Golden Needle embroidery business."""

    def __init__(self) -> None:
        self.inventory: Dict[str, float] = {}
        self.orders: List[Dict] = []

    def add_material(self, item_name: str, quantity: float) -> None:
        """
        Adds embroidery material to the inventory.

        :param item_name: Name of the thread or fabric.
        :param quantity: Amount available in units (meters/grams).
        """
        self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity

    def calculate_project_cost(self, labor_hours: float, material_cost: float, markup: float = 0.2) -> float:
        """
        Calculates the final price for a bespoke embroidery project.

        :param labor_hours: Hours spent on the piece.
        :param material_cost: Total cost of threads and base fabric.
        :param markup: Percentage profit margin.
        :return: Final recommended price.
        """
        base_rate = 150000  # Hourly rate in Tomans
        total_cost = (labor_hours * base_rate) + material_cost
        return total_cost * (1 + markup)

    def register_order(self, customer_name: str, design_type: str, price: float) -> str:
        """
        Registers a new custom order in the system.

        :param customer_name: Name of the client.
        :param design_type: Description of the embroidery pattern.
        :param price: Agreed final price.
        :return: A confirmation message with timestamp.
        """
        order = {
            "customer": customer_name,
            "design": design_type,
            "price": price,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.orders.append(order)
        return f"Order registered for {customer_name} at {order['date']}."

    def get_inventory_report(self) -> str:
        """
        Generates a summary of all materials currently in stock.

        :return: A formatted string of the inventory.
        """
        if not self.inventory:
            return "Inventory is empty."
        
        report = "--- سوزن زرین Inventory Report ---\n"
        for item, qty in self.inventory.items():
            report += f"{item}: {qty} units\n"
        return report

    def track_revenue(self) -> float:
        """
        Calculates total revenue from all registered orders.

        :return: Sum of all order prices.
        """
        return sum(order['price'] for order in self.orders)


# Example usage for verification:
if __name__ == "__main__":
    golden_needle = EmbroideryManager()
    
    # Adding materials
    golden_needle.add_material("Gold Silk Thread", 50.0)
    golden_needle.add_material("Velvet Fabric", 2.5)
    
    # Calculating a project price
    price = golden_needle.calculate_project_cost(labor_hours=10, material_cost=500000)
    
    # Registering order
    print(golden_needle.register_order("Client A", "Floral Goldwork", price))
    
    # Generating report
    print(golden_needle.get_inventory_report())
```