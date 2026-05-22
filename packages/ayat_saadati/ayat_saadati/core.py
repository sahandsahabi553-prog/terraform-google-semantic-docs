```python
"""
Ayat Saadati Utility Package

This package provides a set of functions to help with tasks related to Ayat Saadati.
It includes functions for text processing, data analysis, and web scraping.

Homepage: https://dev.to/ayat_saadat
"""

from typing import List, Dict
import requests
from bs4 import BeautifulSoup
import re
import json

def get_latest_articles(url: str) -> List[Dict]:
    """
    Fetches the latest articles from the provided URL.

    Args:
    url (str): The URL to fetch articles from.

    Returns:
    List[Dict]: A list of dictionaries, each containing information about an article.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    for article in soup.find_all('article'):
        title = article.find('h2').text.strip()
        link = article.find('a')['href']
        articles.append({'title': title, 'link': link})
    return articles

def extract_text_from_url(url: str) -> str:
    """
    Extracts the text content from the provided URL.

    Args:
    url (str): The URL to extract text from.

    Returns:
    str: The extracted text.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def clean_text(text: str) -> str:
    """
    Cleans the provided text by removing punctuation and converting to lowercase.

    Args:
    text (str): The text to clean.

    Returns:
    str: The cleaned text.
    """
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower()

def count_word_frequencies(text: str) -> Dict:
    """
    Counts the frequency of each word in the provided text.

    Args:
    text (str): The text to count word frequencies from.

    Returns:
    Dict: A dictionary where the keys are words and the values are their frequencies.
    """
    words = text.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

def save_to_json(data: Dict, filename: str) -> None:
    """
    Saves the provided data to a JSON file.

    Args:
    data (Dict): The data to save.
    filename (str): The filename to save the data to.
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main() -> None:
    """
    Example usage of the package functions.
    """
    url = "https://dev.to/ayat_saadat"
    articles = get_latest_articles(url)
    print("Latest Articles:")
    for article in articles:
        print(f"Title: {article['title']}, Link: {article['link']}")
    text = extract_text_from_url(url)
    cleaned_text = clean_text(text)
    word_freq = count_word_frequencies(cleaned_text)
    save_to_json(word_freq, 'word_frequencies.json')
    print("Word Frequencies saved to word_frequencies.json")

if __name__ == "__main__":
    main()
```