from DS.Nodes import ForwardNode as Node

class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def push(self, value) -> None:
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height+=1
    
    def pop(self) -> Node:
        if self.height == 0:
            return None

        prev_top = self.top
        if self.height == 1:
            self.top = None
        else:
            self.top = prev_top.next

        self.height-=1
        return prev_top
    

    def __str__(self) -> str:
        if self.height == 0:
            return "EMPTY"
        
        items_str = "TOP"
        current_node = self.top
        while current_node:
            items_str += " => "
            value = current_node.value
            items_str += f"{value}"
            current_node = current_node.next

        return items_str