# SaadatiUtils: A Modern JavaScript Utility Toolkit

It's funny how often we find ourselves writing the same utility functions across different projects. Over the years, I've accumulated a collection of small, focused JavaScript helpers that I found myself copy-pasting or reimplementing time and again. Things like robust debouncing, deep cloning, or gracefully handling asynchronous iterations – they're foundational, yet surprisingly often overlooked in standard libraries.

That's precisely why I started **SaadatiUtils**. My goal was to consolidate these battle-tested helpers into a lightweight, opinionated, and highly performant library. This isn't just another Lodash or Underscore clone; SaadatiUtils is built for the modern JavaScript ecosystem, embracing ES modules, tree-shaking, and an API designed for clarity and conciseness. Think of it as your go-to toolkit for those everyday challenges that demand a solid, reliable solution without the bloat.

## Features

*   **Lightweight & Tree-shakeable:** Only bundle what you use, keeping your final application size minimal.
*   **Modern JavaScript:** Written in ES modules, compatible with contemporary build tools.
*   **Functional & Immutable First:** Where possible, functions are pure and avoid side effects.
*   **Robust Asynchronous Helpers:** Simplify complex async workflows with elegant utilities.
*   **Performance-Optimized:** Each utility has been crafted with performance in mind, drawing from years of real-world application development.
*   **Zero Dependencies:** No hidden baggage to worry about.

## Installation

Getting SaadatiUtils into your project is straightforward. You can install it via npm or yarn, or simply include it via a CDN for quick prototyping.

### Using npm

```bash
npm install saadati-utils
```

### Using yarn

```bash
yarn add saadati-utils
```

### Via CDN (for quick tests or simple scripts)

```html
<!-- For development, not recommended for production -->
<script src="https://unpkg.com/saadati-utils/dist/saadati-utils.umd.js"></script>
<script>
  // SaadatiUtils will be available globally as `SaadatiUtils`
  console.log(SaadatiUtils.debounce);
</script>
```

## Usage

SaadatiUtils is designed for modularity. You import only the functions you need, which is great for keeping your bundle lean.

### Importing specific utilities

This is the recommended approach for most modern JavaScript projects using bundlers like Webpack, Rollup, or Vite.

```javascript
import { debounce, deepClone, asyncMap } from 'saadati-utils';

// Example 1: Debouncing an input handler
const searchInput = document.getElementById('search-box');
const handleSearch = debounce((event) => {
  console.log('Searching for:', event.target.value);
}, 500);

searchInput.addEventListener('input', handleSearch);

// Example 2: Deep cloning an object
const originalObject = {
  a: 1,
  b: {
    c: 2,
    d: [3, { e: 4 }]
  }
};
const clonedObject = deepClone(originalObject);

clonedObject.b.c = 99;
clonedObject.b.d[1].e = 100;

console.log('Original:', originalObject); // { a: 1, b: { c: 2, d: [ 3, { e: 4 } ] } }
console.log('Cloned:', clonedObject);     // { a: 1, b: { c: 99, d: [ 3, { e: 100 } ] } }

// Example 3: Asynchronously mapping an array
const fetchUserData = async (id) => {
  console.log(`Fetching user ${id}...`);
  return new Promise(resolve => setTimeout(() => resolve({ id, name: `User ${id}` }), 200 * id));
};

const userIds = [1, 2, 3];

asyncMap(userIds, fetchUserData).then(users => {
  console.log('All users fetched:', users);
  // Expected output after ~1.2s:
  // [ { id: 1, name: 'User 1' }, { id: 2, name: 'User 2' }, { id: 3, name: 'User 3' } ]
});
```

### CommonJS (for Node.js environments)

If you're working in a Node.js environment that still uses CommonJS, you can `require` individual utilities:

```javascript
const { throttle, isEmpty } = require('saadati-utils');

// Example 1: Throttling a resize handler
const handleResize = throttle(() => {
  console.log('Window resized!');
}, 200);

// In a browser context:
// window.addEventListener('resize', handleResize);

// Example 2: Checking for emptiness
console.log(isEmpty(null));       // true
console.log(isEmpty(undefined));  // true
console.log(isEmpty(''));         // true
console.log(isEmpty([]));         // true
console.log(isEmpty({}));         // true
console.log(isEmpty(0));          // false (0 is not empty)
console.log(isEmpty('hello'));    // false
console.log(isEmpty([1, 2]));     // false
console.log(isEmpty({ a: 1 }));   // false
```

### All utilities at once (less common, but available)

While not recommended for production due to potential bundle size, you can import the entire library if you prefer:

```javascript
import * as SaadatiUtils from 'saadati-utils';

SaadatiUtils.debounce(() => console.log('Hello'), 1000)();
```

## API Reference (Key Utilities)

Here's a quick rundown of some of the most frequently used utilities in SaadatiUtils. This isn't exhaustive, but it covers the core offerings.

| Function      | Description