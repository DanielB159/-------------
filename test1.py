import networkx as nx
import matplotlib.pyplot as plt
import GraphAlgorithms as ga

if __name__ == '__main__':
    G = nx.Graph()
    G.add_nodes_from(["a", "b", "c", "d", "e", "f"])
    G.add_edge("a", "b", weight=5)
    G.add_edge("a", "c", weight=6)
    G.add_edge("c", "e", weight=7)
    G.add_edge("e", "f", weight=2)
    G.add_edge("d", "f", weight=3)
    G.add_edge("c", "f", weight=4)
    G.add_edge("a", "e", weight=1)
    pos = nx.spring_layout(G, seed=7)
    nx.draw_networkx_nodes(G, pos, node_size=400)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(data=True), width=6, alpha=0.5, edge_color="b")
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    ga.Dijkstra(G, "a")
    plt.show()


