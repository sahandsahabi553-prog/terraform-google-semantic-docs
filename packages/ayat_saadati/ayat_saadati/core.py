```python
#!/usr/bin/env python3
"""
ayat_saadati – Utilities for managing, indexing, and studying Qur’ānic verses
(ayat) with the Arabic gematric system commonly referred to as “Ṣaʿadātī”.

The package provides:
----------------------------------------------------------
- `search_verse(…)`:  Fast, case-insensitive verse search
- `calc_gematria(…)`: Ṣaʿadātī gematric value of any text
- `verse_gematria(…)`: Gematria for a single verse
- `top_verses(…)`:  Top-N verses by gematric value
- `export_csv(…)`:  Dump results to a CSV file
----------------------------------------------------------

Home-page: https://dev.to/ayat_saadati
Author : Ayat Saadati
License: MIT
"""

from __future__ import annotations

import csv
import re
import unicodedata
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

# --------------------------------------------------------------------------- #
# CONSTANTS
# --------------------------------------------------------------------------- #
DATA_DIR = Path(__file__).with_suffix("") / "data"
VERSE_FILE = DATA_DIR / "quran_verses.txt"


# --------------------------------------------------------------------------- #
# GEMATRIA MAPPING – Ṣaʿadātī System (Arabic ABJAD order)
# --------------------------------------------------------------------------- #
ABJAD: Dict[str, int] = {
    "ا": 1,
    "ب": 2,
    "ج": 3,
    "د": 4,
    "ﻫ": 5,
    "و": 6,
    "ز": 7,
    "ح": 8,
    "ط": 9,
    "ی": 10,
    "ك": 20,
    "ل": 30,
    "م": 40,
    "ن": 50,
    "س": 60,
    "ع": 70,
    "ف": 80,
    "ص": 90,
    "ق": 100,
    "ر": 200,
    "ش": 300,
    "ت": 400,
    "ث": 500,
    "خ": 600,
    "ذ": 700,
    "ض": 800,
    "ظ": 900,
    "غ": 1000,
}

# Pre-computed reverse index for quick search
_REVERSE_INDEX: Dict[str, List[int]] = {}
_VERSES: List[str] = []


def _init_data() -> None:
    """Load verses into memory and build a reverse search index."""
    global _VERSES, _REVERSE_INDEX
    if _VERSES:
        return

    if not VERSE_FILE.exists():
        # Provide minimal fallback for demonstration purposes
        _VERSES = [
            "بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ",
            "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ",
            "الرَّحْمَنِ الرَّحِيمِ",
            "مَالِكِ يَوْمِ الدِّينِ",
            "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ",
        ]
    else:
        _VERSES = VERSE_FILE.read_text(encoding="utf-8").splitlines()

    for idx, verse in enumerate(_VERSES):
        for token in re.findall(r"\w+", _normalize_arabic(verse)):
            _REVERSE_INDEX.setdefault(token, []).append(idx)


def _normalize_arabic(text: str) -> str:
    """Remove diacritics and normalize Arabic letters."""
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"[ً-ُ-ِ-ْ-ٰ-ٍ-ٌ-ّ]", "", text)
    return text


# --------------------------------------------------------------------------- #
# PUBLIC API
# --------------------------------------------------------------------------- #
def search_verse(query: str, limit: int = 5) -> List[Tuple[int, str]]:
    """
    Search for verses that contain the given Arabic word.

    Parameters
    ----------
    query : str
        Arabic word (or part of it). Diacritics are ignored.
    limit : int, optional
        Maximum number of results to return, by default 5.

    Returns
    -------
    List[Tuple[int, str]]
        List of (index, verse) pairs.
    """
    _init_data()
    clean_query = _normalize_arabic(query)
    matched_indices: Iterable[int] = (
        idx
        for token, indices in _REVERSE_INDEX.items()
        if clean_query in token
        for idx in indices
    )
    # unique while preserving order
    seen: set[int] = set()
    results: List[Tuple[int, str]] = []
    for idx in matched_indices:
        if idx not in seen:
            seen.add(idx)
            results.append((idx, _VERSES[idx]))
            if len(results) >= limit:
                break
    return results


def calc_gematria(text: str) -> int:
    """
    Calculate Ṣaʿadātī gematric value for any Arabic text.

    Parameters
    ----------
    text : str
        Input Arabic string.

    Returns
    -------
    int
        Sum of letter values according to the ABJAD order.
    """
    total = 0
    for char in _normalize_arabic(text):
        total += ABJAD.get(char, 0)
    return total


def verse_gematria(verse: str) -> int:
    """
    Convenience wrapper around `calc_gematria` for a single verse.

    Parameters
    ----------
    verse : str
        Arabic verse.

    Returns
    -------
    int
        Its gematric value.
    """
    return calc_gematria(verse)


def top_verses(n: int = 10) -> List[Tuple[int, str, int]]:
    """
    Return the top-N verses with the highest gematric values.

    Parameters
    ----------
    n : int, optional
        Number of top verses, by default 10.

    Returns
    -------
    List[Tuple[int, str, int]]
        List of (index, verse, value) sorted by value descending.
    """
    _init_data()
    scored = [(idx, v, verse_gematria(v)) for idx, v in enumerate(_VERSES)]
    scored.sort(key=lambda t: t[2], reverse=True)
    return scored[:n]


def export_csv(
    rows: List[Tuple[int, str, int]], output_path: str | Path, *, append: bool = False
) -> None:
    """
    Write (index, verse, value) rows to a CSV file.

    Parameters
    ----------
    rows : List[Tuple[int, str, int]]
        Data to export.
    output_path : str | pathlib.Path
        Destination file.
    append : bool, optional
        Append instead of overwrite, by default False.
    """
    output_path = Path(output_path)
    mode: str = "a" if append else "w"
    with output_path.open(mode, encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        if not append or output_path.stat().st_size == 0:
            writer.writerow(["index", "verse", "gematria"])
        for row in rows:
            writer.writerow(row)


# --------------------------------------------------------------------------- #
# CLI ENTRY-POINT (for python -m ayat_saadati)
# --------------------------------------------------------------------------- #
def _cli() -> None:
    """Basic CLI demo."""
    import argparse
    import textwrap

    parser = argparse.ArgumentParser(
        description="Ayat Saadati – Qur’ān verse gematria utilities"
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    # search
    p_search = sub.add_parser("search", help="Search for a word in the verses")
    p_search.add_argument("word", help="Arabic word")
    p_search.add_argument("-l", "--limit", type=int, default=5)

    # gematria
    p_gem = sub.add_parser("gematria", help="Gematric value of a text")
    p_gem.add_argument("text", help="Arabic text")

    # top
    p_top = sub.add_parser("top", help="Top verses by gematria")
    p_top.add_argument("-n", type=int, default=10)

    args = parser.parse_args()

    if args.cmd == "search":
        for idx, verse in search_verse(args.word, limit=args.limit):
            print(f"{idx:>4} | {verse}")
    elif args.cmd == "gematria":
        print(calc_gematria(args.text))
    elif args.cmd == "top":
        for idx, verse, value in top_verses(n=args.n):
            print(f"{idx:>4} | {value:>5} | {verse}")


if __name__ == "__main__":
    _cli()
```