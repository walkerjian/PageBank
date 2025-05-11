from crawler.scraper import scrape_pages
from ranker.pagerank import compute_pagerank

def main():
    pages = scrape_pages(["https://example.com"])
    ranked = compute_pagerank(pages)
    for url, score in ranked.items():
        print(f"{url}: {score:.4f}")

if __name__ == "__main__":
    main()
