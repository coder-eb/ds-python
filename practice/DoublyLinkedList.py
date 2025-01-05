from practice.Nodes import TwoWayNode as Node 
from practice.BaseLinkedList import BaseLinkedList

class DoublyLinkedList(BaseLinkedList):
    def __init__(self, value):
        self.head = self.tail = Node(value)
        self.length = 0
    
    def append(self, value) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            prev_tail = self.tail
            new_node.prev = prev_tail
            prev_tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True



