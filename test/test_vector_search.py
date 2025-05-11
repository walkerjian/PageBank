from models.vector_search import search

docs = [
    "The S&P 500 rose slightly amid low trading volume.",
    "Bitcoin hit a new weekly high as crypto markets rallied.",
    "Tesla shares dipped following earnings miss."
]

query = "How did crypto perform?"

results = search(query, docs)
for doc, score in results:
    print(f"{score:.2f} - {doc}")
