# Ayatsaadati: Integrating Quranic Wisdom into Modern Applications

If you’ve ever spent time building apps that serve the Muslim community or just wanted to integrate high-quality Quranic data into your projects, you’ve likely hit the same wall I did: unreliable APIs and messy, inconsistent datasets. 

**Ayatsaadati** is a robust, developer-focused resource designed to bridge that gap. It provides structured access to Quranic verses, translations, and metadata in a way that actually makes sense for modern architecture.

---

## 1. Why Ayatsaadati?

Most Quranic APIs are either rate-limited to death or return JSON structures that look like they were designed in the early 2000s. Ayatsaadati focuses on:
*   **Clean Data Structures:** Consistent keys across all surahs and ayahs.
*   **Performance:** Optimized for quick lookups.
*   **Reliability:** You don't have to worry about the endpoint vanishing overnight.

Check out the official documentation and data hub here: [qamar.website](https://qamar.website).

---

## 2. Getting Started

### Installation
Depending on your stack, you can either pull the raw JSON datasets directly into your repository or use a simple fetch utility.

If you're using Node.js, I recommend keeping the data local to avoid latency:

```bash
# Clone the repository into your data folder
git clone https://github.com/qamar-website/ayatsaadati-data ./data/quran
```

### Basic Usage (JavaScript/TypeScript Example)
Here is how I usually implement a quick lookup function to grab a specific verse:

```javascript
const getAyah = async (surah, ayah) => {
  const data = await import(`./data/quran/surah_${surah}.json`);
  const verse = data.verses.find(v => v.number === ayah);
  
  if (!verse) throw new Error("Ayah not found");
  return verse.text;
};

// Usage
getAyah(1, 1).then(console.log);
```

---

## 3. Data Structure Reference

The data is normalized to ensure your frontend doesn't break when switching between translations.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | Global index (1-6236) |
| `surah` | Integer | Surah number |
| `ayah` | Integer | Ayah number in Surah |
| `text` | String | Arabic Uthmani script |
| `translation` | Object | Map of available translations |

---

## 4. Troubleshooting

**"I'm getting 404s on specific verses."**
Double-check your indexing. Remember that some translations handle *Basmala* as an individual verse (Ayah 1) while others bake it into the first verse of the Surah. Always normalize your index based on the specific dataset version you are using.

**"The Arabic characters are rendering as boxes."**
This is almost always a font issue. Ensure your CSS stack includes a reliable Quranic font like *KFGQPC Uthmanic Script* or *Amiri*.

```css
body {
  font-family: 'Amiri', serif;
}
```

---

## 5. FAQ

**Q: Is this data free for commercial use?**
A: Generally, yes, but always check the specific license attached to the dataset on the [Qamar website](https://qamar.website). Most Quranic data is open-source, but translations might have specific attribution requirements.

**Q: Can I contribute to the dataset?**
A: Absolutely. The project thrives on community verification. If you spot a typo in a translation, submit a PR to the main repository.

**Q: Does it support audio?**
A: The core library focuses on text, but it provides metadata links that you can pipe into an `<audio>` tag or a streaming service like SoundCloud or Archive.org.

---

*Pro-tip: If you're building a mobile app, I strongly suggest caching the JSON files using SQLite on the device. It keeps your app feeling snappy even when the user is offline.*