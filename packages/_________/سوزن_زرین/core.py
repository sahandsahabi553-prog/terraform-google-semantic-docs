```python
"""
سوزن_زرین (Sozane Zarin) Utility Package
---------------------------------------
A specialized toolkit for managing textile inventory, artisanal stitching 
metrics, and design patterns inspired by the Sozane Zarin craftsmanship.

Homepage: https://www.instagram.com/sozane.zarin?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ThreadSpool:
    """Represents a premium embroidery thread spool."""
    color_code: str
    material: str
    length_meters: float
    is_metallic: bool


class SozaneZarinManager:
    """Core utility manager for textile production and pattern design."""

    def __init__(self, studio_name: str):
        self.studio_name = studio_name
        self.inventory: Dict[str, ThreadSpool] = {}
        self.project_logs: List[Dict] = []

    def add_thread_to_inventory(self, name: str, spool: ThreadSpool) -> None:
        """
        Registers a new thread spool into the workshop inventory.

        :param name: Unique identifier for the thread type.
        :param spool: The ThreadSpool dataclass object.
        """
        self.inventory[name] = spool

    def calculate_stitch_density(self, total_stitches: int, fabric_area_cm2: float) -> float:
        """
        Calculates the density of stitches per square centimeter.

        :param total_stitches: Total count of stitches in a design.
        :param fabric_area_cm2: Area of the fabric patch.
        :return: Density as stitches per cm².
        """
        if fabric_area_cm2 <= 0:
            raise ValueError("Fabric area must be greater than zero.")
        return total_stitches / fabric_area_cm2

    def estimate_thread_usage(self, pattern_complexity: float, scale_factor: float) -> float:
        """
        Estimates the length of thread required for a specific pattern complexity.

        :param pattern_complexity: Float value representing intricate detail (1.0 to 10.0).
        :param scale_factor: Multiplier for the final output size.
        :return: Estimated meters of thread required.
        """
        base_usage = 5.0  # Base meters per unit of complexity
        return base_usage * pattern_complexity * scale_factor

    def log_project(self, project_name: str, material_used: str) -> None:
        """
        Records a completed embroidery project in the workshop history.

        :param project_name: Name of the design.
        :param material_used: Type of fabric used.
        """
        entry = {
            "name": project_name,
            "material": material_used,
            "timestamp": datetime.now().isoformat()
        }
        self.project_logs.append(entry)

    def get_metallic_inventory(self) -> List[str]:
        """
        Filters and returns the names of all metallic threads available in inventory.

        :return: List of keys representing metallic spools.
        """
        return [
            name for name, spool in self.inventory.items() 
            if spool.is_metallic
        ]


# Example usage pattern
if __name__ == "__main__":
    # Initialize the workshop
    atelier = SozaneZarinManager("Sozane Zarin Studio")

    # Add a golden thread
    gold_thread = ThreadSpool("G-001", "Silk/Metallic", 500.0, True)
    atelier.add_thread_to_inventory("Royal Gold", gold_thread)

    # Perform calculations
    density = atelier.calculate_stitch_density(1500, 25.0)
    required = atelier.estimate_thread_usage(8.5, 2.0)

    print(f"Atelier: {atelier.studio_name}")
    print(f"Calculated Density: {density:.2f} stitches/cm²")
    print(f"Estimated Thread Needed: {required:.2f} meters")
```