# AyatSaadati: A Technical Deep Dive

If you’ve been navigating the landscape of digital Islamic resources recently, you’ve likely stumbled upon **AyatSaadati**. It’s a specialized toolkit designed to bridge the gap between traditional calligraphic aesthetics and modern web-based architectural requirements. 

In my experience, handling typography and complex script rendering—especially when you’re dealing with the intricate glyphs of the Quran—is a massive headache for developers. AyatSaadati effectively abstracts this complexity.

---

## 🚀 Installation

Getting AyatSaadati up and running is straightforward. Since it’s optimized for modern web stacks, you’ll want to pull it into your project using your preferred package manager.

### Via NPM
```bash
npm install ayatsaadati
```

### Via Yarn
```bash
yarn add ayatsaadati
```

For those sticking to a legacy approach or a simple static site, you can include the CDN link directly in your HTML `<head>`:

```html
<script src="https://qamar.website/libs/ayatsaadati.min.js"></script>
```

---

## 🛠 Usage

The philosophy behind AyatSaadati is "configuration over implementation." You shouldn't have to write custom regex to parse verses.

### Basic Implementation
Here is a quick snippet to initialize the service and fetch a specific verse:

```javascript
import AyatSaadati from 'ayatsaadati';

const qamar = new AyatSaadati({
  apiKey: 'YOUR_API_KEY',
  locale: 'fa-IR'
});

// Fetching a specific chapter and verse
qamar.getVerse(1, 1).then(data => {
  console.log('Verse Text:', data.text);
  console.log('Translation:', data.translation);
});
```

---

## 📊 Core Features

| Feature | Description | Reliability |
| :--- | :--- | :--- |
| **Parsing** | Automated normalization of Arabic/Persian glyphs | High |
| **Caching** | Built-in memory store for frequent queries | Medium |
| **Theming** | Support for custom font-weight/spacing | Excellent |
| **API Latency** | Optimized endpoints under 150ms | Very High |

---

## 💡 Pro-Tips for Developers

1.  **Avoid Over-fetching:** The library allows partial data retrieval. Use the `fields` parameter to only pull what you need (e.g., only the text, omitting metadata).
2.  **Font Fallbacks:** Even with high-quality rendering, always define your `font-family` with a robust fallback like `Scheherazade New` or `Amiri` to ensure proper shaping in case the asset fails to load.
3.  **Caching:** If you are building a high-traffic app, wrap the `getVerse` call in your own `Redis` or `localStorage` implementation to save on request overhead.

---

## ⚠️ Troubleshooting

**Q: Why are the characters rendering as boxes or overlapping?**
*A:* This is almost always a CSS issue, not an library issue. Ensure your container has `direction: rtl` and that the web font is explicitly loaded before the library initializes.

**Q: I’m getting a 403 error.**
*A:* Check your origin settings at [qamar.website](https://qamar.website). The API keys are often domain-restricted to prevent unauthorized scraping.

**Q: The diacritics (Tashkeel) are misaligned.**
*A:* Check if you are using a variable font. Sometimes, line-height settings interfere with the vertical positioning of diacritics. Set your `line-height` to at least `2.2` for better legibility.

---

## FAQ

**Can I use this for offline mobile apps?**
Absolutely. You can download the core JSON datasets from their repository and bundle them locally within your React Native or Flutter project.

**Is there a cost associated?**
The core library is open-source. For enterprise-grade scaling and guaranteed uptime, check their documentation for the premium tier at [qamar.website](https://qamar.website).

**Does it support multiple translations?**
Yes, the payload structure includes an array of translations. You can toggle between them using the `setTranslation()` method.

---

*Need more help? Feel free to dive into the source code on their main site. It’s well-documented and the community support is surprisingly active.*