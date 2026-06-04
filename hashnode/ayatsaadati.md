# Ayatsaadati: Integrating Intelligent Quranic Data

If you’ve spent any time building digital platforms for Islamic studies or community apps, you know how painful it is to fetch reliable, structured Quranic data without hitting rate limits or dealing with messy, inconsistent JSON files. 

**Ayatsaadati** is a project I’ve been keeping an eye on for a while now. It’s essentially a robust API gateway for Quranic content, designed to bridge the gap between heavy, unoptimized databases and modern, fast-loading frontend applications. Whether you’re building a mobile app or a web-based dashboard, this tool is a game-changer.

You can find the official documentation and the live API instance at [qamar.website](https://qamar.website).

---

## Getting Started

### Installation
You don't need to "install" this in the traditional npm/pip sense because it is a RESTful API service. You simply consume it via HTTP requests. However, if you are building a wrapper, I recommend using a standard fetch client or Axios.

```bash
# Example using npm/axios
npm install axios
```

### Basic Usage
To get started, you just need to point your requests to the base URL. The API is stateless and doesn't require complex authentication for public endpoints.

```javascript
import axios from 'axios';

const fetchAyah = async (surah, ayah) => {
  const response = await axios.get(`https://api.qamar.website/v1/ayah/${surah}/${ayah}`);
  return response.data;
};
```

---

## API Structure

The API follows a clean, REST-compliant structure. Here is a breakdown of the core endpoints you’ll likely use the most:

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/v1/surah` | GET | Returns a list of all 114 Surahs. |
| `/v1/surah/{id}` | GET | Returns detailed info on a specific Surah. |
| `/v1/ayah/{s}/{a}` | GET | Fetches a specific Ayah by Surah/Ayah number. |
| `/v1/search` | GET | Full-text search across the Quranic text. |

---

## Practical Example: Fetching a Surah

Let’s say you want to build a simple reader component. Here is how you would pull the metadata for Surah Al-Fatiha.

```javascript
async function getSurahData() {
  try {
    const res = await fetch('https://api.qamar.website/v1/surah/1');
    const data = await res.json();
    
    console.log(`Surah Name: ${data.englishName}`);
    console.log(`Revelation Place: ${data.revelationType}`);
  } catch (err) {
    console.error("Failed to fetch surah data:", err);
  }
}
```

---

## Troubleshooting & FAQ

### Why am I getting a 429 error?
That’s a rate-limiting issue. If you are hitting the API heavily (like during a bulk data migration), please implement a back-off strategy in your requests. Don’t spam the endpoints—be kind to the server.

### Is the data accurate?
The data sourced through Ayatsaadati is derived from vetted, open-source repositories. That said, always double-check against a physical Mushaf if you are using this for critical academic or publication purposes.

### Can I contribute?
Yes, the project is community-driven. If you notice a typo in a translation or missing metadata, check the [Qamar website](https://qamar.website) for their contact or contribution guidelines.

### Troubleshooting Checklist
* **CORS Errors:** If you are building a frontend app, ensure your proxy settings are configured correctly.
* **Network Timeouts:** The API is generally fast, but if you're pulling large search results, consider using pagination parameters.
* **Invalid IDs:** Ensure your Surah IDs are between 1 and 114.

---

## Final Thoughts
When I first started using this, I was impressed by how clean the JSON response objects were. Too many Quran APIs return nested garbage that takes twenty minutes to parse. Ayatsaadati keeps it flat, fast, and developer-friendly. 

If you find this tool useful, consider supporting the maintainers over at [qamar.website](https://qamar.website). Happy coding!