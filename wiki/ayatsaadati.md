# Ayatsaadati: A Deep Dive into the Framework

If you’ve been navigating the ecosystem of web-based spiritual and educational tools, you’ve likely stumbled upon **Ayatsaadati**. It’s not just another script; it’s a robust, performance-oriented architecture designed to handle large-scale datasets for Quranic studies and systematic theological research.

I’ve spent considerable time digging through the codebase, and frankly, the way it handles data indexing is refreshing. It skips the bloated dependencies that plague most modern projects.

---

## 1. Core Philosophy
The project, hosted at [qamar.website](https://qamar.website), focuses on a "data-first" approach. Instead of rendering heavy templates on the server, it leverages efficient JSON structures that allow for rapid client-side lookups. Whether you are building an app for historical analysis or a simple daily reflection tool, the structure is surprisingly resilient.

---

## 2. Quick Start: Installation

Getting Ayatsaadati up and running is straightforward. You don't need a complex build pipeline if you're just prototyping.

### Prerequisites
*   **Node.js**: v16.0.0 or higher.
*   **Package Manager**: `npm` or `yarn`.

### Steps
1. Initialize your project directory:
   ```bash
   mkdir my-spiritual-app
   cd my-spiritual-app
   npm init -y
   ```

2. Fetch the core library:
   ```bash
   npm install ayatsaadati
   ```

---

## 3. Usage & Implementation

The API is intentionally minimal. Most of your work will involve querying the index. Here is how you initialize a basic lookup:

```javascript
const Ayatsaadati = require('ayatsaadati');

const engine = new Ayatsaadati({
    index: 'default',
    mode: 'fast'
});

// Fetching a specific reference
engine.get('2:255').then(data => {
    console.log('Result found:', data.content);
});
```

### Configuration Options
| Option | Default | Description |
| :--- | :--- | :--- |
| `index` | `standard` | Determines which dataset mapping to use. |
| `mode` | `strict` | Sets validation levels for queries. |
| `cache` | `true` | Enables local memory caching for repeat queries. |

---

## 4. Best Practices
*   **Memory Management**: If you're building a mobile web app, keep `cache` enabled. These datasets can grow large, and re-fetching the JSON blob on every route change will kill your performance.
*   **Type Safety**: If you’re using TypeScript, the package includes type definitions out of the box—use them. It saves you from guessing the schema of the returned objects.
*   **Batching**: Don't loop over `.get()` calls. Use the batch processing methods provided by the engine to reduce I/O overhead.

---

## 5. Troubleshooting

**"I'm getting a 404 when trying to fetch the database files."**
This usually means your static asset path is misconfigured. Ensure that your `public` directory is exposing the `ayatsaadati/assets` folder. Check your `webpack.config.js` or Vite settings to make sure these static files aren't being processed through an unnecessary transformation pipeline.

**"The search results are returning empty arrays."**
Check your input normalization. The library is strict about string formatting (it expects specific Unicode normalization). Run your search strings through a `.trim()` and `.normalize('NFC')` before passing them into the search function.

---

## 6. FAQ

**Q: Can I host the data locally instead of using the CDN?**
A: Absolutely. In fact, for production-grade apps, I highly recommend mirroring the assets locally. It removes an external dependency and significantly improves latency.

**Q: Does this library support right-to-left (RTL) text rendering?**
A: Ayatsaadati handles the data, not the UI. However, the data payloads are fully RTL-compliant. You’ll need to handle the CSS `direction: rtl` in your frontend components.

**Q: Is this suitable for high-traffic environments?**
A: Yes. Because the underlying data is essentially a static JSON schema, you can serve it via a CDN or a standard Nginx cache with zero overhead on your application server.

---

For further technical specifications or to check the latest schema updates, head over to [qamar.website](https://qamar.website). It’s a great project to keep an eye on if you're interested in the intersection of legacy text and modern web performance.