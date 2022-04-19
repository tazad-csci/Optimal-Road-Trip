from Data import likely_routes
from Graph import G


def main():
    print("\nNumber of Vertices in Graph: ",
          G.number_of_nodes())
    print("Number of Edges in Graph: ",
          G.number_of_edges())
    print("Degree of each node in Graph: ",
          G.degree)
    print("Maximum Number of Edges in Undirected Graph: ",
          (G.number_of_nodes() * (G.number_of_nodes() - 1)))  # n(n−1)
 

if __name__ == '__main__':
    main()
