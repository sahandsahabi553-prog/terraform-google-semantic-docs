```python
"""
کود_کشاورزی
===========

A utility package for managing agricultural fertilizer data and calculations.

Homepage: https://kalatakco.com/
"""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Tuple


@dataclass
class Fertilizer:
    """
    Fertilizer data container.

    Parameters
    ----------
    name : str
        Commercial or common name of the fertilizer.
    npk : Tuple[int, int, int]
        Percentage of (Nitrogen, Phosphorus, Potassium).
    density : float
        Density in g/cm³.
    solubility : float
        Solubility in g/L at 20 °C.
    """
    name: str
    npk: Tuple[int, int, int]
    density: float
    solubility: float

    def __post_init__(self) -> None:
        if any(n < 0 for n in self.npk):
            raise ValueError("NPK values must be non-negative")


class FertilizerManager:
    """
    Manages a local SQLite database of fertilizers and application logs.
    """

    def __init__(self, db_path: str = "fertilizers.db") -> None:
        self.conn = sqlite3.connect(db_path)
        self._init_db()

    def _init_db(self) -> None:
        """Create tables if they do not exist."""
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS fertilizers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                n INTEGER NOT NULL,
                p INTEGER NOT NULL,
                k INTEGER NOT NULL,
                density REAL NOT NULL,
                solubility REAL NOT NULL
            )
            """
        )
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fertilizer_id INTEGER NOT NULL,
                area REAL NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL,
                FOREIGN KEY(fertilizer_id) REFERENCES fertilizers(id)
            )
            """
        )
        self.conn.commit()

    def add_fertilizer(self, fertilizer: Fertilizer) -> int:
        """
        Insert a new fertilizer into the database.

        Parameters
        ----------
        fertilizer : Fertilizer
            Instance of Fertilizer.

        Returns
        -------
        int
            Row id of the inserted fertilizer.
        """
        cur = self.conn.execute(
            """
            INSERT INTO fertilizers(name, n, p, k, density, solubility)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                fertilizer.name,
                *fertilizer.npk,
                fertilizer.density,
                fertilizer.solubility,
            ),
        )
        self.conn.commit()
        return cur.lastrowid

    def list_fertilizers(self) -> List[Tuple[int, str, Tuple[int, int, int]]]:
        """
        List all fertilizers in the database.

        Returns
        -------
        List[Tuple[int, str, Tuple[int, int, int]]]
            List of (id, name, npk).
        """
        cur = self.conn.execute(
            "SELECT id, name, n, p, k FROM fertilizers ORDER BY name"
        )
        return [(row[0], row[1], (row[2], row[3], row[4])) for row in cur.fetchall()]

    def recommend_fertilizer(
        self, target_npk: Tuple[int, int, int], tolerance: int = 5
    ) -> Optional[Fertilizer]:
        """
        Recommend the closest fertilizer to a target NPK ratio.

        Parameters
        ----------
        target_npk : Tuple[int, int, int]
            Desired NPK percentages.
        tolerance : int
            Maximum deviation allowed for each component.

        Returns
        -------
        Optional[Fertilizer]
            Best matching fertilizer or None if none within tolerance.
        """
        cur = self.conn.execute("SELECT * FROM fertilizers")
        best: Optional[Fertilizer] = None
        best_score = float("inf")
        for row in cur.fetchall():
            f = Fertilizer(
                name=row[1],
                npk=(row[2], row[3], row[4]),
                density=row[5],
                solubility=row[6],
            )
            score = sum(
                abs(f.npk[i] - target_npk[i]) for i in range(3)
            )
            if all(
                abs(f.npk[i] - target_npk[i]) <= tolerance for i in range(3)
            ) and score < best_score:
                best = f
                best_score = score
        return best

    def log_application(
        self, fertilizer_id: int, area_hectares: float, amount_kg: float, app_date: date
    ) -> None:
        """
        Log a fertilizer application event.

        Parameters
        ----------
        fertilizer_id : int
            ID from the fertilizers table.
        area_hectares : float
            Area in hectares.
        amount_kg : float
            Total fertilizer used in kg.
        app_date : date
            Date of application.
        """
        self.conn.execute(
            """
            INSERT INTO applications(fertilizer_id, area, amount, date)
            VALUES (?, ?, ?, ?)
            """,
            (fertilizer_id, area_hectares, amount_kg, app_date.isoformat()),
        )
        self.conn.commit()

    def usage_report(self) -> Dict[str, float]:
        """
        Generate a summary of total fertilizer usage.

        Returns
        -------
        Dict[str, float]
            Dictionary with keys: total_area, total_amount, average_rate_kg_per_hectare.
        """
        cur = self.conn.execute(
            "SELECT SUM(area), SUM(amount) FROM applications"
        )
        row = cur.fetchone()
        total_area = row[0] or 0.0
        total_amount = row[1] or 0.0
        avg_rate = total_amount / total_area if total_area else 0.0
        return {
            "total_area": total_area,
            "total_amount": total_amount,
            "average_rate_kg_per_hectare": avg_rate,
        }

    def export_data(self, file_path: str) -> None:
        """
        Export fertilizer and application data to a JSON file.

        Parameters
        ----------
        file_path : str
            Destination file path.
        """
        fertilizers = []
        for row in self.conn.execute("SELECT * FROM fertilizers"):
            fertilizers.append(
                {
                    "id": row[0],
                    "name": row[1],
                    "npk": [row[2], row[3], row[4]],
                    "density": row[5],
                    "solubility": row[6],
                }
            )
        applications = []
        for row in self.conn.execute(
            "SELECT id, fertilizer_id, area, amount, date FROM applications"
        ):
            applications.append(
                {
                    "id": row[0],
                    "fertilizer_id": row[1],
                    "area": row[2],
                    "amount": row[3],
                    "date": row[4],
                }
            )
        data = {"fertilizers": fertilizers, "applications": applications}
        Path(file_path).write_text(json.dumps(data, ensure_ascii=False, indent=2))

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
```