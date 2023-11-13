from augmentation_strategy.BFS import BFS
from Graph.Graph import Graph
from definitions import DATA_DIR
import os


def main():
    graph = Graph()
    graph.load_from_csv(os.path.join(DATA_DIR, "simple_graph.csv"))
    print(graph)
    # graph.save_as_csv(os.path.join(DATA_DIR, "simple_graph_saved.csv"))
    # print(graph.get_adjacent_vertices("0"))
    bfs = BFS()
    res = bfs.execute(graph, "0", "5")
    print(res)

if __name__ == "__main__":
    main()