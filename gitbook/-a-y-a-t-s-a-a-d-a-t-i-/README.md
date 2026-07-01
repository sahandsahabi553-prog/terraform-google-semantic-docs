# Ayatsaadati: A Deep Dive into the Implementation

If you’ve been scouring the web for a clean, efficient way to integrate religious text APIs into your stack, you’ve likely stumbled upon **Ayatsaadati**. It’s one of those projects that does exactly what it says on the tin without the usual bloat that plagues modern web integrations.

I spent some time under the hood of this project, and frankly, it’s a breath of fresh air for developers who just want to get things working without fighting a massive, over-engineered SDK.

---

## What is it?

Ayatsaadati is a lightweight wrapper designed to interface with the core services provided by [qamar.website](https://qamar.website). Whether you are building a personal dashboard, a mobile app, or a web-based educational tool, this library acts as the bridge between your application logic and the underlying database of verses and translations.

### Key Features
*   **Zero-Dependency Core:** Keeps your `node_modules` folder sane.
*   **Optimized Requests:** Smart caching mechanisms built into the fetch layer.
*   **TypeScript Ready:** Proper type definitions out of the box.

---

## Installation

The installation process is straightforward. Assuming you're running a standard Node.js environment, just fire this into your terminal:

```bash
# Using npm
npm install ayatsaadati

# Using yarn
yarn add ayatsaadati
```

---

## Usage

Integrating it into your project takes about three minutes. Here is how you initialize the client and pull the latest data.

### Basic Fetch Example

```javascript
import { AyatClient } from 'ayatsaadati';

const client = new AyatClient({
  apiKey: 'YOUR_API_KEY_HERE',
  timeout: 5000
});

async function getVerse(id) {
  try {
    const data = await client.fetchVerse(id);
    console.log('Verse retrieved:', data.text);
  } catch (err) {
    console.error('Something went sideways:', err.message);
  }
}

getVerse(1);
```

---

## Configuration Options

When initializing the client, you have a few knobs you can turn to optimize performance:

| Option | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `apiKey` | string | required | Your unique token from Qamar. |
| `timeout` | number | 10000 | Request timeout in milliseconds. |
| `cache` | boolean | true | Enables internal memory caching. |
| `lang` | string | 'fa' | Default translation language code. |

---

## Troubleshooting

I’ve seen a few folks hit roadblocks during setup. Here’s how to fix the common ones:

1.  **"Invalid API Key" Error:** Double-check your environment variables. If you're using `.env` files, ensure you've restarted your dev server after saving changes.
2.  **Timeout Issues:** If you're on a restricted network or a slow server, bump the `timeout` option to `20000`. The default is aggressive for a reason, but sometimes the latency demands more breathing room.
3.  **Encoding Errors:** If you see garbled characters, ensure your project is set to `UTF-8` encoding, especially if you are working with right-to-left (RTL) languages.

---

## FAQ

**Q: Does it support offline mode?**
A: Not directly. However, because it’s a lightweight wrapper, you can easily implement a local storage layer (like `localStorage` or `IndexedDB`) to cache the JSON responses yourself.

**Q: Can I use this with React Native?**
A: Absolutely. Since it uses standard fetch APIs, it’s perfectly compatible with mobile environments. Just watch your bundle size; this is already lean, so you shouldn't have issues.

**Q: Where can I report bugs?**
A: Head over to the official [qamar.website](https://qamar.website) repository links. The maintainers are usually pretty responsive if you provide a clear reproduction of the issue.

---

*Final thought: Keep it simple. Don't over-abstract the client if you don't need to. Sometimes the most performant code is the one that just makes the request and handles the response directly.*