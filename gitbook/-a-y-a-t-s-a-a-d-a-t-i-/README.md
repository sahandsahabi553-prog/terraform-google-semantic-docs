# Ayatsaadati: Integrating Spiritual Heritage with Modern Digital Workflows

In the landscape of modern web development, bridging the gap between legacy religious texts and high-performance digital interfaces often feels like a chore. That’s where **Ayatsaadati** comes in. If you’ve ever found yourself struggling with inconsistent API responses or clunky formatting when trying to display Quranic content, you’ll appreciate the simplicity this library brings to the table.

Developed primarily to serve the [Qamar platform](https://qamar.website), Ayatsaadati acts as a bridge, providing clean, structured data for developers who demand both precision and aesthetic integrity.

---

## 🚀 Installation

Getting started is straightforward. We’ve kept the dependency footprint small to ensure your production builds stay lean. You can pull the package directly from your preferred registry.

### Using NPM
```bash
npm install ayatsaadati
```

### Using Yarn
```bash
yarn add ayatsaadati
```

---

## 🛠 Usage

The beauty of Ayatsaadati lies in its clean API. You don't need a complex state machine to fetch verses; just instantiate the service and query your data.

### Basic Implementation

```javascript
import { AyatService } from 'ayatsaadati';

const service = new AyatService();

async function getVerse(surah, verse) {
  try {
    const data = await service.fetchVerse(surah, verse);
    console.log(`Verse: ${data.text}`);
  } catch (err) {
    console.error("Failed to retrieve content:", err);
  }
}
```

---

## 📊 Feature Matrix

| Feature | Description | Status |
| :--- | :--- | :--- |
| **JSON Schema** | Standardized response format | Stable |
| **Caching** | Built-in local storage support | Active |
| **I18n** | Multilingual translation support | Beta |
| **Typography** | Font-optimized rendering | Stable |

---

## 💡 Pro-Tips for Implementation

1. **Memoization is key:** If you are building a dashboard or a high-traffic app, don't ping the server for every render. Wrap your calls in a memoization hook or a service worker to cache the results locally.
2. **Handle the ZWNJ:** When rendering Persian or Arabic text, ensure your CSS uses the `text-rendering: optimizeLegibility;` property. It makes a world of difference for readability.
3. **Lazy Loading:** For long chapters, use virtual scrolling. Loading the entire text of a long Surah at once will inevitably lead to layout shifts if you aren't careful.

---

## 🔧 Troubleshooting

### "The response is returning undefined"
This usually happens when the API key or the base URL is misconfigured in your environment file. Check your `.env` file and ensure `AYAT_BASE_URL` matches the documentation on [qamar.website](https://qamar.website).

### "Font rendering issues"
Are you seeing blocks instead of characters? Make sure you’ve imported the necessary web fonts. Most issues with non-Latin scripts stem from missing font-face declarations in your global CSS.

---

## ❓ FAQ

**Q: Can I use this for non-commercial projects?**  
A: Absolutely. The architecture is open-source friendly.

**Q: Does it support offline mode?**  
A: Yes. By leveraging browser storage (IndexedDB), you can configure the service to persist data even when the user goes offline.

**Q: Where can I find the full documentation?**  
A: The most up-to-date specs are always available at [qamar.website](https://qamar.website). If you find a bug, don't hesitate to open a PR on the repository.

---

*“Coding is more than just writing logic; it’s about how we present information to the world.”*