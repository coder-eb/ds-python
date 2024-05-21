from DS.BinarySearchTree import BinarySearchTree
from DS.LinkedList import LinkedList
from DS.Stack import Stack
from DS.Queue import Queue
from DS.DoublyLinkedList import DoublyLinkedList

def find_kth_from_end(ll: LinkedList, k):
    slow = fast = ll.head
    for iter in range(k):
        if fast == None:
            return None
        fast = fast.next
    
    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow

def main():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(20)
    bst.insert(5)
    bst.insert(15)
    print(bst.contains(15))
     
if __name__ == "__main__":
    main()