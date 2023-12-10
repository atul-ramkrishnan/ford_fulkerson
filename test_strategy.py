from graph.Graph import Graph
import os
from augmentation_strategy.BFS import BFS
from definitions import DATA_DIR
from augmentation_strategy.strategy_factory import strategy_factory


graph = Graph()
file = "test_graph.csv"
graph.load_from_csv(os.path.join(DATA_DIR, file))
strategy = strategy_factory("dfslike")
source = "S"
bfs = BFS()
sink = "T"

path = strategy.get_augmenting_path(graph, source, sink)
print(path)