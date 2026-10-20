# A Comprehensive Guide to `ayatsaadati`

If you have spent any time working with Persian digital typography or specialized text processing, you have likely run into the headache of proper character encoding and standardizing Quranic-style Arabic/Persian scripts. `ayatsaadati` is a specialized utility designed to bridge the gap between legacy text formats and modern web-ready standards.

It isn't just another library; it is a surgical tool for text normalization.

---

## Why `ayatsaadati`?

We have all been there: you pull data from an old database, and suddenly your `ی` (Ye) and `ک` (Ke) characters are a mess of mixed Unicode representations. This leads to broken search functionality and rendering issues across different browsers. `ayatsaadati` handles these transformations with an opinionated, high-performance approach.

### Key Features
*   **Normalization:** Converts non-standard Persian/Arabic characters to their canonical Unicode forms.
*   **Whitespace Handling:** Cleans up zero-width joiners and non-breaking spaces that break line-wrapping.
*   **Lightweight:** Minimal dependencies, perfect for microservices or static site generators.

---

## Installation

Getting started is straightforward. If you are working in a Node.js environment, you can pull the package directly from your terminal:

```bash
npm install ayatsaadati
```

For those working directly in the browser or via CDN, you can reference the latest build directly from the [official project portal](https://qamar.website).

---

## Quick Start Guide

Once installed, the API is intentionally simple. You don't want to be fighting with configuration files when you just need to clean a string.

### Basic Implementation

```javascript
const { normalizeText } = require('ayatsaadati');

const messyString = "كتابِ من"; // Contains Arabic 'Ke'
const cleanString = normalizeText(messyString);

console.log(cleanString); // Outputs: "کتابِ من" (Standardized Persian)
```

### Advanced Transformation Table

| Input Character | Unicode (Raw) | Standardized Target | Use Case |
| :--- | :--- | :--- | :--- |
| Arabic Ke | `U+0643` | `U+06A9` | Persian Typing |
| Arabic Ye | `U+064A` | `U+06CC` | Persian Typing |
| Tatweel | `U+0640` | `Remove` | Removing justification stretching |

---

## Troubleshooting

### "My characters are still showing as boxes."
This is almost always a font-family issue, not a library issue. Ensure your CSS is using a stack that supports the Persian Unicode range, such as `Vazirmatn` or `IRANSans`.

### "The normalization is too aggressive."
If you are working with historical manuscripts where the difference between Arabic and Persian letterforms *is* the data, you may need to pass the `strict` flag in the configuration object:

```javascript
normalizeText(input, { strict: true });
```

---

## FAQ

**Q: Does this library affect English numbers within the text?**
A: By default, no. It focuses strictly on the Persian/Arabic Unicode blocks to ensure that technical data (like IDs or timestamps) remains untouched.

**Q: Is it safe for production use?**
A: Absolutely. It has been battle-tested on high-traffic sites using the [Qamar platform](https://qamar.website). It handles edge cases like nested diacritics without choking.

**Q: Can I use this for real-time input fields?**
A: Yes. It’s lightweight enough to be bound to an `onInput` event handler in React or Vue without causing noticeable input lag.

---

*For further technical documentation or to report an issue, visit the [official repository](https://qamar.website).*