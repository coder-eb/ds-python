from sortedcontainers import SortedList

class MonotonicQueue:
    def __init__(self):
        self.maxq = []

    def max(self):
        if len(self.maxq) == 0:
            return None
        return self.maxq[0]

    def push(self, n: int):
        while len(self.maxq) > 0 and self.maxq[-1] < n:
            self.maxq.pop()

        self.maxq.append(n)

    def pop(self, n: int) -> int:
        if len(self.maxq) == 0:
            return None
        
        if self.maxq[0] == n:
            self.maxq.pop(0)

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end_of_word = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr_node = self.root
        for letter in word:
            position = ord(letter)-ord('a')
            if not curr_node.children[position]:
                curr_node.children[position] = TrieNode()
            
            curr_node = curr_node.children[position]
        curr_node.end_of_word = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for letter in word:
            position = ord(letter)-ord('a')
            if not curr_node.children[position]:
                return False
            
            curr_node = curr_node.children[position]
        return curr_node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for letter in prefix:
            position = ord(letter)-ord('a')
            if not curr_node.children[position]:
                return False
            
            curr_node = curr_node.children[position]
        return True

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.min_stack) > 0:
            val = min(val, self.min_stack[-1])
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

class DDNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None 

    def __str__(self) -> str:
        return f"{self.val}"
    
class DoublyLinkedList:
    def __init__(self):
        self.head=DDNode()
        self.tail=DDNode()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def __str__(self):
        dd_struct = "HEAD -> "
        curr_node = self.head
        
        while curr_node.next:
            dd_struct += f"{curr_node.val} -> "
            curr_node = curr_node.next
        dd_struct += "TAIL"

        return dd_struct
    
    def append(self, val) -> DDNode:
        new_node = DDNode(val)
        new_node.next = self.tail
        new_node.prev = self.tail.prev

        self.tail.prev.next = new_node
        self.tail.prev = new_node

        return new_node
    
    @staticmethod
    def remove_node(node: DDNode):
        node.prev.next, node.next.prev = node.next, node.prev

    def pop(self):
        node: DDNode = self.tail.prev 
        node.prev.next, node.next.prev = node.next, node.prev
        return node
    
    def peek(self):
        return self.tail.prev.val
    
class MaxStack1:
    def __init__(self):
        self.stack = DoublyLinkedList()
        self.sorted_nodes = SortedList(key=lambda x: x.val)

    def push(self, x):
        node = self.stack.append(x)
        self.sorted_nodes.add(node)

    def pop(self):
        node = self.stack.pop()
        self.sorted_nodes.remove(node)
        return node.val

    def top(self):
        return self.stack.peek()

    def peekMax(self):
        return self.sorted_nodes[-1].val

    def popMax(self):
        node = self.sorted_nodes.pop()
        DoublyLinkedList.remove_node(node)
        return node.val

class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, x):
        max_value = x if not self.max_stack else max(self.max_stack[-1], x)

        self.stack.append(x)
        self.max_stack.append(max_value)
        
    """
    @return: An integer
    """
    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()

    """
    @return: An integer
    """
    def top(self):
        return self.stack[-1]

    """
    @return: An integer
    """
    def peekMax(self):
        return self.max_stack[-1]

    """
    @return: An integer
    """
    def popMax(self):
        max_val = self.peekMax()
        buffer_stack = []

        while self.stack and self.stack[-1] != max_val:
            buffer_stack.append(self.pop())
        self.pop()

        while buffer_stack:
            self.push(buffer_stack.pop())
        
        return max_val

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked(lst):
    dummy = ListNode()
    curr = dummy
    for v in lst:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def linked_to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, val):
        self.root = TreeNode(val)

    def __r_insert(self, cur_node, val):
        if cur_node is None:
            return TreeNode(val)
        
        if val ==  cur_node.val:
            return cur_node

        if val < cur_node.val:
            cur_node.left = self.__r_insert(cur_node.left,val)
        else:
            cur_node.right = self.__r_insert(cur_node.right, val)
        return cur_node
  
    def insert(self, val):
        return self.__r_insert(self.root, val)

    def __invert_tree(self, cur_node):
        if cur_node is None:
            return None
        
        left = self.__invert_tree(cur_node.right)
        right = self.__invert_tree(cur_node.left)
        cur_node.left = left
        cur_node.right = right
        return cur_node
    
    def invertTree(self, root):
        return self.__invert_tree(root)


def main():
    bt = BinaryTree(4)
    bt.insert(2)
    bt.insert(7)
    bt.insert(7)
    bt.insert(1)
    bt.insert(3)
    bt.insert(6)
    bt.insert(9)
    bt.insert(5)
    bt.invertTree(bt.root)
    print(bt)

if __name__ == '__main__':
    main()
