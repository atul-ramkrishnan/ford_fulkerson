class Edge:
    def __init__(self, capacity, flow=0):
        self.capacity = capacity
        self.flow = flow

    def get_flow(self):
        return self.flow
    
    def set_flow(self, flow):
        self.flow = flow

    def get_capacity(self):
        return self.capacity
    
    def set_capacity(self, capacity):
        self.capacity = capacity
        
    def __repr__(self):
        return f"Edge(capacity={self.capacity}, flow={self.flow})"
