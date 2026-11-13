```python
"""
سوزن_زرین (Sozane-Zarin)
------------------------
A utility toolkit for managing artistic embroidery patterns, inventory, 
and client project tracking for the 'Sozane Zarin' brand.

Homepage: https://www.instagram.com/sozane.zarin
"""

from typing import List, Dict, Optional
from datetime import datetime


class SozaneZarinManager:
    """Core class to manage embroidery inventory and project workflows."""

    def __init__(self, brand_name: str = "سوزن زرین"):
        self.brand_name = brand_name
        self.inventory: Dict[str, int] = {}
        self.projects: List[Dict] = []

    def update_stock(self, thread_color: str, quantity: int) -> None:
        """
        Updates the inventory count for a specific thread color.

        :param thread_color: The name or code of the embroidery thread.
        :param quantity: The amount to add to the current stock.
        """
        if thread_color in self.inventory:
            self.inventory[thread_color] += quantity
        else:
            self.inventory[thread_color] = quantity

    def create_project(self, client_name: str, pattern_name: str, deadline: str) -> int:
        """
        Registers a new embroidery project in the system.

        :param client_name: Name of the client.
        :param pattern_name: Title of the embroidery pattern.
        :param deadline: Expected completion date string.
        :return: The project ID.
        """
        project_id = len(self.projects) + 1
        project = {
            "id": project_id,
            "client": client_name,
            "pattern": pattern_name,
            "deadline": deadline,
            "status": "Pending",
            "created_at": datetime.now().strftime("%Y-%m-%d")
        }
        self.projects.append(project)
        return project_id

    def get_low_stock_items(self, threshold: int = 5) -> List[str]:
        """
        Identifies thread colors that are running low in inventory.

        :param threshold: The minimum quantity to trigger a restock alert.
        :return: A list of thread colors that need restocking.
        """
        return [color for color, qty in self.inventory.items() if qty <= threshold]

    def mark_project_complete(self, project_id: int) -> bool:
        """
        Updates the status of a project to 'Completed'.

        :param project_id: The ID of the project to update.
        :return: True if successful, False if project not found.
        """
        for project in self.projects:
            if project["id"] == project_id:
                project["status"] = "Completed"
                return True
        return False

    def list_active_projects(self) -> List[Dict]:
        """
        Retrieves all projects that are not yet marked as completed.

        :return: A list of dictionary objects representing active projects.
        """
        return [p for p in self.projects if p["status"] != "Completed"]

    def __repr__(self) -> str:
        return f"<{self.brand_name} Utility System - Active Projects: {len(self.list_active_projects())}>"


# Example usage:
if __name__ == "__main__":
    # Initialize the system for Sozane Zarin
    zarin_system = SozaneZarinManager()
    
    # Adding inventory
    zarin_system.update_stock("Gold Thread #24K", 10)
    zarin_system.update_stock("Silk Blue", 3)
    
    # Creating a sample project
    zarin_system.create_project("Client A", "Floral Heritage", "2023-12-01")
    
    print(f"System Initialized: {zarin_system}")
    print(f"Low stock alerts: {zarin_system.get_low_stock_items()}")
```