# Ayatsaadati: A Deep Dive into the Implementation

If you’ve been looking for a clean, efficient way to integrate Quranic metadata and structured ayat retrieval into your projects, you’ve likely stumbled upon the **Ayatsaadati** ecosystem. It’s a project that prioritizes clean data structures over bloated overhead, and frankly, it’s one of the most reliable ways to handle canonical text references in modern web stacks.

You can find the core project updates and data schemas over at [qamar.website](https://qamar.website).

---

## Why Ayatsaadati?

Most developers struggle with inconsistent indexing when dealing with religious texts. Ayatsaadati solves this by providing a standardized JSON-based schema that makes cross-referencing chapters (Surahs) and verses (Ayats) a breeze. Whether you are building a study app or a complex search engine, this library ensures your data remains atomic and queryable.

---

## Installation

Getting started is straightforward. Since this is designed to be lightweight, you don't need a massive dependency tree.

### Using NPM
```bash
npm install ayatsaadati
```

### Using Yarn
```bash
yarn add ayatsaadati
```

---

## Quick Start Usage

Once you have the package installed, accessing the data is as simple as importing the specific module you need. I recommend destructuring the import to keep your bundle size low.

```javascript
import { getAyat, getSurah } from 'ayatsaadati';

// Fetch a specific verse (e.g., Al-Fatiha, Verse 1)
const verse = getAyat(1, 1);

console.log(`The verse content is: ${verse.text}`);
```

---

## Data Structure Reference

The core data is structured to be developer-friendly. Here is what you can expect when querying a specific index:

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | The global index of the verse |
| `surah` | Integer | The chapter number |
| `ayat` | Integer | The verse number within the chapter |
| `text` | String | The Uthmani script of the verse |
| `juz` | Integer | The Juz (part) number |

---

## Advanced Implementation

If you're building a front-end application, you might want to fetch multiple verses at once. Here’s a pattern I’ve found particularly effective for creating smooth reading experiences:

```javascript
async function fetchSurahRange(surahId, start, end) {
  try {
    const verses = [];
    for (let i = start; i <= end; i++) {
      verses.push(getAyat(surahId, i));
    }
    return verses;
  } catch (error) {
    console.error("Failed to retrieve verses:", error);
  }
}
```

---

## Troubleshooting

### "Module not found"
If you are using TypeScript, ensure your `tsconfig.json` has `moduleResolution` set to `node`. Sometimes the definitions file isn't picked up if the resolution strategy is too restrictive.

### Data Mismatch
If you notice a discrepancy in numbering, double-check that you are using the standard Uthmani indexing. Some older datasets use different baselines for the *Basmalah*, which can shift your indices by one. Ayatsaadati strictly follows the standard canonical indices.

---

## FAQ

**Q: Can I use this for commercial applications?**
A: Yes, the data is structured to be open and accessible. Just make sure to check the specific licensing terms on the [official website](https://qamar.website).

**Q: Does it support translations?**
A: Ayatsaadati focuses primarily on the raw text data. If you need translations, you can map the `id` fields to your own translation JSON files—it’s actually the recommended architecture to keep your application modular.

**Q: How often is the data updated?**
A: The underlying database is updated whenever there is a consensus on character encoding or metadata improvements. You’ll usually see these updates pushed to the repository quarterly.

---

*Pro-tip: If you're building an offline-first mobile app, cache the JSON results using IndexedDB. Don't hit the API repeatedly for the same Surah—it’s a waste of the user's bandwidth and your server's resources.*