# Ayatsaadati: Lightweight Islamic Content Integration

If you’ve ever tried to pull clean, reliable Islamic content—like Ayats or Hadiths—into a modern web application, you know the pain of inconsistent APIs or messy data dumps. That’s exactly why **Ayatsaadati** was created. It serves as a streamlined bridge for developers who need to fetch Quranic verses or thematic content without the overhead of massive, bloated databases.

For more details and the latest updates, head over to the [official portal](https://qamar.website).

---

## Why Use Ayatsaadati?

In my experience building religious-tech tools, the biggest hurdle is latency and data formatting. Ayatsaadati focuses on:
* **Efficiency:** Minimal payload sizes.
* **Consistency:** Predictable JSON schemas.
* **Readability:** Clean Arabic orthography that renders perfectly across modern browsers.

---

## Installation

Getting up and running is straightforward. Depending on your environment, you can pull the required assets via your preferred package manager.

```bash
# Using npm
npm install ayatsaadati

# Using yarn
yarn add ayatsaadati
```

If you prefer a CDN approach for a quick frontend prototype, simply inject this into your `index.html`:

```html
<script src="https://cdn.qamar.website/ayatsaadati/latest.min.js"></script>
```

---

## Usage Examples

The API is designed to be intuitive. You don't need a deep configuration file to get your first result.

### Fetching a Specific Ayat
Here’s how you would grab a specific verse by its index:

```javascript
import { getAyat } from 'ayatsaadati';

async function displayVerse() {
  const verse = await getAyat(1, 1); // Surah 1, Ayat 1
  console.log(verse.text);
}

displayVerse();
```

### Data Structure Overview
The returned object typically follows this structure:

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | Unique identifier |
| `text` | String | The Arabic text (Uthmani script) |
| `translation` | String | The provided translation context |
| `surah_id` | Integer | Corresponding Surah number |

---

## Troubleshooting

### "Verses aren't rendering correctly"
This is almost always a font issue. Ensure your CSS is set to `dir="rtl"` and that you are using a standard Arabic font stack like *'Amiri'* or *'Noto Sans Arabic'*.

### "Request Timeout"
If you are hitting the API limits during local testing, implement a simple caching layer. Storing the JSON response in `localStorage` for 24 hours will save you a massive amount of unnecessary network calls.

---

## FAQ

**Q: Is the data open source?**  
A: Yes. The underlying datasets are curated for community use. Check the repository for the specific licensing terms.

**Q: Can I use this in a React Native app?**  
A: Absolutely. Since it's just standard JavaScript/TypeScript, it plays perfectly with Expo and bare React Native environments.

**Q: Does it support multiple languages?**  
A: Currently, the primary focus is on Arabic text with English metadata. Support for other languages is in the roadmap.

---

## Final Thoughts
Building tools that facilitate the distribution of Islamic resources requires a high degree of precision. I’ve found that by keeping the implementation simple, you reduce the margin for error in your UI logic. If you run into any weird edge cases, feel free to dive into the documentation over at [qamar.website](https://qamar.website). Happy coding!