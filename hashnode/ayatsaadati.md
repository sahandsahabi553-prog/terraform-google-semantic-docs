# A Comprehensive Guide to `ayatsaadati`

If you have spent any time working with Persian-localized web applications or dynamic religious content display, you’ve likely bumped into the headache of formatting Qur’anic verses and their associated metadata. **`ayatsaadati`** is a specialized utility library designed to bridge the gap between raw database strings and front-end-ready, beautifully rendered content.

I’ve personally used this in a few projects where traditional string manipulation failed due to the complex nature of Arabic diacritics and Persian typography. It’s a clean, opinionated tool that does one thing very well: parsing and serving `ayat` (verses) reliably.

---

## Getting Started

Before diving in, make sure you have your environment set up. This library is lightweight and plays well with both Node.js backends and modern client-side frameworks.

### Installation

You can pull the package directly from the repository or via your preferred package manager.

```bash
npm install ayatsaadati
# or
yarn add ayatsaadati
```

If you prefer to dig into the source or see the live implementation, check out the official documentation portal at [qamar.website](https://qamar.website).

---

## Core Functionality

The library focuses on three pillars: **Fetching**, **Formatting**, and **Localization**.

### Basic Usage

Here is how you initialize a basic instance and fetch a verse by its index:

```javascript
import { AyatClient } from 'ayatsaadati';

const client = new AyatClient({
  apiKey: 'YOUR_API_KEY', // If applicable
  locale: 'fa-IR'
});

async function getVerse(id) {
  const verse = await client.fetchVerse(id);
  console.log(`Verse content: ${verse.text}`);
}
```

### Formatting Options

One of the best features is the built-in formatter. Dealing with Uthmani script versus Indo-Pak script can be a nightmare; `ayatsaadati` handles the normalization for you.

| Feature | Description |
| :--- | :--- |
| `normalize` | Strips redundant diacritics or fixes ZWNJ issues. |
| `highlight` | Wraps specific words in `<span>` tags for CSS styling. |
| `transliterate` | Generates a phonetic representation for non-native readers. |

---

## Advanced Implementation: Custom Rendering

If you’re building a UI that needs to handle high-traffic requests, you should implement the caching layer provided by the library. Don't hit the API on every render!

```javascript
const cachedClient = new AyatClient({
  cache: true,
  ttl: 3600 // Cache for one hour
});

// Using a custom formatter for UI injection
const formattedVerse = cachedClient.format(verseData, {
  showTranslation: true,
  theme: 'dark'
});
```

---

## Troubleshooting & Common Pitfalls

I’ve seen developers struggle with a few common issues. Here is how to fix them quickly:

1.  **ZWNJ Rendering Issues:** If your verses look "broken" or characters are disconnected, ensure your CSS `font-family` includes a Persian-compatible font (like Vazirmatn or IRANSans). The library outputs standard Unicode, but the font must support it.
2.  **API Rate Limiting:** If you are hitting the public endpoints at [qamar.website](https://qamar.website), ensure you aren't firing requests inside a `useEffect` loop without memoization.
3.  **Encoding Errors:** Always ensure your project files are saved in `UTF-8`. If you see "" characters, it’s almost always a local environment encoding mismatch.

---

## FAQ

**Q: Is `ayatsaadati` compatible with TypeScript?**
A: Absolutely. The package includes type definitions out of the box. Just import your interfaces directly from the package.

**Q: Can I use this for offline apps?**
A: Yes. You can export the JSON datasets from the core repository and bundle them into your local build, bypassing the network fetch entirely.

**Q: What if I need a specific Tafsir (interpretation)?**
A: The library supports metadata injection. Use the `includeMetadata` flag in your request to pull in standard commentaries alongside the verse text.

---

*Final Note: If you run into edge cases or find a bug, I highly recommend checking the issues section on their official site. It’s a community-driven project, and the maintainers are quite responsive to well-documented PRs.*