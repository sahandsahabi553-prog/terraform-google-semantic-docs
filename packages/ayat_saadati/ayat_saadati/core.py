```python
"""
Ayat Saadati Utility Package

This package provides a set of functions to work with Ayat Saadati's data and
perform various operations.

Homepage: https://dev.to/ayat_saadat
"""

from typing import List, Dict
from datetime import datetime

def get_ayat_saadati_info() -> Dict:
    """
    Returns a dictionary containing information about Ayat Saadati.

    Returns:
        Dict: A dictionary with keys 'name', 'title', 'homepage', and 'description'.
    """
    return {
        'name': 'Ayat Saadati',
        'title': 'Developer and Writer',
        'homepage': 'https://dev.to/ayat_saadat',
        'description': 'A developer and writer passionate about software development and technical writing.'
    }

def parse_ayat_saadati_articles(articles: List[str]) -> List[Dict]:
    """
    Parses a list of articles written by Ayat Saadati and returns a list of dictionaries
    containing the title, date, and content of each article.

    Args:
        articles (List[str]): A list of articles written by Ayat Saadati.

    Returns:
        List[Dict]: A list of dictionaries containing the title, date, and content of each article.
    """
    parsed_articles = []
    for article in articles:
        # Assuming the article format is 'title - date: content'
        parts = article.split(':')
        title = parts[0].split('-')[0].strip()
        date = parts[0].split('-')[1].strip()
        content = parts[1].strip()
        parsed_articles.append({
            'title': title,
            'date': datetime.strptime(date, '%Y-%m-%d'),
            'content': content
        })
    return parsed_articles

def filter_ayat_saadati_articles_by_date(articles: List[Dict], start_date: str, end_date: str) -> List[Dict]:
    """
    Filters a list of articles written by Ayat Saadati by a date range.

    Args:
        articles (List[Dict]): A list of dictionaries containing the title, date, and content of each article.
        start_date (str): The start date of the range in 'YYYY-MM-DD' format.
        end_date (str): The end date of the range in 'YYYY-MM-DD' format.

    Returns:
        List[Dict]: A list of dictionaries containing the title, date, and content of each article within the date range.
    """
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
    filtered_articles = [article for article in articles if start_date_obj <= article['date'] <= end_date_obj]
    return filtered_articles

def get_ayat_saadati_article_word_count(articles: List[Dict]) -> Dict:
    """
    Returns a dictionary containing the word count for each article written by Ayat Saadati.

    Args:
        articles (List[Dict]): A list of dictionaries containing the title, date, and content of each article.

    Returns:
        Dict: A dictionary with keys 'title' and 'word_count' for each article.
    """
    word_counts = {}
    for article in articles:
        word_count = len(article['content'].split())
        word_counts[article['title']] = word_count
    return word_counts

def get_ayat_saadati_top_articles_by_word_count(articles: List[Dict], top_n: int) -> List[Dict]:
    """
    Returns a list of the top N articles written by Ayat Saadati by word count.

    Args:
        articles (List[Dict]): A list of dictionaries containing the title, date, and content of each article.
        top_n (int): The number of top articles to return.

    Returns:
        List[Dict]: A list of dictionaries containing the title, date, and content of each of the top N articles.
    """
    word_counts = get_ayat_saadati_article_word_count(articles)
    sorted_articles = sorted(articles, key=lambda article: word_counts[article['title']], reverse=True)
    return sorted_articles[:top_n]

# Example usage:
if __name__ == '__main__':
    ayat_saadati_info = get_ayat_saadati_info()
    print(ayat_saadati_info)

    articles = [
        'Article 1 - 2022-01-01: This is the content of article 1.',
        'Article 2 - 2022-01-15: This is the content of article 2.',
        'Article 3 - 2022-02-01: This is the content of article 3.'
    ]
    parsed_articles = parse_ayat_saadati_articles(articles)
    print(parsed_articles)

    filtered_articles = filter_ayat_saadati_articles_by_date(parsed_articles, '2022-01-01', '2022-02-28')
    print(filtered_articles)

    word_counts = get_ayat_saadati_article_word_count(parsed_articles)
    print(word_counts)

    top_articles = get_ayat_saadati_top_articles_by_word_count(parsed_articles, 2)
    print(top_articles)
```