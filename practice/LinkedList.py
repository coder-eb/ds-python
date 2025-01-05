from practice.Nodes import ForwardNode as Node
from practice.BaseLinkedList import BaseLinkedList

class LinkedList(BaseLinkedList):
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

    def find_middle_node(self):
        fast = slow = self.head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_loop(self):
        fast = slow = self.head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
    
    def find_kth_from_end(self, k):
        fast = slow = self.head
        for iter in range(k):
            if fast is None:
                return None
                        
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        return slow

    def remove_duplicates(self):
        seen = set()

        prev_node = None
        curr_node = self.head
        while curr_node:
            if curr_node.value not in seen:
                seen.add(curr_node.value)
                prev_node = curr_node
                curr_node = curr_node.next
                continue
            else:
                next_node = curr_node.next
                while next_node and next_node in seen:
                    next_node = next_node.next
                    self.length -= 1
                prev_node.next = next_node
                curr_node = prev_node.next
                self.length -= 1
    
    def binary_to_decimal(self):
        decimal = 0

        curr_node = self.head
        for index in range(self.length):
            binary = curr_node.value
            power = self.length - index - 1
            converted_value = binary * ( 2 ** power )
            decimal += converted_value

            curr_node = curr_node.next
        return decimal

    def partition_list(self, x):
        if self.head is None:
            return

        # Two nodes to hold values below and above x
        small_head = Node(0)
        large_head = Node(0)
        small_tail = small_head
        large_tail = large_head

        curr_node = self.head
        while curr_node:
            curr_value = curr_node.value
            if curr_value < x:
                small_tail.next = curr_node
                small_tail = curr_node
            else:
                large_tail.next = curr_node
                large_tail = curr_node

            # Keep traversing
            curr_node = curr_node.next

        large_tail.next = None
        small_tail.next = large_head.next
        self.head = small_head.next

    def reverse_between(self, start_index, end_index):
        if self.head is None or self.length == 1:
            return 

        dummy_node = Node(None)
        dummy_node.next = self.head
        previous_node = dummy_node

        for i in range(start_index):
            previous_node = previous_node.next

        current_node = previous_node.next
        for i in range(end_index-start_index):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move
            
        self.head = dummy_node.next

    def reverse_between_1(self, start_index, end_index):
        if self.head is None or self.length == 1:
            return 

        before_start = None
        start = self.head
        index = 0
        while index < start_index:
            before_start = start
            start = start.next
            index += 1
        
        before = before_start
        current = start
        while index <= end_index:
            after = current.next
            current.next = before
            before = current
            current = after
            index += 1

        start.next = after
        if before_start is None:
            self.head = before
        else:
            before_start.next = before