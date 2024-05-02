class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return f"The current node is: {self.value}"
    
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

    def get_penultimate_node(self) -> Node:
        current_node = self.head 
        next_node = self.head.next 
        while next_node.next:
            current_node = current_node.next
            next_node = next_node.next 
        return current_node
    
    def pop(self) -> Node:
        prev_tail = self.tail

        if self.length == 0:
            return None
        
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.get_penultimate_node()
            self.tail.next = None
        
        self.length-=1
        return prev_tail

    def prepend(self, value) -> bool:
        new_node = Node(value)

        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length+=1
        return True            

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


def main():
    linked_list = LinkedList(5)
    print(linked_list.pop())
    # linked_list.append(10)
    # linked_list.prepend(11)
    linked_list.prepend(8)
    linked_list.prepend(6)
    # print(linked_list.pop())
    linked_list.print_list()

if __name__ == '__main__':
    main()