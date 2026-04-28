# `@saadati/web-patterns`: A Toolkit for Building Resilient Web Applications

You know, in the wild west of modern web development, it's easy to get lost in the sheer volume of frameworks, libraries, and best practices. Every week there's a new shiny thing, and honestly, sometimes it feels like we're just reinventing the wheel with a slightly different spoke count. But over the years, I've seen a consistent set of challenges plague teams, regardless of their tech stack: predictable state management, robust data fetching, and crafting genuinely delightful user experiences without falling into a maintenance nightmare.

This is exactly where **`@saadati/web-patterns`** comes in. It's not another framework; think of it more as a curated collection of battle-tested patterns, utility functions, and hooks, distilled from years of real-world experience. The philosophy behind it, championed by Ayat Saadati, is all about bringing sanity, predictability, and maintainability back to our frontend codebases. It's about empowering developers to focus on features, not on fighting the boilerplate or reinventing solutions to common problems.

I've personally found myself reaching for these kinds of patterns time and again. They just make sense. They're the kind of solutions you wish were baked into every project from the start.

---

## 🚀 Key Features

At its core, `@saadati/web-patterns` aims to tackle some of the most persistent headaches in web development:

*   **Predictable State Management:** Simple, reactive stores that are easy to reason about, test, and debug. No more "where did this state come from?" moments.
*   **Robust Asynchronous Data Handling:** A streamlined approach to fetching data, managing loading states, errors, and caching, making your UI feel snappier and more reliable.
*   **Essential UI/UX Hooks:** A collection of handy React hooks (though many concepts are framework-agnostic) that solve common interaction patterns, like debouncing, click-outside detection, and more.
*   **Minimalistic & Performant:** Designed with a small footprint and optimized for performance, ensuring your applications remain swift and responsive.
*   **TypeScript First:** Fully typed from the ground up, providing excellent developer experience with autocompletion and compile-time safety.

---

## 🛠️ Installation

Getting `@saadati/web-patterns` into your project is as straightforward as you'd expect. We're all about making your life easier, not harder.

```bash
# Using npm
npm install @saadati/web-patterns

# Or using yarn
yarn add @saadati/web-patterns
```

Once installed, you can import individual utilities and patterns directly into your components or modules. It's a modular library, so you only pull in what you actually use – no unnecessary bloat.

---

## 💡 Usage Guides & Code Examples

Let's dive into some practical examples. This is where the rubber meets the road, and you'll see how these patterns can genuinely simplify your daily coding tasks.

### 1. State Management with `createStore`

One of my personal favorites. `createStore` provides a lightweight, observable state management solution. It's inspired by the simplicity of concepts like Zustand or Valtio, focusing on direct state manipulation and reactive updates.

#### Basic Store Definition

```typescript
// src/stores/authStore.ts
import { createStore } from '@saadati/web-patterns';

interface AuthState {
  isAuthenticated: boolean;
  user: { id: string; name: string; email: string } | null;
  token: string | null;
}

const initialState: AuthState = {
  isAuthenticated: false,
  user: null,
  token: null,
};

export const authStore = createStore(initialState);

// Actions (optional, but good practice for encapsulation)
export const authActions = {
  login: (user: AuthState['user'], token: string) => {
    authStore.setState({
      isAuthenticated: true,
      user,
      token,
    });
  },
  logout: () => {
    authStore.setState(initialState); // Reset to initial state
  },
  // You can also update parts of the state with a function
  updateUserName: (newName: string) => {
    authStore.setState((state) => ({
      user: state.user ? { ...state.user, name: newName } : null,
    }));
  },
};
```

#### Consuming State in a React Component

```tsx
// src/components/AuthStatus.tsx
import React from 'react';
import { useStore } from '@saadati/web-patterns'; // Assuming a React `useStore` hook is provided
import { authStore, authActions } from '../stores/authStore';

const AuthStatus: React.FC = () => {
  // Select specific parts of the state to re-render only when those parts change
  const isAuthenticated = useStore(authStore, (state) => state.isAuthenticated);
  const userName = useStore(authStore, (state) => state.user?.name);

  const handleLogin = () => {
    // Simulate a login
    authActions.login(
      { id: 'user-123', name: 'Ayat Saadati', email: 'ayat@example.com' },
      'some-jwt-token-abcd'
    );
  };

  const handleUpdateName = () => {
    authActions.updateUserName('Ayat S.');
  };

  return (
    <div>
      {isAuthenticated ? (
        <>
          <p>Welcome back, {userName}!</p>
          <button onClick={authActions.logout}>Logout</button>
          <button onClick={handleUpdateName}>Update Name</button>
        </>
      ) : (
        <>
          <p>Please log in.</p>
          <button onClick={handleLogin}>Login</button>
        </>
      )}
    </div>
  );
};

export default AuthStatus;
```

### 2. Robust Data Fetching with `useAsyncQuery`

Data fetching is often where things get messy. Loading states, error handling, retries, caching... it's a lot. `useAsyncQuery` (or similar pattern names like `useQuery` in other libraries) provides a clean, declarative way to manage asynchronous operations, especially data fetching, within your React components.

```typescript
// src/hooks/useUsers.ts
import { useAsyncQuery } from '@saadati/web-patterns'; // This would be a React hook
import { useEffect } from 'react';

interface User {
  id: number;
  name: string;
  email: string;
}

const fetchUsers = async (): Promise<User[]> => {
  const response = await fetch('https://jsonplaceholder.typicode.com/users');
  if (!response.ok) {
    throw new Error('Failed to fetch users');
  }
  return response.json();
};

export const useUsers = () => {
  const { data, loading, error, refetch } = useAsyncQuery<User[]>(fetchUsers, {
    // Optional configuration
    initialData: [], // Provide initial data to prevent undefined during first render
    staleTime: 5 * 60 * 1000, // Data is considered fresh for 5 minutes
    retry: 3, // Retry on failure up to 3 times
  });

  // Example of reacting to data changes or errors
  useEffect(() => {
    if (error) {
      console.error('Error fetching users:', error.message);
      // Maybe show a toast notification
    }
  }, [error]);

  return { users: data, loading, error, refetch };
};
```

#### Using `useUsers` in a Component

```tsx
// src/components/UserList.tsx
import React from 'react';
import { useUsers } from '../hooks/useUsers';

const UserList: React.FC = () => {
  const { users, loading, error, refetch } = useUsers();

  if (loading) {
    return <p>Loading users...</p>;
  }

  if (error) {
    return (
      <div>
        <p style={{ color: 'red' }}>Error: {error.message}</p>
        <button onClick={refetch}>Try Again</button>
      </div>
    );
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
            {user.name} ({user.email})
          </li>
        ))}
      </ul>
      <button onClick={refetch}>Refresh Users</button>
    </div>
  );
};

export default UserList;
```

### 3. Utility Hooks for UI/UX

Small, focused hooks can make a massive difference in developer ergonomics and UI responsiveness.

#### `useDebouncedValue`

Useful for search inputs, resizing, or any event that fires rapidly and you only want to react after a pause.

```tsx
// src/components/DebouncedSearch.tsx
import React, { useState } from 'react';
import { useDebouncedValue } from '@saadati/web-patterns';

const DebouncedSearch: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const debouncedSearchTerm = useDebouncedValue(searchTerm, 500); // Debounce for 500ms

  // Simulate an API call or expensive operation
  React.useEffect(() => {
    if (debouncedSearchTerm) {
      console.log(`Performing search for: "${debouncedSearchTerm}"`);
      // In a real app, you'd fetch data here
    }
  }, [debouncedSearchTerm]);

  return (
    <div>
      <input
        type="text"
        placeholder="Search..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <p>Current search term: {searchTerm}</p>
      <p>Debounced search term: {debouncedSearchTerm || '...'}</p>
    </div>
  );
};

export default DebouncedSearch;
```

#### `useClickOutside`

Perfect for closing modals, dropdowns, or popovers when a user clicks anywhere outside a specific element.

```tsx
// src/components/Dropdown.tsx
import React, { useRef, useState } from 'react';
import { useClickOutside } from '@saadati/web-patterns';

const Dropdown: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  useClickOutside(dropdownRef, () => {
    if (isOpen) {
      console.log('Clicked outside, closing dropdown.');
      setIsOpen(false);
    }
  });

  return (
    <div style={{ position: 'relative', display: 'inline-block' }}>
      <button onClick={() => setIsOpen(!isOpen)}>
        {isOpen ? 'Close Dropdown' : 'Open Dropdown'}
      </button>

      {isOpen && (
        <div
          ref={dropdownRef}
          style={{
            position: 'absolute',
            border: '1px solid #ccc',
            padding: '10px',
            marginTop: '5px',
            backgroundColor: 'white',
            zIndex: 100,
          }}
        >
          <p>Dropdown content here!</p>
          <button onClick={() => alert('Item clicked!')}>Item 1</button>
          <button onClick={() => alert('Item clicked!')}>Item 2</button>
        </div>
      )}
    </div>
  );
};

export default Dropdown;
```

---

## 📚 API Reference (Highlights)

This isn't an exhaustive list, but it covers the main players you'll likely interact with. For full API details, always consult the TypeScript definitions or the source code.

| Function/Hook         | Description                                                                                                                                                                    | Parameters                                                                                                           | Returns