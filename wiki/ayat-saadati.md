# SaadatUI: A Performant & Accessible Web Component Library

Welcome to the documentation for **SaadatUI**, a meticulously crafted collection of lightweight, performant, and accessible web components and utility functions. Born from a passion for building robust web experiences with a keen eye on developer ergonomics and end-user satisfaction, SaadatUI aims to streamline your development process without sacrificing quality.

At its core, SaadatUI embodies the principles I've championed throughout my career: leveraging native browser capabilities, prioritizing accessibility from the ground up, and squeezing every drop of performance out of our applications. It's built with modern web standards and designed to integrate seamlessly into any framework or no framework at all.

---

## Table of Contents

1.  [Introduction](#introduction)
2.  [Why SaadatUI? My Philosophy](#why-saadatui-my-philosophy)
3.  [Installation](#installation)
    *   [NPM/Yarn](#npmyarn)
    *   [CDN](#cdn)
4.  [Quick Start](#quick-start)
5.  [Core Concepts](#core-concepts)
    *   [Web Components](#web-components)
    *   [Accessibility First](#accessibility-first)
    *   [Performance Mindset](#performance-mindset)
6.  [Components](#components)
    *   [`<saadat-button>`](#saadat-button)
    *   [`<saadat-modal>`](#saadat-modal)
    *   [`<saadat-accordion>`](#saadat-accordion)
7.  [Utilities](#utilities)
    *   [`debounce(func, delay)`](#debouncefunc-delay)
8.  [Advanced Usage](#advanced-usage)
    *   [Theming & Customization](#theming--customization)
    *   [Integrating with Frameworks](#integrating-with-frameworks)
9.  [FAQ](#faq)
10. [Troubleshooting](#troubleshooting)
11. [Contributing](#contributing)
12. [License](#license)
13. [About the Author](#about-the-author)

---

## 1. Introduction

SaadatUI isn't just another component library; it's a toolkit built with intention. It provides a set of ready-to-use, framework-agnostic web components that are designed to be highly customizable and incredibly efficient. From simple buttons to complex modals and interactive accordions, each component is engineered to deliver a top-tier user experience while maintaining a minimal footprint.

My goal with SaadatUI was to create something that I, as a developer deeply invested in web performance and accessibility, would genuinely love to use in my own projects. It's about empowering developers to build beautiful, fast, and inclusive web applications without reinventing the wheel every time.

## 2. Why SaadatUI? My Philosophy

Look, in today's web landscape, it's easy to get bogged down by choice. There are dozens of component libraries, each with its own quirks and dependencies. My personal gripe has always been the sheer bloat many of them introduce. We often pull in massive libraries for just a handful of components, trading performance for convenience.

SaadatUI takes a different path. It's built on a few core tenets that I believe are non-negotiable for modern web development:

*   **Native First:** Where possible, we lean on native browser features. Why polyfill or abstract away something the browser already does perfectly well?
*   **Web Components for True Agnosticism:** This isn't about promoting one framework over another. Web Components are the future of reusable UI, offering true encapsulation and interoperability. You can drop SaadatUI into a React, Vue, Angular, Svelte, or vanilla JS project without a second thought. That's powerful.
*   **Performance is Paramount:** Every line of code is scrutinized for its impact on load times and runtime performance. We're talking about tiny bundle sizes, efficient rendering, and minimal JavaScript overhead. If your users are waiting, you're losing them.
*   **Accessibility Isn't an Afterthought:** This is huge for me. Building accessible UIs isn't just good practice; it's a moral imperative. Every SaadatUI component adheres to WCAG guidelines, including proper ARIA attributes, keyboard navigation, and semantic HTML. It's baked in, not bolted on.
*   **Developer Experience Matters:** While performance and accessibility are king, developer happiness is also crucial. SaadatUI aims for intuitive APIs, clear documentation, and easy customization. Because if it's a pain to use, you won't use it.

SaadatUI is my answer to the common pitfalls I've observed and experienced. It's about providing a solid foundation so you can focus on your application's unique features, not battling your UI library.

## 3. Installation

Getting SaadatUI into your project is straightforward. Choose the method that best suits your development workflow.

### NPM/Yarn

For most modern projects using a module bundler (like Webpack, Rollup, or Vite), installing via npm or yarn is the recommended approach.

```bash
# Using npm
npm install @saadatui/core

# Using yarn
yarn add @saadatui/core
```

Once installed, you can import individual components or the entire library:

```javascript
// Import a specific component
import '@saadatui/core/dist/saadat-button.js';
// Now you can use <saadat-button> in your HTML

// Or import multiple components if you prefer a single entry point
import '@saadatui/core';
// This will register all available components
```

**Note:** Importing the full `@saadatui/core` might be convenient during development, but for production, I highly recommend importing only the components you actually use. This ensures optimal bundle size and faster load times. Tree-shaking often works, but explicit imports are always safer for web components.

### CDN

If you're working on a simpler project, prototyping, or just prefer not to use a build step, you can include SaadatUI directly from a CDN.

```html
<!-- Include the full SaadatUI library (registers all components) -->
<script type="module" src="https://unpkg.com/@saadatui/core/dist/saadat-ui.js"></script>

<!-- Or, for specific components, you can target them directly -->
<script type="module" src="https://unpkg.com/@saadatui/core/dist/saadat-button.js"></script>
<script type="module" src="https://unpkg.com/@saadatui/core/dist/saadat-modal.js"></script>
```

When using the CDN, ensure your script tag has `type="module"` as SaadatUI components are ES Modules.

## 4. Quick Start

Let's get a basic button and a modal up and running in a simple HTML file.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SaadatUI Quick Start</title>
    <style>
        body { font-family: sans-serif; margin: 2rem; }
        saadat-modal::part(overlay) { background-color: rgba(0, 0, 0, 0.6); }
        saadat-modal::part(panel) { border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }
    </style>
    <!-- Import SaadatUI components (using CDN for quick example) -->
    <script type="module" src="https://unpkg.com/@saadatui/core/dist/saadat-button.js"></script>
    <script type="module" src="https://unpkg.com/@saadatui/core/dist/saadat-modal.js"></script>
</head>
<body>
    <h1>Welcome to SaadatUI!</h1>

    <p>Click the button to open a modal:</p>
    <saadat-button id="openModalButton" variant="primary">Open Saadat Modal</saadat-button>

    <saadat-modal id="myModal" header-text="Greetings from SaadatUI!" dismissible>
        <p>This is the content of your first modal. It's performant, accessible, and highly customizable.</p>
        <p>You can put any HTML content here, including other SaadatUI components!</p>
        <saadat-button slot="footer" variant="secondary" id="closeModalButton">Close</saadat-button>
    </saadat-modal>

    <script type="module">
        const openButton = document.getElementById('openModalButton');
        const modal = document.getElementById('myModal');
        const closeButton = document.getElementById('closeModalButton');

        openButton.addEventListener('click', () => {
            modal.setAttribute('open', ''); // Or modal.open = true;
        });

        closeButton.addEventListener('click', () => {
            modal.removeAttribute('open'); // Or modal.open = false;
        });

        // You can also listen for the component's own events
        modal.addEventListener('saadat-modal-closed', () => {
            console.log('Modal was closed via escape key or overlay click!');
            // Perhaps reset some form data or perform other cleanup
        });
    </script>
</body>
</html>
```

This simple example demonstrates how easy it is to integrate and interact with SaadatUI components. Notice how we're using standard HTML attributes and DOM manipulation, which is the beauty of Web Components!

## 5. Core Concepts

Understanding these underlying principles will help you get the most out of SaadatUI.

### Web Components

SaadatUI is built entirely using the [Web Components standard](https://developer.mozilla.org/en-US/docs/Web/Web_Components). This means:

*   **Custom Elements:** You define new HTML tags (like `<saadat-button>`).
*   **Shadow DOM:** Components encapsulate their internal structure, styles, and behavior, preventing conflicts with the rest of your page. This is a game-changer for maintainability.
*   **HTML Templates:** Reusable markup structures.
*   **ES Modules:** Components are delivered as standard JavaScript modules.

The key takeaway here is framework independence. If it renders HTML and runs JavaScript, it can use SaadatUI.

### Accessibility First

This isn't just a buzzword for me; it's a commitment. Every SaadatUI component is designed with WCAG (Web Content Accessibility Guidelines) in mind. This includes:

*   **Semantic HTML:** Using the right HTML elements for the job.
*   **