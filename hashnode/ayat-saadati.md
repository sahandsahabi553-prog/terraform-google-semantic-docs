# The `ayat-fetcher` Library: Simplifying Your API Interactions

Hey there! If you've ever found yourself wrestling with repetitive HTTP request boilerplate, manually handling retries, or just wishing there was a cleaner way to interact with APIs in Python, you're in the right place. I've been there countless times, and that's precisely why I built `ayat-fetcher`.

This library isn't about reinventing the wheel; it's about making that wheel spin smoother, faster, and with far less friction. My goal was to create a lightweight, intuitive toolkit that abstracts away the tedious parts of API consumption, letting you focus on the data and your application's logic. Think of it as your trusty sidekick for all things HTTP.

## Table of Contents

1.  [Introduction](#introduction)
2.  [Key Features](#key-features)
3.  [Installation](#installation)
4.  [Quick Start & Basic Usage](#quick-start--basic-usage)
    *   [Making a GET Request](#making-a-get-request)
    *   [Sending Data with POST](#sending-data-with-post)
    *   [Custom Headers & Authentication](#custom-headers--authentication)
5.  [Configuration & Advanced Usage](#configuration--advanced-usage)
    *   [Setting a Base URL](#setting-a-base-url)
    *   [Automatic Retries](#automatic-retries)
    *   [Error Handling](#error-handling)
    *   [Async Support](#async-support)
6.  [Frequently Asked Questions (FAQ)](#frequently-asked-questions-faq)
7.  [Troubleshooting Common Issues](#troubleshooting-common-issues)
8.  [Contributing](#contributing)
9.  [License](#license)
10. [Connect with Me](#connect-with-me)

---

## 1. Introduction

Let's be honest, interacting with REST APIs often involves a lot of boilerplate code: setting up `requests`, parsing JSON, checking status codes, handling network errors, and sometimes even implementing retries. It's a fundamental part of modern development, but it shouldn't be a chore.

`ayat-fetcher` was born out of a desire to streamline this process. It provides a high-level, opinionated interface over popular HTTP libraries, offering sensible defaults and common functionalities right out of the box. Whether you're fetching data from a public API, integrating with a third-party service, or building a microservice, `ayat-fetcher` aims to make your life a little easier.

I've poured my experiences from various projects into this, focusing on what typically causes headaches and how to eliminate them. The result is a library that's both powerful and incredibly simple to get started with.

## 2. Key Features

Here's what `ayat-fetcher` brings to the table:

*   **Dead Simple Syntax**: Make requests with minimal lines of code.
*   **Automatic JSON Parsing**: Get your response data as a Python dictionary or list, no manual `response.json()` needed.
*   **Built-in Retry Logic**: Configurable exponential backoff and retry attempts for transient network issues.
*   **Request Presets**: Define common headers, authentication, and base URLs once.
*   **Robust Error Handling**: Clear exceptions for common HTTP errors (4xx, 5xx) and network problems.
*   **Asynchronous Support**: Integrate seamlessly into your `asyncio` applications.
*   **Lightweight & Minimal Dependencies**: Keep your project slim.
*   **Extensible**: Easily add custom middleware or hook into different stages of the request lifecycle.

## 3. Installation

Getting `ayat-fetcher` up and running is a breeze. It's available on PyPI, so a simple `pip` command is all you need.

```bash
pip install ayat-fetcher
```

If you need `async` support, you'll want to install it with the `async` extra:

```bash
pip install "ayat-fetcher[async]"
```

This will pull in `aiohttp`, which is what we use under the hood for asynchronous operations.

## 4. Quick Start & Basic Usage

Let's dive into some code! You'll see how `ayat-fetcher` simplifies common API interactions.

### Making a GET Request

The most common operation is fetching data. With `ayat-fetcher`, it's just one line.

```python
from ayat_fetcher import fetcher

# Fetch some public data, e.g., from JSONPlaceholder
try:
    data = fetcher.get("https://jsonplaceholder.typicode.com/posts/1")
    print("Fetched data:")
    print(data)
    print(f"Title: {data.get('title')}")
except Exception as e:
    print(f"An error occurred: {e}")

# Example output:
# Fetched data:
# {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
# Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
```

Notice how `data` is immediately a Python dictionary. No `response.json()` calls needed! If the API returns a list, you'll get a list. If it's plain text, you'll get a string. `ayat-fetcher` intelligently handles the content type for you.

### Sending Data with POST

Submitting data is equally straightforward. Just pass your payload as a dictionary to the `data` parameter.

```python
from ayat_fetcher import fetcher

new_post = {
    "title": "My New Post",
    "body": "This is the content of my exciting new post.",
    "userId": 1,
}

try:
    response_data = fetcher.post("https://jsonplaceholder.typicode.com/posts", data=new_post)
    print("\nNew post created:")
    print(response_data)
    print(f"Assigned ID: {response_data.get('id')}")
except Exception as e:
    print(f"An error occurred: {e}")

# Example output:
# New post created:
# {'title': 'My New Post', 'body': 'This is the content of my exciting new post.', 'userId': 1, 'id': 101}
# Assigned ID: 101
```

`ayat-fetcher` automatically sets the `Content-Type` header to `application/json` when you pass a dictionary to `data`, and serializes it for you. If you need to send form data, you can pass a dictionary to `form` instead.

### Custom Headers & Authentication

You'll often need to send custom headers, especially for authentication. You can pass a `headers` dictionary to any request.

```python
from ayat_fetcher import fetcher
import os

# Imagine you have an API key stored in an environment variable
API_KEY = os.getenv("MY_SUPER_SECRET_API_KEY", "your_fallback_api_key_if_not_set")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "X-Custom-Header": "My-App-Id-123",
    "Accept": "application/json"
}

try:
    # Let's hit an imaginary authenticated endpoint
    protected_data = fetcher.get("https://api.example.com/v1/user/profile", headers=headers)
    print("\nProtected profile data:")
    print(protected_data)
except Exception as e:
    print(f"Could not fetch profile: {e}")

# Example output (assuming success):
# Protected profile data:
# {'user_id': 'abc-123', 'username': 'ayat_dev', 'email': 'ayat@example.com'}
```

## 5. Configuration & Advanced Usage

While the basic usage is powerful, `ayat-fetcher` also provides ways to configure default behaviors and handle more complex scenarios.

### Setting a Base URL

For APIs where you're constantly hitting the same base URL, it's cumbersome to type it out every time. `ayat-fetcher` lets you create a `Fetcher` instance with a predefined base URL.

```python
from ayat_fetcher import Fetcher

# Create a fetcher instance for the JSONPlaceholder API
json_api = Fetcher(base_url="https://jsonplaceholder.typicode.com")

try:
    post_data = json_api.get("/posts/2") # Notice the relative path
    print("\nFetched post with base URL:")
    print(post_data.get('title'))

    comments = json_api.get("/posts/2/comments")
    print(f"Found {len(comments)} comments for post 2.")

except Exception as e:
    print(f"Error with base URL fetch: {e}")

# Example output:
# Fetched post with base URL:
# qui est esse
# Found 5 comments for post 2.
```

You can also pass default `headers`, `timeout`, and `retries` to the `Fetcher` constructor.

```python
from ayat_fetcher import Fetcher
import os

API_TOKEN = os.getenv("ANOTHER_API_TOKEN", "some_default_token")

# Create a fetcher with default headers and retries
my_service_fetcher = Fetcher(
    base_url="https://api.my-internal-service.com/v2",
    headers={
        "Authorization": f"Token {API_TOKEN}",
        "X-Request-Source": "My-Python-App"
    },
    retries=3, # Default to 3 retries for all requests from this instance
    timeout=10 # Default timeout of 10 seconds
)

try:
    user_info = my_service_fetcher.get("/users/current")
    print("\nUser info from internal service:")
    print(user_info)

    # This request will also use the default headers and retries
    audit_log = my_service_fetcher.post("/audit/log", data={"action": "user_fetched_profile"})
    print("Audit log recorded.")

except Exception as e:
    print(f"Failed to interact with internal service: {e}")
```

### Automatic Retries

Network glitches happen. APIs can momentarily be unavailable. `ayat-fetcher` helps you gracefully handle these transient errors with built-in retry logic. By default, retries are *off* for the global `fetcher` instance, but you can enable them.

```python
from ayat_fetcher import fetcher

# Enable retries for a specific request
try:
    # Imagine this endpoint is flaky and sometimes returns a 500 error
    flaky_data = fetcher.get("https://flaky-api.example.com/data", retries=5, backoff_factor=0.5)
    print("\nSuccessfully fetched data from flaky API after retries.")
except Exception as e:
    print(f"Failed to fetch from flaky API even after retries: {e}")

# You can also configure retries when creating a Fetcher instance
from ayat_fetcher import Fetcher
resilient_fetcher = Fetcher(base_url="https://api.another-service.com", retries=3, backoff_factor=1)

try:
    product_list = resilient_fetcher.get("/products")
    print(f"\nFetched {len(product_list)} products with built-in resilience.")
except Exception as e:
    print(f"Failed to get products: {e}")
```

*   `retries`: The maximum number of retry attempts.
*   `backoff_factor`: A factor to calculate the sleep time between retries (e.g., `sleep_time = backoff_factor * (2 ** (retry_number - 1))`).

### Error Handling

`ayat-fetcher` raises specific exceptions for different types of errors, making it easier to catch and handle them programmatically.

```python
from ayat_fetcher import fetcher
from ayat_fetcher.exceptions import (
    HTTPStatusError,
    NetworkError,
    TimeoutError,
    FetchError # Base exception for all ayat_fetcher errors
)

# Example 1: Non-existent endpoint (404 Not Found)
try:
    fetcher.get("https://jsonplaceholder.typicode.com/non-existent-path")
except HTTPStatusError as e:
    print(f"\nCaught HTTP status error: {e.status_code} - {e.message}")
    print(f"Response body: {e.response_text}") # You can access the raw response text
except FetchError as e: # Catch all ayat_fetcher specific errors
    print(f"\nCaught a generic fetcher error: {e}")


# Example 2: Invalid domain (Network Error)
try:
    fetcher.get("https://definitely-not-a-real-domain-12345.com")
except NetworkError as e:
    print(f"\n