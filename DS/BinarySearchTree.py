from DS.Nodes import TreeNode as Node

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node: Node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        
        curr_node: Node = self.root
        while curr_node:
            # BST can't contain duplicates
            if new_node.value == curr_node.value:
                return False
            
            # Lesser value nodes should be placed to the left
            if new_node.value < curr_node.value:
                if curr_node.left is None:
                    curr_node.left = new_node
                    return True
                else:
                    curr_node = curr_node.left
            # Larger value nodes should be placed to the right
            else:
                if curr_node.right is None:
                    curr_node.right = new_node
                    return True
                else:
                    curr_node = curr_node.right