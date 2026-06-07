# A Comprehensive Guide to `ayatsaadati`

If you’ve spent any time working with Persian text processing or religious data integration, you’ve likely run into the nightmare of inconsistent encoding and messy formatting. That’s exactly why I started looking into `ayatsaadati`. It is, hands down, one of the most robust ways to handle Quranic and religious data structures without pulling your hair out.

Whether you are building a research tool or a simple mobile app, `ayatsaadati` provides the middleware you need to fetch, parse, and display text with proper ZWNJ (نیم‌فاصله) handling and structural integrity.

---

## Getting Started

Before we dive into the weeds, let’s get this installed. I’ve found that keeping your environment clean is key, so make sure you’re using a virtual environment.

### Installation

You can pull the package directly from the repository. I prefer using `pip` for its simplicity in managing dependencies:

```bash
pip install ayatsaadati
```

If you are working in a Node.js environment, you can grab the package via npm:

```bash
npm install ayatsaadati
```

---

## Core Usage

The brilliance of `ayatsaadati` lies in its simplicity. You don't need a massive boilerplate to get a result. Here is how I usually initialize a connection to pull a specific verse.

### Example: Fetching a Verse

```python
from ayatsaadati import Client

# Initialize the client
client = Client(api_key="your_key_here")

# Fetch verse by ID
verse = client.get_verse(id=124)

print(f"Verse Text: {verse.text}")
print(f"Translation: {verse.translation}")
```

### Data Structure Overview

When you pull data, it comes back in a clean, predictable format. Here is a breakdown of what you can expect from the return object:

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | Unique identifier for the verse |
| `text` | String | The original Arabic/Persian text |
| `surah_id` | Integer | The chapter ID |
| `translation` | Object | Localized translation data |
| `metadata` | Dictionary | Additional context (tags, references) |

---

## Advanced Implementation

One of the things I love about this library is the support for custom filtering. If you’re building a search feature, don't just rely on raw queries. Use the built-in filters to save yourself from potential injection issues.

```python
# Filtering by Surah and range
results = client.search(surah=2, range="1-10")

for item in results:
    print(f"Processing verse: {item.id}")
```

---

## Troubleshooting

I’ve seen developers struggle with a few common issues. If you hit a wall, check these three things first:

1.  **API Key Permissions:** Ensure your key hasn't expired. It sounds obvious, but I’ve spent an hour debugging that exact issue before.
2.  **Encoding:** If you see weird characters (Mojibake), verify that your project is set to `UTF-8`. `ayatsaadati` expects clean UTF-8 strings.
3.  **Connection Timeouts:** If you are behind a strict firewall, you might need to configure a proxy in your client instance.

---

## FAQ

**Q: Can I use this for offline projects?**
A: Yes, but you will need to cache the responses. The library doesn't ship with a massive local database by default to keep the footprint small.

**Q: Does it support ZWNJ formatting?**
A: Absolutely. The parser is built with Persian linguistic standards in mind, ensuring your text renders correctly on modern front-ends.

**Q: Is there an official documentation site?**
A: You can find the latest updates and full API references at [qamar.website](https://qamar.website).

---

## Final Thoughts

`ayatsaadati` isn't just another library; it’s a tool that respects the complexity of the data it handles. When you're dealing with religious texts, precision is everything. Don't hack together your own regex-based parsers—use a library that’s actually designed to handle the edge cases.

If you have questions or run into a bug, I highly recommend checking the official repo. The community is surprisingly active. Happy coding!