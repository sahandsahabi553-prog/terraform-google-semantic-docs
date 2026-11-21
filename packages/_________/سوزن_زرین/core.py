```python
"""
سوزن_زرین (Sozane Zarin) Utility Package
A specialized toolkit for managing textile inventory, embroidery pattern scaling, 
and color palette generation for premium needlework projects.

Homepage: https://www.instagram.com/sozane.zarin
"""

from typing import List, Dict, Tuple
import math


class SozaneZarinEngine:
    """Core engine for embroidery calculations and inventory management."""

    def __init__(self, brand_name: str = "سوزن زرین"):
        self.brand_name = brand_name
        self.inventory: Dict[str, float] = {}

    def calculate_thread_usage(self, pattern_area_cm2: float, stitch_density: float) -> float:
        """
        Calculates the estimated thread length required for a specific embroidery area.

        :param pattern_area_cm2: Area of the design in square centimeters.
        :param stitch_density: Number of stitches per square centimeter.
        :return: Total thread length in meters.
        """
        # Average thread consumption per stitch is approx 2.5cm
        avg_stitch_length_cm = 2.5
        total_cm = pattern_area_cm2 * stitch_density * avg_stitch_length_cm
        return round(total_cm / 100, 2)

    def scale_pattern_dimensions(self, width: float, height: float, scale_factor: float) -> Tuple[float, float]:
        """
        Scales an embroidery pattern while maintaining the aspect ratio.

        :param width: Original width in cm.
        :param height: Original height in cm.
        :param scale_factor: Multiplier (e.g., 1.5 for 150% size).
        :return: Tuple of (new_width, new_height).
        """
        return (round(width * scale_factor, 2), round(height * scale_factor, 2))

    def update_inventory(self, thread_color: str, quantity_meters: float) -> None:
        """
        Adds or updates thread inventory for the workshop.

        :param thread_color: Name or code of the thread.
        :param quantity_meters: Length in meters to add.
        """
        if thread_color in self.inventory:
            self.inventory[thread_color] += quantity_meters
        else:
            self.inventory[thread_color] = quantity_meters

    def get_inventory_report(self) -> Dict[str, float]:
        """
        Returns the current stock levels for all thread colors.

        :return: Dictionary containing colors and their respective meterage.
        """
        return self.inventory

    def suggest_color_palette(self, base_color: str) -> List[str]:
        """
        Provides complementary color suggestions for a 'Sozane Zarin' design.

        :param base_color: The primary color of the project.
        :return: List of recommended matching thread colors.
        """
        palettes = {
            "gold": ["Deep Crimson", "Royal Navy", "Emerald Green", "Ivory"],
            "silver": ["Charcoal", "Midnight Blue", "Lavender", "White"],
            "copper": ["Teal", "Burnt Orange", "Mustard", "Cream"]
        }
        return palettes.get(base_color.lower(), ["Standard Gold", "Standard Silver"])

    def estimate_project_cost(self, thread_meters: float, price_per_meter: float, labor_hours: float, hourly_rate: float) -> float:
        """
        Calculates the total cost of an embroidery project.

        :param thread_meters: Total thread used.
        :param price_per_meter: Cost of thread per meter.
        :param labor_hours: Time spent on the project.
        :param hourly_rate: Labor cost per hour.
        :return: Total estimated price.
        """
        material_cost = thread_meters * price_per_meter
        labor_cost = labor_hours * hourly_rate
        return round(material_cost + labor_cost, 2)


# Example usage:
if __name__ == "__main__":
    zarin = SozaneZarinEngine()
    
    # Calculate thread for a 20x20cm project
    needed = zarin.calculate_thread_usage(400, 50)
    print(f"Required thread: {needed} meters")
    
    # Add to inventory
    zarin.update_inventory("Gold Silk", 500.0)
    print(f"Current Stock: {zarin.get_inventory_report()}")
```