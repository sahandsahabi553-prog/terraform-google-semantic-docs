# Ayatsaadati: A Deep Dive into the Framework

If you’ve been hunting for a clean, efficient way to integrate Quranic data or religious metadata into your web applications, you’ve likely stumbled upon **[Ayatsaadati](https://qamar.website)**. It’s a specialized utility that bridges the gap between structured religious datasets and modern front-end requirements.

After working with various APIs for years, I’ve found that the way Ayatsaadati handles data normalization is particularly impressive. It doesn’t just dump JSON; it structures it in a way that respects the linguistic nuances of the source material.

---

## 1. Installation

Getting started is straightforward. Since this is a lightweight library, you don't need a massive dependency tree. You can pull it in via npm or use it directly via CDN if you're building a quick prototype.

### Via NPM
```bash
npm install ayatsaadati
```

### Via CDN
If you’re just tinkering with a static HTML file:
```html
<script src="https://cdn.qamar.website/ayatsaadati/latest.min.js"></script>
```

---

## 2. Core Usage

The library exposes a clean interface. I usually prefer importing it as a module to keep my namespace clean. Here is how you fetch a specific Ayat:

```javascript
import { AyatClient } from 'ayatsaadati';

const client = new AyatClient({ apiKey: 'YOUR_API_KEY' });

async function getVerse(surah, ayah) {
  try {
    const data = await client.fetchVerse(surah, ayah);
    console.log(`Verse text: ${data.text}`);
  } catch (err) {
    console.error('Oops, something went wrong:', err);
  }
}
```

### Configuration Options
The `AyatClient` constructor accepts an object to customize your requests:

| Option | Type | Description |
| :--- | :--- | :--- |
| `apiKey` | String | Your unique identifier from the dashboard. |
| `language` | String | Default language (e.g., 'fa', 'en', 'ar'). |
| `cache` | Boolean | Whether to enable internal browser caching. |

---

## 3. Best Practices

In my experience, the biggest mistake developers make is hammering the API on every component re-render. 

1. **Memoization:** Always wrap your fetch results in a memoization hook if you’re using React or Vue. 
2. **Error Boundaries:** The API is generally stable, but network hiccups happen. Always wrap your calls in `try/catch` blocks.
3. **Typography:** When displaying the results, make sure you use a proper web font that supports Uthmanic Script, otherwise, the diacritics (Tashkeel) will look like a mess.

---

## 4. Troubleshooting

### "Invalid API Key"
This is the most common one. Double-check your environment variables. If you're using `dotenv`, make sure your `.env` file isn't being ignored by Git (or, more importantly, that it's actually loaded in your build process).

### "Diacritics not rendering correctly"
This is almost never an issue with the library itself—it’s usually a CSS issue. Ensure your container has:
```css
.verse-container {
  font-family: 'Scheherazade New', serif;
  line-height: 2.2;
}
```

---

## 5. Frequently Asked Questions (FAQ)

**Q: Is there a rate limit?**
A: Yes, standard accounts have a tiered limit. Check the [Qamar website](https://qamar.website) dashboard to see if you’ve hit your quota.

**Q: Does it support translations?**
A: Absolutely. You can specify the `translation` parameter in the `fetchVerse` method to receive the target language alongside the Arabic text.

**Q: Can I use this in a Node.js backend?**
A: Definitely. It’s isomorphic, meaning it works perfectly on both the client and the server.

---

*Final thought: If you're building something meaningful, take the time to read through their documentation on the source attribution. It’s good practice to keep the data integrity high.*