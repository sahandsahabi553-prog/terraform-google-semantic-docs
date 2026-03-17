# SaadatFlow: Streamlining Your Workflows with Elegance

Alright, folks, let's talk about something I've been really passionate about lately, something I've poured a good bit of thought and code into: **SaadatFlow**.

You know how it goes. You're building out a new system, perhaps a data pipeline, an automation script, or even just a sequence of tasks that need to run in a specific order. Suddenly, you're drowning in nested functions, callback hell, or a spaghetti of `if/else` statements trying to manage state and dependencies. It's a mess, and frankly, it's not fun to maintain.

That's where SaadatFlow comes in. I built this library because I genuinely believe that defining and executing workflows shouldn't be a chore. It should be intuitive, readable, and robust. SaadatFlow is a lightweight, opinionated Python library designed to help you construct and orchestrate sequences of tasks with a focus on clarity, simplicity, and elegant error handling. It's born from countless hours wrestling with complex systems and a firm belief that our code should tell a story, not just execute commands.

My goal with SaadatFlow was to create a tool that feels natural to use, allowing developers to focus on *what* needs to be done rather than *how* to manage the flow itself. It's not a heavy-duty distributed orchestration engine – think of it more as your trusty sidekick for local, sequential, or moderately complex task management within a single application or process.

---

## Table of Contents

1.  [Features](#features)
2.  [Installation](#installation)
3.  [Quick Start: Your First Flow](#quick-start-your-first-flow)
4.  [Usage Guide](#usage-guide)
    *   [Defining Tasks](#defining-tasks)
    *   [Building Flows](#building-flows)
    *   [Running Flows](#running-flows)
    *   [Passing Data Between Tasks](#passing-data-between-tasks)
    *   [Conditional Execution](#conditional-execution)
    *   [Error Handling and Retries](#error-handling-and-retries)
5.  [Code Examples](#code-examples)
    *   [Simple ETL Pattern](#simple-etl-pattern)
    *   [Web Scraping Workflow](#web-scraping-workflow)
6.  [FAQ](#faq)
7.  [Troubleshooting](#troubleshooting)
8.  [Contributing](#contributing)
9.  [About Ayat Saadat](#about-ayat-saadat)

---

## Features

Here's what SaadatFlow brings to the table:

*   **Declarative Task Definition:** Define your tasks as simple, self-contained units.
*   **Sequential Workflow Orchestration:** Easily chain tasks together to form a logical flow.
*   **Data Passing:** Seamlessly pass outputs from one task as inputs to the next.
*   **Conditional Logic:** Implement branching logic to execute tasks based on previous results.
*   **Robust Error Handling:** Define retry mechanisms and fallback tasks to gracefully handle failures.
*   **Clear Logging:** Get insightful feedback on your workflow's execution.
*   **Lightweight & Minimal Dependencies:** No unnecessary bloat, just the core functionality you need.

---

## Installation

Getting SaadatFlow up and running is as simple as a `pip install`. I've tried to keep the dependencies to a minimum, so you won't be pulling in half the internet.

```bash
pip install saadatflow
```

If you're feeling adventurous and want the latest unreleased features or want to contribute, you can always clone the repository and install it in editable mode:

```bash
git clone https://github.com/ayat-saadat/saadatflow.git
cd saadatflow
pip install -e .
```

I always recommend using a virtual environment, especially for new projects. It keeps your dependencies tidy and prevents conflicts. A quick `python -m venv .venv && source .venv/bin/activate` usually does the trick.

---

## Quick Start: Your First Flow

Let's get our hands dirty with a super simple "Hello, Flow!" example. This will give you a taste of how SaadatFlow works.

```python
from saadatflow import Task, Flow

# 1. Define your tasks
class GreetTask(Task):
    def execute(self, name: str) -> str:
        print(f"Executing GreetTask for {name}...")
        return f"Hello, {name}!"

class ShoutTask(Task):
    def execute(self, message: str) -> str:
        print(f"Executing ShoutTask for '{message}'...")
        return message.upper() + "!!!"

# 2. Build your flow
# The 'depends_on' argument establishes the sequence
my_first_flow = (
    Flow("Greeting Process")
    .add_task("greeting", GreetTask, name="World") # 'name' is passed to GreetTask
    .add_task("shouting", ShoutTask, depends_on="greeting") # 'message' will be output of 'greeting'
)

# 3. Run the flow!
if __name__ == "__main__":
    print("--- Starting My First Flow ---")
    result = my_first_flow.run()
    print(f"--- Flow Finished ---")
    print(f"Final Result: {result}")
```

**What's happening here?**

*   We define two classes, `GreetTask` and `ShoutTask`, both inheriting from `saadatflow.Task`. Each has an `execute` method where your actual logic lives.
*   We create a `Flow` instance, giving it a name ("Greeting Process").
*   We add tasks to the flow using `add_task()`.
    *   The `greeting` task uses `GreetTask` and takes a direct parameter `name="World"`.
    *   The `shouting` task uses `ShoutTask`. Crucially, `depends_on="greeting"` tells SaadatFlow that `shouting` should run *after* `greeting`, and the output of `greeting` will be passed as the primary input (`message`) to `shouting`.
*   Finally, `my_first_flow.run()` kicks everything off. The `result` will be the output of the very last task in the flow (`shouting` in this case).

This pattern, I've found, is incredibly powerful for keeping things modular and readable.

---

## Usage Guide

Let's dive a bit deeper into the core components and how to use them effectively.

### Defining Tasks

A task is the fundamental building block in SaadatFlow. It's a self-contained unit of work.

*   **Inherit from `saadatflow.Task`**: Your task class *must* inherit from this base class.
*   **Implement `execute` method**: This is where your business logic goes. It can accept arguments (which SaadatFlow will try to inject) and should return the result of the task.

```python
from saadatflow import Task

class MyCustomTask(Task):
    """
    A simple task that takes two numbers and adds them.
    """
    def execute(self, num1: int, num2: int) -> int:
        print(f"Adding {num1} and {num2}...")
        return num1 + num2

class DataFetcherTask(Task):
    """
    A task to simulate fetching data from an external source.
    """
    def execute(self, api_endpoint: str) -> dict:
        print(f"Fetching data from {api_endpoint}...")
        # In a real scenario, this would involve network requests
        import time
        time.sleep(0.5) # Simulate network latency
        return {"data": [1, 2, 3], "source": api_endpoint}
```

**Important Note on `execute` Signature:**
SaadatFlow will try its best to match the arguments in your `execute` method to parameters provided during `add_task` or outputs from previous tasks. Type hints are highly recommended!

### Building Flows

Flows are created by chaining tasks together using the `add_task` method.

```python
from saadatflow import Flow

my_flow = (
    Flow("Data Processing Pipeline")
    .add_task("step_one", MyCustomTask, num1=10, num2=20)
    .add_task("step_two", DataFetcherTask, api_endpoint="https://api.example.com/data", depends_on="step_one")
    # 'step_two' doesn't use the output of 'step_one' as its primary input here.
    # It uses a named parameter 'api_endpoint'.
    # We'll see how to pass outputs as primary inputs next.
)
```

**`add_task` Parameters:**

*   `name` (str): A unique identifier for this task within the flow. Crucial for `depends_on`.
*   `task_class` (Type[Task]): The class of the task to be executed.
*   `depends_on` (str or List[str], optional): The name(s) of the task(s) that must complete successfully before this task runs.
*   `*args`, `**kwargs`: Any additional arguments you pass here will be directly forwarded to the `execute` method of your `task_class`.

### Running Flows

Running a flow is straightforward:

```python
if __name__ == "__main__":
    result = my_flow.run()
    print(f"Flow completed with final result: {result}")
```

The `run()` method executes the entire workflow. It returns the output of the *last* task added to the flow.

### Passing Data Between Tasks

This is where SaadatFlow really shines and simplifies things.

*   **Default Behavior:** If a task `B` `depends_on` task `A`, the *output* of task `A` will be passed as the *first positional argument* to task `B`'s `execute` method, unless explicitly overridden by a named parameter.

Let's revisit our quick start example:

```python
class GreetTask(Task):
    def execute(self, name: str) -> str:
        return f"Hello, {name}!"

class ShoutTask(Task):
    def execute(self, message: str) -> str: # 'message' will receive the output of GreetTask
        return message.upper() + "!!!"

my_flow = (
    Flow("Greeting Process")
    .add_task("greeting", GreetTask, name="World")
    .add_task("shouting", ShoutTask, depends_on="greeting") # Output of 'greeting' becomes 'message' for 'shouting'
)
```

If `GreetTask` returned `"Hello, World!"`, then `ShoutTask` would receive `"Hello, World!"` as its `message` argument. Pretty neat, right?

### Conditional Execution

Sometimes you only want to run a task if a previous condition is met. SaadatFlow handles this with a `condition` argument in `add_task`.

The `condition` should be a callable (a function or a lambda) that accepts the output of the `depends_on` task(s) and returns `True` or `False`.

```python
class CheckValueTask(Task):
    def execute(self, value: int) -> bool:
        print(f"Checking if {value} is even...")
        return value % 2 == 0

class EvenNumberTask(Task):
    def execute(self, num: int) -> str:
        print(f"{num} is even!")
        return f"Processed even number: {num}"

class OddNumberTask(Task):
    def execute(self, num: int) -> str:
        print(f"{num} is odd!")
        return f"Processed odd number: {num}"

conditional_flow = (
    Flow("Conditional Branching")
    .add_task("initial_value", Task, value=7) # A simple task to just pass a value
    .add_task("check_parity", CheckValueTask, depends_on="initial_value")
    .add_task(
        "handle_even",
        EvenNumberTask,
        depends_on="initial_value", # Still needs the original value
        condition=lambda is_even: is_even # This lambda checks the output of 'check_parity'
    )
    .add_task(
        "handle_odd",
        OddNumberTask,
        depends_on="initial_value", # Still needs the original value
        condition=lambda is_even: not is_even # This lambda checks the output of 'check_parity'
    )
)

if __name__ == "__main__":
    print("--- Starting Conditional Flow ---")
    result = conditional_flow.run()
    print(f"--- Flow Finished ---")
    print(f"Final Result: {result}")
    # Output will be from 'handle_odd' because 7 is odd.
```

Notice how `handle_even` and `handle_odd` both depend on `initial_value` for their *input*, but their *condition* depends on the output of `check_parity`. This separation of concerns is powerful!

### Error Handling and Retries

Things break. It's a fact of life in software. SaadatFlow gives you tools to handle those inevitable bumps in the road.

*   **`max_retries`**: How many times should a task be retried if it fails?
*   **`retry_delay_seconds`**: How long to wait between retries?
*   **`on_failure`**: The name of another task to execute if *this* task ultimately fails after all retries.

```python
import random

class UnreliableTask(Task):
    def execute(self) -> str:
        if random.random() < 0.7: # 70% chance of failure
            print("UnreliableTask FAILED!")
            raise ValueError("Something went wrong!")
        print("UnreliableTask SUCCEEDED!")
        return "Reliable data!"

class FallbackTask(Task):
    def execute(self, error_message: str) -> str:
        print(f"Executing FallbackTask due to error: {error_message}")
        return "Using fallback data due to failure."

class SuccessLoggerTask(Task):
    def execute(self, data: