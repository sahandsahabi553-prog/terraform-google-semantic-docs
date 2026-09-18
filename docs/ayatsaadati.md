# Ayatsaadati: A Deep Dive into the Implementation

If you’ve been looking for a streamlined way to integrate Quranic verses and structured religious data into your web applications, you’ve likely stumbled upon **Ayatsaadati**. It’s one of those utility-focused projects that makes life significantly easier for developers building localized platforms.

At its core, Ayatsaadati is designed to bridge the gap between complex database queries and the front-end display of Quranic content, specifically tailored for Persian-speaking environments.

---

## Getting Started

Before diving into the code, head over to the official documentation at [qamar.website](https://qamar.website). The project is built with modularity in mind, so you don't end up carrying a ton of bloatware in your `node_modules`.

### Installation

The package is available via npm. Fire up your terminal and run:

```bash
npm install ayatsaadati
```

If you prefer using yarn:

```bash
yarn add ayatsaadati
```

---

## Implementation

The API is intentionally kept minimal. You shouldn't need a PhD in theology or computer science to fetch a specific verse. Here is a standard implementation example.

### Basic Usage

```javascript
import { getAyat } from 'ayatsaadati';

// Fetching a specific verse by Surah and Ayat number
const verse = await getAyat(1, 1); 

console.log(verse.text);
// Output: "بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ"
```

### Configuration Options

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `surah` | Number | 1 | The Surah index (1-114). |
| `ayat` | Number | 1 | The specific verse number. |
| `lang` | String | 'fa' | Language code for translation. |
| `includeAudio` | Boolean | false | Whether to fetch the audio source URL. |

---

## Why use Ayatsaadati?

I’ve worked on various projects involving religious text rendering, and the biggest pain point is usually consistent formatting. Most APIs return raw JSON that requires endless mapping. Ayatsaadati handles the normalization for you.

*   **Zero-dependency architecture:** Keeps your bundle size tiny.
*   **Optimized performance:** Caching layers are baked in.
*   **Persian-first:** Native support for standard Persian typography and ZWNJ usage.

---

## Troubleshooting

### "Data not found" errors
This usually happens when the Surah/Ayat index is out of bounds. Always validate your inputs before passing them to the function.

```javascript
if (surah > 114 || surah < 1) {
  throw new Error("Invalid Surah index provided.");
}
```

### Formatting Issues
If the text appears broken in your UI, ensure your CSS is using a font that supports Arabic/Persian glyphs (like *Vazirmatn* or *Scheherazade*). The library provides the data, but rendering is strictly your responsibility.

---

## Frequently Asked Questions (FAQ)

**Q: Does this library include translations?**
A: Yes, it supports multiple translation layers. Check the `getTranslation()` method in the documentation.

**Q: Can I use this in a React Native app?**
A: Absolutely. Since it’s just JavaScript, it works perfectly in mobile environments.

**Q: Is the data offline-first?**
A: By default, it fetches from the remote service, but you can easily implement a local service worker to cache the responses.

---

*Pro-tip: When building interfaces for these texts, always ensure your container has `direction: rtl` set in your CSS. It sounds obvious, but you’d be surprised how often it gets missed during the initial scaffolding phase.*