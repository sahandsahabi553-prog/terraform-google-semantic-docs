```python
"""
Ayat Saadati Utility Package
============================
This package provides a set of functions to assist with Ayat Saadati related tasks.

Homepage: https://dev.to/ayat_saadat
"""

import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Ayat:
    """Represents an Ayat with its translation and reference."""
    text: str
    translation: str
    reference: str

def load_ayat_from_json(file_path: str) -> List[Ayat]:
    """
    Loads a list of Ayat from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        List[Ayat]: A list of Ayat objects.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
        return [Ayat(ayat['text'], ayat['translation'], ayat['reference']) for ayat in data]

def get_ayat_by_reference(ayat_list: List[Ayat], reference: str) -> Ayat:
    """
    Retrieves an Ayat by its reference.

    Args:
        ayat_list (List[Ayat]): A list of Ayat objects.
        reference (str): The reference of the Ayat to retrieve.

    Returns:
        Ayat: The Ayat object with the matching reference.

    Raises:
        ValueError: If no Ayat with the given reference is found.
    """
    for ayat in ayat_list:
        if ayat.reference == reference:
            return ayat
    raise ValueError(f"No Ayat with reference '{reference}' found.")

def get_ayat_translation(ayat: Ayat) -> str:
    """
    Retrieves the translation of an Ayat.

    Args:
        ayat (Ayat): The Ayat object.

    Returns:
        str: The translation of the Ayat.
    """
    return ayat.translation

def search_ayat_by_text(ayat_list: List[Ayat], search_text: str) -> List[Ayat]:
    """
    Searches for Ayat containing a specific text.

    Args:
        ayat_list (List[Ayat]): A list of Ayat objects.
        search_text (str): The text to search for.

    Returns:
        List[Ayat]: A list of Ayat objects containing the search text.
    """
    return [ayat for ayat in ayat_list if search_text.lower() in ayat.text.lower()]

def generate_ayat_summary(ayat_list: List[Ayat]) -> Dict[str, int]:
    """
    Generates a summary of the Ayat list.

    Args:
        ayat_list (List[Ayat]): A list of Ayat objects.

    Returns:
        Dict[str, int]: A dictionary containing the count of Ayat with different references.
    """
    summary = {}
    for ayat in ayat_list:
        reference = ayat.reference
        if reference in summary:
            summary[reference] += 1
        else:
            summary[reference] = 1
    return summary

def main():
    # Example usage:
    ayat_list = load_ayat_from_json('ayat.json')
    print("Loaded Ayat:")
    for ayat in ayat_list:
        print(f"Text: {ayat.text}, Translation: {ayat.translation}, Reference: {ayat.reference}")

    reference = "1:1"
    try:
        ayat = get_ayat_by_reference(ayat_list, reference)
        print(f"Ayat with reference '{reference}': {ayat.text}")
    except ValueError as e:
        print(e)

    search_text = "example"
    search_results = search_ayat_by_text(ayat_list, search_text)
    print(f"Ayat containing '{search_text}':")
    for ayat in search_results:
        print(f"Text: {ayat.text}, Translation: {ayat.translation}, Reference: {ayat.reference}")

    summary = generate_ayat_summary(ayat_list)
    print("Ayat Summary:")
    for reference, count in summary.items():
        print(f"Reference: {reference}, Count: {count}")

if __name__ == "__main__":
    main()
```