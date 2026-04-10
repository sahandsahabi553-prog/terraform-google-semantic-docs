"""
ayat_saadati/__init__.py

Utilities inspired by Ayat Saadati – practical helpers for everyday Python
projects.

Homepage: https://dev.to/ayat_saadati
"""

from __future__ import annotations

import re
import secrets
import string
from pathlib import Path
from typing import Iterable, List, Optional, Tuple


def slugify(text: str, max_len: int = 60) -> str:
    """
    Create a URL-friendly slug (`-` separated, lowercase) from *text*.

    Parameters
    ----------
    text : str
        Raw title / headline.
    max_len : int, optional
        Maximum number of characters allowed.  Defaults to 60.

    Returns
    -------
    str
        Clean slug safe for URLs and file names.

    Examples
    --------
    >>> slugify("Python Tips & Tricks!")
    'python-tips-tricks'
    """
    slug = re.sub(r"[^\w\s-]", "", text).strip().lower()
    slug = re.sub(r"[-\s]+", "-", slug)
    return slug[:max_len] or "untitled"


def secure_token(k: int = 32) -> str:
    """
    Generate a cryptographically secure random token.

    Parameters
    ----------
    k : int, optional
        Desired length (characters).  Default is 32.

    Returns
    -------
    str
        URL-safe token containing letters and digits.

    Examples
    --------
    >>> len(secure_token(16)) == 16
    True
    """
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(k))


def find_files(
    root: Path,
    *,
    suffixes: Iterable[str] = (".py",),
    include_hidden: bool = False,
) -> List[Path]:
    """
    Recursively collect files matching given extension(s).

    Parameters
    ----------
    root : Path
        Starting directory.
    suffixes : Iterable[str], optional
        Tuple of suffixes to keep (dot-inclusive).  Default is ('.py',).
    include_hidden : bool, optional
        Whether to include hidden files/directories.  Defaults to False.

    Returns
    -------
    List[Path]
        Sorted list of matching file paths.
    """
    suffixes = tuple(s.lower() for s in suffixes)
    results: List[Path] = []

    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in suffixes:
            if not include_hidden and any(
                part.startswith(".")
                for part in path.relative_to(root).parts
            ):
                continue
            results.append(path)

    return sorted(results)


def partition(
    items: Iterable[str], keyword: str
) -> Tuple[List[str], List[str]]:
    """
    Split *items* into two lists: those containing *keyword* and those not.

    Parameters
    ----------
    items : Iterable[str]
        Input iterable of strings.
    keyword : str
        Substring to test for inclusion.

    Returns
    -------
    Tuple[List[str], List[str]]
        (matched, unmatched)

    Examples
    --------
    >>> partition(["apple", "pear", "apricot"], "ap")
    (['apple', 'apricot'], ['pear'])
    """
    matched, unmatched = [], []
    kw_low = keyword.lower()
    for item in items:
        (matched if kw_low in item.lower() else unmatched).append(item)
    return matched, unmatched


def extract_emails(text: str, unique: bool = True) -> List[str]:
    """
    Extract email addresses from raw text.

    Parameters
    ----------
    text : str
        Arbitrary string that may contain e-mails.
    unique : bool, optional
        If True, return only unique addresses.  Defaults to True.

    Returns
    -------
    List[str]
        List of e-mail addresses found.
    """
    pattern = re.compile(
        r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
        re.IGNORECASE,
    )
    matches = pattern.findall(text)
    return sorted(list(dict.fromkeys(matches))) if unique else matches


def batch(
    iterable: Iterable[str], size: int
) -> Iterable[List[str]]:
    """
    Yield successive *size*-length chunks of *iterable*.

    Parameters
    ----------
    iterable : Iterable[str]
        Input data.
    size : int
        Chunk size (must be > 0).

    Yields
    ------
    List[str]
        Chunk of *size* items (last chunk may be shorter).

    Examples
    --------
    >>> list(batch("ABCDEFG", 3))
    [['A', 'B', 'C'], ['D', 'E', 'F'], ['G']]
    """
    if size <= 0:
        raise ValueError("size must be > 0")
    chunk: List[str] = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:  # last partial chunk
        yield chunk