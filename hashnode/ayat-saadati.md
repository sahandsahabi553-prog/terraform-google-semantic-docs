# `ayat-configurator`: Robust Configuration Management for Modern Applications

Hey folks, Ayat Saadati here! You can find me usually tinkering with code over at [dev.to/@ayat_saadat](https://dev.to/ayat_saadat). I'm excited to introduce `ayat-configurator`, a Python library I've been refining to tackle one of those often-underestimated challenges in software development: robust, flexible, and secure configuration management.

Let's be honest, dealing with application configurations can be a real headache. Whether you're juggling environment variables, YAML files, JSON blobs, or even just old-school `.ini` files, getting it right, keeping it consistent across environments, and ensuring sensitive data stays out of source control is a constant battle. I've been there, more times than I care to admit, debugging production issues only to find a misplaced configuration value. That's why I built `ayat-configurator`. My goal was to create a straightforward, yet powerful, tool that makes managing application settings less of a chore and more of a pleasure.

## What is `ayat-configurator`?

`ayat-configurator` is a Python library designed to simplify the loading, parsing, and validation of application configurations from multiple sources. It prioritizes clarity, type safety, and security, allowing you to define your configuration schema once and then effortlessly load values from environment variables, YAML, JSON, and even custom sources, all with sensible defaults and built-in secret handling.

I'm a firm believer that configuration should be an explicit part of your application's design, not an afterthought. This library reflects that philosophy by pushing you towards well-defined schemas and clear separation of concerns.

## Key Features

*   **Multi-Source Loading**: Seamlessly load configurations from environment variables, YAML files, JSON files, and even custom sources, with a clear precedence order.
*   **Schema Definition & Validation**: Define your expected configuration structure and data types using simple Python classes. `ayat-configurator` handles validation automatically, catching issues early.
*   **Type Coercion**: Automatically converts string values from environment variables into appropriate Python types (integers, booleans, lists, etc.).
*   **Secret Management**: Built-in support for placeholders that can resolve to secrets from external vault systems or environment variables, keeping sensitive data out of your main config files.
*   **Environment-Specific Overrides**: Easily manage different configurations for development, staging, and production environments.
*   **Sensible Defaults**: Define default values directly in your schema, reducing boilerplate and making configurations more resilient.
*   **Extensible**: Designed with extensibility in mind, allowing you to easily add support for new configuration sources or custom validation logic.

## Installation

Getting `ayat-configurator` up and running is as simple as a `pip` command. I try to keep dependencies lean, so you won't be pulling in half the internet with this one.

```bash
pip install ayat-configurator
```

If you need support for specific file formats like YAML, you'll want to include the extra dependencies:

```bash
pip install ayat-configurator[yaml]
pip install ayat-configurator[json] # JSON support is usually built-in, but just in case for complex scenarios.
```

My advice? Start simple and add what you need. `pip install ayat-configurator[all]` will grab everything, which is often what I do for quick prototyping.

## Usage

Let's dive into some examples. I'll walk you through defining a simple configuration, loading it, and then showing off some of the more advanced features.

### 1. Defining Your Configuration Schema

The heart of `ayat-configurator` is defining your configuration schema using a `dataclass`-like structure. This gives you strong typing and makes your configuration self-documenting.

```python
# app_config.py
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class DatabaseConfig:
    host: str = "localhost"
    port: int = 5432
    user: str = "admin"
    password: Optional[str] = None # Sensitive, often from environment/secrets
    name: str = "my_app_db"

@dataclass
class APIConfig:
    api_key: str
    base_url: str = "https://api.example.com"
    timeout_seconds: int = 30

@dataclass
class AppConfig:
    env: str = "development"
    debug: bool = False
    log_level: str = "INFO"
    admin_emails: List[str] = field(default_factory=list)
    database: DatabaseConfig
    api: APIConfig
```

See how clear that is? No more guessing what keys are expected or what types they should be.

### 2. Loading Basic Configuration

Now, let's load this configuration. `ayat-configurator` is smart enough to infer types and handle basic parsing.

```python
# main.py
from ayat_configurator import ConfigLoader
from app_config import AppConfig

# Initialize the loader with your root configuration class
loader = ConfigLoader(AppConfig)

try:
    config = loader.load()
    print("Configuration Loaded Successfully:")
    print(f"Environment: {config.env}")
    print(f"Debug Mode: {config.debug}")
    print(f"Database Host: {config.database.host}")
    print(f"API Key: {config.api.api_key[:5]}...") # Don't print full secrets!

    if config.admin_emails:
        print(f"Admin Emails: {', '.join(config.admin_emails)}")

except Exception as e:
    print(f"Error loading configuration: {e}")

# Example of how you might set environment variables before running:
# export APP_API__API_KEY="supersecretapikey"
# export APP_DATABASE__PASSWORD="my_db_password"
# python main.py
```

When you run this, `ayat-configurator` will look for environment variables. Notice the double underscore `__` for nested configuration values (e.g., `APP_API__API_KEY`). This is a convention I've adopted that works really well for hierarchical configurations.

### 3. Loading from Multiple Sources (YAML, Environment)

This is where `ayat-configurator` really shines. You can specify multiple sources, and it will apply them in order, with later sources overriding earlier ones. Environment variables always take precedence by default, which is a common best practice for Twelve-Factor Apps.

Let's create a `config.yaml` file:

```yaml
# config.yaml
env: staging
debug: true
log_level: DEBUG
admin_emails:
  - ayat@example.com
  - support@example.com

database:
  host: db.staging.example.com
  name: app_staging_db

api:
  base_url: https://api.staging.example.com
  timeout_seconds: 60
```

Now, load it:

```python
# main.py (continued)
from ayat_configurator import ConfigLoader, YamlSource, EnvSource
from app_config import AppConfig

loader = ConfigLoader(AppConfig,
    sources=[
        YamlSource("config.yaml"), # Load from YAML first
        EnvSource()                # Environment variables override YAML
    ]
)

try:
    config = loader.load()
    print("\nConfiguration Loaded from YAML & Environment:")
    print(f"Environment: {config.env}")
    print(f"Debug Mode: {config.debug}")
    print(f"Database Host: {config.database.host}")
    print(f"API Key: {config.api.api_key[:5]}...") # Still from ENV
    print(f"Admin Emails: {', '.join(config.admin_emails)}")

except Exception as e:
    print(f"Error loading configuration: {e}")

# Try running with:
# export APP_API__API_KEY="anothersecretfromenv"
# python main.py
```

If `APP_API__API_KEY` is set in the environment, it will override any `api.api_key` you might place in `config.yaml`. This explicit precedence order is crucial for predictable configurations.

### 4. Secret Handling

Often, you don't want secrets directly in your YAML or even environment variables that are easily logged. `ayat-configurator` supports a simple placeholder mechanism that allows you to specify that a value should be resolved from an external source, typically another environment variable meant specifically for secrets.

Let's modify `config.yaml` to reference a secret:

```yaml
# config.yaml
# ... other configs ...
database:
  host: db.staging.example.com
  name: app_staging_db
  password: "${DB_PASSWORD}" # This will be resolved from the DB_PASSWORD env var

api:
  base_url: https://api.staging.example.com
  timeout_seconds: 60
  api_key: "${API_AUTH_TOKEN}" # This will be resolved from API_AUTH_TOKEN env var
```

Now, when loading:

```python
# main.py (continued)
from ayat_configurator import ConfigLoader, YamlSource, EnvSource
from app_config import AppConfig

loader = ConfigLoader(AppConfig,
    sources=[
        YamlSource("config.yaml"),
        EnvSource()
    ]
)

try:
    config = loader.load()
    print("\nConfiguration with Secrets Resolved:")
    print(f"Database Password: {config.database.password[:5]}...")
    print(f"API Key: {config.api.api_key[:5]}...")

except Exception as e:
    print(f"Error loading configuration: {e}")

# To run this, you'd set these environment variables:
# export DB_PASSWORD="my_super_secret_db_pass"
# export API_AUTH_TOKEN="long_jwt_token_here"
# python main.py
```

`ayat-configurator` will look for `DB_PASSWORD` and `API_AUTH_TOKEN` in the environment and substitute them. This pattern is incredibly useful when deploying to systems like Kubernetes or CI/CD pipelines where secrets are injected as environment variables.

## API Reference (Brief Overview)

I'll keep this concise. The core components are pretty intuitive:

| Class/Function        | Description                                                                                                                                                                                           |
| :-------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ConfigLoader(config_cls, sources=None)` | The main class to instantiate. Takes your root configuration `dataclass` and an optional list of `ConfigSource` instances. |
| `loader.load()`       | Method to trigger the configuration loading process. Returns an instance of your `config_cls` populated with values.                                                                          |
| `ConfigSource`        | Abstract base class for all configuration sources. You'd typically use its concrete implementations.                                                                                                    |
| `EnvSource(prefix=None)` | Loads configuration values from environment variables. An optional `prefix` can be used to filter variables (e.g., `prefix="APP_"`).                                                           |
| `YamlSource(file_path)` | Loads configuration values from a YAML file.                                                                                                                                                          |
| `JsonSource(file_path)` | Loads configuration values from a JSON file.                                                                                                                                                          |
| `DictSource(data)`      | Loads configuration values directly from a Python dictionary. Useful for testing or programmatic configurations.                                                                                    |
| `@dataclass`          | Python's built-in decorator for data classes. Used to define your configuration schema.                                                                                                                |
| `field(default_factory=list)` | From `dataclasses`, useful for mutable defaults like lists or dictionaries to avoid unexpected shared state.                                                                                      |

## Troubleshooting

I've tried to make `ayat-configurator` robust, but sometimes things go sideways. Here are a few common gotchas and how to fix them:

*   **`ConfigValidationError: Missing required field '...'`**: This is probably the most common. It means a field in your schema was marked as required (i.e., didn't have a default value or `Optional` type hint), and `ayat-configurator` couldn't find a value for it in any of your specified sources.
    *   **Fix**: Check your `config.yaml`/`config.json`, environment variables (remember the `APP_PARENT__CHILD` naming convention!), or ensure you've provided a default value in your `dataclass`.
*   **`ConfigValidationError: Invalid type for field '...': expected <int>, got 'abc'`**: You tried to assign a string like "abc" to an `int` field. `ayat-configurator` does its best with type coercion, but sometimes it just can't make sense of it.
    *   **Fix**: Ensure your configuration values match the types defined in your schema. For environment variables, values are always strings, so make sure they can be safely converted (e.g., "true"/"false" for `bool`, "123" for `int`).
*   **Secrets not resolving (`password: "${DB_PASSWORD}"` literal string showing up)**: This means the environment variable `DB_PASSWORD` wasn't set when `ayat-configurator` tried to resolve the placeholder.
    *   **Fix**: Double-check that the environment variable is indeed set in the shell or deployment environment where your application is