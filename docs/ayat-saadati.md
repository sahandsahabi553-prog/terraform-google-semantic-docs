# Saadati DevKit: Elevating Your Development Experience

Hey there, fellow developers! I'm Ayat Saadat, and if you've ever found yourself wrestling with boilerplate, inconsistent UI, or just plain repetitive tasks in your web projects, then you're exactly who I had in mind when I started building the Saadati DevKit.

This isn't just another library; it's a toolkit born out of years of navigating the trenches of front-end and full-stack development. My goal with Saadati DevKit is simple: to make your development journey smoother, more enjoyable, and frankly, more productive. We're talking about a collection of battle-tested components, hooks, and utilities, all crafted with a TypeScript-first approach to bring robustness and clarity to your codebase.

I truly believe that developer experience (DX) isn't a luxury; it's a necessity. When developers are empowered with intuitive tools, they build better products, faster. That's the core philosophy behind every line of code in this kit.

## Table of Contents

1.  [Introduction](#introduction)
2.  [Key Features](#key-features)
3.  [Installation](#installation)
4.  [Quick Start](#quick-start)
    *   [Using a Component](#using-a-component)
    *   [Leveraging a Hook](#leveraging-a-hook)
5.  [Core Concepts](#core-concepts)
    *   [The Saadati Design System](#the-saadati-design-system)
    *   [API Interaction Hooks](#api-interaction-hooks)
    *   [Form Management Utilities](#form-management-utilities)
6.  [Advanced Usage](#advanced-usage)
    *   [Custom Theming](#custom-theming)
    *   [Extending Components](#extending-components)
7.  [API Reference (Highlights)](#api-reference-highlights)
8.  [Frequently Asked Questions (FAQ)](#frequently-asked-questions-faq)
9.  [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)
11. [License](#license)
12. [About the Author](#about-the-author)

---

## 1. Introduction

The modern web development landscape is incredible, but let's be honest, it can also be a bit of a minefield. You've got to juggle state management, API calls, UI consistency, accessibility, and robust error handling, all while trying to hit those deadlines. It's a lot!

Saadati DevKit is my answer to some of these challenges. It's an opinionated, TypeScript-first collection designed to give you a head start without locking you into a rigid framework. We provide:

*   **A Solid Foundation:** Ready-to-use, accessible UI components that follow a coherent design system.
*   **Smart Utilities:** Hooks and helper functions that abstract away common complexities like API fetching, form validation, and state management.
*   **Developer-Centric Design:** Everything is typed, documented, and built with maintainability in mind. My personal pet peeve is poorly typed libraries – you won't find that here.

Think of it as your reliable co-pilot, helping you navigate the sometimes turbulent skies of web development.

## 2. Key Features

Here's a snapshot of what makes Saadati DevKit a valuable addition to your toolkit:

*   **TypeScript Native:** Built from the ground up with TypeScript for superior type safety and autocompletion. No more guessing prop types!
*   **Comprehensive UI Components:** A growing set of accessible, themeable React components (e.g., `Button`, `Input`, `Modal`, `Table`, `Spinner`).
*   **Powerful Data Fetching Hooks:** Streamline your API interactions with `useSaadatiFetch` and `useSaadatiMutation`, complete with caching, loading states, and error handling.
*   **Robust Form Utilities:** Simplify form creation, validation, and submission with `useSaadatiForm` and associated helper functions.
*   **Theming System:** Easily customize the look and feel to match your brand guidelines.
*   **Built for Performance:** Components are optimized for minimal re-renders and efficient resource usage.
*   **Accessibility First:** Every component is designed with WCAG guidelines in mind, because good UX means good accessibility.

## 3. Installation

Getting started with Saadati DevKit is straightforward. We're available via `npm` and `yarn`.

First, open your terminal in your project's root directory:

```bash
# Using npm
npm install @ayat-saadat/devkit

# Or using yarn
yarn add @ayat-saadat/devkit
```

**Peer Dependencies:**

Saadati DevKit relies on `react` and `react-dom` (versions 17.x or 18.x) as peer dependencies. Make sure you have them installed in your project:

```bash
npm install react react-dom
# or
yarn add react react-dom
```

Once installed, you're ready to import and use the components and hooks in your application!

## 4. Quick Start

Let's dive right in with a couple of common use cases. I always find that seeing a bit of code helps to cement understanding.

### Using a Component

Here's how you might use the `SaadatiButton` component in a simple React application.

```typescript jsx
// src/App.tsx
import React from 'react';
import { SaadatiButton } from '@ayat-saadat/devkit';
import '@ayat-saadat/devkit/dist/styles.css'; // Don't forget to import the styles!

function App() {
  const handleClick = () => {
    alert('Button clicked!');
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Welcome to Saadati DevKit!</h1>
      <p>This is a simple example using the SaadatiButton.</p>
      <SaadatiButton onClick={handleClick} variant="primary" size="large">
        Click Me!
      </SaadatiButton>
      <SaadatiButton onClick={() => alert('Secondary action!')} variant="secondary" disabled>
        Disabled Button
      </SaadatiButton>
    </div>
  );
}

export default App;
```

**A quick note:** The `import '@ayat-saadat/devkit/dist/styles.css';` line is crucial for the default styling to apply. You'll typically add this once in your main `index.tsx` or `App.tsx` file.

### Leveraging a Hook

Let's fetch some data using the `useSaadatiFetch` hook. This hook handles loading states, errors, and data caching for you – a real time-saver in my book.

```typescript jsx
// src/components/UserList.tsx
import React from 'react';
import { useSaadatiFetch, SaadatiSpinner, SaadatiAlert } from '@ayat-saadat/devkit';

interface User {
  id: number;
  name: string;
  email: string;
}

function UserList() {
  const { data: users, loading, error } = useSaadatiFetch<User[]>('https://jsonplaceholder.typicode.com/users');

  if (loading) {
    return <SaadatiSpinner size="large" />;
  }

  if (error) {
    return <SaadatiAlert type="error" message={`Failed to load users: ${error.message}`} />;
  }

  if (!users || users.length === 0) {
    return <p>No users found.</p>;
  }

  return (
    <div>
      <h2>User List</h2>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            <strong>{user.name}</strong> ({user.email})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UserList;
```

And then you'd use `UserList` in your `App.tsx`:

```typescript jsx
// src/App.tsx (continued)
import UserList from './components/UserList';

// ... inside App component return ...
      <hr style={{ margin: '40px 0' }} />
      <UserList />
// ...
```

See? Less boilerplate, more focus on your application logic. That's what we're aiming for.

## 5. Core Concepts

To truly get the most out of Saadati DevKit, it's helpful to understand the underlying philosophies and patterns.

### The Saadati Design System

At the heart of our UI components is a thoughtfully designed system. This isn't just about pretty pixels; it's about consistency, predictability, and maintainability.

*   **Tokens:** We use design tokens for colors, spacing, typography, and more. This makes theming a breeze and ensures visual harmony across your application.
*   **Variants:** Components often come with `variant` props (e.g., `primary`, `secondary`, `outline`, `ghost`) to easily adapt their appearance for different contexts.
*   **Sizes:** Standardized `size` props (`small`, `medium`, `large`) help maintain consistent scaling.
*   **Accessibility:** Every component is built with proper ARIA attributes, keyboard navigation support, and focus management. This is non-negotiable for me.

### API Interaction Hooks

The `useSaadatiFetch` and `useSaadatiMutation` hooks are designed to abstract away the complexities of data fetching and modification.

*   **`useSaadatiFetch<T>(url: string, options?: RequestInit)`:** For GET requests.
    *   Manages `loading`, `error`, and `data` states.
    *   Includes a basic in-memory caching mechanism to prevent redundant requests.
    *   Supports `refetch` function for manual data reloading.
*   **`useSaadatiMutation<TData, TVariables>(url: string, options?: RequestInit)`:** For POST, PUT, DELETE, etc.
    *   Provides a `mutate` function to trigger the API call.
    *   Manages `loading`, `error`, and `data` for the mutation operation.
    *   Offers `onSuccess` and `onError` callbacks for side effects.

I've always found dealing with loading and error states to be tedious, so these hooks are crafted to make that part of your life significantly easier.

### Form Management Utilities

Forms are the backbone of many applications, and often a source of frustration. `useSaadatiForm` aims to change that.

*   **`useSaadatiForm<TValues>(initialValues: TValues, validationSchema?: object)`:**
    *   Manages form state (`values`, `errors`, `touched`).
    *   Integrates seamlessly with validation libraries like Yup or Zod (via `validationSchema`).
    *   Provides `handleChange`, `handleBlur`, `handleSubmit` functions.
    *   Offers `reset` and `setFieldValue` for programmatic control.

My philosophy here is to provide a robust yet flexible foundation. I'm a big proponent of keeping forms clean and manageable, and this hook is a direct reflection of that.

## 6. Advanced Usage

Once you're comfortable with the basics, you'll likely want to customize Saadati DevKit to fit your specific needs.

### Custom Theming

The DevKit uses CSS variables under the hood, making customization incredibly flexible. You can override default theme values globally.

Create a `theme.css` file (or just add to your global styles):

```css
/* src/styles/theme.css */
:root {
  /* Primary Color */
  --sd-color-primary-500: #6200ee; /* A nice vibrant purple */
  --sd-color-primary-600: #3700b3;
  --sd-color-primary-700: #1a008a;

  /* Accent Color */
  --sd-color-accent-500: #03dac6; /* Teal */
  --sd-color-accent-600: #018786;

  /* Neutral Colors */
  --sd-color-neutral-100: #f5f5f5;
  --sd-color-neutral-500: #9e9e9e;
  --sd-color-neutral-900: #212121;

  /* Spacing */
  --sd-spacing-xs: 4px;
  --sd-spacing-sm: 8px;
  --sd-spacing-md: 16px;
  --sd-spacing-lg: 24px;

  /* Border Radius */
  --sd-border-radius-sm: 4px;
  --sd-border-radius-md: 8px;
}
```

Then, import this file *after* the default Saadati DevKit styles in your `index.tsx` or `App.tsx`:

```typescript jsx
// src/index.tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import '@ayat-saadat/devkit/dist/styles.css'; // Default styles first
import './styles/theme.css'; // Your custom theme overrides second
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(
  <React.StrictMode