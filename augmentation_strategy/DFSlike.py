import heapq
import sys
from .AugmentationStrategy import AugmentationStrategy


class DFSlike(AugmentationStrategy):
    def __init__(self):
        self.counter = sys.maxsize

    def _get_counter(self):
        return self.counter
    
    def _decrement_counter(self):
        self.counter -= 1
    
    def _relax(self, u, v, distance, predecessors):
        if distance[v] == float('inf'):
            distance[v] = self._get_counter()
            self._decrement_counter()
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
                print(f"{u} --> {v}")             
                if self._relax(u, v, distance, predecessors):
                    heapq.heappush(Q, (distance[v], v))

        if sink not in predecessors:
            return None

        path = []
        current_vertex = sink
        while current_vertex is not None:
            path.insert(0, current_vertex)
            current_vertex = predecessors[current_vertex]

        return path
