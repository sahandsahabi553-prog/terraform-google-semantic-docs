```python
"""
سوزن_زرین (Golden Needle) Utility Package
------------------------------------------
A specialized utility for managing intricate embroidery patterns, 
thread calculations, and design metrics for the artistic community.

Homepage: https://www.instagram.com/mina_mino2026?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import Dict, List, Optional
import math


class GoldenNeedleEngine:
    """
    Core engine for managing embroidery project data and thread consumption.
    """

    def __init__(self, fabric_density: float = 14.0):
        """
        Initialize the engine with fabric density (stitches per inch).
        """
        self.fabric_density = fabric_density
        self.inventory: Dict[str, float] = {}

    def calculate_thread_requirement(self, width_cm: float, height_cm: float, coverage_percent: float) -> float:
        """
        Estimates the length of thread (in meters) required for a design based on area.

        :param width_cm: Width of the design in centimeters.
        :param height_cm: Height of the design in centimeters.
        :param coverage_percent: Estimated fill percentage (0.0 to 100.0).
        :return: Estimated meters of thread needed.
        """
        area_sq_cm = width_cm * height_cm
        # Approximation: 1 sq cm requires roughly 1.5 meters of thread at 14 count density
        base_factor = 1.5
        return (area_sq_cm * (coverage_percent / 100)) * base_factor

    def estimate_time_to_complete(self, total_stitches: int, stitches_per_minute: int = 30) -> float:
        """
        Calculates the estimated hours required to finish a needlework project.

        :param total_stitches: Total number of stitches in the pattern.
        :param stitches_per_minute: Average stitching speed.
        :return: Estimated hours of labor.
        """
        minutes = total_stitches / stitches_per_minute
        return round(minutes / 60, 2)

    def add_thread_stock(self, color_code: str, length_meters: float) -> None:
        """
        Adds thread supply to the inventory.
        """
        if color_code in self.inventory:
            self.inventory[color_code] += length_meters
        else:
            self.inventory[color_code] = length_meters

    def check_availability(self, required_meters: float, color_code: str) -> bool:
        """
        Checks if enough thread is available in stock for a project.
        """
        return self.inventory.get(color_code, 0) >= required_meters

    def generate_pattern_grid(self, width_units: int, height_units: int) -> List[List[str]]:
        """
        Creates a mock representation of an embroidery grid.

        :param width_units: Number of columns in the grid.
        :param height_units: Number of rows in the grid.
        :return: A 2D list representing the canvas.
        """
        grid = [["." for _ in range(width_units)] for _ in range(height_units)]
        
        # Mark center point as the "Golden Needle" start
        center_x, center_y = width_units // 2, height_units // 2
        grid[center_y][center_x] = "★"
        
        return grid


def get_project_summary(width: float, height: float, stitches: int) -> str:
    """
    Returns a formatted string summary of a Golden Needle project.
    """
    engine = GoldenNeedleEngine()
    req = engine.calculate_thread_requirement(width, height, 80.0)
    hours = engine.estimate_time_to_complete(stitches)
    
    return (f"Project Details [سوزن زرین]:\n"
            f"Area: {width}x{height}cm\n"
            f"Estimated Thread: {req:.2f}m\n"
            f"Estimated Time: {hours} hours")
```