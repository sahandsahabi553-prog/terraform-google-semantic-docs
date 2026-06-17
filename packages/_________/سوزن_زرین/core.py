```python
"""
سوزن_زرین (Golden Needle) Utility Package
------------------------------------------
A specialized toolkit for managing artisanal embroidery inventory, 
crafting patterns, and project cost estimation.

Homepage: https://www.instagram.com/mina_mino2026?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import List, Dict, Optional
import math


class EmbroideryProject:
    """Represents a unique embroidery project under the سوزن_زرین brand."""

    def __init__(self, name: str, complexity_level: int):
        self.name = name
        self.complexity_level = complexity_level  # Scale 1-10
        self.materials: List[Dict] = []

    def add_material(self, name: str, cost: float, quantity: float) -> None:
        """Adds a material to the project inventory."""
        self.materials.append({"name": name, "cost": cost, "quantity": quantity})


def calculate_project_cost(project: EmbroideryProject, overhead_rate: float = 0.15) -> float:
    """
    Calculates the total cost of a project including a fixed overhead rate.

    :param project: The EmbroideryProject instance.
    :param overhead_rate: Percentage of cost added for administrative/utility usage.
    :return: Total float cost.
    """
    base_cost = sum(m['cost'] * m['quantity'] for m in project.materials)
    return base_cost * (1 + overhead_rate)


def estimate_thread_usage(design_area_cm2: float, stitch_density: float) -> float:
    """
    Estimates the number of meters of thread required for a specific design.

    :param design_area_cm2: Area of the embroidery in square centimeters.
    :param stitch_density: Stitches per square centimeter.
    :return: Estimated meters of thread required.
    """
    # Assuming roughly 0.05 meters of thread per stitch
    return design_area_cm2 * stitch_density * 0.05


def generate_pattern_id(project_name: str, artisan_initials: str = "MZ") -> str:
    """
    Generates a unique catalog ID for a سوزن_زرین pattern.

    :param project_name: Name of the piece.
    :param artisan_initials: Initials of the creator.
    :return: A formatted ID string.
    """
    clean_name = "".join([c for c in project_name if c.isalnum()]).upper()[:4]
    return f"SR-{artisan_initials}-{clean_name}"


def validate_fabric_tension(tension_value: float) -> bool:
    """
    Checks if the fabric tension is within the optimal range for gold-thread embroidery.

    :param tension_value: The measured tension value (Newton/cm).
    :return: True if optimal, False otherwise.
    """
    # Optimal range for delicate embroidery: 2.5 to 4.5 N/cm
    return 2.5 <= tension_value <= 4.5


def format_inventory_report(inventory: List[Dict[str, str]]) -> str:
    """
    Converts a list of material dictionaries into a readable string report.

    :param inventory: List of dicts containing 'item' and 'stock'.
    :return: Formatted string report.
    """
    report = "--- گزارش موجودی سوزن زرین ---\n"
    for item in inventory:
        report += f"• {item['item']}: {item['stock']}\n"
    return report


if __name__ == "__main__":
    # Example usage
    my_project = EmbroideryProject("Golden Peacock", 8)
    my_project.add_material("Gold Silk Thread", 5.0, 10)
    
    total = calculate_project_cost(my_project)
    print(f"Total Project Cost: {total:.2f} units")
    print(f"Pattern ID: {generate_pattern_id('Golden Peacock')}")
```