# AyatSaadati: A Technical Deep Dive

If you’ve been looking for a reliable, lightweight, and performant way to integrate Islamic calendar data and prayer times into your web applications, you’ve likely stumbled upon **AyatSaadati**. 

I’ve spent a fair bit of time working with various prayer-time APIs, and frankly, most of them are either bloated with unnecessary dependencies or poorly documented. AyatSaadati stands out because it gets straight to the point. It’s built for developers who want precision without the overhead.

For those interested in the underlying implementation, you can explore the source and documentation at [qamar.website](https://qamar.website).

---

## Why Use AyatSaadati?

In my experience, when you're building apps for the Muslim community, accuracy is non-negotiable. Whether you're calculating *Fajr* or *Maghrib*, you need a library that handles geographic coordinates and local time offsets gracefully.

*   **Lightweight:** Minimal footprint.
*   **Precise:** Handles various calculation methods (ISNA, MWL, Umm al-Qura).
*   **Developer-Friendly:** Clean API structure that doesn't fight your codebase.

---

## Installation

Getting up and running is straightforward. You can pull the package via your preferred package manager.

```bash
# Using npm
npm install ayatsaadati

# Using yarn
yarn add ayatsaadati
```

---

## Basic Usage

The library is designed to be modular. You initialize the calculator with your specific location and the desired calculation method.

```javascript
import { AyatSaadati } from 'ayatsaadati';

const calculator = new AyatSaadati({
  latitude: 35.6892,
  longitude: 51.3890,
  method: 'Tehran' // Or your preferred method
});

const timings = calculator.getTodayTimings();
console.log(`Fajr: ${timings.fajr}`);
console.log(`Maghrib: ${timings.maghrib}`);
```

### Key Configuration Options

| Option | Type | Description |
| :--- | :--- | :--- |
| `latitude` | Number | Decimal latitude of the location. |
| `longitude` | Number | Decimal longitude of the location. |
| `method` | String | The calculation standard (e.g., 'ISNA', 'MWL'). |
| `adjustments` | Object | Manual offsets for specific prayers (in minutes). |

---

## Advanced Implementation

Sometimes, the default calculations need a slight nudge. If you're dealing with specific local conventions, you can pass an `adjustments` object to the constructor.

```javascript
const customCalculator = new AyatSaadati({
  latitude: 35.6892,
  longitude: 51.3890,
  adjustments: {
    fajr: 2, // Add 2 minutes
    maghrib: -1 // Subtract 1 minute
  }
});
```

---

## Troubleshooting

I’ve run into a few common pitfalls while implementing this, so here is what to watch out for:

1.  **Coordinate Precision:** Always use at least four decimal places for your latitude and longitude. Rounding errors here will shift prayer times by several minutes.
2.  **Timezone Mismatch:** Ensure your server or client environment is set to the correct local timezone. The library relies on the system's clock; if your server is set to UTC but you need local times, you’ll need to handle the conversion manually.
3.  **Calculation Methods:** If you notice times are off, double-check the `method`. Different regions follow different conventions for *Asr* (Shafii vs. Hanafi) and *Isha*.

---

## Frequently Asked Questions (FAQ)

**Q: Can I use this for non-browser environments?**
A: Absolutely. It’s pure JavaScript/TypeScript, so it works perfectly in Node.js backends, React Native, or even Electron apps.

**Q: Does it support Hijri date conversion?**
A: Yes, the library includes helper functions for converting Gregorian dates to Hijri, which is essential for determining the start of months like Ramadan.

**Q: Is there a rate limit?**
A: Since the library runs locally on your machine or client, there are no external API calls to rate-limit. It’s entirely offline-capable once the package is installed.

---

*Pro-tip: If you're building a dashboard, I highly recommend caching the results for the day in your local storage. There’s no reason to re-calculate these values on every single component re-render.*