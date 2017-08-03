import networkx as nx

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(["u","v"])
G.add_edge(1,2)
G.add_edge("u","v")
G.add_edges_from([(1,3), (1,4), (1,5), (1,6)])
G.add_edge("u", "w")
G.remove_node(2)

import matplotlib.pyplot as plt
G = nx.karate_club_graph()
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
plt.savefig("karateGraph.pdf")

#random graphs
from scipy.stats import bernoulli
bernoulli.rvs(p=0.2)

N=20
p = 0.2

#create empty graph
# add all N nodes in the graph
# loop over all paris of nodes
    #add an edge with prob b
def er_graph(N, p):
    """Generate an ER graph"""
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p):
                G.add_edge(node1, node2)
    return G
nx.draw(er_graph(10, 0), node_size = 40, node_color="gray")

def plot_degree_distribution(G):
    plt.hist(list(G.degree().values()), histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree Distribution")
    
G = er_graph(500, 0.08)
plot_degree_distribution(G)
plt.savefig("hist1.fig")