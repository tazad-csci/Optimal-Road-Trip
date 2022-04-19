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
        
        
#shortest_paths = dict(nx.shortest_path_length(G))
#node_path_avg = [sum(paths).values()) / len(G.nodes) for node, paths in shortest_path.items()]
#print(nx.shortest_path(G,'NY','VT'))
print(nx.info(G))

#for i in nx.clustering(G).items():
    #print(i)
    
#print("Average Clustering: ", nx.average_clustering(G)) 
print("Destiny: ", nx.density(G))         #measures how interconnected a graph is

#nx.radius(G) 

#nx.diameter(G)
print(nx.is_connected(G))
components = nx.connected_components(G)
largest_component = max(components, key=len)

subgraph = G.subgraph(largest_component)
diameter = nx.diameter(subgraph)
print('Network diameter of largest component:', diameter)

print('Triadic closure:', nx.transitivity(G))  #ratio of all triangles over possible triangles; measures how interconnected a graph is

def plot_deg_dist(G):
    all_degrees = [v for k, v in nx.degree(G)]    #all the degrees
    unique_degrees = list(set(all_degrees))       #all the unique degrees

    count_of_degrees = []
    for i in range(0,max(unique_degrees)):
        x = all_degrees.count(i)
        count_of_degrees.append(x)

        
    plt.figure(figsize=(9, 6))
    plt.plot(unique_degrees, count_of_degrees)   
    plt.title("Degree Distribution")
    plt.ylabel("Number of Nodes")
    plt.xlabel("Degrees")  
    plt.show()    
    
plot_deg_dist(G)  
