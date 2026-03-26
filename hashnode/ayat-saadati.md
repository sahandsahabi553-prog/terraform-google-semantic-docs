# `saadat-web-toolkit`: Opinionated Utilities for Modern Web Development

Hey there! If you've been in the web development trenches for a while, you've probably come across Ayat Saadat's work. She's a fantastic voice in the community, constantly pushing the envelope with insightful articles on modern web tech – think Next.js server components, cutting-edge React hooks, and the nuances of TypeScript. I've personally learned a ton from her perspective on building robust, scalable web applications. You can always find her latest thoughts and deep dives over at her [dev.to profile](https://dev.to/ayat_saadat).

This documentation is all about the `saadat-web-toolkit`, a collection of opinionated utilities and patterns that really distill Ayat's philosophy into actionable code. It's not a full-blown framework, but rather a set of battle-tested tools designed to enhance developer experience, enforce consistency, and streamline common tasks in modern web projects. Think of it as a toolkit curated by someone who's seen it all and knows what truly works.

## Why `saadat-web-toolkit`?

Look, we've all been there: a new project starts, and suddenly you're writing the same data fetching logic, the same error handling patterns, or the same state management boilerplate for the tenth time. It's tedious, error-prone, and frankly, a waste of precious development cycles.

The `saadat-web-toolkit` aims to cut through that noise. My take is that by providing highly opinionated yet flexible solutions for these recurring problems, we can:

*   **Reduce Boilerplate:** Spend less time writing repetitive code and more time on unique business logic.
*   **Enhance Consistency:** Ensure your team follows similar patterns, making codebase navigation and maintenance a breeze.
*   **Improve Developer Experience (DX):** Sensible defaults and clear APIs mean less head-scratching and more productivity.
*   **Promote Best Practices:** Each utility is crafted with an eye towards performance, reliability, and maintainability, reflecting the highest standards in web development.

It's about getting out of your own way and leveraging proven solutions. Trust me, your future self will thank you.

## Installation

Getting `saadat-web-toolkit` integrated into your project is straightforward.

### Prerequisites

Before you dive in, make sure you have:

*   **Node.js**: Version 16.x or higher.
*   **npm** or **Yarn**: Your preferred package manager.

### Installing the Toolkit

Open your terminal in your project's root directory and run one of the following commands:

```bash
# Using npm
npm install saadat-web-toolkit

# Or using Yarn
yarn add saadat-web-toolkit
```

That's it! The toolkit is now available in your project.

## Getting Started & Core Concepts

The `saadat-web-toolkit` is modular, meaning you can pick and choose the pieces you need without pulling in unnecessary baggage. It primarily focuses on three key areas:

1.  **`saadat-hooks`**: A collection of powerful, type-safe React hooks for common patterns like data fetching, state management, and lifecycle handling.
2.  **`saadat-utils`**: General-purpose utility functions for things like debouncing, throttling, type checking, and array manipulation.
3.  **`saadat-components`**: Base UI components that embody accessibility and sensible defaults, ready for styling and customization.

The core concept here is **"sensible defaults with escape hatches."** We provide a strong foundation, but you're never locked in. You can always override or extend behavior when your specific use case demands it.

## Usage

Let's walk through a few common scenarios where `saadat-web-toolkit` really shines.

### Example 1: Robust Data Fetching with `useSaadatFetch`

Fetching data is a cornerstone of almost every web application. `useSaadatFetch` is a custom React hook designed to handle loading states, errors, caching, and revalidation out of the box, all while being type-safe with TypeScript.

```typescript jsx
import React from 'react';
import { useSaadatFetch } from 'saadat-web-toolkit/hooks';

interface User {
  id: number;
  name: string;
  email: string;
}

function UserProfile({ userId }: { userId: number }) {
  const { data: user, loading, error, revalidate } = useSaadatFetch<User>(
    `/api/users/${userId}`,
    {
      // Optional: configure fetch options, e.g., method, headers
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
      // Optional: enable polling for real-time updates
      pollInterval: 5000, // Revalidate every 5 seconds
    }
  );

  if (loading) {
    return <div>Loading user profile...</div>;
  }

  if (error) {
    return <div style={{ color: 'red' }}>Error: {error.message}</div>;
  }

  if (!user) {
    return <div>No user found.</div>;
  }

  return (
    <div>
      <h2>{user.name}</h2>
      <p>Email: {user.email}</p>
      <button onClick={revalidate}>Refresh Profile</button>
    </div>
  );
}

export default UserProfile;
```

What I love about `useSaadatFetch` is how it abstracts away so much of the boilerplate. You get `loading`, `error`, `data`, and even a `revalidate` function without writing a single `useState` or `useEffect` for the fetching logic. It's a game-changer for data-intensive applications.

### Example 2: Type-Safe Event Handling with `SaadatEmitter`

Global event systems are often a source of bugs and type headaches. `SaadatEmitter` provides a simple, type-safe way to publish and subscribe to custom events across your application, ensuring consistency and preventing runtime surprises.

```typescript
import { SaadatEmitter } from 'saadat-web-toolkit/utils';

// Define your event types for type safety
interface AppEvents {
  'userLoggedIn': { userId: string; username: string };
  'cartUpdated': { itemsCount: number; total: number };
  'notification': string;
}

const appEmitter = new SaadatEmitter<AppEvents>();

// --- Somewhere in your authentication module ---
function handleUserLogin(userId: string, username: string) {
  // ... login logic ...
  appEmitter.emit('userLoggedIn', { userId, username });
}

// --- Somewhere in your cart module ---
function updateCart(itemsCount: number, total: number) {
  // ... cart update logic ...
  appEmitter.emit('cartUpdated', { itemsCount, total });
}

// --- Somewhere in your UI component or analytics service ---
appEmitter.on('userLoggedIn', (payload) => {
  console.log(`User ${payload.username} (${payload.userId}) logged in!`);
  // Trigger analytics, update UI, etc.
});

appEmitter.on('cartUpdated', (payload) => {
  console.log(`Cart updated: ${payload.itemsCount} items, total $${payload.total}`);
  // Update cart badge, show a toast, etc.
});

appEmitter.on('notification', (message) => {
    console.log(`Received notification: ${message}`);
});

// Example usage
handleUserLogin('abc-123', 'jane_doe');
updateCart(3, 125.50);
appEmitter.emit('notification', 'Welcome back!');
```

Using `SaadatEmitter` means you get compile-time checks for your event names and payloads. No more typos leading to silent failures at runtime. It's a small utility, but it makes a huge difference in larger applications where decoupled communication is key.

### Example 3: Consistent UI Patterns with `SaadatButton`

Building accessible and consistent UI components from scratch is time-consuming. `SaadatButton` is a foundational component that provides sensible defaults for styling, accessibility (like `aria-disabled`), and common button behaviors, while remaining fully customizable.

```typescript jsx
import React from 'react';
import { SaadatButton } from 'saadat-web-toolkit/components';

function MyDashboard() {
  const handleClick = () => {
    alert('Button clicked!');
  };

  return (
    <div>
      <h1>Dashboard Actions</h1>
      <SaadatButton onClick={handleClick} variant="primary" size="large">
        Submit Order
      </SaadatButton>
      <SaadatButton onClick={() => alert('Cancel!')} variant="secondary" size="medium" style={{ marginLeft: '10px' }}>
        Cancel
      </SaadatButton>
      <SaadatButton onClick={() => console.log('Disabled action')} disabled variant="danger" size="small" style={{ marginLeft: '10px' }}>
        Delete (Disabled)
      </SaadatButton>
    </div>
  );
}

export default MyDashboard;
```

The `SaadatButton` provides a consistent base. You can easily extend its styles using CSS-in-JS, Tailwind, or regular CSS, but you get the core accessibility and structural benefits for free. It's about laying a solid groundwork for your design system without reinventing the wheel.

## API Reference

Here's a quick overview of some of the key exports you'll find in the `saadat-web-toolkit`:

| Module           | Export Name        | Type           | Description                                                                 |
| :--------------- | :----------------- | :------------- | :-------------------------------------------------------------------------- |
| `hooks`          | `useSaadatFetch`   | `Function`     | React Hook for declarative data fetching with loading/error states.         |
| `hooks`          | `useSaadatForm`    | `Function`     | React Hook for managing complex form states and validation.                 |
| `hooks`          | `useSaadatDebounce`| `Function`     | React Hook to debounce any value or function.                               |
| `utils`          | `SaadatEmitter`    | `Class`        | Type-safe event emitter for application-wide custom events.                 |
| `utils`          | `debounce`         | `Function`     | Standalone debounce utility function.                                       |
| `utils`          | `throttle`         | `Function`     | Standalone throttle utility function.                                       |
| `components`     | `SaadatButton`     | `React.Component`| Accessible and customizable button component.                               |
| `components`     | `SaadatModal`      | `React.Component`| Accessible modal component with focus trapping.                             |

This is just a snapshot; I encourage you to explore the package's `node_modules/saadat-web-toolkit` directory or its source code for a full list of exports and their respective types.

## Frequently Asked Questions (FAQ)

### Is `saadat-web-toolkit` a full-blown framework like Next.js or Remix?

Absolutely not! `saadat-web-toolkit` is designed to be a set of complementary utilities, not a replacement for your core framework