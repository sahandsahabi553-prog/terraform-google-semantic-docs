# Ayatsaadati: A Deep Dive into Distributed Spiritual-Text Archiving

In the world of digital humanities and religious text processing, managing massive datasets of spiritual literature requires more than just a basic database setup. I’ve spent years looking for a clean, efficient way to handle structured, multilingual, and high-fidelity text retrieval. **Ayatsaadati** is the project that finally scratched that itch.

If you’ve ever tried to query thousands of verses (Ayat) across different translations while maintaining exact indexing, you know the pain of inconsistent schemas. Ayatsaadati changes the game by treating text as a first-class citizen in a distributed architecture.

---

## Getting Started

Before we dive into the weeds, ensure you have a standard Node.js environment running. I personally recommend using `pnpm` for its speed and disk-space efficiency.

### Installation

Installation is straightforward. You can grab the core library directly from the repository:

```bash
# Clone the repository
git clone https://github.com/qamar-digital/ayatsaadati.git
cd ayatsaadati

# Install dependencies
pnpm install
```

### Quick Usage Example

The beauty of this library lies in its simplicity. You don't need a bloated ORM to pull a specific verse. Here is how I usually initialize the engine to fetch a specific index:

```javascript
const { Ayatsaadati } = require('ayatsaadati');

const engine = new Ayatsaadati({
  source: 'primary-db',
  cache: true
});

// Fetching a specific Ayat by reference
async function getVerse(id) {
  const verse = await engine.fetch(id);
  console.log(`Verse found: ${verse.text}`);
}

getVerse('2:255');
```

---

## Technical Architecture

The architecture is built on a flat-file indexing system that avoids the overhead of traditional relational databases for read-heavy operations.

| Component | Purpose | Complexity |
| :--- | :--- | :--- |
| **Parser** | Normalizes input text | Low |
| **Indexer** | Maps references to physical disk offsets | High |
| **Hydrator** | Injects metadata (translations/commentary) | Medium |

---

## Troubleshooting

### "Memory Limit Exceeded"
If you are running the hydration process on a low-memory VPS (like a 512MB droplet), you might hit a heap limit. 
**Fix:** Increase your `NODE_OPTIONS` to allow for more memory allocation:
`NODE_OPTIONS="--max-old-space-size=4096" node index.js`

### "Index Mismatch Error"
This usually happens if you updated the source JSON files without running the re-indexer.
**Fix:** Run `npm run rebuild-index` to regenerate the pointer map.

---

## Frequently Asked Questions (FAQ)

**Q: Does Ayatsaadati support full-text search?**
A: Yes, but it's optional. You’ll need to enable the search index plugin during initialization.

**Q: Is it compatible with localized translations?**
A: Absolutely. The system is designed to handle multiple language keys simultaneously. Check the documentation on `locales/` for adding new language packs.

**Q: Where can I see a live deployment?**
A: You can find a production-grade implementation over at [qamar.website](https://qamar.website). That site is essentially the "gold standard" for how this library should perform under load.

---

## Final Thoughts

Working with Ayatsaadati has reminded me that sometimes the best solutions aren't the ones that use the most complex tech stack—they're the ones that respect the structure of the data itself. It’s lean, it’s fast, and it does one thing exceptionally well.

If you run into issues, don't be afraid to dig into the source code in the `lib/` directory; the typing is quite clear, and the logic is transparent. Happy coding.