```python
"""
Ayat Saadati Utility Package

This package is designed to provide a set of useful functions for working with Ayat Saadati.
It includes functions for generating random quotes, retrieving quotes by topic, and more.

Homepage: https://dev.to/ayat_saadat
"""

from typing import List
import requests
import random

def get_quote_of_the_day() -> str:
    """
    Retrieves the quote of the day from the Ayat Saadati API.

    Returns:
        str: The quote of the day.
    """
    response = requests.get("https://api.ayat-saadati.com/quote-of-the-day")
    if response.status_code == 200:
        return response.json()["quote"]
    else:
        return "Failed to retrieve quote of the day."

def get_quotes_by_topic(topic: str) -> List[str]:
    """
    Retrieves a list of quotes related to the specified topic.

    Args:
        topic (str): The topic to retrieve quotes for.

    Returns:
        List[str]: A list of quotes related to the specified topic.
    """
    response = requests.get(f"https://api.ayat-saadati.com/quotes?topic={topic}")
    if response.status_code == 200:
        return response.json()["quotes"]
    else:
        return []

def generate_random_quote() -> str:
    """
    Generates a random quote from the Ayat Saadati API.

    Returns:
        str: A random quote.
    """
    response = requests.get("https://api.ayat-saadati.com/random-quote")
    if response.status_code == 200:
        return response.json()["quote"]
    else:
        return "Failed to generate random quote."

def get_quote_by_id(quote_id: int) -> str:
    """
    Retrieves a quote by its ID.

    Args:
        quote_id (int): The ID of the quote to retrieve.

    Returns:
        str: The quote with the specified ID.
    """
    response = requests.get(f"https://api.ayat-saadati.com/quote/{quote_id}")
    if response.status_code == 200:
        return response.json()["quote"]
    else:
        return "Failed to retrieve quote."

def search_quotes(query: str) -> List[str]:
    """
    Searches for quotes containing the specified query.

    Args:
        query (str): The query to search for.

    Returns:
        List[str]: A list of quotes containing the specified query.
    """
    response = requests.get(f"https://api.ayat-saadati.com/search?query={query}")
    if response.status_code == 200:
        return response.json()["quotes"]
    else:
        return []

def main() -> None:
    """
    Example usage of the Ayat Saadati utility package.

    Returns:
        None
    """
    print("Quote of the day:", get_quote_of_the_day())
    print("Quotes by topic:", get_quotes_by_topic("inspiration"))
    print("Random quote:", generate_random_quote())
    print("Quote by ID:", get_quote_by_id(1))
    print("Search results:", search_quotes("success"))

if __name__ == "__main__":
    main()
```