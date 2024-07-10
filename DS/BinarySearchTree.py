from DS.Nodes import TreeNode as Node

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value) -> bool:
        new_node: Node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        
        curr_node: Node|None = self.root
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

    def __r_contains(self, node: Node|None, value):
        if node == None:
            return False
        if node.value == value:
            return True 
        if value > node.value:
            return self.__r_contains(node.right, value)
        if value < node.value:
            return self.__r_contains(node.left, value)

    def __r_insert(self, curr_node: Node|None, value):
        if curr_node is None:
            return Node(value)
        if value < curr_node.value:
            curr_node.left = self.__r_insert(curr_node.left, value)
        if value > curr_node.value:
            curr_node.right = self.__r_insert(curr_node.right, value)
        return curr_node

    def __delete_node(self, current_node: Node|None, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                return current_node.right
            elif current_node.right == None:
                return current_node.left
            else:
                pass #TODO
            
        return current_node
    
    def delete_node(self, value):
        return self.__delete_node(self.root, value)
    
    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        return self.__r_insert(self.root, value)
     
    def r_contains(self, value):
        return self.__r_contains(self.root, value)