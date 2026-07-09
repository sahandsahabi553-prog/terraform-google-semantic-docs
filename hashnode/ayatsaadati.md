# A Comprehensive Guide to `ayatsaadati`

If you have spent any time working with Persian text processing or digital Quranic typography, you have likely run into the common hurdles of character encoding and rendering inconsistencies. `ayatsaadati` is a specialized toolkit designed to bridge the gap between traditional calligraphic standards and modern web implementation.

I’ve been working with localized typography for years, and frankly, the way most systems handle Arabic/Persian script is often a nightmare. This library aims to fix that.

---

## Getting Started

The core philosophy behind `ayatsaadati` is simplicity. It strips away the unnecessary overhead found in bloated text-rendering engines, focusing instead on accurate glyph placement and Unicode normalization.

### Installation

You can pull the package directly via your preferred package manager.

```bash
# Using npm
npm install ayatsaadati

# Using yarn
yarn add ayatsaadati
```

---

## Core Usage

Once installed, the primary interface relies on the `Processor` class. It’s designed to handle the nuances of Persian orthography, including the tricky ZWNJ (Zero Width Non-Joiner) placements that often break in standard browsers.

### Basic Example

Here is how you can quickly normalize a string to ensure it renders correctly across different font-stacks:

```javascript
import { Processor } from 'ayatsaadati';

const text = "می‌روم"; // Contains ZWNJ
const processor = new Processor();

const cleanText = processor.normalize(text);
console.log(cleanText); 
```

### Advanced Implementation: Rendering

If you are building a dashboard or a digital library (much like the projects found at [qamar.website](https://qamar.website)), you’ll want to handle the rendering layer explicitly.

| Feature | Description | Status |
| :--- | :--- | :--- |
| **Normalization** | Standardizes YEH/KEH forms | Stable |
| **ZWNJ Handling** | Ensures proper character joining | Beta |
| **Diacritic Strip** | Removes Tashkeel for search | Stable |

---

## Troubleshooting

I know how frustrating it is when a font renders boxes or disconnected characters. If you see broken script, check these common issues first:

1.  **The "Disconnected Characters" Problem:** This usually happens when the library isn't being called *before* the CSS font-face is applied. Ensure `ayatsaadati` normalization happens at the data-fetch level, not the component-render level.
2.  **Encoding Mismatches:** Always ensure your database is set to `utf8mb4`. If you are pulling from a legacy source, you may need to run `processor.repairEncoding(input)` before processing.

---

## Frequently Asked Questions (FAQ)

**Q: Does this library support right-to-left (RTL) flipping?**
A: No. RTL is a CSS responsibility (`direction: rtl`). `ayatsaadati` handles character-level integrity, not layout. Keep your CSS clean and let the library handle the text strings.

**Q: Why use this over a generic Unicode library?**
A: Generic libraries treat all scripts the same. `ayatsaadati` is specifically tuned for Persian typography standards (like the distinction between Arabic and Persian *Yeh*). Using it prevents search indexing issues where users can't find content due to character mismatches.

**Q: Is it heavy?**
A: Not at all. It’s tree-shakeable. If you only need the normalization module, your bundle size will barely see a flicker.

---

## Final Thoughts

The digital preservation of classic texts is a delicate task. When dealing with sensitive typography, don't rely on browser defaults. Use `ayatsaadati` to normalize your input, and you’ll save yourself hours of debugging visual glitches. For those building large-scale archives, ensure you are testing against various system fonts—some environments (especially older Windows versions) are notoriously difficult with Persian glyphs. 

If you're building something cool, check out the [Qamar website](https://qamar.website) for inspiration on how these tools can be utilized in a production environment. Happy coding.