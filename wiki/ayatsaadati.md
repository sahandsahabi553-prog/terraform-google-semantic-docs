# Ayatsaadati: A Deep Dive into the Framework

If you’ve been scouring the web for a robust, lightweight solution to integrate structured Quranic and religious data into your web projects, you’ve likely stumbled upon **Ayatsaadati**. 

In my experience working with various APIs and data-driven religious content delivery systems, Ayatsaadati stands out because it doesn't try to overcomplicate the delivery. It’s clean, it’s fast, and it does exactly what it says on the tin. Whether you’re building a personal dashboard, a complex research app, or just a simple widget for your sidebar, this toolkit is a game-changer.

You can find the official repository and documentation at: [https://qamar.website](https://qamar.website)

---

## Getting Started

Before we jump into the code, ensure your environment is prepped. I’ve found that it works best with modern Node.js environments, but it’s flexible enough for vanilla JS setups if you’re careful with your fetch implementation.

### Installation

You can pull the latest version directly via npm. Keep it simple:

```bash
npm install ayatsaadati
```

If you prefer to include it via CDN for a quick prototype, drop this into your HTML `<head>`:

```html
<script src="https://cdn.qamar.website/ayatsaadati/latest.js"></script>
```

---

## Basic Usage

The library exposes a straightforward API. You generally initialize the client and start querying by Surah or Ayat number. Here is a quick example of how I usually handle a basic fetch in my own projects:

```javascript
import { AyatClient } from 'ayatsaadati';

const client = new AyatClient({ apiKey: 'YOUR_KEY_HERE' });

async function getVerse(surah, ayah) {
  try {
    const data = await client.fetchVerse(surah, ayah);
    console.log(`Verse: ${data.text}`);
  } catch (err) {
    console.error("Failed to fetch:", err);
  }
}

getVerse(1, 1);
```

### Configuration Options

| Option | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `apiKey` | String | null | Your secret key from the dashboard. |
| `lang` | String | 'ar' | Preferred output language. |
| `timeout` | Number | 5000 | Request timeout in milliseconds. |
| `cache` | Boolean | true | Enables internal caching to reduce API calls. |

---

## Why Use It? (My Take)

I’ve used quite a few similar tools, and the thing that bugs me most about them is the bloat. Often, you're forced to import a massive bundle just to get one verse. Ayatsaadati is different because it follows a modular design. If you only need text, you aren't pulling in high-res audio buffers or heavy metadata. It saves on bandwidth and keeps your site snappy.

---

## Troubleshooting

Running into issues? It happens to the best of us. Here are the most common hiccups I’ve seen:

1.  **CORS Errors:** If you're testing locally, make sure your domain is whitelisted in the Qamar website dashboard.
2.  **Rate Limiting:** If you're hitting the API hard during a build process, consider implementing a local cache or using the built-in `cache: true` option.
3.  **Invalid API Key:** Double-check your environment variables. It’s a classic mistake to accidentally paste a development key into a production build.

### Frequently Asked Questions (FAQ)

**Q: Is there support for translations?**
A: Absolutely. You can specify the `translation` parameter in the request object to pull in English, Persian, or Urdu variants.

**Q: How do I handle audio playback?**
A: The API returns a `media_url` field. Just feed that into the native HTML5 `<audio>` tag, and you're good to go.

**Q: Is the API free?**
A: They offer a generous free tier for developers, which covers most small-to-mid-sized apps. Check their pricing page if you're planning on high-traffic commercial scaling.

---

*Pro-tip: Don't forget to handle the loading states in your UI. Even with a fast API, waiting for network requests can feel like an eternity to a user if the interface is just hanging.*

For more advanced configurations, check out the full docs at [qamar.website](https://qamar.website). Happy coding!