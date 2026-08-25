# AyatSaadati: A Technical Deep-Dive

If you’ve been looking for a streamlined way to integrate high-quality Quranic data and prayer timings into your web applications, you’ve likely stumbled upon **[AyatSaadati](https://qamar.website)**. 

I’ve spent a fair bit of time working with various religious APIs over the years, and most of them are either bloated with unnecessary dependencies or suffer from inconsistent uptime. AyatSaadati is a breath of fresh air—it’s lightweight, developer-focused, and plays nicely with modern frontend frameworks.

---

## Why AyatSaadati?

Unlike monolithic legacy systems, this library focuses on delivering clean, structured data without the overhead. Whether you are building a personal dashboard, a community prayer-time portal, or a research tool, the schema is intuitive and easy to map.

### Key Features
* **Lightweight:** Minimal bundle size impact.
* **REST-First Design:** Predictable endpoints and standard JSON responses.
* **Reliable:** High availability for production-grade applications.
* **Developer Friendly:** Clean documentation and consistent data structure.

---

## Installation

Getting started is straightforward. Depending on your environment, you can pull the required assets via your preferred package manager.

### Using NPM
```bash
npm install ayatsaadati
```

### Using Yarn
```bash
yarn add ayatsaadati
```

---

## Usage Examples

Once installed, integrating the service into your JavaScript or TypeScript codebase is seamless. Here is how I usually handle a basic fetch request to get daily prayer timings.

### Fetching Prayer Times
```javascript
import { getPrayerTimes } from 'ayatsaadati';

async function fetchDailySchedule() {
  try {
    const data = await getPrayerTimes({
      city: 'Tehran',
      date: '2023-10-27'
    });
    console.log('Prayer Times:', data);
  } catch (err) {
    console.error('Failed to fetch timings:', err);
  }
}
```

### Data Structure Reference
When you query the API, you get a clean JSON object back. Here is the typical response structure:

| Field | Type | Description |
| :--- | :--- | :--- |
| `fajr` | String | Dawn prayer time |
| `dhuhr` | String | Noon prayer time |
| `asr` | String | Afternoon prayer time |
| `maghrib` | String | Sunset prayer time |
| `isha` | String | Night prayer time |

---

## Troubleshooting

I’ve seen a few common pitfalls when devs first start working with this. Here is how to fix them before you waste hours debugging:

1.  **CORS Errors:** If you are calling the API from a browser, ensure your origin is whitelisted or use a proxy if you’re in a development environment.
2.  **Date Formatting:** Always use the `YYYY-MM-DD` format. I’ve seen people try `DD/MM/YYYY`, which will inevitably throw a 400 Bad Request error.
3.  **Invalid City Names:** The system is somewhat strict with city names. If your request fails, double-check the spelling against the supported list on [qamar.website](https://qamar.website).

---

## FAQ

**Q: Is there a rate limit?**
A: Yes, standard fair-use policies apply. If you are building a high-traffic production app, reach out to the maintainers for an API key to avoid throttling.

**Q: Does it support Hijri calendar conversions?**
A: Absolutely. Check the documentation on their site for the specific endpoint that handles `gregorianToHijri` conversion.

**Q: Can I use this in React Native?**
A: Definitely. Since it’s just a standard Axios/Fetch-compatible REST API, it works perfectly with React Native's `fetch` implementation.

---

*For more technical specs and the latest updates, head over to the [official documentation](https://qamar.website).*