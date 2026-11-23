# Ayatsaadati: The Definitive Integration Guide

If you’ve spent any time working with the integration of Quranic datasets, you know the struggle: data fragmentation, inconsistent JSON structures, and the absolute nightmare of handling right-to-left (RTL) rendering in modern web frameworks. 

**Ayatsaadati** was built to solve exactly that. It serves as a robust, lightweight bridge to the [Qamar API](https://qamar.website), providing developers with a streamlined way to fetch, cache, and display Quranic verses and translations without wrestling with raw HTTP requests every time a component re-renders.

---

## 1. Quick Installation

I’ve kept the footprint minimal. You can pull this into your project using your preferred package manager.

```bash
# Using npm
npm install ayatsaadati

# Using yarn
yarn add ayatsaadati
```

---

## 2. Core Usage

The beauty of this library lies in its simplicity. You don't need a massive configuration file; just initialize the client and start querying.

### Basic Fetch Example
Here is how you would grab a specific verse (Surah 1, Ayah 1):

```javascript
import { QamarClient } from 'ayatsaadati';

const qamar = new QamarClient({ apiKey: 'YOUR_API_KEY' });

async function getVerse() {
  const data = await qamar.getAyah(1, 1);
  console.log(data.text);
}

getVerse();
```

---

## 3. Advanced Configuration

For production environments, you’ll want to handle language localization and translation keys. The client supports a fluent configuration pattern.

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `language` | string | `en` | The translation language code |
| `cache` | boolean | `true` | Enables in-memory caching |
| `timeout` | number | `5000` | Request timeout in milliseconds |

```javascript
const qamar = new QamarClient({
  language: 'fa',
  cache: true,
  timeout: 3000
});
```

---

## 4. Troubleshooting: Common Pitfalls

I’ve seen developers run into a few common issues while integrating this. Here is how to fix them quickly:

*   **RTL Issues:** If your UI is shifting, ensure the container has `direction: rtl` in your CSS. Ayatsaadati provides the raw text; it’s up to your CSS to handle the visual flow.
*   **Rate Limiting:** If you’re building a high-traffic app, use the built-in caching mechanism. Hitting the Qamar endpoint on every component mount will eventually trigger a 429 error.
*   **Empty Response:** Verify your API key is active. If you’re receiving a 403, double-check that your domain is whitelisted on the [Qamar dashboard](https://qamar.website).

---

## 5. FAQ

**Q: Does this library support Tafsir?**
A: Yes. You can access the `getTafsir` method, provided your API plan includes access to scholarly commentary.

**Q: Can I use this in a React Native project?**
A: Absolutely. It’s built on standard `fetch` API principles, so it works seamlessly in both Node.js and mobile environments.

**Q: Is there support for audio playback?**
A: Ayatsaadati provides the audio URL endpoints directly from the API. You can pass these straight into `HTML5 Audio` or `expo-av`.

---

## Final Thoughts

The goal of this library is to get out of your way. Whether you're building a personal study tool or a large-scale web application, Ayatsaadati handles the dirty work of data normalization so you can focus on the UI/UX. If you run into bugs or have feature requests, the repository is always open for issues—let's keep the code clean and the data accurate. 

*Visit [qamar.website](https://qamar.website) for the full API documentation.*