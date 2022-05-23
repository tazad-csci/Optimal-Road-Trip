#***************************************************************#
#Purpose: Summary of statistics that describe the graph/network we have constructed;


#***************************************************************#

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from Data import all_routes, capitals
from Graph import G
import os 

v = list(set(G.nodes))
    
def Basic_Info(G):
    
    print("\nGraph with {} nodes and {} edges".format(G.number_of_nodes(),G.number_of_edges()))
       
    
def Average_Shortest_Path(G):
    
    print("average_shortest_path_length: ", nx.average_shortest_path_length(G,weight='weight'))

    
def Average_Clustering(G):
    
    # Ratio of all triangles over possible triangles; measures how interconnected a graph is
    print('Average Clustering:', nx.average_clustering(G,weight='weight'))      
    

def Clustering(G):
    
    # Ratio of all triangles over possible triangles; measures how interconnected a graph is
    #print('Clustering:', nx.clustering(G,weight='weight'))  
    gc = G.subgraph(max(nx.connected_components(G)))

    closeness_dict = nx.clustering(G,weight='weight')
    sorted_closeness = sorted(closeness_dict.items(), key=lambda elem: elem[1], reverse=True)
    
    print('\nTop 20 Capitals by clustering')
    for b in sorted_closeness[:20]:
        print(b)
    
    lcc = nx.clustering(G,weight='weight')
    
    cmap = plt.get_cmap('autumn')
    norm = plt.Normalize(0, max(lcc.values()))
    node_colors = [cmap(norm(lcc[node])) for node in gc.nodes]

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 4))
    nx.draw_spring(gc, node_color=node_colors, with_labels=True, ax=ax1)
    fig.colorbar(ScalarMappable(cmap=cmap, norm=norm), label='Clustering', shrink=0.95, ax=ax1)

    ax2.hist(lcc.values(), bins=10)
    ax2.set_title('Clustering')
    ax2.set_xlabel('Clustering')
    ax2.set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()    
    
    
def Closeness_Centrality(G):
    
    gc = G.subgraph(max(nx.connected_components(G)))
    lcc = nx.closeness_centrality(G,distance='weight')

    closeness_dict = nx.closeness_centrality(G,distance='weight')
    sorted_closeness = sorted(closeness_dict.items(), key=lambda elem: elem[1], reverse=True)
    
    print('\nTop 20 Capitals by closeness')
    for b in sorted_closeness[:20]:
        print(b)
    
    
    cmap = plt.get_cmap('autumn')
    norm = plt.Normalize(0, max(lcc.values()))
    node_colors = [cmap(norm(lcc[node])) for node in gc.nodes]
    
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 4))
    nx.draw_spring(gc, node_color=node_colors, with_labels=True, ax=ax1)
    fig.colorbar(ScalarMappable(cmap=cmap, norm=norm), label='Centrality', shrink=0.95, ax=ax1)
    
    ax2.hist(lcc.values(), bins=10)
    ax2.set_title('Closeness Centrality')
    ax2.set_xlabel('Closeness')
    ax2.set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()   
    
    
def Betweenness_Centrality(G):
    
    gc = G.subgraph(max(nx.connected_components(G)))
    lcc = nx.betweenness_centrality(G,weight='weight')

    cmap = plt.get_cmap('autumn')
    norm = plt.Normalize(0, max(lcc.values()))
    node_colors = [cmap(norm(lcc[node])) for node in gc.nodes]
    
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 4))
    nx.draw_spring(gc, node_color=node_colors, with_labels=True, ax=ax1)
    fig.colorbar(ScalarMappable(cmap=cmap, norm=norm), label='Centrality', shrink=0.95, ax=ax1)
    
    ax2.hist(lcc.values(), bins=10)
    ax2.set_title('Betweenness Centrality')
    ax2.set_xlabel('Betweenness')
    ax2.set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()   
    


    
def Nearest_Neighbor(starting_captial):
    
    G_deep = G.copy()
    unvisited_capitals = set()
    path = [starting_captial]
    mileage = 0
    
    for i in v:
        if i != starting_captial:
            unvisited_capitals.add(i)

    current_captial = starting_captial
    
    for i in range(0,len(unvisited_capitals)):

        list_of_edges = list(G_deep.edges(current_captial, data="weight"))            
        nearest_neighbor = min(list_of_edges, key = lambda t: t[2])
        
        mileage = mileage + nearest_neighbor[2]        

        for i in unvisited_capitals:
            G_deep.remove_edge(current_captial, i)
        
        
        current_captial = nearest_neighbor[1]
        path.append(current_captial)
        unvisited_capitals.remove(current_captial)
           
    index1 = 0
    index2 = 1
    
    while (index2 != 49):
        info = all_routes[path[index1] ][ path[index2] ]
        route_taken = info[1:]
        start_dest_capital = capitals[ path[index1] ][0]
        start_dest_state = capitals[ path[index1] ][1]
        end_dest_capital = capitals[ path[index2] ][0]
        end_dest_state = capitals[ path[index2] ][1]
        
        
    
        index1, index2 = index1+1, index2+1
                
            
    return mileage

    
    
def Mileage(G):
    
    capital_miles = []
    list_capitals = list(G.nodes)

    for capital in G.nodes:

        miles = Nearest_Neighbor(capital)
        capital_miles.append(miles)    
    
    x = list_capitals
    y = capital_miles
    plt.bar(x,y,color=['black', 'red', 'green', 'blue', 'cyan'])

    plt.title("Total Mileage To Travel")
    plt.xlabel('States')
    plt.ylabel("Miles")
    plt.show()
    
    
def main():
    
    Basic_Info(G)
    Clustering(G)
    Average_Clustering(G)
    Average_Shortest_Path(G)
    Closeness_Centrality(G)   
    Betweenness_Centrality(G)
    Mileage(G)
    os.system('Interface.py')

    print('----------------------------------------------------------------------')
    
if __name__ == '__main__':
    main()
    
