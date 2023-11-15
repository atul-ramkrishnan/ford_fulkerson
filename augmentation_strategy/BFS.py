from .AugmentationStrategy import AugmentationStrategy


class BFS(AugmentationStrategy):
    def get_augmenting_path(self, graph, source, sink):
        visited = [source]
        queue = [(source, [source])]

        while queue:
            m, path = queue.pop()
            for neighbour in graph.get_adjacent_vertices(m):
                if neighbour == sink:
                    return (path + [neighbour])
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append((neighbour, path + [neighbour]))

    def get_longest_acyclic_path(self, graph, source):
        visited = {}
        queue = [source]
        predecessors = {source: None}
        visited[source] = 0
        
        while queue:
            m = queue.pop()
            for neighbour in graph.get_adjacent_vertices(m):
                if neighbour not in visited:
                    visited[neighbour] = visited[m] + 1
                    predecessors[neighbour] = m
                    queue.append(neighbour)

        farthest_vertex = max(visited, key=visited.get)
        longest_acyclic_path = []
        current_vertex = farthest_vertex

        while current_vertex is not None:
            longest_acyclic_path.insert(0, current_vertex)
            current_vertex = predecessors[current_vertex]

        return longest_acyclic_path
