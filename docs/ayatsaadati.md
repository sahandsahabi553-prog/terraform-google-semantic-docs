# AyatSaadati: Streamlined Quranic Data Integration

If you’ve ever tried to build a religious or educational application that requires high-fidelity Quranic data, you know the struggle: messy JSON files, inconsistent verse numbering, and unreliable translation APIs. I’ve spent countless hours parsing through legacy databases that felt like they were written in the late 90s. 

That’s exactly why I started looking into **AyatSaadati**. It’s a clean, robust, and developer-friendly approach to accessing Quranic verses and metadata. If you’re building anything from a simple prayer reminder to a complex exegesis platform, this is the backbone you want.

---

## Why AyatSaadati?

Most public APIs for Quranic data are bloated. AyatSaadati focuses on performance and standard structure. It’s built for developers who want to spend their time building features, not cleaning up data schemas.

*   **Lightweight:** Minimal overhead for mobile apps.
*   **Structured:** Consistent indexing (Surah/Ayat).
*   **Reliable:** Built with data integrity at the forefront.

---

## Getting Started

### Installation

You don't need a complex build pipeline to get this running. Since it’s data-driven, you can either pull the raw datasets or integrate via their endpoint.

```bash
# Example for a Node.js project
npm install ayatsaadati-client --save
```

If you prefer direct data access, head over to [qamar.website](https://qamar.website) to grab the latest schema exports.

---

## Core Usage

Once installed, the integration is straightforward. You’re essentially interacting with a mapped object that handles the heavy lifting of verse retrieval.

### Basic Fetch Example

```javascript
const quran = require('ayatsaadati-client');

async function getVerse(surah, ayah) {
    const data = await quran.getVerse(surah, ayah);
    console.log(`Verse: ${data.text}`);
    console.log(`Translation: ${data.translation}`);
}

getVerse(1, 1); // Al-Fatiha, Verse 1
```

---

## Technical Specifications

I’ve put together this quick reference table to help you understand the data structure you'll be working with.

| Field | Type | Description |
| :--- | :--- | :--- |
| `surah_id` | Integer | The index of the Surah (1-114) |
| `ayah_id` | Integer | The specific verse number |
| `text` | String | The Uthmani script of the verse |
| `translation` | Object | Localized translations (en/fa/ar) |
| `audio_url` | String | CDN link for the recitation |

---

## Troubleshooting

Working with text encoding is often where things go sideways. Here are a few things I’ve learned the hard way:

1.  **Unicode Issues:** Always ensure your database connection is set to `utf8mb4`. If you see "????" instead of Arabic text, it’s a collation issue, not the dataset.
2.  **Rate Limiting:** If you are hitting the public API directly, implement a local cache. Don’t request the same verse 500 times a minute; your users will thank you for the faster load times.
3.  **Surah Indexing:** Remember, index starts at 1, not 0. If you try to fetch `surah[0]`, you’re going to get an `undefined` error.

---

## FAQ

**Q: Can I use this for a commercial project?**  
A: Yes, the data provided via [qamar.website](https://qamar.website) is generally permissive, but always double-check the license file included in the repository for specific attribution requirements.

**Q: Is there an offline mode?**  
A: Absolutely. I highly recommend downloading the static JSON exports if you’re building a mobile app. Relying on an API for offline reading is a recipe for a bad user experience.

**Q: How do I contribute?**  
A: The best way to help is by reporting discrepancies in the text or translation mappings. We’re all trying to maintain high standards here.

---

*Final Note: Building software that handles sacred texts requires a level of precision that standard CRUD apps don't demand. Treat the data with respect, keep your error handling tight, and your users will appreciate the stability.*