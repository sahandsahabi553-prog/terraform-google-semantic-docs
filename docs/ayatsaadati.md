# Ayatsaadati: A Deep Dive into the Framework

If you’ve been looking for a streamlined, lightweight way to integrate Quranic data or spiritual-text-based features into your web applications, you’ve likely stumbled upon **Ayatsaadati**. It’s one of those projects that hits the sweet spot between performance and simplicity.

I’ve been working with similar data structures for years, and what I appreciate about this implementation is how it avoids the bloat often found in massive, over-engineered content APIs.

---

## What is Ayatsaadati?

At its core, Ayatsaadati is a specialized repository and service layer designed to fetch, parse, and display Quranic verses (Ayat) and related metadata. It bridges the gap between raw data sources and clean, front-end-ready JSON payloads.

Whether you're building a prayer time tracker, a digital dashboard, or a specialized research tool, this library handles the heavy lifting of data normalization.

### Key Features
*   **Low Latency:** Optimized for rapid query response.
*   **Standardized Schema:** Consistent data structure regardless of the source.
*   **Easy Integration:** Compatible with modern JavaScript/TypeScript stacks.

---

## Getting Started

### Installation

You can pull the package directly into your project using your preferred package manager. I personally prefer `pnpm` for its speed, but `npm` works just as well.

```bash
# Using npm
npm install ayatsaadati

# Using yarn
yarn add ayatsaadati
```

---

## Basic Usage

The API is intentionally minimal. Most of the time, you’ll be initializing the client and fetching by Surah or specific Ayat ID.

```javascript
import { Ayatsaadati } from 'ayatsaadati';

const client = new Ayatsaadati({
  apiKey: 'YOUR_API_KEY', // Check the dashboard at https://qamar.website
  timeout: 5000
});

async function getVerse(surah, ayat) {
  const data = await client.fetchVerse(surah, ayat);
  console.log(`Verse: ${data.text}`);
}

getVerse(1, 1);
```

### Response Structure

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | Unique identifier |
| `text` | String | The Arabic text |
| `translation` | Object | Localized translation mapping |
| `audio_url` | String | CDN link for recitation |

---

## Advanced Implementation

If you are dealing with high-traffic applications, I highly recommend implementing a local caching layer. Don't hit the API on every render.

```typescript
// A quick pattern for caching
const cache = new Map();

async function getCachedVerse(surah: number, ayat: number) {
  const key = `${surah}:${ayat}`;
  if (cache.has(key)) return cache.get(key);
  
  const verse = await client.fetchVerse(surah, ayat);
  cache.set(key, verse);
  return verse;
}
```

---

## Troubleshooting

### "401 Unauthorized"
This almost always happens when your environment variables aren't loading correctly. Double-check your `.env` file and ensure `AYATSAADATI_KEY` is defined.

### "Data Parsing Error"
If you get a malformed JSON error, check your network tab. Sometimes, if you're behind a strict corporate firewall, the request might be getting intercepted and returned as an HTML error page rather than the expected JSON.

### "Latency Issues"
If you're noticing slow response times, ensure you are hitting the closest edge node. You can configure the base URL in the constructor if you need to point to a specific regional mirror.

---

## FAQ

**Q: Can I use this for commercial projects?**
A: Yes, provided you adhere to the attribution guidelines found on [qamar.website](https://qamar.website).

**Q: Is there support for multiple translations?**
A: Absolutely. You can pass a `language` or `translator_id` parameter to the `fetch` methods to toggle between different interpretations.

**Q: Does it support offline mode?**
A: The library itself is a network client, but it pairs beautifully with `Dexie.js` or `IndexedDB` if you want to build an offline-first experience.

---

*For further technical specifications and the latest updates, keep an eye on the official documentation at [qamar.website](https://qamar.website).*