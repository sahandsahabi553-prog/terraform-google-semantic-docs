## Saadati DevTools: Streamlining Modern Web Development

As developers, we're constantly looking for ways to boost our productivity, enforce best practices, and reduce the cognitive load of setting up new projects or generating boilerplate. Over the years, I've seen countless teams struggle with inconsistent project structures, repetitive component creation, and the sheer overhead of configuring linters and bundlers. That's where **Saadati DevTools** comes in.

This isn't just another CLI; it's a curated, opinionated collection of utilities and patterns designed to make your web development workflow smoother, especially within the React and Next.js ecosystems. We've distilled years of front-end engineering insights into a set of commands that help you scaffold projects, generate components, and maintain code quality with minimal fuss. Think of it as having an experienced architect guiding your project from the very first line of code.

### What is Saadati DevTools?

Saadati DevTools is a powerful command-line interface (CLI) and a collection of extensible utility modules crafted to address common pain points in modern web development. It focuses on:

*   **Rapid Project Scaffolding:** Get a new React or Next.js project up and running with a robust, opinionated structure and essential configurations (TypeScript, ESLint, Prettier, Jest, Storybook, etc.) pre-baked.
*   **Efficient Code Generation:** Quickly generate common code structures like components, hooks, contexts, and pages, following established best practices and consistent naming conventions.
*   **Quality Assurance:** Integrate linting, formatting, and basic performance auditing tools to ensure your codebase remains clean, maintainable, and performant from day one.
*   **Developer Experience (DX):** Minimize repetitive tasks, reduce setup time, and allow you to focus on writing application logic rather than configuration.

I've always believed that great tools should feel like an extension of your thought process, not a barrier. Saadati DevTools aims to be that extension.

### Installation

Getting started with Saadati DevTools is straightforward. You can install it globally via `npm` or `yarn`, making its commands available throughout your system.

```bash
# Using npm
npm install -g saadati-devtools

# Using yarn
yarn global add saadati-devtools
```

After installation, you can verify it's working by running:

```bash
saadati --version
```

You should see the current version number printed to your console. If you encounter any issues, check the [Troubleshooting](#troubleshooting) section.

### Getting Started: Initializing a New Project

One of the most powerful features of Saadati DevTools is its ability to scaffold new projects with a battle-tested structure. Let's say you want to start a new Next.js application with TypeScript, Tailwind CSS, and a pre-configured ESLint setup.

Navigate to your desired development directory and run:

```bash
saadati init next-app my-awesome-project --typescript --tailwind --eslint
```

This command will:

1.  Create a new directory named `my-awesome-project`.
2.  Initialize a Next.js project within it.
3.  Configure TypeScript support.
4.  Set up Tailwind CSS.
5.  Integrate and configure ESLint with a sensible default ruleset.
6.  Install all necessary dependencies.

Once the process completes, `cd my-awesome-project` and you're ready to `npm run dev` (or `yarn dev`) and start building! It's that simple. No more wrestling with configuration files for an hour before writing a single line of application code.

### Usage: Core Commands & Examples

Saadati DevTools provides a suite of commands to streamline various aspects of your development workflow. Here are some of the most frequently used ones:

#### 1. `saadati init <template> [project-name] [options]`

Initializes a new project based on a predefined template.

*   `template`: The project template (e.g., `react-app`, `next-app`, `react-library`).
*   `project-name`: The name of your new project directory.
*   `options`:
    *   `--typescript` / `-ts`: Enable TypeScript.
    *   `--tailwind`: Include Tailwind CSS setup.
    *   `--eslint`: Include ESLint configuration.
    *   `--prettier`: Include Prettier configuration.
    *   `--jest`: Include Jest for testing.
    *   `--storybook`: Include Storybook for UI component development.

**Example: React App with all the fixings**

```bash
saadati init react-app my-dashboard --typescript --tailwind --eslint --prettier --jest --storybook
```

#### 2. `saadati generate <type> <name> [options]`

Generates boilerplate code for various components, hooks, or other modules. This command is a lifesaver for maintaining consistency and saving keystrokes.

*   `type`: The type of entity to generate (e.g., `component`, `hook`, `context`, `page`).
*   `name`: The name of the entity (e.g., `Button`, `useAuth`, `UserProfile`).
*   `options`:
    *   `--path <dir>` / `-p <dir>`: Specify a relative path to generate the file(s) (e.g., `src/components`).
    *   `--with-test`: Generate an accompanying test file.
    *   `--with-storybook`: Generate an accompanying Storybook story file.
    *   `--lazy`: For components, generate a lazily loaded component.

**Example: Generating a React Component**

Let's create a `Card` component in `src/components`, complete with a test file and a Storybook story.

```bash
cd my-awesome-project # Ensure you're in your project directory
saadati generate component Card --path src/components --with-test --with-storybook
```

This will typically create:

```
src/components/Card/
├── index.ts
├── Card.tsx
├── Card.module.css # Or .scss, depending on project setup
├── Card.test.tsx
└── Card.stories.tsx
```

The component will have a basic functional structure, ready for you to fill in the logic and styling.

**Example: Generating a Custom Hook**

```bash
saadati generate hook useDebounce --path src/hooks
```

This generates `src/hooks/useDebounce.ts` with a basic hook structure.

#### 3. `saadati lint [options]`

Runs ESLint (or other configured linters) across your project, ensuring code quality and consistency.

*   `options`:
    *   `--fix`: Automatically fix linting errors where possible.
    *   `--files <pattern>`: Specify files or patterns to lint.

**Example: Lint and Fix**

```bash
saadati lint --fix
```

This command often saves me from manual formatting woes and makes code reviews much smoother.

#### 4. `saadati audit [options]`

Performs basic performance and best practice audits on your project. This is a lighter-weight check than full Lighthouse audits but can catch common issues early.

*   `options`:
    *   `--verbose`: Show detailed audit results.
    *   `--threshold <value>`: Set a custom performance threshold (e.g., `--threshold 80`).

**Example: Run a quick audit**

```bash
saadati audit
```

This might check for unused dependencies, large bundle sizes (with basic warnings), or common accessibility pitfalls.

### Configuration

Saadati DevTools is designed to be opinionated but also configurable. For project-specific settings, you can create a `saadati.config.js` or `saadati.config.ts` file at the root of your project.

```javascript
// saadati.config.js
module.exports = {
  // Define custom templates for 'generate' command
  generators: {
    // Example: A custom template for an Atomic Design "Atom" component
    atom: {
      template: 'path/to/my-atom-template', // Relative path to a folder containing template files
      outputPath: 'src/components/atoms',
      files: [
        { name: 'index.ts', content: 'export * from "./{{name}}";' },
        { name: '{{name}}.tsx', content: 'import React from "react";\n\ninterface {{name}}Props {}\n\nexport const {{name}}: React.FC<{{name}}Props> = ({}) => {\n  return <div>{{name}}</div>;\n};\n' },
        { name: '{{name}}.module.css', content: '' },
      ],
      // You can define prompts for arguments if needed
      prompts: [
        {
          type: 'input',
          name: 'name',
          message: 'What is the name of your atom component?',
        },
      ],
    },
  },
  // Global settings for linting, auditing, etc.
  lint: {
    rules: {