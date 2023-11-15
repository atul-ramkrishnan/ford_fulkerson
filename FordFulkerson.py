from graph.Graph import Graph


class FordFulkerson:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def _initialize_flow(self, graph):
        for from_vertex in graph.get_vertices():
            for to_vertex in graph.get_adjacent_vertices(from_vertex):
                graph.set_flow(from_vertex, to_vertex, 0)

    def _get_residual_graph(self, graph):
        residual_graph = Graph()

        for vertex in graph.get_vertices():
            residual_graph.add_vertex(vertex)

        for from_vertex in graph.get_vertices():
            for to_vertex in graph.get_adjacent_vertices(from_vertex):
                    capacity = graph.get_capacity(from_vertex, to_vertex)
                    flow = graph.get_flow(from_vertex, to_vertex)

                    if capacity > flow:
                        residual_graph.add_edge(from_vertex, to_vertex, capacity - flow)

                    if flow > 0:
                        residual_graph.add_edge(to_vertex, from_vertex, flow)
        
        return residual_graph

    def _get_bottleneck_capacity(self, path, residual_graph):
        path = list(zip(path[:-1], path[1:]))
        return min(residual_graph.get_capacity(from_vertex, to_vertex) for from_vertex, to_vertex in path)

    def _augment_flow(self, path, residual_graph, graph):
        bottleneck_capacity = self._get_bottleneck_capacity(path, residual_graph)
        for from_vertex, to_vertex in list(zip(path[:-1], path[1:])):
            if graph.has_edge(from_vertex, to_vertex):
                graph.add_flow(from_vertex, to_vertex, bottleneck_capacity)
            else:
                graph.add_flow(to_vertex, from_vertex, -bottleneck_capacity)

    def _get_total_flow(self, graph, source):
        return sum(graph.get_flow(source, neighbour) for neighbour in graph.get_adjacent_vertices(source))

    def get_flow(self, graph, source, sink):
        self._initialize_flow(graph)
        path = self.strategy.get_augmenting_path(self._get_residual_graph(graph), source, sink)
        while path:
            self._augment_flow(path, self._get_residual_graph(graph), graph)
            path = self.strategy.get_augmenting_path(self._get_residual_graph(graph), source, sink)

        return self._get_total_flow(graph, source)
