from crawler.scraper import scrape_pages
from ranker.pagerank import compute_pagerank
from models.vector_search import search
from models.summarizer import summarize_text

# 1. Scrape pages
pages = scrape_pages(["https://example.com"])
page_texts = list(pages.keys())

# 2. Rank them
ranking = compute_pagerank(pages)
print("PageRank scores:")
for url, score in ranking.items():
    print(f"{url}: {score:.4f}")

# 3. Vector search demo
print("\nSearch Results:")
query = "example website content"
results = search(query, page_texts)
for doc, score in results:
    print(f"{score:.2f} - {doc}")

# 4. Summarization demo
print("\nSummarization:")
for url in page_texts[:1]:
    print(f"{url}:")
    print(summarize_text(pages[url]))

summary = summarize_text(pages[url])
print(f"Summary of {url}:\n{summary}\n")
