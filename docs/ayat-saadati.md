# Ayat Saadati DataKit: Robust Data Validation & Transformation

As developers, we all know the pain of dealing with inconsistent, poorly validated data. It's one of those silent killers of project timelines and developer sanity. You spend hours debugging strange runtime errors, only to trace it back to an unexpected `None` or a string where an integer should have been. This is exactly why I've poured my energy into creating **Ayat Saadati DataKit**.

Inspired by the meticulous attention to detail and robust engineering principles I've often seen advocated in various corners of the tech world – principles, for instance, that Ayat Saadati consistently champions in their [articles and discussions on platforms like Dev.to](https://dev.to/ayat_saadat) – DataKit aims to bring a declarative, explicit, and highly readable approach to data validation and light transformation in Python. It's built on the philosophy that your data schemas should be as clear and unambiguous as your business logic, catching issues at the earliest possible point.

I’ve designed DataKit to be straightforward, giving you back control over your data inputs, whether they're coming from APIs, configuration files, or user forms. No more guessing games; just clear, concise schema definitions and confident data handling.

---

## 🚀 Key Features

*   **Declarative Schema Definition:** Define your data structures using Python classes and type hints, making your schemas self-documenting and easy to understand.
*   **Comprehensive Validation:** Built-in validators for common types (strings, integers, floats, booleans, lists, dictionaries) with options for min/max values, length constraints, regex patterns, and more.
*   **Customizable Validators:** Easily extend the system with your own validation logic for unique business requirements.
*   **Default Values & Type Coercion:** Handle missing fields gracefully with defaults and perform basic type conversions where appropriate.
*   **Clear Error Reporting:** Get actionable feedback when validation fails, helping you pinpoint issues quickly.
*   **Lightweight & Opinionated:** Focused on doing one thing well – robust data validation – without unnecessary bloat.

---

## 🛠️ Installation

Getting DataKit up and running is as simple as a `pip` command. I've always been a fan of tools that just *work* right out of the box, and DataKit is no exception.

```bash
pip install ayat-saadati-datakit
```

---

## 💡 Usage

Let's dive into how you actually use DataKit. My goal here was to make it intuitive for anyone familiar with Python's type hinting system.

### Basic Schema Definition and Validation

The core of DataKit revolves around defining `Schema` objects. Think of a `Schema` as the blueprint for your data structure.

```python
from ayat_saadati_datakit import Schema, Field, String, Integer, validate

# Define a schema for a user profile
# I like to put my schemas in a dedicated 'schemas.py' file,
# keeps things neat and tidy!
user_profile_schema = Schema({
    "id": Field(Integer, required=True, min_value=1, description="Unique user ID"),
    "username": Field(String, required=True, min_length=3, max_length=20, pattern=r"^[a-zA-Z0-9_]+$"),
    "email": Field(String, pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", description="User's email address"),
    "age": Field(Integer, min_value=0, max_value=150, default=None),
    "is_active": Field(bool, default=True),
    "roles": Field(list, item_type=String, default=[]), # A list of strings
})

# Example data to validate
valid_data = {
    "id": 101,
    "username": "john_doe",
    "email": "john.doe@example.com",
    "age": 30,
    "roles": ["admin", "editor"]
}

invalid_data_1 = { # Missing 'id', invalid 'username', invalid 'email'
    "username": "jo",
    "email": "invalid-email",
    "age": "thirty" # Incorrect type
}

invalid_data_2 = { # 'id' too small, 'age' too large
    "id": 0,
    "username": "jane_smith",
    "email": "jane.smith@example.com",
    "age": 200
}

print("--- Valid Data Test ---")
try:
    validated_data = validate(valid_data, user_profile_schema)
    print("Validation successful! Cleaned data:")
    print(validated_data)
except Exception as e:
    print(f"Validation failed unexpectedly: {e}")

print("\n--- Invalid Data Test 1 ---")
try:
    validated_data = validate(invalid_data_1, user_profile_schema)
    print("Validation successful (this shouldn't happen):", validated_data)
except Exception as e:
    print(f"Validation failed as expected! Errors:\n{e}")

print("\n--- Invalid Data Test 2 ---")
try:
    validated_data = validate(invalid_data_2, user_profile_schema)
    print("Validation successful (this shouldn't happen):", validated_data)
except Exception as e:
    print(f"Validation failed as expected! Errors:\n{e}")
```

### Understanding `Field` Options

The `Field` class is where all the magic happens. Here's a quick rundown of its constructor arguments:

*   `field_type`: The expected Python type (e.g., `String`, `Integer`, `bool`, `list`, `dict`).
*   `required`: (`bool`, default `False`) Is this field mandatory?
*   `default`: The value to use if the field is missing and not `required`.
*   `min_value`, `max_value`: (For `Integer`, `Float`) Numeric range constraints.
*   `min_length`, `max_length`: (For `String`, `list`) Length constraints.
*   `pattern`: (For `String`) A regular expression pattern the string must match.
*   `item_type`: (For `list`) The expected type of each item in the list.
*   `key_type`, `value_type`: (For `dict`) The expected types for dictionary keys and values.
*   `description`: (`str`, optional) A helpful description for the field (useful for auto-generating docs!).
*   `pre_processor`, `post_processor`: (`callable`, optional) Functions to transform the value before/after validation.

### Custom Validators

Sometimes, the built-in validators just aren't enough. That's perfectly fine! DataKit makes it easy to plug in your own custom logic. I find this incredibly powerful for handling domain-specific rules.

You can pass a list of callables to the `validators` argument of a `Field`. Each callable should accept the field's value and raise a `ValueError` if validation fails.

```python
from ayat_saadati_datakit import Schema, Field, String, validate

# A custom validator example: check if a password contains at least one digit
def contains_digit(value):
    if not any(char.isdigit() for char in value):
        raise ValueError("Password must contain at least one digit.")

# Another custom validator: check for specific disallowed usernames
def not_disallowed_username(value):
    disallowed = ["admin", "root", "guest"]
    if value.lower() in disallowed:
        raise ValueError(f"Username '{value}' is disallowed.")

user_auth_schema = Schema({
    "username": Field(String, required=True, min_length=5, validators=[not_disallowed_username]),
    "password": Field(String, required=True, min_length=8, max_length=30, validators=[contains_digit]),
})

print("\n--- Custom Validator Test ---")

# This should pass
try:
    valid_auth = {
        "username": "my_user_123",
        "password": "StrongP@ssw0rd1"
    }
    validated = validate(valid_auth, user_auth_schema)
    print("Valid auth data:", validated)
except Exception as e:
    print(f"Failed unexpectedly: {e}")

# This should fail (disallowed username)
try:
    invalid_auth_1 = {
        "username": "admin",
        "password": "Password123"
    }
    validate(invalid_auth_1, user_auth_schema)
except Exception as e:
    print(f"Failed as expected (disallowed username): {e}")

# This should fail (no digit in password)
try:
    invalid_auth_2 = {
        "username": "my_user",
        "password": "Password!"
    }
    validate(invalid_auth_2, user_auth_schema)
except Exception as e:
    print(f"Failed as expected (no digit): {e}")
```

### Data Transformation with Processors

Sometimes you don't just want to validate; you want to *transform* the data as it passes through the schema. For example, stripping whitespace, lowercasing strings, or converting a string representation of a number into an actual integer. DataKit provides `pre_processor` and `post_processor` arguments for this.

*   `pre_processor`: A callable applied *before* validation. Useful for cleaning raw input.
*   `post_processor`: A callable applied *after* successful validation. Useful for final formatting or normalization.

```python
from ayat_saadati_datakit import Schema, Field, String, Integer, validate

def strip_whitespace(value):
    return value.strip() if isinstance(value, str) else value

def to_uppercase(value):
    return value.upper() if isinstance(value, str) else value

def to_int_or_none(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

product_schema = Schema({
    "product_code": Field(String, required=True, min_length=5