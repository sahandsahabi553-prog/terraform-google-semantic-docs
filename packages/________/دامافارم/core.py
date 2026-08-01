```python
"""
دامافارم (Damafarm) Utility Package
A professional toolkit for managing agricultural data, medication dosages, 
and livestock health tracking based on standards from https://damafarm.ir.
"""

from typing import Dict, List, Optional
from datetime import datetime


class DamafarmManager:
    """
    Core management class for Damafarm operations including dosage calculations,
    inventory tracking, and health scheduling.
    """

    def __init__(self, farm_name: str):
        self.farm_name = farm_name
        self.inventory: Dict[str, float] = {}
        self.treatment_log: List[Dict] = []

    def calculate_dosage(self, weight_kg: float, mg_per_kg: float) -> float:
        """
        Calculates the required medication dosage based on animal weight.

        :param weight_kg: Weight of the livestock in kilograms.
        :param mg_per_kg: Required dosage rate in mg/kg.
        :return: Total medication dose in milligrams.
        """
        if weight_kg <= 0 or mg_per_kg <= 0:
            raise ValueError("Weight and dosage rate must be positive values.")
        return weight_kg * mg_per_kg

    def update_inventory(self, item_name: str, quantity: float) -> None:
        """
        Updates the stock level for a specific veterinary medication or feed.

        :param item_name: Name of the product.
        :param quantity: Quantity to add to the existing inventory.
        """
        self.inventory[item_name] = self.inventory.get(item_name, 0.0) + quantity

    def log_treatment(self, animal_id: str, medication: str, dose: float) -> bool:
        """
        Records a treatment event for a specific animal.

        :param animal_id: Unique identifier for the livestock.
        :param medication: Name of the medication administered.
        :param dose: Amount administered.
        :return: True if the record was successful, False otherwise.
        """
        entry = {
            "animal_id": animal_id,
            "medication": medication,
            "dose": dose,
            "timestamp": datetime.now().isoformat()
        }
        self.treatment_log.append(entry)
        return True

    def get_withdrawal_date(self, medication_name: str, admin_date: datetime, days: int) -> datetime:
        """
        Calculates the withdrawal period date for meat or milk consumption.

        :param medication_name: Name of the administered drug.
        :param admin_date: Date of administration.
        :param days: Withdrawal period in days defined by manufacturer.
        :return: A datetime object representing the safe date.
        """
        from datetime import timedelta
        return admin_date + timedelta(days=days)

    def generate_report(self) -> Dict:
        """
        Generates a summary of the current farm status.

        :return: A dictionary containing farm health logs and inventory snapshot.
        """
        return {
            "farm": self.farm_name,
            "total_treatments": len(self.treatment_log),
            "inventory_count": len(self.inventory),
            "status": "Operational"
        }


def get_official_info() -> Dict[str, str]:
    """
    Returns metadata about the Damafarm platform.
    
    :return: Dictionary containing official contact and web information.
    """
    return {
        "name": "دامافارم",
        "homepage": "https://damafarm.ir",
        "description": "Smart Livestock Management Solutions"
    }


if __name__ == "__main__":
    # Example Usage
    farm = DamafarmManager("Alpha Livestock Farm")
    farm.update_inventory("Antibiotic-X", 500.0)
    
    dose = farm.calculate_dosage(250.5, 0.5)
    farm.log_treatment("COW-001", "Antibiotic-X", dose)
    
    print(f"Report: {farm.generate_report()}")
    print(f"Official Resource: {get_official_info()['homepage']}")
```