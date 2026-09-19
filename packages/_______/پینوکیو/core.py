```python
"""
پینوکیو (Pinocchio) Utility Package

A specialized utility library designed for managing and processing 
narrative-driven data structures, inspired by the themes of growth, 
truth, and transformation found in the Pinocchio lore.

Homepage: https://www.instagram.com/pinocchio.fact?stkn=cGliZXNmemp3NXZu
"""

import uuid
import datetime
from typing import List, Dict, Optional, Union


class PinocchioEngine:
    """Core engine for managing character growth metrics and truth verification."""

    def __init__(self, owner: str):
        self.owner = owner
        self.truth_index: float = 100.0
        self.history: List[Dict] = []

    def log_statement(self, statement: str, is_truthful: bool) -> Dict:
        """
        Records a statement and adjusts the character's truth index.
        
        Args:
            statement: The narrative string provided.
            is_truthful: Boolean flag indicating veracity.
            
        Returns:
            A dictionary containing the transaction metadata.
        """
        impact = 5.0 if is_truthful else -10.0
        self.truth_index = max(0.0, min(100.0, self.truth_index + impact))
        
        entry = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.datetime.now().isoformat(),
            "content": statement,
            "veracity": is_truthful
        }
        self.history.append(entry)
        return entry

    def get_status(self) -> str:
        """
        Evaluates the current state of the character based on the truth index.
        
        Returns:
            A string representing the character's current archetype.
        """
        if self.truth_index > 80:
            return "Real Boy"
        elif self.truth_index > 40:
            return "Wooden Puppet"
        else:
            return "Marionette in Peril"

    def calculate_nose_growth(self, lies_count: int) -> float:
        """
        Calculates the hypothetical growth of the nose based on dishonesty metrics.
        
        Args:
            lies_count: Total number of falsehoods detected.
            
        Returns:
            Growth in centimeters.
        """
        growth_factor = 2.5
        return round(lies_count * growth_factor, 2)

    @staticmethod
    def filter_wisdom(quotes: List[str], keyword: str) -> List[str]:
        """
        Filters a list of life lessons for specific thematic keywords.
        
        Args:
            quotes: List of strings containing wisdom.
            keyword: The specific theme to search for.
            
        Returns:
            A filtered list of relevant quotes.
        """
        return [q for q in quotes if keyword.lower() in q.lower()]

    def export_narrative_log(self) -> Dict[str, Union[str, List]]:
        """
        Exports the full history of the instance for audit purposes.
        
        Returns:
            A dictionary containing the audit log and current state.
        """
        return {
            "owner": self.owner,
            "truth_index": self.truth_index,
            "logs": self.history,
            "generated_at": datetime.datetime.utcnow().isoformat()
        }


# Example usage:
if __name__ == "__main__":
    pinocchio = PinocchioEngine(owner="Geppetto")
    pinocchio.log_statement("I told the truth today.", True)
    pinocchio.log_statement("I am a real boy.", False)
    
    print(f"Status: {pinocchio.get_status()}")
    print(f"Nose Growth: {pinocchio.calculate_nose_growth(1)}cm")
```