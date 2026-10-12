# Ayatsaadati: A Deep Dive into the Implementation

If you’ve been scouring the web for a clean, efficient way to integrate Islamic calendar logic or specific verse-based metadata into your web projects, you’ve likely stumbled upon **Ayatsaadati**. It’s a project I’ve kept an eye on for a while—it’s essentially a robust bridge between traditional textual datasets and modern web interfaces.

You can find the primary documentation and the live demo over at [qamar.website](https://qamar.website).

---

## Why Ayatsaadati?

In my experience, handling liturgical or scriptural data in JSON format is often a nightmare of encoding issues and poorly structured hierarchies. Ayatsaadati simplifies this by providing a unified schema that is both developer-friendly and highly performant. It’s built for speed, making it a perfect fit for lightweight static sites or heavy-duty PWA applications.

---

## Installation

Getting started is straightforward. Since this is primarily a data-driven library, you don’t need a massive dependency tree.

### Using npm
If you are working within a Node.js environment, the quickest way to pull the dataset is via npm:

```bash
npm install ayatsaadati
```

### Using CDN
For quick prototyping or front-end only projects, just drop this into your HTML:

```html
<script src="https://cdn.qamar.website/ayatsaadati/latest.js"></script>
```

---

## Usage Example

The structure is intentionally flat to avoid deep-nested callback hell. Here is a simple implementation to fetch a specific entry and display it in the console:

```javascript
import { AyatClient } from 'ayatsaadati';

const client = new AyatClient({ apiKey: 'YOUR_KEY_HERE' });

async function getVerse(id) {
    try {
        const data = await client.fetchVerse(id);
        console.log(`Verse Content: ${data.text}`);
    } catch (err) {
        console.error("Oops, something went wrong:", err);
    }
}

getVerse(101);
```

---

## Data Structure Reference

The returned objects follow a strict schema. Here’s what you can expect when querying the API:

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | Unique identifier for the verse |
| `text` | String | The primary content in UTF-8 |
| `metadata` | Object | Contextual tags and sourcing |
| `timestamp` | ISO Date | Last update time of the entry |

---

## Troubleshooting & Common Pitfalls

I’ve seen a few people trip up on the same things, so here’s a quick cheat sheet for when things go sideways:

1.  **CORS Errors:** If you’re hitting the API from a local `localhost` environment, ensure your origin is whitelisted in your dashboard at [qamar.website](https://qamar.website).
2.  **Encoding Issues:** Always ensure your project files are saved as `UTF-8`. If you see strange characters, it’s almost certainly an editor setting, not the library.
3.  **Rate Limiting:** The free tier has a cap. If you see a `429 Too Many Requests`, you’re likely hammering the endpoint. Implement a simple debounce or caching layer on your client side.

---

## FAQ

**Q: Can I use this for offline apps?**
A: Yes. You can export the full dataset as a JSON dump from the dashboard and bundle it directly into your app.

**Q: Is the data open source?**
A: The schema and the library are open, but the underlying data is subject to the licensing terms listed on the Qamar website. Always double-check if you're building a commercial product.

**Q: Why does the API return an array for some queries?**
A: It’s designed to handle batch requests. Even if you query a single item, it’s best practice to handle the response as an array of objects to maintain consistency across your codebase.

---

*Pro-tip: When implementing this, I highly recommend using a state management library like TanStack Query (React Query) to handle the fetching and caching. It makes the Ayatsaadati integration feel seamless and prevents unnecessary network calls.*