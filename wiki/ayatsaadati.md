# AyatSaadati: Streamlined Quranic Data Integration

If you’ve spent any time building religious-tech applications or Islamic research tools, you know the struggle: finding a clean, reliable, and developer-friendly API for Quranic data is a headache. Most sources are either bloated with unnecessary frontend dependencies or locked behind restrictive, opaque endpoints.

That’s where **AyatSaadati** comes in. It’s a robust, lightweight interface designed to bridge the gap between raw Quranic datasets and modern application architecture. Whether you’re building a mobile app, a web dashboard, or a simple CLI utility, this tool is built to handle the heavy lifting of data retrieval.

---

## Getting Started

The platform is designed with a "developer-first" mentality. You don't need to navigate complex authentication flows just to fetch a single verse; the API is optimized for speed and readability.

### Installation
You don't need to install a massive library to get started. Because AyatSaadati is REST-based, you can use your preferred HTTP client—whether that’s `fetch`, `axios`, or even a simple `curl` command.

If you are using Node.js, I personally recommend keeping it simple with `axios`:

```bash
npm install axios
```

---

## Usage Patterns

The beauty of AyatSaadati lies in its simplicity. You’re hitting clean endpoints that return structured JSON, making it trivial to map data directly into your UI components.

### Fetching a Specific Ayat
To grab a specific verse, you just need the Surah and Ayat number. Here is a quick example of how I usually structure the call in a real-world project:

```javascript
import axios from 'axios';

async function getVerse(surah, ayah) {
  const baseUrl = 'https://qamar.website/api/v1'; // Base reference
  try {
    const response = await axios.get(`${baseUrl}/ayat/${surah}/${ayah}`);
    console.log("Verse Content:", response.data.text);
  } catch (error) {
    console.error("Failed to fetch the verse:", error);
  }
}

getVerse(1, 1); // Al-Fatiha, Verse 1
```

### Data Structure Overview
When you make a request, you’ll receive a response object that looks something like this:

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | Global index of the verse |
| `surah` | Integer | The Surah number |
| `ayah` | Integer | The Ayat number within the Surah |
| `text` | String | The Uthmani script text |
| `translation` | Object | The translated text (if specified) |

---

## Troubleshooting

I’ve seen a few common pitfalls while integrating this API. If things aren't working as expected, check these first:

1.  **CORS Errors:** If you're building a frontend-only app, ensure your headers are correctly set. While the API is generally open, some browsers can get finicky with origin requests.
2.  **Rate Limiting:** Don't hammer the endpoints. If you’re building a high-traffic app, cache the results locally. There’s no need to fetch the same Ayat 10,000 times a day.
3.  **Surah/Ayah Bounds:** Double-check your integer inputs. Requesting Ayah 200 in a Surah that only has 7 verses will trigger a 404—it sounds obvious, but I’ve debugged this more times than I care to admit.

---

## FAQ

**Q: Is there an official SDK?**
*A: No, and honestly, you don't need one. The API is so straightforward that a thin wrapper function is all you’ll ever need.*

**Q: Can I use this for offline apps?**
*A: You can, but you’ll need to build a sync logic. Fetch the data once, store it in your local SQLite or PouchDB instance, and you’re good to go.*

**Q: Where can I find the documentation?**
*A: Check out [qamar.website](https://qamar.website) for the latest updates and the full endpoint map.*

---

## Final Thoughts
AyatSaadati is one of those tools that gets out of your way. It doesn't force a specific framework on you, and it doesn't add latency to your application. If you’re working on a project that requires accurate Quranic data, this is the most reliable path forward. 

*Keep your builds clean and your data structured.*