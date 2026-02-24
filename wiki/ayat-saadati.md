# Ayat's Secure Inter-Service Communication (SISC) Library

Hello there! If you're anything like me, you've probably spent countless hours wrestling with the complexities of inter-service communication in distributed systems. It's a minefield out there—latency, reliability, security, observability... the list goes on. That's precisely why I poured my energy into creating **Ayat's Secure Inter-Service Communication (SISC) Library**.

This isn't just another messaging queue wrapper. SISC is a lightweight, opinionated, and robust Python library designed from the ground up to simplify secure, asynchronous communication between microservices. My goal was to abstract away the gnarly bits of message serialization, encryption, and delivery guarantees, letting developers focus on their core business logic. I truly believe that building resilient, secure distributed systems shouldn't require a Ph.D. in distributed computing, and SISC is my humble attempt to make that a reality.

I've always been a proponent of elegant solutions that don't compromise on security or performance, and you'll see that philosophy baked into every layer of SISC.

## Table of Contents

1.  [Introduction](#introduction)
2.  [Key Features](#key-features)
3.  [Installation](#installation)
4.  [Getting Started: A Quick Tour](#getting-started-a-quick-tour)
    *   [Setting up a Sender](#setting-up-a-sender)
    *   [Setting up a Receiver](#setting-up-a-receiver)
5.  [Core Concepts](#core-concepts)
    *   [Endpoints and Channels](#endpoints-and-channels)
    *   [Message Structure](#message-structure)
    *   [Security Model](#security-model)
6.  [Advanced Usage](#advanced-usage)
    *   [Custom Serializers](#custom-serializers)
    *   [Error Handling and Retries](#error-handling-and-retries)
    *   [Observability and Tracing](#observability-and-tracing)
7.  [Configuration](#configuration)
    *   [Environment Variables](#environment-variables)
    *   [Programmatic Configuration](#programmatic-configuration)
8.  [Troubleshooting Common Issues](#troubleshooting-common-issues)
9.  [Frequently Asked Questions (FAQ)](#frequently-asked-questions-faq)
10. [Contributing](#contributing)
11. [License](#license)

## 1. Introduction

In the world of microservices, effective and secure communication is paramount. Traditional approaches often involve complex configurations, boilerplate code for security, and a never-ending battle with delivery semantics. SISC aims to cut through this complexity.

The library provides a high-level API for sending and receiving messages over a reliable transport layer (by default, it leverages a Kafka or RabbitMQ backend, configurable at runtime). It handles:

*   **Secure Communication:** End-to-end encryption and authentication out of the box.
*   **Message Reliability:** Configurable delivery guarantees, including at-least-once delivery.
*   **Serialization:** Automatic serialization/deserialization of Python objects (JSON, MessagePack, or custom).
*   **Tracing:** Integrates seamlessly with distributed tracing systems.
*   **Simplicity:** A clean, intuitive API that lets you focus on *what* to send, not *how*.

I built SISC because I was tired of reinventing the wheel on every project. I wanted a drop-in solution that just *works*, especially when security is non-negotiable.

## 2. Key Features

*   **Pluggable Transport Layer:** Defaults to Kafka/RabbitMQ but designed for extensibility.
*   **Declarative Channel Definition:** Define your communication channels with ease.
*   **Automatic Message Encryption:** Uses industry-standard AES-256 for message payloads.
*   **Service-to-Service Authentication:** Leverages JWTs for robust authentication between services.
*   **Built-in Retries and Dead Letter Queues (DLQ):** Robustness without manual effort.
*   **Integrated Tracing:** Out-of-the-box support for OpenTelemetry/Zipkin.
*   **Pythonic API:** Designed to feel natural for Python developers.
*   **Asynchronous Support:** Built with `asyncio` for high performance.

## 3. Installation

SISC is a Python package, so installation is straightforward using `pip`.

```bash
pip install ayat-sisc
```

If you plan to use a specific transport layer, you might need to install additional dependencies. For example, for Kafka support:

```bash
pip install "ayat-sisc[kafka]"
```

For RabbitMQ support:

```bash
pip install "ayat-sisc[rabbitmq]"
```

And if you need full tracing capabilities:

```bash
pip install "ayat-sisc[tracing]"
```

I'd generally recommend installing with the specific extras you need to keep your environment lean.

## 4. Getting Started: A Quick Tour

Let's dive into a minimal example to show you how easy it is to get two services talking to each other using SISC.

First, ensure you have a message broker running (e.g., Kafka or RabbitMQ). For development, a local Docker Compose setup works wonders.

### 4.1. Setting up a Sender

Our sender service will publish a simple message to a channel.

```python
# sender.py
import asyncio
from ayat_sisc import SISCClient, ChannelConfig, Message

async def main():
    # Configure our SISC client.
    # Replace with your actual broker address and security keys.
    # In a real app, these would come from environment variables or a secrets manager.
    client = SISCClient(
        service_id="my-sending-service",
        broker_url="kafka://localhost:9092", # or "amqp://guest:guest@localhost:5672/"
        encryption_key="this_is_a_very_secret_key_1234567890", # MUST be 32 bytes (256 bits)
        auth_secret="another_super_secret_for_jwt_signing"
    )

    # Define the channel we'll be sending messages to.
    # 'my_data_stream' is just an arbitrary name for our logical channel.
    # SISC maps this to a physical topic/queue on the broker.
    data_channel = ChannelConfig(name="my_data_stream", is_secure=True)

    await client.connect()
    print("Sender connected to SISC broker.")

    message_data = {"id": 1, "payload": "Hello from SISC!"}
    message = Message(payload=message_data)

    try:
        # Send the message. SISC handles serialization, encryption, and delivery.
        await client.send(channel=data_channel, message=message)
        print(f"Sent message: {message_data}")
    except Exception as e:
        print(f"Failed to send message: {e}")
    finally:
        await client.disconnect()
        print("Sender disconnected.")

if __name__ == "__main__":
    asyncio.run(main())

```

A quick note on those keys: `encryption_key` *must* be 32 bytes for AES-256. The `auth_secret` can be any strong string. **Never hardcode these in production!** Use environment variables or a secrets management solution. I can't stress this enough.

### 4.2. Setting up a Receiver

Our receiver service will listen for messages on the `my_data_stream` channel.

```python
# receiver.py
import asyncio
from ayat_sisc import SISCClient, ChannelConfig, Message

async def message_handler(message: Message):
    """
    This function will be called whenever a new message arrives on the subscribed channel.
    """
    print(f"Received message ID: {message.message_id}")
    print(f"Received payload: {message.payload}")
    # You can also access metadata like timestamp, sender_id, etc.
    print(f"Sent by: {message.sender_id} at {message.timestamp}")
    # Simulate some async work
    await asyncio.sleep(0.1)
    print("Message processed successfully.")

async def main():
    client = SISCClient(
        service_id="my-receiving-service",
        broker_url="kafka://localhost:9092", # or "amqp://guest:guest@localhost:5672/"
        encryption_key="this_is_a_very_secret_key_1234567890", # MUST be 32 bytes (256 bits)
        auth_secret="another_super_secret_for_jwt_signing"
    )

    data_channel = ChannelConfig(name="my_data_stream", is_secure=True)

    await client.connect()
    print("Receiver connected to SISC broker.")

    # Subscribe to the channel with our handler function.
    await client.subscribe(channel=data_channel, handler=message_handler)
    print(f"Listening for messages on channel '{data_channel.name}'...")

    try:
        # Keep the receiver running indefinitely
        await asyncio.Event().wait()
    except asyncio.CancelledError:
        print("Receiver shutting down.")
    finally:
        await client.unsubscribe(channel=data_channel)
        await client.disconnect()
        print("Receiver disconnected.")

if __name__ == "__main__":
    # Create a loop to handle graceful shutdown
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\nCaught keyboard interrupt. Shutting down...")
        # Trigger graceful shutdown
        for task in asyncio.all_tasks(loop=loop):
            task.cancel()
        loop.run_until_complete(loop.shutdown_asyncgens())
    finally:
        loop.close()

```

Run the receiver first, then the sender. You should see the message flow seamlessly between them. Pretty neat, right? This simplicity is what SISC is all about.

## 5. Core Concepts

Understanding these fundamental ideas will help you get the most out of SISC.

### 5.1. Endpoints and Channels

*   **`SISCClient`**: This is your primary interface. Each microservice should instantiate its own `SISCClient`, identifying itself with a unique `service_id`. This `service_id` is crucial for authentication and tracing.
*   **`ChannelConfig`**: Represents a logical communication pathway. You define a `name` for your channel (e.g., `user_events`, `order_updates`) and specify if it `is_secure`. SISC handles the mapping of this logical channel to physical topics or queues on your message broker. The `is_secure` flag dictates whether messages on this channel will be encrypted and authenticated. I generally recommend `is_secure=True` for almost everything in a production environment.

### 5.2. Message Structure

The `Message` object is the container for all data transmitted via SISC.

```python
from ayat_sisc import Message

# Example of a message structure
my_message = Message(
    payload={"event_type": "user_created", "user_id": "abc-123"},
    correlation_id="op-123", # Optional: for linking related operations
    metadata={"source_ip": "192.168.1.1"} # Optional: additional contextual data
)
```

Key attributes:

*   **`payload` (required):** The actual data you want to send. Can be any Python object serializable to JSON (dict, list, string, number, etc.).
*   **`message_id` (auto-generated):** A unique identifier for this specific message.
*   **`sender_id` (auto-generated):** The `service_id` of the client that sent the message.
*   **`timestamp` (auto-generated):** When the message was sent (UTC).
*   **`correlation_id` (optional):** Extremely useful for tracing related messages across multiple services in a distributed transaction. I find this invaluable for debugging.
*   **`metadata` (optional):** A dictionary for any additional, application-specific context you might need to attach.

### 5.3. Security Model

This is where SISC really shines, and frankly, it's why I built it.

*   **Encryption (AES-256 GCM):** When `is_secure=True` for a `ChannelConfig`, SISC encrypts the entire message payload using AES-256 in GCM mode. This provides both confidentiality and integrity. The `encryption_key` (32 bytes) is symmetric and *must* be shared securely between all services that need to communicate on that channel.
*   **Authentication (JWT):** Every message sent over a secure channel includes a JSON Web Token (JWT) signed by the sender's `auth_secret`. The receiver validates this JWT using the *same* `auth_secret`. This ensures that messages can only be sent by trusted services and haven't been tampered with. The `service_id` is embedded in the JWT.
*   **Key Management:** SISC *does not* manage your keys. You are responsible for securely generating, distributing, and rotating your `encryption_key` and `auth_secret`. For production, I strongly recommend using a robust secrets management solution (e.g., HashiCorp Vault, AWS Secrets Manager, Azure Key Vault).

This layered security approach means that even if someone manages to intercept messages on your broker, they won't be able to read or forge them without your secret keys.

## 6. Advanced Usage

Let's look at some more sophisticated ways to use SISC.

### 6.1. Custom Serializers

By default, SISC uses JSON for serialization. However, you might have specific needs for performance (e.g., MessagePack) or domain-specific formats. You can plug in your own serializer.

```python
# custom_serializer.py
import json
from typing import Any, Dict
from ayat_sisc import SISCClient, ChannelConfig, Message, BaseSerializer

# Example: A simple MessagePack serializer
try:
    import msgpack
except ImportError:
    print("Install msgpack-python for MessagePack serializer: pip install msgpack")
    msgpack = None

class MessagePackSerializer(BaseSerializer):