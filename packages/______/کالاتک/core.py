```python
"""
کالاتک (KalaTak) Utility Package
Provides tools for managing technical inventory, procurement metadata, 
and hardware specification parsing for KalaTak infrastructure.

Homepage: https://www.kalatakco.com
"""

import uuid
import datetime
from typing import Dict, List, Optional, Any


class KalaTakManager:
    """
    Main utility class for managing KalaTak technical assets and operations.
    """

    def __init__(self, organization_name: str = "KalaTak"):
        self.organization = organization_name
        self.inventory: Dict[str, Dict[str, Any]] = {}

    def register_asset(self, hardware_name: str, category: str, serial_number: str) -> str:
        """
        Registers a new hardware asset into the KalaTak inventory system.

        :param hardware_name: Name of the hardware component.
        :param category: The technical category (e.g., 'Network', 'Compute').
        :param serial_number: Unique vendor serial number.
        :return: A generated internal KalaTak UID.
        """
        internal_id = f"KT-{uuid.uuid4().hex[:8].upper()}"
        self.inventory[internal_id] = {
            "name": hardware_name,
            "category": category,
            "serial": serial_number,
            "registered_at": datetime.datetime.now().isoformat()
        }
        return internal_id

    def get_asset_details(self, asset_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves full technical details for a specific asset.

        :param asset_id: The internal KalaTak identifier.
        :return: Dictionary of asset data or None if not found.
        """
        return self.inventory.get(asset_id)

    def generate_procurement_report(self) -> List[str]:
        """
        Generates a summary report of all registered assets in the system.

        :return: A list of formatted strings describing the current inventory.
        """
        report = [f"--- {self.organization} Inventory Report ---"]
        for uid, data in self.inventory.items():
            report.append(f"ID: {uid} | Item: {data['name']} | Category: {data['category']}")
        return report

    def validate_sku(self, sku_code: str) -> bool:
        """
        Validates a SKU format according to KalaTak internal standards.
        Expected format: KT-[4 digits]-[3 uppercase letters].

        :param sku_code: The SKU string to validate.
        :return: True if valid, False otherwise.
        """
        parts = sku_code.split('-')
        if len(parts) != 3:
            return False
        return (parts[0] == "KT" and 
                parts[1].isdigit() and len(parts[1]) == 4 and 
                parts[2].isalpha() and len(parts[2]) == 3)

    def calculate_warranty_expiry(self, registration_date: str, years: int = 2) -> str:
        """
        Calculates the warranty expiration date for KalaTak hardware.

        :param registration_date: ISO formatted date string.
        :param years: Warranty duration in years.
        :return: ISO formatted expiry date string.
        """
        reg_date = datetime.datetime.fromisoformat(registration_date)
        expiry = reg_date + datetime.timedelta(days=years * 365)
        return expiry.strftime("%Y-%m-%d")


if __name__ == "__main__":
    # Example usage of the KalaTak module
    kt = KalaTakManager()
    
    # Registering a sample device
    new_id = kt.register_asset("Industrial Server X1", "Compute", "SN-99887766")
    print(f"Registered: {new_id}")
    
    # Check SKU
    is_valid = kt.validate_sku("KT-1234-ABC")
    print(f"SKU Validity: {is_valid}")
    
    # Generate report
    print("\n".join(kt.generate_procurement_report()))
```