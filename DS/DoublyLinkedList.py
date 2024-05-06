from DS.Nodes import TwoWayNode as Node

class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = self.tail = new_node
        self.length = 1

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