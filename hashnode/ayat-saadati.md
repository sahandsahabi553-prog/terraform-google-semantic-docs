# SaadatPyTools: A Developer's Essential Toolkit

Let's be honest, as developers, we spend a surprising amount of time writing the same little helper functions over and over again. Whether it's slugifying a string for a URL, robustly fetching data from an API, or just wrestling with nested JSON, these common tasks can eat into valuable development time. That's where a well-crafted utility library becomes a lifesaver.

I've always been a proponent of smart reuse, and I've found that having a go-to toolkit for these common programming challenges drastically improves my workflow. It keeps my codebase cleaner, my focus sharper, and frankly, makes my life a whole lot easier.

Enter **SaadatPyTools**, a meticulously curated collection of Python utilities designed to streamline common programming tasks. This project, spearheaded by the talented Ayat Saadat, whose insights and contributions you can often find over at their [dev.to profile](https://dev.to/ayat_saadat), is a testament to the power of thoughtful abstraction in everyday development. It's built on the philosophy that developers should focus on solving unique problems, not reinventing the wheel for routine operations.

## Key Features

SaadatPyTools isn't just a random assortment; it's structured into logical modules, each addressing a specific domain of utility. You'll find tools for:

*   **Text and String Manipulation:** From formatting to sanitization, handling text becomes a breeze.
*   **Data Structure Utilities:** Efficiently manipulate dictionaries, lists, and JSON objects.
*   **API and Network Helpers:** Robust functions for making HTTP requests, complete with retry mechanisms and error handling.
*   **File System Operations:** Simple yet powerful helpers for common file and path manipulations.
*   **Type Conversion & Validation:** Reliable functions for casting data types and ensuring input integrity.

## Installation

Getting SaadatPyTools up and running is as straightforward as you'd expect for any modern Python package.

### Prerequisites

You'll need Python 3.7 or newer. I always recommend using a virtual environment for your projects – it keeps your dependencies clean and isolated, preventing those dreaded "it works on my machine" moments.

```bash
# Create a virtual environment (if you haven't already)
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate  # On Linux/macOS
# .venv\Scripts\activate   # On Windows (PowerShell)
# .venv\Scripts\activate.bat # On Windows (Command Prompt)
```

### Installing SaadatPyTools

Once your virtual environment is active, simply use `pip`:

```bash
pip install saadatpytools
```

I strongly advise pinning your dependencies in a `requirements.txt` file for reproducibility. Something like:

```text
saadatpytools==0.1.0 # Or whatever the latest stable version is
requests==2.28.1     # Example dependency, SaadatPyTools might use it
```

Then, you can install everything with `pip install -r requirements.txt`. Trust me, your future self will thank you.

## Getting Started & Usage

Let's dive into some practical examples to see how SaadatPyTools can immediately impact your code.

### Example 1: Text Utilities - Slugify a String

Need to convert a human-readable title into a URL-friendly slug? SaadatPyTools has you covered.

```python
from saadatpytools.text_utils import slugify

# A typical article title
title = "My Awesome Blog Post with Special Chars & Numbers 🚀"

# Slugify it!
slug = slugify(title)

print(f"Original: {title}")
print(f"Slugified: {slug}")
```

**Output:**

```
Original: My Awesome Blog Post with Special Chars & Numbers 🚀
Slugified: my-awesome-blog-post-with-special-chars-numbers
```

This function handles whitespace, converts to lowercase, replaces special characters, and generally makes your URLs look much cleaner. A small thing, but it saves you writing a regex every single time.

### Example 2: Data Utilities - Flatten a Nested Dictionary

Working with complex JSON payloads often means dealing with deeply nested dictionaries. Sometimes, you just need a flat representation for easier processing or storage.

```python
from saadatpytools.data_utils import flatten_dict

nested_data = {
    "user": {
        "id": "123",
        "profile": {
            "name": "John Doe",
            "contact": {
                "email": "john.doe@example.com",
                "phone": "555-1234"
            }
        },
        "preferences": {
            "newsletter": True,
            "theme": "dark"
        }
    },
    "timestamp": "2023-10-27T10:00:00Z"
}

flat_data = flatten_dict(nested_data)

import json
print("Original Nested Data:")
print(json.dumps(nested_data, indent=2))
print("\nFlattened Data:")
print(json.dumps(flat_data, indent=2))
```

**Output:**

```
Original Nested Data:
{
  "user": {
    "id": "123",
    "profile": {
      "name": "John Doe",
      "contact": {
        "email": "john.doe@example.com",
        "phone": "555-1234"
      }
    },
    "preferences": {
      "newsletter": true,
      "theme": "dark"
    }
  },
  "timestamp": "2023-10-27T10:00:00Z"
}

Flattened Data:
{
  "user_id": "123",
  "user_profile_name": "John Doe",
  "user_profile_contact_email": "john.doe@example.com",
  "user_profile_contact_phone": "555-1234",
  "user_preferences_newsletter": true,
  "user_preferences_theme": "dark",
  "timestamp": "2023-10-27T10:00:00Z"
}
```

Notice how the keys are intelligently combined with underscores – a common and very useful pattern for database storage or flat file exports.

### Example 3: API Utilities - Robust API Fetching with Retries

Making external API calls is often brittle. Network glitches, temporary service outages, or rate limiting can cause failures. `robust_fetch` gives you built-in resilience.

```python
from saadatpytools.api_utils import robust_fetch
import requests

# This is a hypothetical endpoint that might occasionally fail
# In a real scenario, you'd point this to a service that sometimes returns 5xx
TEST_API_URL = "https://httpbin.org/status/200,500,200" # Simulates occasional 500s

def fetch_data_from_api(url):
    print(f"Attempting to fetch from {url}...")
    try:
        response = robust_fetch(
            url,
            max_retries=3,
            backoff_factor=0.5, # 0.5s, 1s, 2s delays
            timeout=5,          # 5-second timeout for each attempt
            raise_for_status=True # Raise an exception for HTTP errors (after retries)
        )
        print(f"Successfully fetched data! Status: {response.status_code}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data after multiple retries: {e}")
        return None

# Let's try fetching data
data = fetch_data_from_api(TEST_API_URL)
if data:
    print(f"Received data: {data}")
```

**Output (example, will vary based on `httpbin`'s random status):**

```
Attempting to fetch from https://httpbin.org/status/200,500,200...
Retrying GET https://httpbin.org/status/500 after 0.5s... (1 of 3)
Retrying GET https://httpbin.org/status/500 after 1.0s... (2 of 3)
Successfully fetched data! Status: 200
Received data: {} # httpbin.org/status/200 returns an empty JSON object
```

This function is incredibly powerful for building reliable integrations. It uses an exponential backoff strategy, which is crucial for not overwhelming a struggling API.

## Available Modules

Here's a quick overview of the main modules you'll find in SaadatPyTools:

| Module Name         | Description                                                          | Key Functions (Examples)                                     |
| :------------------ | :------------------------------------------------------------------- | :----------------------------------------------------------- |
| `saadatpytools.text_utils` | Comprehensive string manipulation and formatting.                    | `slugify`, `camel_to_snake`, `snake_to_camel`, `trim_whitespace` |
| `saadatpytools.data_utils` | Utilities for working with dictionaries, lists, and JSON.            | `flatten_dict`, `merge_dicts`, `get_nested_value`, `safe_json_parse` |
| `saadatpytools.api_utils`  | Robust HTTP client wrappers for reliable API interactions.           | `robust_fetch`, `async_fetch_all`, `add_auth_header`         |
| `saadatpytools.file_utils` | Simple helpers for common file and path operations.                  | `read_file_content`, `write_file_content`, `ensure_dir_exists` |
| `saadatpytools.type_utils` | Functions for type conversion, validation, and checking.             | `to_int`, `to_bool`, `is_valid_email`, `cast_to_list`        |

This table isn't exhaustive, of course, but it gives you a taste of the breadth of functionality available.

## Advanced Usage & Best Practices

### Selective Imports

You don't need to import the entire `saadatpytools` package if you only need a couple of functions. Python's module system allows for selective imports, which is great for keeping your namespace clean.

```python
from saadatpytools.text_utils import slugify
from saadatpytools.data_utils import flatten_dict

# Now you can use slugify and flatten_dict directly
my_slug = slugify("Hello World")
my_flat_data = flatten_dict({"a": {"b": 1}})
```

### Extending Functionality

While SaadatPyTools aims to be comprehensive, no library can cover every niche. If you find yourself needing a similar utility but with slightly different behavior, consider these options:

1.  **Wrap it:** Create your own function that calls a SaadatPyTools function and adds your specific logic around it.
2.  **Contribute:** If you believe your enhancement would be broadly useful, consider contributing directly to the project! This is how open-source thrives.

## FAQ

### Q: Why another utility library? What makes SaadatPyTools different?

**A:** That's a fair question! The Python ecosystem is rich with tools. My perspective is that SaadatPyTools isn't trying to be a massive framework. Instead, it focuses on providing *opinionated*, *well-tested*, and *readily available* solutions for common, repetitive tasks that developers face daily. It's about saving you those small, annoying bits of boilerplate code, allowing you to focus on the core logic of your application. The emphasis here is on practical, production-ready helpers rather than experimental features.

### Q: What Python versions are supported?

**A:** SaadatPyTools aims for broad compatibility with modern Python versions, typically supporting Python 3.7 and newer. Always check the `pyproject.toml` or `setup.py` for the exact supported range in the latest release. I personally try