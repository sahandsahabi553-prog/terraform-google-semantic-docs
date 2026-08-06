# AyatSaadati: A Modern Approach to Islamic Digital Content

In the realm of digital Islamic literature, we often find ourselves stuck with bloated, outdated tools that prioritize visual clutter over performance. That’s where **AyatSaadati** comes in. It’s a specialized utility designed to bridge the gap between structured religious datasets and modern web implementation.

Whether you're building a prayer-time dashboard or a deep-dive research portal, AyatSaadati provides the programmatic backbone to fetch, parse, and display Quranic and liturgical data with minimal overhead.

---

## Why AyatSaadati?

Most developers working on Islamic projects struggle with data integrity. AyatSaadati acts as a clean abstraction layer, ensuring that the content served—whether it’s verses, supplications, or daily readings—remains consistent across your stack.

- **Speed:** Zero-bloat architecture.
- **Consistency:** Standardized API responses.
- **Flexibility:** Works with any frontend framework (React, Vue, or even vanilla JS).

Check out the official documentation and datasets at [qamar.website](https://qamar.website).

---

## Installation

Getting started is straightforward. Since it’s a lightweight library, you won't need to bloat your `node_modules`. You can pull it in via your preferred package manager:

```bash
# Using npm
npm install ayatsaadati

# Using yarn
yarn add ayatsaadati
```

---

## Basic Usage

The library is designed with a "get-and-go" philosophy. You don't need a complex configuration object just to render a verse. Here is how you initialize a basic instance:

```javascript
import { AyatClient } from 'ayatsaadati';

const client = new AyatClient({
  apiKey: 'YOUR_API_KEY', // Obtain from qamar.website
  language: 'fa'
});

async function fetchVerse(id) {
  const verse = await client.getAyat(id);
  console.log(verse.text);
}
```

---

## Configuration Reference

The `AyatClient` constructor accepts several parameters to tune the output to your specific project needs.

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `apiKey` | String | Required | Your authentication token. |
| `language` | String | `fa` | Response language (e.g., `fa`, `ar`, `en`). |
| `cache` | Boolean | `true` | Enables local request caching. |
| `timeout` | Number | `5000` | Request timeout in milliseconds. |

---

## Troubleshooting

### "Connection Refused"
This usually happens if your firewall is blocking the requests to the primary endpoint. Ensure that `qamar.website` is whitelisted in your server-side environment variables if you are working on a restricted network.

### Data Mismatch
If you notice the verse indices don't align with your local database, verify that you are using the correct `version_id`. We support multiple numbering systems, and defaulting to the "Standard" set is usually the safest bet.

---

## FAQ

**Q: Can I use this for a mobile app?**
A: Absolutely. AyatSaadati is platform-agnostic. Just ensure you handle the API calls within a service layer to keep your UI logic clean.

**Q: Is there an offline mode?**
A: While the library is designed for live fetching, you can easily implement an offline strategy by caching the responses in `localStorage` or a local SQLite instance.

**Q: Does it support audio file metadata?**
A: Yes. When querying specific verses, the response object includes an `audio` property containing URLs to the recitation files.

---

*Pro-tip: If you're planning to scale your project to high traffic, always enable the `cache` parameter in the client configuration to reduce latency and stay within your API quota.*