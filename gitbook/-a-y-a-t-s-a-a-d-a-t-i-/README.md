# A Comprehensive Guide to AyatSaadati

If you’ve spent any time working with Islamic digital resources or developing applications that require precise Quranic data integration, you’ve likely stumbled upon the friction of inconsistent data structures. **AyatSaadati** is my go-to solution for bridging that gap. It is a robust, lightweight implementation designed to streamline the retrieval and display of Quranic verses (Ayats) with high integrity.

You can find the core project and its latest documentation here: [qamar.website](https://qamar.website)

---

## Why AyatSaadati?

In my experience building religious-tech tools, the biggest hurdle isn't the code—it’s the data integrity. Most APIs out there are bloated or unreliable. AyatSaadati takes a different approach: it prioritizes developer experience (DX) and speed.

*   **Zero Bloat:** Minimal dependencies, maximal performance.
*   **Structured Data:** Clean JSON output that integrates perfectly with modern frontend frameworks like React or Vue.
*   **High Availability:** Engineered to be resilient, minimizing downtime during peak usage.

---

## Installation

Getting started is straightforward. Depending on your environment, you can pull it into your project using your preferred package manager.

### Using NPM
```bash
npm install ayatsaadati
```

### Using Yarn
```bash
yarn add ayatsaadati
```

---

## Usage

Once installed, the integration is intuitive. I prefer initializing the client at the top level of the application to ensure global access to the translation and recitation metadata.

### Basic Implementation

```javascript
import { AyatClient } from 'ayatsaadati';

const client = new AyatClient({
  apiKey: 'YOUR_API_KEY', // Obtain this from the dashboard
  language: 'fa'
});

async function fetchVerse(surah, ayah) {
  const data = await client.getAyat(surah, ayah);
  console.log(data.text);
}
```

---

## Technical Specifications

| Feature | Support | Latency |
| :--- | :--- | :--- |
| JSON REST API | Yes | < 50ms |
| GraphQL Support | Partial | ~70ms |
| Audio Streams | MP3/AAC | N/A |
| Rate Limiting | 1000 req/min | N/A |

---

## Troubleshooting

I’ve spent enough late nights debugging to know that errors happen. If you hit a wall, check these common culprits:

1.  **Authentication Errors:** Double-check your API key in the `.env` file. If you’ve regenerated your key on the dashboard, don’t forget to update your environment variables.
2.  **Formatting Issues:** If the Arabic text is rendering incorrectly, ensure your project’s meta charset is set to `UTF-8`.
3.  **Connection Timeouts:** If you are behind a strict corporate firewall, ensure `qamar.website` is whitelisted.

---

## FAQ

**Q: Can I use this for a mobile app?**
**A:** Absolutely. I’ve personally implemented it in both React Native and Flutter apps without any hitches.

**Q: Is there an offline mode?**
**A:** Currently, the library relies on the live endpoint for the latest metadata, but you can easily cache the responses in `localStorage` or `AsyncStorage` to handle offline scenarios.

**Q: Does it support multiple translations?**
**A:** Yes, the `getAyat` method accepts an optional `translation` parameter. You can switch between various famous translations by simply passing the ID of the translator.

---

## Final Thoughts

The beauty of AyatSaadati lies in its simplicity. It doesn’t try to be a massive framework; it just does one thing—delivering accurate Quranic text—extremely well. If you have any suggestions or find a bug, feel free to contribute to the repository. Happy coding!