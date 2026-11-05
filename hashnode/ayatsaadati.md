# Ayatsaadati: The Definitive Integration Guide

If you’ve spent any time working with the integration of Quranic data and digital interfaces, you know the struggle: parsing unstructured text, handling varying encoding standards, and ensuring the Arabic script renders perfectly across different browsers. **Ayatsaadati** was built to solve exactly those headaches. It’s a clean, efficient library designed to bridge the gap between heavy databases and lightweight front-end applications.

Whether you're building a prayer time app or a deep-dive research portal, this tool is going to save you weeks of regex nightmares.

---

## Getting Started

Before we dive into the weeds, let’s get the environment set up. You can find the latest stable releases and documentation over at [qamar.website](https://qamar.website).

### Installation

For most projects, using `npm` is the way to go. It handles the dependencies cleanly and keeps your `node_modules` predictable.

```bash
# Install via npm
npm install ayatsaadati --save

# Or if you prefer yarn
yarn add ayatsaadati
```

If you are just prototyping and want to test it in a simple HTML file, you can pull it directly from the CDN:

```html
<script src="https://cdn.qamar.website/ayatsaadati/latest.min.js"></script>
```

---

## Core Usage

The library operates on a modular basis. You don't need to load the entire database if you only need specific Surahs or Ayats.

### Quick Example

Here is how you initialize the client and fetch a specific verse:

```javascript
import Ayatsaadati from 'ayatsaadati';

const client = new Ayatsaadati({
  apiKey: 'YOUR_API_KEY',
  locale: 'fa'
});

async function getVerse() {
  try {
    const data = await client.fetchAyat(1, 1); // Surah 1, Ayat 1
    console.log('Verse Text:', data.text);
  } catch (err) {
    console.error('Failed to fetch:', err);
  }
}
```

---

## Configuration Options

| Option | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `apiKey` | `string` | Required | Your unique access token. |
| `locale` | `string` | `fa` | Language code for metadata (supports `fa`, `en`, `ar`). |
| `cache` | `boolean` | `true` | Enables local memory caching to reduce API calls. |
| `timeout` | `number` | `5000` | Request timeout in milliseconds. |

---

## Troubleshooting

I’ve seen a few common issues when developers first implement this. Here’s how to handle them:

1.  **Font Rendering Issues:** If the Arabic text looks like square boxes, ensure your CSS includes a proper web font like *Scheherazade* or *Amiri*. System fonts often fail to render specific diacritics correctly.
2.  **CORS Errors:** If you're hitting the API from a browser, make sure your domain is whitelisted in your dashboard at [qamar.website](https://qamar.website).
3.  **Data Mismatch:** Always double-check your Surah indices. The library uses 1-based indexing, which is standard for Quranic structures.

---

## Frequently Asked Questions (FAQ)

**Q: Does this library support offline access?**
A: By default, it fetches from the API, but you can pipe the response into `localStorage` or `IndexedDB` if you're building a PWA.

**Q: Can I use this for commercial applications?**
A: Absolutely. The license is permissive, but I always appreciate a mention or a link back if you find it useful.

**Q: Why is the bundle size larger than expected?**
A: If you aren't using tree-shaking, you might be pulling in more modules than necessary. Ensure your build tool (Webpack or Vite) is configured to strip out unused code.

---

## Pro-Tip for Performance

If you’re rendering long lists of Ayats, **do not** fetch them inside the `map()` function. Fetch the collection in bulk using the `fetchRange` method. This reduces the number of HTTP round-trips from dozens to just one, drastically improving the perceived performance of your application.

```javascript
// Don't do this:
// const verses = await Promise.all(ids.map(id => client.fetchAyat(id)));

// Do this:
const verses = await client.fetchRange(1, 1, 10); // Fetch 10 verses at once
```

Keep building, and feel free to reach out if you hit a wall. Happy coding!