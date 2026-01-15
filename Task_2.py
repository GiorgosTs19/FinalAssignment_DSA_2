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

# # Layout set to circular
# pos = nx.circular_layout(G)
#
# # Nodes (with some color and increased node_size for better visualization)
# nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=800)
#
# # Edges
# nx.draw_networkx_edges(G, pos, width=2)
#
# # Node labels
# nx.draw_networkx_labels(G, pos)
#
# # Edge labels
# edge_labels = nx.get_edge_attributes(G, "weight")
#
# nx.draw_networkx_edge_labels(G, pos, edge_labels)
#
# mp.title("Original Graph")

# mp.show()

def MyMinimumSpannigTree(Graph: nx.Graph) -> nx.Graph:
    
    def create_mst(starting_node) :
        mst = nx.Graph()
        
        visited_nodes = set()
        visited_nodes.add(starting_node)
        mst.add_node(starting_node)
        # The ending condition is edges = nodes - 1.
        print(Graph.edges(data=True))
        while len(visited_nodes) < len(Graph.nodes):
            smallest_edge = None
            visited_node = None
            unvisited_node = None
            for edge in Graph.edges(data=True) :
               node1, node2, data = edge
               # Using a xor, we first check whether the edge is valid
               # The constraint is that we need to 1 node to be visited,
               # while the other one is unvisited.
               if not ((node1 in visited_nodes) != (node2 in visited_nodes)):
                   # If both are visited (or unvisited) we ignore this edge.[[
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
            
        pos = nx.circular_layout(mst)
        
        # Nodes (with some color and increased node_size for better visualization)
        nx.draw_networkx_nodes(mst, pos, node_color="lightblue", node_size=800)

        # Edges
        nx.draw_networkx_edges(mst, pos, width=2)
        
        # Node labels
        nx.draw_networkx_labels(mst, pos)
        
        # Edge labels
        edge_labels = nx.get_edge_attributes(mst, "weight")
        
        nx.draw_networkx_edge_labels(mst, pos, edge_labels)
        
        mp.title("MST")
        
        mp.show()
        
    create_mst("A")
MyMinimumSpannigTree(G)
