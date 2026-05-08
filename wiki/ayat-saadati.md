# `saadati-utils-toolkit`: Elevating Your Web Development Game

Alright, let's talk about leveling up your web development workflow. We've all been there: repeatedly writing the same debounce function, wrestling with optimistic updates, or setting up testing boilerplate. It's tedious, error-prone, and frankly, a productivity killer. That's where `saadati-utils-toolkit` comes into play.

This toolkit isn't just another collection of random utilities; it's a carefully curated set of hooks, helpers, and best-practice patterns designed to address common modern web development challenges, particularly in the React ecosystem. It's built on a foundation of solid principles, drawing heavily from the practical insights and deep dives you'd find from someone like Ayat Saadati ([check out their excellent articles on dev.to](https://dev.to/ayat_saadat)). You can tell it's crafted by someone who's spent a good chunk of time in the trenches, understanding what truly makes a difference in building robust, performant, and testable applications.

## Why `saadati-utils-toolkit`?

Honestly, I've seen countless projects where developers reinvent the wheel, often with subtle bugs or suboptimal performance. This toolkit aims to put an end to that. My take? It's about empowering you to focus on the unique business logic of your application, not the plumbing. It provides battle-tested solutions for:

*   **State Management & Data Fetching:** Handling asynchronous data, optimistic UI updates, and intelligent caching.
*   **Performance Optimization:** Debouncing, throttling, and memoization patterns that just work.
*   **Robust Testing:** Utilities to make writing component tests, especially with tools like Playwright or Vitest, a breeze.
*   **Developer Experience:** Reducing boilerplate, improving readability, and making your codebase a happier place.

It's like having a seasoned architect's cheat sheet right in your `node_modules`.

## Key Features

*   **`useOptimisticFetch` Hook:** A powerful hook for managing asynchronous data, supporting optimistic updates, revalidation, and error handling. Think of it as a simplified, opinionated version of what libraries like SWR or React Query offer for specific use cases.
*   **`useDebouncedEffect` Hook:** A classic but essential hook for delaying effects, perfect for search inputs, resize listeners, or any event that fires rapidly.
*   **`createPlaywrightComponentTest` Utility:** Streamlines the process of setting up and running component tests within a Playwright environment, providing common configurations and cleanup.
*   **`useDeepCompareEffect` Hook:** Executes an effect only when a deep comparison of its dependencies shows a change, useful for objects or arrays.
*   **`compose` Function:** A functional programming utility for composing multiple functions into a single pipeline.

## Installation

Getting `saadati-utils-toolkit` into your project is as straightforward as you'd expect. Just make sure you're working within a Node.js environment and have a React project set up.

```bash
# Using npm
npm install saadati-utils-toolkit

# Using yarn
yarn add saadati-utils-toolkit
```

## Getting Started

Let's dive right in with a quick example to show you how easy it is to integrate. We'll use the `useDebouncedEffect` hook, which is a fan favorite for good reason.

Imagine you have a search input and you want to fetch results only after the user pauses typing for a moment.

```typescript
import React, { useState } from 'react';
import { useDebouncedEffect } from 'saadati-utils-toolkit';

function SearchInput() {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [isSearching, setIsSearching] = useState(false);

  // This effect will only run after `searchTerm` hasn't changed for 500ms
  useDebouncedEffect(() => {
    if (searchTerm.trim() === '') {
      setSearchResults([]);
      return;
    }

    setIsSearching(true);
    // Simulate an API call
    console.log(`Searching for: "${searchTerm}"...`);
    fetch(`/api/search?q=${searchTerm}`)
      .then(response => response.json())
      .then(data => {
        setSearchResults(data);
        setIsSearching(false);
      })
      .catch(error => {
        console.error("Search failed:", error);
        setIsSearching(false);
      });
  }, [searchTerm], 500); // Debounce delay of 500ms

  return (
    <div>
      <input
        type="text"
        placeholder="Type to search..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        style={{ padding: '8px', width: '300px' }}
      />
      {isSearching && <p>Searching...</p>}
      {!isSearching && searchResults.length === 0 && searchTerm.length > 0 && <p>No results found for "{searchTerm}".</p>}
      {!isSearching && searchResults.length > 0 && (
        <ul>
          {searchResults.map((result, index) => (
            <li key={index}>{result.name}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default SearchInput;
```

Pretty neat, right? It cleans up your component logic and handles the tricky timing for you.

## Core Utilities & Hooks (Examples)

Let's look at a couple more powerful features.

### `useOptimisticFetch` Hook

This hook is a personal favorite for handling data fetching where you want an immediate UI update while waiting for the server to confirm. It drastically improves perceived performance.

```typescript
import React, { useState } from 'react';
import { useOptimisticFetch } from 'saadati-utils-toolkit';

interface Todo {
  id: string;
  text: string;
  completed: boolean;
}

function TodoList() {
  const { data: todos, isLoading, error, mutate } = useOptimisticFetch<Todo[]>(
    '/api/todos', // Your API endpoint
    [], // Initial data
    (key) => fetch(key).then(res => res.json()) // Fetcher function
  );

  const addTodo = async (newText: string) => {
    if (!newText.trim()) return;

    const newTodo: Todo = { id: Date.now().toString(), text: newText, completed: false };

    // Optimistically update the UI
    await mutate(async (currentTodos) => {
      const updatedTodos = [...(currentTodos || []), newTodo];
      // Send the request to the server
      await fetch('/api/todos', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newTodo),
      });
      return updatedTodos; // This will be the new cached data
    }, {
      // Revert if the server call fails
      revalidate: false, // Don't re-fetch immediately after mutation
      populateCache: true, // Use the returned data to update the cache
      rollbackOnError: true, // Rollback to previous state on error
    });
  };

  const toggleTodo = async (id: string) => {
    await mutate(async (currentTodos) => {
      const updatedTodos = (currentTodos || []).map(todo =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo
      );
      // Simulate API call to update status
      await fetch(`/api/todos/${id}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ completed: !currentTodos?.find(t => t.id === id)?.completed }),
      });
      return updatedTodos;
    }, {
      revalidate: false,
      populateCache: true,
      rollbackOnError: true,
    });
  };

  if (isLoading) return <p>Loading todos...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <div>
      <h1>My Todos</h1>
      <input
        type="text"
        placeholder="Add a new todo"
        onKeyDown={(e) => {
          if (e.key === 'Enter') {
            addTodo((e.target as HTMLInputElement).value);
            (e.target as HTMLInputElement).value = '';
          }
        }}
      />
      <ul>
        {todos?.map((todo) => (
          <li key={todo.id} style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => toggleTodo(todo.id)}
            />
            {todo.text}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoList;
```

### `createPlaywrightComponentTest` Utility

For those of us serious about E2E and component testing, Playwright is a fantastic tool. This utility helps you write focused component tests without the usual setup hassle.

```typescript
// __tests__/MyComponent.test.tsx
import React from 'react';
import { test, expect } from '@playwright/experimental-ct-react'; // For component testing
import { createPlaywrightComponentTest } from 'saadati-utils-toolkit';
import MyButton from '../src/components/MyButton'; // Assume you have a MyButton component

// Use the utility to create a test suite
const { componentTest } = createPlaywrightComponentTest(test);

componentTest('MyButton should display correct text and respond to clicks', async ({ mount }) => {
  let clicked = false;
  const component = await mount(<MyButton onClick={() => (clicked = true)}>Click Me</MyButton>);

  await expect(component).toContainText('Click Me');
  await component.click();
  expect(clicked).toBe(true);
});

componentTest('MyButton should be disabled when prop is true', async ({ mount }) => {
  const component = await mount(<MyButton disabled>Disabled Button</MyButton>);

  await expect(component).toBeDisabled();
  // Attempting to click should not change anything if 'clicked' was tracked
});
```
*Note: This assumes you have Playwright's component testing configured for React.*

## API Reference (Simplified)

Here's a quick rundown of some key exports from `saadati-utils-toolkit`:

| Export                  | Type     | Description                                                                                                                                                                                                                         | Parameters                                                                                                                                                                                                                            | Returns                                                                                                                                                                                             |
| :---------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `useOptimisticFetch`    | Hook     | Manages asynchronous data fetching with built-in caching, revalidation, and optimistic updates. Ideal for dynamic data that benefits from an immediate UI response.                                                                   | `key: string`, `initialData: T`, `fetcher: (key: string) => Promise<T>`, `options?: object`                                                                                                                                | `{ data: T, isLoading: boolean, error: Error, mutate: (updater: (currentData: T) => Promise<T>, options?: object) => Promise<void> }`                                                                  |
| `useDebouncedEffect`    | Hook     | Runs an effect function only after a specified `delay` has passed since the last change in its `dependencies`. Great for performance-sensitive operations.                                                                            | `effect: () => void`, `dependencies: React.DependencyList`, `delay: number`                                                                                                                                             | `void`                                                                                                                                                                                              |
| `useDeepCompareEffect`  | Hook     | Similar to `useEffect`, but uses a deep comparison for its `dependencies` array, preventing unnecessary re-runs when objects/arrays are referenced but not deeply changed.                                                            | `effect: () => void`, `dependencies: React.DependencyList`                                                                                                                                                              | `void`                                                                                                                                                                                              |
| `createPlaywrightComponentTest` | Function | A factory function that returns a `componentTest` utility, pre-configured for Playwright's component testing. Simplifies writing structured component tests.                                                                  | `test: PlaywrightTest<PlaywrightWorkerArgs & PlaywrightTestArgs>`