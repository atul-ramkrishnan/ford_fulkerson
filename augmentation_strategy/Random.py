import heapq
import random
from .AugmentationStrategy import AugmentationStrategy


class Random(AugmentationStrategy):
    def _relax(self, u, v, w, distance, predecessors):
        if distance[v] > distance[u] + w:
            distance[v] = distance[u] + w
            predecessors[v] = u
            return True
        return False
    
    def get_augmenting_path(self, graph, source, sink):
        distance = {vertex:float('inf') for vertex in graph.get_vertices()}
        distance[source] = 0
        Q = [(0, source)]
        heapq.heapify(Q)
        predecessors = {source: None}
        visited = set()

        while Q:
            u_distance, u = heapq.heappop(Q)
            # print(sink, u)
            if u == sink:
                break

            if u in visited:
                continue
            visited.add(u)

            for v in graph.get_adjacent_vertices(u):
                if self._relax(u, v, random.uniform(0, 1), distance, predecessors):
                    heapq.heappush(Q, (distance[v], v))

        if sink not in predecessors:
            return None

        path = []
        current_vertex = sink
        while current_vertex is not None:
            path.insert(0, current_vertex)
            current_vertex = predecessors[current_vertex]

        return path
