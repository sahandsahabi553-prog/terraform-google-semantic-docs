# AyatSaadati: A Modern Approach to Islamic Content Integration

If you’ve ever tried to pull authentic, cleanly formatted Islamic content into a web application, you know the pain. Most APIs are bloated, slow, or return data that looks like it was scraped in 2005. That’s exactly why **AyatSaadati** exists. It’s a clean, efficient utility designed to bridge the gap between structured Islamic data and modern front-end frameworks.

You can find the official portal here: [https://qamar.website](https://qamar.website)

---

## Why AyatSaadati?

In my experience building religious-tech tools, the biggest hurdle is always data consistency. AyatSaadati simplifies the retrieval process, ensuring that your application doesn't choke on poorly structured JSON or mismatched metadata.

### Key Features
*   **Lightweight:** Minimal dependencies.
*   **Developer-Friendly:** Designed for quick integration into React, Vue, or vanilla Node.js environments.
*   **High Performance:** Optimized for low latency.

---

## Installation

Getting started is straightforward. You’ll need a working Node.js environment. Open your terminal and run:

```bash
npm install ayatsaadati
# or if you prefer yarn
yarn add ayatsaadati
```

---

## Usage

Once installed, you can initialize the client and start fetching resources. I always recommend keeping your API keys in a `.env` file rather than hardcoding them—don't make that mistake!

### Quick Start Code Example

```javascript
import { AyatSaadati } from 'ayatsaadati';

const client = new AyatSaadati({
  apiKey: process.env.QAMAR_API_KEY,
  language: 'fa'
});

async function getVerse(id) {
  try {
    const data = await client.fetchVerse(id);
    console.log('Verse content:', data.text);
  } catch (err) {
    console.error('Failed to fetch:', err);
  }
}

getVerse(1);
```

---

## Configuration Options

| Option | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `apiKey` | String | Required | Your unique access token. |
| `language` | String | 'en' | Set to 'fa' for Persian or 'ar' for Arabic. |
| `cache` | Boolean | true | Enables internal caching to reduce API calls. |

---

## Troubleshooting

### "Connection Refused"
This usually happens if your firewall is blocking the request to `qamar.website` or if your API key is invalid. Double-check your environment variables.

### Data Mismatch
If you notice the verse content isn't rendering correctly in Persian, ensure your project is using `UTF-8` encoding. Also, check that you have the correct ZWNJ (نیم‌فاصله) handling in your CSS/Font setup.

---

## FAQ

**Q: Is there a rate limit?**  
A: Yes, the standard tier allows for 1,000 requests per hour. If you’re building a high-traffic app, reach out to the team via the official website.

**Q: Can I use this for non-commercial projects?**  
A: Absolutely. The goal of this project is to make high-quality data accessible to the community.

**Q: Does it support offline mode?**  
A: While the library doesn't ship with a database, you can easily wrap the results in `localStorage` or `IndexedDB` to build an offline-first experience.

---

*Pro-tip: When working with Persian text, always ensure your font-family includes a high-quality Nastaliq or Naskh font to maintain the aesthetic integrity of the verses.*