from DS.Nodes import TreeNode as Node
from helpers import timeit

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
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
            
        return current_node
    
    def delete_node(self, value):
        return self.__delete_node(self.root, value)

    def min_value(self, current_node: Node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
     
    def r_insert(self, value):
        # if self.root is None:
        #     self.root = Node(value)
        self.root = self.__r_insert(self.root, value)
    
    def __sorted_list_to_bst(self, nums, left, right):
        if left > right:
            return None
            
        middle = (left + right) // 2
        current = Node(nums[middle])
        
        current.left = self.__sorted_list_to_bst(nums, left, middle - 1)
        current.right = self.__sorted_list_to_bst(nums, middle + 1, right)
        
        return current
    
    def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)
    
    def __invert_tree(self, current_node: Node|None):
        if current_node == None:
            return None
        
        """ 
        Method 1:
        
        temp_left = self.__invert_tree(current_node.right)
        current_node.right = self.__invert_tree(current_node.left)
        current_node.left = temp_left
        """
        
        # Method 2:
        current_node.left, current_node.right = self.__invert_tree(current_node.right), self.__invert_tree(current_node.left)

        return current_node

    def invert_tree(self):
        self.root = self.__invert_tree(self.root)
        return self.root
    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def BFS(self):
        results = []

        queue = [self.root]
        while len(queue) > 0:
            current_node: Node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def DFS_preorder(self):
        results = []

        def traverse(current_node: Node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
                
        traverse(self.root)
        return results




def populate_slow_bst(bst: BinarySearchTree, length):
    for number in range(0, length + 1):
        bst.insert(number)

def populate_fast_bst(bst: BinarySearchTree, length):
    numbers = list(range(0, length + 1))
    bst.sorted_list_to_bst(numbers)

@timeit
def check_bst_performance(bst: BinarySearchTree, value):
    is_exists = bst.contains(value)
    print(f"BST contains value: {value} - {is_exists}")

def test_balanced_bst():
    slow_bst = BinarySearchTree()
    fast_bst = BinarySearchTree()
    NO_OF_ELEMENTS = 90_000

    populate_slow_bst(slow_bst, NO_OF_ELEMENTS)
    populate_slow_bst(fast_bst, NO_OF_ELEMENTS)

    check_bst_performance(slow_bst, 1_00_000)
    check_bst_performance(fast_bst, 1_00_000)

def test_invert_tree():
    bst = BinarySearchTree()
    nums = [1, 2, 3]
    bst.sorted_list_to_bst(nums)
    bst.invert_tree()
    print()