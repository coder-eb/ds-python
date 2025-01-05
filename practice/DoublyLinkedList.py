from practice.Nodes import TwoWayNode as Node 
from practice.BaseLinkedList import BaseLinkedList

class DoublyLinkedList(BaseLinkedList):
    def __init__(self, value):
        self.head = self.tail = Node(value)
        self.length = 1
    
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

    def get(self, index) -> Node|None:
        if index < 0 or index >= self.length:
            return None
        
        if index < self.length // 2:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for i in range(self.length - index - 1):
                current_node = current_node.prev

        return current_node
    
    def set_value(self, index, value) -> bool:
        target_node = self.get(index)
        if target_node is None:
            return False
        
        target_node.value = value
        return True

    def insert(self, index, value) -> bool:
        if index < 0 or index > self.length:
            return False 
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value) 
        prev_node = self.get(index-1)
        next_node = prev_node.next

        new_node.prev = prev_node
        new_node.next = next_node

        prev_node.next = new_node
        next_node.prev = new_node

        self.length += 1
        return True

    def remove(self, index) -> Node|None:
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        target_node = self.get(index)
        prev_node = target_node.prev
        next_node = target_node.next

        prev_node.next = next_node
        next_node.prev = prev_node
        target_node.prev = target_node.next = None

        self.length -= 1
        return target_node