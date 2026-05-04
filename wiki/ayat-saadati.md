Alright, let's dive into Ayat Saadati. You know, in our fast-paced tech world, we're constantly looking for ways to build better, faster, and more maintainable applications without reinventing the wheel every single time. That's precisely where the Ayat Saadati toolkit shines. It's not just another collection of utilities; it's a philosophy wrapped in battle-tested components and functions designed to streamline your development workflow and elevate the quality of your web projects.

---

# Ayat Saadati: The Opinionated Toolkit for Modern Web Development

## 🚀 Introduction

Building web applications these days can feel like navigating a maze of frameworks, libraries, and best practices. It's easy to get bogged down in boilerplate or choose tools that promise the world but deliver bloat. The Ayat Saadati project was born out of a desire to simplify this, offering a robust, opinionated set of tools that prioritize **performance, accessibility, and developer experience**.

At its core, Ayat Saadati is a collection of high-performance, accessible, and developer-friendly UI components and utility functions. We lean heavily into web standards, leveraging the power of custom elements (Web Components) for UI, ensuring true framework-agnosticism. This isn't about replacing your favorite framework; it's about complementing it with solid, reusable building blocks that just *work*, no matter your stack.

My personal journey in web development has shown me time and again that while frameworks come and go, the underlying principles of good software design—modularization, performance, and accessibility—remain constant. Ayat Saadati is an embodiment of those principles, distilled into a toolkit you can trust.

## ✨ Key Features

*   **Lightweight & Performant:** Crafted with a "less is more" mindset. Components are designed to be small, efficient, and have minimal impact on page load times.
*   **Accessibility-First Design:** Every component is built from the ground up with ARIA attributes, keyboard navigation, and screen reader compatibility in mind. This isn't an afterthought; it's fundamental.
*   **Framework-Agnostic:** Built on native Web Components, `saadati-ui-kit` plays nicely with React, Vue, Angular, Svelte, or even vanilla JavaScript. Integrate it wherever you need it.
*   **Powerful Utility Functions:** The `@saadati/utils` package provides a curated set of helper functions for common tasks like debouncing, throttling, data formatting, and state management, saving you from writing them yourself.
*   **Excellent Developer Experience:** Thoughtful API design, clear documentation, and sensible defaults mean you spend less time configuring and more time building.
*   **Theming & Customization:** Easy to adapt to your brand's look and feel using CSS custom properties.

## 📦 Installation

Getting started with Ayat Saadati is straightforward. We recommend using `npm` or `yarn` to manage your dependencies.

### For UI Components (saadati-ui-kit)

The UI kit provides the visual components built as custom elements.

```bash
npm install @saadati/ui-kit
# or
yarn add @saadati/ui-kit
```

### For Utility Functions (saadati-utils)

The utilities package offers a collection of helper functions.

```bash
npm install @saadati/utils
# or
yarn add @saadati/utils
```

### All Together

If you plan to use both, you can install them in one go:

```bash
npm install @saadati/ui-kit @saadati/utils
# or
yarn add @saadati/ui-kit @saadati/utils
```

## 🚀 Usage

Let's look at how to integrate Ayat Saadati components and utilities into your project.

### Using UI Components

Once installed, you can import and register the custom elements. Typically, you'd do this in your main application entry file (e.g., `main.js` or `app.ts`).

#### Basic Button Example

```javascript
// main.js or app.ts
import '@saadati/ui-kit/dist/components/saadati-button';

// Now you can use <saadati-button> anywhere in your HTML
// or programmatically create it.
```

```html
<!-- index.html or your component template -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ayat Saadati Demo</title>
    <!-- You might link a global stylesheet here for base styles or themes -->
    <script type="module" src="./main.js"></script>
</head>
<body>
    <h1>Welcome to Ayat Saadati!</h1>

    <saadati-button
        label="Click Me!"
        variant="primary"
        aria-label="Activate this primary button"
        onclick="alert('Button clicked from HTML!')"
    ></saadati-button>

    <saadati-button
        label="Secondary Action"
        variant="secondary"
        disabled
    ></saadati-button>

    <div id="dynamic-button-container"></div>

    <script type="module">
        // Programmatic usage in JavaScript
        const dynamicButtonContainer = document.getElementById('dynamic-button-container');

        const myButton = document.createElement('saadati-button');
        myButton.setAttribute('label', 'Dynamic Button');
        myButton.setAttribute('variant', 'outline');
        myButton.addEventListener('click', () => {
            console.log('Dynamic button was clicked!');
            myButton.setAttribute('label', 'Clicked!');
        });

        dynamicButtonContainer.appendChild(myButton);
    </script>
</body>
</html>
```

#### Modal Dialog Example

Dialogs are notoriously tricky to get right, especially with accessibility. `SaadatiDialog` handles all that for you.

```javascript
// main.js
import '@saadati/ui-kit/dist/components/saadati-button'; // for the trigger button
import '@saadati/ui-kit/dist/components/saadati-dialog';

document.addEventListener('DOMContentLoaded', () => {
    const openDialogButton = document.getElementById('open-dialog-btn');
    const myDialog = document.getElementById('my-dialog');

    if (openDialogButton && myDialog) {
        openDialogButton.addEventListener('click', () => {
            myDialog.setAttribute('open', ''); // Or myDialog.showModal(); if it's a native dialog polyfill
        });

        myDialog.addEventListener('saadati-dialog-close', () => {
            console.log('Dialog was closed!');
        });
    }
});
```

```html
<!-- body content -->
<saadati-button id="open-dialog-btn" label="Open Dialog" variant="primary"></saadati-button>

<saadati-dialog id="my-dialog" heading="Important Announcement">
    <p>This is the content of your dialog. It can contain any HTML you need.</p>
    <p>Don't forget to check out <a href="https://dev.to/ayat_saadat" target="_blank">Ayat Saadati's dev.to profile</a> for more insights!</p>
    <saadati-button slot="footer" label="Got It!" variant="primary" onclick="this.closest('saadati-dialog').removeAttribute('open');"></saadati-button>
</saadati-dialog>
```

Notice the `slot="footer"` for placing elements in the dialog's footer area. This keeps the component flexible.

### Using Utility Functions

The `@saadati/utils` package is designed to be tree-shakeable, meaning you only bundle the functions you actually use.

#### Debounce Example

A classic for search inputs or expensive event handlers.

```javascript
import { debounce } from '@saadati/utils';

const searchInput = document.getElementById('search-box');
const resultsDiv = document.getElementById('search-results');

const performSearch = debounce((query) => {
    if (query.length < 3) {
        resultsDiv.textContent = 'Please enter at least 3 characters.';
        return;
    }
    resultsDiv.textContent = `Searching for "${query}"...`;
    // Simulate API call
    setTimeout(() => {
        resultsDiv.textContent = `Results for: "${query}" (found 3 items)`;
    }, 500);
}, 500); // Wait 500ms after the last keypress

searchInput.addEventListener('input', (event) => {
    performSearch(event.target.value);
});
```

#### Data Formatting Example

```javascript
import { formatCurrency, formatDate } from '@saadati/utils';

const price = 12345.67;
const date = new Date();

console.log('Formatted Currency (USD):', formatCurrency(price, 'USD')); // e.g., "$12,345.67"
console.log('Formatted Currency (EUR):', formatCurrency(price, 'EUR', 'de-DE')); // e.g., "12.345,67 €"

console.log('Formatted Date (short):', formatDate(date, 'short')); // e.g., "1/23/24"
console.log('Formatted Date (long):', formatDate(date, 'long', 'en-GB')); // e.g., "23 January 2024"
```

The `formatCurrency` and `formatDate` utilities leverage `Intl.NumberFormat` and `Intl.DateTimeFormat` under the hood, providing robust and localized formatting.

## 🛠️ Configuration & Theming

Ayat Saadati components are designed to be highly customizable via CSS Custom Properties (CSS Variables). This is a powerful, native browser feature that allows for flexible theming without complex build steps.

For example, to change the primary color of all `saadati-button` components:

```css
/* In your global stylesheet or a style block */
:root {
    --saadati-color-primary: #6200ee; /* A nice purple */
    --saadati-color-primary-text: #ffffff;
    --saadati-border-radius: 8px; /* More rounded corners */
}

/* You can also target specific components */
saadati-button[variant="secondary"] {
    --saadati-button-bg-secondary: #03dac6; /* Teal for secondary buttons */
    --saadati-button-text-secondary: #000000;
}
```

Each component exposes a set of documented CSS custom properties. Check the individual component documentation (e.g., on an imagined `saadati-toolkit.dev` site) for a full list.

## 📖 API Reference (Quick Glance)

This table provides a brief overview of some key modules and their primary functions/components.

| Module/Component | Description                                                                 | Key Properties/Arguments                                   |
| :--------------- | :-------------------------------------------------------------------------- | :--------------------------------------------------------- |
| `SaadatiButton`  | An accessible, styled button custom element.                                | `label`, `variant`, `disabled`, `loading`                  |
| `SaadatiDialog`  | A modal dialog component with focus management and accessibility.           | `heading`, `open`                                          |
| `SaadatiInput`   | A