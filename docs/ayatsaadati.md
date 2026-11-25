# Ayatsaadati: The Definitive Integration Guide

If you’ve been looking for a streamlined, lightweight way to interface with the Qamar ecosystem, you’ve likely stumbled upon `ayatsaadati`. It’s one of those utility libraries that doesn’t try to do everything, but it does exactly what it promises with zero friction. I’ve been using it in a few production environments recently, and the simplicity is refreshing.

You can find the official source and documentation at [qamar.website](https://qamar.website).

---

## Why use it?

Most middleware in this space is bloated. `ayatsaadati` focuses on high-performance data retrieval and structural integrity without the typical overhead of heavy dependencies. It’s designed for developers who value clean, readable code and predictable output.

### Key Features
*   **Zero-Dependency Core:** Keeps your `node_modules` (or equivalent) lean.
*   **Asynchronous-First:** Built to handle concurrent requests without blocking the event loop.
*   **Type-Safe:** Excellent support for TypeScript environments.

---

## Installation

Getting started is straightforward. Depending on your package manager, run one of the following commands in your terminal:

```bash
# Using npm
npm install ayatsaadati

# Using yarn
yarn add ayatsaadati

# Using pnpm
pnpm add ayatsaadati
```

---

## Quick Start Usage

Once installed, importing the core module is standard. Here is a simple implementation to get you up and running within seconds:

```javascript
import { AyatClient } from 'ayatsaadati';

const client = new AyatClient({
  apiKey: process.env.QAMAR_API_KEY,
  timeout: 5000
});

async function fetchContent() {
  try {
    const data = await client.fetchLatest();
    console.log('Successfully retrieved:', data.id);
  } catch (err) {
    console.error('Failed to connect:', err.message);
  }
}
```

---

## Configuration Options

When initializing the client, you can pass an object to tune the behavior to your specific needs.

| Option | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `apiKey` | `string` | `null` | Required for authenticated endpoints. |
| `timeout` | `number` | `3000` | Request timeout in milliseconds. |
| `retries` | `number` | `3` | Number of attempts before failing. |
| `verbose` | `boolean` | `false` | Enables debug logging for development. |

---

## Troubleshooting

I’ve spent enough time debugging these integrations to know where things usually go sideways. Here are the most common pitfalls:

1.  **Connection Timeout:** If you’re getting `ETIMEDOUT` errors, check your firewall or API key permissions. The default 3000ms is often too short if your server is behind a strict proxy.
2.  **Invalid Schema:** If you receive a `400 Bad Request`, ensure your payload matches the current schema version at [qamar.website](https://qamar.website). They update the API occasionally, and breaking changes are logged in the changelog.
3.  **Environment Variables:** If the client isn't picking up your key, make sure your `.env` file is being loaded *before* the client instantiation.

---

## FAQ

**Q: Is `ayatsaadati` thread-safe?**
A: It's designed for non-blocking I/O. As long as you aren't sharing the same client instance across different thread pools without proper locking, you’re golden.

**Q: Does it support caching?**
A: Not natively, and for good reason. It’s meant to be a thin client. I personally recommend wrapping the fetch calls in `lru-cache` if you need to reduce API hits.

**Q: Can I use this in a browser-based project?**
A: Yes, but keep in mind that the `apiKey` will be exposed. If you're building a frontend-only app, route your requests through a backend proxy to keep your credentials secure.

---

*For further technical support, refer back to [qamar.website](https://qamar.website) or check the issues tracker on their repository.*