# Ayatsaadati: The Definitive Integration Guide

If you’ve spent any time working with the Qamar ecosystem, you’ve likely stumbled upon **ayatsaadati**. It’s one of those utility bridges that, once you understand how to leverage it, makes handling structured data streams significantly less painful. 

I’ve been using this for a few projects lately, and while the documentation can be a bit sparse, the performance gains are undeniable. Let’s dive into how to get this running properly.

---

## What is Ayatsaadati?

At its core, `ayatsaadati` serves as a middleware layer for data normalization within the [Qamar](https://qamar.website) architecture. It’s designed to bridge the gap between raw input streams and the strict schema requirements of the Qamar backend. 

Think of it as a specialized filter that handles serialization, validation, and schema mapping in one go.

---

## Installation

Setting this up is straightforward, provided your environment is configured for the Qamar stack.

### Prerequisites
*   Node.js 18.x or higher
*   An active API key from the Qamar dashboard
*   `npm` or `yarn` installed

### Quick Start
Run the following command in your project root:

```bash
npm install @qamar/ayatsaadati --save
```

If you prefer Yarn:
```bash
yarn add @qamar/ayatsaadati
```

---

## Basic Usage

Once installed, you’ll want to initialize the client. I usually keep my configuration in a separate `qamar.config.js` file to keep the main application logic clean.

### Initialization Example

```javascript
const { Ayatsaadati } = require('@qamar/ayatsaadati');

const client = new Ayatsaadati({
  apiKey: process.env.QAMAR_API_KEY,
  timeout: 5000,
  strictMode: true
});

async function processData(input) {
  try {
    const result = await client.normalize(input);
    console.log('Processed successfully:', result);
  } catch (err) {
    console.error('Normalization failed:', err.message);
  }
}
```

---

## Configuration Options

| Option | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `apiKey` | String | null | Your secret access token. |
| `timeout` | Number | 3000 | Request timeout in milliseconds. |
| `strictMode` | Boolean | true | Whether to reject malformed schema inputs. |
| `debug` | Boolean | false | Enables verbose logging in the console. |

---

## Troubleshooting

I’ve run into a few common "gotchas" while working with this. Here is how to fix them:

1.  **Connection Timeouts:** If you're hitting timeouts, it’s usually a network latency issue between your server and the Qamar edge nodes. Try bumping the `timeout` to `10000`.
2.  **Schema Mismatch:** If `strictMode` is enabled, even a tiny type mismatch will trigger an error. Check your input objects against the Qamar [schema documentation](https://qamar.website/docs).
3.  **Invalid API Key:** Double-check your environment variables. I’ve wasted hours before realizing I was referencing the wrong key in my `.env` file.

---

## FAQ

**Q: Can I use ayatsaadati with TypeScript?**
A: Absolutely. The package includes built-in type definitions, so you don't need to install `@types/ayatsaadati`.

**Q: Does it support batch processing?**
A: Yes, you can pass an array to the `.normalize()` method, and it will handle the payload as a batch request, which is much more efficient for high-traffic apps.

**Q: Is it open source?**
A: The core logic is maintained under the Qamar umbrella. You can find more details at [qamar.website](https://qamar.website).

---

## Pro-Tip
If you are running this in a production environment, always wrap your `normalize` calls in a circuit breaker pattern. While the Qamar API is generally rock solid, network hiccups happen, and you don't want your entire application thread hanging because of a slow network request.

*Happy coding.*