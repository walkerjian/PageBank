import requests
from bs4 import BeautifulSoup

def scrape_pages(urls):
    page_graph = {}
    for url in urls:
        try:
            resp = requests.get(url, timeout=5)
            soup = BeautifulSoup(resp.text, 'html.parser')
            links = [a['href'] for a in soup.find_all('a', href=True)]
            page_graph[url] = links
        except Exception as e:
            print(f"Failed to scrape {url}: {e}")
    return page_graph
