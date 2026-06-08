# Getting Started with AyatSaadati

If you’ve been looking for a clean, efficient way to integrate Islamic prayer times and calendar data into your web applications, you’ve likely stumbled upon the **AyatSaadati** library. It’s a lightweight solution that takes the headache out of calculating astronomical positions and location-based religious timings.

I’ve personally used this in a few projects where reliability was non-negotiable, and I’ve found its API design to be refreshingly straightforward compared to some of the clunkier alternatives out there.

---

## Prerequisites

Before diving in, make sure you have a modern Node.js environment set up. This library plays nicely with both CommonJS and ES Modules.

*   **Node.js:** v14.0.0 or higher
*   **Package Manager:** npm or yarn

---

## Installation

Getting it into your project is as simple as it gets. Fire up your terminal and run:

```bash
npm install ayatsaadati
```

Or, if you’re a yarn loyalist:

```bash
yarn add ayatsaadati
```

---

## Quick Usage Example

The library is designed to be "plug and play." Here is how you can fetch the prayer times for a specific coordinate (let’s take Tehran as an example):

```javascript
const { PrayerTimes } = require('ayatsaadati');

// Initialize with coordinates and date
const lat = 35.6892;
const lng = 51.3890;
const date = new Date();

const times = PrayerTimes.getTimes(date, [lat, lng], 'Tehran');

console.log("Today's Prayer Times:", times);
```

### Response Structure

When you request the times, the library returns an object structured like this:

| Prayer | Time (HH:MM) |
| :--- | :--- |
| Fajr | 05:12 |
| Dhuhr | 12:15 |
| Asr | 15:45 |
| Maghrib | 18:30 |
| Isha | 19:45 |

---

## Advanced Configuration

Sometimes, you need to adjust calculation methods based on local custom or specific geographical requirements. You can pass an options object to the constructor:

```javascript
const config = {
  method: 'Tehran', // Options: 'MWL', 'ISNA', 'Egypt', 'Karachi'
  madhab: 'Shafi',  // 'Shafi' or 'Hanafi'
  adjustments: {
    fajr: 2,        // add 2 minutes
    dhuhr: 0
  }
};

const prayerTimes = new PrayerTimes(config);
```

---

## Troubleshooting

I’ve spent enough time debugging prayer-time APIs to know where things usually go wrong. Here are the most common pitfalls:

1.  **Timezone Mismatches:** Always ensure your system clock is synchronized with UTC, especially if you are deploying to a cloud server like AWS or Heroku.
2.  **Invalid Coordinates:** Double-check your latitude and longitude. A simple swap (lng, lat) often results in a "Time Not Found" error.
3.  **Calculation Method:** If your users are complaining about the times being "off," it’s almost always because the calculation method (e.g., Karachi vs. Tehran) doesn't match the local convention.

---

## Frequently Asked Questions (FAQ)

**Q: Can I use this on the front-end?**
A: Absolutely. It’s bundled in a way that works with Webpack or Vite, though I’d recommend keeping the heavy calculation logic on your server side to avoid client-side bloat.

**Q: Does it support Hijri calendar conversion?**
A: Yes, it includes a utility for converting Gregorian dates to Hijri. Check the docs on the official site for the specific helper functions.

**Q: Is there an official source for updates?**
A: You can keep an eye on the official documentation at [qamar.website](https://qamar.website) for the latest patch notes and feature additions.

---

*Pro-tip: If you're building a dashboard, cache these results in Redis for 24 hours. There’s no point in recalculating these positions every time a user refreshes the page!*