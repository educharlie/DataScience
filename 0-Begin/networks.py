import networkx as nx

edgelist = {(0,1), (0,2), (0,3), (0,5), (0,9), (1,3), (1,4), (1,6), (1,9), (2,3), (2,5), (3,4), (3,5), (3,6), (4,6), (5,6), (7,8), (8,9)}
G = nx.Graph()
for edge in edgelist:
    G.add_edge(edge[0], edge[1])

import matplotlib.pyplot as plt
nx.draw(G)
#plt.show()
print nx.degree_centrality(G)
print nx.betweenness_centrality(G)
print nx.closeness_centrality(G)
print nx.eigenvector_centrality(G)
