import csv


class Graph:
    def __init__(self, directed=True):
        self.adj_list = {}
        self.directed = directed

    def reset_graph(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        # Ensure that the vertex is not already in the adjacency list
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight=1):        
        self.adj_list[from_vertex].append((to_vertex, weight))
        
        # If the graph is undirected, add an edge from the to_vertex back to the from_vertex
        if not self.directed:
            self.adj_list[to_vertex].append((from_vertex, weight))

    def remove_edge(self, from_vertex, to_vertex):
        # Remove edge from the from_vertex
        self.adj_list[from_vertex] = [(vertex, weight) for vertex, weight in self.adj_list[from_vertex] if vertex != to_vertex]
        
        # If the graph is undirected, remove the reverse edge too
        if not self.directed:
            self.adj_list[to_vertex] = [(vertex, weight) for vertex, weight in self.adj_list[to_vertex] if vertex != from_vertex]

    def remove_vertex(self, vertex):
        # Remove all edges to this vertex
        for from_vertex, edges in self.adj_list.items():
            self.adj_list[from_vertex] = [(to_vertex, weight) for to_vertex, weight in edges if to_vertex != vertex]
        
        # Remove the vertex from the adjacency list
        if vertex in self.adj_list:
            del self.adj_list[vertex]

    def get_adjacent_vertices(self, vertex):
        return self.adj_list[vertex]
    
    def get_vertices(self):
        return self.adj_list.keys()
    
    def get_edges(self):
        # Get all edges in the graph
        edges = []
        for from_vertex, to_vertices in self.adj_list.items():
            for to_vertex, weight in to_vertices:
                if self.directed or (to_vertex, from_vertex, weight) not in edges:
                    edges.append((from_vertex, to_vertex, weight))
        return edges

    def save_as_csv(self, filename):
        with open(filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Source', 'Target', 'Weight'])
            for source, edges in self.adj_list.items():
                for target, weight in edges:
                    writer.writerow([source, target, weight])

    def load_from_csv(self, filename, overwrite=False):
        if overwrite:
            self.reset_graph()
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                source, target, weight = row
                weight = int(weight)
                self.add_vertex(source)
                self.add_edge(source, target, weight)

    def __str__(self):
        # For printing the graph's adjacency list
        return '\n'.join([f'{vertex}: {neighbors}' for vertex, neighbors in self.adj_list.items()])

# graph = Graph(directed=False)
# graph.add_vertex('A')
# graph.add_vertex('B')
# graph.add_vertex('C')
# graph.add_edge('A', 'B', 1)
# graph.add_edge('A', 'C', 2)
# graph.add_edge('B', 'C', 3)
# graph.add_edge('A', 'B', 2)

# print(graph)