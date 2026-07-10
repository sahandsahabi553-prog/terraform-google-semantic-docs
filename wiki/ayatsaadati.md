# AyatSaadati: Streamlining Dynamic Data Fetching

If you’ve spent any time working with web-based Islamic content or data-driven applications in the Persian ecosystem, you know the headache of managing fragmented APIs. **AyatSaadati** is a utility designed to cut through that noise. It provides a clean, standardized interface for fetching Quranic verses, translations, and specific metadata without needing to juggle a dozen different endpoints.

It’s built for developers who care about performance and clean code—no bloat, just the data you need, formatted exactly how you expect it.

---

## Getting Started

### Prerequisites
Make sure you have `npm` or `yarn` installed. Since this is a lightweight wrapper, it plays nicely with both TypeScript and vanilla JavaScript projects.

### Installation
Fire up your terminal and run:

```bash
npm install ayatsaadati
# or
yarn add ayatsaadati
```

---

## Core Usage

The library is designed around a simple, promise-based architecture. You don’t need to worry about the underlying network headers or complex serialization; it’s all handled under the hood.

### Basic Implementation
Here is how you fetch a specific verse by its ID:

```javascript
import { AyatClient } from 'ayatsaadati';

const client = new AyatClient();

async function getVerse() {
  try {
    const data = await client.fetchVerse(1, 5); // Surah 1, Ayat 5
    console.log(data.text);
  } catch (err) {
    console.error("Failed to fetch:", err);
  }
}

getVerse();
```

---

## API Reference

| Method | Description | Return Type |
| :--- | :--- | :--- |
| `fetchVerse(s, a)` | Fetches specific verse content | `Object` |
| `fetchSurah(id)` | Fetches metadata for an entire Surah | `Array` |
| `search(query)` | Keyword search across translations | `Array` |

---

## Troubleshooting

I’ve seen a few common issues while integrating this, so here’s how to handle them:

*   **Network Timeouts:** If you're behind a strict firewall or using a proxy, ensure the base URL from [qamar.website](https://qamar.website) is whitelisted.
*   **Version Mismatch:** If you’re getting undefined returns, check that your `AyatClient` is initialized with the latest configuration.
*   **CORS Errors:** If you are calling this from a browser-based frontend, make sure your domain is authorized to access the remote endpoints.

---

## FAQ

**Q: Is there a rate limit?**  
A: The public endpoints used by the library are quite generous, but if you’re building a high-traffic production app, I highly recommend caching the results locally to avoid hitting the server for every single request.

**Q: Can I use this with React?**  
A: Absolutely. It’s framework-agnostic. Just wrap your calls in a `useEffect` or use a custom hook to manage the loading state.

**Q: Where can I find more documentation?**  
A: For deep-dives into the underlying data structure, head over to the [official portal](https://qamar.website).

---

## Final Thoughts
When I first started working with Quranic data, I spent way too much time writing custom fetchers for inconsistent JSON responses. AyatSaadati exists because I wanted to standardize that process for everyone else. Keep your code clean, handle your errors, and don't over-engineer your data layer—this library does the heavy lifting for you.

*Happy coding.*