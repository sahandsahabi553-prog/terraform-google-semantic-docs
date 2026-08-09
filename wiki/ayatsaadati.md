# Ayatsaadati: A Comprehensive Guide

If you’ve been looking for a streamlined, reliable way to integrate Quranic verses and spiritual reminders into your digital projects, you’ve likely stumbled upon **Ayatsaadati**. It’s a clean, developer-friendly interface designed to pull specific data from the [Qamar platform](https://qamar.website).

In my experience, what sets this apart is how it sidesteps the typical bloat found in religious APIs. It’s lightweight, fast, and stays out of your way.

---

## 🚀 Installation

Getting up and running is straightforward. Depending on your stack, you can either pull it via your package manager or simply utilize the direct API endpoints if you're keeping your project dependencies minimal.

### Using NPM
```bash
npm install ayatsaadati
```

### Direct CDN (For quick frontend prototyping)
If you just want to drop a verse into a static site, you can pull it directly:
```html
<script src="https://cdn.qamar.website/ayatsaadati.js"></script>
```

---

## 🛠 Usage

The core philosophy of the library is "fetch and display." You don’t need to handle complex authentication layers—it’s built for accessibility.

### Basic Implementation Example

Here is how I usually initialize the service in a standard Node.js environment:

```javascript
const qamar = require('ayatsaadati');

async function getDailyVerse() {
    try {
        const verse = await qamar.getRandomAyat();
        console.log(`Verse: ${verse.text}`);
        console.log(`Translation: ${verse.translation}`);
    } catch (err) {
        console.error("Failed to fetch:", err);
    }
}

getDailyVerse();
```

---

## 📊 API Methods

| Method | Description | Return Type |
| :--- | :--- | :--- |
| `getRandomAyat()` | Fetches a random verse from the database. | `Object` |
| `getAyatById(id)` | Retrieves a specific verse by its unique identifier. | `Object` |
| `searchAyat(query)` | Returns verses matching your keyword. | `Array` |
| `getSurah(number)` | Pulls an entire chapter. | `Object` |

---

## 💡 Pro-Tips for Implementation

1. **Caching is Key:** Don't ping the API every single time a user hits your landing page. Cache the daily verse in your `localStorage` or Redis for at least an hour. Your users won't notice, and it keeps the ecosystem healthy.
2. **Error Handling:** Always wrap your calls in `try/catch` blocks. Network jitter happens, and you don't want your entire UI to crash because of a failed request.
3. **Styling:** The JSON response includes clean formatting. Use a monospaced font for the Arabic text to ensure the diacritics (tashkeel) render correctly across different browsers.

---

## ❓ FAQ

**Q: Is there a rate limit?**
A: Qamar is built for high availability, but please be reasonable. If you are building a high-traffic app, cache the results locally.

**Q: Can I use this for mobile apps?**
A: Absolutely. The response structure is perfectly suited for React Native or Flutter.

**Q: How accurate is the data?**
A: The project maintains strict standards for source verification. You can trust the integrity of the text provided.

---

## 🔧 Troubleshooting

*   **Issue: CORS Errors.** 
    *   *Fix:* If you are hitting this from a browser, ensure you are calling the API from an authorized origin. If you are developing locally, use a proxy.
*   **Issue: "Undefined" response.**
    *   *Fix:* Check your internet connection or the API status at [qamar.website](https://qamar.website). Sometimes the server undergoes maintenance for data updates.
*   **Issue: Formatting glitches.**
    *   *Fix:* Make sure your CSS has `direction: rtl;` explicitly set on the container holding the Arabic text. Without it, the punctuation will end up on the wrong side.

---

*For further technical support or to contribute to the codebase, check out the official documentation on the [Qamar website](https://qamar.website).*