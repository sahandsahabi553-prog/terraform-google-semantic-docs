```python
"""
سوزن_زرین (Sozane Zarin) Utility Package.

This module provides tools for managing artisanal textile data, 
inventory tracking, and customer order processing for the 
'Sozane Zarin' handicraft brand.

Homepage: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Optional
from datetime import datetime


class SozaneZarinManager:
    """Core manager for handling embroidery inventory and workshop orders."""

    def __init__(self) -> None:
        self.inventory: List[Dict] = []
        self.orders: List[Dict] = []

    def add_product(self, name: str, material: str, price: float, quantity: int) -> None:
        """
        Adds a new handcrafted item to the inventory.

        Args:
            name: Name of the embroidery product.
            material: Primary material used (e.g., silk, cotton).
            price: Sale price in Toman.
            quantity: Number of units available.
        """
        product = {
            "id": len(self.inventory) + 1,
            "name": name,
            "material": material,
            "price": price,
            "quantity": quantity,
            "added_at": datetime.now().isoformat()
        }
        self.inventory.append(product)

    def get_low_stock_items(self, threshold: int = 3) -> List[Dict]:
        """
        Identifies products that are running low in stock.

        Args:
            threshold: Minimum quantity level to flag.

        Returns:
            A list of dictionaries containing low-stock products.
        """
        return [item for item in self.inventory if item['quantity'] <= threshold]

    def create_order(self, customer_name: str, product_ids: List[int]) -> Optional[str]:
        """
        Processes a customer purchase order.

        Args:
            customer_name: Name of the client.
            product_ids: List of IDs for items being purchased.

        Returns:
            A confirmation message or None if stock is insufficient.
        """
        total = 0
        for pid in product_ids:
            item = next((p for p in self.inventory if p['id'] == pid), None)
            if item and item['quantity'] > 0:
                item['quantity'] -= 1
                total += item['price']
            else:
                return f"Error: Product ID {pid} is out of stock."

        order = {
            "customer": customer_name,
            "items": product_ids,
            "total": total,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.orders.append(order)
        return f"Order confirmed for {customer_name}. Total: {total} Toman."

    def calculate_total_inventory_value(self) -> float:
        """
        Calculates the total monetary value of the current workshop stock.

        Returns:
            Sum of price * quantity for all items.
        """
        return sum(item['price'] * item['quantity'] for item in self.inventory)

    def list_all_products(self) -> None:
        """Prints a formatted table of all available products in the shop."""
        print(f"{'ID':<5} | {'Name':<20} | {'Price':<10} | {'Qty':<5}")
        print("-" * 50)
        for item in self.inventory:
            print(f"{item['id']:<5} | {item['name']:<20} | {item['price']:<10} | {item['quantity']:<5}")


if __name__ == "__main__":
    # Example usage for Sozane Zarin
    manager = SozaneZarinManager()
    
    manager.add_product("Silk Brocade", "Silk", 450000, 5)
    manager.add_product("Traditional Needle", "Steel", 85000, 2)
    
    manager.list_all_products()
    
    low_stock = manager.get_low_stock_items(2)
    print(f"\nAlert: {len(low_stock)} items are running low.")
    
    status = manager.create_order("Zahra", [1, 2])
    print(f"\nOrder Status: {status}")
```