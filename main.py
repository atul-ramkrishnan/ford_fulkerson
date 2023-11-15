import os
import random
from augmentation_strategy.BFS import BFS
from augmentation_strategy.Dijkstra import Dijkstra
from augmentation_strategy.ShortestAugmentingPath import ShortestAugmentingPath
from augmentation_strategy.DFSlike import DFSlike
from augmentation_strategy.MaximumCapacity import MaximumCapacity
from augmentation_strategy.Random import Random
from graph.Graph import Graph
from graph.GraphGenerator import GraphGenerator
from definitions import DATA_DIR
from FordFulkerson import FordFulkerson
from utilities.Metrics import Metrics


def print_metrics(max_flow, length_longest_acyclic_path, metrics):
    print(f"Max flow: {max_flow}")
    print(f"Longest acyclic path length: {length_longest_acyclic_path}")
    print(f"Number paths: {metrics.get_number_paths()}")
    print(f"Mean length: {metrics.get_mean_length()}")
    print(f"MPL: {metrics.get_mean_proportional_length()}")
    print(f"Total edges: {metrics.get_total_edges()}")


def main():
    n = 100
    r = 0.2
    upperCap = 2
    graphGenerator = GraphGenerator(n, r, upperCap)
    graph = graphGenerator.generate()
    
    # graph = Graph()
    # graph.load_from_csv(os.path.join(DATA_DIR, "simple_graph.csv"))
    # source = "S"
    source = str(random.randint(0, n))
    # # print(graph)
    bfs = BFS()
    longest_acyclic_path = bfs.get_longest_acyclic_path(graph, source)
    sink = longest_acyclic_path[-1]
    length_longest_acyclic_path = len(longest_acyclic_path)
    total_edges = len(graph.get_edges())
    metrics = Metrics(length_longest_acyclic_path, total_edges)

    strategies = [BFS(), Dijkstra(), ShortestAugmentingPath(), DFSlike(), MaximumCapacity(), Random()]

    for strategy in strategies:
        print(f"<-------- Strategy {strategy.__class__.__name__} -------->")
        ff = FordFulkerson(strategy=strategy)
        max_flow = ff.get_flow(graph, source, sink, metrics)
        print_metrics(max_flow, length_longest_acyclic_path, metrics)
        metrics.reset()

    # graph_params = [
    #     {'n': 100, 'r': 0.2, 'upperCap': 2},
    #     {'n': 200, 'r': 0.2, 'upperCap': 2},
    #     {'n': 100, 'r': 0.3, 'upperCap': 2},
    #     {'n': 200, 'r': 0.3, 'upperCap': 2},
    #     {'n': 100, 'r': 0.2, 'upperCap': 50},
    #     {'n': 200, 'r': 0.2, 'upperCap': 50},
    #     {'n': 100, 'r': 0.3, 'upperCap': 50},
    #     {'n': 200, 'r': 0.3, 'upperCap': 50}
    # ]

    # for graph_param in graph_params:
    #     graph_generator = GraphGenerator(graph_param['n'], graph_param['r'], graph_param['upperCap'])
    #     graph = graph_generator.generate()


if __name__ == "__main__":
    main()
