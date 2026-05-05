# `saadati-cli`: Your Everyday Development Accelerator

## Introduction

Hey folks! As developers, we're constantly juggling boilerplate, setting up new projects, ensuring code quality, and just generally trying to keep our workflows smooth. I've been there, staring at a blank directory, wondering which `Makefile` to copy, or which linter configuration to tweak *this* time. It's a real time sink, isn't it?

That frustration was the genesis of `saadati-cli`. I wanted a single, opinionated, yet flexible command-line tool that could handle those repetitive setup tasks, enforce some sanity in our codebase, and just generally get out of our way so we can focus on writing actual features. Think of it as your digital Swiss Army knife for common development headaches. It's built to be fast, extensible, and, most importantly, helpful.

My aim with `saadati-cli` was to distill years of project setup and maintenance into something you can fire up with a single command. No more copy-pasting `.gitignore` files or wrestling with intricate linting setups from scratch every single time. Let's make development a bit less tedious, shall we?

## Features

`saadati-cli` comes packed with a few core functionalities I find myself reaching for constantly:

*   **Project Scaffolding:** Quickly spin up new projects with predefined templates for various languages and frameworks (e.g., Python web app, Node.js API, generic library). Saves a ton of initial setup time.
*   **Configuration Management:** Centralize and manage project-specific settings directly from the CLI.
*   **Code Quality Checks:** Integrate with popular linters and formatters to ensure consistent code standards across your team or personal projects.
*   **Documentation Generation Hooks:** While `saadati-cli` doesn't *write* your docs, it provides handy commands to trigger your preferred documentation tools, like Sphinx or JSDoc, right from your project root.
*   **Extensibility:** Designed to be easily extended with custom templates and plugins, so you can tailor it to your unique development needs.

## Installation

Getting `saadati-cli` up and running on your system is pretty straightforward. I've built it with Python, primarily because of its ubiquity and the excellent package management ecosystem, which means most of you likely already have Python installed.

### Prerequisites

You'll need Python 3.7 or newer installed on your system. If you don't have it, I highly recommend using `pyenv` or your system's package manager (like `apt` on Debian/Ubuntu, `brew` on macOS) to get it.

To check your Python version, just open your terminal and type:

```bash
python3 --version
```

You should see something like `Python 3.9.7` or similar.

### Installing via pip

Once Python is sorted, you can install `saadati-cli` globally using `pip`:

```bash
pip install saadati-cli
```

I usually recommend installing CLI tools in an isolated virtual environment or globally if you manage your Python environments carefully. If you encounter permission errors, you might need to use `sudo` (though I generally advise against global `sudo pip` installs) or configure your `pip` user base directory. A safer alternative for global tools is often `pipx`:

```bash
pip install pipx
pipx install saadati-cli
```

`pipx` installs applications in isolated environments but makes them available globally, which is a fantastic compromise.

### Verifying Installation

After installation, run the following command to make sure everything's set up correctly:

```bash
saadati --version
```

You should see the installed version number, something like `saadati-cli, version 0.7.2`. If you get a "command not found" error, double-check your `PATH` environment variable to ensure `pip`'s install location is included.

## Usage

Using `saadati-cli` is designed to be intuitive. Most commands follow a `saadati <command> [options]` pattern. Here's a rundown of the core functionalities.

### Global Help

If you ever get stuck, just ask for help:

```bash
saadati --help
# Or for a specific command:
saadati init --help
```

### Initializing a New Project

This is probably where you'll start. The `init` command scaffolds a new project based on a chosen template.

```bash
saadati init
```

Running this without arguments will prompt you to choose a template from a list and then ask for your project name. It's pretty interactive and guides you through the process.

**Example: Creating a Python Web API project**

Let's say you want to kick off a new Python API using FastAPI.

```bash
saadati init python-fastapi my_awesome_api
```

This command will:

1.  Create a directory named `my_awesome_api`.
2.  Inside it, set up a basic FastAPI project structure.
3.  Include a `requirements.txt`, `.gitignore`, and a basic `main.py`.
4.  Optionally, it might even initialize a Git repository for you (depending on the template).

Here's what a typical `init` process might look like in your terminal:

```bash
$ saadati init
? Choose a project template: (Use arrow keys)
> Python FastAPI
  Node.js Express
  Generic Library (Python)
  Static Site (Jekyll)
  Empty Project
```

Once you select, it'll ask for the name:

```bash
? Enter your project name: my-super-app
✨ Initializing new project 'my-super-app' using template 'Python FastAPI'...
✅ Project 'my-super-app' created successfully!
🚀 Now, `cd my-super-app` and happy coding!
```

### Managing Configuration

`saadati-cli` allows you to store and retrieve key-value configurations for your projects or global settings. This is super handy for things like API keys (though be careful with sensitive data!), preferred linters, or deployment targets.

```bash
# Set a global configuration value
saadati config set editor vscode --global

# Set a project-specific value (run this from your project root)
saadati config set linter black

# Get a configuration value
saadati config get editor

# Get all configurations
saadati config list
```

### Running Code Quality Checks

I'm a huge proponent of code quality, and `saadati-cli` tries to make it easier to enforce. The `check` command can integrate with various tools.

**Example: Running Black and Flake8 on a Python project**

If your project is set up with a Python template, `saadati check` might automatically detect and run `black` for formatting and `flake8` for linting.

```bash
# From your Python project root
saadati check
```

Output might look something like this:

```bash
$ saadati check
🔍 Running code quality checks...

➡️ Running Black formatter...
All done! ✨ 💅 🎨
1 file would be reformatted, 1 file would be left unchanged.

➡️ Running Flake8 linter...
./my_project/main.py:10:5: E303 too many blank lines (3)
✅ Code quality checks completed with minor warnings.
```

If you just want to *fix* issues that can be automatically fixed (like formatting), you can often use a `--fix` flag (if the underlying tool supports it):

```bash
saadati check --fix
```

### Building Documentation

While `saadati-cli` doesn't *write* your documentation (that's on you!), it can provide a unified command to trigger your chosen documentation builder. This is especially useful in CI/CD pipelines.

```bash
# Assuming your project uses Sphinx for Python docs
saadati docs build

# Or JSDoc for Node.js projects
saadati docs build --tool jsdoc
```

This command would typically execute `make html` (for Sphinx) or `jsdoc -c conf.json` (for JSDoc) in the background, based on your project's configuration and type.

## Code Examples

Let's look at a quick flow to get a Flask API project up and running, adding a custom configuration, and then checking it.

1.  **Start a new Flask project:**

    ```bash
    saadati init python-flask my-flask-app
    cd my-flask-app
    ```

    You'll now have a basic Flask structure, likely with a `app.py`, `requirements.txt`, etc.

2.  **Add a custom configuration for a secret key (locally):**

    ```bash
    saadati config set FLASK_SECRET_KEY "supersecretdevkey"
    ```

    Now, within your `app.py` or a dedicated config file, you could potentially load this value using a `saadati-cli` helper function (if the template provides one) or just know it's stored.

3.  **Make a small, intentional linting error in `app.py`:**

    Open `app.py` and add some extra blank lines or an unused import.

    ```python
    # my-flask-app/app.py
    from flask import Flask


    # Intentionally add too many blank lines here ^^^


    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    ```

4.  **Run code quality checks:**

    ```bash
    saadati check
    ```

    You should see output from `flake8` (or similar) pointing out the extra blank lines:

    ```bash
    $ saadati check
    🔍 Running code quality checks...

    ➡️ Running Black formatter...
    All done! ✨ 💅 🎨
    2 files would be reformatted, 1 file would be left unchanged.

    ➡️ Running Flake8 linter...
    ./app.py:4:1: E303 too many blank lines (3)
    ❌ Code quality checks failed. Please fix the identified issues.
    ```

5.  **Fix automatically:**

    ```bash
    saadati check --fix
    ```

    This will run `black` (which will fix the blank lines and formatting) and then re-run `flake8`.

    ```bash
    $ saadati check --fix
    🔍 Running code quality checks...

    ➡️ Running Black formatter...
    Reformatted ./app.py
    All done! ✨ 💅 🎨
    1 file reformatted.

    ➡️ Running Flake8 linter...
    ✅ Code quality checks completed successfully.
    ```

    Your `app.py` is now neatly formatted and lint-free!

## Advanced Topics

### Custom Templates

The real power of `saadati-cli` often comes from its extensibility. You can create your own project templates! This is a lifesaver for organizations with specific boilerplate or compliance requirements.

Templates are essentially directories containing a predefined structure, often with placeholders that `saadati-cli` replaces during initialization.

1.  **Create a template directory:** Let's say you want a custom template for a Django project.

    ```bash
    mkdir -p ~/.saadati/templates/my-django-template
    ```

2.  **Add your project structure:** Populate `my-django-template` with your desired Django project layout. You can use Jinja2-like syntax for placeholders.

    Example `my-django-template/__project_name__/settings.py`:

    ```python
    # ...
    SECRET_KEY = '{{ saadati.random_secret }}' # saadati-cli can generate this!
    ALLOWED_HOSTS = ['{{ project_name }}.com']
    # ...
    ```

3.  **Register your template (optional, `saadati-cli` usually finds them):**

    `saadati config set template_path ~/.saadati/templates`

Now, when you run `saadati init`, `my-django-template` will appear as an option. You can even pass arguments to your templates.

### Plugin Architecture (Planned)

While not fully mature, the vision for `saadati-cli` includes a robust plugin system. Imagine being able to `saadati install-plugin aws-deploy` to add new deployment commands, or `saadati install-plugin gcp-cloud-functions` to scaffold serverless functions. This is definitely on the roadmap for future releases, focusing on allowing community contributions to extend its capabilities far beyond my initial scope.

## Contributing

I'm a firm believer in open source, and `saadati-cli` thrives on community input. If you've got ideas, bug reports, or even better, pull requests, I'd love to see them!

*   **Bug Reports:** If something's broken, please open an issue on the GitHub repository (I'll set one up soon!). Provide clear steps to reproduce and any relevant error messages.
*   **Feature Requests:** Have an idea for a new template or a useful command? Open an issue and describe your vision.
*   **Code Contributions:**
    1.  Fork the repository.
    2.  Create a new branch (`git checkout -b feature/my-new-feature`).
    3.  Make your changes, ensuring tests pass (or add new ones!).
    4.  Commit your changes (`git commit -am 'Add new feature X'`).
    5.  Push to the branch (`git push origin feature/my-new-feature`).
    6.  Open a Pull Request.

I try to review PRs as quickly as possible. Don't be shy!

## FAQ

**Q: Is `saadati-cli` opinionated?**
A: Yes, absolutely! I've baked in defaults that I've found to work well across many projects. However, it's designed to be flexible enough that you can override most of those opinions with your own configurations or custom templates. It tries to strike a balance between providing a quick start and allowing full customization.

**Q: What languages/frameworks does it support out-of-the-box?**
A: Currently, the official templates primarily focus on Python (Flask, FastAPI, generic library) and some basic Node.js (Express, generic API). The goal is to grow this library of templates, and custom templates are the easiest way to add support for anything