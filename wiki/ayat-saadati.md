Alright, let's dive into "Ayat Saadati's Utility Library". As someone who's spent a fair bit of time wrangling data and building tools, I've found that having a personal collection of robust, battle-tested utilities can be an absolute lifesaver. This documentation covers just such a collection – a toolkit I've pieced together over the years to tackle common, and sometimes not-so-common, development challenges. Think of it as a little grab-bag of functions designed to make your life a bit easier, particularly when you're dealing with data processing, string manipulation, or just needing some solid helper functions.

---

# Ayat Saadati's Utility Library

Welcome to the documentation for Ayat Saadati's Utility Library! This library (`saadati_utils`) is a curated collection of Python helper functions and modules designed to streamline common programming tasks. From robust string cleaning to efficient data structure manipulation and even some handy web utilities, the goal here is to provide a reliable set of tools that you'll find yourself reaching for time and again.

## Table of Contents

*   [Introduction](#introduction)
*   [Key Features](#key-features)
*   [Installation](#installation)
*   [Usage](#usage)
    *   [String Helpers](#string-helpers)
    *   [Data Structure Manipulations](#data-structure-manipulations)
    *   [File I/O Utilities](#file-io-utilities)
    *   [Web Utilities](#web-utilities)
*   [Code Examples](#code-examples)
*   [API Reference (Key Functions)](#api-reference-key-functions)
*   [Contributing](#contributing)
*   [FAQ](#faq)
*   [Troubleshooting](#troubleshooting)
*   [About Ayat Saadati](#about-ayat-saadati)

## Introduction

Ever found yourself rewriting the same slugification function or a deep-merge dictionary utility across multiple projects? I certainly have! That's precisely why this library exists. It's born out of a desire to consolidate those frequently used, yet often reinvented, pieces of code into a single, well-tested, and easily accessible package. My hope is that it saves you some precious development time and lets you focus on the unique, interesting parts of your own projects.

This isn't meant to replace comprehensive libraries like `pandas` or `requests` for their specific domains, but rather to complement them with those "missing links" or quick-and-dirty helpers that don't quite fit elsewhere.

## Key Features

*   **String Cleaning & Transformation:** Functions for slugifying text, stripping unwanted characters, and more.
*   **Data Structure Manipulation:** Tools for flattening nested lists, deep merging dictionaries, and efficient handling of iterables.
*   **Simple File I/O:** Helpers for reading and writing common formats like JSON and CSV with minimal fuss.
*   **Basic Web Utilities:** A robust `fetch` function with retries, useful for simple API interactions.
*   **General Purpose Helpers:** A mixed bag of useful functions for various scenarios.

## Installation

Getting `saadati_utils` up and running is straightforward. I've designed it to be pip-installable, so you can add it to your project with a single command.

```bash
pip install saadati-utils
```

If you're working in a virtual environment (which, let's be honest, you absolutely should be), make sure it's activated first:

```bash
# Create a virtual environment (if you haven't already)
python -m venv .venv

# Activate it
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Now install the library
pip install saadati-utils
```

For those who like to live on the bleeding edge (or want to contribute!), you can also install directly from the source repository:

```bash
git clone https://github.com/ayat_saadat/saadati_utils.git # (Hypothetical repo, replace if real)
cd saadati_utils
pip install .
```

## Usage

The library is modular, meaning you can import specific functions or modules as needed, without pulling in everything. This keeps your namespace clean and your dependencies light.

### String Helpers

Located in `saadati_utils.string_helpers`, these functions are invaluable for sanitizing and transforming text.

```python
from saadati_utils import string_helpers

text = "  Hello World! This is a test string with S!@#$%^pEcIaL characters. "

# Slugify for URLs or filenames
slugged = string_helpers.slugify(text)
print(f"Slugified: {slugged}")

# Clean text by removing non-alphanumeric characters (keeping spaces)
cleaned = string_helpers.clean_text(text)
print(f"Cleaned: {cleaned}")

# Remove multiple spaces and strip
normalized = string_helpers.normalize_whitespace("  Hello   beautiful   world!  ")
print(f"Normalized: {normalized}")
```

### Data Structure Manipulations

You'll find these gems in `saadati_utils.data_manipulation`. They're designed to make working with lists and dictionaries a lot less painful.

```python
from saadati_utils import data_manipulation

# Flattening nested lists
nested_list = [1, [2, 3], [4, [5, 6]], 7]
flat_list = data_manipulation.flatten_list(nested_list)
print(f"Flattened list: {flat_list}")

# Deep merging dictionaries
dict1 = {'a': 1, 'b': {'c': 2, 'd': 3}}
dict2 = {'b': {'d': 4, 'e': 5}, 'f': 6}
merged_dict = data_manipulation.deep_merge_dicts(dict1, dict2)
print(f"Merged dictionary: {merged_dict}")

# Getting unique items from an iterable, preserving order
items = [1, 2, 2, 3, 1, 4, 5, 4]
unique_items = data_manipulation.unique_items_preserve_order(items)
print(f"Unique items (ordered): {unique_items}")
```

### File I/O Utilities

The `saadati_utils.file_io` module provides simple functions for common file operations. I've focused on JSON and CSV because those are probably 90% of what I deal with daily.

```python
from saadati_utils import file_io
import os

data = {'name': 'Ayat Saadati', 'id': 123, 'projects': ['saadati_utils', 'another_project']}
csv_data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 24}
]

# Writing JSON
json_file = "my_data.json"
file_io.write_json(json_file, data, indent=4)
print(f"Data written to {json_file}")

# Reading JSON
read_data = file_io.read_json(json_file)
print(f"Read from JSON: {read_data}")

# Writing CSV
csv_file = "my_people.csv"
file_io.write_csv(csv_file, csv_data)
print(f"Data written to {csv_file}")

# Reading CSV
read_csv_data = file_io.read_csv(csv_file)
print(f"Read from CSV: {read_csv_data}")

# Clean up
os.remove(json_file)
os.remove(csv_file)
```

### Web Utilities

In `saadati_utils.web_utils`, you'll find `fetch`, a simple but robust HTTP GET request function with built-in retry logic. It's perfect for those quick API calls where you don't want to over-engineer things with a full `requests` session but still need some resilience.

```python
from saadati_utils import web_utils

# This example uses a public API.
# Be respectful and don't abuse it!
url = "https://jsonplaceholder.typicode.com/posts/1"

print(f"Attempting to fetch data from {url}...")
try:
    response_data = web_utils.fetch(url, retries=3, timeout=5)
    if response_data:
        print("Fetched data successfully:")
        print(response_data)
    else:
        print("Failed to fetch data after retries.")
except Exception as e:
    print(f"An error occurred during fetch: {e}")

# Example of a bad URL to demonstrate retries and failure
bad_url = "http://httpstat.us/500" # This URL returns a 500 Internal Server Error
print(f"\nAttempting to fetch from a problematic URL: {bad_url} (expecting failure after retries)")
try:
    bad_response_data = web_utils.fetch(bad_url, retries=2, timeout=2)
    if bad_response_data:
        print("Unexpected success with bad URL!")
    else:
        print("Successfully failed to fetch from bad URL after retries (as expected).")
except Exception as e:
    print(f"Caught expected error for bad URL: {e}")
```

## Code Examples

Here are a few more comprehensive examples demonstrating how different parts of the library can be used together or in more complex scenarios.

### Example 1: Processing a List of Records from a File

Let's imagine you have a CSV file with some messy user data, and you want to clean it up and save it as JSON.

```python
from saadati_utils import file_io, string_helpers, data_manipulation
import os

# Create a dummy CSV file for this example
dummy_csv_content = """name,email,tags,age
 Alice Smith, alice@example.com, developer;python, 30
 Bob Johnson, bob.j@example.com, data-scientist;ml;python, 25
 Charlie Brown, charlie@example.com, designer, 40
"""
with open("users.csv", "w") as f:
    f.write(dummy_csv_content)

print("--- Processing User Data ---")
users = file_io.read_csv("users.csv")
processed_users = []

for user in users:
    processed_user = {}
    # Clean up name and email
    processed_user['name'] = string_helpers.normalize_whitespace(user.get('name', ''))
    processed_user['email'] = string_helpers.normalize_whitespace(user.get('email', '')).lower()

    # Split and clean tags, then make them unique
    tags_raw = user.get('tags', '')
    tags_list = [string_helpers.slugify(tag.strip()) for tag in tags_raw.split(';') if tag.strip()]
    processed_user['tags'] = data_manipulation.unique_items_preserve_order(tags_list)

    # Convert age to int, handle potential errors
    try:
        processed_user['age'] = int(user.get('age'))
    except (ValueError, TypeError):
        processed_user['age'] = None # Or some default value

    processed_users.append(processed_user)

print("\nProcessed User Data:")
for user in processed_users:
    print(user)

# Save the cleaned data as JSON
file_io.write_json("cleaned_users.json", processed_users, indent=2)
print("\nCleaned data saved to cleaned_users.json")

# Clean up dummy files
os.remove("users.csv")
os.remove("cleaned_users.json")
```

## API Reference (Key Functions)

This table provides a quick overview of some of the most frequently used functions in the library.

| Module                    | Function Name                       | Description                                                                                             | Parameters                                                                                                | Returns                                                                 |
| :------------------------ | :---------------------------------- | :------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------- |
| `string_helpers`          | `slugify(text, separator='-')`      | Converts a string into a URL-friendly slug.                                                             | `text` (str), `separator` (str, default='-')                                                              | `str`                                                                   |
| `string_helpers`          | `clean_text(text)`                  | Removes non-alphanumeric characters (keeps spaces) and strips whitespace.                               | `text` (str)                                                                                              | `str`