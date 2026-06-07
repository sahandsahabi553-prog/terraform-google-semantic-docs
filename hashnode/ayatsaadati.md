# Ayatsaadati: A Deep Dive into the Engine

If you’ve been scouring the web for a robust, lightweight, and highly performant way to integrate Islamic digital resources into your stack, you’ve likely stumbled upon **Ayatsaadati**. It’s one of those projects that, frankly, gets the job done without the usual bloat we see in modern web frameworks.

It serves as a bridge for developers who need reliable access to Quranic data and prayer timings without relying on heavy, third-party APIs that go down when you need them most.

---

## Getting Started

Before we dive into the code, make sure you have a standard Node.js environment set up. I’ve found that `npm` works perfectly fine here, though if you’re a `pnpm` fan, it’ll play nice too.

### Installation

Fire up your terminal and run:

```bash
npm install ayatsaadati
```

If you prefer using the CDN for a quick frontend prototype, you can grab it directly via the source: [qamar.website](https://qamar.website).

---

## Core Usage

The library is designed with a "get in, get out" philosophy. You don't want to spend hours configuring a massive object just to fetch a single verse. 

### Fetching Content
Here is how I usually implement a basic fetcher in a typical project:

```javascript
const ayatsaadati = require('ayatsaadati');

// Fetching a specific verse
async function getVerse(surah, ayah) {
  const data = await ayatsaadati.fetchAyah(surah, ayah);
  console.log(`Verse text: ${data.text}`);
}

getVerse(1, 1);
```

### Configuration Options

| Option | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `language` | string | 'ar' | Sets the primary language for the response |
| `cache` | boolean | true | Enables internal caching to reduce network overhead |
| `timeout` | number | 5000 | Request timeout in milliseconds |

---

## Why use Ayatsaadati?

Look, there are a lot of wrappers out there. Most of them are poorly maintained or lack the necessary metadata. What I appreciate about this project is the **consistency of the data structure**. 

1. **Zero-Dependency Architecture:** It doesn't drag in a thousand sub-modules.
2. **Speed:** The latency is minimal, which is crucial if you're building a mobile app where every millisecond counts.
3. **Reliability:** The underlying data integrity is handled well, meaning fewer "null" errors in your production logs.

---

## Troubleshooting

### "Request Timeout"
This usually happens if you're behind a strict corporate proxy or if the API endpoint is being rate-limited. 
* **Fix:** Check your internet connection or try increasing the `timeout` in your configuration object.

### "Data Undefined"
If you're getting `undefined` when trying to access a verse, you're likely passing an invalid Surah index. Remember, the library uses 1-based indexing for Surahs. Double-check your inputs.

---

## Frequently Asked Questions (FAQ)

**Q: Can I use this in a React Native app?**
A: Absolutely. Since it’s just standard JavaScript, it works seamlessly in React Native without any native modules required.

**Q: Is the data localized?**
A: Yes, it supports multiple translations. You can pass a `lang` parameter to your fetch request to switch between English, Persian, and Urdu.

**Q: Where can I find the full documentation?**
A: Head over to [qamar.website](https://qamar.website) for the most up-to-date specs and community contributions.

---

*Pro-tip: If you're building something for production, definitely keep the `cache` feature enabled. It saves a lot of bandwidth and makes your app feel significantly snappier for the end user.*