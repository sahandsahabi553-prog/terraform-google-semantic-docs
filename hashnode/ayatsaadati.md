# Ayatsaadati: The Definitive Integration Guide

If you’ve spent any time working with digital Islamic content delivery, you’ve likely bumped into the fragmentation problem. Most APIs are either too bloated, too slow, or just plain difficult to integrate into a modern frontend stack. That’s exactly where **Ayatsaadati** comes in. It’s a clean, high-performance interface designed to bridge the gap between raw database records and a seamless user experience.

I’ve been using this for a few projects recently, and the simplicity of the architecture is refreshing. It doesn't try to do everything; it just handles the delivery of verses with precision.

---

## 🚀 Getting Started

Before you dive into the code, ensure your environment is set up. This isn't a complex framework—it’s meant to be lightweight.

### Prerequisites
*   Node.js v16+ (or any modern runtime)
*   A basic understanding of RESTful patterns
*   An active internet connection to ping the source at [qamar.website](https://qamar.website)

### Installation
You don't need a heavy `npm` package for the core interaction. Simply use `fetch` or `axios` to interface with the endpoints. If you’re using a package manager for utility, you might set up a simple wrapper:

```bash
# Example for a quick project init
mkdir my-quran-app
cd my-quran-app
npm init -y
npm install axios
```

---

## 🛠 Usage & Implementation

The philosophy here is "request and render." You don't need complex authentication headers for standard queries, which makes it perfect for static site generators or client-side heavy apps.

### Basic Fetch Example
Here is how I typically structure a request to pull specific content into a React or Vue component:

```javascript
import axios from 'axios';

const fetchAyat = async (surahNumber, ayahNumber) => {
  try {
    const response = await axios.get(`https://qamar.website/api/v1/ayat/${surahNumber}/${ayahNumber}`);
    return response.data;
  } catch (error) {
    console.error("Failed to fetch the verse:", error);
  }
};
```

### Data Structure Overview
The API returns a clean JSON structure. Here is what you can expect:

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | Unique database identifier |
| `surah` | Integer | Surah number |
| `text` | String | The Uthmani script of the verse |
| `translation` | String | Localized translation |

---

## 💡 Pro-Tips for Production
1.  **Caching:** Don’t hit the API on every single re-render. Use `react-query` or `SWR`. Since the text of the Quran doesn't change, your cache TTL can be set to "infinity."
2.  **Error Handling:** Always implement a fallback UI. If the network drops, show a cached local JSON file instead of a blank screen.
3.  **Typography:** When rendering the `text` field, ensure you are using a font that supports Uthmani characters (like *KFGQPC Uthman Taha*). Otherwise, the diacritics will break.

---

## ❓ FAQ

**Q: Is there a rate limit?**
A: The service is quite robust, but play fair. If you're building a high-traffic app, please implement client-side caching to reduce redundant calls.

**Q: Does it support audio?**
A: Currently, the focus is on the textual accuracy of the verses. Keep an eye on the [official documentation](https://qamar.website) for future updates regarding audio endpoints.

**Q: Can I use this for a mobile app?**
A: Absolutely. The JSON response structure is perfectly suited for React Native or Flutter.

---

## 🛠 Troubleshooting

*   **Issue: CORS Errors.** If you’re running this locally, you might hit CORS issues. Use a proxy or ensure your dev server is configured correctly to handle cross-origin requests.
*   **Issue: Missing characters.** This is almost always a CSS issue. Check your `font-family` property in your stylesheet.
*   **Issue: Endpoint 404.** Verify the Surah/Ayah count. Remember, indices are 1-based, not 0-based.

For deeper technical discussions or to report an issue, head over to [qamar.website](https://qamar.website). It’s a great project with a very clear mission. Happy coding!