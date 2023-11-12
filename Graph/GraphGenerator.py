import Graph


class GraphGenerator:
    def __init__(self, n: int, r: float, upperCap: float) -> None:
        self.n = n
        self.r = r
        self.upperCap = upperCap
    
    def generate(self) -> Graph:
