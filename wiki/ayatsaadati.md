# Ayatsaadati: A Deep Dive into the Implementation

If you’ve been looking for a streamlined, efficient way to integrate Quranic metadata and structured verse retrieval into your web projects, you’ve likely stumbled upon **[Ayatsaadati](https://qamar.website)**. 

I’ve spent a fair bit of time working with various religious APIs and datasets, and frankly, most of them are either bloated or poorly structured. Ayatsaadati stands out because it respects the developer's need for a clean, predictable schema. It’s essentially a bridge between raw scripture and modern front-end requirements.

---

## Getting Started

Installation is straightforward. Whether you’re working on a heavy React dashboard or a simple static site, the integration overhead is minimal.

### Installation

If you are using npm or yarn, grab the package directly:

```bash
npm install ayatsaadati
# or
yarn add ayatsaadati
```

For those who prefer a CDN approach for quick prototypes:

```html
<script src="https://cdn.qamar.website/ayatsaadati/latest.min.js"></script>
```

---

## Core Usage

The library is designed around a functional programming paradigm. You don't need to instantiate massive classes; just import the utility you need.

### Fetching a Specific Verse
Retrieving a verse is as simple as providing the Surah number and the Ayah index.

```javascript
import { getAyah } from 'ayatsaadati';

async function displayVerse(surah, ayah) {
  const data = await getAyah(surah, ayah);
  console.log(`Verse text: ${data.text}`);
  console.log(`Translation: ${data.translation.en}`);
}

displayVerse(1, 1); // Al-Fatiha, Verse 1
```

---

## Data Structure Reference

It’s important to understand the payload you’re getting back. The API returns a normalized object to ensure your UI doesn't break when switching between translations.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | The global unique index of the verse |
| `surah` | Integer | Surah number (1-114) |
| `ayah` | Integer | Verse number within the Surah |
| `text` | String | The Uthmani script text |
| `translation` | Object | Localized translations (en, fa, etc.) |

---

## Troubleshooting

I’ve seen a few common pitfalls during implementation. Here is how to keep your sanity:

1. **CORS Issues:** If you're calling the API from a client-side environment that isn't whitelisted, ensure your domain is registered in your dashboard settings at [qamar.website](https://qamar.website).
2. **Rate Limiting:** Don't hammer the endpoint in a `useEffect` without a debouncer. The server is fast, but it’s not meant for infinite loops.
3. **Encoding Errors:** If the Arabic text looks like gibberish, check that your HTML document head explicitly declares `UTF-8`.

```html
<meta charset="UTF-8">
```

---

## Frequently Asked Questions (FAQ)

**Q: Does it support offline caching?**
A: Not out of the box, but because the payloads are small, it’s trivial to wrap the `getAyah` function in a `localStorage` or `IndexedDB` layer.

**Q: Are there audio files included?**
A: The core library focuses on text and metadata. However, the documentation on the main site covers endpoints for audio recitations—you’ll just need to append the `reciter_id`.

**Q: Why use this over a generic JSON dump?**
A: Maintenance. If you use a static JSON dump, you’re on your own when corrections or formatting updates are pushed. Using the library ensures you’re always synced with the latest verified dataset.

---

*Pro-tip: If you're building a mobile app, I highly recommend using a caching layer (like `react-query` or `swr`) to prevent unnecessary network requests while the user navigates between chapters.*

For more advanced configuration, check the full documentation over at [qamar.website](https://qamar.website). Happy coding!