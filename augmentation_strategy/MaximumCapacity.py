import heapq
from .AugmentationStrategy import AugmentationStrategy


class MaximumCapacity(AugmentationStrategy):
    def _relax(self, u, v, w, distance, predecessors):
        if distance[v] < min(distance[u], w):
            distance[v] = min(distance[u], w)
            predecessors[v] = u
            return True
        return False
    
    def get_augmenting_path(self, graph, source, sink):
        distance = {vertex:float('-inf') for vertex in graph.get_vertices()}            
        distance[source] = float('inf')
        Q = [(float('-inf'), source)]
        heapq.heapify(Q)
        predecessors = {source: None}
        visited = set()

        while Q:
            u_distance, u = heapq.heappop(Q)
            u_distance = -u_distance
            # print(sink, u)
            if u == sink:
                break

            if u in visited:
                continue
            visited.add(u)

            for v in graph.get_adjacent_vertices(u):
                if self._relax(u, v, graph.get_capacity(u, v), distance, predecessors):
                    heapq.heappush(Q, (-distance[v], v))

        if sink not in predecessors:
            return None

        path = []
        current_vertex = sink
        while current_vertex is not None:
            path.insert(0, current_vertex)
            current_vertex = predecessors[current_vertex]

        return path
