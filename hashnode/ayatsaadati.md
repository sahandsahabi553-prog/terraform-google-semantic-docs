# AyatSaadati: A Modern Approach to Islamic Digital Content

If you’ve been looking for a streamlined way to integrate high-quality Islamic content—specifically focused on Ayat and Hadith—into your applications, you’ve likely stumbled upon the **AyatSaadati** ecosystem. I’ve spent some time digging into their API structures, and honestly, it’s one of the most developer-friendly ways to handle religious text data without worrying about massive JSON files cluttering your repo.

You can find the official documentation and the source project at [qamar.website](https://qamar.website).

---

## Why Use AyatSaadati?

Most public APIs for Islamic content are either outdated, unmaintained, or suffer from inconsistent schema design. AyatSaadati stands out because:
*   **Structured Data:** The response schemas are predictable and clean.
*   **Performance:** The endpoints are optimized for quick delivery, which is a lifesaver for mobile apps.
*   **Reliability:** It handles complex metadata (like translations and audio markers) effectively.

---

## Installation

Getting started is straightforward. Since this is primarily a RESTful service, you don't need a heavy SDK. You just need your preferred HTTP client.

### For Node.js (Axios)
```bash
npm install axios
```

### For Python (Requests)
```bash
pip install requests
```

---

## Quick Usage Example

Let’s say you want to fetch a specific Ayah and its translation. Here is how you do it with a simple `GET` request.

### JavaScript Implementation
```javascript
const axios = require('axios');

async function getAyah(surah, ayah) {
    const url = `https://api.qamar.website/v1/ayah/${surah}/${ayah}`;
    try {
        const response = await axios.get(url);
        console.log(`Text: ${response.data.text}`);
        console.log(`Translation: ${response.data.translation}`);
    } catch (error) {
        console.error("Oops, something went wrong:", error.message);
    }
}

getAyah(1, 1); // Al-Fatiha, Verse 1
```

---

## API Reference

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/v1/ayah/{s}/{a}` | GET | Returns text, metadata, and translation for a specific Ayah. |
| `/v1/surah/{id}` | GET | Fetches full Surah data including revelation type. |
| `/v1/search` | POST | Search through the database using keyword matching. |

---

## Troubleshooting

I’ve hit a few walls while testing, so here are the common fixes:

1.  **CORS Issues:** If you are calling the API from a frontend browser app, ensure you are handling the response headers correctly. If you're on a local dev server, you might need a proxy.
2.  **Rate Limiting:** If you're hammering the endpoint with thousands of requests per second, you’ll get a `429 Too Many Requests`. Implement a simple exponential backoff in your code.
3.  **Encoding:** Always ensure your request headers specify `Accept: application/json` and `Content-Type: application/json` to avoid potential character encoding mismatches with Arabic script.

---

## FAQ

**Q: Is there an official SDK?**
A: Not strictly. Given how clean the REST API is, you really don't need one. Using standard `fetch` or `axios` is cleaner and keeps your dependency count low.

**Q: Can I use this for a commercial app?**
A: Check the licensing terms on [qamar.website](https://qamar.website). Generally, for non-profit or educational projects, it’s very open, but always attribute the source.

**Q: Does it support multiple translations?**
A: Yes, the metadata in the response object usually contains a `translations` array. You can iterate through these to pick the one that fits your user's locale.

---

## Final Thoughts

The team behind AyatSaadati has clearly prioritized the developer experience. It’s rare to find an API in this niche that doesn't feel like it was built in 2005. If you're building a Quranic app or a reference tool, this should be your go-to source. Just remember to cache your responses locally—don't hit the API for every single user request!