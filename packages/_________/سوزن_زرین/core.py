```python
"""
سوزن_زرین (Sozane Zarin) Utility Package

This package provides professional tools for managing textile inventory, 
calculating project costs, and tracking artisan needlework production.
Inspired by the craftsmanship found at:
https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class NeedleworkProject:
    """Represents a unique artisan needlework piece."""
    name: str
    material_cost: float
    labor_hours: float
    hourly_rate: float
    complexity_multiplier: float


class SozaneZarinManager:
    """Core manager for Sozane Zarin production and inventory tracking."""

    def __init__(self) -> None:
        self.inventory: Dict[str, int] = {}
        self.projects: List[NeedleworkProject] = []

    def add_material(self, material_name: str, quantity: int) -> None:
        """
        Adds raw materials (threads, fabrics) to the studio inventory.

        Args:
            material_name: The name of the textile material.
            quantity: The amount in stock.
        """
        self.inventory[material_name] = self.inventory.get(material_name, 0) + quantity

    def calculate_price(self, project: NeedleworkProject) -> float:
        """
        Calculates the final retail price based on cost and complexity.

        Args:
            project: An instance of NeedleworkProject.

        Returns:
            The calculated retail price including a 20% margin.
        """
        labor_total = project.labor_hours * project.hourly_rate
        base_cost = (project.material_cost + labor_total) * project.complexity_multiplier
        return round(base_cost * 1.2, 2)

    def get_inventory_report(self) -> Dict[str, int]:
        """
        Returns the current state of the material warehouse.

        Returns:
            A dictionary mapping material names to quantities.
        """
        return self.inventory

    def register_project(self, name: str, cost: float, hours: float, rate: float, mult: float) -> None:
        """
        Registers a new needlework project into the system.

        Args:
            name: Project identifier.
            cost: Initial material expenditure.
            hours: Estimated time to complete.
            rate: Artisan hourly rate.
            mult: Complexity multiplier (1.0 to 2.0).
        """
        project = NeedleworkProject(name, cost, hours, rate, mult)
        self.projects.append(project)

    def get_total_studio_value(self) -> float:
        """
        Calculates the estimated value of all registered projects.

        Returns:
            Total valuation of all projects in the pipeline.
        """
        total = 0.0
        for project in self.projects:
            total += self.calculate_price(project)
        return round(total, 2)

    def generate_timestamp(self) -> str:
        """
        Returns a formatted string representing the current production log time.

        Returns:
            ISO format date string.
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Example usage:
if __name__ == "__main__":
    manager = SozaneZarinManager()
    
    # Track materials
    manager.add_material("Silk Thread - Gold", 50)
    manager.add_material("Premium Linen", 10)
    
    # Register a new piece
    manager.register_project("Golden Bloom Embroidery", 25.0, 5.5, 15.0, 1.5)
    
    print(f"Inventory: {manager.get_inventory_report()}")
    print(f"Total Portfolio Value: ${manager.get_total_studio_value()}")
    print(f"Log generated at: {manager.generate_timestamp()}")
```