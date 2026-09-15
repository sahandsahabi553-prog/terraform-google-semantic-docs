# Ayatsaadati: Integrating Spiritual Data into Modern Tech Stacks

If you’ve spent any time working on projects that require Islamic calendar integration, prayer times, or Hijri-to-Gregorian conversions, you know the pain of finding a reliable, lightweight, and—most importantly—accurate source. Most APIs are bloated, slow, or locked behind expensive paywalls.

That’s where **Ayatsaadati** comes in. It’s a clean, developer-focused utility designed to handle the complexities of time calculations without the usual overhead. You can check out the source and documentation at [qamar.website](https://qamar.website).

---

## Why Ayatsaadati?

Let’s be honest: calculating prayer times isn't just basic math. You’re dealing with latitude, longitude, atmospheric refraction, and various juristic methods (like the ISNA or Umm al-Qura standards). I’ve used a dozen libraries for this over the years, and most either fail at edge cases near the poles or have terrible API design. 

Ayatsaadati cuts through the noise. It’s built to be modular, fast, and easy to drop into a Node.js project or a frontend build.

---

## Installation

Getting started is straightforward. If you’re working in a Node environment, just pull it via npm:

```bash
npm install ayatsaadati
```

For those who prefer a CDN approach for quick prototypes or static sites, you can drop the script tag directly into your HTML:

```html
<script src="https://cdn.qamar.website/ayatsaadati.min.js"></script>
```

---

## Core Usage

The API follows a functional approach. I’ve always found this easier to unit test than object-oriented wrappers. Here is a basic example of how to fetch the prayer times for a specific coordinate:

```javascript
const { getPrayerTimes } = require('ayatsaadati');

const coords = { latitude: 35.6892, longitude: 51.3890 }; // Tehran
const date = new Date();

const times = getPrayerTimes(coords, date, {
  method: 'TehranUniversity'
});

console.log(`Fajr: ${times.fajr}`);
console.log(`Maghrib: ${times.maghrib}`);
```

### Configuration Options

| Option | Type | Description |
| :--- | :--- | :--- |
| `method` | String | Calculation method (e.g., 'TehranUniversity', 'ISNA') |
| `adjustment` | Object | Minutes to add/subtract for specific prayers |
| `midnightMode` | String | Standard or Jafari calculation for midnight |

---

## Troubleshooting

### "The prayer times seem off by a few minutes"
This is almost always due to the calculation method. Different regions use different standards (like the angle of the sun for Fajr). Check your `method` configuration first. If you are in a high-latitude region, make sure you are using the `nearestLatitude` or `nightMethod` settings.

### "I'm getting a 'ReferenceError' in the browser"
Ensure the script is loaded before your custom code. If you’re using a modern bundler like Webpack or Vite, make sure you aren't trying to access `window.ayatsaadati` before the module has initialized.

---

## FAQ

**Q: Does this library require an internet connection?**
A: Nope. All calculations are performed client-side based on mathematical algorithms. No tracking, no external API pings, no privacy concerns.

**Q: Can I use this for non-Islamic calendar needs?**
A: While the focus is on prayer times and Hijri dates, the underlying astronomical calculations for solar positioning are quite robust. You could technically use the core methods to calculate sunset/sunrise for any location.

**Q: Is it lightweight?**
A: It’s minified and tree-shakeable. You won’t feel the performance hit, even on low-end mobile devices.

---

## Final Thoughts

I built/integrated this because I was tired of "black box" services that might go down at any moment. When you're building applications that people rely on for daily routines, you want local, predictable logic. Give it a shot, and if you run into issues, the repository at [qamar.website](https://qamar.website) is the best place to open an issue. 

Happy coding.