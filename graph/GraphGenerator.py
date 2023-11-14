import random
from .Graph import Graph


class GraphGenerator:
    def __init__(self, n, r, upperCap):
        self.n = n
        self.r = r
        self.upperCap = upperCap
    
    def _squared_euclidean_distance(self, point1, point2):
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    
    def _connect_vertices(self, graph, vertex_coordinates):
        for from_vertex in vertex_coordinates:
            for to_vertex in vertex_coordinates:
                if ((from_vertex != to_vertex) and 
                (self._squared_euclidean_distance(vertex_coordinates[from_vertex], vertex_coordinates[to_vertex]) <= self.r**2)):
                    rand = random.uniform(0, 1)
                    if rand < 0.5:
                        if not (graph.has_edge(str(from_vertex), str(to_vertex)) or graph.has_edge(str(to_vertex), str(from_vertex))):
                            graph.add_edge(str(from_vertex), str(to_vertex), random.randint(1, self.upperCap))
                    else:
                        if not (graph.has_edge(str(from_vertex), str(to_vertex)) or graph.has_edge(str(to_vertex), str(from_vertex))):
                            graph.add_edge(str(to_vertex), str(from_vertex), random.randint(1, self.upperCap))
                
    def generate(self):
        graph = Graph()
        vertex_coordinates = {}
        for i in range(self.n):
            graph.add_vertex(str(i))
            vertex_coordinates[i] = (random.uniform(0, 1), random.uniform(0, 1))

        self._connect_vertices(graph, vertex_coordinates)

        return graph
