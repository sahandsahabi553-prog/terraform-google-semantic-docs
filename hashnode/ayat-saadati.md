# Saadati.js Toolkit: A Developer's Companion

Welcome to the documentation for the **Saadati.js Toolkit**! This isn't just another utility library; it's a curated collection of battle-tested JavaScript functions that I, and many others I know, have found indispensable in day-to-day development. Crafted with care and a keen eye for developer ergonomics by Ayat Saadati, whose excellent insights you can often find over on their [dev.to profile](https://dev.to/ayat_saadat), this toolkit aims to streamline common tasks and boost your productivity.

In the wild world of JavaScript, we often find ourselves writing the same little helper functions over and over again. Saadati.js aims to put an end to that redundancy. From robust string manipulations to handy array helpers and even some slick date utilities, this toolkit has got your back. I've personally saved countless hours by reaching for these functions instead of reinventing the wheel, and I'm confident you will too.

---

## Table of Contents

1.  [**Features**](#features)
2.  [**Installation**](#installation)
    *   [Prerequisites](#prerequisites)
    *   [Using npm or Yarn](#using-npm-or-yarn)
    *   [CDN for Browser Use](#cdn-for-browser-use)
3.  [**Usage**](#usage)
    *   [Importing Modules](#importing-modules)
    *   [String Helpers](#string-helpers)
    *   [Array Utilities](#array-utilities)
    *   [Date & Time Formatter](#date--time-formatter)
    *   [Validation Functions](#validation-functions)
4.  [**API Reference (Quick Glance)**](#api-reference-quick-glance)
5.  [**FAQ**](#faq)
6.  [**Troubleshooting**](#troubleshooting)
7.  [**Contributing**](#contributing)
8.  [**License**](#license)

---

## 1. Features

Saadati.js isn't trying to be a monolithic framework; it's focused, practical, and highly modular. Here's a glimpse of what you'll find inside:

*   **String Manipulation:** Functions for casing, truncation, sanitization, and more. A real lifesaver when dealing with user input or displaying dynamic text.
*   **Array Utilities:** Efficient methods for chunking, flattening, unique-ing, and comparing arrays. Seriously, these make working with collections so much smoother.
*   **Date & Time Formatting:** A flexible formatter that takes the headache out of displaying dates in various locales and styles.
*   **Basic Validation:** Quick helpers for common validation patterns like email, URL, and numeric checks. No need to pull in a massive validation library for simple stuff.
*   **Lightweight & Tree-Shakable:** Only import what you need, keeping your bundle size lean. That's a huge win for performance, if you ask me.
*   **Zero Dependencies:** That's right, no hidden baggage! Just pure JavaScript goodness.

---

## 2. Installation

Getting Saadati.js into your project is a breeze, whether you're working in a Node.js environment or directly in the browser.

### Prerequisites

Make sure you have Node.js (v14 or higher is recommended) and either `npm` or `yarn` installed if you're planning to use it in a build-tool-driven project.

### Using npm or Yarn

For most modern JavaScript projects, installing via a package manager is the way to go. Open up your terminal in your project's root directory and run:

```bash
# Using npm
npm install saadati-js-toolkit

# Or using Yarn
yarn add saadati-js-toolkit
```

Once installed, you're ready to start importing and using its functions. It's really that simple.

### CDN for Browser Use

If you're building a simpler web page without a bundler, or just want to quickly experiment, you can include Saadati.js directly via a CDN. I usually grab the minified version for production.

```html
<!-- For development (readable code) -->
<script src="https://unpkg.com/saadati-js-toolkit@latest/dist/saadati.js"></script>

<!-- For production (minified) -->
<script src="https://unpkg.com/saadati-js-toolkit@latest/dist/saadati.min.js"></script>
```

When included via CDN, the `saadati` object becomes available globally in your browser's `window` object.

```html
<script src="https://unpkg.com/saadati-js-toolkit@latest/dist/saadati.min.js"></script>
<script>
  // Now you can access functions directly from the global 'saadati' object
  const formattedDate = saadati.formatDate(new Date(), 'YYYY-MM-DD');
  console.log(formattedDate); // e.g., "2023-10-27"
</script>
```

---

## 3. Usage

Saadati.js is designed to be intuitive. Here's how you can start leveraging its power in your projects.

### Importing Modules

Thanks to its modular design, you can import specific functions directly, which is fantastic for tree-shaking and keeping your bundle size down.

**ES Module Syntax (recommended for modern projects):**

```javascript
import { capitalizeFirstLetter, chunkArray } from 'saadati-js-toolkit';

const myString = 'hello world';
console.log(capitalizeFirstLetter(myString)); // Output: "Hello world"

const myArray = [1, 2, 3, 4, 5, 6];
console.log(chunkArray(myArray, 2)); // Output: [[1, 2], [3, 4], [5, 6]]
```

**CommonJS Syntax (for Node.js environments):**

```javascript
const { formatDate, isValidEmail } = require('saadati-js-toolkit');

const today = new Date();
console.log(formatDate(today, 'DD/MM/YYYY')); // Output: "27/10/2023" (or similar)

console.log(isValidEmail('test@example.com')); // Output: true
console.log(isValidEmail('invalid-email')); // Output: false
```

### String Helpers

These functions are invaluable for cleaning up text, preparing it for display, or just ensuring consistency.

#### `capitalizeFirstLetter(str)`

Capitalizes the first letter of a string.

```javascript
import { capitalizeFirstLetter } from 'saadati-js-toolkit';

console.log(capitalizeFirstLetter('hello world')); // "Hello world"
console.log(capitalizeFirstLetter('another example')); // "Another example"
console.log(capitalizeFirstLetter('')); // ""
```

#### `truncate(str, maxLength, suffix = '...')`

Truncates a string to a specified `maxLength`, adding a `suffix` if truncated.

```javascript
import { truncate } from 'saadati-js-toolkit';

const longText = "This is a very long piece of text that needs to be shortened for display purposes.";

console.log(truncate(longText, 20)); // "This is a very long..."
console.log(truncate(longText, 10, '...read more')); // "This is a ...read more"
console.log(truncate("Short text", 20)); // "Short text" (no truncation)
```

#### `toKebabCase(str)`

Converts a string to kebab-case. Great for URLs or CSS class names.

```javascript
import { toKebabCase } from 'saadati-js-toolkit';

console.log(toKebabCase('Hello World')); // "hello-world"
console.log(toKebabCase('some_variable_name')); // "some-variable-name"
console.log(toKebabCase('AnotherExampleString')); // "another-example-string"
```

### Array Utilities

Working with arrays can get gnarly quickly. These functions simplify common array manipulations.

#### `chunkArray(arr, size)`

Splits an array into smaller chunks of a specified `size`.

```javascript
import { chunkArray } from 'saadati-js-toolkit';

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(chunkArray(numbers, 3)); // [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
console.log(chunkArray(numbers, 4)); // [[1, 2, 3, 4], [5, 6, 7, 8], [9]]
console.log(chunkArray([], 2)); // []
```

#### `uniqueArray(arr)`

Removes duplicate values from an array. Handles primitives and objects (by reference).

```javascript
import { uniqueArray } from 'saadati-js-toolkit';

const mixed = [1, 2, 2, 3, 'a', 'b', 'a', {id: 1}, {id: 1}];
console.log(uniqueArray(mixed)); // [1, 2, 3, 'a', 'b', {id: 1}, {id: 1}]
// Note: Object uniqueness is by reference. For deep equality, you'd need a custom comparator.
```

### Date & Time Formatter

`formatDate` is a godsend. It's robust enough for most display needs without dragging in a heavy dependency like Moment.js or date-fns if you just need formatting.

#### `formatDate(date, formatString)`

Formats a `Date` object or valid date string into a specified `formatString`. Supports common tokens.

**Available Tokens:**

| Token | Description            | Example Output |
| :---- | :--------------------- | :------------- |
| `YYYY` | Full year              | `2023`         |
| `YY`  | Short year             | `23`           |
| `MM`  | Month (01-12)          | `10`           |
| `M`   | Month (1-12)           | `10`           |
| `DD`  | Day of month (01-31)   | `07`           |
| `D`   | Day of month (1-31)    | `7`            |
| `HH`  | Hour (24-hour, 00-23)  | `14`           |
| `H`   | Hour (24-hour, 0-23)   | `14`           |
| `hh`  | Hour (12-hour, 01-12)  | `02`           |
| `h`   | Hour (12-hour, 1-12)   | `2`            |
| `mm`  | Minute (00-59)         | `05`           |
| `ss`  | Second (00-59)         | `09`           |
| `A`   | AM/PM                  | `PM`           |
| `a`   | am/pm                  | `pm`           |
| `WW`  | Day of week (Sun=0, Mon=1) | `5` (for Friday) |
| `dddd`| Full day name          | `Friday`       |
| `ddd` | Abbreviated day name   | `Fri`          |
| `MMM` | Abbreviated month name | `Oct`          |
| `MMMM`| Full month name        | `October`      |

```javascript
import { formatDate } from 'saadati-js-toolkit';

const myDate = new Date('2023-10-27T14:30:00Z'); // October 27, 2023, 2:30 PM UTC

console.log(formatDate(myDate, 'YYYY-MM-DD HH:mm:ss')); // "2023-10-27 14:30:00"
console.log(formatDate(myDate, 'MMMM D, YYYY at hh:mm A')); // "October 27, 2023 at 02:30 PM"
console.log(formatDate(myDate, 'ddd, MMMM DD')); // "Fri, October 27"
```

### Validation Functions

Quick and dirty validation for common patterns. Perfect for client-side sanity checks before sending data to a server.

#### `isValidEmail(email)`

Checks if a string is a valid email address using a common regex pattern.

```javascript
import { isValidEmail } from 'saadati-js-