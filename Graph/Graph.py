import csv
import ast


class Graph:
    def __init__(self):
        self.adj_list = {}

    def reset_graph(self):
        self.adj_list.clear()

    def add_vertex(self, vertex):
        # Ensure that the vertex is not already in the adjacency list
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight=1):        
        self.adj_list[from_vertex].append((to_vertex, weight))

    def remove_edge(self, from_vertex, to_vertex):
        # Remove edge from the from_vertex
        self.adj_list[from_vertex] = [(vertex, weight) for vertex, weight in self.adj_list[from_vertex] if vertex != to_vertex]

    def remove_vertex(self, vertex):
        # Remove all edges to this vertex
        for from_vertex, edges in self.adj_list.items():
            self.adj_list[from_vertex] = [(to_vertex, weight) for to_vertex, weight in edges if to_vertex != vertex]
        
        # Remove the vertex from the adjacency list
        if vertex in self.adj_list:
            del self.adj_list[vertex]

    def get_adjacent_vertices(self, vertex):
        if vertex in self.adj_list:
            return self.adj_list[vertex]
        else:
            raise Exception("Vertex not in graph.")
    
    def get_vertices(self):
        return self.adj_list.keys()
    
    def get_edges(self):
        # Get all edges in the graph
        edges = []
        for from_vertex, to_vertices in self.adj_list.items():
            for to_vertex, weight in to_vertices:
                if (to_vertex, from_vertex, weight) not in edges:
                    edges.append((from_vertex, to_vertex, weight))
        return edges

    def save_as_csv(self, filename, overwrite=True):
        write_mode = 'w' if overwrite else 'a'
        with open(filename, write_mode) as csv_file:
            writer = csv.writer(csv_file)
            for source, edges in self.adj_list.items():
                data = [source]
                for target, weight in edges:
                    data.append((target, weight))
                writer.writerow(data)

    def load_from_csv(self, filename, overwrite=True):
        if overwrite:
            self.reset_graph()
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                source = row[0]
                self.add_vertex(source)
                for col in range(1, len(row)):
                    target, weight = ast.literal_eval(row[col])
                    self.add_edge(source, target, weight)

    def __str__(self):
        # For printing the graph's adjacency list
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