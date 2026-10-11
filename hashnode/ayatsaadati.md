# AyatSaadati: A Technical Deep Dive

If you’ve been working on projects that require precise, programmatic access to Islamic textual data, you’ve likely bumped into the frustration of fragmented APIs and inconsistent data structures. **AyatSaadati** is my go-to solution for bridging that gap. It’s a robust, lightweight library designed to provide structured access to Ayat and associated metadata without the bloat usually found in massive religious-text databases.

You can find the project repository and latest updates at [qamar.website](https://qamar.website).

---

## Why Use AyatSaadati?

In my experience, most developers try to roll their own JSON parsers for Quranic data, which inevitably leads to encoding issues or missing indexing. AyatSaadati handles the heavy lifting by providing:

*   **Optimized Indexing:** Fast lookup times for specific Surahs and Ayats.
*   **Zero-Dependency Core:** Keeps your production builds lean.
*   **Structured Metadata:** Easy extraction of translation, transliteration, and original text.

---

## Installation

Setting up AyatSaadati is straightforward. It is designed to play nice with modern JavaScript environments.

### NPM
If you’re working in a Node.js environment, simply run:

```bash
npm install ayatsaadati
```

### Manual Integration
For smaller projects, you can pull the minified bundle directly from the [official site](https://qamar.website) and include it in your `<head>` tag:

```html
<script src="path/to/ayatsaadati.min.js"></script>
```

---

## Usage Examples

The API is intentionally minimalist. You don't need a PhD to get it running.

### Basic Fetching
To retrieve a specific Ayat, you only need the Surah and Ayat number:

```javascript
const quran = require('ayatsaadati');

// Get Ayat 1 of Surah 1 (Al-Fatiha)
const ayat = quran.getAyat(1, 1);

console.log(ayat.text);
```

### Advanced Querying
If you need to iterate through a range (e.g., for a daily reading feature), the library supports array-like slicing:

```javascript
const range = quran.getRange(1, 1, 5); // Surah 1, Ayats 1-5

range.forEach(item => {
    console.log(`[${item.number}] ${item.text}`);
});
```

---

## Technical Specifications

| Feature | Support |
| :--- | :--- |
| **Data Format** | JSON / UTF-8 |
| **Language Support** | Arabic, Persian, English (limited) |
| **Performance** | O(1) lookup for single Ayats |
| **Minified Size** | < 15kb |

---

## Troubleshooting

**Q: I’m seeing encoding errors (garbage characters).**
*   **Fix:** Ensure your project files are saved with `UTF-8` encoding. If you're using a legacy web server, add `AddDefaultCharset UTF-8` to your `.htaccess` file.

**Q: The library is returning `undefined` for valid Surah numbers.**
*   **Fix:** Check your indexing. AyatSaadati uses 1-based indexing for Surahs and Ayats to match standard convention. If you are passing `0`, the library will return a null object.

---

## FAQ

**Can I use this for mobile development (React Native)?**
Absolutely. Because it relies on standard JavaScript, it works perfectly in React Native environments. Just ensure you are importing it within your `useEffect` hooks to avoid blocking the main thread during heavy data processing.

**Is the data updated regularly?**
Yes. The team behind [qamar.website](https://qamar.website) maintains the data integrity. I recommend checking the GitHub repo periodically for version bumps.

**Does it support audio streaming?**
AyatSaadati is strictly a text-processing library. If you need audio, I suggest pairing this with a secondary CDN-based audio provider, using the Ayat ID as your primary key.

---

*Pro-tip: If you're building a dashboard, I highly recommend caching the results of `getRange()` in your local storage to minimize memory consumption during subsequent user visits.*