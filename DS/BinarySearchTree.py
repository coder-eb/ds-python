from DS.Nodes import TreeNode as Node

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value) -> bool:
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
        return False
    
    def contains(self, value) -> bool:
        curr_node: Node = self.root
        while curr_node:
            if curr_node.value == value:
                return True
            
            if value < curr_node.value:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        return False

    def __r_contains(self, node: Node, value):
        if node == None:
            return False
        if node.value == value:
            return True 
        if value > node.value:
            return self.__r_contains(node.right, value)
        if value < node.value:
            return self.__r_contains(node.left, value)
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)