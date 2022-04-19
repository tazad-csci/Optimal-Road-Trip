import networkx as nx
import seaborn as sns
import matplotlib.pyplot as plt
from data import likely_routes
%matplotlib inline
sns.set()

def main():

    # Add redundant elements to create a 2-way 2-dimensional dictionary
    for origin in list(likely_routes):
        data = likely_routes[origin]
        for target, data in data.items():
            if not target in likely_routes:
                likely_routes[target] = {}

            # Set distance and reverse the routes
            likely_routes[target][origin] = [data[0]]
            for route in reversed(list(enumerate(data))[1:]):
                likely_routes[target][origin].append(route)

    graph = nx.Graph()
    for source in list(likely_routes):
        des = likely_routes[source]
        for target2, des in des.items():
            graph.add_edge(source, target2, weight=des[0])

            #print("Started: {} ---> Destination: {}, Millage: {}".format(source, target2, des[0]))

    print("\nNumber of Vertices in Graph: ",
          graph.number_of_nodes())
    print("Number of Edges in Graph: ",
          graph.number_of_edges())
    print("Maximum Number of Edges in Undirected Graph: ",
          (graph.number_of_nodes() * (graph.number_of_nodes() - 1)))  # n(n−1)


if __name__ == '__main__':
    main()
