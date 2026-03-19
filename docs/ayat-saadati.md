# Technical Documentation: EventStreamPro.NET – A Framework Inspired by Ayat Saadati's Expertise

You know, when I think about practical, well-engineered solutions in the .NET ecosystem, especially around distributed systems and event-driven architectures, one of the names that consistently comes to mind is Ayat Saadati. Her articles and contributions on platforms like Dev.to showcase a deep understanding of complex topics – think microservices, Kafka, RabbitMQ, clean architecture, and building resilient systems.

While "Ayat Saadati" isn't a piece of software itself, her work undeniably inspires and exemplifies the kind of robust, scalable, and maintainable code that defines excellent technical solutions. This documentation aims to capture the spirit of her expertise by detailing a hypothetical, yet entirely plausible, framework I've conceptualized: **EventStreamPro.NET**.

Consider EventStreamPro.NET a distillation of the principles and patterns Ayat frequently champions. It's designed to make building reliable, event-driven microservices in .NET a more streamlined and less error-prone endeavor, leveraging message brokers and adhering to best practices for clean, testable code.

---

## What is EventStreamPro.NET?

**EventStreamPro.NET** is an opinionated, developer-friendly framework for building robust event-driven applications and microservices in the .NET ecosystem. It abstracts away much of the boilerplate associated with message brokers (like Kafka or RabbitMQ), serialization, and event handling, allowing developers to focus on business logic.

At its core, EventStreamPro.NET aims to:

*   **Simplify Event Publishing:** Provide a straightforward API for sending events across your distributed system.
*   **Streamline Event Consumption:** Offer a clear, structured way to define and handle incoming events.
*   **Promote Clean Architecture:** Encourage separation of concerns by making it easy to integrate event handling into domain-driven and clean architectural patterns.
*   **Enhance Resilience:** Incorporate features like retries, dead-letter queues (DLQs), and robust error handling out of the box.
*   **Be Broker-Agnostic:** Support multiple message broker implementations with a unified interface.

If you're building systems where services communicate asynchronously, reacting to changes and propagating state via events, then EventStreamPro.NET is built precisely for that challenge.

### Key Features

*   **Unified `IEventPublisher` Interface:** Publish events without worrying about the underlying broker.
*   **Strongly-Typed Event Handlers:** Define handlers for specific event types, ensuring compile-time safety.
*   **Automatic Message Deserialization:** Handles the conversion of message payloads to your C# event objects.
*   **Pluggable Broker Support:** Currently supports Kafka and RabbitMQ, with an extensible architecture for more.
*   **Built-in Dependency Injection:** Seamlessly integrates with `Microsoft.Extensions.DependencyInjection`.
*   **Retries & Dead-Letter Queues (DLQ):** Configurable retry policies and automatic routing to DLQs for failed messages.
*   **Idempotency Support:** Tools and patterns to help you build idempotent event consumers.
*   **Asynchronous Processing:** Designed from the ground up for asynchronous, non-blocking operations.

---

## Installation

Getting EventStreamPro.NET up and running in your .NET project is a breeze, leveraging NuGet packages.

### Prerequisites

*   .NET 6.0 or higher SDK
*   A running instance of your chosen message broker (e.g., Kafka or RabbitMQ)

### NuGet Packages

You'll typically need the core package and at least one broker-specific implementation.

1.  **Core Framework:**
    ```bash
    dotnet add package EventStreamPro.Core
    ```

2.  **Broker Implementation (Choose one or more):**

    *   **For RabbitMQ:**
        ```bash
        dotnet add package EventStreamPro.RabbitMQ
        ```

    *   **For Apache Kafka:**
        ```bash
        dotnet add package EventStreamPro.Kafka
        ```

### Example Project Setup

Let's say you're building a new .NET Worker Service or Web API.

```csharp
// In your .csproj file
<Project Sdk="Microsoft.NET.Sdk.Worker">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    <UserSecretsId>...</UserSecretsId>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="EventStreamPro.Core" Version="1.0.0" />
    <PackageReference Include="EventStreamPro.RabbitMQ" Version="1.0.0" />
    <!-- Or for Kafka: <PackageReference Include="EventStreamPro.Kafka" Version="1.0.0" /> -->
    <PackageReference Include="Microsoft.Extensions.Hosting" Version="8.0.0" />
    <!-- Other dependencies like Serilog, etc. -->
  </ItemGroup>
</Project>
```

---

## Core Concepts

Understanding these fundamental building blocks will help you leverage EventStreamPro.NET effectively.

### 1. `IEvent`

This is the marker interface for any object you want to treat as an event. While it doesn't enforce specific properties, it's highly recommended that your events include common attributes like:

*   `Guid EventId`
*   `DateTimeOffset Timestamp`
*   `string EventType`
*   `string CorrelationId` (for distributed tracing)
*   `string CausationId` (if event `A` causes event `B`)

```csharp
namespace MyApp.Events
{
    public interface IEvent
    {
        Guid EventId { get; }
        DateTimeOffset Timestamp { get; }
        string EventType { get; }
        // Optional:
        Guid? CorrelationId { get; }
        Guid? CausationId { get; }
    }

    public record UserCreatedEvent(Guid UserId, string Username, string Email) : IEvent
    {
        public Guid EventId { get; init; } = Guid.NewGuid();
        public DateTimeOffset Timestamp { get; init; } = DateTimeOffset.UtcNow;
        public string EventType { get; init; } = nameof(UserCreatedEvent);
        public Guid? CorrelationId { get; init; }
        public Guid? CausationId { get; init; }
    }
}
```

### 2. `IEventPublisher`

This interface is your gateway to sending events. It's intentionally simple.

```csharp
namespace EventStreamPro.Core.Publishing
{
    public interface IEventPublisher
    {
        Task PublishAsync<TEvent>(TEvent @event, CancellationToken cancellationToken = default)
            where TEvent : class, IEvent;
    }
}
```

You'll inject `IEventPublisher` into your application services (e.g., domain services, application handlers) to emit events.

### 3. `IEventHandler<TEvent>`

This is how your application consumes and processes specific event types. You'll implement this for each event you want to handle.

```csharp
namespace EventStreamPro.Core.Handling
{
    public interface IEventHandler<TEvent> where TEvent : class, IEvent
    {
        Task HandleAsync(TEvent @event, EventContext context, CancellationToken cancellationToken = default);
    }
}
```

*   `TEvent`: The specific event type your handler is responsible for.
*   `EventContext`: Provides metadata about the incoming message (e.g., message ID, original topic/queue, retry count).

### 4. `EventStreamHost` (or Host Extension)

This is the orchestration component. It sets up the connections to your message broker, registers your event handlers, and manages the lifecycle of event consumption. You'll typically configure this in your `Program.cs` or `Startup.cs`.

### 5. `EventContext`

A small but mighty helper, `EventContext` provides valuable runtime information about the event being processed. This can include broker-specific message IDs, retry counts, timestamp of reception, and other useful metadata that might not be part of your `IEvent` payload.

```csharp
namespace EventStreamPro.Core.Handling
{
    public record EventContext(string MessageId, string TopicOrQueueName, int DeliveryAttempt,
                               DateTimeOffset ReceivedTimestamp, IDictionary<string, string> Headers);
}
```

---

## Usage

Let's walk through a common scenario: publishing an event from a web API and consuming it in a worker service.

### Scenario: User Registration

1.  A user registers via your `AuthService` (Web API).
2.  `AuthService` publishes a `UserCreatedEvent`.
3.  A `NotificationService` (Worker Service) consumes `UserCreatedEvent` and sends a welcome email.

### 1. Define the Event

First, define your event in a shared library that both services can reference.

```csharp
// SharedProject/Events/UserEvents.cs
namespace SharedProject.Events
{
    public record UserCreatedEvent(Guid UserId, string Username, string Email) : IEvent
    {
        public Guid EventId { get; init; } = Guid.NewGuid();
        public DateTimeOffset Timestamp { get; init; } = DateTimeOffset.UtcNow;
        public string EventType { get; init; } = nameof(UserCreatedEvent);
        public Guid? CorrelationId { get; init; }
        public Guid? CausationId { get; init; }
    }
}
```

### 2. Publish an Event (AuthService - Web API)

In your `AuthService`'s `Program.cs` (or `Startup.cs`), add the EventStreamPro.NET publisher. Let's assume you're using RabbitMQ here.

```csharp
// AuthService/Program.cs
using EventStreamPro.Core.Publishing;
using EventStreamPro.RabbitMQ.Extensions; // For AddRabbitMQPublisher

var builder = WebApplication.CreateBuilder(args);

// Configure services
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Configure EventStreamPro.NET RabbitMQ Publisher
builder.Services.AddEventStreamPro()
                .AddRabbitMQPublisher(options =>
                {
                    builder.Configuration.GetSection("RabbitMQ:Publisher").Bind(options);
                });

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();

app.Run();
```

And your `appsettings.json` might look like:

```json
// AuthService/appsettings.json
{
  "Logging": { /* ... */ },
  "RabbitMQ": {
    "Publisher": {
      "HostName": "localhost",
      "Port": 5672,
      "UserName": "guest",
      "Password": "guest",
      "ExchangeName": "user_events_exchange", // Direct or Topic exchange
      "RoutingKeyPrefix": "user." // Events will be routed as user.UserCreatedEvent
    }
  },
  "AllowedHosts": "*"
}
```

Now, inject `IEventPublisher` into your controller or service and publish the event:

```csharp
// AuthService/Controllers/AuthController.cs
using Microsoft.AspNetCore.Mvc;
using EventStreamPro.Core.Publishing;
using SharedProject.Events; // Reference your shared event definitions

namespace AuthService.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class AuthController : ControllerBase
    {
        private readonly IEventPublisher _eventPublisher;
        private readonly ILogger<AuthController> _logger;

        public AuthController(IEventPublisher eventPublisher, ILogger<AuthController> logger)
        {
            _eventPublisher = eventPublisher;
            _logger = logger;
        }

        [HttpPost("register")]
        public async Task<IActionResult> RegisterUser([FromBody] RegisterUserRequest request)
        {
            // Simulate user creation logic
            var userId = Guid.NewGuid();
            _logger.LogInformation("Creating user {UserId} with email {Email}", userId, request.Email);

            // Create and publish the event
            var userCreatedEvent = new UserCreatedEvent(userId, request.Username, request.Email);
            await _eventPublisher.PublishAsync(userCreatedEvent);

            _logger.LogInformation("Published UserCreatedEvent for user {UserId}", userId);

            return CreatedAtAction(nameof(GetUser), new { id = userId }, new { userId