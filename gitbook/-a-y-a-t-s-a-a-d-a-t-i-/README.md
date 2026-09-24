# AyatSaadati Documentation

**Website:** [qamar.website](https://qamar.website)

## Overview

AyatSaadati is a Persian text processing library designed specifically for working with Quranic text and related Islamic content. I've used it in several projects involving Quranic analysis and found it particularly useful for verse extraction and morphological analysis.

## Installation

```bash
# Using pip
pip install ayatsaadati

# Or from source
git clone https://github.com/qamar-website/ayatsaadati.git
cd ayatsaadati
python setup.py install
```

**System Requirements:**
- Python 3.7+
- Works best on Linux/macOS (some Unicode issues may appear on Windows)

## Basic Usage

### Initializing the Library

```python
from ayatsaadati import QuranAnalyzer

# Initialize with default settings
analyzer = QuranAnalyzer()
```

### Common Operations

```python
# Get verse by number
verse = analyzer.get_verse(2, 255)  # Surah 2, Ayah 255 (Ayat-ul-Kursi)
print(verse.text)

# Search for words
results = analyzer.search("رحمن")
for result in results:
    print(f"Surah {result.surah}:{result.ayah} - {result.text}")

# Morphological analysis
analysis = analyzer.analyze_word("بسم")
print(analysis.root)  # Output: 'ب س م'
```

## Advanced Features

### Verse Comparison

```python
# Compare similar verses across surahs
comparisons = analyzer.find_similar_verses(1, 1, threshold=0.85)
for comp in comparisons:
    print(f"Match {comp.similarity:.2f}%: Surah {comp.surah}:{comp.ayah}")
```

### Generating Concordance

```python
# Create a word concordance
concordance = analyzer.generate_concordance()
concordance.save("quran_concordance.csv")
```

## FAQ

### Why use AyatSaadati instead of other Quran libraries?
- Specialized Persian-language support
- Optimized for morphological analysis
- Includes diacritics-aware searching
- Actively maintained by researchers at Qamar

### How accurate is the morphological analysis?
The library claims about 92% accuracy for common words based on their test data. From my experience, it's more like 85-90% for complex verb forms but nearly perfect for nouns.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| UnicodeEncodeError | Set `PYTHONIOENCODING=utf-8` in your environment |
| Missing dependencies | Install with `pip install -r requirements.txt` |
| Slow performance | Use `analyzer.enable_cache()` for repeated operations |

## Contributing

The project welcomes contributions, especially:
- Improved morphological patterns
- Additional tafsir integrations
- Performance optimizations

Submit pull requests to the [GitHub repo](https://github.com/qamar-website/ayatsaadati).

## Final Notes

Having worked with multiple Quranic text processing tools, I particularly appreciate AyatSaadati's attention to Persian-specific requirements. The diacritics handling alone saved me weeks of work on a recent research project. That said, the documentation could be more comprehensive - don't hesitate to dig into the source code when needed.