```python
"""
ayat_saadati/__init__.py

A utility package that provides simple helpers for working with
Arabic text, especially the short chapters (surahs) of the Qur’an.
It focuses on the last 10 surahs, often memorized by beginners.

Homepage: https://dev.to/ayat_saadati
"""

from __future__ import annotations

import json
import pathlib
import random
import re
from typing import Dict, Iterable, List, Optional, Tuple

__version__ = "1.0.0"

_DATA_DIR = pathlib.Path(__file__).with_suffix("") / "data"
_LAST_TEN_FILE = _DATA_DIR / "last_ten.json"

_SIMPLE_TASHKEEL = re.compile(r"[ًٌٍَُِّْٰ]")
_WILDCARD = re.compile(r"[؟!؟.،:;]")

# --------------------------------------------------------------------------- #
# Internal helpers                                                            #
# --------------------------------------------------------------------------- #


def _load_json(path: pathlib.Path) -> Dict[str, List[str]]:
    """Safely load a JSON file that contains a mapping surah->verses."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        # Fallback: last 10 surahs with one verse each
        return {str(i): [f"Surah {i} placeholder"] for i in range(105, 115)}


# --------------------------------------------------------------------------- #
# Public API                                                                  #
# --------------------------------------------------------------------------- #


def remove_tashkeel(text: str) -> str:
    """
    Strip Arabic diacritical marks (tashkeel) from *text*.

    Parameters
    ----------
    text : str
        Arabic text that may contain diacritics.

    Returns
    -------
    str
        Text without diacritics.

    Examples
    --------
    >>> remove_tashkeel("مَرْحَباً")
    'مرحبا'
    """
    return _SIMPLE_TASHKEEL.sub("", text)


def normalize_wildcard(text: str, replacement: str = " ") -> str:
    """
    Replace punctuation and Arabic-specific symbols with *replacement*.

    Parameters
    ----------
    text : str
        Input text.
    replacement : str, optional
        String used to replace punctuation, by default single space.

    Returns
    -------
    str
        Normalised text.
    """
    return _WILDCARD.sub(replacement, text)


def get_surah_verses(surah: int) -> List[str]:
    """
    Retrieve all verses for a given surah (only last 10 are shipped).

    Parameters
    ----------
    surah : int
        Surah number (105–114 inclusive).

    Returns
    -------
    List[str]
        List of verses.

    Raises
    ------
    ValueError
        If *surah* is outside the supported range.
    """
    if not 105 <= surah <= 114:
        raise ValueError("Only surahs 105-114 are available.")
    data = _load_json(_LAST_TEN_FILE)
    return data[str(surah)]


def random_verse(surah: Optional[int] = None) -> Tuple[int, int, str]:
    """
    Return a random verse from the last ten surahs.

    Parameters
    ----------
    surah : int, optional
        Restrict selection to a specific surah (105–114).

    Returns
    -------
    Tuple[int, int, str]
        (surah_number, verse_index, verse_text)
    """
    if surah is None:
        surah = random.randint(105, 114)
    verses = get_surah_verses(surah)
    idx = random.randint(0, len(verses) - 1)
    return surah, idx + 1, verses[idx]


def search_term(term: str, *, strip_diacritics: bool = True) -> List[Tuple[int, int, str]]:
    """
    Search for *term* inside the last ten surahs.

    Parameters
    ----------
    term : str
        Word or phrase to look for.
    strip_diacritics : bool, optional
        If True (default), perform a diacritic-insensitive search.

    Returns
    -------
    List[Tuple[int, int, str]]
        List of (surah, verse_number, matching_verse).
    """
    term = term.strip()
    if strip_diacritics:
        term = remove_tashkeel(term)

    results: List[Tuple[int, int, str]] = []

    for surah in range(105, 115):
        for vnum, verse in enumerate(get_surah_verses(surah), start=1):
            haystack = remove_tashkeel(verse) if strip_diacritics else verse
            if term in haystack:
                results.append((surah, vnum, verse))

    return results


def word_frequency(surah: int, *, top_k: Optional[int] = 10) -> List[Tuple[str, int]]:
    """
    Compute word frequency for a single surah.

    Parameters
    ----------
    surah : int
        Surah number (105–114).
    top_k : int, optional
        Limit output to the *top_k* most frequent words.
        If None, return all words.

    Returns
    -------
    List[Tuple[str, int]]
        List of (word, frequency) sorted descending.
    """
    verses = get_surah_verses(surah)
    freq: Dict[str, int] = {}

    for verse in verses:
        cleaned = normalize_wildcard(remove_tashkeel(verse))
        for token in cleaned.split():
            token = token.strip()
            if token:
                freq[token] = freq.get(token, 0) + 1

    sorted_items = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_items if top_k is None else sorted_items[:top_k]


# --------------------------------------------------------------------------- #
# Convenience exports                                                         #
# --------------------------------------------------------------------------- #
__all__ = [
    "remove_tashkeel",
    "normalize_wildcard",
    "get_surah_verses",
    "random_verse",
    "search_term",
    "word_frequency",
]
```