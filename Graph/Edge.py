class Edge:
    def __init__(self, capacity, flow=0):
        self.capacity = capacity
        self.flow = flow

    def __repr__(self):
        return f"Edge(capacity={self.capacity}, flow={self.flow})"

class Graph:
    def __init__(self):
        self.adj_list = {}

    def reset_graph(self):
        self.adj_list.clear()

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = {}

    def add_edge(self, from_vertex, to_vertex, capacity):
        if from_vertex not in self.adj_list:
            self.add_vertex(from_vertex)
        if to_vertex not in self.adj_list:
            self.add_vertex(to_vertex)
        # Each edge is now stored with an Edge instance
        self.adj_list[from_vertex][to_vertex] = Edge(capacity)

    def remove_edge(self, from_vertex, to_vertex):
        if to_vertex in self.adj_list[from_vertex]:
            del self.adj_list[from_vertex][to_vertex]

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            # Remove all edges from this vertex
            del self.adj_list[vertex]
            # Remove all edges to this vertex
            for from_vertex in self.adj_list:
                if vertex in self.adj_list[from_vertex]:
                    del self.adj_list[from_vertex][vertex]

    def get_adjacent_vertices(self, vertex):
        return list(self.adj_list[vertex].keys())

    def get_vertices(self):
        return list(self.adj_list.keys())

    def get_edges(self):
        edges = []
        for from_vertex, to_vertices in self.adj_list.items():
            for to_vertex, edge in to_vertices.items():
                edges.append((from_vertex, to_vertex, edge.capacity, edge.flow))
        return edges

    def save_as_csv(self, filename):
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Source', 'Target', 'Capacity', 'Flow'])
            for source, targets in self.adj_list.items():
                for target, edge in targets.items():
                    writer.writerow([source, target, edge.capacity, edge.flow])

    def load_from_csv(self, filename):
        self.reset_graph()
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
            for row in reader:
                source, target, capacity, flow = row
                self.add_edge(source, target, int(capacity))
                self.adj_list[source][target].flow = int(flow)

    def __str__(self):
        return '\n'.join([f'{vertex}: {neighbors}' for vertex, neighbors in self.adj_list.items()])

# The Edge class now stores both capacity and flow.
# The Graph class has been refactored to use the Edge class for storing edges.
# The add_edge, remove_edge, and remove_vertex methods have been updated accordingly.
# The save_as_csv and load_from_csv methods have been updated to handle the Edge class.
# The __str__ method and other methods have been adapted to the new representation of edges.
