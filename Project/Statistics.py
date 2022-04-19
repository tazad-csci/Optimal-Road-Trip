#***************************************************************#
#Purpose: Summary of statistics that describe the graph/network we have constructed;


#***************************************************************#

import networkx as nx
import matplotlib.pyplot as plt
from Graph import G


    
def Basic_Info(G):
    
    print("\nGraph with {} nodes and {} edges".format(G.number_of_nodes(),G.number_of_edges()))
    print("Degree of each node in Graph: ", {node:val for (node, val) in G.degree()})
    print("Maximum Number of Edges in Undirected Graph: ",(G.number_of_nodes() * (G.number_of_nodes() - 1)))  # n(n−1)
    
    
def Density(G):    
    
    # A number that measures how interconnected a graph is
    print("Destiny: ", nx.density(G))

    
def Transitivity(G):
    
    # Ratio of all triangles over possible triangles; measures how interconnected a graph is
    print('Transitivity:', nx.transitivity(G))  
    
    
def plot_deg_dist(G):
    
    all_degrees = [v for k, v in nx.degree(G)]    #all the degrees
    unique_degrees = list(set(all_degrees))       #all the unique degrees

    count_of_degrees = []
    for i in range(0,max(unique_degrees)):
        x = all_degrees.count(i)
        count_of_degrees.append(x)

    #Degrees distribution line graph
    f = plt.figure(1)
    plt.plot(unique_degrees, count_of_degrees)   
    plt.title("Degree Distribution")
    plt.ylabel("Number of Nodes")
    plt.xlabel("Degrees")  
    f.show()
    plt.show()
    
    #Degrees distribution Histogram
    g = plt.figure(2)
    plt.title("Degrees Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degrees")        
    plt.hist([v for k,v in nx.degree(G)])
    g.show()
    plt.show()
    
    
def plot_betweenness_centrality(G):
    
    # Run Betweenness Centrality
    betweenness_dict = nx.betweenness_centrality(G)
    sorted_betweenness = sorted(betweenness_dict.items(),key=lambda elem: elem[1], reverse=True)

    print('\n\nTop 20 Captials by betweenness centrality')
    for b in sorted_betweenness[:20]:
        print(b)
    
    plt.hist(nx.centrality.betweenness_centrality(G).values())
    plt.title("Betweenness Centrality")
    plt.show()
    
    
def plot_eigenvector_centrality(G):   
    
    
    print('\nCaptials by eigenvector centrality')
    most_important_link = nx.eigenvector_centrality(G)
    for w in sorted(most_important_link, key=most_important_link.get, reverse=True):
        print(w,most_important_link[w])
    
    
def plot_degree_centrality(G):    
    
    
    print('\nCaptials by degree centrality')
    most_influential = nx.degree_centrality(G)
    for w in sorted(most_influential, key=most_influential.get, reverse=True):
        print(w,most_influential[w])
        
    plt.hist(nx.degree_centrality(G).values())
    plt.title("Degree Centrality")
    plt.show()

    
def main():
    
    Basic_Info(G)
    Density(G)
    Transitivity(G)
    plot_deg_dist(G) 
    plot_betweenness_centrality(G)
    plot_eigenvector_centrality(G)
    plot_degree_centrality(G)


if __name__ == '__main__':
    main()
    
