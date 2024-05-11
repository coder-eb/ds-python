from DS.Nodes import TwoWayNode as Node

class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = self.tail = new_node
        self.length = 1

    def append(self, value) -> None:
        new_node = Node(value)

        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1 

        return True    

    def pop(self) -> Node:
        if self.length == 0:
            return None

        prev_tail = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = prev_tail.prev
            self.tail.next = None
        self.length -= 1

        return prev_tail
    
    def prepend(self, value) -> None:
        new_node = Node(value)

        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

        return True

    def pop_first(self) -> Node:
        if self.length == 0:
            return None
            
        prev_head = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1 
        
        return prev_head
    
    def get(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
        
        current_node = self.head
        for iter in range(index):
            current_node = current_node.next
        
        return current_node

    def set_value(self, index, value) -> bool:
        target_node = self.get(index)
        if not target_node:
            return False
        
        target_node.value = value
        return True

    def insert(self, index, value) -> bool:
        # Insert at first position  
        if index == 0:
            return self.prepend(value)
        # Insert at last position
        if index == self.length:
            return self.append(value)

        prev_node = self.get(index-1)
        # Invalid index
        if not prev_node: 
            return False

        new_node = Node(value)
        next_node : Node = prev_node.next
        new_node.next = next_node 
        new_node.prev = prev_node
        prev_node.next = new_node
        next_node.prev = new_node
        
        return True
    
    def remove(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        target_node = self.get(index)
        prev_node : Node = target_node.prev 
        next_node : Node = target_node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        return target_node 

    def reverse(self) -> None:
        current = self.head
        while current is not None:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def is_palindrome(self) -> bool:
        if self.length <= 1:
            return True
        
        forward = self.head
        backward = self.tail

        for iter in range(self.length // 2):
            if forward.value != backward.value:
                return False
            forward = forward.next
            backward = backward.prev
        return True

    def __str__(self) -> str:
        if self.length == 0:
            return "EMPTY"
        
        items_str = "HEAD"
        current_node = self.head
        while current_node:
            items_str += " => "
            value = current_node.value
            items_str += f"{value}"
            current_node = current_node.next

        return items_str