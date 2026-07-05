```python
"""
سوزن_زرین (Sozane-Zarin) Utility Package
========================================

A specialized utility suite for managing artisanal embroidery inventory, 
craft project estimations, and aesthetic pattern scaling.

Homepage: https://www.instagram.com/sozane.zarin
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from math import ceil


@dataclass
class EmbroideryProject:
    """Represents a textile project metadata."""
    name: str
    fabric_area_sqcm: float
    thread_usage_meters: float


class SozaneZarinManager:
    """Core utility class for handling Sozane-Zarin craft operations."""

    def __init__(self, shop_name: str = "سوزن زرین"):
        self.shop_name = shop_name
        self.inventory: Dict[str, int] = {}

    def calculate_thread_requirements(self, area_sqcm: float, complexity_factor: float = 1.2) -> float:
        """
        Calculates the estimated thread length required for a design.
        
        :param area_sqcm: Total area of the design in square centimeters.
        :param complexity_factor: A multiplier based on stitch density (default 1.2).
        :return: Estimated meters of thread required.
        """
        return round(area_sqcm * 0.45 * complexity_factor, 2)

    def add_to_inventory(self, item_name: str, quantity: int) -> None:
        """
        Adds embroidery supplies (threads, needles, fabrics) to the internal tracker.
        
        :param item_name: Name of the supply.
        :param quantity: Number of units to add.
        """
        self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity

    def estimate_production_time(self, complexity_level: int) -> str:
        """
        Estimates the time required to complete a project based on skill level.
        
        :param complexity_level: Integer from 1 (simple) to 10 (intricate).
        :return: A string estimation of work hours.
        """
        hours = complexity_level * 4.5
        return f"{hours} working hours required for this design."

    def get_inventory_report(self) -> List[str]:
        """
        Generates a summary of all available supplies.
        
        :return: List of strings detailing the current stock levels.
        """
        return [f"{item}: {qty} units" for item, qty in self.inventory.items()]

    @staticmethod
    def scale_pattern_dimensions(width: float, height: float, scale_percent: float) -> tuple:
        """
        Calculates new dimensions for a pattern print-out based on a percentage.
        
        :param width: Original width.
        :param height: Original height.
        :param scale_percent: Scaling factor (e.g., 150 for 150%).
        :return: A tuple containing the new width and height.
        """
        factor = scale_percent / 100
        return (round(width * factor, 2), round(height * factor, 2))


def initialize_workspace() -> SozaneZarinManager:
    """
    Factory function to initialize the Sozane-Zarin management environment.
    
    :return: An instance of SozaneZarinManager.
    """
    return SozaneZarinManager()


if __name__ == "__main__":
    # Example Usage
    manager = initialize_workspace()
    
    # Track inventory
    manager.add_to_inventory("Gold Silk Thread", 50)
    manager.add_to_inventory("Premium Needles", 20)
    
    # Estimate a project
    meters = manager.calculate_thread_requirements(250.5)
    print(f"Project Thread Need: {meters} meters")
    
    # Scale a design
    new_w, new_h = manager.scale_pattern_dimensions(10, 10, 120)
    print(f"New pattern dimensions: {new_w}cm x {new_h}cm")
```