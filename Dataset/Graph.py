import networkx as nx
from graph import likely_routes


class Edge:

    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def getEdgeDetails(self):
        return "Edge: {} <----{}---> {}".format(self.vertex1, self.weight, self.vertex2)


class Graph:

    def __init__(self):
        self.vertices = dict()

    def addEdge(self, edge, isDirected=False):

        if edge.vertex1 not in self.vertices:
            self.vertices[edge.vertex1] = []

        if not isDirected:
            if edge.vertex2 not in self.vertices:
                self.vertices[edge.vertex2] = []

        self.vertices[edge.vertex1].append((edge.vertex2, edge.weight))

        if not isDirected:
            self.vertices[edge.vetex2].append((edge.vertex1, edge.weight))

    def printGraph(self):
        print("Number of Vertices in Graph: ",
              len(self.vertices))
        print("Number of Edges in Graph: ",
              (len(self.vertices) * (len(self.vertices) - 1)))  # n(n−1)


def main():

    likely_routes = {
        "NY": {
            "MA": [170, "I-90"],
            "PA": [298, "I-87", "I-84", "I-81"],
            "CT": [113, "I-90", "I-91"],
            "NJ": [201, "I-87", "I-287"]},
        "MD": {
            "DE": [65, "US-50", "US-301"],
            "DC": [32, "US-50"]},
        "GA": {
            "SC": [214, "I-20"],
            "MS": [381, "I-20"],
            "AL": [161, "I-85"],
            "TN": [250, "I-75", "I-24"],
            "NC": [405, "I-85", "I-40"],
            "VA": [530, "I-85"],
            "FL": [373, "I-75", "I-10"]},
        "ME": {
            "MA": [167, "I-95"]},
        "TX": {
            "LA": [530, "I-35", "I-10"],
            "OK": [388, "I-35"],
            "AZ": [1059, "I-35", "I-10"],
            "NM": [992, "I-35", "I-40", "I-25"]},
        "LA": {
            "MS": [117, "I-12", "I-55"],
            "AL": [367, "I-10", "I-65"],
            "FL": [443, "I-10"]},
        "ND": {
            "MT": [703, "I-94", "I-90", "I-15"],
            "SD": [205, "US-83"],
            "MN": [435, "I-94"]},
        "ID": {
            "WA": [536, "I-84", "I-5"],
            "OR": [476, "I-84", "I-5"],
            "UT": [339, "I-84"]},
        "MA": {
            "NH": [68,  "I-93"],
            "CT": [101, "I-90", "I-84"],
            "RI": [59,  "I-90", "I-95"]},
        "NV": {
            "CA": [163, "I-580", "I-80"],
            "UT": [546, "I-580", "I-80"]},
        "WV": {
            "SC": [355, "I-64", "I-77"],
            "OH": [212, "I-77", "I-70"],
            "KY": [197, "I-64"],
            "PA": [366, "I-79", "I-68", "I-81"],
            "TN": [389, "I-64", "I-65"],
            "NC": [366, "I-64", "I-77", "I-40"],
            "VA": [317, "I-64"]},
        "WY": {
            "CO": [100, "I-25"],
            "MT": [699, "I-25", "I-90", "I-15"],
            "NE": [442, "I-80"],
            "SD": [694, "I-25", "I-90", "US-83"],
            "UT": [439, "I-80"],
            "KS": [631, "I-25", "I-70"]},
        "SC": {
            "KY": [458, "I-26", "I-40", "I-75"],
            "NC": [456, "I-20", "I-95", "I-40"],
            "FL": [203, "I-26", "I-95", "I-10"]},
        "OH": {
            "KY": [203, "I-71", "I-75", "I-64"],
            "PA": [368, "I-70", "I-76"],
            "IN": [176, "I-70"],
            "MI": [338, "I-70", "I-75", "I-96"]},
        "NH": {
            "VT": [116, "I-89"],
            "RI": [120, "I-93", "I-95"]},
        "CO": {
            "NE": [485, "I-76", "I-80"],
            "UT": [599, "I-70", "I-15"],
            "NM": [390, "I-25"],
            "KS": [542, "I-70"]},
        "IA": {
            "MO": [349, "I-35", "I-70"],
            "NE": [190, "I-80"],
            "WI": [354, "I-80", "I-88", "I-90"],
            "IL": [337, "I-80", "I-74", "I-55"],
            "MN": [248, "I-35"],
            "KS": [225, "I-35", "I-70"]},
        "DE": {
            "NJ": [106, "US-13", "I-95"]},
        "KY": {
            "IN": [165, "I-64", "I-65"],
            "MO": [445, "I-64", "I-70", "US-54"],
            "TN": [219, "I-64", "I-65"]},
        "PA": {
            "TN": [720, "I-81", "I-40"],
            "NJ": [130, "I-76"],
            "DC": [120, "I-83", "I-95"]},
        "CT": {
            "VT": [119, "I-91", "I-89"],
            "RI": [78,  "I-84", "US-44"],
            "NJ": [184, "I-91", "I-95"]},
        "MT": {
            "WA": [720, "I-15", "I-90", "I-5"],
            "SD": [856, "I-15", "I-90", "US-83"],
            "UT": [484, "I-15"]},
        "IN": {
            "MI": [255, "I-69"],
            "WI": [334, "I-65", "I-90"],
            "TN": [289, "I-65"],
            "IL": [212, "I-74", "I-72"]},
        "MS": {
            "AR": [347, "I-55", "I-40"],
            "AL": [248, "I-20", "US-80"],
            "IL": [588, "I-55"]},
        "MO": {
            "AR": [521, "I-70", "I-55", "I-40"],
            "IL": [221, "I-70", "I-55"],
            "KS": [219, "I-70"]},
        "MI": {
            "WI": [364, "I-69", "I-94", "I-90"],
            "IL": [391, "I-69", "I-94", "I-55"]},
        "NE": {
            "SD": [461, "I-80", "I-29", "I-90", "US-83"],
            "KS": [284, "I-80", "I-29", "I-70"]},
        "AR": {
            "TN": [349, "I-40"],
            "OK": [339, "I-40"]},
        "WI": {
            "IL": [264, "I-55", "I-39", "I-90"],
            "MN": [262, "I-94"]},
        "AL": {
            "TN": [280, "I-65"],
            "FL": [412, "I-65", "I-10"]},
        "TN": {
            "NC": [539, "I-40"]},
        "OK": {
            "AZ": [1007, "I-40", "I-17"],
            "NM": [603, "I-40", "I-25"],
            "KS": [293, "I-35", "I-335"]},
        "WA": {
            "OR": [159, "I-5"]},
        "AZ": {
            "CA": [755, "I-10", "I-5"],
            "UT": [663, "I-17", "I-15"],
            "NM": [527, "I-17", "I-40", "I-25"]},
        "SD": {
            "MN": [490, "US-80", "I-90", "I-35"]},
        "NC": {
            "VA": [208, "I-40", "I-95"]},
        "VA": {
            "DC": [108, "I-95"]},
        "CA": {
            "OR": [536, "I-5"],
            "UT": [649, "I-80"]},
        "NJ": {
            "DC": [182, "I-95"]},
    }

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
