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
         
plt.axes([1.3, 1.3, 1.3, 1.3])
plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")        
plt.hist([v for k,v in nx.degree(G)])
