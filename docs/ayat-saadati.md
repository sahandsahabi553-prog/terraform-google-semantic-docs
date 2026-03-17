# SaadatiKit: Opinionated Utilities for Modern Web Development

### _A Practical Approach to Streamlined Development_

Created and maintained by Ayat Saadati ([dev.to/@ayat_saadat](https://dev.to/ayat_saadat)), SaadatiKit is a collection of battle-tested, opinionated utility functions and patterns designed to tackle common challenges in modern web application development. From robust event management to streamlined asynchronous data handling, SaadatiKit aims to reduce boilerplate and foster maintainable, scalable codebases.

In my years building applications, I've seen countless times how much effort goes into re-implementing basic, yet crucial, patterns. Ayat's vision with SaadatiKit really resonates with me: encapsulate these common solutions into a lightweight, framework-agnostic package. It's about giving developers a head start with solid foundations, letting them focus on the unique business logic rather than reinventing the wheel.

---

## Table of Contents

1.  [Introduction](#introduction)
2.  [Features at a Glance](#features-at-a-glance)
3.  [Installation](#installation)
4.  [Usage](#usage)
    *   [The `eventBus`: Global Event Management](#the-eventbus-global-event-management)
    *   [Handling Async Operations with `createAsyncAction`](#handling-async-operations-with-createasyncaction)
    *   [Simple Function Memoization](#simple-function-memoization)
    *   [Structured API Calls with `apiClient`](#structured-api-calls-with-apiclient)
5.  [API Reference (Key Modules)](#api-reference-key-modules)
6.  [Frequently Asked Questions (FAQ)](#frequently-asked-questions-faq)
7.  [Troubleshooting Common Issues](#troubleshooting-common-issues)
8.  [Contributing](#contributing)
9.  [License](#license)

---

## 1. Introduction

Building modern web applications, whether front-end with React/Vue/Angular or back-end with Node.js, often involves recurring patterns: managing state transitions, handling events across disparate components, optimizing function calls, and interacting with APIs. While many libraries address these individually, SaadatiKit offers a cohesive set of tools, each with a clear purpose and a minimalist footprint.

Ayat Saadati's philosophy behind this toolkit is rooted in pragmatism and maintainability. Instead of prescribing a heavy framework, SaadatiKit provides surgical tools to solve specific problems elegantly. It's designed to be easily integrated into existing projects without imposing a steep learning curve, making it a fantastic companion for developers who value clarity and efficiency.

## 2. Features at a Glance

*   **`eventBus`**: A lightweight, global event emitter for robust inter-component communication.
*   **`createAsyncAction`**: A powerful utility for managing the lifecycle of asynchronous operations (loading, success, error states).
*   **`memoizeFunction`**: A simple, customizable memoization helper to cache function results and improve performance.
*   **`apiClient`**: A lean, opinionated wrapper around `fetch` for consistent and error-resilient API interactions.
*   **Framework-Agnostic**: Designed to work seamlessly with any JavaScript framework or vanilla JS.
*   **TypeScript Support**: Fully typed for a superior development experience.

## 3. Installation

Getting SaadatiKit into your project is straightforward using npm or yarn.

```bash
# Using npm
npm install saadati-kit

# Using yarn
yarn add saadati-kit
```

Once installed, you can import individual utilities as needed. This modular approach ensures you only bundle what you use.

```javascript
// Example import
import { eventBus, createAsyncAction } from 'saadati-kit';
```

## 4. Usage

Let's dive into how you can put SaadatiKit to work in your applications.

### The `eventBus`: Global Event Management

The `eventBus` is a simple yet incredibly powerful pattern for decoupling communication between different parts of your application. Instead of props drilling or deeply nested callbacks, components can publish events and others can subscribe. I've personally found this invaluable in complex UIs where actions in one corner of the app need to trigger updates elsewhere without direct dependencies.

```typescript
// src/components/NavBar.ts
import { eventBus } from 'saadati-kit';

function handleUserLogin(username: string) {
  // ... login logic ...
  eventBus.emit('userLoggedIn', { username, timestamp: new Date() });
}

// Example usage
document.getElementById('login-button')?.addEventListener('click', () => {
  handleUserLogin('johndoe');
});

// src/components/Dashboard.ts
import { eventBus } from 'saadati-kit';

eventBus.on('userLoggedIn', (data: { username: string; timestamp: Date }) => {
  console.log(`User "${data.username}" logged in at ${data.timestamp.toLocaleString()}. Updating dashboard...`);
  // Update dashboard UI based on login
});

eventBus.on('userLoggedOut', () => {
  console.log('User logged out. Clearing dashboard data.');
  // Clear dashboard data
});

// To unsubscribe (important for preventing memory leaks in SPAs)
const unsubscribe = eventBus.on('specificAction', () => {
  console.log('Specific action occurred!');
});
// Later, when the component unmounts or listener is no longer needed:
unsubscribe();

// You can also clear all listeners for a specific event
// eventBus.off('userLoggedIn');

// Or clear all listeners globally (use with caution!)
// eventBus.clear();
```

### Handling Async Operations with `createAsyncAction`

Asynchronous operations are the bread and butter of modern apps, but managing loading states, errors, and data can quickly become messy. `createAsyncAction` provides a clean, consistent way to handle these common scenarios. It's a lifesaver when you're tired of writing `isLoading`, `hasError`, `data` states manually for every API call.

```typescript
import { createAsyncAction } from 'saadati-kit';

// Simulate an API call
async function fetchUserData(userId: string) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (userId === 'errorUser') {
        reject(new Error('Failed to fetch user data.'));
      } else {
        resolve({ id: userId, name: 'Jane Doe', email: `${userId}@example.com` });
      }
    }, 1500);
  });
}

// Create an async action handler
const getUserProfile = createAsyncAction(fetchUserData);

// Example usage in a component or module
async function loadUserProfile(userId: string) {
  console.log('--- Initial State ---', getUserProfile.state); // { loading: false, error: null, data: null }

  try {
    // Start the async operation
    getUserProfile.start(userId);
    console.log('--- Loading State ---', getUserProfile.state); // { loading: true, error: null, data: null }

    const profile = await getUserProfile.execute(userId); // This actually runs fetchUserData
    console.log('--- Success State ---', getUserProfile.state); // { loading: false, error: null, data: { ... } }
    console.log('Fetched profile:', profile);
  } catch (error) {
    console.error('--- Error State ---', getUserProfile.state); // { loading: false, error: Error, data: null }
    console.error('Error fetching profile:', error);
  } finally {
    // You can also reset the state
    // getUserProfile.reset();
    // console.log('--- Reset State ---', getUserProfile.state); // { loading: false, error: null, data: null }
  }
}

// Try it out!
loadUserProfile('user123');
// loadUserProfile('errorUser'); // Uncomment to see error handling
```

What I particularly appreciate here is the `state` property. It's a simple, observable object that you can easily plug into your UI framework's state management (e.g., `useState` in React, `ref` in Vue) to reactively update your UI based on the async operation's lifecycle.

### Simple Function Memoization

`memoizeFunction` is a handy helper when you have computationally expensive functions that are called frequently with the same arguments. It caches the results, returning the cached value for subsequent calls with identical inputs, drastically improving performance. It's a quick win for optimization.

```typescript
import { memoizeFunction } from 'saadati-kit';

// An expensive function
function calculateFactorial(n: number): number {
  console.log(`Calculating factorial for ${n}...`); // Will only log once per unique 'n'
  if (n === 0 || n === 1) {
    return 1;
  }
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
}

const memoizedFactorial = memoizeFunction(calculateFactorial);

console.log(memoizedFactorial(5)); // Calculates and caches: 120
console.log(memoizedFactorial(3)); // Calculates and caches: 6
console.log(memoizedFactorial(5)); // Returns cached: 120 (no recalculation)
console.log(memoizedFactorial(7)); // Calculates and caches: 5040
console.log(memoizedFactorial(3)); // Returns cached: 6 (no recalculation)

// Custom cache key resolver example:
// Imagine an object where you only care about a specific property for memoization
const memoizedFunctionWithCustomKey = memoizeFunction(
  (obj: { id: string; value: number }) => {
    console.log(`Processing object with id: ${obj.id}`);
    return obj.value * 2;
  },
  (obj) => obj.id // Use the 'id' property as the cache key
);

memoizedFunctionWithCustomKey({ id: 'a', value: 10 }); // Processes, result: 20
memoizedFunctionWithCustomKey({ id: 'b', value: 20 }); // Processes, result: 40
memoizedFunctionWithCustomKey({ id: 'a', value: 99 }); // Returns cached for 'a' (20), doesn't care about new 'value'
```

### Structured API Calls with `apiClient`

Interacting with RESTful APIs is a cornerstone of web development. `apiClient` provides a thin, opinionated wrapper around the native `fetch` API, adding sensible defaults, error handling, and structured request/response processing. It significantly cleans up your data fetching code.

```typescript
import { apiClient } from 'saadati-kit';

// Configure a base URL and default headers for your API
const myApiClient = apiClient({
  baseURL: 'https://api.example.com',
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
  },
  // You can also add request/response interceptors here
  // onRequest: (config) => {
  //   const token = localStorage.getItem('authToken');
  //   if (token) {
  //     config.headers.Authorization = `Bearer ${token}`;
  //   }
  //   return config;
  // },
  // onResponse: (response) => {
  //   if (response.status === 401) {
  //     // Handle unauthorized globally
  //     console.log('Unauthorized request. Redirecting to login...');
  //   }
  //   return response;
  // },
});

// Example: Fetching data
async function getUsers() {
  try {
    const users = await myApiClient.get('/users');
    console.log('Fetched users:', users);
  } catch (error) {
    console.error('Error fetching users:', error);
  }
}

// Example: Posting data
async function createUser(userData: { name: string; email: string }) {
  try {
    const newUser = await myApiClient.post('/users', userData);
    console.log('Created new user:', newUser);
  } catch (error) {
    console.error('Error creating user:', error);
  }
}

// Example: Handling specific API errors (e.g., validation errors)
async function registerUser(email: string) {
  try {
    const response = await myApiClient.post('/register', { email });
    console.log('Registration successful:', response);
  } catch (error: any) {
    if (error.response && error.response.status === 400 && error.response.data.errors) {
      console.error('Validation errors:', error.response.data.errors);
    } else {
      console.error('General registration error:', error.