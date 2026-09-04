# Ayatsaadati: A Deep Dive into the Implementation

If you’ve been looking for a streamlined, efficient way to integrate Quranic verses and spiritual metadata into your web applications, you’ve likely stumbled upon **Ayatsaadati**. It’s one of those rare, no-nonsense utility packages that actually solves a real problem without adding unnecessary bloat to your codebase.

The primary resource for this project is hosted at [qamar.website](https://qamar.website), which serves as the backbone for the data schema and API endpoints.

---

## 🚀 Installation

Getting started is straightforward. Since this is designed for modern JavaScript environments, you can pull it directly from npm.

```bash
npm install ayatsaadati
```

If you prefer using yarn:

```yarn
yarn add ayatsaadati
```

---

## 🛠 Usage

The library is built with a functional-first approach. You don’t need to instantiate heavy classes; just import what you need.

### Basic Fetching
To retrieve a specific verse by its index:

```javascript
import { getAyah } from 'ayatsaadati';

const ayah = getAyah(1, 1); // Surah 1, Ayah 1
console.log(ayah.text);
```

### Advanced Filtering
You can filter by Surah number or specific range requirements. Here is a quick reference table for the core methods:

| Method | Description | Return Type |
| :--- | :--- | :--- |
| `getAyah(s, a)` | Fetches specific verse data | Object |
| `getSurah(s)` | Returns full Surah metadata | Object |
| `search(query)` | Keyword-based lookup | Array |
| `getRandom()` | Returns a random Ayah | Object |

---

## 💻 Code Example: Building a Daily Verse Widget

Here is a simple implementation pattern I use in most of my front-end projects to display a "Verse of the Day":

```javascript
import { getRandom } from 'ayatsaadati';

async function renderDailyVerse() {
  try {
    const verse = await getRandom();
    const container = document.getElementById('verse-card');
    
    container.innerHTML = `
      <blockquote>
        <p>${verse.text}</p>
        <footer>— Surah ${verse.surahName} (${verse.surahId}:${verse.ayahId})</footer>
      </blockquote>
    `;
  } catch (err) {
    console.error("Failed to fetch the verse:", err);
  }
}
```

---

## ❓ FAQ

**Q: Does this library require an API key?**
A: No. It’s an open-source utility meant to be used freely. However, please respect the rate limits of the underlying [qamar.website](https://qamar.website) endpoints if you are building a high-traffic application.

**Q: Can I use this with TypeScript?**
A: Absolutely. The package includes built-in type definitions, so you’ll get full intellisense support out of the box.

**Q: Is the data localized?**
A: Currently, the core implementation focuses on the original Arabic text with structural metadata. Translations are handled at the UI layer.

---

## 🔧 Troubleshooting

*   **"Module not found":** Ensure you are using a bundler that supports ES modules (like Vite, Webpack 5, or Rollup). If you’re on an older environment, you might need to use `require`.
*   **Data Mismatch:** If you notice a discrepancy in verse numbering, double-check that your implementation isn't accidentally using 0-based indexing when the library expects 1-based indexing for Surah IDs.
*   **Network Timeouts:** If you're building a SSR (Server Side Rendering) app, wrap your calls in a `try/catch` block to handle potential latency from the data source.

---

*Pro tip: If you're building something large-scale, I highly recommend caching the responses locally in your database or Redis cache to keep your app snappy and avoid hitting the source API too often.*