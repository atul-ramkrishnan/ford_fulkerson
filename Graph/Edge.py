class Edge:
    def __init__(self, capacity, flow=0):
        self.capacity = capacity
        self.flow = flow

    def __repr__(self):
        return f"Edge(capacity={self.capacity}, flow={self.flow})"