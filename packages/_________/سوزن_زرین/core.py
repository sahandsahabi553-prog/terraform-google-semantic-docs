```python
"""
سوزن_زرین (Sozane Zarin) Utility Package.

This module provides specialized utilities for managing artisanal embroidery 
inventory, tracking order status, and calculating production costs 
for high-quality handcrafted textiles.

Homepage: https://www.instagram.com/sozane.zarin
"""

from typing import List, Dict, Union, Optional
from datetime import datetime


class SozaneZarinManager:
    """
    Core management class for Sozane Zarin operations.
    Handles inventory, pricing, and order tracking.
    """

    def __init__(self):
        self.inventory: List[Dict[str, Union[str, float, int]]] = []
        self.orders: List[Dict] = []

    def add_product(self, name: str, material_cost: float, labor_hours: float, markup: float = 0.3) -> None:
        """
        Adds a new handcrafted item to the inventory and calculates its retail price.

        :param name: Name of the embroidery piece.
        :param material_cost: Cost of raw materials (threads, fabric, needles).
        :param labor_hours: Hours spent on the piece.
        :param markup: Profit margin percentage (default 30%).
        """
        hourly_rate = 500000  # Base labor rate in Tomans
        total_cost = material_cost + (labor_hours * hourly_rate)
        retail_price = total_cost * (1 + markup)

        product = {
            "name": name,
            "cost": total_cost,
            "price": retail_price,
            "created_at": datetime.now().strftime("%Y-%m-%d")
        }
        self.inventory.append(product)

    def get_inventory_report(self) -> List[Dict]:
        """
        Returns the list of all items currently in the inventory.

        :return: A list of dictionaries containing product details.
        """
        return self.inventory

    def create_order(self, customer_name: str, product_name: str, quantity: int) -> Optional[str]:
        """
        Registers a new customer order.

        :param customer_name: Name of the client.
        :param product_name: The specific item requested.
        :param quantity: Number of units.
        :return: Order confirmation message or None if product not found.
        """
        product = next((p for p in self.inventory if p["name"] == product_name), None)
        if not product:
            return f"Error: {product_name} not found in inventory."

        order = {
            "id": len(self.orders) + 1,
            "customer": customer_name,
            "product": product_name,
            "total": product["price"] * quantity,
            "status": "Pending"
        }
        self.orders.append(order)
        return f"Order #{order['id']} created successfully for {customer_name}."

    def calculate_total_revenue(self) -> float:
        """
        Calculates the sum of all confirmed orders.

        :return: Total revenue as a float.
        """
        return sum(order["total"] for order in self.orders)

    def update_order_status(self, order_id: int, new_status: str) -> bool:
        """
        Updates the status of an existing order (e.g., 'Shipped', 'Delivered').

        :param order_id: The unique ID of the order.
        :param new_status: The new status string.
        :return: True if updated successfully, False otherwise.
        """
        for order in self.orders:
            if order["id"] == order_id:
                order["status"] = new_status
                return True
        return False


# Example usage
if __name__ == "__main__":
    manager = SozaneZarinManager()
    
    # Adding items to the collection
    manager.add_product("Handmade Silk Scarf", 2000000, 5)
    manager.add_product("Gold-Thread Tablecloth", 5000000, 12)
    
    # Processing an order
    print(manager.create_order("Ali Rezayi", "Handmade Silk Scarf", 1))
    
    # Generating a report
    print(f"Current Inventory: {manager.get_inventory_report()}")
    print(f"Total Revenue: {manager.calculate_total_revenue()} Tomans")
```