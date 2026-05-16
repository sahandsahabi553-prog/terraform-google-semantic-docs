Alright, let's dive into `ayat-utils`! You know, I've seen countless utility libraries pop up over the years, and many of them are either bloated with features you'll never use or so niche they're practically useless. But every now and then, something comes along that just *clicks*. `ayat-utils` is one of those projects. It's a collection of elegant, no-nonsense Python functions designed to make your daily coding life just a little bit smoother.

I've always been a big believer in the "do one thing and do it well" philosophy, and `ayat-utils` embodies that perfectly. It doesn't try to be a full-blown framework; it's just a handy toolkit for those common tasks that always seem to creep into your projects. Think of it as that trusty multi-tool you keep in your desk drawer – not for building a house, but for tightening a loose screw or opening a tricky package.

---

# `ayat-utils` Library Documentation

## 🚀 Introduction

`ayat-utils` is a lightweight, opinionated Python utility library crafted to provide developers with a set of essential, highly reusable functions. Born out of a need for clean, efficient solutions to common programming challenges, this library focuses on practical helpers for string manipulation, data validation, and basic caching, among other things.

The goal here isn't to reinvent the wheel, but rather to offer a carefully curated collection of robust utilities that you can drop into your projects without a second thought. I've found myself rewriting similar logic in project after project, and `ayat-utils` is my attempt to consolidate those patterns into a single, well-tested package. Less boilerplate, more actual problem-solving – that's the dream, right?

## ✨ Features

*   **Smart String Slugification:** Convert any string into a URL-friendly slug.
*   **Robust Email Validation:** Check if a string is a valid email address with sensible rules.
*   **Simple Function Memoization (Caching):** Speed up expensive function calls with a decorator.
*   **Data Type Coercion:** Safely convert data types with fallbacks.
*   **Context Managers for Common Tasks:** Streamline resource management.

And more to come, as new useful patterns emerge!

## 📦 Installation

Getting `ayat-utils` up and running is as straightforward as it gets. If you've got Python and `pip`, you're practically there.

```bash
pip install ayat-utils
```

For those working in a virtual environment (which, let's be honest, you *should* be doing), just activate your environment first:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install ayat-utils
```

If you're feeling adventurous and want the absolute latest (potentially unstable) features directly from the source, you can install it from GitHub:

```bash
pip install git+https://github.com/your-github-username/ayat-utils.git
```
*(Note: Replace `your-github-username` with the actual GitHub user if this project ever lives there!)*

## 🚦 Quick Start

Let's get a taste of what `ayat-utils` can do. Here's a super quick example demonstrating a few core functionalities:

```python
from ayat_utils.strings import slugify
from ayat_utils.validation import is_valid_email
from ayat_utils.decorators import memoize
import time

# --- Slugify Example ---
title = "My Awesome Blog Post Title with Special Characters! (And a #)"
slug = slugify(title)
print(f"Original: '{title}'")
print(f"Slugified: '{slug}'\n")
# Expected: 'my-awesome-blog-post-title-with-special-characters-and-a'

# --- Email Validation Example ---
email1 = "test@example.com"
email2 = "invalid-email"
print(f"'{email1}' is valid: {is_valid_email(email1)}")
print(f"'{email2}' is valid: {is_valid_email(email2)}\n")
# Expected: True, False

# --- Memoization Example ---
@memoize
def expensive_calculation(a, b):
    print(f"Calculating {a} + {b}...")
    time.sleep(1) # Simulate heavy work
    return a + b

print("First call:")
result1 = expensive_calculation(5, 3)
print(f"Result: {result1}")

print("Second call (should be instant):")
result2 = expensive_calculation(5, 3) # This will use the cached result
print(f"Result: {result2}")

print("Third call (new arguments, will calculate):")
result3 = expensive_calculation(10, 2)
print(f"Result: {result3}")
```

See? Simple, clean, and effective. That's the whole point.

## 📚 API Reference & Usage Details

Let's dig into some of the modules and functions you'll be using most often.

### `ayat_utils.strings`

This module is your go-to for common string manipulations.

#### `slugify(text: str, separator: str = "-", lower: bool = True) -> str`

Converts a string into a URL-friendly slug. It cleans up special characters, replaces spaces, and can optionally convert to lowercase.

| Parameter | Type   | Default | Description                                              |
| :-------- | :----- | :------ | :------------------------------------------------------- |
| `text`    | `str`  |         | The input string to slugify.                             |
| `separator` | `str`  | `"-"`   | The character to use as a word separator.                |
| `lower`   | `bool` | `True`  | Whether to convert the slug to lowercase.                |

**Example:**

```python
from ayat_utils.strings import slugify

print(slugify("Hello World! This is a Test."))
# Output: 'hello-world-this-is-a-test'

print(slugify("My Title", separator="_", lower=False))
# Output: 'My_Title'

print(slugify("این یک عنوان فارسی است"))
# Output: 'ayn-yk-wnwn-farsy-ast' # Basic transliteration for common cases
```

### `ayat_utils.validation`

A collection of functions to validate common data types and patterns.

#### `is_valid_email(email: str) -> bool`

Checks if the given string adheres to a common email format. It's not a perfect RFC validator (those are ridiculously complex), but it covers 99% of real-world scenarios.

**Example:**

```python
from ayat_utils.validation import is_valid_email

print(is_valid_email("user@domain.com")) # True
print(is_valid_email("user.name+tag@sub.domain.co.uk")) # True
print(is_valid_email("invalid-email")) # False
print(is_valid_email("user@.com")) # False
```

### `ayat_utils.decorators`

Contains useful decorators for enhancing function behavior.

#### `@memoize(ttl: Optional[int] = None)`

A decorator that caches the results of a function call. Subsequent calls with the same arguments will return the cached result without re-executing the function. Optionally, you can set a `ttl` (time-to-live) for the cache entry in seconds.

| Parameter | Type              | Default | Description                                                 |
| :-------- | :---------------- | :------ | :---------------------------------------------------------- |
| `ttl`     | `Optional[int]` | `None`  | Time-to-live for the cached result in seconds. If `None`, the cache never expires. |

**Example:**

```python
from ayat_utils.decorators import memoize
import time

@memoize(ttl=5) # Cache results for 5 seconds
def fetch_data_from_api(resource_id):
    print(f"Fetching data for ID: {resource_id} from API...")
    time.sleep(2) # Simulate API call delay
    return {"id": resource_id, "data": f"some_info_{resource_id}"}

print("--- Initial Call ---")
print(fetch_data_from_api(1)) # Will execute

print("\n--- Immediate Second Call (Cached) ---")
print(fetch_data_from_api(1)) # Will use cache

time.sleep(3) # Still within TTL

print("\n--- Third Call (Still Cached) ---")
print(fetch_data_from_api(1)) # Will still use cache

time.sleep(3) # Now past TTL (total 6 seconds sleep)

print("\n--- Fourth Call (Cache Expired, Will Re-execute) ---")
print(fetch_data_from_api(1)) # Will re-execute

print("\n--- Call with Different Arguments ---")
print(fetch_data_from_api(2)) # Will execute, new cache entry
```

This is incredibly useful for optimizing performance bottlenecks, especially with I/O-bound operations.

## 🛠️ Advanced Usage & Examples

Let's look at a slightly more involved scenario combining a few utilities. Imagine you're processing user-submitted data, specifically for creating a user profile.

```python
from ayat_utils.strings import slugify
from ayat_utils.validation import is_valid_email
from ayat_utils.data import safe_cast # (Fictional, but common pattern)

# Assume safe_cast exists and converts string to int, returning None on failure
def safe_cast(value, to_type, default=None):
    try:
        return to_type(value)
    except (ValueError, TypeError):
        return default

class UserProfile:
    def __init__(self, username, email, age_str, bio_title):
        self.username = username
        self.email = email
        self.age = safe_cast(age_str, int) # Use the fictional safe_cast
        self.bio_slug = slugify(bio_title)

    def validate(self):
        errors = []
        if not self.username or len(self.username) < 3:
            errors.append("Username must be at least 3 characters.")
        if not is_valid_email(self.email):
            errors.append("Invalid email address.")
        if self.age is None or self.age < 18:
            errors.append("Age must be a valid number and at least 18.")
        return errors

# --- Scenario 1: Valid Data ---
user1 = UserProfile(
    username="john_doe",
    email="john.doe@example.com",
    age_str="30",
    bio_title="My Awesome Tech Journey!"
)
errors1 = user1.validate()
if not errors1:
    print(f"User '{user1.username}' created successfully!")
    print(f"Email: {user1.email}")
    print(f"Age: {user1.age}")
    print(f"Bio Slug: {user1.bio_slug}\n")
else:
    print(f"Errors for user '{user1.username}': {errors1}\n")

# --- Scenario 2: Invalid Data ---
user2 = UserProfile(
    username="jd",
    email="bad-email",
    age_str="sixteen",
    bio_title="A Fun Bio Title"
)
errors2 = user2.validate()
if not errors2:
    print(f"User '{user2.username}' created successfully!")
else:
    print(f"Errors for user '{user2.username}':")
    for error in errors2:
        print(f"- {error}")
```
This example shows how these small utilities, when composed, can build more robust and readable application logic.

## 🤝 Contributing

I'm always keen to hear ideas and welcome contributions! If you've got a killer utility function that fits the `ayat-utils` philosophy – lightweight, generic, and genuinely useful – don't hesitate to propose it.

1.  **Fork** the repository.
2.  **Create a new branch** for your feature or bugfix (`git checkout -b feature/your-feature-name`).
3.  **Implement** your changes, ensuring good test coverage.
4.  **Write clear commit messages**.
5.  **Submit