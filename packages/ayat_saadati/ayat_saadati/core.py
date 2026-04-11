```python
"""
ayat_saadati – Personal utility toolkit for everyday Python workflows.

Homepage: https://dev.to/ayat_saadati
Author: Ayat Saadati
"""

from __future__ import annotations

import csv
import json
import os
import re
import time
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Union

__version__ = "1.0.0"

JSONType = Union[Dict[str, Any], List[Any], str, int, float, bool, None]


def ensure_directory(path: Union[str, Path]) -> Path:
    """
    Ensure that *path* exists as a directory, creating it if necessary.

    Parameters
    ----------
    path : str or pathlib.Path
        Target directory path.

    Returns
    -------
    pathlib.Path
        Absolute path to the directory (guaranteed to exist).

    Examples
    --------
    >>> ensure_directory("logs")
    PosixPath('/absolute/path/to/logs')
    """
    path = Path(path).expanduser().resolve()
    path.mkdir(parents=True, exist_ok=True)
    return path


def atomic_write_text(
    content: str,
    target: Union[str, Path],
    *,
    encoding: str = "utf-8",
    newline: str = "",
) -> None:
    """
    Atomically write *content* to *target* file.

    The file is first written to a temporary sibling with ``.tmp`` suffix
    and then renamed to *target*, ensuring that *target* is never in a
    half-written state.

    Parameters
    ----------
    content : str
        Text to be written.
    target : str or pathlib.Path
        Destination file path.
    encoding : str, optional
        Text encoding (default ``utf-8``).
    newline : str, optional
        Controls universal newlines (default ``""``).
    """
    target = Path(target).expanduser().resolve()
    tmp = target.with_suffix(target.suffix + ".tmp")

    try:
        tmp.write_text(content, encoding=encoding, newline=newline)
        tmp.replace(target)
    except Exception:
        tmp.unlink(missing_ok=True)
        raise


def load_json_or_default(
    path: Union[str, Path],
    *,
    default: JSONType = None,
    encoding: str = "utf-8",
) -> JSONType:
    """
    Load JSON from *path* or return *default* if the file does not exist or is invalid.

    Parameters
    ----------
    path : str or pathlib.Path
        JSON file path.
    default : JSON-serializable, optional
        Value returned when loading fails (default ``None``).
    encoding : str, optional
        Text encoding (default ``utf-8``).

    Returns
    -------
    dict | list | str | int | float | bool | None
        Parsed JSON or *default*.
    """
    try:
        with open(path, encoding=encoding) as fh:
            return json.load(fh)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def slugify(text: str, *, sep: str = "-") -> str:
    """
    Convert *text* to URL-safe slug.

    Lower-cases the string and replaces non-alphanumeric characters with *sep*.

    Parameters
    ----------
    text : str
        Input string.
    sep : str, optional
        Separator (default ``"-"``).

    Returns
    -------
    str
        Slugified string.

    Examples
    --------
    >>> slugify("Hello, World!")
    'hello-world'
    >>> slugify("Python 3.12", sep="_")
    'python_3_12'
    """
    text = re.sub(r"[^\w\s-]", "", text.lower())
    text = re.sub(r"[-\s]+", sep, text).strip(sep)
    return text


def csv_to_jsonl(
    csv_path: Union[str, Path],
    jsonl_path: Union[str, Path],
    *,
    encoding: str = "utf-8",
    dialect: str = "excel",
) -> None:
    """
    Convert CSV file to JSON-lines format.

    Parameters
    ----------
    csv_path : str or pathlib.Path
        Source CSV file.
    jsonl_path : str or pathlib.Path
        Destination JSON-lines file.
    encoding : str, optional
        Text encoding (default ``utf-8``).
    dialect : str, optional
        CSV dialect (default ``"excel"``).
    """
    with open(csv_path, newline="", encoding=encoding) as csv_f, open(
        jsonl_path, "w", encoding=encoding
    ) as jl_f:
        reader = csv.DictReader(csv_f, dialect=dialect)
        for row in reader:
            jl_f.write(json.dumps(row, ensure_ascii=False) + "\n")


def timed_cache(seconds: int = 60) -> Any:
    """
    Decorator that caches a function result for *seconds*.

    Parameters
    ----------
    seconds : int, optional
        Cache duration in seconds (default ``60``).

    Returns
    -------
    Callable
        Decorated function with time-based cache.
    """

    def decorator(func):
        cache: Dict[str, tuple[float, Any]] = {}

        def wrapper(*args, **kwargs):
            key = str(args) + str(sorted(kwargs.items()))
            now = time.monotonic()
            if key in cache:
                stamp, value = cache[key]
                if now - stamp < seconds:
                    return value
            value = func(*args, **kwargs)
            cache[key] = (now, value)
            return value

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper

    return decorator


def flatten_dict(
    data: Dict[str, Any],
    *,
    parent_key: str = "",
    sep: str = ".",
) -> Dict[str, Any]:
    """
    Flatten nested dictionary into single-level keys using *sep*.

    Parameters
    ----------
    data : dict
        Source dictionary.
    parent_key : str, optional
        Internal parameter for recursion (default ``""``).
    sep : str, optional
        Separator (default ``"."``).

    Returns
    -------
    dict
        Flattened dictionary.

    Examples
    --------
    >>> flatten_dict({"a": {"b": 1, "c": {"d": 2}}})
    {'a.b': 1, 'a.c.d': 2}
    """
    items: List[tuple[str, Any]] = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, parent_key=new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def env_bool(name: str, default: bool = False) -> bool:
    """
    Retrieve boolean value from environment variable.

    Accepts ``true``, ``yes``, ``1``, ``on`` (case-insensitive) as ``True``;
    everything else is ``False``.

    Parameters
    ----------
    name : str
        Environment variable name.
    default : bool, optional
        Default value if variable is not set (default ``False``).

    Returns
    -------
    bool
        Parsed boolean.

    Examples
    --------
    >>> import os
    >>> os.environ["DEBUG"] = "yes"
    >>> env_bool("DEBUG")
    True
    """
    val = os.getenv(name)
    if val is None:
        return default
    return val.lower() in {"true", "yes", "1", "on"}
```