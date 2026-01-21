import networkx as nx
import matplotlib.pyplot as mp

def MyMinimumSpannigTree(Graph: nx.Graph) -> nx.Graph:
    print("Creating MST using Prim's algorithm")
    mst = nx.Graph()
    starting_node = "A"
    visited_nodes = set()
    visited_nodes.add(starting_node)
    mst.add_node(starting_node)
    print(f"Starting node: {starting_node}")
    # The ending condition is edges = nodes - 1.
    while len(visited_nodes) < len(Graph.nodes):
        smallest_edge = None
        
        for edge in Graph.edges(data=True) :
           node1, node2, data = edge
           # Using a xor, we first check whether the edge is valid
           # The constraint is that we need to 1 node to be visited,
           # while the other one is unvisited.
           if not ((node1 in visited_nodes) != (node2 in visited_nodes)):
               reason = ''
               if(node1 in visited_nodes and node2 in visited_nodes):
                   reason = 'both nodes have already been visited'
               elif (node1 not in visited_nodes) and (node2 not in visited_nodes):
                   reason = 'it is not connected to the existing graph'
               print(f"Skipping edge ({node1}, {node2}) because {reason}")
               # If both are visited (or unvisited) we ignore this edge.
               continue
               
           if smallest_edge is None or data["weight"] < smallest_edge[2]["weight"]:
               smallest_edge = edge
        
        node1, node2, data = smallest_edge
        
        if node1 in visited_nodes:
            visited_node = node1
            unvisited_node = node2
        else :
            visited_node = node2
            unvisited_node = node1
        
        print(f"Added edge ({visited_node}, {unvisited_node}) with weight {data['weight']}")
        visited_nodes.add(unvisited_node)
        mst.add_edge(visited_node, unvisited_node, weight=data["weight"])
        
    return mst

# Will use subplots so both graphs appear in the same plot
fig, axes = mp.subplots(3, 2, figsize=(15, 13))

def draw_graph_and_mst(graph, row, title):
    # Layout set to circular
    pos = nx.circular_layout(graph)
    
    # Nodes (with some color and increased node_size for better visualization)
    nx.draw_networkx_nodes(graph, pos, ax=axes[row][0], node_color="lightblue", node_size=800)
    
    # Edges
    nx.draw_networkx_edges(graph, pos, ax=axes[row][0], width=2)
    
    # Node labels
    nx.draw_networkx_labels(graph, pos, ax=axes[row][0])
    
    # Edge labels
    edge_labels = nx.get_edge_attributes(graph, "weight")
    
    nx.draw_networkx_edge_labels(graph, pos, edge_labels, ax=axes[row][0])
    
    axes[row][0].set_title(title)
    
    axes[row][1].axis("off")
    
    mst = MyMinimumSpannigTree(graph)
    
    pos2 = nx.circular_layout(mst)
    
    # Nodes (with some color and increased node_size for better visualization)
    nx.draw_networkx_nodes(mst, pos2, ax=axes[row][1], node_color="lightblue", node_size=800)
    
    # Edges
    nx.draw_networkx_edges(mst, pos2, ax=axes[row][1], width=2)
    
    # Node labels
    nx.draw_networkx_labels(mst, pos2, ax=axes[row][1])
    
    # Edge labels
    edge_labels = nx.get_edge_attributes(mst, "weight")
    
    nx.draw_networkx_edge_labels(mst, pos2, edge_labels, ax=axes[row][1], )
    
    axes[row][1].set_title(f"Minimum Spanning Tree {row + 1}")
    
    axes[row][1].axis("off")

# ---------------------------------------- Graph 1 ----------------------------------------
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

draw_graph_and_mst(G, 0, "Original Graph")

print('\n')

# ---------------------------------------- Graph 2 ----------------------------------------
G2 = nx.Graph()

# Graph 2 should be at least 5 nodes
nodes = ["A", "B", "C", "D", "E"]

G2.add_nodes_from(nodes)

# And then I also need at least 8 weighted edges
G2.add_edge("A", "B", weight=4)

G2.add_edge("A", "E", weight=11)

G2.add_edge("A", "D", weight=12)

G2.add_edge("B", "C", weight=17)

G2.add_edge("B", "D", weight=7)

G2.add_edge("B", "E", weight=22)

G2.add_edge("C", "D", weight=10)

G2.add_edge("C", "B", weight=4)

G2.add_edge("D", "E", weight=15)

draw_graph_and_mst(G2, 1, "Graph 2")

print('\n')

# ---------------------------------------- Graph 3 ----------------------------------------
G3 = nx.Graph()

# Graph 3 should also be at least 5 nodes
nodes = ["A", "B", "C", "D", "E", "F"]

G3.add_nodes_from(nodes)

# And then I also need again, at least 8 weighted edges
G3.add_edge("A", "C", weight=9)

G3.add_edge("A", "B", weight=7)

G3.add_edge("A", "D", weight=5)

G3.add_edge("A", "E", weight=2)

G3.add_edge("A", "F", weight=15)

G3.add_edge("B", "C", weight=6)

G3.add_edge("B", "D", weight=13)

G3.add_edge("B", "E", weight=20)

G3.add_edge("C", "D", weight=30)

G3.add_edge("C", "B", weight=35)

G3.add_edge("D", "E", weight=24)

G3.add_edge("E", "F", weight=34)

draw_graph_and_mst(G3, 2, "Graph 3")

mp.show()
