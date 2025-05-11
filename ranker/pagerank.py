import networkx as nx

def compute_pagerank(page_graph):
    G = nx.DiGraph()
    for src, links in page_graph.items():
        for dst in links:
            G.add_edge(src, dst)
    return nx.pagerank(G)
