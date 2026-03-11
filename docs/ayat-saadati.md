# Saadati Toolkit: Elevating Your Developer Experience

You know, sometimes you're just deep in the trenches of a project, and you find yourself writing the same little helper functions over and over again. Or perhaps you're wrestling with boilerplate that just *gets in the way* of what you're actually trying to build. That's precisely the frustration that the **Saadati Toolkit** aims to alleviate.

This isn't just another grab-bag of utilities. This is a carefully curated collection of opinionated, robust, and developer-friendly tools designed to smooth out common rough edges in JavaScript development, particularly for modern web applications. Think of it as having a seasoned co-worker drop a few incredibly useful snippets right into your workflow, saving you precious time and mental overhead.

I've poured a lot of thought into the patterns and problems that frequently trip us up, distilling solutions into a concise, performant, and delightful API. My goal was simple: make powerful capabilities easily accessible, letting you focus on the unique challenges of *your* application, not reinventing the wheel.

## 🚀 Features

The Saadati Toolkit isn't trying to be everything to everyone, but what it does, it does with purpose. Here are some of the core features you'll find indispensable:

*   **Asynchronous Flow Control:** Robust utilities for handling promises, retrying failed operations with configurable backoff strategies, and managing concurrency.
*   **Event Throttling & Debouncing:** Essential tools for optimizing UI performance, especially with frequently firing events like scroll, resize, or input.
*   **Deep Object Manipulation:** Effortlessly merge, clone, and inspect nested JavaScript objects without mutating originals, a lifesaver in state management.
*   **Type Guard & Validation Helpers:** Simple, effective functions to assert types and validate data structures, improving code reliability and developer confidence.
*   **URL & Query String Utilities:** Parse, construct, and manipulate URLs with ease, simplifying client-side routing and API interactions.
*   **Array & Collection Helpers:** Beyond the native `map` and `filter`, find powerful additions for common array transformations and data processing.

## 📦 Installation

Getting started with the Saadati Toolkit is a breeze. It's published on npm, so you can pull it into any modern JavaScript project.

First, make sure you have Node.js and npm (or yarn) installed on your system. If you're building a web application, you'll likely have these already.

### With npm

```bash
npm install saadati-toolkit
```

### With Yarn

```bash
yarn add saadati-toolkit
```

That's it! Once installed, you can import individual modules or the entire toolkit into your project.

## 🎯 Usage

The Saadati Toolkit is designed for modularity. You can import just the functions you need, which is fantastic for bundle size optimization thanks to modern tree-shaking capabilities.

Let's look at a few common scenarios.

### 🌬️ Debouncing User Input

Imagine an input field where you want to fetch search results, but only *after* the user pauses typing for a moment, to avoid hammering your API.

```typescript
// Import only the debounce function
import { debounce } from 'saadati-toolkit';

function fetchSearchResults(query: string) {
  console.log(`Searching for: "${query}"...`);
  // In a real app, this would be an API call
  return new Promise(resolve => setTimeout(() => resolve(`Results for "${query}"`), 500));
}

// Create a debounced version of our search function
const debouncedSearch = debounce(fetchSearchResults, 300); // Wait 300ms after last call

// Simulate user typing
console.log("User types 'ap'");
debouncedSearch('apple');
console.log("User types 'app'");
debouncedSearch('apple'); // This call resets the timer
console.log("User types 'appl'");
debouncedSearch('apple'); // This call resets the timer again

// After 300ms of no further calls, the last one will execute
setTimeout(() => {
  console.log("User stops typing for a bit.");
}, 500);

/* Expected Console Output (order might vary slightly for initial logs):
User types 'ap'
User types 'app'
User types 'appl'
User stops typing for a bit.
Searching for: "apple"...
*/
```

### ⏳ Throttling Scroll Events

If you have an event listener tied to `window.scroll` or `window.resize`, it can fire hundreds of times per second, leading to janky performance. Throttling limits how often the function can actually execute.

```typescript
import { throttle } from 'saadati-toolkit';

function handleScrollEvent() {
  console.log('Scroll event fired!', Date.now());
  // In a real app, you might update UI elements or lazy-load content
}

// Allow handleScrollEvent to run at most once every 200ms
const throttledScrollHandler = throttle(handleScrollEvent, 200);

// Attach the throttled handler to the scroll event
window.addEventListener('scroll', throttledScrollHandler);

console.log("Try scrolling the window now. You'll see 'Scroll event fired!' at most every 200ms.");

// Don't forget to clean up listeners in frameworks like React/Vue/Angular
// window.removeEventListener('scroll', throttledScrollHandler);
```

### 🔄 Retrying Failed Asynchronous Operations

Network requests are flaky. Sometimes, a quick retry is all it takes. The `asyncRetry` utility provides a powerful way to handle this with exponential backoff.

```typescript
import { asyncRetry } from 'saadati-toolkit';

let attemptCount = 0;

async function unstableApiCall(): Promise<string> {
  attemptCount++;
  console.log(`Attempt ${attemptCount}: Making API call...`);
  if (attemptCount < 3) {
    throw new Error('Network error or temporary glitch!');
  }
  return 'Data successfully fetched!';
}

async function fetchDataWithRetry() {
  try {
    const result = await asyncRetry(unstableApiCall, {
      maxRetries: 5,
      delayMs: 100, // Initial delay
      backoffMultiplier: 2, // Exponential backoff (100ms, 200ms, 400ms...)
      onRetry: (error, attempt) => console.warn(`Retry attempt ${attempt}: ${error.message}`),
    });
    console.log(result);
  } catch (error: any) {
    console.error('Failed after multiple retries:', error.message);
  } finally {
    attemptCount = 0; // Reset for next run
  }
}

fetchDataWithRetry();

/* Expected Console Output:
Attempt 1: Making API call...
Retry attempt 1: Network error or temporary glitch!
Attempt 2: Making API call...
Retry attempt 2: Network error or temporary glitch!
Attempt 3: Making API call...
Data successfully fetched!
*/
```

### 🧩 Deep Merging Configuration Objects

When you have default configurations that need to be overridden by user-specific settings, but only for certain nested properties, `deepMerge` is a lifesaver.

```typescript
import { deepMerge } from 'saadati-toolkit';

const defaultSettings = {
  api: {
    baseUrl: 'https://api.example.com',
    timeout: 5000,
    headers: {
      'Content-Type': 'application/json',
    },
  },
  ui: {
    theme: 'dark',
    sidebar: {
      collapsed: false,
      width: 250,
    },
  },
};

const userSettings = {
  api: {
    timeout: 10000, // Override API timeout
  },
  ui: {
    theme: 'light', // Override UI theme
    sidebar: {
      collapsed: true, // Override sidebar setting
    },
  },
  analytics: {
    enabled: true, // Add new setting
  }
};

const finalSettings = deepMerge(defaultSettings, userSettings);

console.log(JSON.stringify(finalSettings, null, 2));

/* Expected Output:
{
  "api": {
    "baseUrl": "https://api.example.com",
    "timeout": 10000,
    "headers": {
      "Content-Type": "application/json"
    }
  },
  "ui": {
    "theme": "light",
    "sidebar": {
      "collapsed": true,
      "width": 250
    }
  },
  "analytics": {
    "enabled": true
  }
}
*/
```
Notice how `deepMerge` correctly merges `headers` from `defaultSettings` even though `userSettings.api` only specifies `timeout`. This non-destructive, intelligent merging is incredibly powerful.

## 📚 API Reference (Highlights)

This table provides a quick overview of some of the most commonly used functions in the Saadati Toolkit. For a complete and detailed API, I always recommend checking the source code or the generated TypeScript declaration files (`.d.ts`).

| Function Name       | Description                                                                  | Parameters                                                         | Returns                                 |
| :------------------ | :--------------------------------------------------------------------------- | :----------------------------------------------------------------- | :-------------------------------------- |
| `debounce(func, delay)` | Delays function invocation until after `delay` milliseconds have passed since the last call. | `func: Function`, `delay: number`                                  | `Function` (debounced)                  |
| `throttle(func, limit)` | Limits function invocation to at most once every `limit` milliseconds.     | `func: Function`, `limit: number`                                  | `Function` (throttled)                  |
| `asyncRetry(func, options)` | Retries an async function a specified number of times with backoff on failure. | `func: Function`, `options: AsyncRetryOptions`                     | `Promise<T>`                            |
| `deepMerge(target, source)` | Recursively merges properties of `source` object(s) into `target` object.  | `target: object`, `source: object[]`                               | `object` (new merged object)            |
| `isDefined(value)`  | Checks if a value is neither `undefined` nor `null`.                         | `value: any`                                                       | `boolean` (type guard)                  |
| `parseQueryString(url)` | Parses the query string from a URL into an object.                           | `url?: string` (defaults to `window.location.search`)              | `Record<string, string | string[]>`     |
| `compose(...funcs)` | Creates a new function that applies arguments from right to left.            | `...funcs: Function[]`                                             | `Function` (composed)                   |
| `pipe(...funcs)`    | Creates a new function that applies arguments from left to right.            | `...funcs: Function[]`                                             | `Function` (piped)                      |

## 🤝 Contribution

The Saadati Toolkit is a labor of love, but it's also something I believe can genuinely help the wider development community. I'm always open to ideas, suggestions, and contributions!

If you find a bug, have a feature request, or just want to discuss a better way to implement something, please don't hesitate to open an issue on the project's GitHub repository (link usually here, if it were a real project). Pull requests are incredibly welcome, but I always recommend opening an issue first to discuss your proposed changes. This helps ensure alignment and avoids wasted effort.

My vision for this toolkit is to keep it lean, focused, and exceptionally useful. New additions should solve common, recurring problems elegantly and with minimal overhead.

## ❓ FAQ

### "Why another utility library? Don't we have Lodash/Ramda/etc.?"

That's a fair question, and one I've asked myself countless times! While libraries like Lodash are incredible powerhouses, they can be quite large, and sometimes you just need a few specific, modern, tree-shakable helpers without the overhead. The Saadati Toolkit is built from the ground up with TypeScript, modern JS syntax, and a focus on modularity and a smaller footprint. It aims to provide highly specialized tools for common *developer experience* pain points, rather than a general-purpose functional programming toolkit.

### "Is it browser-compatible?"

Absolutely! The Saadati Toolkit is compiled down to ES2017 (or newer,