from augmentation_strategy.BFS import BFS
from graph.Graph import Graph
from graph.GraphGenerator import GraphGenerator
from definitions import DATA_DIR
import os
from FordFulkerson import FordFulkerson


def main():
    # graph = Graph()
    # graph.load_from_csv(os.path.join(DATA_DIR, "simple_graph.csv"))
    # # print(graph)
    # bfs = BFS()
    # ff = FordFulkerson(strategy=bfs)
    # print(ff.get_flow(graph, "S", "T"))
    # test_dict = {}
    # print(test_dict is not None)
    n = 100
    r = 0.2
    upperCap = 2
    graphGenerator = GraphGenerator(n, r, upperCap)
    graph = graphGenerator.generate()
    graph.save_as_csv(os.path.join(DATA_DIR, "test_new_graph_gen.csv"))



if __name__ == "__main__":
    main()