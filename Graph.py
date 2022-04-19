import networkx as nx
from Data import likely_routes

G = nx.Graph()
    
for source in list(likely_routes):
    des = likely_routes[source]
    for target2, des in des.items():
        G.add_edge(source, target2, weight=des[0])
            #print("Started: {} ---> Destination: {}, Millage: {}".format(source, target2, des[0]))
