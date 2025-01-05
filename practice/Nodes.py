class BaseNode:
    def __str__(self):
        return f"Node: {self.value}"

class ForwardNode(BaseNode):
    def __init__(self, value):
        self.value = value
        self.next = None
class TwoWayNode(BaseNode):
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None