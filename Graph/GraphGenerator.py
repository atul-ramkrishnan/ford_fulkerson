import random
from Graph import Graph


class GraphGenerator:
    def __init__(self, n, r, upperCap):
        self.n = n
        self.r = r
        self.upperCap = upperCap
    
    def _euclidean_distance(self, point1, point2):
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
    
    def _connect_vertices(self, graph, vertex_coordinates):
        for from_vertex in vertex_coordinates:
            for to_vertex in vertex_coordinates:
                print(f"{from_vertex} --> {to_vertex}")
                if from_vertex < to_vertex and self._euclidean_distance(vertex_coordinates[from_vertex], vertex_coordinates[to_vertex]) < self.r:
                    graph.add_edge(from_vertex, to_vertex, random.randint(1, self.upperCap))

    def generate(self, directed=True):
        graph = Graph(directed)
        vertex_coordinates = {}
        for i in range(self.n):
            graph.add_vertex(i)
            vertex_coordinates[i] = (random.uniform(0, 1), random.uniform(0, 1))

        self._connect_vertices(graph, vertex_coordinates)

        return graph
    

# graph_generator = GraphGenerator(100, 0.2, 2)
# graph = graph_generator.generate(directed=True)
# print(graph)
# graph.save_as_csv("test1.csv")

graph = Graph()
graph.load_from_csv("test1.csv")
graph.save_as_csv("test2.csv")