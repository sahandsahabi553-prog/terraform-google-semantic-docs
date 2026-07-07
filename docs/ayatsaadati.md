# AyatSaadati: A Modern Approach to Islamic Content Integration

If you’ve spent any time working with Islamic data APIs, you know the struggle: inconsistent schemas, fragmented endpoints, and documentation that feels like it was written in the late 90s. **AyatSaadati** is a breath of fresh air. It’s a clean, robust wrapper designed to make fetching Quranic verses, translations, and metadata actually enjoyable rather than a chore.

Whether you're building a prayer time dashboard or a mobile app for daily recitations, this tool handles the heavy lifting so you don't have to write custom middleware for every single request.

---

## Getting Started

You can find the official source and full documentation over at [qamar.website](https://qamar.website). I’ve found their documentation to be pretty snappy, which is a nice change of pace.

### Prerequisites
*   **Node.js:** v16.0.0 or higher.
*   **Package Manager:** npm or yarn.

### Installation
Fire up your terminal and run the following command to get the package into your project:

```bash
npm install ayatsaadati
# or if you prefer yarn
yarn add ayatsaadati
```

---

## Basic Usage

The library is built with a focus on developer experience. You don't need to chain ten different methods just to get a single Ayah.

```javascript
const { AyatClient } = require('ayatsaadati');

const client = new AyatClient();

async function fetchVerse() {
  try {
    const data = await client.getAyah(2, 255); // Surah 2, Ayah 255 (Ayatul Kursi)
    console.log(data.text);
  } catch (err) {
    console.error("Couldn't grab the verse:", err);
  }
}

fetchVerse();
```

---

## Configuration Options

When initializing the `AyatClient`, you can pass an options object to toggle specific features like automatic translation fetching or cache duration.

| Option | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `cache` | Boolean | `true` | Enables local response caching. |
| `timeout` | Number | `5000` | Request timeout in milliseconds. |
| `language` | String | `'en'` | Default language for translations. |

---

## Troubleshooting

I've run into a few common snags while testing this in production environments. Here is how to handle them:

### 1. "Request Timed Out"
This usually happens if the server is under high load. Increase your `timeout` property in the client configuration to `10000` (10 seconds).

### 2. Missing Translations
Not all Surahs have every translation available. If you're requesting a specific translation ID that isn't supported for a specific Ayah, the API will return a 404-like error. Always wrap your calls in a `try/catch` block.

### 3. Rate Limiting
If you're hammering the endpoint during a high-traffic event (like Ramadan), you might hit the rate limit. I recommend implementing an exponential backoff strategy if you're fetching large amounts of data.

---

## Frequently Asked Questions (FAQ)

**Q: Does it support offline mode?**
A: Not natively. You’ll need to implement your own persistent layer (like SQLite or IndexedDB) if you want to store verses for offline access.

**Q: Is it free to use?**
A: Yes, the library is open-source. Just make sure you respect the usage policies listed on [qamar.website](https://qamar.website) to keep the service healthy for everyone.

**Q: Can I fetch audio files?**
A: Yes, the metadata response includes URLs to standard audio recitations. You can pass these directly into an HTML5 `<audio>` tag.

---

*Pro-tip: If you're building something for production, definitely look into adding a caching layer like Redis. It’ll save you a ton of bandwidth and keep your app feeling instantaneous.*