from .AugmentationStrategy import BFS, DFSlike, Dijkstra, MaximumCapacity, Random, ShortestAugmentingPath

def strategy_factory(self, strategy):
    if strategy.lower() == "normal" or strategy.lower() == "bfs":
        return BFS()
    elif strategy.lower() == "dfslike":
        return DFSlike()
    elif strategy.lower() == "dijkstra":
        return Dijkstra()
    elif strategy.lower() == "maxcap" or strategy.lower() == "maximumcapacity":
        return MaximumCapacity()
    elif strategy.lower() == "sap" or strategy.lower() == "shortestaugmentingpath":
        return ShortestAugmentingPath()
    elif strategy.lower() == "random":
        return Random()
    else:
        raise ValueError(f"Unknown strategy type: {strategy}")