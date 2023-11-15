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



def main():
    # n = 30
    # r = 0.2
    # upperCap = 2
    # graphGenerator = GraphGenerator(n, r, upperCap)
    # graph = graphGenerator.generate()
    # graph.save_as_csv(os.path.join(DATA_DIR, f"test_n_{n}_r_{r}_upperCap_{upperCap}.csv"))
    # bfs = BFS()
    # source = str(random.randint(0, n))
    # farthestVertex = bfs.get_farthest_vertex(graph, source) 
    # print(source, farthestVertex)

    graph = Graph()
    graph.load_from_csv(os.path.join(DATA_DIR, "simple_graph.csv"))
    # # print(graph)


    ff = FordFulkerson(strategy=BFS())
    print(ff.get_flow(graph, "S", "T"))

    ff = FordFulkerson(strategy=Dijkstra())    
    print(ff.get_flow(graph, "S", "T"))

    ff = FordFulkerson(strategy=ShortestAugmentingPath())
    print(ff.get_flow(graph, "S", "T"))

    ff = FordFulkerson(strategy=DFSlike())
    print(ff.get_flow(graph, "S", "T"))

    ff = FordFulkerson(strategy=MaximumCapacity())
    print(ff.get_flow(graph, "S", "T"))

    ff = FordFulkerson(strategy=Random())
    print(ff.get_flow(graph, "S", "T"))


if __name__ == "__main__":
    main()
