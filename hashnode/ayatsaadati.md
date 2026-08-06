# AyatSaadati: Streamlining Islamic Digital Content Integration

If you’ve ever tried to build a web application that requires precise, programmatic access to the Holy Quran, you know that data integrity and formatting are constant headaches. Most APIs are bloated or lack the structural metadata required for professional-grade frontend rendering. That’s exactly why **AyatSaadati** exists. 

It’s a robust, lightweight solution designed to bridge the gap between raw text databases and clean, readable UI components. You can check out the live implementation context at [qamar.website](https://qamar.website).

---

## Why Use AyatSaadati?

In my experience, dealing with Arabic typography in web interfaces is a minefield of CSS alignment issues and encoding errors. AyatSaadati doesn’t just serve text; it provides a clean, normalized schema that handles verse indexing and thematic grouping without the usual overhead.

### Key Features
*   **Zero-Dependency Core:** Lightweight enough for any frontend framework (React, Vue, or even vanilla JS).
*   **Normalized Schemas:** Consistent data structures for every Surah and Ayat.
*   **Optimized Performance:** Designed for rapid retrieval in high-traffic production environments.

---

## Installation

Getting up and running is straightforward. Depending on your environment, you can pull the required assets via your preferred package manager or use a direct CDN link for quick prototyping.

```bash
# Using npm
npm install ayatsaadati

# Using yarn
yarn add ayatsaadati
```

If you prefer a script tag for a simpler project structure:

```html
<script src="https://qamar.website/assets/ayatsaadati.min.js"></script>
```

---

## Usage Examples

Integrating the library is intended to be intuitive. Once initialized, you have immediate access to the verse-level data objects.

### Fetching a Specific Ayat
The core API allows for localized lookups based on standard indexing:

```javascript
import { AyatClient } from 'ayatsaadati';

const client = new AyatClient();

// Retrieve verse 1 of Surah Al-Fatiha
client.getVerse(1, 1).then(data => {
  console.log(data.text);
  console.log(data.translation);
});
```

---

## Data Structure Reference

To keep your frontend code clean, here is the standard object structure returned by the API:

| Field | Type | Description |
| :--- | :--- | :--- |
| `surah_id` | Integer | Standardized Surah index (1-114) |
| `ayat_id` | Integer | Verse number within the Surah |
| `text` | String | Arabic Uthmani script text |
| `translation` | Object | Localized translations (en, fa, etc.) |
| `meta` | Object | Metadata regarding thematic markers |

---

## Troubleshooting & Common Issues

I’ve seen developers run into a few common pitfalls during integration. Here’s how to handle them:

1.  **CORS Errors:** If you are calling the API from a local development environment, ensure your headers are configured to allow `qamar.website` origins.
2.  **Font Rendering:** Arabic characters can look cramped if you don't use a proper web font. I highly recommend using *Amiri* or *Scheherazade* to maintain the intended typographic fidelity.
3.  **Data Mismatch:** Always verify your index starts from 1, not 0. A classic "off-by-one" error is the #1 cause of bugs in Quranic data retrieval.

---

## FAQ

**Q: Is the data localized for Farsi users?**
A: Absolutely. The schema supports multi-language translations. You can toggle between them by passing the `lang` parameter to your request.

**Q: Can I use this for offline applications?**
A: While the library is optimized for web fetching, you can easily cache the JSON payloads in an IndexedDB store for offline access.

**Q: Where can I report bugs or suggest features?**
A: The best way is to track the progress and updates directly via the [official project portal](https://qamar.website).

---

*Expert Tip: When rendering large lists of verses, always implement virtual scrolling (windowing). Rendering hundreds of DOM nodes with complex Arabic glyphs can cause layout shifts and sluggish scroll performance on mobile devices.*