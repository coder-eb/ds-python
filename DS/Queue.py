from DS.Node import Node

class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = self.last = new_node
        self.length = 1
    
    def enqueue(self, value) -> None:
        new_node = Node(value)
        if self.length == 0:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        
        self.length += 1

    def dequeue(self) -> Node:
        if self.length == 0:
            return None
        
        prev_first = self.first
        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = prev_first.next
        
        self.length -= 1
        return prev_first

    def __str__(self) -> str:
        if self.length == 0:
            return "EMPTY"
        
        items_str = "FIRST"
        current_node = self.first
        while current_node:
            items_str += " => "
            value = current_node.value
            items_str += f"{value}"
            current_node = current_node.next

        return items_str