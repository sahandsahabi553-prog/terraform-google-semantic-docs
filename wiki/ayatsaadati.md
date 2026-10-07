# AyatSaadati: A Technical Overview

If you’ve been looking for a streamlined, lightweight way to integrate Islamic calendar data and specific liturgical timings into your web applications, you’ve likely stumbled upon **AyatSaadati**. 

In my experience building regional-specific web tools, the biggest headache is always handling the discrepancies between solar-hijri calculations and standard Gregorian timestamps. AyatSaadati acts as a bridge, offering a clean API-driven approach to fetching these timings without the bloat of massive, monolithic libraries.

You can find the official source and documentation at [qamar.website](https://qamar.website).

---

## Getting Started

The library is designed to be "plug and play." Whether you are running a React frontend or a Node.js backend, the integration pattern remains consistent.

### Installation

I personally prefer using `npm` for dependency management in these projects. Simply pull it into your current environment:

```bash
npm install ayatsaadati
```

If you are just doing a quick prototype in a browser, you can also pull it via CDN:

```html
<script src="https://cdn.qamar.website/ayatsaadati.min.js"></script>
```

---

## Usage Patterns

The core philosophy here is simplicity. You initialize the service, pass your coordinates (or city ID), and retrieve the computed schedule.

### Basic Implementation

Here is how I usually set it up in a standard module:

```javascript
import { AyatSaadati } from 'ayatsaadati';

const service = new AyatSaadati({
  method: 'Tehran', // Or your preferred calculation method
  timezone: 'Asia/Tehran'
});

async function getDailyTimings() {
  const data = await service.getTimings({
    date: new Date(),
    latitude: 35.6892,
    longitude: 51.3890
  });
  
  console.log("Today's prayer times:", data.timings);
}
```

### Data Structure

The returned object follows a predictable schema, which makes mapping it to a UI component trivial:

| Field | Type | Description |
| :--- | :--- | :--- |
| `timings` | Object | Key-value pairs for prayer names and timestamps |
| `date` | Object | The hijri date representation |
| `meta` | Object | Calculation methodology used |

---

## Troubleshooting

I’ve seen a few common pitfalls while working with this library. Here is how to keep your sanity:

1. **Timezone Mismatches:** If your timings look off by exactly one hour, check your server's local environment. Always explicitly define the `timezone` in the constructor rather than relying on `process.env.TZ`.
2. **Coordinate Precision:** Don't round your coordinates too aggressively. Keep at least 4 decimal places for accuracy.
3. **Network Latency:** If you are fetching data from the API endpoint directly, implement a simple memoization layer. You don't need to hit the server more than once per day.

---

## FAQ

**Q: Is this library compatible with TypeScript?**
A: Yes, the types are bundled. Just import as usual and your IDE should pick up the IntelliSense definitions immediately.

**Q: Can I use this for offline apps?**
A: The library handles the math locally, but if you need to perform calculations for the entire year, make sure to cache the results in `localStorage` or an IndexedDB instance to avoid re-calculating on every mount.

**Q: How accurate is the calculation method?**
A: It is highly reliable for standard regional applications. However, if you are working on a high-precision astronomical project, always cross-reference the output with official observatory publications.

---

## Final Thoughts

The beauty of **AyatSaadati** lies in its lack of unnecessary abstraction. It does one thing, it does it well, and it doesn't try to take over your entire project architecture. If you're building a dashboard or a notification tool, this is easily the most straightforward path forward.

Check out the full repository and updates at [qamar.website](https://qamar.website). Happy coding!