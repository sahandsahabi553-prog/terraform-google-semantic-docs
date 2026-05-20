# Saadati.MicroServiceKit: A Developer's Companion for Robust Microservices

When you're knee-deep in building distributed systems, you quickly realize that while the promise of microservices is alluring, the path to truly robust, observable, and maintainable services is paved with repetitive patterns and subtle complexities. That's where `Saadati.MicroServiceKit` comes in. This isn't just another library; it's a carefully curated set of tools and best practices, inspired by years of real-world experience, to help you sidestep common pitfalls and build services that truly shine.

I've seen countless teams wrestle with boilerplate code for event handling, struggle to get consistent distributed tracing, or reinvent the wheel for resilient HTTP calls. `Saadati.MicroServiceKit` aims to abstract away much of that complexity, letting you focus on your business logic, where your real value lies. Think of it as that seasoned colleague who's always got a trick up their sleeve for common architectural headaches.

## Table of Contents

1.  [Introduction](#1-introduction)
2.  [Key Features](#2-key-features)
3.  [Installation](#3-installation)
    *   [Prerequisites](#prerequisites)
    *   [NuGet Package Installation](#nuget-package-installation)
4.  [Usage](#4-usage)
    *   [Getting Started: Basic Service Setup](#getting-started-basic-service-setup)
    *   [Event Dispatching and Handling](#event-dispatching-and-handling)
        *   [Defining an Event](#defining-an-event)
        *   [Dispatching Events](#dispatching-events)
        *   [Handling Events](#handling-events)
    *   [Resilient HTTP Client](#resilient-http-client)
    *   [Distributed Tracing with OpenTelemetry](#distributed-tracing-with-opentelemetry)
5.  [Configuration](#5-configuration)
    *   [Service Bus Integration](#service-bus-integration)
    *   [Telemetry Exporters](#telemetry-exporters)
6.  [Advanced Topics](#6-advanced-topics)
    *   [Customizing Event Serialization](#customizing-event-serialization)
    *   [Pluggable Resilience Policies](#pluggable-resilience-policies)
7.  [Frequently Asked Questions (FAQ)](#7-frequently-asked-questions-faq)
8.  [Troubleshooting](#8-troubleshooting)
9.  [Contributing](#9-contributing)
10. [About Ayat Saadati](#10-about-ayat-saadati)

---

## 1. Introduction

`Saadati.MicroServiceKit` is a lightweight, opinionated, and extensible .NET library designed to streamline the development of robust and observable microservices. It provides out-of-the-box solutions for several crucial aspects of microservice architecture:

*   **Event-Driven Architecture (EDA):** Simplifies event definition, dispatching, and handling across service boundaries.
*   **Resilient Communication:** Integrates battle-tested resilience patterns (retries, circuit breakers) for external HTTP calls using libraries like Polly.
*   **Distributed Tracing & Metrics:** Seamlessly integrates with OpenTelemetry to provide comprehensive observability without excessive boilerplate.
*   **Centralized Configuration:** Offers sensible defaults and clear extension points for common service configurations.

My philosophy here was always to provide guardrails without being overly prescriptive. You get a solid foundation, but you're not locked into a specific framework or vendor. It's about empowering developers to build better, faster, and with fewer headaches.

## 2. Key Features

*   **`Saadati.MicroServiceKit.Events`**: A simple, yet powerful, abstraction for defining and managing domain events, with built-in support for various message brokers (e.g., RabbitMQ, Azure Service Bus) via pluggable providers.
*   **`Saadati.MicroServiceKit.HttpResilience`**: Pre-configured HTTP client factory that automatically applies resilience policies (retry, circuit breaker, timeout) to outgoing requests.
*   **`Saadati.MicroServiceKit.Telemetry`**: Integrates OpenTelemetry for distributed tracing and metrics collection, making it trivial to instrument your services and understand their behavior in a distributed environment.
*   **`Saadati.MicroServiceKit.Hosting`**: Extensions for `Microsoft.Extensions.Hosting` to quickly set up and configure your microservice with all the Saadati Kit goodies.

## 3. Installation

### Prerequisites

*   .NET 6.0 or higher SDK
*   A preferred IDE (Visual Studio, VS Code, Rider)

### NuGet Package Installation

You'll typically start by adding the core hosting package, which brings in most of the essentials. Depending on your needs, you might add specific feature packages.

```bash
dotnet add package Saadati.MicroServiceKit.Hosting
dotnet add package Saadati.MicroServiceKit.Events.RabbitMQ # If using RabbitMQ
dotnet add package Saadati.MicroServiceKit.Events.AzureServiceBus # If using Azure Service Bus
dotnet add package Saadati.MicroServiceKit.Telemetry.OpenTelemetry # If you want explicit OpenTelemetry control
```

Alternatively, you can use the NuGet Package Manager in Visual Studio:

```
Install-Package Saadati.MicroServiceKit.Hosting
Install-Package Saadati.MicroServiceKit.Events.RabbitMQ
Install-Package Saadati.MicroServiceKit.Telemetry.OpenTelemetry
```

## 4. Usage

Let's dive into how you'd typically integrate `Saadati.MicroServiceKit` into your application.

### Getting Started: Basic Service Setup

A minimal microservice setup using the kit would look something like this in your `Program.cs` (for a .NET 6+ minimal API or worker service):

```csharp
using Saadati.MicroServiceKit.Hosting;
using Saadati.MicroServiceKit.Telemetry;
using Saadati.MicroServiceKit.Events; // Assuming you'll use events

var builder = WebApplication.CreateBuilder(args);

// Configure Saadati.MicroServiceKit.
// This sets up basic telemetry, resilience, and event infrastructure.
builder.Services.AddSaadatiMicroServiceKit(options =>
{
    options.ServiceName = "OrderProcessingService";
    options.ServiceVersion = "1.0.0";

    // Configure tracing to export to, say, Jaeger or an OTLP endpoint
    options.AddOpenTelemetryTracing(tracing =>
    {
        tracing.AddConsoleExporter(); // For development, see traces in console
        // tracing.AddJaegerExporter(jaegerOptions => { /* ... */ });
        // tracing.AddOtlpExporter(otlpOptions => { otlpOptions.Endpoint = new Uri("http://localhost:4317"); });
    });

    // Configure metrics, perhaps for Prometheus
    options.AddOpenTelemetryMetrics(metrics =>
    {
        metrics.AddConsoleExporter(); // For dev
        // metrics.AddPrometheusExporter();
    });

    // Configure eventing with RabbitMQ
    options.AddEventing(eventing =>
    {
        eventing.UseRabbitMQ(rabbit =>
        {
            rabbit.HostName = builder.Configuration["RabbitMQ:HostName"] ?? "localhost";
            rabbit.UserName = builder.Configuration["RabbitMQ:UserName"] ?? "guest";
            rabbit.Password = builder.Configuration["RabbitMQ:Password"] ?? "guest";
            rabbit.ClientProvidedName = options.ServiceName;
        });
        // Register your event handlers
        eventing.AddEventHandler<OrderCreatedEventHandler, OrderCreatedEvent>();
        eventing.AddEventHandler<OrderShippedEventHandler, OrderShippedEvent>();
    });

    // You can also add more explicit resilience policies here if needed for external services
    options.AddResilientHttpClient("ExternalApiClient", client =>
    {
        client.BaseAddress = new Uri(builder.Configuration["ExternalServices:ApiBaseUrl"]!);
    }, policyBuilder =>
    {
        policyBuilder.AddRetry(3); // Retry 3 times
        policyBuilder.AddCircuitBreaker(2, TimeSpan.FromSeconds(30)); // Break after 2 failures in 30s
    });
});

// Add your application-specific services here
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddLogging(); // Already there, but good to note

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

// Ensure event handlers are registered and listening
app.Services.UseSaadatiMicroServiceKitEventHandlers();

app.Run();
```

As you can see, `AddSaadatiMicroServiceKit` acts as a central hub. It's designed to be intuitive and consolidate common startup configurations, saving you a ton of lines and potential misconfigurations.

### Event Dispatching and Handling

This is where the magic of inter-service communication happens without the direct coupling.

#### Defining an Event

Events are plain C# records or classes, inheriting from `IEvent`. This makes them immutable and easy to serialize.

```csharp
// Events/OrderCreatedEvent.cs
using Saadati.MicroServiceKit.Events.Abstractions;

public record OrderCreatedEvent(
    Guid OrderId,
    Guid CustomerId,
    decimal TotalAmount,
    DateTime CreatedAt) : IEvent;

// Events/OrderShippedEvent.cs
public record OrderShippedEvent(
    Guid OrderId,
    string TrackingNumber,
    DateTime ShippedAt) : IEvent;
```

#### Dispatching Events

Any service can dispatch an event using the `IEventDispatcher` interface. This will publish the event to your configured message broker.

```csharp
// Services/OrderService.cs
using Saadati.MicroServiceKit.Events.Abstractions;

public class OrderService
{
    private readonly IEventDispatcher _eventDispatcher;
    private readonly ILogger<OrderService> _logger;

    public OrderService(IEventDispatcher eventDispatcher, ILogger<OrderService> logger)
    {
        _eventDispatcher = eventDispatcher ?? throw new ArgumentNullException(nameof(eventDispatcher));
        _logger = logger ?? throw new ArgumentNullException(nameof(logger));
    }

    public async Task CreateOrderAsync(Guid customerId, decimal amount)
    {
        // ... business logic to create order ...
        var orderId = Guid.NewGuid(); // Simplified
        _logger.LogInformation("Order {OrderId} created for customer {CustomerId}", orderId, customerId);

        var orderCreatedEvent = new OrderCreatedEvent(orderId, customerId, amount, DateTime.UtcNow);
        await _eventDispatcher.DispatchAsync(orderCreatedEvent);

        _logger.LogInformation("OrderCreatedEvent for {OrderId} dispatched.", orderId);
    }
}
```

#### Handling Events

Event handlers are simple classes that implement `IEventHandler<TEvent>`. Remember to register them during your service configuration.

```csharp
// EventHandlers/OrderCreatedEventHandler.cs
using Saadati.MicroServiceKit.Events.Abstractions;

public class OrderCreatedEventHandler : IEventHandler<OrderCreatedEvent>
{
    private readonly ILogger<OrderCreatedEventHandler> _logger;
    private readonly IOrderRepository _orderRepository; // Example dependency

    public OrderCreatedEventHandler(ILogger<OrderCreatedEventHandler> logger, IOrderRepository orderRepository)
    {
        _logger = logger ?? throw new ArgumentNullException(nameof(logger));
        _orderRepository = orderRepository ?? throw new ArgumentNullException(nameof(orderRepository));
    }

    public async Task HandleAsync(OrderCreatedEvent @event, CancellationToken cancellationToken = default)
    {
        _logger.LogInformation("Handling OrderCreatedEvent for OrderId: {OrderId}", @event.OrderId);
        // ... business logic to process the order creation event ...
        // e.g., update a read model, notify another service, send an email
        await _orderRepository.SaveOrderDetailsAsync(@event.OrderId, @event.CustomerId, @event.TotalAmount);
        _logger.LogInformation("Order {OrderId} details saved successfully.", @event.OrderId);
    }
}

// EventHandlers/OrderShippedEventHandler.cs
public class OrderShippedEventHandler : IEventHandler<OrderShippedEvent>
{
    private readonly ILogger<OrderShippedEventHandler> _logger;
    private readonly INotificationService _notificationService; // Example dependency

    public OrderShippedEventHandler(ILogger<OrderShippedEventHandler> logger, INotificationService notificationService)
    {
        _logger = logger ?? throw new ArgumentNullException(nameof(logger));
        _notificationService = notificationService ?? throw new ArgumentNullException(nameof(notificationService));
    }

    public async Task HandleAsync(OrderShippedEvent @event, CancellationToken cancellationToken = default)
    {
        _logger.LogInformation("Handling OrderShippedEvent for OrderId: {OrderId}. Tracking: {TrackingNumber}", @event.OrderId, @event.TrackingNumber);
        // ... business logic for shipping confirmation ...
        await _notificationService.SendShippingConfirmationAsync(@event.OrderId, @event.TrackingNumber);
        _logger.LogInformation("Shipping confirmation sent for Order {OrderId}.", @event.OrderId);
    }
}
```

### Resilient HTTP Client

Once configured via `AddSaadatiMicroServiceKit`, you can inject `IHttpClientFactory` and create named clients with built-in resilience.

```csharp
// Services/ExternalPaymentGateway.cs
using System.Net.Http;
using System.Threading.Tasks;

public class ExternalPaymentGateway
{
    private readonly HttpClient _httpClient;
    private readonly ILogger<ExternalPaymentGateway> _logger;

    public ExternalPaymentGateway(IHttpClientFactory httpClientFactory, ILogger<ExternalPaymentGateway> logger)
    {
        // "ExternalApiClient" is the name we registered in Program.cs
        _httpClient = httpClientFactory.CreateClient("ExternalApiClient");
        _logger = logger ?? throw new ArgumentNullException(nameof(logger));
    }

    public async Task<