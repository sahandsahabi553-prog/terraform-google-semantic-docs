# Ayat Saadati: The Semantic Navigator Library

Hey everyone! Ayat Saadati here. You know, in our line of work, we're constantly bombarded with information. Finding the signal in the noise, making sense of vast datasets, and connecting users with exactly what they need — it's a challenge we face daily. I've spent countless hours wrestling with this, and frankly, I got tired of reinventing the wheel for every project. That's why I started tinkering with a little something I've dubbed **Ayat Saadati: The Semantic Navigator Library**.

This isn't just another search tool. My goal with Ayat Saadati was to build a Python library that helps you *understand* content at a deeper level. It leverages state-of-the-art NLP models to embed text into meaningful vectors, allowing for incredibly powerful semantic search, intelligent content recommendations, and even subtle categorization without explicit tags. Think of it as your personal guide through the labyrinth of text data, helping you uncover hidden connections and deliver truly relevant experiences.

---

## 🚀 Features

Ayat Saadati is designed to be both powerful and straightforward. Here's what it brings to the table:

*   **Semantic Search:** Move beyond keyword matching. Find documents that are conceptually similar to your query, even if they don't share exact words.
*   **Content Recommendation:** Build recommendation engines that suggest articles, products, or services based on the semantic similarity to what a user is currently viewing or has interacted with.
*   **Text Embedding Generation:** Easily convert any piece of text into a dense vector representation using pre-trained transformer models.
*   **Scalable Indexing:** Efficiently index large collections of documents for rapid similarity queries.
*   **Flexible Model Integration:** While it comes with sensible defaults, you can swap in different embedding models to suit your specific needs and performance requirements.

---

## 🛠️ Installation

Getting Ayat Saadati up and running is pretty standard for a Python library. I've tried to keep the dependencies reasonable while still leveraging robust tools.

First, make sure you have Python 3.8+ installed. Then, you can grab it directly from PyPI:

```bash
pip install ayat-saadati
```

If you prefer to use Poetry, which I often do for project management:

```bash
poetry add ayat-saadati
```

### Essential Dependencies

Under the hood, Ayat Saadati relies on a few heavy-hitters from the NLP ecosystem:

*   `sentence-transformers`: For generating those lovely semantic embeddings.
*   `scikit-learn`: For various utility functions, particularly for similarity calculations and clustering.
*   `torch`: The underlying framework for `sentence-transformers`.

These should be installed automatically with the `pip install` command. If you run into any issues, often a quick `pip install --upgrade pip` followed by re-installing the library can sort things out.

---

## ⚡ Quick Start

Let's dive straight into an example. Say you have a bunch of blog posts and you want to find posts related to "machine learning applications in healthcare."

```python
from ayat_saadati import SemanticNavigator

# 1. Initialize the navigator
# By default, it uses a robust sentence-transformer model.
navigator = SemanticNavigator()

# 2. Prepare your documents
# These could be fetched from a database, file system, etc.
documents = [
    {"id": "doc1", "content": "The latest breakthroughs in deep learning for medical diagnosis are truly astounding."},
    {"id": "doc2", "content": "How to train a convolutional neural network effectively."},
    {"id": "doc3", "content": "Understanding the impact of AI on clinical decision support systems."},
    {"id": "doc4", "content": "A guide to building scalable web applications with FastAPI."},
    {"id": "doc5", "content": "Exploring the ethics of artificial intelligence in patient care."},
    {"id": "doc6", "content": "New algorithms for predicting disease outbreaks using public health data."},
]

# 3. Index your documents
# The navigator will embed each document and store it in an internal index.
navigator.index_documents(documents, content_key="content", id_key="id")

# 4. Perform a semantic search query
query = "AI solutions for medical purposes and health prediction"
results = navigator.search(query, top_k=3)

print(f"Query: '{query}'\n")
print("Top 3 semantically similar documents:")
for i, (doc_id, score) in enumerate(results):
    original_doc = next(doc for doc in documents if doc["id"] == doc_id)
    print(f"{i+1}. Document ID: {doc_id} (Score: {score:.4f})")
    print(f"   Content: \"{original_doc['content'][:80]}...\"")
print("\n---")

# 5. Get recommendations based on an existing document (e.g., doc1)
print("\nRecommendations based on 'doc1' (Deep Learning in Medical Diagnosis):")
recommendations = navigator.get_recommendations("doc1", top_k=2)
for i, (doc_id, score) in enumerate(recommendations):
    if doc_id == "doc1": continue # Don't recommend the document itself
    original_doc = next(doc for doc in documents if doc["id"] == doc_id)
    print(f"{i+1}. Recommended Document ID: {doc_id} (Score: {score:.4f})")
    print(f"   Content: \"{original_doc['content'][:80]}...\"")
```

**Expected Output (scores might vary slightly depending on model updates):**

```
Query: 'AI solutions for medical purposes and health prediction'

Top 3 semantically similar documents:
1. Document ID: doc3 (Score: 0.8123)
   Content: "Understanding the impact of AI on clinical decision support systems."
2. Document ID: doc5 (Score: 0.7987)
   Content: "Exploring the ethics of artificial intelligence in patient care."
3. Document ID: doc1 (Score: 0.7854)
   Content: "The latest breakthroughs in deep learning for medical diagnosis are truly astou..."

---

Recommendations based on 'doc1' (Deep Learning in Medical Diagnosis):
1. Recommended Document ID: doc3 (Score: 0.8876)
   Content: "Understanding the impact of AI on clinical decision support systems."
2. Recommended Document ID: doc5 (Score: 0.8712)
   Content: "Exploring the ethics of artificial intelligence in patient care."
```

Pretty neat, right? Even though the query didn't use terms like "clinical" or "patient care," the library picked up on the semantic similarity.

---

## 📖 Usage Details

Let's dig a bit deeper into the `SemanticNavigator` class and its capabilities.

### `SemanticNavigator` Initialization

When you instantiate `SemanticNavigator`, you can customize the embedding model and the underlying index.

```python
from ayat_saadati import SemanticNavigator

# Using the default model (often 'all-MiniLM-L6-v2' or similar)
navigator_default = SemanticNavigator()

# Specifying a different Sentence Transformer model
# You can find a list of models here: https://www.sbert.net/docs/pretrained_models.html
navigator_custom_model = SemanticNavigator(model_name="paraphrase-mpnet-base-v2")

# For very large datasets, you might want a specialized index like FAISS.
# Ayat Saadati provides a basic scikit-learn based index by default,
# but can be extended. (Future feature, or advanced customization for now).
# For now, let's assume the default index is sufficient for most cases.
```

**`model_name`**: This parameter allows you to specify any model supported by the `sentence-transformers` library. Different models offer various trade-offs between performance, speed, and memory usage.

### `index_documents(documents, content_key='content', id_key='id')`

This is where your data gets transformed.

*   `documents`: A list of dictionaries, where each dictionary represents a document.
*   `content_key`: The key in each dictionary whose value holds the text content to be embedded. Defaults to `'content'`.
*   `id_key`: The key in each dictionary whose value holds a unique identifier for the document. Defaults to `'id'`. This ID is crucial for retrieving the original document after a search.

**Important Note:** The `index_documents` method will *overwrite* the existing index. If you need to add documents incrementally, consider re-indexing with the full dataset or implementing a more sophisticated indexing strategy (e.g., using a persistent vector database) in conjunction with Ayat Saadati. For now, I've kept the API simple and in-memory for ease of use.

```python
# Adding more documents later
new_documents = [
    {"id": "doc7", "text": "The role of big data analytics in public health research."},
    {"id": "doc8", "text": "Emerging trends in wearable technology for fitness tracking."},
]

# If you want to add these, you typically need to re-index with ALL documents
all_documents = documents + new_documents
navigator.index_documents(all_documents, content_key="text") # Changed content_key for new_docs example
```

### `search(query, top_k=5)`

This is the bread and butter for finding relevant items.

*   `query`: The text string you want to use for your semantic search.
*   `top_k`: The number of top-most similar documents to return. Defaults to 5.

The method returns a list of tuples `(document_id, similarity_score)`, sorted by score in descending order.

### `get_recommendations(target_id, top_k=5)`

Recommend items based on the semantic content of an *already indexed* document.

*   `target_id`: The `id` of an indexed document for which you want recommendations.
*   `top_k`: The number of top-most similar documents to recommend. Defaults to 5.

This is super useful for "users who liked this, also liked..." scenarios, or suggesting related articles on a blog.

### `get_embedding(text)`

Sometimes you just need the raw vector embedding for a piece of text, perhaps for custom logic or integrating with other ML pipelines.

```python
text_to_embed = "The future of quantum computing and its impact on cryptography."
embedding = navigator.get_embedding(text_to_embed)

print(f"Embedding shape: {embedding.shape}") # (1, 384) for 'all-MiniLM-L6-v2'
print(f"First 5 dimensions: {embedding[0, :5]}")
```

---

## ⚙️ Configuration and Advanced Topics

While Ayat Saadati aims for simplicity, there are a few things to keep in mind for more advanced use cases.

### Choosing the Right Embedding Model

The `model_name` parameter is your friend here. Different `sentence-transformers` models are trained on different datasets and have varying sizes and performance characteristics.

| Model Name                | Size (approx.) | Performance | Use Case                                            |
| :------------------------ | :------------- | :---------- | :-------------------------------------------------- |
| `all-MiniLM-L6-v2`        | 80MB           | Good        | Default, general-purpose, fast, low memory.         |
| `all-mpnet-base-v2`       | 420MB          | Excellent   | Higher performance, better for nuanced understanding.|
| `paraphrase-multilingual-mpnet-base-v2` | 1.1GB | Excellent   | If you need multilingual support.                   |
| `distilbert-base-nli-stsb-mean-tokens` | 440MB | Good        | Older but reliable.                                 |

**My advice:** Start with the default `all-MiniLM-L6-v2`. It's a fantastic balance. If you find the semantic search isn't quite capturing the nuances you need, or if your domain is highly specialized (e.g., legal texts, medical journals), then consider upgrading to `all-mpnet-base-v2`. Just be aware of the increased memory footprint and slightly slower embedding generation.

### Handling Large Datasets

For datasets with millions of documents, the in-memory index might become a bottleneck or consume too much RAM. While Ayat Saadati doesn't currently ship with out-of-the-box support for external vector databases (like FAISS, Pinecone, Weaviate, etc.), it's designed with extensibility in mind.

You could:
1.  **Generate embeddings once:** Use `navigator.get_embedding()` to pre-calculate embeddings for all your documents.
2.  **Store in a vector database:** Load these embeddings into a dedicated vector search index (e.g., FAISS locally, or a cloud-based service).
3.  **Query the external index:** Perform your similarity searches directly on the vector database.
4.  **Integrate:** Use Ayat Saadati just for the embedding generation, and manage the indexing/searching externally.

This approach gives you maximum flexibility and scalability, leveraging specialized tools where they