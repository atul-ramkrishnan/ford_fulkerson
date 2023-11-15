import os
import random
from augmentation_strategy.BFS import BFS
from augmentation_strategy.Dijkstra import Dijkstra
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


if __name__ == "__main__":
    main()
