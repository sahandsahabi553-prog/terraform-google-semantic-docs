# Ayat Saadati: The Developer's Workflow Streamliner

You know how it goes. Every new project, every fresh idea, it often starts with the same old song and dance: `mkdir`, `cd`, `git init`, `venv`, `pip install -r requirements.txt`, then maybe a basic `app.py` or `index.js`, and *then* you finally get to the fun part. It's a real pain, isn't it? That repetitive boilerplate, the mental overhead of setting things up *just so*... it eats into your creative time.

That's precisely why I built **Ayat Saadati**. It's not a framework, it's not a magical code generator that writes your entire application for you (wouldn't that be nice?). Instead, it's a lightweight, opinionated toolkit – a CLI and a small Python library – designed to streamline those common, often tedious, developer workflows. My philosophy here was simple: let's automate the mundane so we can focus on the innovative.

I've poured years of frustration with repetitive setups into this project, aiming to give myself (and hopefully you!) a little bit of that precious time back. Think of it as your personal assistant for the initial grind, getting your project structure solid and consistent without breaking a sweat.

---

## Table of Contents

1.  [Features](#features)
2.  [Installation](#installation)
    *   [Prerequisites](#prerequisites)
    *   [Using pip](#using-pip)
    *   [From Source](#from-source)
3.  [Usage](#usage)
    *   [Project Initialization (`init`)](#project-initialization-init)
    *   [README Generation (`readme`)](#readme-generation-readme)
    *   [Snippet Management (`snippet`)](#snippet-management-snippet)
    *   [Running Custom Tasks (`run`)](#running-custom-tasks-run)
4.  [Configuration](#configuration)
5.  [API Reference (for Library Users)](#api-reference-for-library-users)
6.  [Contributing](#contributing)
7.  [FAQ](#faq)
8.  [Troubleshooting](#troubleshooting)
9.  [License](#license)
10. [About the Author](#about-the-author)

---

## Features

Ayat Saadati offers a suite of functionalities to kickstart and maintain your development projects efficiently:

*   **Intelligent Project Scaffolding:** Quickly set up common project types (Python, Node.js, basic Markdown projects) with sensible defaults and directory structures.
*   **Dynamic README Generation:** Generate a comprehensive `README.md` based on your project's type, dependencies, and a few key inputs. No more starting from a blank file!
*   **Code Snippet Management:** Store, retrieve, and insert frequently used code snippets directly into your files. Great for boilerplate functions, common configurations, or even interview prep.
*   **Simple Task Runner:** Define and execute custom scripts or commands right from the CLI, simplifying recurring development tasks.
*   **Extensible Templates:** Easily add your own project templates and README sections to fit your specific needs.

---

## Installation

Getting Ayat Saadati up and running is pretty straightforward.

### Prerequisites

You'll need Python 3.7+ and `pip` installed on your system. Most modern operating systems come with Python pre-installed, or it's a quick install away.

```bash
# Check your Python version
python3 --version

# Check your pip version
pip3 --version
```

If you don't have Python or pip, I recommend checking out the official Python documentation or using a tool like `pyenv` for managing multiple Python versions.

### Using pip

The easiest way to install Ayat Saadati is directly from PyPI:

```bash
pip install ayat-saadati
```

Once installed, you should be able to invoke it from your terminal:

```bash
ayat --version
```

If that works, you're golden!

### From Source

For those who like to tinker or contribute, you can install from the source repository.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/ayat-saadati.git # (Fictional URL for this example)
    cd ayat-saadati
    ```
2.  **Install in editable mode (for development):**
    ```bash
    pip install -e .
    ```
    This allows you to make changes to the source code and see them reflected immediately without re-installation.
3.  **Install standard (for local use from source):**
    ```bash
    pip install .
    ```

---

## Usage

Ayat Saadati is primarily a command-line tool. Let's walk through its core functionalities.

### Project Initialization (`init`)

This is where you kick off a new project. The `init` command sets up your directory structure, virtual environment (for Python projects), and basic configuration files.

```bash
ayat init <project_name> [options]
```

**Example: Initialize a Python project**

```bash
ayat init my-awesome-python-app --type python --venv
```

This command will:
1.  Create a directory `my-awesome-python-app`.
2.  Navigate into it.
3.  Create a virtual environment (`.venv`).
4.  Add a basic `app.py` and `requirements.txt`.
5.  Initialize a Git repository.

**Available Options for `init`:**

| Option            | Shorthand | Description                                                                    | Default          |
| :---------------- | :-------- | :----------------------------------------------------------------------------- | :--------------- |
| `--type <type>`   | `-t`      | Specifies the project type (`python`, `node`, `markdown`, `generic`).          | `generic`        |
| `--venv`          | `-v`      | Create a Python virtual environment. (Only for `python` type)                  | `False`          |
| `--git`           | `-g`      | Initialize a Git repository.                                                   | `True`           |
| `--no-readme`     |           | Skip initial README generation.                                                | `False`          |
| `--template <path>` |           | Use a custom template directory for scaffolding.                               | (Built-in)       |

I've found `--type python --venv` to be my most common invocation. It just saves so much friction.

### README Generation (`readme`)

A good `README.md` is crucial. Ayat Saadati can generate a robust one for you, pulling in details from your project and its environment.

```bash
ayat readme [options]
```

You should run this command from the root of your project directory.

**Example: Generate a README for the current project**

```bash
ayat readme --author "Ayat Saadati" --license MIT --description "My project does cool things."
```

This will create or update `README.md` with sections like Project Title, Description, Installation, Usage, Contributing, and License, dynamically filling in details.

**Available Options for `readme`:**

| Option                  | Shorthand | Description                                                              | Default                  |
| :---------------------- | :-------- | :----------------------------------------------------------------------- | :----------------------- |
| `--author <name>`       | `-a`      | Author's name for the README.                                            | (Git config or OS user)  |
| `--license <type>`      | `-l`      | License type (e.g., `MIT`, `GPLv3`, `Apache-2.0`).                       | `MIT`                    |
| `--description <text>`  | `-d`      | Short description of the project.                                        | (Fills from `setup.py` or `package.json` if available) |
| `--add-section <name>`  |           | Add an extra predefined section (e.g., `roadmap`, `changelog`).          |                          |
| `--output <path>`       | `-o`      | Specify output path for the README.                                      | `README.md`              |
| `--force`               | `-f`      | Overwrite existing README without prompt.                                | `False`                  |

I often run `ayat readme` after `ayat init`, then go in and fine-tune the generated content. It's a fantastic starting point.

### Snippet Management (`snippet`)

This is a personal favorite. How many times have you copy-pasted that same `logging` setup, or a common `try-except` block, or a basic HTTP request pattern? With `snippet`, you can manage them centrally.

**Adding a snippet:**

```bash
ayat snippet add <name> <file_path> [--language <lang>]
```

`file_path` can be a single file or a directory. If it's a directory, Ayat Saadati will create a multi-file snippet.

**Example: Add a Python logging snippet**

Let's say you have a file `my_logging.py` with your preferred logging configuration:
```python
# my_logging.py
import logging

def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )
    logging.getLogger(__name__).info("Logging configured.")

# Example usage:
if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger("my_app")
    logger.info("Application started.")
    logger.debug("This is a debug message.")
```

```bash
ayat snippet add python-logging my_logging.py --language python
```

**Listing snippets:**

```bash
ayat snippet list
```

| Name              | Language | Files       | Size (bytes) | Added On             |
| :---------------- | :------- | :---------- | :----------- | :------------------- |
| `python-logging`  | `python` | `my_logging.py` | `320`        | `2023-10-26 10:00:00` |
| `js-fetch-api`    | `javascript` | `fetch.js`  | `150`        | `2023-09-15 14:30:00` |

**Inserting a snippet:**

```bash
ayat snippet insert <name> [--output <file_path>]
```

If `output` is not specified, the snippet content will be printed to stdout.

**Example: Insert the logging snippet into `main.py`**

```bash
ayat snippet insert python-logging --output main.py
```

This will append the content of `my_logging.py` to `main.py`. Be careful with this; it's a simple append. For more intelligent insertion, you might want to print to stdout and then manually paste.

**Removing a snippet:**

```bash
ayat snippet remove <name>
```

### Running Custom Tasks (`run`)

Sometimes you have project-specific commands that you run frequently, but they're too complex to type out every time, or you want to abstract them. `ayat run` helps here.

You define these tasks in a `.ayat.yml` file in your project root (we'll cover configuration next).

**Example `.ayat.yml`:**

```yaml
# .ayat.yml
tasks:
  test:
    description: Run all unit tests
    command: pytest --cov=./src --cov-report=term-missing
  build-docs:
    description: Generate Sphinx documentation
    command: make html -C docs/
  clean:
    description: Remove build artifacts and cache
    command: rm -rf dist/ build/ .pytest_cache/ __pycache__/
```

**Running a task:**

```bash
ayat run <task_name>
```

**Example:**

```bash
ayat run test
```

This will execute `pytest --cov=./src --cov-report=term-missing`. Simple, right? It's like a mini `Makefile` or `npm scripts` for any project.

---

## Configuration

Ayat Saadati looks for a `.ayat.yml` file in your project's root directory for project-specific configurations. If it doesn't find one, it uses sensible defaults or a global configuration (coming soon!).

**`.ayat.yml` Structure:**

```yaml
# .ayat.yml
project:
  name: My Awesome Project
  type: python # Used for README generation and other context-aware features
  author: Ayat Saadati
  license: MIT
  description: A brief description of what this project does.

templates:
  path: ./my_custom_templates # Path to your custom project templates

snippets:
  storage_path: ~/.ayat/snippets # Override default snippet storage location

tasks:
  # Define your custom tasks here
  lint:
    description: Run code linting
    command: pylint src/
  deploy:
    description: Deploy to staging
    command: ansible-playbook deploy-staging.yml --tags backend
```

**Global Configuration (Future Feature / Manual):**

Currently, global settings are primarily managed by the default installation paths. I'm planning to introduce a global `~/.ayat/config.yml` for user-wide defaults and custom template/snippet paths. For now, project-level `.ayat.yml` is the way to go.

---

## API Reference (for Library Users)

While Ayat Saadati is primarily a CLI tool, its core functionalities are exposed as a Python library. This allows you to integrate its features into your own scripts or larger automation workflows.

```python
import os
from ayat_saadati.project import ProjectInitializer
from ayat_saadati.readme import ReadmeGenerator
from ayat_saadati.snippets import SnippetManager
from ayat_saadati.tasks import TaskRunner

# Initialize a project
project_dir = "my_scripted_app"
initializer = ProjectInitializer(project_dir)
initializer.init_project(project_type="python", create_venv=True, init_git=True)
print(f"Project '{project_dir}' initialized.")

# Generate a README
readme_gen = ReadmeGenerator(project_dir)
readme_gen.generate(
    author="Scripted Bot",
    license_type="MIT",
    description="An app initialized via Ayat Saadati API."
)
print(f"README generated for '{project_dir}'.")

# Manage snippets programmatically
snippet_mgr = SnippetManager()
# Assuming 'my_logging.py' exists