from graph.Graph import Graph
import os
from augmentation_strategy.BFS import BFS
from definitions import DATA_DIR
from augmentation_strategy.strategy_factory import strategy_factory


graph = Graph()
file = "test_graph.csv"
graph.load_from_csv(os.path.join(DATA_DIR, file))

source = "S"
bfs = BFS()
sink = "T"

strategy_sap = strategy_factory("sap")
path = strategy_sap.get_augmenting_path(graph, source, sink)
assert path == ['S', 'E', 'F', 'T'], "Incorrect augmenting path for SAP"

strategy_maxcap = strategy_factory("maxcap")
path = strategy_maxcap.get_augmenting_path(graph, source, sink)
assert path == ['S', 'E', 'B', 'C', 'D', 'T'], "Incorrect augmenting path for MaxCap"