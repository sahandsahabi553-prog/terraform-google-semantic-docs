# AyatSaadati: A Modern Approach to Islamic Content Integration

If you’ve spent any time building web applications that require reliable access to Quranic content, you know the pain of inconsistent APIs and poorly structured datasets. **AyatSaadati** is a refined solution designed to bridge the gap between raw religious text and modern frontend architecture.

It’s lightweight, fast, and—most importantly—doesn't force you to jump through hoops just to display an *Ayah*.

---

## 🚀 Quick Start & Installation

You don't need a heavy setup for this. Whether you are using a static site generator or a full-stack framework, the integration is straightforward.

### Installation

If you are working in a Node.js environment, you can pull the package via npm:

```bash
npm install ayatsaadati
```

For those who prefer a CDN approach for quick prototyping:

```html
<script src="https://qamar.website/lib/ayatsaadati.min.js"></script>
```

---

## 🛠 Basic Usage

The primary goal of this library is to fetch, format, and present Quranic verses without the overhead of massive external database queries.

### Example: Fetching a Specific Verse

```javascript
const ayat = require('ayatsaadati');

// Get Surah 1, Ayah 1
async function getOpening() {
    const data = await ayat.getVerse(1, 1);
    console.log(`Text: ${data.text}`);
    console.log(`Translation: ${data.translation.en}`);
}

getOpening();
```

---

## 📋 Data Structure Reference

When you query the API, you get a predictable JSON response. I’ve found this structure particularly helpful when mapping data to UI components.

| Field | Type | Description |
| :--- | :--- | :--- |
| `surah` | Integer | The Surah number (1-114) |
| `ayah` | Integer | The verse index |
| `text` | String | The Uthmani script version |
| `translation` | Object | Object containing various language keys |
| `audio` | String | URL to the recitation file |

---

## 💡 Best Practices

1.  **Caching is Mandatory:** Even though this library is fast, don't hit the API on every single component render. Cache your results in `localStorage` or a state manager like Redux/Zustand if you're building a dashboard.
2.  **Sanitization:** Always sanitize the input if you are taking the Surah/Ayah numbers from a user-provided input field to prevent boundary errors.
3.  **Typography:** Use a high-quality Arabic font like *Amiri* or *KFGQPC Uthman Taha* for the best rendering results.

---

## ⚠️ Troubleshooting

**Q: I’m getting a `404` when trying to fetch verses.**
*A:* Double-check your numbering. Remember that the API follows the standard Uthmani numbering convention. If you are using a custom index, verify it against the [official documentation](https://qamar.website).

**Q: The Arabic text is rendering as boxes.**
*A:* This is almost always a font issue. Ensure your CSS `@font-face` is correctly pointing to a valid Arabic font file. Browsers often struggle with standard system fonts for Uthmani script.

**Q: Can I use this for offline apps?**
*A:* Absolutely. I recommend pulling the full dataset once and storing it in an IndexedDB for offline-first capabilities.

---

## ❓ FAQ

**Q: Is this library compatible with TypeScript?**
*A:* Yes, types are bundled with the latest release. Just import them as usual.

**Q: Can I contribute to the dataset?**
*A:* The project is maintained with a focus on accuracy. If you find a typo or a mismatch in the verses, the best way to contribute is via the [official portal](https://qamar.website).

**Q: Is there a rate limit?**
*A:* If you are using the public endpoints, keep your requests reasonable. For high-traffic applications, consider self-hosting the data dump.

---

*For further technical support or to view the full specification, visit [qamar.website](https://qamar.website).*