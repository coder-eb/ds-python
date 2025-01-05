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

    def pop(self) -> Node|None:
        if self.length == 0:
            return None

        prev_tail = self.tail        
        if self.length == 1:
            self.head = self.tail = None
        else:
            new_tail = prev_tail.prev
            new_tail.next = None
            self.tail = new_tail

        self.length -= 1
        return prev_tail

    def prepend(self, value) -> bool:
        new_node = Node(value)

        if self.length == 0:
            self.head = self.tail = new_node
        else:
            prev_head = self.head
            new_node.next = prev_head
            prev_head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self) -> Node|None:
        if self.length == 0:
            return None

        prev_head = self.head
        if self.length == 1:
            self.head = self.tail = None        
        else:
            new_head = prev_head.next
            new_head.prev = None
            self.head = new_head

        self.length -= 1

        prev_head.next = None
        return prev_head
