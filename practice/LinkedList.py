from practice.Nodes import ForwardNode as Node

class LinkedList:
    def __init__(self) -> None:
        self.head = self.tail = None
        self.length = 0

    def append(self, value) -> bool:
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def get(self, index) -> Node|None:
        if index < 0 or index >= self.length:
            return None
        
        curr_node = self.head
        for iter in range(index):
            curr_node = curr_node.next
        return curr_node

    def pop(self) -> Node|None:
        if self.length == 0:
            return None

        prev_tail = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            last_index = self.length - 1
            new_tail = self.get(last_index-1)
            new_tail.next = None
            self.tail = new_tail

        self.length -= 1
        return prev_tail

    def prepend(self, value) -> bool:
        new_head = Node(value)
        prev_head = self.head
        if self.length == 0:
            self.head = self.tail = new_head
        else:
            new_head.next = prev_head
            self.head = new_head

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
            self.head = new_head

        self.length -= 1
        return prev_head
    
    def set_value(self, index, value):
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
        
        prev_node = self.get(index-1)
        next_node = prev_node.next

        new_node = Node(value)
        new_node.next = next_node
        prev_node.next = new_node

        self.length += 1
        return True

    def remove(self, index) -> Node|None:
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        prev_node = self.get(index-1)
        target_node = prev_node.next
        next_node = target_node.next
        prev_node.next = next_node

        self.length -= 1
        return target_node

    def reverse(self) -> None:
        # initialize variables
        before = None
        current = self.head
        while current:
            # reverse next node 
            after = current.next
            current.next = before

            # next iteration
            before = current
            current = after
        
        self.head, self.tail = self.tail, self.head

    def __str__(self):
        builder = ""

        curr_node = self.head
        while curr_node:
            builder += f"{curr_node.value} => "
            curr_node = curr_node.next

        return f"\n(HEAD) {builder}END\n"