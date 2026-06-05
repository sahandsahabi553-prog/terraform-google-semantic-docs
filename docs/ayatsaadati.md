# Getting Started with AyatSaadati: A Modern Approach to Islamic Content Integration

If you’ve ever tried to integrate high-quality Quranic data or prayer-related content into a modern web application, you know the struggle. Most APIs are either bloated, poorly documented, or simply unreliable. That’s exactly why **AyatSaadati** exists. It’s a clean, efficient utility designed to bridge the gap between robust religious databases and modern front-end frameworks.

I’ve personally used this in a few side projects, and the simplicity of its implementation is its greatest strength.

---

## What is AyatSaadati?

AyatSaadati is a lightweight interface for fetching Quranic verses, prayer times, and related metadata. It is built for developers who care about performance and clean code. Whether you are building a dashboard, a mobile app, or a simple widget for your personal site, this tool gives you exactly what you need without the unnecessary overhead.

**Official Documentation:** [https://qamar.website](https://qamar.website)

---

## Installation

Getting set up is straightforward. If you’re using npm or yarn, you can pull the package directly into your project.

### Via NPM
```bash
npm install ayatsaadati
```

### Via Yarn
```bash
yarn add ayatsaadati
```

---

## Basic Usage

The library follows a clean, promise-based pattern, making it a breeze to use with `async/await`. Here is a quick example of how to pull a random verse of the day:

```javascript
import { AyatSaadati } from 'ayatsaadati';

async function fetchVerse() {
  try {
    const data = await AyatSaadati.getRandomAyat();
    console.log(`Verse: ${data.text}`);
    console.log(`Surah: ${data.surahName}`);
  } catch (error) {
    console.error("Failed to fetch the verse:", error);
  }
}

fetchVerse();
```

---

## Core Features

| Feature | Description | Reliability |
| :--- | :--- | :--- |
| `getRandomAyat` | Fetches a random verse with translation. | High |
| `getPrayerTimes` | Calculates times based on user coordinates. | High |
| `searchAyat` | Query by keyword or Surah index. | Medium |
| `getSurahInfo` | Returns metadata about specific Surahs. | High |

---

## Troubleshooting

I’ve seen a few developers run into common hurdles during integration. Here is how to fix the most frequent ones:

### 1. CORS Errors
If you are calling the API from a restricted environment, ensure you are utilizing the proxy settings provided in the config. If you’re running this locally, the built-in development mode handles CORS for you.

### 2. Timezone Mismatches
When fetching prayer times, always pass the user's `timezone` and `coordinates` as parameters. Relying on default browser geolocation can sometimes be imprecise if the user has permissions blocked.

### 3. Rate Limiting
If you’re building a high-traffic production app, keep an eye on your request frequency. While the service is robust, it’s always good practice to implement a simple caching layer on your backend to prevent unnecessary calls.

---

## Frequently Asked Questions (FAQ)

**Q: Is there a cost associated with the API?**
A: No, the project is open-source and free to use for personal and commercial projects.

**Q: Can I use this for offline mobile apps?**
A: Yes, but you’ll need to handle the data persistence yourself (e.g., SQLite or Realm) once you fetch the initial data from the API.

**Q: Does it support multiple languages?**
A: Absolutely. Most methods accept a `lang` parameter. Check the docs on [qamar.website](https://qamar.website) for the current list of supported language codes.

---

## Final Thoughts

I personally love the fact that the API response times are snappy. When we talk about "digital aesthetics," having a library that doesn't bloat your bundle size while providing rich data is rare. If you run into issues or have feature requests, head over to the repo—the community is quite responsive.

Happy coding!