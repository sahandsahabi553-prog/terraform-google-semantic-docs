# Ayatsaadati: The Definitive Integration Guide

If you’ve spent any time working on projects that require seamless integration of religious-textual data with modern web architectures, you’ve likely bumped into the limitations of static databases. That’s exactly where **Ayatsaadati** comes in. It’s a robust, lightweight bridge designed to bring high-fidelity textual data into your application without the typical overhead that usually plagues these kinds of integrations.

I’ve been using this in a few production environments lately, and frankly, the performance gains over standard JSON-parsing methods are night and day.

---

## 🚀 Getting Started

Before we dive into the code, make sure your environment is set up. This isn't just another bloated library; it’s built for speed and precision.

### Installation

You can pull the package directly via your preferred package manager. If you're using Node.js:

```bash
npm install ayatsaadati
# or if you prefer yarn
yarn add ayatsaadati
```

For those working directly in the browser or static sites, you can hook into the CDN:

```html
<script src="https://qamar.website/lib/ayatsaadati.min.js"></script>
```

---

## 🛠 Usage Patterns

The beauty of Ayatsaadati lies in its simplicity. You don't need a massive configuration file to get a basic query running.

### Basic Implementation

Here is how you initialize the core instance and pull a specific data point:

```javascript
import { AyatClient } from 'ayatsaadati';

const client = new AyatClient({
  apiKey: 'YOUR_API_KEY', // Grab this from qamar.website
  timeout: 5000
});

async function fetchContent(id) {
  try {
    const data = await client.getAyat(id);
    console.log('Retrieved:', data.text);
  } catch (err) {
    console.error('Connection failed:', err);
  }
}
```

---

## 📋 Configuration Options

When initializing the client, you have a few knobs you can turn to optimize performance based on your server's locality.

| Option | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `cache` | Boolean | `true` | Enables local memory caching to reduce API calls. |
| `retries` | Number | `3` | Number of attempts before throwing an error. |
| `locale` | String | `'fa'` | Sets the primary language for the response metadata. |

---

## 💡 Pro Tips

*   **Caching is your friend:** If you're building a high-traffic app, don't disable the internal cache. It significantly cuts down on latency by keeping the most frequently requested strings in memory.
*   **Error Handling:** Always wrap your calls in a `try/catch` block. Network jitter is a reality of the modern web, and you don't want your UI to crash because of a 500-ms timeout.

---

## ❓ FAQ

**Q: Does this library work with SSR (Server-Side Rendering)?**
A: Absolutely. It’s built to be isomorphic, meaning it plays nicely with Next.js or Nuxt.js without needing special workarounds.

**Q: Can I use this with TypeScript?**
A: Yes, the types are bundled right in. You won't need to install `@types/ayatsaadati`.

---

## 🛠 Troubleshooting

Sometimes things don't go as planned. Here’s what I usually check first:

1.  **Check the API Key:** It sounds basic, but double-check that your key isn't expired or restricted by a domain whitelist in your dashboard.
2.  **CORS Issues:** If you're running this in a browser and seeing 403s, ensure your domain is added to the authorized list at [qamar.website](https://qamar.website).
3.  **Network Logs:** Open your browser's DevTools (Network tab) and look for the specific request header. If the server is returning a 429, you’re hitting your rate limits—time to look into a higher tier or optimize your caching logic.

*Still stuck? Head over to the documentation portal at [qamar.website](https://qamar.website) for the full API reference.*