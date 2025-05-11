# PageBank

An experimental AI-driven search engine that scrapes, ranks, and analyzes financial web content.

## 🔍 Features

- **Self-Scraping Web Agent**: Crawls URLs and collects link data.
- **PageRank Analysis**: Ranks scraped URLs using network topology.
- **Vector-Based Semantic Search**: Ranks content relevance using sentence embeddings.
- **GPT-Based Summarization**: Generates summaries of textual content.
- **Modular Layout**: Easily extensible and testable.

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python run_demo.py
```

## 🧪 Testing

```bash
python test/test_vector_search.py
python test/test_summarizer.py
```

## ⚠️ Note

You must provide an OpenAI API key in `models/summarizer.py` to use the GPT-based summarization.
