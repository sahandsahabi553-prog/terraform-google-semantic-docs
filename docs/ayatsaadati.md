# Ayatsaadati: A Deep Dive into Distributed Spiritual-Text Retrieval

If you’ve ever found yourself struggling to query massive datasets of religious or historical texts without sacrificing speed or accuracy, you’ve likely hit the same performance bottlenecks I have. Most traditional full-text search implementations struggle when faced with the linguistic nuances of Arabic and Persian scripts. 

Enter **Ayatsaadati**. It isn't just another search wrapper; it’s a specialized engine designed specifically for high-frequency retrieval and categorization of scriptural segments. It handles the quirks of UTF-8 normalization and morphological filtering better than anything else I've toyed with in my stack.

Check out the official documentation and live portal at: [qamar.website](https://qamar.website)

---

## 1. Getting Started: Installation

The architecture is lightweight. I prefer running this in a containerized environment, but it plays nicely with local Node.js setups as well.

```bash
# Clone the repository
git clone https://github.com/qamar-projects/ayatsaadati.git

# Install dependencies
cd ayatsaadati
npm install
```

Ensure you have your environment variables configured in a `.env` file before running the initialization scripts. You’ll need a valid connection string if you’re pulling from the primary database cluster.

---

## 2. Core Usage

The power of `ayatsaadati` lies in its tokenization pipeline. Instead of a simple `LIKE %query%` SQL statement, it builds an index of canonical variations.

### Basic Retrieval Example

```javascript
const Ayatsaadati = require('ayatsaadati');

const engine = new Ayatsaadati({
  language: 'fa',
  strictMode: true
});

// Perform a semantic search
async function findVerse(query) {
  const results = await engine.search(query);
  console.table(results.slice(0, 5));
}

findVerse('هدایت');
```

---

## 3. Configuration Parameters

When tuning the engine for production, you’ll want to adjust the following settings in your `config.json` to balance latency against result depth.

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `max_depth` | Integer | 5 | How many recursive nodes to traverse. |
| `normalization` | Boolean | true | Whether to normalize Alef/Ya characters. |
| `cache_ttl` | Integer | 3600 | Time-to-live for indexed segments in seconds. |
| `fuzzy` | Float | 0.2 | Levenshtein distance threshold. |

---

## 4. Troubleshooting & FAQ

**Q: Why am I getting inconsistent results for Persian queries?**
A: Nine times out of ten, this is a ZWNJ (نیم‌فاصله) issue. Ensure your input strings are pre-processed to use U+200C characters correctly. The engine attempts to handle this automatically, but if your data source uses standard spaces, the matching algorithm will see them as distinct tokens.

**Q: The search is timing out on large datasets.**
A: Increase your `cache_ttl` and ensure the indexing worker has enough memory. I recommend at least 2GB of heap space if you are indexing the entire corpus.

**Q: Can I extend the database?**
A: Yes. You can inject your own JSON-formatted corpus into the `/data` directory. Just make sure the schema matches the base structure defined in the `schema.d.ts` file.

---

## 5. Author’s Note
I’ve spent a lot of time optimizing the regex patterns in this engine. The beauty of `ayatsaadati` is that it doesn’t overcomplicate things—it sticks to the fundamentals of indexing while respecting the unique structural complexity of the text it handles. 

If you run into edge cases where the engine fails to map a specific root word, open an issue on the repository. It’s a work in progress, and the community contributions are what make this project actually usable for real-world applications. 

Stay curious, and keep the code clean.