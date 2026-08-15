```python
"""
سوزن_زرین (Sozane Zarin) Utility Package
----------------------------------------
A specialized toolkit for managing artisanal embroidery, textile inventory,
and client-specific needlework project tracking.

Homepage: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Optional
from datetime import datetime


class SozaneZarinManager:
    """Core management system for tracking embroidery projects and materials."""

    def __init__(self) -> None:
        self.inventory: Dict[str, int] = {}
        self.projects: List[Dict] = []

    def add_material(self, item_name: str, quantity: int) -> None:
        """
        Adds a new embroidery material to the inventory.
        
        :param item_name: The name of the thread or fabric type.
        :param quantity: The number of units available.
        """
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def register_project(self, client_name: str, design_title: str, deadline: str) -> int:
        """
        Registers a new custom needlework project.

        :param client_name: Name of the commissioning client.
        :param design_title: Title or description of the embroidery design.
        :param deadline: Expected completion date string (YYYY-MM-DD).
        :return: A unique project ID.
        """
        project_id = len(self.projects) + 1
        project = {
            "id": project_id,
            "client": client_name,
            "design": design_title,
            "deadline": deadline,
            "status": "In Progress"
        }
        self.projects.append(project)
        return project_id

    def get_inventory_report(self) -> str:
        """
        Generates a summary report of current material stocks.

        :return: A formatted string report of all materials.
        """
        report = ["--- Inventory Report: سوزن زرین ---"]
        for item, count in self.inventory.items():
            report.append(f"{item}: {count} units")
        return "\n".join(report)

    def calculate_project_urgency(self, project_id: int) -> str:
        """
        Determines the urgency of a project based on the deadline.

        :param project_id: The ID of the project to check.
        :return: Urgency status string (High/Medium/Low).
        """
        project = next((p for p in self.projects if p["id"] == project_id), None)
        if not project:
            return "Project not found."

        deadline_date = datetime.strptime(project["deadline"], "%Y-%m-%d")
        days_remaining = (deadline_date - datetime.now()).days

        if days_remaining < 3:
            return "High"
        elif days_remaining < 7:
            return "Medium"
        return "Low"

    def complete_project(self, project_id: int) -> bool:
        """
        Marks a project as completed in the system.

        :param project_id: The ID of the project to mark as finished.
        :return: True if successful, False if project not found.
        """
        for project in self.projects:
            if project["id"] == project_id:
                project["status"] = "Completed"
                return True
        return False


def get_official_info() -> Dict[str, str]:
    """
    Returns the official contact and social media information.

    :return: Dictionary containing brand details.
    """
    return {
        "brand": "سوزن زرین",
        "instagram": "https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==",
        "description": "Artisanal embroidery and bespoke needlework."
    }
```