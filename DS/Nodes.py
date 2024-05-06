def get_formatted_value(value) -> str:
    return f"The current node is: {value}"

class ForwardNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return get_formatted_value(self.value)
    
class TwoWayNode:
    def __init__(self, value):
        self.value = value
        self.prev = self.next = None

    def __str__(self) -> str:
        return get_formatted_value(self.value)