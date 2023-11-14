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

    def get_farthest_vertex(self, graph, source):
        visited = {}
        queue = [source]
        visited[source] = 0
        while queue:
            m = queue.pop()
            for neighbour in graph.get_adjacent_vertices(m):
                if neighbour not in visited:
                    visited[neighbour] = visited[m] + 1
                    queue.append(neighbour)
        return max(visited, key=visited.get)
