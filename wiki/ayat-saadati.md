# `dev-tools` by Ayat Saadat: Streamlining Your Development Workflow

I've always been a big believer in making our lives as developers easier. We spend countless hours on setup, configuration, and repetitive tasks that, frankly, steal time from the creative, problem-solving work we love. That's precisely why I started building `dev-tools` – a command-line interface (CLI) designed to cut through the boilerplate and give you back valuable development time.

Think of `dev-tools` as your trusty Swiss Army knife for common development headaches. Whether you're kicking off a new project, trying to make sense of a complex dependency tree, or just need a quick boilerplate code snippet, this tool aims to be right there with you, making things just a little bit smoother. My goal with `dev-tools` was never to replace sophisticated IDEs or build systems, but rather to complement them, handling those quick, tactical tasks that often break your flow.

---

## Table of Contents

1.  [Introduction](#introduction)
2.  [Features](#features)
3.  [Installation](#installation)
    *   [Prerequisites](#prerequisites)
    *   [Installation Steps](#installation-steps)
    *   [Verifying Installation](#verifying-installation)
4.  [Usage](#usage)
    *   [Basic Commands](#basic-commands)
    *   [`dev-tools init`](#dev-tools-init)
    *   [`dev-tools deps`](#dev-tools-deps)
    *   [`dev-tools snippet`](#dev-tools-snippet)
5.  [Configuration](#configuration)
6.  [Code Examples](#code-examples)
    *   [Scaffolding a React Project](#scaffolding-a-react-project)
    *   [Analyzing Project Dependencies](#analyzing-project-dependencies)
    *   [Generating a Simple Function Snippet](#generating-a-simple-function-snippet)
7.  [FAQ](#faq)
8.  [Troubleshooting](#troubleshooting)
9.  [Getting Involved & Further Reading](#getting-involved--further-reading)

---

## Introduction

As I mentioned, `dev-tools` is a CLI focused on developer experience. It's written primarily in Node.js, making it highly accessible to anyone familiar with the JavaScript ecosystem, but its utility extends to projects across various languages and frameworks. I built it to be modular, so you can pick and choose the features you need without bloat. It's really about giving you sensible defaults and quick actions for common development tasks.

### Why `dev-tools`?

You might be thinking, "Another CLI? Don't we have enough?" And you're right, there are tons of fantastic tools out there. But `dev-tools` aims for a different niche: being that generalized helper that understands common pain points across different project types. I found myself repeatedly writing similar scripts or searching for the same boilerplate, and I figured, why not centralize some of that wisdom? It's not a framework-specific tool; it's a *developer-specific* tool.

---

## Features

Here's a quick rundown of what `dev-tools` brings to the table right now. I'm always adding more, so keep an eye out!

*   **Project Scaffolding (`init`):** Quickly create new projects from predefined templates (e.g., React, Vue, Node.js API). Saves you from `create-react-app` fatigue.
*   **Dependency Analysis (`deps`):** Get insights into your project's dependencies, visualize their tree, identify potential security vulnerabilities, or simply list them out cleanly. Works across `npm`, `yarn`, and `pnpm`.
*   **Code Snippet Generation (`snippet`):** Generate common code constructs (e.g., React components, Redux reducers, basic function skeletons) directly into your files. No more copy-pasting from old projects!
*   **Configuration Management:** Simple JSON-based configuration to customize templates and behaviors.

---

## Installation

Getting `dev-tools` up and running is straightforward. Since it's built with Node.js, you'll need Node.js and `npm` (or `yarn`, `pnpm`) installed first.

### Prerequisites

Before you install `dev-tools`, make sure you have:

*   **Node.js:** Version 14.x or higher. I typically recommend using the latest LTS version.
    *   You can download it from [nodejs.org](https://nodejs.org/) or use a version manager like `nvm`.
*   **npm (Node Package Manager):** Usually bundled with Node.js.
    *   Alternatively, `yarn` (v1.x or v2+) or `pnpm` are fully supported.

You can check your Node.js and npm versions with:

```bash
node -v
npm -v
```

### Installation Steps

Once your prerequisites are met, install `dev-tools` globally using your preferred package manager. I usually go with `npm`:

```bash
# Using npm
npm install -g @ayat-saadat/dev-tools

# Using yarn
yarn global add @ayat-saadat/dev-tools

# Using pnpm
pnpm install -g @ayat-saadat/dev-tools
```

I chose a scoped package name (`@ayat-saadat/dev-tools`) to make it clear who's behind it and to avoid potential naming conflicts with other tools out there.

### Verifying Installation

To ensure everything is installed correctly, open a new terminal window and run:

```bash
dev-tools --version
```

You should see the installed version number printed to the console. If you get an error like `command not found`, double-check your installation steps and ensure your global `npm` binaries path is in your system's `PATH` environment variable.

---

## Usage

`dev-tools` is designed to be intuitive. Most commands follow a `dev-tools <command> [options]` pattern.

### Basic Commands

Here are some fundamental commands to get you started:

*   **`dev-tools --help`**: Displays a list of all available commands and global options.
*   **`dev-tools <command> --help`**: Provides detailed help for a specific command, including its options and arguments.

```bash
# Get general help
dev-tools --help

# Get help for the 'init' command
dev-tools init --help
```

### `dev-tools init`

The `init` command is your go-to for scaffolding new projects. It's interactive by default, guiding you through template selection and project naming.

```bash
dev-tools init [project-name] [options]
```

**Options:**

| Option         | Shorthand | Description                                           | Type      | Default      |
| :------------- | :-------- | :---------------------------------------------------- | :-------- | :----------- |
| `--template`   | `-t`      | Specify a template (e.g., `react`, `node-api`).     | `string`  | Interactive  |
| `--install`    | `-i`      | Automatically run `npm install` after scaffolding.  | `boolean` | `true`       |
| `--git`        | `-g`      | Initialize a Git repository.                          | `boolean` | `true`       |
| `--dry-run`    | `-d`      | Simulate creation without writing files.              | `boolean` | `false`      |

**Example:**

```bash
# Interactive mode
dev-tools init

# Create a React project named 'my-app' without auto-installing dependencies
dev-tools init my-app --template react --no-install
```

### `dev-tools deps`

This command helps you inspect your project's dependencies. It can be a real lifesaver when you're trying to figure out why a package is there or if you have conflicting versions.

```bash
dev-tools deps [options]
```

**Options:**

| Option        | Shorthand | Description                                               | Type      | Default   |
| :------------ | :-------- | :-------------------------------------------------------- | :-------- | :-------- |
| `--tree`      | `-t`      | Display dependencies as a hierarchical tree.              | `boolean` | `false`   |
| `--depth`     | `-d`      | Max depth for `--tree` view (0 for direct deps only).     | `number`  | `Infinity`|
| `--json`      | `-j`      | Output dependency data as JSON.                           | `boolean` | `false`   |
| `--prod-only` | `-P`      | Only show production dependencies.                        | `boolean` | `false`   |
| `--dev-only`  | `-D`      | Only show development dependencies.                       | `boolean` | `false`   |

**Example:**

```bash
# List all direct dependencies
dev-tools deps

# Show the full dependency tree
dev-tools deps --tree

# Show production dependencies up to depth 2
dev-tools deps --tree --depth 2 --prod-only
```

### `dev-tools snippet`

Need a quick code block? The `snippet` command is perfect for injecting common code patterns into your files or just printing them to the console.

```bash
dev-tools snippet <type> [name] [options]
```

**Arguments:**

*   `<type>`: The type of snippet to generate (e.g., `react-func-comp`, `node-express-route`, `js-async-func`).
*   `[name]`: Optional name for the snippet (e.g., component name, function name).

**Options:**

| Option         | Shorthand | Description                                               | Type      | Default      |
| :------------- | :-------- | :-------------------------------------------------------- | :-------- | :----------- |
| `--output`     | `-o`      | Specify an output file path. Prints to stdout if omitted. | `string`  | `stdout`     |
| `--lang`       | `-l`      | Specify target language (e.g., `js`, `ts`).               | `string`  | `js`         |
| `--overwrite`  | `-w`      | Overwrite the output file if it exists.                   | `boolean` | `false`      |

**Example:**

```bash
# Generate a React functional component to stdout
dev-tools snippet react-func-comp MyComponent

# Generate an async JavaScript function and save it to a file
dev-tools snippet js-async-func fetchData --name getUserData --output src/utils/api.js

# Generate a TypeScript interface
dev-tools snippet ts-interface User --output src/types/User.ts --lang ts
```

---

## Configuration

`dev-tools` can be configured globally or on a per-project basis.

**Global Configuration:**
Located at `~/.config/dev-tools/config.json` (or equivalent for your OS), this file stores default templates, preferred package managers, and other global settings.

**Project-level Configuration:**
You can place a `.devtoolsrc.json` file at the root of your project to override global settings for that specific project.

Here's an example of what your `config.json` or `.devtoolsrc.json` might look like:

```json
{
  "defaultPackageManager": "npm",
  "templates": {
    "react-ts": "https://github.com/ayat-saadat/dev-tools-templates/react-ts-starter",
    "my-custom-node-api": "/path/to/my/local/template"
  },
  "snippetDefaults": {
    "lang": "js",
    "react-func-comp": {
      "extension": ".jsx"
    }
  }
}
```

**Key Configuration Options:**

| Key                     | Type     | Description                                                               | Example Value                       |
| :---------------------- | :------- | :------------------------------------------------------------------------ | :---------------------------------- |
| `defaultPackageManager` | `string` | The package manager `dev-tools` should use for `init --install`.          | `"yarn"`, `"pnpm"`, `"npm"`         |
| `templates`             | `object` | Map of custom template names to their Git URLs or local paths.            | `{"my-tpl": "https://..."}`         |
| `snippetDefaults`       | `object` | Default settings for snippet generation (e.g., default `lang`, extensions). | `{"lang": "ts"}`                    |
| `gitUser`               | `string` | Your default Git username for new project commits.                        | `"Ayat Saadat"`                     |
| `gitEmail`              | `string` | Your default Git email for new project commits.                           | `"ayat@example.com"`                |

---

## Code Examples

Let's walk through some practical use cases to really show `dev-tools` in action.

### Scaffolding a React Project

Imagine you're starting a new React application. Instead of wrestling with `create-react-app` or manually setting up Webpack, just use `dev-tools init`:

```bash
# In your desired parent directory
dev-tools init my-cool-react-app --template react
```

This will:

1.  Create a new directory named `my-cool-react-app`.
2.  Clone the default React template (or your custom one).
3.  Install all `npm` dependencies (unless `--no-install` is specified).
4.  Initialize a Git repository.

You'll see output similar to this:

```
🚀 Initializing new project 'my-cool-react-app'...
  Template: react (https://github.com/ayat-saadat/dev-tools-templates/react-starter)
  Destination: /path/to/my-cool-react-app

✅ Template copied successfully.
📦 Installing dependencies with npm...
  (This might take a moment...)
✅ Dependencies installed.
🌲 Initializing Git repository...
✅ Git repository initialized.

🎉 Your project 'my-cool-react-app' is ready!
   cd my-cool-react-app
   npm start
```

### Analyzing Project Dependencies

Let's say you've joined a new project, and you want to quickly understand its dependency landscape.

```bash
# Inside your project directory
dev-tools deps --tree --depth 1
```

This command will give you a nicely formatted tree view of all direct dependencies and their immediate children. It's super helpful for spotting duplicate packages or unexpected sub-dependencies.

```
📦 Project Dependencies for my-cool-react-app:

├── react@18.2.0
│   └── @babel/runtime@7.23.6
├── react-dom@18.2.0
│   └── scheduler@0.23.