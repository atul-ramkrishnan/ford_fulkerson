from augmentation_strategy.BFS import BFS
from Graph.Graph import Graph
from definitions import DATA_DIR
import os
from FordFulkerson import FordFulkerson


def main():
    graph = Graph()
    graph.load_from_csv(os.path.join(DATA_DIR, "simple_graph.csv"))
    # print(graph)
    bfs = BFS()
    ff = FordFulkerson(strategy=bfs)
    print(ff.get_flow(graph, "S", "T"))



if __name__ == "__main__":
    main()