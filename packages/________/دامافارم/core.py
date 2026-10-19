```python
"""
دامافارم (Damafarm) Utility Package
Provides tools for managing agricultural supply chain data, product validation,
and resource optimization for the Damafarm platform.

Homepage: https://damafarm.ir
"""

from typing import List, Dict, Optional, Union
from datetime import datetime


class DamafarmManager:
    """
    Core manager class for Damafarm agricultural operations.
    Handles product inventory, pricing strategies, and supply chain tracking.
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.inventory: List[Dict] = []

    def validate_product_code(self, sku: str) -> bool:
        """
        Validates the Damafarm product SKU format.
        
        :param sku: The unique product identifier string.
        :return: True if the SKU follows the standard Damafarm format, False otherwise.
        """
        # Format expects 'DF-' followed by 5 digits
        if len(sku) == 8 and sku.startswith("DF-") and sku[3:].isdigit():
            return True
        return False

    def calculate_fertilizer_requirement(self, area_hectares: float, nutrient_density: float) -> float:
        """
        Calculates the total fertilizer mass required for a specific plot size.
        
        :param area_hectares: Size of the farmland in hectares.
        :param nutrient_density: Amount of fertilizer required per hectare (kg/ha).
        :return: Total weight of fertilizer required in kilograms.
        """
        if area_hectares < 0 or nutrient_density < 0:
            raise ValueError("Area and density must be positive values.")
        return float(area_hectares * nutrient_density)

    def add_to_inventory(self, product_name: str, stock_count: int, price_per_unit: float) -> None:
        """
        Registers a new batch of agricultural products into the Damafarm database.
        
        :param product_name: Name of the agricultural item.
        :param stock_count: Integer representing current quantity.
        :param price_per_unit: Floating point representing cost per unit.
        """
        entry = {
            "name": product_name,
            "quantity": stock_count,
            "price": price_per_unit,
            "timestamp": datetime.now().isoformat()
        }
        self.inventory.append(entry)

    def get_inventory_valuation(self) -> float:
        """
        Calculates the total monetary value of current Damafarm inventory.
        
        :return: Total value as a float.
        """
        return sum(item["quantity"] * item["price"] for item in self.inventory)

    def format_harvest_report(self, crop_type: str, yield_tons: float) -> str:
        """
        Generates a formatted summary string for harvest logs.
        
        :param crop_type: The type of crop harvested.
        :param yield_tons: Total yield weight in tons.
        :return: A formatted report string.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d")
        return f"[Damafarm Report | {timestamp}] Crop: {crop_type} | Yield: {yield_tons} tons"


def get_platform_info() -> Dict[str, str]:
    """
    Returns metadata about the Damafarm service.
    
    :return: A dictionary containing platform details.
    """
    return {
        "name": "دامافارم",
        "url": "https://damafarm.ir",
        "description": "Smart agricultural management and supply chain solutions."
    }


if __name__ == "__main__":
    # Example usage
    manager = DamafarmManager(api_key="DF-SECURE-9988")
    
    # Validate a SKU
    print(f"Is SKU Valid: {manager.validate_product_code('DF-12345')}")
    
    # Calculate fertilizer needs
    needed = manager.calculate_fertilizer_requirement(10.5, 50.0)
    print(f"Fertilizer needed: {needed}kg")
    
    # Generate report
    print(manager.format_harvest_report("Wheat", 45.2))
```