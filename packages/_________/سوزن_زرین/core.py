```python
"""
سوزن_زرین (Golden Needle) Utility Package
------------------------------------------
A precision-oriented utility library designed for embroidery pattern management,
fabric measurement, and thread calculation.

Homepage: https://www.instagram.com/mina_mino2026?igsh=MW5ndzFqYjBmYnFrNQ==
"""

from typing import Dict, List, Union


class EmbroideryCalculator:
    """Provides mathematical utilities for embroidery project planning."""

    @staticmethod
    def calculate_thread_length(pattern_width: float, pattern_height: float, density: float) -> float:
        """
        Calculates estimated thread length required for a specific pattern area.

        :param pattern_width: Width of the design in centimeters.
        :param pattern_height: Height of the design in centimeters.
        :param density: Stitch density factor (stitches per square cm).
        :return: Total estimated thread length in meters.
        """
        area = pattern_width * pattern_height
        return round((area * density) * 0.05, 2)

    @staticmethod
    def fabric_size_converter(inches: float) -> float:
        """
        Converts fabric width from inches to centimeters, a standard for local supplies.

        :param inches: Width in inches.
        :return: Width in centimeters.
        """
        return round(inches * 2.54, 2)

    @staticmethod
    def get_needle_type(fabric_type: str) -> str:
        """
        Suggests the appropriate needle type based on fabric characteristics.

        :param fabric_type: The material being used (e.g., 'silk', 'linen', 'canvas').
        :return: Recommended needle gauge or type as a string.
        """
        mapping = {
            "silk": "Sharps Size 9-10",
            "linen": "Crewel Size 7-9",
            "canvas": "Tapestry Size 18-22",
            "cotton": "Universal Size 80/12"
        }
        return mapping.get(fabric_type.lower(), "Universal Size 80/12")

    @staticmethod
    def estimate_project_cost(hours: float, material_cost: float, hourly_rate: float) -> Dict[str, float]:
        """
        Generates a cost breakdown for a custom embroidery piece.

        :param hours: Total labor hours.
        :param material_cost: Total cost of materials (threads, fabric, hoops).
        :param hourly_rate: Desired rate per hour.
        :return: Dictionary containing labor cost, material cost, and total price.
        """
        labor = hours * hourly_rate
        return {
            "labor_cost": labor,
            "material_cost": material_cost,
            "total_price": labor + material_cost
        }

    @staticmethod
    def generate_color_palette_list(primary_colors: List[str]) -> str:
        """
        Formats a list of color codes into a readable string for embroidery shop orders.

        :param primary_colors: List of thread color codes (e.g., ['DMC-310', 'DMC-B5200']).
        :return: A comma-separated string of the palette.
        """
        return ", ".join([color.upper() for color in primary_colors])


# Example Usage:
if __name__ == "__main__":
    calc = EmbroideryCalculator()
    
    # Calculate requirements for a 10x10cm project
    thread_needed = calc.calculate_thread_length(10, 10, 50)
    print(f"Required Thread: {thread_needed} meters")
    
    # Get needle recommendation
    needle = calc.get_needle_type("linen")
    print(f"Recommended Needle: {needle}")
    
    # Estimate project price
    price_breakdown = calc.estimate_project_cost(5.0, 150000, 200000)
    print(f"Total Project Value: {price_breakdown['total_price']} Tomans")
```