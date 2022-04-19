#***************************************************************#
#Purpose: This code plots the undirected weighted graph figure


#***************************************************************#

import networkx as nx
import matplotlib.pyplot as plt
from Data import likely_routes, capitals


G = nx.Graph()
   
# Create the nodes of the graph by using the State, Latitude, and Longtiude 
for state, val in capitals.items():
    #print(state, val[2])
    G.add_node(state, pos=(val[2],val[3]))

# Create the edges of the graph by using the Start, Destination, and Mileage     
for source in list(likely_routes):
    des = likely_routes[source]
    for target2, des in des.items():
        G.add_edge(source, target2, weight=des[0])
            #print("Start: {} ---> Destination: {}: Millage: {}".format(source, target2, des[0]))
            
            
# Plot the figure
weight = nx.get_edge_attributes(G, 'weight')
pos = nx.get_node_attributes(G, 'pos')

plt.figure(figsize=(150,150))
plt.title("Weighted Undirected Graph")
nx.draw_networkx(G,pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)

plt.show()

