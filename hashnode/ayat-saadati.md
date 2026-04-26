# Saadati.InsightKit: Unlocking Developer Wisdom

Navigating the vast ocean of technical knowledge can be daunting, right? We're constantly bombarded with new frameworks, design patterns, and best practices. Sometimes, it feels like you spend more time trying to *find* the right piece of information than actually *using* it. That's a challenge I've personally grappled with for years. You read a fantastic article, jot down a note, and then a few weeks later, you can't quite recall the nuance or the specific implementation detail.

This is precisely the problem `Saadati.InsightKit` aims to solve. Inspired by the meticulous and insightful contributions of developers like Ayat Saadati, whose work on platforms like `dev.to` ([https://dev.to/ayat_saadat](https://dev.to/ayat_saadat)) consistently distills complex topics into actionable knowledge, `Saadati.InsightKit` is a lightweight, extensible framework designed to help you curate, analyze, and synthesize developer insights from various sources.

Think of it as your personal knowledge assistant, helping you turn raw information — whether it's a blog post, a documentation page, or even a chunk of code comments — into structured, retrievable wisdom. It's not just about collecting data; it's about extracting the *essence*, the *insight*, and making it readily available for your next project or learning endeavor.

## Features

`Saadati.InsightKit` isn't a one-trick pony. It's built with flexibility in mind, offering a suite of functionalities to enhance your knowledge workflow:

*   **Intelligent Content Parsing:** Extract key information, code snippets, and structured data from various text formats (Markdown, HTML, plain text).
*   **Insight Graph Generation:** Automatically identify relationships between concepts and generate a navigable graph of interconnected insights.
*   **Customizable Extractors:** Write your own rules and patterns to pull out precisely what you need from specific types of content.
*   **Semantic Tagging:** Auto-suggest and apply relevant tags to your extracted insights, making them easily searchable.
*   **Integrated Storage Backends:** Store your insights in a format that suits you, from simple JSON files to more robust databases like SQLite or even a local vector store.
*   **CLI & API Access:** Whether you prefer command-line power or integrating into your Python applications, `Saadati.InsightKit` has you covered.
*   **Summarization & Q&A (Experimental):** Leveraging local NLP models to provide concise summaries and answer questions based on your curated knowledge base.

## Installation

Getting `Saadati.InsightKit` up and running is straightforward. We recommend using `pip` within a virtual environment to keep your project dependencies tidy.

### Prerequisites

*   Python 3.8+
*   `pip` (Python package installer)

### Basic Installation

First, create and activate a virtual environment:

```bash
# Create a virtual environment
python3 -m venv insightkit-env

# Activate it (on macOS/Linux)
source insightkit-env/bin/activate

# Activate it (on Windows)
insightkit-env\Scripts\activate
```

Now, install `Saadati.InsightKit` using pip:

```bash
pip install saadati-insightkit
```

### Optional Dependencies

Depending on the features you plan to use, you might want to install additional dependencies:

*   **Web Scraping/HTML Parsing:** For processing web pages.
    ```bash
    pip install saadati-insightkit[web]
    ```
*   **Database Integration (SQLite):** For persistent storage of insights.
    ```bash
    pip install saadati-insightkit[db]
    ```
*   **Local NLP (Advanced Summarization/Q&A):** For leveraging local language models.
    *   *Note: This can be resource-intensive and might require additional model downloads.*
    ```bash
    pip install saadati-insightkit[nlp]
    ```

You can also install all optional dependencies at once:

```bash
pip install saadati-insightkit[all]
```

## Usage

`Saadati.InsightKit` offers both a command-line interface (CLI) for quick tasks and a Python API for more programmatic control.

### CLI Usage: Quick Insights

The `ik` command-line tool is your go-to for basic operations.

#### Extracting Insights from a Local File

Let's say you have a Markdown file `my_notes.md`:

```markdown
# My Project Setup Notes

## Frontend Stack
- React 18
- Vite for bundling
- Tailwind CSS for styling

## Backend Stack
- FastAPI for API
- SQLAlchemy for ORM
- PostgreSQL database

### Key Takeaway
Vite is incredibly fast for dev servers. FastAPI's async capabilities are a game-changer for high-performance APIs.
```

You can extract insights from it like this:

```bash
ik extract my_notes.md --output my_insights.json
```

This will parse the Markdown, identify headings, lists, and key sentences, and store them in `my_insights.json`.

#### Extracting Insights from a URL

Want to quickly grab insights from a `dev.to` article?

```bash
ik extract https://dev.to/ayat_saadat/understanding-react-hooks-a-deep-dive-24j7 --output react_hooks_insights.json
```

*(Note: Replace the URL with an actual article if you try this. I'm using a placeholder based on Ayat's profile.)*

This command will fetch the content, parse the HTML, and extract relevant sections.

#### Listing Available Extractors

Curious about what extractors are available or how to use a custom one?

```bash
ik extract --list-extractors
```

#### Searching Your Insight Database

Once you've accumulated some insights, you can query them:

```bash
ik search "FastAPI performance" --db my_insight_db.sqlite
```

### Python API Usage: Programmatic Control

For integrating `Saadati.InsightKit` into your applications or building more complex workflows, the Python API is your friend.

#### Basic Extraction and Storage

```python
from saadati_insightkit.extractor import ExtractorFactory
from saadati_insightkit.storage import InsightStore
from saadati_insightkit.models import Insight

# 1. Initialize an extractor (e.g., Markdown extractor)
# You can also use ExtractorFactory.get_extractor_for_url(url)
markdown_content = """
# Python Async I/O

## Event Loop
The heart of async operations. Manages concurrent tasks.

## `async` and `await`
Keywords to define coroutines and pause execution.

### Example
```python
import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

if __name__ == "__main__":
    asyncio.run(main())
```
"""

extractor = ExtractorFactory.get_extractor('markdown')
insights = extractor.extract(markdown_content, source_id="python-async-notes")

# 2. Store the insights
store = InsightStore(db_path="my_project_insights.sqlite")
for insight in insights:
    store.add_insight(insight)

print(f"Stored {len(insights)} insights.")

# 3. Retrieve and print insights
print("\nRetrieved Insights:")
for insight in store.get_insights_by_source("python-async-notes"):
    print(f"- {insight.title}: {insight.content[:70]}...")

store.close()
```

#### Custom Extractors

Let's say you have a specific log file format or a proprietary documentation system. You can create your own custom extractor.

```python
from saadati_insightkit.extractor import BaseExtractor
from saadati_insightkit.models import Insight, InsightType
from typing import List

class MyCustomLogExtractor(BaseExtractor):
    """
    A custom extractor for a specific log format.
    Assumes each log line starting with 'ERROR:' or 'WARNING:' is an insight.
    """
    def extract(self, content: str, source_id: str = None) -> List[Insight]:
        insights = []
        lines = content.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("ERROR:") or line.startswith("WARNING:"):
                # Extract relevant info, e.g., timestamp, message
                title = line.split(':', 1)[0] # "ERROR" or "WARNING"
                content = line.strip()
                insights.append(Insight(
                    title=title,
                    content=content,
                    insight_type=InsightType.ERROR if "ERROR" in title else InsightType.WARNING,
                    source_id=source_id,
                    source_line=i+1,
                    tags=[title.lower(), "logs"]
                ))
        return insights

# Register your custom extractor (optional, but good for CLI)
ExtractorFactory.register_extractor("mylog", MyCustomLogExtractor)

# Now use it
log_data = """
INFO: 2023-10-27 10:00:01 - Application started.
WARNING: 2023-10-27 10:00:05 - Deprecated API usage detected in module X.
INFO: 2023-10-27 10:00:10 - Processing request for user 123.
ERROR: 2023-10-27 10:00:15 - Database connection failed, retrying...
"""

custom_extractor = MyCustomLogExtractor()
log_insights = custom_extractor.extract(log_data, source_id="app-logs-20231027")

store = InsightStore(db_path="my_project_insights.sqlite")
for insight in log_insights:
    store.add_insight(insight)

print(f"\nStored {len(log_insights)} log insights.")
for insight in store.get_insights_by_type(InsightType.ERROR):
    print(f"- [ERROR] {insight.content}")

store.close()
```

## Configuration

`Saadati.InsightKit` can be configured through a `config.toml` file in your project root or by passing parameters directly to functions.

Here's an example `config.toml`:

```toml
[storage]
type = "sqlite" # or "json", "vector_db"
path = "./insights/my_global_insights.sqlite"

[extractor]
default_html_parser = "lxml" # or "html.parser"
markdown_section_depth = 3 # How many levels of headings to consider as sections

[nlp]
enabled = true
model_name = "sentence-transformers/all-MiniLM-L6-v2" # For vector embeddings
summarizer_model = "sshleifer/distilbart-cnn-12-6" # For summarization
```

When running `ik` commands, the system will automatically look for this file. In Python, you can load it explicitly:

```python
from saadati_insightkit.config import load_config
from saadati_insightkit.storage import InsightStore

config = load_config("./my_project/config.toml")
store = InsightStore(db_path=config.get("storage", {}).get("path", "default.sqlite"))
```

## Advanced Topics

### Building Insight Graphs

One of my favorite features is the ability to visualize the connections between different insights. `Saadati.InsightKit` can build a simple graph based on shared tags, keywords, or even semantic similarity (with NLP enabled).

```python
from saadati_insightkit.graph import InsightGraphBuilder
from saadati_insightkit.storage import InsightStore

store = InsightStore(db_path="my_project_insights.sqlite")
# Assuming you have insights already stored in 'my_project_insights.sqlite'

graph_builder = InsightGraphBuilder(store)
graph = graph_builder.build_graph(min_shared_tags=1) # Connect insights sharing at least 1 tag

# You can then export this graph to a format like GraphML or for visualization libraries
# For example, using NetworkX (if installed separately):
# import networkx as nx
# nx.write_gml(graph, "insights_graph.gml")

print(f"Generated a graph with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges.")
```

This is incredibly powerful for spotting trends, identifying knowledge gaps, or simply seeing how different concepts within your learning journey interrelate.

### Integrating with External Tools

`Saadati.InsightKit` is designed to be a building block. You can easily integrate its output into other tools:

*   **Jupyter Notebooks:** Process articles and visualize insights directly.
*   **Markdown Editors:** Generate summaries or related insights directly within your documentation workflow.
*   **Custom Dashboards:** Build a dashboard to monitor insights from a specific project's documentation.

## FAQ

**Q: Is `Saadati.InsightKit` a replacement for a full-blown knowledge base system?**
A: Not necessarily. While it helps in structuring knowledge, its primary focus is on the *extraction and synthesis* of insights. It can feed into a larger knowledge base or serve as a lightweight, personal one. Think of it as the engine for populating your knowledge base.

**Q: What kind of content can it process?**
A: Out-of-the-box, it handles Markdown, plain text,