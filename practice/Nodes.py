class ForwardNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return f"Node: {self.value}"

class TwoWayNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None