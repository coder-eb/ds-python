class BaseLinkedList:
    def __init__(self):
        pass

    def __str__(self):
        builder = ""

        curr_node = self.head
        while curr_node:
            builder += f"{curr_node.value} => "
            curr_node = curr_node.next

        return f"\n(HEAD) {builder}END\n"