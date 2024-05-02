from DS.Node import Node

class LinkedList:
    def __init__(self, value) -> None:
        self.head = self.tail = None
        self.length = 0
        self.append(value)

    def append(self, value) -> bool:
        prev_head = self.head
        prev_tail = self.tail
        new_tail = Node(value)

        if prev_head is None:
            self.head = self.tail = new_tail
        else:
            prev_tail.next = new_tail
            self.tail = new_tail
        self.length+=1 
        
        return True

    def set_value(self, index, value):
        target_node = self.get(index)
        if not target_node: 
            return False

        target_node.value = value 
        return True
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        # Adds to beginning
        if index == 0:
            self.prepend(value)
            return True
        # Adds to last
        if index == self.length:
            self.append(value)
            return True
        
        new_node = Node(value)
        prev_node = self.get(index-1)
        new_node.next = prev_node.next
        prev_node.next = new_node 
        self.length+=1
        return True

    def remove(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        prev_node = self.get(index-1)
        target_node : Node = prev_node.next
        prev_node.next = target_node.next
        self.length-=1
        return target_node

    def get(self, index) -> Node:
        # Handles invalid index
        if index < 0 or index >= self.length:
            return None
        
        current_node = self.head
        for iter in range(0, index):
            current_node = current_node.next
        return current_node
    
    def pop(self) -> Node:
        prev_tail = self.tail

        if self.length == 0:
            return None
        
        if self.length == 1:
            self.head = self.tail = None
        else:
            penultimate_node_index = self.length-2
            self.tail = self.get(penultimate_node_index)
            self.tail.next = None
        
        self.length-=1
        return prev_tail

    def pop_first(self) -> Node:
        if self.length == 0:
            return None
        
        prev_head = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            # Moves head a step forward
            self.head = self.head.next
        self.length-=1

        return prev_head

    def prepend(self, value) -> bool:
        new_node = Node(value)

        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length+=1
        return True            

    def reverse(self) -> None:
        prev_head = self.head
        self.head = self.tail
        self.tail = prev_head

        before = None
        current = self.tail
        after = self.tail
        for iter in range(self.length):
            after = after.next
            current.next = before
            before = current
            current = after

    def __str__(self) -> str:
        if self.length == 0:
            return "EMPTY"
        
        linked_list_str = "HEAD"

        current_node = self.head
        while current_node:
            linked_list_str += " => "
            value = current_node.value
            linked_list_str += f"{value}"
            current_node = current_node.next

        return linked_list_str

    def print_list(self):
        print(self.__str__())
