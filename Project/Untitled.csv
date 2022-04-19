import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from Data import likely_routes

G = nx.Graph()
    
for source in list(likely_routes):
    des = likely_routes[source]
    for target2, des in des.items():
        G.add_edge(source, target2, weight=des[0])
        
nx.draw_spring(G)
#nx.diameter(G)
#nx.cluster.average_clustering(G)
        
#plt.figure(2)

#G_Erdos = nx.erdos_renyi_graph(1000,0.1)
#degrees = [G_Erdos.degree[i] for i in G_Erdos.nodes]
#plt.title("Degree Histogram")
#plt.ylabel("p_k")
#plt.xlabel("k")     
#plt.hist(degrees, bins = range( min(degrees), max(degrees) ) )
