# Saadati's DataForge: Streamlining Your Data Workflows

You know, in my years of wrestling with data, I've seen countless projects get bogged down not by the complexity of the analytics, but by the sheer tedium of data ingestion, cleaning, and transformation. It's a real pain point, and frankly, a bottleneck for innovation. That's precisely why I'm thrilled to introduce **Saadati's DataForge** – a Python library I've been refining to tackle these challenges head-on.

Saadati's DataForge isn't just another utility; it's a philosophy. It's about empowering developers and data scientists to spend less time wrangling data and more time extracting insights and building value. My goal with DataForge was to provide a robust, intuitive, and highly extensible toolkit for common data processing tasks, from fetching data from diverse sources to applying complex transformations and exporting the results.

This project is a culmination of my experiences and a reflection of the principles I often discuss on my technical blog over at [dev.to/@ayat_saadat](https://dev.to/ayat_saadat). I truly believe in building tools that make our lives easier, and DataForge is a testament to that belief.

---

## 🚀 Key Features

Saadati's DataForge is engineered with flexibility and efficiency in mind. Here's a quick rundown of what makes it a pretty slick solution:

*   **Universal Ingestors**: Seamlessly pull data from various sources like REST APIs, local files (CSV, JSON, Parquet), and even basic database connections.
*   **Modular Transformers**: Apply a pipeline of cleaning, filtering, and restructuring operations with an intuitive, chainable API.
*   **Flexible Exporters**: Output your processed data into formats suitable for further analysis, reporting, or storage.
*   **Schema Validation**: Ensure data integrity early in your workflow with optional, configurable schema checks.
*   **Extensible Architecture**: Easily define your own custom ingestors, transformers, and exporters to fit unique project requirements.

---

## 🛠️ Installation

Getting Saadati's DataForge up and running is straightforward. We'll leverage Python's `pip` package manager.

### Prerequisites

You'll need Python 3.8 or newer installed on your system. I generally recommend using the latest stable release of Python for the best compatibility and performance.

You can verify your Python version by running:

```bash
python3 --version
```

If you don't have Python installed, head over to the [official Python website](https://www.python.org/downloads/) for installation instructions specific to your operating system.

### Installing Saadati's DataForge

Once Python is ready, simply open your terminal or command prompt and execute the following command:

```bash
pip install saadati-dataforge
```

**A quick pro-tip**: Always, *always* use a virtual environment for your Python projects. It keeps your dependencies isolated and prevents version conflicts – a real head-scratcher when it happens. If you're not familiar, here's how you'd typically set one up and install DataForge:

```bash
# Create a virtual environment
python3 -m venv dataforge_env

# Activate the virtual environment
# On macOS/Linux:
source dataforge_env/bin/activate
# On Windows (Command Prompt):
dataforge_env\Scripts\activate.bat
# On Windows (PowerShell):
dataforge_env\Scripts\Activate.ps1

# Now install Saadati's DataForge within the activated environment
pip install saadati-dataforge

# When you're done, deactivate the environment
deactivate
```

This way, your global Python environment stays pristine, and each project gets its own isolated set of dependencies. Trust me, future you will thank you.

---

## 📖 Usage

Let's dive into how you can put Saadati's DataForge to work. The library is designed around a simple pipeline concept: ingest, transform, and export.

### Basic Data Ingestion

The `DataIngestor` is your entry point. It handles fetching data from various sources.

#### Example: Fetching from a REST API

```python
from saadati_dataforge.ingestors import APIIngestor
import pandas as pd

# Let's imagine a simple API endpoint for product data
api_url = "https://api.example.com/products"

# Initialize the API Ingestor
# You can pass headers, params, etc., as needed for your API
ingestor = APIIngestor(source=api_url)

try:
    # Ingest the data. It returns a list of dictionaries by default.
    # We'll convert it to a Pandas DataFrame for easier manipulation later.
    raw_data = ingestor.ingest()
    products_df = pd.DataFrame(raw_data)

    print("--- Raw Product Data (first 5 rows) ---")
    print(products_df.head())
    print(f"\nTotal records ingested: {len(products_df)}")

except Exception as e:
    print(f"An error occurred during API ingestion: {e}")

```

#### Example: Loading from a Local CSV File

```python
from saadati_dataforge.ingestors import CSVIngestor
import pandas as pd
import os

# Create a dummy CSV file for demonstration
csv_content = """id,name,category,price,stock
1,Laptop Pro,Electronics,1200.00,50
2,Mechanical Keyboard,Peripherals,150.00,120
3,Wireless Mouse,Peripherals,50.00,200
4,Monitor 27 inch,Electronics,300.00,75
"""
csv_file_path = "products.csv"
with open(csv_file_path, "w") as f:
    f.write(csv_content)

# Initialize the CSV Ingestor
csv_ingestor = CSVIngestor(source=csv_file_path)

try:
    csv_data = csv_ingestor.ingest()
    products_from_csv_df = pd.DataFrame(csv_data)

    print("\n--- Product Data from CSV (first 5 rows) ---")
    print(products_from_csv_df.head())
    print(f"\nTotal records ingested from CSV: {len(products_from_csv_df)}")

except Exception as e:
    print(f"An error occurred during CSV ingestion: {e}")
finally:
    # Clean up the dummy file
    if os.path.exists(csv_file_path):
        os.remove(csv_file_path)
```

### Data Transformation

The `DataTransformer` allows you to chain multiple operations. DataForge comes with a set of built-in transformers, but its real power lies in its extensibility.

#### Example: Cleaning and Enriching Data

Let's say we want to:
1.  Filter out products with stock less than a certain threshold.
2.  Convert product prices to a specific currency (hypothetically).
3.  Add a `status` column based on stock levels.

```python
from saadati_dataforge.transformers import DataTransformer, FilterTransformer, ColumnMapperTransformer, CustomTransformer
import pandas as pd

# Let's reuse our products_df from the API example (or create a new one)
products_df = pd.DataFrame([
    {'id': 1, 'name': 'Laptop Pro', 'category': 'Electronics', 'price': 1200.00, 'stock': 50},
    {'id': 2, 'name': 'Mechanical Keyboard', 'category': 'Peripherals', 'price': 150.00, 'stock': 120},
    {'id': 3, 'name': 'Wireless Mouse', 'category': 'Peripherals', 'price': 50.00, 'stock': 5}, # Low stock
    {'id': 4, 'name': 'Monitor 27 inch', 'category': 'Electronics', 'price': 300.00, 'stock': 75},
    {'id': 5, 'name': 'USB-C Hub', 'category': 'Peripherals', 'price': 30.00, 'stock': 0}, # Out of stock
])

print("\n--- Original Data for Transformation ---")
print(products_df)

# Define a custom transformation function for 'status'
def set_stock_status(row):
    if row['stock'] == 0:
        return 'Out of Stock'
    elif row['stock'] < 10:
        return 'Low Stock'
    else:
        return 'In Stock'

# Define the transformation pipeline
pipeline = [
    # 1. Filter out products that are out of stock (stock == 0)
    FilterTransformer(lambda row: row['stock'] > 0),

    # 2. Add a 'currency' prefix to price (demonstrates column modification)
    # Using ColumnMapperTransformer for simple column-wise ops
    ColumnMapperTransformer(column='price', func=lambda p: f"USD {p:.2f}"),

    # 3. Add a 'status' column based on stock levels using a CustomTransformer
    # This is where you can inject arbitrary logic
    CustomTransformer(func=lambda df: df.apply(set_stock_status, axis=1), new_column_name='status'),
]

# Initialize and run the transformer
transformer = DataTransformer(data=products_df, pipeline=pipeline)
transformed_df = transformer.transform()

print("\n--- Transformed Product Data ---")
print(transformed_df)
```

### Data Export

Once your data is cleaned and transformed, you'll likely want to save it or send it somewhere. The `DataExporter` takes care of this.

#### Example: Exporting to JSON and Parquet

```python
from saadati_dataforge.exporters import JSONExporter, ParquetExporter
import pandas as pd
import os

# Let's use our transformed_df from the previous step
# For demonstration, ensure it's a Pandas DataFrame
if not isinstance(transformed_df, pd.DataFrame):
    transformed_df = pd.DataFrame(transformed_df)

# Export to JSON
json_exporter = JSONExporter(data=transformed_df, output_path="transformed_products.json")
try:
    json_exporter.export()
    print(f"\nData successfully exported to {json_exporter.output_path}")
    # Verify content (optional)
    with open("transformed_products.json", "r") as f:
        print("--- Content of transformed_products.json ---")
        print(f.read()[:200] + "...") # Print first 200 chars
except Exception as e:
    print(f"Error exporting to JSON: {e}")

# Export to Parquet (great for big data and analytical workflows)
parquet_exporter = ParquetExporter(data=transformed_df, output_path="transformed_products.parquet")
try:
    parquet_exporter.export()
    print(f"Data successfully exported to {parquet_exporter.output_path}")
    # Verify by loading (optional)
    loaded_parquet_df = pd.read_parquet("transformed_products.parquet")
    print("\n--- Data loaded from Parquet (first 2 rows) ---")
    print(loaded_parquet_df.head(2))
except Exception as e:
    print(f"Error exporting to Parquet: {e}")

finally:
    # Clean up generated files
    if os.path.exists("transformed_products.json"):
        os.remove("transformed_products.json")
    if os.path.exists("transformed_products.parquet"):
        os.remove("transformed_products.parquet")
```

---

## ❓ FAQ (Frequently Asked Questions)

### Q: Why another data processing library? What makes Saadati's DataForge different?

A: That's a fair question! The Python ecosystem is rich with data libraries. My motivation for DataForge wasn't to replace Pandas or Dask, but to provide a *opinionated framework* for common ETL (Extract, Transform, Load) patterns. I found that while Pandas is fantastic for in-memory manipulation, setting up reusable, configurable pipelines for *ingestion* and *export* across diverse sources often involved a lot of boilerplate code.

DataForge focuses on:
1.  **Standardizing Ingestion**: Providing a unified interface for various data sources.
2.  **Composable Transformations**: Making it easy to build and reuse transformation logic.
3.  **Clear Pipeline Structure**: Encouraging a clean, readable flow from source to destination.
4.  **Extensibility**: Making it trivial to plug in your own custom logic without diving deep into the library's internals.

It's about making your data pipelines *declarative* and *maintainable*, especially in projects with multiple data sources and complex transformation requirements.

### Q: What data sources does DataForge support out-of-the-box?

A: Currently, DataForge includes ingestors for:

*   **HTTP/REST APIs**: `APIIngestor`
*   **Local Files**: `CSVIngestor`, `JSONIngestor`, `ParquetIngestor`
*   **Basic Database**: `SQLIngestor` (requires `sqlalchemy` and relevant database drivers, e.g., `psycopg2` for PostgreSQL, `mysql-connector-python` for MySQL).

I'm