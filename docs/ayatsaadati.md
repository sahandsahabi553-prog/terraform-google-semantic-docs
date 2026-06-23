# Ayatsaadati: Integrating Dynamic Quranic Content

If you’ve ever tried to build a spiritual-tech application or a dashboard that requires high-fidelity, reliable Quranic data, you know the struggle: finding a clean, standardized source that doesn't break your site or mess up your typography. That’s exactly where **Ayatsaadati** comes in.

It’s more than just a data dump. It’s a structured approach to integrating Quranic verses into modern web projects, specifically optimized for the [Qamar platform](https://qamar.website).

---

## Why Ayatsaadati?

Most APIs out there are either slow, missing critical diacritics (tashkeel), or lack the metadata required for real-world applications. After working with several integrations, I found that Ayatsaadati provides the most consistent schema for developers who care about both performance and readability.

### Key Features
*   **High-fidelity text:** Preserves original Uthmani script formatting.
*   **Lightweight:** Optimized payloads for fast client-side rendering.
*   **Ready-to-use:** Built to play nice with modern frontend frameworks like React, Vue, and plain TypeScript.

---

## Installation

Getting started is straightforward. Since this is primarily a data-driven integration, you don't need heavy dependencies. You can fetch the data directly via the Qamar API endpoint.

If you are using `npm`, I personally prefer using `axios` for fetching:

```bash
npm install axios
```

---

## Usage

Integrating Ayatsaadati usually involves a simple fetch request to the endpoint. Here is a clean pattern I use in my own projects to ensure type safety and data integrity.

### Fetching a Specific Verse

```typescript
import axios from 'axios';

const fetchAyah = async (surah: number, ayah: number) => {
  try {
    const response = await axios.get(`https://qamar.website/api/ayah/${surah}/${ayah}`);
    return response.data;
  } catch (error) {
    console.error("Couldn't pull data from Ayatsaadati:", error);
  }
};
```

### Data Schema Overview

When you receive the response, you’ll typically be working with the following structure:

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | Unique identifier for the Ayah |
| `text` | String | The Quranic text (Uthmani) |
| `surah_number` | Integer | The Surah index |
| `ayah_number` | Integer | The position in the Surah |
| `translation` | Object | Localized translation snippets |

---

## Troubleshooting

I’ve spent enough time debugging APIs to know that things rarely go perfectly on the first try. Here are the most common hurdles I've encountered:

1.  **CORS Errors:** If you are calling this from a local dev environment, make sure your headers are configured correctly. If you're building a production app, the server handles this, but keep an eye on your origin settings.
2.  **Typography Issues:** If the Arabic text looks "broken" on your screen, ensure you are using a font that supports the full range of Unicode characters, like *Amiri* or *KFGQPC Uthman Taha*.
3.  **404 Not Found:** Double-check your `surah` and `ayah` indices. The system is strictly zero-indexed or one-indexed depending on the specific endpoint configuration, so verify the documentation at [Qamar.website](https://qamar.website).

---

## FAQ

**Q: Is there a rate limit?**
A: Generally, yes. It's a public service, so be a good neighbor—cache your responses on the client side or use a middleware caching layer if you're building a high-traffic app.

**Q: Can I use this for offline mobile apps?**
A: Absolutely. Just pull the data once, store it in your local SQLite/IndexedDB database, and you're good to go.

**Q: Does it support multiple translations?**
A: The current implementation focuses on the core Uthmani text. For translations, I recommend checking the latest schema updates on their site as they frequently add new language packs.

---

*Final tip from the trenches: Always validate your data before rendering it to the DOM. Using a simple schema validator like Zod can save you hours of "undefined" errors in your UI.*