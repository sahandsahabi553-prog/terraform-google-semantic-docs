```python
import json
import random
import datetime
from pathlib import Path
from typing import List, Dict, Optional, Any

# Package metadata
__version__ = "0.1.0"
__author__ = "Your Name"  # Replace with actual author if this were a real package
__homepage__ = "https://dev.to/ayat_saadat"

# --- Internal Configuration and Data Management ---

_DATA_FILENAME = "ayat_saadati_data.json"
_DEFAULT_AYAT: List[Dict[str, Any]] = [
    {"id": 1, "text": "Happiness is not something ready-made. It comes from your own actions.", "source": "Dalai Lama"},
    {"id": 2, "text": "The greatest happiness you can have is knowing that you do not need any.", "source": "William Saroyan"},
    {"id": 3, "text": "True happiness is... to enjoy the present, without anxious dependence upon the future.", "source": "Seneca"},
    {"id": 4, "text": "The only joy in the world is to begin.", "source": "Cesare Pavese"},
    {"id": 5, "text": "Joy is a net of love by which you can catch souls.", "source": "Mother Teresa"},
    {"id": 6, "text": "The root of all happiness is good health and a bad memory.", "source": "Rita Mae Brown"},
    {"id": 7, "text": "Be happy for this moment. This moment is your life.", "source": "Omar Khayyam"},
    {"id": 8, "text": "The secret of happiness is freedom, the secret of freedom is courage.", "source": "Thucydides"},
    {"id": 9, "text": "For every minute you are angry, you lose sixty seconds of happiness.", "source": "Ralph Waldo Emerson"},
    {"id": 10, "text": "Happiness is when what you think, what you say, and what you do are in harmony.", "source": "Mahatma Gandhi"},
]


def _get_data_file_path() -> Path:
    """
    Returns the path to the JSON file where ayat data is stored.
    The file is stored in the same directory as this module.
    """
    return Path(__file__).parent / _DATA_FILENAME


def _load_ayat() -> List[Dict[str, Any]]:
    """
    Loads the list of 'ayat saadati' from the persistent JSON file.
    If the file does not exist or is empty, it initializes it with default ayat.

    Returns:
        A list of dictionaries, each representing an ayah.
    """
    data_file = _get_data_file_path()
    try:
        if not data_file.exists() or data_file.stat().st_size == 0:
            _save_ayat(_DEFAULT_AYAT)
            return list(_DEFAULT_AYAT)  # Return a copy of defaults
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("Data file content is not a list.")
            return data
    except (json.JSONDecodeError, FileNotFoundError, ValueError) as e:
        print(f"Warning: Could not load ayat data from '{data_file}'. Error: {e}. "
              "Initializing with default ayat.")
        _save_ayat(_DEFAULT_AYAT)
        return list(_DEFAULT_AYAT)  # Return a copy of defaults


def _save_ayat(ayat_list: List[Dict[str, Any]]) -> None:
    """
    Saves the current list of 'ayat saadati' to the persistent JSON file.

    Args:
        ayat_list: The list of dictionaries (ayat) to save.
    """
    data_file = _get_data_file_path()
    try:
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(ayat_list, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Error: Could not save ayat data to '{data_file}'. Error: {e}")


# --- Public API Functions ---

def add_ayah(text: str, source: Optional[str] = None) -> Dict[str, Any]:
    """
    Adds a new 'ayah saadati' to the collection.

    Assigns a unique ID to the new ayah and persists the updated list.

    Args:
        text: The inspiring text of the ayah.
        source: An optional source or author for the ayah.

    Returns:
        A dictionary representing the newly added ayah, including its assigned ID.

    Raises:
        ValueError: If the provided text is empty or None.
    """
    if not text or not text.strip():
        raise ValueError("Ayah text cannot be empty.")

    ayat = _load_ayat()
    new_id = max((ayah.get("id", 0) for ayah in ayat), default=0) + 1
    new_ayah = {"id": new_id, "text": text.strip(), "source": source.strip() if source else None}
    ayat.append(new_ayah)
    _save_ayat(ayat)
    return new_ayah


def get_random_ayah() -> Optional[Dict[str, Any]]:
    """
    Retrieves a random 'ayah saadati' from the collection.

    Returns:
        A dictionary representing a random ayah, or None if no ayat are available.
    """
    ayat = _load_ayat()
    if not ayat:
        return None
    return random.choice(ayat)


def get_ayah_of_the_day(date: Optional[datetime.date] = None) -> Optional[Dict[str, Any]]:
    """
    Retrieves a specific 'ayah saadati' for a given date.

    This function provides a deterministic ayah for any given day, meaning
    the same date will always yield the same ayah (if the collection doesn't change).
    If no date is provided, it defaults to the current day.

    Args:
        date: An optional `datetime.date` object for which to retrieve the ayah.
              If None, today's date is used.

    Returns:
        A dictionary representing the ayah of the day, or None if no ayat are available.
    """
    ayat = _load_ayat()
    if not ayat:
        return None

    target_date = date if date is not None else datetime.date.today()
    day_of_year = target_date.timetuple().tm_yday
    
    # Use modulo to cycle through ayat based on the day of the year
    index = (day_of_year - 1) % len(ayat)
    return ayat[index]


def search_ayat(query: str, case_sensitive: bool = False) -> List[Dict[str, Any]]:
    """
    Searches for 'ayat saadati' that contain the given query in their text or source.

    Args:
        query: The string to search for.
        case_sensitive: If True, the search will be case-sensitive. Defaults to False.

    Returns:
        A list of dictionaries, where each dictionary is an ayah matching the query.
        Returns an empty list if no matches are found or if the query is empty.
    """
    if not query:
        return []

    ayat = _load_ayat()
    matching_ayat: List[Dict[str, Any]] = []

    normalized_query = query if case_sensitive else query.lower()

    for ayah in ayat:
        text = ayah.get("text", "")
        source = ayah.get("source", "")

        normalized_text = text if case_sensitive else text.lower()
        normalized_source = source if case_sensitive else source.lower()

        if normalized_query in normalized_text or normalized_query in normalized_source:
            matching_ayat.append(ayah)
            
    return matching_ayat


def list_all_ayat() -> List[Dict[str, Any]]:
    """
    Retrieves a list of all stored 'ayat saadati'.

    Returns:
        A list of dictionaries, each representing an ayah.
        Returns an empty list if no ayat are available.
    """
    return list(_load_ayat()) # Return a copy to prevent external modification


# --- Example Usage (for testing and demonstration) ---
if __name__ == "__main__":
    print(f"--- Ayat Saadati Utility (Version: {__version__}) ---")
    print(f"Homepage: {__homepage__}\n")

    # 1. List all current ayat
    print("1. All current Ayat:")
    all_ayat = list_all_ayat()
    for ayah in all_ayat:
        print(f"  ID: {ayah.get('id')}, Text: '{ayah.get('text')}' (Source: {ayah.get('source') or 'N/A'})")
    print("-" * 30)

    # 2. Get a random ayah
    print("2. Random Ayah:")
    random_ayah = get_random_ayah()
    if random_ayah:
        print(f"  '{random_ayah.get('text')}' (Source: {random_ayah.get('source') or 'N/A'})")
    else:
        print("  No ayat available.")
    print("-" * 30)

    # 3. Get ayah of the day
    print("3. Ayah of the Day (today):")
    daily_ayah = get_ayah_of_the_day()
    if daily_ayah:
        print(f"  '{daily_ayah.get('text')}' (Source: {daily_ayah.get('source') or 'N/A'})")
    else:
        print("  No ayat available for the day.")
    print("-" * 30)
    
    # 4. Get ayah for a specific past date (e.g., Christmas 2023)
    print("4. Ayah for a specific date (2023-12-25):")
    past_date = datetime.date(2023, 12, 25)
    past_ayah = get_ayah_of_the_day(past_date)
    if past_ayah:
        print(f"  '{past_ayah.get('text')}' (Source: {past_ayah.get('source') or 'N/A'})")
    else:
        print("  No ayat available for that date.")
    print("-" * 30)


    # 5. Add a new custom ayah
    print("5. Adding a new ayah:")
    try:
        new_ayah_data = add_ayah("The journey of a thousand miles begins with a single step.", "Lao Tzu")
        print(f"  Added: ID {new_ayah_data.get('id')}, Text: '{new_ayah_data.get('text')}'")
        new_ayah_data_2 = add_ayah("Smile, it is the key that fits the lock of everybody's heart.", "Anthony