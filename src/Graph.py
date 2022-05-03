#***************************************************************#
#Purpose: This code plots the undirected weighted graph figure


#***************************************************************#

import networkx as nx
import matplotlib.pyplot as plt
from Data import all_routes, capitals, likely_routes

G = nx.Graph()
#G = nx.random_geometric_graph(20, radius=0.4, seed=3)

# Create the nodes of the graph by using the State, Latitude, and Longtiude 
for state, val in capitals.items():
    #print(state, val[2])
    G.add_node(state,label="This is the state of {}".format(val[1]))

# Create the edges of the graph by using the Start, Destination, and Mileage     
for source in list(all_routes):
    des = all_routes[source]
    for target2, des in des.items():
        G.add_edge(source, target2, weight=des[0])
            #print("Start: {} ---> Destination: {}: Millage: {}".format(source, target2, des[0]))            
        
# Plot the figure
#weight = nx.get_edge_attributes(G, 'weight')
#nx.draw_networkx_edge_labels(G,pos=pos, edge_labels=weight)
plt.figure(figsize=(25,25))
plt.title("Complete Graph of US Capitals")
pos = nx.spring_layout(G, seed=675)
nx.draw(G,pos=pos)
nx.draw_networkx_labels(G,pos=pos)
plt.show()
