from .AugmentationStrategy import AugmentationStrategy


class BFS(AugmentationStrategy):
    def getAugmentingPath(self, graph, source, sink):
        visited = [source]
        queue = [(source, [source])]

        while queue:
            m, path = queue.pop()
            for neighbour in graph.get_adjacent_vertices(m):
                if neighbour[0] == sink:
                    return (path + [neighbour[0]])
                if neighbour[0] not in visited:
                    visited.append(neighbour[0])
                    queue.append((neighbour[0], path + [neighbour[0]]))
