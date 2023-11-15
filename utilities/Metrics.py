class Metrics:
    def __init__(self, length_longest_acyclic_path, total_edges):
        self.path_lengths = []
        self.length_longest_acyclic_path = length_longest_acyclic_path
        self.total_edges = total_edges
    
    def reset(self):
        self.path_lengths.clear()
    
    def get_number_paths(self):
        return len(self.path_lengths)

    def get_mean_length(self):
        return sum(self.path_lengths) / len(self.path_lengths)

    def get_mean_proportional_length(self):
        self.get_mean_length() / self.length_longest_acyclic_path

    def get_total_edges(self):
        return self.total_edges

    def add_path_length(self, path):
        self.path_lengths.append(len(path))
