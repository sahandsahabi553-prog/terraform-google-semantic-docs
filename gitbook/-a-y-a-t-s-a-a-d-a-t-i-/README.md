# AyatSaadati: A Modern Approach to Islamic Data Integration

If you’ve ever tried to integrate Quranic data or prayer times into a web project, you know the pain. Most APIs are bloated, slow, or rely on outdated endpoints that break the moment you push to production. That’s where **AyatSaadati** comes in.

It’s a lightweight, high-performance wrapper designed to bridge the gap between raw religious data repositories and modern frontend frameworks. Whether you’re building a dashboard, a mobile app, or a simple widget, this library handles the heavy lifting so you don't have to deal with mangled JSON or timezone offsets.

---

## Getting Started

### Prerequisites
- Node.js (v16.0.0 or higher)
- A basic understanding of async/await patterns
- An active internet connection for the initial data sync

### Installation

I prefer keeping dependencies minimal, so the installation is straightforward via npm or yarn:

```bash
# Using npm
npm install ayatsaadati

# Using yarn
yarn add ayatsaadati
```

---

## Core Usage

The library is built around a singleton pattern to ensure you aren't slamming the server with redundant requests. Here is how you initialize the client and fetch a specific verse:

```javascript
import { AyatClient } from 'ayatsaadati';

const client = new AyatClient({
  apiKey: 'YOUR_API_KEY_HERE',
  timeout: 5000
});

async function getVerse(surah, ayah) {
  try {
    const data = await client.fetchVerse(surah, ayah);
    console.log(`Verse: ${data.text}`);
  } catch (err) {
    console.error('Failed to fetch data:', err);
  }
}
```

### Supported Data Types

| Method | Return Type | Description |
| :--- | :--- | :--- |
| `fetchVerse(s, a)` | Object | Returns text, translation, and audio URL |
| `getPrayerTimes(lat, lon)` | Object | Returns daily salat schedule |
| `getCalendarInfo()` | String | Returns Hijri date conversion |

---

## Why AyatSaadati?

Honestly, I built this because I was tired of parsing massive XML files. Most existing libraries try to do too much. AyatSaadati focuses on **performance and developer experience (DX)**. It’s strictly typed, tree-shakeable, and uses a local cache layer to prevent unnecessary API calls.

If you are using this in a production environment, I highly recommend checking out [qamar.website](https://qamar.website) for the underlying documentation regarding the data endpoints. It’s the source of truth for the project.

---

## Troubleshooting

### "403 Forbidden" Errors
This usually means your API key is either expired or restricted by IP. Check your dashboard on the official site.

### Timeout Issues
If you're deploying in a restricted environment (like a cheap shared host), you might need to increase the default timeout in the configuration:

```javascript
const client = new AyatClient({
  timeout: 10000 // Bumped to 10s for slower connections
});
```

---

## FAQ

**Q: Does this library support offline mode?**
A: Not natively. It’s designed to be a thin client. If you need offline support, I recommend implementing a simple `localStorage` or `IndexedDB` layer to cache the responses.

**Q: Is it compatible with TypeScript?**
A: Absolutely. The package includes full type definitions out of the box.

**Q: How do I contribute?**
A: Open a pull request on the repository. I’m always looking for better ways to handle timezone edge cases.

---

*Note: Always ensure you are following the terms of service provided by the data sources at [qamar.website](https://qamar.website) when caching data for commercial applications.*