# Saadat Connect: An Opinionated API Gateway & BFF Framework

Alright, let's talk about building robust, developer-friendly API layers. Over the years, I've seen countless teams wrestle with the complexities of managing API gateways, especially when dealing with a sprawling microservices landscape or simply trying to provide a tailored experience for different client applications. That's precisely why I started to formalize a set of patterns and tools that eventually coalesced into **Saadat Connect**.

At its heart, Saadat Connect is a lightweight, opinionated framework designed to simplify the creation of API gateways and Backend-for-Frontend (BFF) services. My primary goal here was to bake in best practices for observability, security, and maintainability right from the start, all while keeping the developer experience (DX) front and center. Because let's be honest, if it's not a joy to use, it won't get used properly.

## 🚀 Core Philosophy & Why It Matters

You might be thinking, "Another API gateway framework? Really?" And that's a fair question. The truth is, while there are many excellent tools out there, many are either overly complex for typical use cases, or they leave too much boilerplate for the developer to figure out. Saadat Connect aims to strike a balance.

My philosophy with Saadat Connect boils down to a few key principles:

1.  **Opinionated Defaults for Best Practices:** I've baked in sensible defaults for things like request logging, error handling, and security headers. You can override them, of course, but the idea is to guide you towards a secure and observable API without endless configuration.
2.  **Focus on Developer Experience (DX):** Configuration should be intuitive, and development loops should be fast. I want you to spend more time building features and less time fighting the framework.
3.  **Extensible & Modular:** While opinionated, it's not a black box. You can easily plug in your own middleware, integrate with various service discovery mechanisms, and extend its functionality to fit your specific needs.
4.  **Performance & Reliability:** Built on battle-tested HTTP server foundations, Saadat Connect is designed to be performant and resilient, handling high loads with grace. We're not reinventing the wheel on the networking side; we're just making it easier to drive.
5.  **Observability First:** Good APIs aren't just about functionality; they're about understanding what's happening under the hood. Saadat Connect provides built-in mechanisms for logging, tracing, and metrics, making it easier to debug and monitor your services.

## 📦 Installation

Getting Saadat Connect up and running is pretty straightforward. We're primarily targeting Node.js environments, but there's also a Docker option for quick deployment.

### Prerequisites

Before you start, make sure you have:

*   **Node.js (v16.x or later):** Saadat Connect is built with modern JavaScript features in mind.
*   **npm or yarn:** For package management.
*   **Docker (Optional):** If you prefer containerized deployments.

### Installing with npm/yarn

The easiest way to get started is to create a new project and add `saadat-connect` as a dependency.

1.  **Create a new project directory:**

    ```bash
    mkdir my-saadat-gateway
    cd my-saadat-gateway
    ```

2.  **Initialize your project:**

    ```bash
    npm init -y
    # or
    yarn init -y
    ```

3.  **Install Saadat Connect:**

    ```bash
    npm install saadat-connect
    # or
    yarn add saadat-connect
    ```

### Setting up a new Saadat Connect Project

Once installed, you can use the `saadat` CLI to scaffold a basic project structure. This gives you a great starting point with sensible defaults.

```bash
npx saadat init # or yarn saadat init
```

This command will create a basic `src/` directory, an `index.js` entry point, and a `config.js` file, pre-configured with a simple gateway setup.

### Docker Deployment (Experimental)

For those who prefer containerization from the get-go, we provide a base Docker image.

1.  **Create your `gateway.js` (or `index.js`) file:** Define your gateway logic as you would normally.
2.  **Create a `Dockerfile`:**

    ```dockerfile
    # Use a lightweight Node.js base image
    FROM node:18-alpine

    WORKDIR /app

    # Copy package.json and package-lock.json first to leverage Docker cache
    COPY package*.json ./

    # Install dependencies
    RUN npm install --production

    # Copy your application code
    COPY . .

    # Expose the port your gateway listens on (default 3000)
    EXPOSE 3000

    # Command to run your gateway
    CMD ["node", "index.js"]
    ```

3.  **Build and run your Docker image:**

    ```bash
    docker build -t my-saadat-gateway .
    docker run -p 80:3000 my-saadat-gateway
    ```

## 🛠️ Usage

Let's dive into how you actually define your gateway logic with Saadat Connect.

### Defining Your Gateway

The core of Saadat Connect revolves around a central `Gateway` instance where you register your routes and middleware.

Here's a minimal example (`index.js`):

```javascript
const { Gateway } = require('saadat-connect');
const config = require('./config'); // Assuming you have a config file

async function startGateway() {
  const gateway = new Gateway(config);

  // Define a simple proxy route
  gateway.route('/users/:id')
    .get('http://user-service:8080/api/users/:id')
    .post('http://user-service:8080/api/users')
    .put('http://user-service:8080/api/users/:id');

  // Define a route that aggregates data or transforms
  gateway.route('/dashboard/:userId')
    .get(async (req, res) => {
      try {
        // Example: Fetch data from multiple services
        const userData = await fetch(`http://user-service:8080/api/users/${req.params.userId}`).then(r => r.json());
        const ordersData = await fetch(`http://order-service:8081/api/orders/user/${req.params.userId}`).then(r => r.json());

        res.json({
          user: userData,
          recentOrders: ordersData.slice(0, 5) // Just take the latest 5 orders
        });
      } catch (error) {
        console.error('Dashboard aggregation failed:', error.message);
        res.status(500).json({ error: 'Failed to retrieve dashboard data' });
      }
    });

  // Start the gateway server
  await gateway.start();
  console.log(`Saadat Connect Gateway running on port ${config.port}`);
}

startGateway().catch(console.error);
```

### Configuration

Your `config.js` file will typically hold settings for the server, logging, and potentially upstream service details.

```javascript
// config.js
module.exports = {
  port: process.env.PORT || 3000,
  logLevel: process.env.LOG_LEVEL || 'info',
  // You can define upstream service base URLs here for easier management
  services: {
    userService: 'http://localhost:8080',
    orderService: 'http://localhost:8081'
  },
  // Global middleware configuration
  middleware: {
    // Example: Rate limiting
    rateLimit: {
      windowMs: 15 * 60 * 1000, // 15 minutes
      max: 100 // limit each IP to 100 requests per windowMs
    },
    // CORS settings
    cors: {
      origin: '*', // Be specific in production!
      methods: ['GET', 'POST', 'PUT', 'DELETE'],
      allowedHeaders: ['Content-Type', 'Authorization']
    }
  }
};
```

### Middleware: The Real Powerhouse

This is where Saadat Connect really shines. You can apply middleware globally, to specific routes, or even to specific HTTP methods on a route. Middleware can handle authentication, logging, rate limiting, data transformation, and much more.

```javascript
const { Gateway, Middleware } = require('saadat-connect');
const config = require('./config');
const jwt = require('jsonwebtoken'); // Example for authentication

// Custom authentication middleware
const authenticate = (req, res, next) => {
  const authHeader = req.headers.authorization;
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ message: 'Authentication required' });
  }

  const token = authHeader.split(' ')[1];
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET || 'supersecretkey');
    req.user = decoded; // Attach user info to request
    next();
  } catch (err) {
    return res.status(403).json({ message: 'Invalid or expired token' });
  }
};

async function startGateway() {
  const gateway = new Gateway(config);

  // Apply a global rate limit middleware (if configured)
  gateway.use(Middleware.rateLimit(config.middleware.rateLimit));
  // Apply global CORS settings
  gateway.use(Middleware.cors(config.middleware.cors));
  // Apply global request logging
  gateway.use(Middleware.requestLogger());

  // A public route
  gateway.route('/health')
    .get((req, res) => res.status(200).send('OK'));

  // A protected route
  gateway.route('/profile')
    .use(authenticate) // Apply authentication only to this route
    .get('http://user-service:8080/api/profile');

  // Another protected route, but with specific permissions check
  gateway.route('/admin/users')
    .use(authenticate)
    .use((req, res, next) => { // Custom authorization middleware
      if (req.user && req.user.roles.includes('admin')) {
        next();
      } else {
        res.status(403).json({ message: 'Admin access required' });
      }
    })
    .get('http://user-service:8080/api/admin/users');

  await gateway.start();
  console.log(`Saadat Connect Gateway running on port ${config.port}`);
}

startGateway().catch(console.error);
```

### Error Handling

Saadat Connect comes with sensible default error handling, but you can also define custom error handling middleware. Any `next(error)` call in your middleware chain will be caught by the error handler.

```javascript
// In your gateway setup
gateway.use((err, req, res, next) => {
  console.error('Caught error:', err.message, err.stack);
  if (res.headersSent) {
    return next(err); // Delegate to default Express error handler if headers already sent
  }
  res.status(err.statusCode || 500).json({
    error: {
      message: err.message || 'An unexpected error occurred.',
      code: err.code || 'INTERNAL_SERVER_ERROR'
    }
  });
});
```

## 📖 Configuration Reference

Saadat Connect's configuration is designed to be flexible yet straightforward. Here's a table of common configuration options you'll find in your `config.js` or `process.env`.

| Option             | Type     | Default         | Description                                                                                             |
| :----------------- | :------- | :-------------- | :------------------------------------------------------------------------------------------------------ |
| `port`             | `number` | `3000`          | The port on which the gateway server will listen.                                                       |
| `logLevel`         | `string` | `'info'`        | Minimum log level for console output (`debug`, `info`, `warn`, `error`).                              |
| `env`              | `string` | `'development'` | Environment mode (`development`, `production`, `test`). Affects error detail verbosity.                 |
| `jsonBodyLimit`    | `string` | `'100kb'`       | Maximum request body size for JSON payloads.                                                            |
| `urlEncodedLimit`  | `string` | `'100kb'`       | Maximum request body size for URL-encoded payloads.                                                     |
| `middleware.cors`  | `object` | `{}`            | CORS configuration options (e.g., `origin`, `methods`, `allowedHeaders`). Passed directly to `cors` lib. |
| `middleware.rateLimit` | `object` | `{}`        | Rate limiting options (e.g., `windowMs`, `max`). Passed directly to `express-rate-limit` lib.         |
| `errorHandling`    | `object` | `{}`            | Custom error handling settings. E.g., `showStackTrace: false` in production.                            |
| `services`         | `object` | `{}`            | A map of service names to their base URLs, useful for cleaner route definitions.                        |

## ❓ FAQ

### Why should I use Saadat Connect over other API gateways like Nginx, Kong, or even a custom Express server?

Great question! Saadat Connect isn't trying to replace a full-blown enterprise-grade gateway like Kong or Apache APISIX, especially if you need advanced features like protocol translation, caching across heterogeneous systems, or deep analytics out-of-the-box.

Where Saadat Connect shines is when you need a **lightweight, code-first, developer-centric gateway or BFF layer** that's easily integrated into your existing Node