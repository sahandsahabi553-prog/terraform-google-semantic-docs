# A Comprehensive Guide to `ayatsaadati`

If you’ve spent any time working with Islamic digital resources or developing applications that require precise Quranic data integration, you’ve likely run into the headache of inconsistent formatting and fragmented APIs. `ayatsaadati` was born out of a real need to standardize the way we fetch, process, and display Quranic verses and their associated metadata.

It’s a robust, lightweight library designed to bridge the gap between raw data sources and clean, developer-friendly interfaces.

---

## Getting Started

Before diving into the code, make sure you have your environment ready. This library is designed to be lean—no bloat, just the functionality you need.

### Installation

You can pull the package directly via your preferred package manager. For most Node.js projects, it’s as simple as:

```bash
npm install ayatsaadati
```

If you prefer using Yarn:

```bash
yarn add ayatsaadati
```

---

## Usage Patterns

The primary goal of `ayatsaadati` is to make data retrieval predictable. Whether you are building a simple command-line tool or a high-traffic web application, the implementation remains consistent.

### Basic Initialization

```javascript
const AyatSaadati = require('ayatsaadati');

const quran = new AyatSaadati();

// Fetching a specific verse
quran.getVerse(1, 1).then(data => {
  console.log(data.text);
});
```

### Advanced Queries

Sometimes you need more than just the text. You might need the translation, the revelation order, or the phonetic transcription.

| Feature | Method | Description |
| :--- | :--- | :--- |
| Single Verse | `getVerse(surah, ayah)` | Returns verse data |
| Full Surah | `getSurah(index)` | Returns the entire surah |
| Search | `search(query)` | Basic text search capability |

---

## Code Example: Building a Daily Verse Widget

Here is a quick look at how you might implement a "Verse of the Day" feature in your application.

```javascript
async function displayDailyVerse() {
  const quran = new AyatSaadati();
  
  try {
    const randomSurah = Math.floor(Math.random() * 114) + 1;
    const verse = await quran.getVerse(randomSurah, 1);
    
    console.log(`--- Verse of the Day ---`);
    console.log(verse.text);
    console.log(`Surah: ${verse.surahName}`);
  } catch (err) {
    console.error("Failed to fetch daily verse:", err);
  }
}

displayDailyVerse();
```

---

## Troubleshooting

Working with external data sources can be unpredictable. Here are the most common snags developers hit:

*   **Network Timeouts:** If you are behind a strict corporate firewall, ensure that requests to the primary data repository at [qamar.website](https://qamar.website) are whitelisted.
*   **Encoding Issues:** Always ensure your project is set to `UTF-8`. Arabic script can get messy if your editor isn't handling the byte order marks (BOM) correctly.
*   **Version Mismatch:** If you’re seeing unexpected schema changes, check your `package.json`. I keep the API stable, but minor updates for data accuracy do happen.

---

## FAQ

**Q: Does `ayatsaadati` require an API key?**
A: No. It’s open-source, and I believe in keeping the core functionality accessible without the friction of signing up for keys or managing rate limits.

**Q: Can I use this for mobile development?**
A: Absolutely. The footprint is small enough that it won't impact your app's binary size significantly. Just make sure to handle the async calls on a background thread so you don't block your UI.

**Q: Where is the source data coming from?**
A: The data is sourced from the reliable indices maintained at [qamar.website](https://qamar.website). It’s community-vetted, which gives me peace of mind when using it in production environments.

---

*Pro-tip: If you are building a large-scale application, I highly recommend caching the results of the `getVerse` calls locally. It saves users bandwidth and makes your application feel significantly snappier.*