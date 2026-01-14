import networkx as nx
import matplotlib.pyplot as mp

G = nx.Graph()

# Original Graph should be 6 nodes
nodes = ["A", "B", "C", "D", "E", "F"]

G.add_nodes_from(nodes)

# And then I also need 10 weighted edges
G.add_edge("A", "B", weight=2)

G.add_edge("A", "C", weight=7)

G.add_edge("A", "F", weight=20)

G.add_edge("B", "F", weight=25)

G.add_edge("C", "D", weight=4)

G.add_edge("C", "B", weight=9)

G.add_edge("D", "E", weight=15)

G.add_edge("D", "F", weight=10)

G.add_edge("C", "F", weight=5)

G.add_edge("E", "F", weight=13)


# Layout set to circular
pos = nx.circular_layout(G)

# Nodes (with some color and increased node_size for better visualization)
nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=800)

# Edges
nx.draw_networkx_edges(G, pos, width=2)

# Node labels
nx.draw_networkx_labels(G, pos)

# Edge labels
edge_labels = nx.get_edge_attributes(G, "weight")


nx.draw_networkx_edge_labels(G, pos, edge_labels)

mp.title("Original Graph")

mp.show()

def MyMinimumSpannigTree(Graph: nx.Graph) -> nx.Graph:
