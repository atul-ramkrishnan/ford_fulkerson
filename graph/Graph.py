import csv
from .Edge import Edge

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

    def get_flow(self, from_vertex, to_vertex):
        return self.adj_list[from_vertex][to_vertex].get_flow()
    
    def set_flow(self, from_vertex, to_vertex, flow):
        self.adj_list[from_vertex][to_vertex].set_flow(flow)

    def add_flow(self, from_vertex, to_vertex, delta):
        self.set_flow(from_vertex, to_vertex, self.get_flow(from_vertex, to_vertex) + delta)

    def get_capacity(self, from_vertex, to_vertex):
        return self.adj_list[from_vertex][to_vertex].get_capacity()

    def get_adjacent_vertices(self, vertex):
        return list(self.adj_list[vertex].keys())

    def get_vertices(self):
        return list(self.adj_list.keys())
    
    def has_edge(self, from_vertex, to_vertex):
        return from_vertex in self.adj_list and to_vertex in self.adj_list[from_vertex]
    
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
            for source in self.get_vertices():
                if source in self.adj_list and self.adj_list[source]:
                    for target, edge in self.adj_list[source].items():
                        writer.writerow([source, target, edge.capacity, edge.flow])
                else:
                    writer.writerow([source, None, None, None])

    def load_from_csv(self, filename):
        self.reset_graph()
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)  # Skip the header
            for row in reader:
                source = row[0]
                self.add_vertex(source)
                if row[1]:
                    target, capacity, flow = row[1], int(row[2]), int(row[3])
                    self.add_edge(source, target, capacity)
                    self.adj_list[source][target].flow = flow

    def __str__(self):
        return '\n'.join([f'{vertex}: {neighbors}' for vertex, neighbors in self.adj_list.items()])

# graph = Graph()
# graph.add_vertex('A')
# graph.add_vertex('B')
# graph.add_vertex('C')
# graph.add_edge('A', 'B', 1)
# graph.add_edge('A', 'C', 2)
# graph.add_edge('B', 'C', 3)
# graph.add_edge('A', 'B', 2)

# print(graph)